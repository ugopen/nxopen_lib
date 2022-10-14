/*=============================================================================

                    Copyright (c) 2004 UGS PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description :
This sample program demostrats the interoprability between NX Open and NX Open
UF API. 

 
=============================================================================
*/
using System;
using System.IO;
using NXOpen;
using NXOpen.Utilities;
using NXOpen.UF;
//********************************************************************************
//
//Steps
//
//1. Create a new part file			using		NXOpen
//2. Query the part name 			using		NXOpen.UF
//3. Create Line					using		NXOpen
//4. Query line data				using		NXOpen.UF
//5. Create Arc						using		NXOpen.UF
//6. Query  Arc parameters			using		NXOpen
//7. Save the Part					using		NXOpen.UF
//*********************************************************************************
// How to get NX Open object from NX Open .Net Tag
//		NXOpen.Arc NxArc= (NXOpen.Arc)NXOpen.Utilities.NXObjectManager.Get(arc);
//
// How to get NX Open .Net Tag from NXOpen Object
//			NXOpen.Line line1  
//			NXOpen.Tag line_tag= line1.Tag
//*********************************************************************************

namespace NXOpenTestCase
{
    class InteropNXOpenWithUFWrap
    {
        static void Main(string[] args)
        {
            //Get the NX Open API
            Session theNXAutomationSession = Session.GetSession();
            // Get the NX Open API
            //NXOpen.UI theUI = UI.GetUI();
            //Get the UF Session using NX Open UF API
            UFSession theNXOpenNetSession = UFSession.GetUFSession();
            try
            {
                //Declartions
                string name;

                // Intilize the NX Open UF Session, This will not needed once UF 
				// will get intilized in Session. 
                //theNXOpenNetSession.UF.Initialize();

                //Create new part using NX Open UF API
                //string part_name = "CreateLine2";
                //int units =2; 
                //theNXOpenNetSession.Part.New(part_name, units, out part);

                //Create New Part file using NX Open API
                NXOpen.Part myPart= theNXAutomationSession.Parts.NewDisplay("InteropNXOpenWithUFWrap",NXOpen.Part.Units.Millimeters);
                NXOpen.Tag part=myPart.Tag;
                //Query the part name using NX Open API
                theNXOpenNetSession.Part.AskPartName(part, out name);
                
                // Create Line using NX Open APIs
                NXOpen.Point3d point3d1 = new Point3d(-2.45197396411307, 3.58206319143819, 0);
                NXOpen.Point3d point3d2 = new Point3d(5.32514590979158, -1.0012853802839, 0);
                NXOpen.Line line1 = theNXAutomationSession.Parts.Work.Curves.CreateLine(point3d1, point3d2);

                //Ask line data using NX Open UF API
                NXOpen.UF.UFCurve.Line line_coords;
                theNXOpenNetSession.Curve.AskLineData(line1.Tag,out line_coords);
			
                // Create Arc using NXOpen UF API
                NXOpen.Tag arc, wcs;
                NXOpen.UF.UFCurve.Arc arc_coords = new NXOpen.UF.UFCurve.Arc();		
		
                // Fill out the data structure 
                arc_coords.start_angle = 0.0;
                arc_coords.end_angle = 3.0;
                arc_coords.arc_center=new double[3];
                arc_coords.arc_center[0] = 0.0;
                arc_coords.arc_center[1] = 0.0;
                arc_coords.arc_center[2] = 1.0;
                arc_coords.radius = 2.0;
		
                // Create a ARC using NXOpen UF API
                theNXOpenNetSession.Csys.AskWcs(out wcs);
                theNXOpenNetSession.Csys.AskMatrixOfObject(wcs,out arc_coords.matrix_tag);
                theNXOpenNetSession.Curve.CreateArc(ref arc_coords,out arc);

                // Create NX Open Arc Object using NXOpen UF arc Tag
                Arc NxArc= (Arc)NXOpen.Utilities.NXObjectManager.Get(arc);

                //Get the Arc parameters using NX Open APIs
                double start_angle= NxArc.StartAngle;
                double end_angle= NxArc.EndAngle;
                NXOpen.Point3d arc_center=NxArc.CenterPoint;

                // Save the Part using NXOpen UF API
                theNXOpenNetSession.Part.Save();
             }
            catch(NXException e)
            {	
                Console.WriteLine("Exception is: {0}", e.Message);
            }
        }
    }
}


