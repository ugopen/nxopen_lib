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
    /// This example will create EX_Curve_CreateArc.prt, EX_Curve_CreateArc.log files 
    /// and creates an Arc using theUfSession.Curve.CreateArc()method.
    /// The program prints the report to the log file called "EX_Curve_CreateArc.log".
    public class EX_Curve_CreateArc
    {
        private static FileStream fs; 
        private static StreamWriter w;
        private static UFSession theUfSession;
        private static Session theSession;

        public int Execute()
        {
            Tag UFPart;
            string part_name = "EX_Curve_CreateArc";
            int units =2; 
            string name;
          
            theUfSession.Part.New(part_name, units, out UFPart);
            theUfSession.Part.AskPartName(UFPart, out name);
            w.WriteLine("Loaded: " + name);
            
            Tag arc, wcs;
            UFCurve.Arc arc_coords = new UFCurve.Arc();     
            
            /* Fill out the data structure */
            arc_coords.start_angle = 0.0;
            arc_coords.end_angle = 3.0;
            arc_coords.arc_center=new double[3];
            arc_coords.arc_center[0] = 0.0;
            arc_coords.arc_center[1] = 0.0;
            arc_coords.arc_center[2] = 1.0;
            arc_coords.radius = 2.0;
            
            theUfSession.Csys.AskWcs(out wcs);
            theUfSession.Csys.AskMatrixOfObject(wcs,out arc_coords.matrix_tag);
            theUfSession.Curve.CreateArc(ref arc_coords,out arc);
            theUfSession.Part.Save();
            return 0;
        }
        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Curve_CreateArc.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Curve_CreateArc.prt") ) 
            {
                w.WriteLine("Remove EX_Curve_CreateArc.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Curve_CreateArc.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Curve_CreateArc curveTest1 = new EX_Curve_CreateArc();
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
