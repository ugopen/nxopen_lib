/*
==============================================================================
 
        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved

==============================================================================

 Description
    This file contains some utility methods for importing a simulation setup.


==============================================================================*/
using NXOpen;
using NXOpen.Assemblies;
using System;
using System.Collections.Generic;
using System.IO;

namespace CAMSetupImport
{
    class Utils
    {
        static Dictionary<string, GeometryImporter> importerMap = new Dictionary<string, GeometryImporter>()
        {
            [".stl"] = new StlGeometryImporter(),
            [".igs"] = new IGESGeometryImporter(),
            [".iges"] = new IGESGeometryImporter(),
            [".stp"] = new StepGeometryImporter(),
            [".step"] = new StepGeometryImporter()
        };

        // Adds a component to the current workPart
        public static Component AddComponent(string path)
        {

            Session theSession = Session.GetSession();
            Part workPart = theSession.Parts.Work;
            PartLoadStatus partLoadStatus1 = null;

            String fileExtension = Path.GetExtension(path);
            Part part = null;
            if (importerMap.ContainsKey(fileExtension))
            {
                GeometryImporter importer = importerMap[fileExtension];
                part = importer.Import(path);
            }
            else
            {
                try
                {
                    part = (Part)theSession.Parts.OpenBase(path, out partLoadStatus1);
                    partLoadStatus1.Dispose();
                }
                catch (NXException ex)
                {
                    // File already exists
                    if(ex.ErrorCode == 1020004)
                    {
                        part = (Part)theSession.Parts.FindObject(path);
                    }
                }
            }

            if (part == null)
            {
                MessageUtils.ShowError(path + " could not be opened");
                return null;
            }

            string referenceSet = "None";
            string componentName = Path.GetFileNameWithoutExtension(path);
            int layer = -1;

            NXOpen.Assemblies.Component component1;
            NXOpen.Assemblies.AddComponentBuilder addComponentBuilder1;
            addComponentBuilder1 = workPart.AssemblyManager.CreateAddComponentBuilder();

            addComponentBuilder1.SetCount(1);
            addComponentBuilder1.SetScatterOption(true);
            addComponentBuilder1.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.DisplayedPartWCS);
            addComponentBuilder1.ReferenceSet = referenceSet;
            addComponentBuilder1.Layer = layer;

            Part[] partstouse1 = new Part[1];
            partstouse1[0] = part;
            addComponentBuilder1.SetPartsToAdd(partstouse1);

            addComponentBuilder1.ComponentName = componentName;
            try
            {
                component1 = (NXOpen.Assemblies.Component)addComponentBuilder1.Commit();
            }
            catch(NXException)
            {
                MessageUtils.ShowError(path + " could not be added as a component.");
                return null;
            }

            addComponentBuilder1.Destroy();
            theSession.CleanUpFacetedFacesAndEdges();
            
            return component1;
        }

        public static Part CreateNewCAMSetupPart()
        {
            String tmpFileName = Path.GetTempPath() + "nx_" + DateTime.Now.Ticks + ".prt";

            Session theSession = Session.GetSession();

            FileNew fileNew = theSession.Parts.FileNew();
            fileNew.TemplateFileName = "'Blank";
            fileNew.UseBlankTemplate = true;
            fileNew.ApplicationName = "CamTemplate";
            fileNew.Units = Part.Units.Millimeters;
            fileNew.UsesMasterModel = "No";
            fileNew.SetCanCreateAltrep(false);
            fileNew.NewFileName = tmpFileName;
            fileNew.MakeDisplayedPart = true;
            NXObject obj = fileNew.Commit();

            fileNew.Destroy();
            var part = (Part)obj;

            bool result = theSession.IsCamSessionInitialized();
            if (!result)
                theSession.CreateCamSession();
            part.CreateCamSetup("mill_planar");
            part.CreateKinematicConfigurator();
            theSession.ApplicationSwitchImmediate("UG_APP_MANUFACTURING");
            return part;
        }

        public static void SetWorkPart(Part part)
        {
            Session theSession = Session.GetSession();
            PartLoadStatus partLoadStatus1;
            PartCollection.SdpsStatus status1;
            status1 = theSession.Parts.SetDisplay(part, false, true, out partLoadStatus1);
            partLoadStatus1.Dispose();
            bool result = theSession.IsCamSessionInitialized();
            theSession.ApplicationSwitchImmediate("UG_APP_MANUFACTURING");
        }
    }
}
