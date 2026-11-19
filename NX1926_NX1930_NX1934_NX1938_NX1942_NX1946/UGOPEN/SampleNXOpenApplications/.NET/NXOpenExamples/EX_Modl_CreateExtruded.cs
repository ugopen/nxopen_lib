/*=============================================================================

                    Copyright (c) 2004 UGS PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: Example for Wrapped UFUNC (NXOpen.NET)
/*  */
using System;
using System.IO;
using System.Collections;
using NXOpen;
using NXOpen.UF;

namespace NetExample
{
    /// This example will create EX_Modl_CreateExtruded.prt, EX_Modl_CreateExtruded.log files. 
    /// This example extrudes lines and arcs along the z-axis. Three lines and two arcs are drawn. 
    /// The center line is a reference line only, and is not included in the objects to be extruded.
    /// The program prints the report to the log file called "EX_Modl_CreateExtruded.log".
    public class EX_Modl_CreateExtruded
    {
        private static FileStream fs; 
        private static StreamWriter w;
        public static UFSession theUfSession;
        private static Session theSession;


        //Constants
        public const double PI = 3.14159265358979324;

         public int Execute()
         {
             Tag UFPart;
             string part_name = "EX_Modl_CreateExtruded";
             int units =2; 
             string name;


             theUfSession.Part.New(part_name, units, out UFPart);
             theUfSession.Part.AskPartName(UFPart, out name);
             w.WriteLine("Loaded: " + name);

             double[] l1_endpt1 = {-1.4476606170268,2.3788333712953,0.0};
             double[] l1_endpt2 = { 1.5471310496399,2.2539419253757,0.0};
             double[] l2_endpt1 = {-1.4476606170268,1.2548103580189,0.0};
             double[] l2_endpt2 = { 1.5471310496399,1.3797018039385,0.0};
             double[] l3_endpt1 = {-1.4710981170268,1.8168218646571,0.0};
             double[] l3_endpt2 = { 1.5289018829732,1.8168218646571,0.0};
             double[] direction = {0.0,0.0,1.0};
             double[] ref_pt= new double[3];
             double arc1_start_ang = (PI/180)*87.611984536731;
             double arc1_end_ang   = (PI/180)*272.38801546327;
             double arc1_rad       = 0.5625;
             double arc2_start_ang = (PI/180)*272.38801546327;
             double arc2_end_ang   = (PI/180)*447.61198453673;
             double arc2_rad       = 0.4375;
             string taper_angle = "0.0";
             string[] limit1 = {"1.0", "1.25"};
             int i, count = 4;
             Tag[] objarray= new Tag[5];
             Tag wcs_tag, matrix_tag;
             Tag[] loop_list, features;
             UFCurve.Line line1 = new UFCurve.Line();
             UFCurve.Line line2 = new UFCurve.Line();
             UFCurve.Line line3 = new UFCurve.Line();
             UFCurve.Arc arc1 = new UFCurve.Arc();
             UFCurve.Arc arc2 = new UFCurve.Arc();

             line1.start_point = new double[3];
             line1.start_point[0] = l1_endpt1[0];
             line1.start_point[1] = l1_endpt1[1];
             line1.start_point[2] = l1_endpt1[2];
             line1.end_point = new double[3];
             line1.end_point[0]   = l1_endpt2[0];
             line1.end_point[1]   = l1_endpt2[1];
             line1.end_point[2]   = l1_endpt2[2];

             line2.start_point = new double[3];
             line2.start_point[0] = l2_endpt1[0];
             line2.start_point[1] = l2_endpt1[1];
             line2.start_point[2] = l2_endpt1[2];
             line2.end_point = new double[3];
             line2.end_point[0]   = l2_endpt2[0];
             line2.end_point[1]   = l2_endpt2[1];
             line2.end_point[2]   = l2_endpt2[2];
            
             line3.start_point = new double[3];
             line3.start_point[0] = l3_endpt1[0];
             line3.start_point[1] = l3_endpt1[1];
             line3.start_point[2] = l3_endpt1[2];
             line3.end_point = new double[3];
             line3.end_point[0]   = l3_endpt2[0];
             line3.end_point[1]   = l3_endpt2[1];
             line3.end_point[2]   = l3_endpt2[2];
            
             arc1.start_angle   = arc1_start_ang;
             arc1.end_angle     = arc1_end_ang;
             arc1.arc_center = new double[3];
             arc1.arc_center[0] = l3_endpt1[0];
             arc1.arc_center[1] = l3_endpt1[1];
             arc1.arc_center[2] = l3_endpt1[2];
             arc1.radius        = arc1_rad;
             arc2.start_angle   = arc2_start_ang;
             arc2.end_angle     = arc2_end_ang;
             arc2.arc_center = new double[3];
             arc2.arc_center[0] = l3_endpt2[0];
             arc2.arc_center[1] = l3_endpt2[1];
             arc2.arc_center[2] = l3_endpt2[2];
             arc2.radius        = arc2_rad;

             theUfSession.Curve.CreateLine(ref line1,out objarray[0]);
             theUfSession.Curve.CreateLine(ref line2,out objarray[1]);
             theUfSession.Curve.CreateLine(ref line3,out objarray[4]);
             theUfSession.Csys.AskWcs(out wcs_tag);
             theUfSession.Csys.AskMatrixOfObject(wcs_tag, out matrix_tag);
             arc1.matrix_tag = matrix_tag;
             arc2.matrix_tag = matrix_tag;
             theUfSession.Curve.CreateArc(ref arc1,out objarray[2]);
             theUfSession.Curve.CreateArc(ref arc2, out objarray[3]);
             //Create loop list
             ArrayList arr_loop_list = new ArrayList();
             for(i = 0; i < count; i++) 
             {
                 arr_loop_list.Add(objarray[i]);
             }
             loop_list = (Tag [])arr_loop_list.ToArray(typeof(Tag));

             // while sending parameters to this function the order was 
             // loop_list, taper_angle, limit1, ref_pt, FeatureSigns.Nullsign, direction, out features
             // as above .. there were some compilation problem due to function prototype match.
             // Atul changed the order as follows in order to compile it successfully.
             // loop_list, taper_angle, limit1, ref_pt, direction, FeatureSigns.Nullsign, out features
             theUfSession.Modl.CreateExtruded(loop_list, taper_angle, limit1,
                 ref_pt, direction, FeatureSigns.Nullsign,  out features);

             theUfSession.Part.Save();
             return 0;
        }

        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Modl_CreateExtruded.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Modl_CreateExtruded.prt") ) 
            {
                w.WriteLine("Remove EX_Modl_CreateExtruded.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Modl_CreateExtruded.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Modl_CreateExtruded curveTest1 = new EX_Modl_CreateExtruded();
                if (curveTest1.Execute()==0)
                {
                    w.WriteLine("Successful");
                }
                else
                {
                    w.WriteLine("Failed");
                }
            }
            catch(NXException e)
            {   
                w.WriteLine("Exception is: {0}", e.Message);
            }
            w.WriteLine("End of Log File");
            w.Close();
        }
        public static int GetUnloadOption(string dummy) 
        {
            return UFConstants.UF_UNLOAD_IMMEDIATELY;
        }
    }
}
