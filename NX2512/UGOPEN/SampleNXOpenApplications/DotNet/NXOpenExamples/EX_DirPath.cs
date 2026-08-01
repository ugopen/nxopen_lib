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
    /// This example will create EX_DirPath.prt, EX_DirPath.log files 
    /// and queries directories at UGII_BASE_DIR and directories created using theUfSession.Dirpath.CreateFromDirs(), 
    /// using theUfSession.Dirpath.AskDirs() method. 
    /// The program prints the report to the log file called "EX_DirPath.log".
    public class EX_DirPath
    {
        private static FileStream fs; 
        private static StreamWriter w;
        private static UFSession theUfSession;
        private static Session theSession;

        public int Execute()
        {
            Tag UFPart;
            string part_name = "EX_DirPath";
            int units =2; 
            string name;

            theUfSession.Part.New(part_name, units, out UFPart);
            theUfSession.Part.AskPartName(UFPart, out name);
            w.WriteLine("Loaded: " + name);
            
            int numdir =0;
            string[] path =null;
            
            Tag  retTag;
            
            theUfSession.Dirpath.CreateFromEnv("UGII_BASE_DIR",out retTag);
            theUfSession.Dirpath.AskDirs( retTag, out numdir, out path);

            for(int ii=0; ii<numdir; ii++)
            {
                w.WriteLine("Dir Path: " + path[ii]);
            }
            
            path = null;
            NXOpen.Tag a_path;
            string[] dirs = {"/dir1", "/dir2" };
            theUfSession.Dirpath.CreateFromDirs( 2, dirs, out a_path );
            theUfSession.Dirpath.AskDirs( a_path, out numdir, out path);

            for(int ii=0; ii<numdir; ii++)
            {
                w.WriteLine("Dir Path: " + path[ii]);
            }

            string[] dirs1 = {"/dir3", "/dir4" };
            theUfSession.Dirpath.AppendFromDirs( a_path, 2, dirs1 );

            theUfSession.Dirpath.AskDirs( a_path, out numdir, out path);

            string curr_dir;
            theUfSession.Dirpath.AskCurrDir(a_path, out curr_dir);
            w.WriteLine("Current Dir : " + curr_dir );

            string nth_dir="";
            w.WriteLine("Index\t" + " Nth Dir");
            for(int index=0;index<numdir;index++)
            {
                theUfSession.Dirpath.AskNthDir(a_path,index,out nth_dir);
                w.WriteLine(index + "\t" + nth_dir );
            }
 
            theUfSession.Part.Save();
            return 0;
        }

        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_DirPath.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file
            if ( File.Exists("EX_DirPath.prt") ) 
            {
                  w.WriteLine("Remove EX_DirPath.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_DirPath.prt already exists. !!");
                w.Close();
                return;
               }

            try
            {
                EX_DirPath curveTest1 = new EX_DirPath();
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
