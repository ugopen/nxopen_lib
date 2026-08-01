/*=============================================================================

                    Copyright (c) 2004 UGS PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: Example for Wrapped UFUNC (NXOpen.NET)
/*  */
using System;
using System.IO;
using NXOpen;
using NXOpen.UF;

namespace NetExample
{
    /// This example will create EX_Curve_CreateFillet.prt, EX_Curve_CreateFillet.log files 
    /// and creates fillet between Line and Arc using theUfSession.Curve.CreateFillet()    method.
    /// The program prints the report to the log file called "EX_Curve_CreateFillet.log"
    public class EX_Curve_CreateFillet
    {
        private static FileStream fs; 
        private static StreamWriter w;
        private static UFSession theUfSession;
        private static Session theSession;

       
        //Constants
        public const int UF_CURVE_2_CURVE = 0;
        public const double DEGRA = .01745329251994328;
            
        public int Execute()
        {
            Tag part;
            string part_name = "EX_Curve_CreateFillet";
            int units =2; 
            string name;


            theUfSession.Part.New(part_name, units, out part);
            theUfSession.Part.AskPartName(part, out name);
            w.WriteLine("Loaded: " + name);
            
            double[] center= new double[3];
            double radius;
            int[] trim_opts = new int[3];
            int[] arc_opts={0,0,0};
            UFCurve.Line line_coords1 = new UFCurve.Line();
            line_coords1.start_point = new double[3];
            line_coords1.start_point[0] = 1.2;
            line_coords1.start_point[1] = 0.2;
            line_coords1.start_point[2] = 0.0;
            line_coords1.end_point = new double[3];
            line_coords1.end_point[0] = -0.5;
            line_coords1.end_point[1] = 2.5;
            line_coords1.end_point[2] = 0.0;
            
            UFCurve.Line line_coords2 = new UFCurve.Line();
            line_coords2.start_point = new double[3];
            line_coords2.start_point[0] = 3.2;
            line_coords2.start_point[1] = 2.25;
            line_coords2.start_point[2] = 0.0;
            line_coords2.end_point = new double[3];
            line_coords2.end_point[0] = 2.5;
            line_coords2.end_point[1] = 3.5;
            line_coords2.end_point[2] = 0.0;
            
            UFCurve.Arc arc_coords1 = new UFCurve.Arc();        
            arc_coords1.matrix_tag = Tag.Null;
            arc_coords1.start_angle =238*DEGRA ;
            arc_coords1.end_angle = 357*DEGRA;
            arc_coords1.arc_center=new double[3];
            arc_coords1.arc_center[0] = 0.22;
            arc_coords1.arc_center[1] = 4.3;
            arc_coords1.arc_center[2] = 0.0;
            arc_coords1.radius = 2.0;

            UFCurve.Arc arc_coords2 = new UFCurve.Arc();        
            arc_coords2.matrix_tag = Tag.Null;
            arc_coords2.start_angle = 82*DEGRA ;
            arc_coords2.end_angle = 175*DEGRA;
            arc_coords2.arc_center=new double[3];
            arc_coords2.arc_center[0] = 3.0;
            arc_coords2.arc_center[1] = 0.43;
            arc_coords2.arc_center[2] = 0.0;
            arc_coords2.radius = 2.0;
            
            Tag line1,line2,arc1,arc2;
            Tag[] curve_objs= new Tag[3];
            Tag fillet_obj1,fillet_obj2, wcs_tag, matrix_tag;

            
            /* create 2 lines */
            theUfSession.Curve.CreateLine(ref line_coords1, out line1);
            theUfSession.Curve.CreateLine(ref line_coords2, out line2);
            /* create 2 arcs */
            theUfSession.Csys.AskWcs(out wcs_tag);
            theUfSession.Csys.AskMatrixOfObject(wcs_tag, out matrix_tag);
            arc_coords1.matrix_tag=matrix_tag;
            arc_coords2.matrix_tag=matrix_tag;

            theUfSession.Curve.CreateArc(ref arc_coords1, out arc1);
            theUfSession.Curve.CreateArc(ref arc_coords2, out arc2);

            /*create fillet between "arc1" and "line1"*/
            curve_objs[0] = arc1;
            curve_objs[1] = line1;
            center[0] = 0.0;
            center[1] = 2.1;
            center[2] = 0.0;
            radius = .25;
            trim_opts[0] = 1;          /*trim first UFCurve*/
            trim_opts[1] = 1;         /*trim second UFCurve*/
            
            theUfSession.Curve.CreateFillet(UF_CURVE_2_CURVE,curve_objs,   center, radius, trim_opts,
                arc_opts, out fillet_obj1);
            /*create fillet between "line1" and "arc2"*/
            curve_objs[0] = line1;
            curve_objs[1] = arc2;
            center[0] = 0.8;
            center[1] = 1.0;
            center[2] = 0.0;
            radius = .25;
            trim_opts[0] = 1;          /*trim first UFCurve*/
            trim_opts[1] = 1;         /*trim second UFCurve*/
            
            theUfSession.Curve.CreateFillet(UF_CURVE_2_CURVE,curve_objs,   center, radius,
                trim_opts, arc_opts, out fillet_obj2);

            theUfSession.Part.Save();
            return 0;
        }
        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Curve_CreateFillet.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Curve_CreateFillet.prt") ) 
            {
                w.WriteLine("Remove EX_Curve_CreateFillet.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Curve_CreateFillet.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Curve_CreateFillet curveTest1 = new EX_Curve_CreateFillet();
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
