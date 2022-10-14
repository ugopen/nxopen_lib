/*
==============================================================================
 
        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved

==============================================================================

 Description
    This file contains classes to import geometry files into the current work part


==============================================================================*/

using NXOpen;
using System;
using System.Collections.Generic;
using System.IO;

namespace CAMSetupImport
{
    abstract class GeometryImporter
    {
        static Dictionary<string, string> s_importedParts = new Dictionary<string, string>();

        public Part Import(String path)
        {
            Session theSession = Session.GetSession();
            Part previousWorkPart = theSession.Parts.Work;

            if (s_importedParts.ContainsKey(path))
            {
                try
                {
                    return (Part)theSession.Parts.FindObject(s_importedParts[path]);
                }
                catch (NXException)
                {
                    // User closed the file in the meantime
                    s_importedParts.Remove(path);
                }
            }

            String directory = Path.GetDirectoryName(path);
            String fileName = Path.GetFileName(path).Replace('.', '_') + ".prt";
            String newFilePath = Path.Combine(directory, fileName);
            Part createdPart = null;
            try
            {
                createdPart = DoImport(newFilePath, path);
                s_importedParts.Add(path, newFilePath);
            }
            catch (NXException ex)
            {
                if (ex.ErrorCode == 1020004)
                    createdPart = (Part)theSession.Parts.FindObject(newFilePath);
            }

            Utils.SetWorkPart(previousWorkPart);
            return createdPart;
        }

        abstract protected Part DoImport(String outputPath, String inputPath);

    }

    abstract class TwoStepGeometryImporter : GeometryImporter
    {
        override
        protected Part DoImport(String outputPath, String inputPath)
        {
            Session theSession = Session.GetSession();

            FileNew fileNew1;
            fileNew1 = theSession.Parts.FileNew();
            fileNew1.TemplateFileName = "model-plain-1-mm-template.prt";
            fileNew1.ApplicationName = "ModelTemplate";
            fileNew1.Units = Part.Units.Millimeters;
            fileNew1.UsesMasterModel = "No";
            fileNew1.TemplatePresentationName = "Model";
            fileNew1.SetCanCreateAltrep(false);
            fileNew1.NewFileName = outputPath;
            fileNew1.MakeDisplayedPart = true;
            Part newPart = (Part)fileNew1.Commit();
            fileNew1.Destroy();
            theSession.ApplicationSwitchImmediate("UG_APP_MODELING");

            DoImport(newPart, inputPath);

            return newPart;
        }

        abstract protected void DoImport(Part workPart, String path);
    }

    class StlGeometryImporter : TwoStepGeometryImporter
    {
        override
        protected void DoImport(Part workPart, String path)
        {
            NXOpen.Facet.STLImportBuilder sTLImportBuilder1;
            sTLImportBuilder1 = workPart.FacetedBodies.CreateSTLImportBuilder();
            sTLImportBuilder1.File = path;
            sTLImportBuilder1.Commit();
            sTLImportBuilder1.Destroy();
        }
    }

    class IGESGeometryImporter : TwoStepGeometryImporter
    {
        override
        protected void DoImport(Part workPart, String path)
        {
            Session theSession = Session.GetSession();

            NXOpen.IgesImporter igesImporter1;
            igesImporter1 = theSession.DexManager.CreateIgesImporter();
            igesImporter1.CopiousData = NXOpen.IgesImporter.CopiousDataEnum.LinearNURBSpline;
            igesImporter1.SmoothBSurf = true;
            igesImporter1.LayerDefault = 1;
            igesImporter1.GeomFixupTol = 0.012699999999999999;
            igesImporter1.ImportTo = IgesImporter.ImportToEnum.WorkPart;
            igesImporter1.SettingsFile = NXOpen.Session.GetSession().GetEnvironmentVariableValue("IGES_DIR") + "\\igesimport.def";
            igesImporter1.InputFile = path;
            igesImporter1.OutputFile = workPart.FullPath;
            igesImporter1.LayerMask = "0-99999";
            igesImporter1.Commit();
            igesImporter1.Destroy();
        }
    }

    class StepGeometryImporter : TwoStepGeometryImporter
    {
        override
        protected void DoImport(Part workPart, String path)
        {
            Session theSession = Session.GetSession();

            NXOpen.Step214Importer step214Importer1;
            step214Importer1 = theSession.DexManager.CreateStep214Importer();
            step214Importer1.SimplifyGeometry = true;
            step214Importer1.LayerDefault = 1;
            step214Importer1.ObjectTypes.Curves = true;
            step214Importer1.ObjectTypes.Surfaces = true;
            step214Importer1.ObjectTypes.Solids = true;
            step214Importer1.ObjectTypes.PmiData = true;
            step214Importer1.SettingsFile = NXOpen.Session.GetSession().GetEnvironmentVariableValue("STEP214UG_DIR") + "\\step214ug.def";
            step214Importer1.InputFile = path;
            step214Importer1.OutputFile = workPart.FullPath;
            step214Importer1.FileOpenFlag = false;
            step214Importer1.Commit();
            step214Importer1.Destroy();
        }
    }
}
