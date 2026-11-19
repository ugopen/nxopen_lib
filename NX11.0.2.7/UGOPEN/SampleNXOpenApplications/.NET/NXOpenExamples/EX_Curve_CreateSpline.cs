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
    /// This example will create EX_Curve_CreateSpline.prt, EX_Curve_CreateSpline.log files 
    /// and creates two planar B-curves and calculates 
    /// their inflection points    using theUfSession.Curve.AskCurveInflections().
    /// The program prints the report to the log file called "EX_Curve_CreateSpline.log".
    public class EX_Curve_CreateSpline
    {
        private static FileStream fs; 
        private static StreamWriter w;
        private static UFSession theUfSession;
        private static Session theSession;

        //Constants
        public const int UF_OBJ_NAME_LEN = 30;
            
        public int Execute()
        {
            Tag UFPart;
            string part_name = "EX_Curve_CreateSpline";
            int units =2; 
            string name;


            theUfSession.Part.New(part_name, units, out UFPart);
            theUfSession.Part.AskPartName(UFPart, out name);
            w.WriteLine("Loaded: " + name);
            
            int i, k, curve_cnt=0;
            Tag curve_array;
            char[] buf = new char[UFConstants.UF_OBJ_NAME_BUFSIZE];
            String newnam= new String(buf);
            int num_infpts;
            double[] range={0.0, 100.0};
            double[] inf_pts;
            double[] proj_matrx={ 1.0, 0.0, 0.0, 0.0, 1.0, 0.0,0.0, 0.0, 1.0};
            int    knot1_fix, knot2_fix, pole1_fix, pole2_fix;

            double[] bc1_knots = {-3.0/8.0, -2.0/8.0, -1.0/8.0, 0.0, 1.0/8.0,
                                     2.0/8.0, 3.0/8.0, 4.0/8.0, 5.0/8.0, 6.0/8.0,
                                     7.0/8.0, 1.0, 9.0/8.0, 10.0/8.0, 11.0/8};

            double[] bc1_poles = { 2.0, 0.0, 0.0, 1.0,
                                     4.0, 0.0, 0.0, 1.0,
                                     3.5, 2.0, 0.0, 1.0,
                                     6.0, 6.0, 0.0, 1.0,
                                     2.0, 3.5, 0.0, 1.0,
                                     0.0, 4.0, 0.0, 1.0,
                                     0.0, 2.0, 0.0, 1.0,
                                     0.0, 0.0, 0.0, 1.0,
                                     2.0, 0.0, 0.0, 1.0,
                                     4.0, 0.0, 0.0, 1.0,
                                     3.5, 2.0, 0.0, 1.0  };

            double[] bc2_knots = {0.0, 0.0, 0.0, 1.0/3.0,
                                     2.0/3.0, 1.0, 1.0, 1.0};

            double[] bc2_poles = {0.0, 0.0, 1.0, 1.0,
                                     1.0, 2.0, 1.0, 1.0,
                                     0.625, 0.0, 0.25, 0.25,
                                     4.0, 2.0, 1.0, 1.0,
                                     5.0, 0.0, 1.0, 1.0 };
            
            /*    create two B-curves   */
            theUfSession.Modl.CreateSpline(11,4,bc1_knots,bc1_poles,out curve_array,out knot1_fix,out pole1_fix);
            newnam = String.Copy("BCURVE_1");
            
            theUfSession.Obj.SetName(curve_array,newnam);
            curve_cnt ++;
            theUfSession.Modl.CreateSpline(5,3,bc2_knots,bc2_poles,out curve_array,out knot2_fix,out pole2_fix);
            newnam = String.Copy("BCURVE_2");
            theUfSession.Obj.SetName(curve_array, newnam);
            curve_cnt ++;
            
            /* loop over each UFCurve and compute their inflections */
            for (i = 0; i < curve_cnt; i++)
            {
                /* used a pre-definied projection matrix and predefined UFCurve's
                range for the inflection points calculation
                */
                theUfSession.Curve.AskCurveInflections(curve_array,proj_matrx,range,out num_infpts,out inf_pts);

                if (num_infpts > 0)
                {
                    w.WriteLine("There are {0} inflection points for UFCurve {1}\n",num_infpts, i+1);
                    for(k = 0; k < (num_infpts * 4); k++)
                    {
                        w.WriteLine("inf_pts[{0}] = {1}\n", k, inf_pts[k]);
                    }
                } 
            }
            theUfSession.Part.Save();
            return 0;
        }
        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Curve_CreateSpline.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Curve_CreateSpline.prt") ) 
            {
                w.WriteLine("Remove EX_Curve_CreateSpline.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Curve_CreateSpline.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Curve_CreateSpline curveTest1 = new EX_Curve_CreateSpline();
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
