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
    /// This example will create EX_Drf_AskPreferences.prt, EX_Drf_AskPreferences.log files 
    /// and queries the current settings of the drafting parameters using theUfSession.Drf.AskPreferences().
    ///The program prints the report to the log file called "EX_Drf_AskPreferences.log".
    public class EX_Drf_AskPreferences
    {
        private static FileStream fs; 
        private static StreamWriter w;
        private static UFSession theUfSession;
        private static Session theSession;

        //Constants
        //  public const int UF_cylinder_type = 16;

        public int Execute()
        {
            Tag UFPart;
            string part_name = "EX_Drf_AskPreferences";
            int units =2; 
            string name;


            theUfSession.Part.New(part_name, units, out UFPart);
            theUfSession.Part.AskPartName(UFPart, out name);
            w.WriteLine("Loaded: " + name);
            
            //int ifail,errorCode;
            int[] mpi_array = new int[100];
            double[] mpr_array = new double[70];

            string rad_symbol; 
            string dia_symbol;

            Tag part_tag = Tag.Null;
            Tag dimension_tag = Tag.Null;
            int i;

            part_tag = theUfSession.Part.AskDisplayPart();     
            w.WriteLine("Dimension Creation method: 1- Automatic Text;\n");
            w.WriteLine( "                           2- Automatic Text, Appended Text;\n" );
            w.WriteLine( "                           3- Manual Text;\n" );
            w.WriteLine("                            4-Manual Text, Appended Text.\n" );
            w.WriteLine( "Dimension Tag    Creation symbol\n\n" );
            /* cycle for dimensions */
            theUfSession.Obj.CycleObjsInPart(part_tag,UFConstants.UF_dimension_type,ref dimension_tag );
            /* find dimension creation parameters */
            theUfSession.Drf.AskPreferences(mpi_array, mpr_array, out rad_symbol, out dia_symbol );

            for(i=0;i <=99;i++)
            {
                w.WriteLine(mpi_array[i]);
                if( i % 3 == 0)
                {
                    w.WriteLine("\n");
                }
            }
            for(i=0;i <=51;i++)
            {
                w.WriteLine(mpi_array[i]);
                if( i % 3 == 0)
                {
                    w.WriteLine("\n");
                }
            }
            w.WriteLine("\n");
            w.WriteLine("\n");
            mpi_array[6] = 4; /* Set Tolerance type */
            mpi_array[12] = 2; /* Set Tolerance site */

            mpr_array[24] = 0.02;  /* Set Upper Tolerance */
            mpr_array[25] = 0.02;   /* Set Lower Tolerance */
                
            theUfSession.Drf.AskPreferences( mpi_array, mpr_array, out rad_symbol, out dia_symbol );
                       
            for(i=0;i <=99;i++)
            {
                w.WriteLine(mpi_array[i]);
                if( i % 3 == 0)
                {
                    w.WriteLine("\n");
                }
            }
            for(i=0;i <=51;i++)
            {
                w.WriteLine(mpi_array[i]);
                if( i % 3 == 0)
                {
                    w.WriteLine("\n");
                }
            }
            w.WriteLine("\n");
            w.WriteLine("\n");
            theUfSession.Part.Save();
            return 0;
        }

        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Drf_AskPreferences.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Drf_AskPreferences.prt") ) 
            {
                w.WriteLine("Remove EX_Drf_AskPreferences.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Drf_AskPreferences.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Drf_AskPreferences curveTest1 = new EX_Drf_AskPreferences();
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
