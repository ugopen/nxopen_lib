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
    /// This example will create EX_Curve_CreateSplineThruPts.prt, EX_Curve_CreateSplineThruPts.log files 
    /// and creates spline through points using theUfSession.Curve.CreateSplineThruPts(().
    /// The program prints the report to the log file called "EX_Curve_CreateSplineThruPts.log".
    public class EX_Curve_CreateSplineThruPts
    {
        private static FileStream fs; 
        private static StreamWriter w;
        private static UFSession theUfSession;
        private static Session theSession;

  
        //Constants
        public const int NUMBER_POINTS = 5;

        public const int UF_CURVE_SLOPE_NONE = -1;  /* UF_CURVE_ASK_SPLINE_THRU_PTS */
        public const int UF_CURVE_SLOPE_AUTO =  0;   /* UF_CURVE_ASK_SPLINE_THRU_PTS */
        public const int UF_CURVE_SLOPE_DIR  =  1;   /* UF_CURVE_ASK_SPLN_BY_DEF_DATA */ 
        public const int UF_CURVE_SLOPE_VEC  =  2;   /* UF_CURVE_ASK_SPLN_BY_DEF_DATA */

        public const int UF_CURVE_CRVATR_NONE = -1;  /* UF_CURVE_CREATE_SPLINE_THRU_PTS */
        public const int UF_CURVE_CRVATR_AUTO_DIR = 1;   /* UF_CURVE_CREATE_SPLINE_THRU_PTS */
        public const int UF_CURVE_CRVATR_VEC = 2;   /* UF_CURVE_CREATE_SPLINE_THRU_PTS */
    
        public int Execute()
        {
            Tag UFPart;
            string part_name = "EX_Curve_CreateSplineThruPts";
            int units =2; 
            string name;


            theUfSession.Part.New(part_name, units, out UFPart);
            theUfSession.Part.AskPartName(UFPart, out name);
            w.WriteLine("Loaded: " + name);
            
            /* B-spline parameters  */
            int degree = 3;
            int periodicity = 0;
            int num_points = NUMBER_POINTS;

            /* Point/slope UFCurve attribute array */
            UFCurve.PtSlopeCrvatr[] point_data = new UFCurve.PtSlopeCrvatr[NUMBER_POINTS];
            
            /* Arrays of user's defining point data */
            double[] parameters={0.00,  0.17,  0.32,  0.45,1.29};
            double[] points = {1.1000,  0.5320,  2.0000,
                                  1.5240,  0.6789,  2.3000,
                                  2.0000,  0.9000,  3.5956,
                                  2.3456,  1.3456,  3.7890,
                                  3.1000,  2.4567,  3.3214};
            int[] slopeTypes = { UF_CURVE_SLOPE_DIR,
                                   UF_CURVE_SLOPE_AUTO,
                                   UF_CURVE_SLOPE_NONE,
                                   UF_CURVE_SLOPE_DIR,
                                   UF_CURVE_SLOPE_VEC};
            double[] slopeVecs = {1.2300,  5.0506,  4.0360,
                                     0.0000,  0.0000,  0.0000,
                                     0.0000,  0.0000,  0.0000,
                                     0.5000,  1.0000,  0.5000,
                                     1.0000, -2.0000,  1.0000};
            int[] crvatrTypes = {UF_CURVE_CRVATR_NONE,
                                    UF_CURVE_CRVATR_AUTO_DIR,
                                    UF_CURVE_CRVATR_NONE,
                                    UF_CURVE_CRVATR_VEC,
                                    UF_CURVE_CRVATR_VEC};
            double[] crvatrVecs = {0.0000,  0.0000,  0.0000,
                                      1.0000,  2.5780,  5.6700,
                                      0.0000,  0.0000,  0.0000,
                                      1.0000,  -1.0000,  1.0000,
                                      -1.0000,  -1.0000,  -1.0000};
            int i, save_def_data = 1;

            Tag spline_tag;
            for (i= 0;   i<NUMBER_POINTS; i++)
            {
                point_data[i].point= new double[3]; 
                point_data[i].point[0] = points[3*i];
                point_data[i].point[1] = points[3*i+1];
                point_data[i].point[2] = points[3*i+2];
                point_data[i].slope_type = slopeTypes[i];
                point_data[i].slope= new double[3]; 
                point_data[i].slope[0] = slopeVecs[3*i];
                point_data[i].slope[1] = slopeVecs[3*i+1];
                point_data[i].slope[2] = slopeVecs[3*i+2];
                point_data[i].crvatr_type = crvatrTypes[i];
                point_data[i].crvatr= new double[3]; 
                point_data[i].crvatr[0] = crvatrVecs[3*i];
                point_data[i].crvatr[1] = crvatrVecs[3*i+1];
                point_data[i].crvatr[2] = crvatrVecs[3*i+2];
            }
            /* Create B-spline UFCurve */
            theUfSession.Curve.CreateSplineThruPts(degree,
                periodicity,
                num_points,
                point_data,
                parameters,
                save_def_data,
                out spline_tag);
            theUfSession.Part.Save();
            return 0;
        }
        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Curve_CreateSplineThruPts.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Curve_CreateSplineThruPts.prt") ) 
            {
                w.WriteLine("Remove EX_Curve_CreateSplineThruPts.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Curve_CreateSplineThruPts.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Curve_CreateSplineThruPts curveTest1 = new EX_Curve_CreateSplineThruPts();
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
