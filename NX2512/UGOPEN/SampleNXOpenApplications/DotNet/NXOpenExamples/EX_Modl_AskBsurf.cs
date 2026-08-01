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
    /// This example will create EX_Modl_AskBsurf.prt, EX_Modl_AskBsurf.log files 
    /// and creates B-Surface and Spline, and then queries its data. 
    /// The program prints the report to the log file called "EX_Modl_AskBsurf.log".
    public class EX_Modl_AskBsurf
    {
        private static FileStream fs; 
        private static StreamWriter w;
        public static UFSession theUfSession;
        private static Session theSession;

        //Constants
        public const double PI = 3.14159265358979324;

         public int Execute()
         {
             Tag part;
             string part_name = "EX_Modl_AskBsurf";
             int units =2; 
             string name;


             theUfSession.Part.New(part_name, units, out part);
             theUfSession.Part.AskPartName(part, out name);
             w.WriteLine("Loaded: " + name);
            
             int    knot_fixup,pole_fixup;
             Tag  bcurv1,bcurv2,bsurf;

             int[]    bsurf_idata = {4,4,4,4};
             double[] bsurf_uknot = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0};
             double[] bsurf_vknot = {0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0};
             double[] bsurf_poles = {0.0,0.0,6.0,1.0,
                                        2.0,2.0,6.0,1.0,
                                        5.0,1.5,6.0,1.0,
                                        8.0,3.0,6.0,1.0,
                                        0.0,2.0,4.0,1.0,
                                        2.0,4.0,4.0,1.0,
                                        5.0,3.5,4.0,1.0,
                                        8.0,5.0,4.0,1.0,
                                        0.0,2.0,2.0,1.0,
                                        2.0,4.0,2.0,1.0,
                                        5.0,3.5,2.0,1.0,
                                        8.0,5.0,2.0,1.0,
                                        0.0,0.0,0.0,1.0,
                                        2.0,2.0,0.0,1.0,
                                        5.0,1.5,0.0,1.0,
                                        8.0,3.0,0.0,1.0} ;
             int[]    bcurv1_idata = {3,3} ;
             double[] bcurv1_knots = {0.0,0.0,0.0,1.0,1.0,1.0};
             double[] bcurv1_poles = {-0.5,-2.5,3.5,1.0,
                                         2.5,-2.5,3.5,1.0,
                                         2.5,-2.5,6.5,1.0};

             int[]    bcurv2_idata = {8,4} ;
             double[] bcurv2_knots = {-0.6,-0.4,-0.2,0.0,0.2,
                                         0.4, 0.6, 0.8,1.0,1.2,
                                         1.4, 1.6};
             double[] bcurv2_poles = {3.0,-2.5,2.0,1.0,
                                         4.0,-2.5,1.0,1.0,
                                         7.0,-2.5,1.0,1.0,
                                         6.0,-2.5,3.0,1.0,
                                         3.0,-2.5,3.0,1.0,
                                         3.0,-2.5,2.0,1.0,
                                         4.0,-2.5,1.0,1.0,
                                         7.0,-2.5,1.0,1.0};

             //int num_gaps,discard = 0;
             double[] proj_vector = {0.0,1.0,0.0};
             double[] ptdata = {1.312,1.896,4.8,
                                   4.464,3.312,2.4};
    
             /*
             Create the b-surface.
             */
             theUfSession.Modl.CreateBsurf(bsurf_idata[0],
                 bsurf_idata[1],
                 bsurf_idata[2],
                 bsurf_idata[3],
                 bsurf_uknot,
                 bsurf_vknot,
                 bsurf_poles,
                 out bsurf,
                 out knot_fixup,
                 out pole_fixup);
             w.WriteLine("UFModl.CreateBsurf- Successful");
             UFModl.Bsurface bSurfData;
             theUfSession.Modl.AskBsurf(bsurf,out bSurfData);
             w.WriteLine("UFModl.AskBsurf- Successful");
             /*
             Create the splines.
             */
             theUfSession.Modl.CreateSpline(bcurv1_idata[0],
                 bcurv1_idata[1],
                 bcurv1_knots,
                 bcurv1_poles,
                 out bcurv1,
                 out knot_fixup,
                 out pole_fixup);
             w.WriteLine("UFModl.CreateSpline- Successful");
             theUfSession.Modl.CreateSpline(bcurv2_idata[0],
                 bcurv2_idata[1],
                 bcurv2_knots,
                 bcurv2_poles,
                 out bcurv2,
                 out knot_fixup,
                 out pole_fixup);
             w.WriteLine("UFModl.CreateSpline- Successful");
             UFCurve.Spline cSpline;
             theUfSession.Curve.AskSplineData(bcurv2,out cSpline);
             w.WriteLine("Curve.AskSplineData- Successful");
             w.WriteLine("Start Param="+cSpline.start_param);
             w.WriteLine("End Param="+cSpline.end_param);
             w.WriteLine("Is Rational="+cSpline.is_rational);
             w.WriteLine("Order="+cSpline.order);
             w.WriteLine("# of Poles="+cSpline.num_poles);
             for(int i=0;i<cSpline.poles.Length/4;i++)
             {
                 w.WriteLine("Pole["+i+",0]="+cSpline.poles[i,0]);
                 w.WriteLine("Pole["+i+",1]="+cSpline.poles[i,1]);
                 w.WriteLine("Pole["+i+",2]="+cSpline.poles[i,2]);
                 w.WriteLine("Pole["+i+",3]="+cSpline.poles[i,3]);
             }
             theUfSession.Modl.Update();
             theUfSession.Part.Save();
             

             w.WriteLine("UFPart.Save- Successful");
             return 0;
        }

        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Modl_AskBsurf.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Modl_AskBsurf.prt") ) 
            {
                w.WriteLine("Remove EX_Modl_AskBsurf.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Modl_AskBsurf.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Modl_AskBsurf curveTest1 = new EX_Modl_AskBsurf();
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
