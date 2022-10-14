/*=============================================================================

                    Copyright (c) 2008 Siemens PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: Sample NX/Open Application
===============================================================================

=============================================================================
*/


using System;
using System.IO;
using System.Runtime.Remoting;
using System.Runtime.Remoting.Channels;
using System.Text;
using System.Diagnostics;

using System.Collections;

using NXOpen;
using NXOpen.Utilities;
using NXOpen.UF;


public class NXOpenRemotingClient
{
    public static void DoLog(String s)
    {
        Session.GetSession().LogFile.WriteLine(s);
        Console.WriteLine(s);
    }

    static void Main(string[] args)
    {
        Session theSession = (Session)Activator.GetObject(typeof(Session), "http://localhost:4567/NXOpenSession");
        UFSession theUFSession = (UFSession)Activator.GetObject(typeof(UFSession), "http://localhost:4567/UFSession");

        try
        {
            DoLog("working");
            theSession.LogFile.WriteLine("\nITS WORKING\n");

            // ----------------------------------------------
            //   Menu: File->New...
            // ----------------------------------------------
            NXOpen.Session.UndoMarkId markId1;
            markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "'Start");

            NXOpen.FileNew fileNew1;
            fileNew1 = theSession.Parts.FileNew();

            theSession.SetUndoMarkName(markId1, "''New Dialog");

            NXOpen.Session.UndoMarkId markId2;
            markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "'New");

            theSession.DeleteUndoMark(markId2, null);

            NXOpen.Session.UndoMarkId markId3;
            markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "'New");

            fileNew1.TemplateFileName = "model-plain-1-mm-template.prt";

            fileNew1.UseBlankTemplate = false;

            fileNew1.ApplicationName = "ModelTemplate";

            fileNew1.Units = NXOpen.Part.Units.Millimeters;

            fileNew1.RelationType = "";

            fileNew1.UsesMasterModel = "No";

            fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item;

            fileNew1.TemplatePresentationName = "Model";

            fileNew1.ItemType = "";

            fileNew1.Specialization = "";

            fileNew1.SetCanCreateAltrep(false);

            fileNew1.NewFileName = "Remoting.prt";

            fileNew1.MasterFileName = "";

            fileNew1.MakeDisplayedPart = true;

            NXOpen.NXObject nXObject1;
            nXObject1 = fileNew1.Commit();

            NXOpen.Part workPart = theSession.Parts.Work;
            NXOpen.Part displayPart = theSession.Parts.Display;
            theSession.DeleteUndoMark(markId3, null);

            fileNew1.Destroy();

            NXOpen.Session.UndoMarkId markId4;
            markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Gateway");

            theSession.ApplicationSwitchImmediate("UG_APP_GATEWAY");

            theSession.ApplicationSwitchImmediate("UG_APP_MODELING");

            NXOpen.Session.UndoMarkId markId5;
            markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Modeling");

            // Create Line using NXOpen Jam APIs
            Point3d point3d1 = new Point3d(-2.45197396411307, 3.58206319143819, 0);
            Point3d point3d2 = new Point3d(5.32514590979158, -1.0012853802839, 0);
            Line line1 = theSession.Parts.Work.Curves.CreateLine(point3d1, point3d2);

            //Ask line data using wrapped NXOpen.UF API
            UFCurve.Line line_coords;
            theUFSession.Curve.AskLineData(line1.Tag, out line_coords);

            // Create Arc using wrapped NXOpen.UF APIs
            Tag arc, wcs;
            UFCurve.Arc arc_coords = new UFCurve.Arc();

            // Fill out the data structure
            arc_coords.start_angle = 0.0;
            arc_coords.end_angle = 3.0;
            arc_coords.arc_center = new double[3];
            arc_coords.arc_center[0] = 0.0;
            arc_coords.arc_center[1] = 0.0;
            arc_coords.arc_center[2] = 1.0;
            arc_coords.radius = 2.0;

            // Create a ARC using wrapped NXOpen.UF API
            theUFSession.Csys.AskWcs(out wcs);
            theUFSession.Csys.AskMatrixOfObject(wcs, out arc_coords.matrix_tag);
            theUFSession.Curve.CreateArc(ref arc_coords, out arc);

            // Create an NX Open Arc object from the UF arc tag using the NXObjectManager.
            // You need to get the NXObjectManager from the remote session object.
            NXObjectManager theNXOM = theSession.GetObjectManager();
            Arc theArc = (Arc)theNXOM.GetTaggedObject(arc);

            theSession.Information.DisplayObjectsDetails(new NXObject[] { theArc });
        }
        catch (NXException e)
        {
            DoLog("NX Exception is: {0} " + e.Message);
        }
        catch (Exception e)
        {
            DoLog("Exception is: {0} " + e.Message);
        }
        finally
        {
            DoLog("Done");
            theSession.LogFile.WriteLine("DONE\n");
        }

    }
}

