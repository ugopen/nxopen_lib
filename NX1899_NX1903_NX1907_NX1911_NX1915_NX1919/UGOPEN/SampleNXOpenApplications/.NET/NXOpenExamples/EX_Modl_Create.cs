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
    /// This example will create EX_Modl_Create.prt, EX_Modl_Create.log files 
    /// and creates rectangular groove using theUfSession.Modl.CreateRectGroove() method.
    /// The program prints the report to the log file called "EX_Modl_Create.log".
    public class EX_Modl_Create
    {
        private static FileStream fs; 
        private static StreamWriter w;
        public static UFSession theUfSession;
        private static Session theSession;

        public int Execute()
        {
            Tag UFPart;
            string part_name = "EX_Modl_Create";
            int units =2; 
            string name;


            theUfSession.Part.New(part_name, units, out UFPart);
            theUfSession.Part.AskPartName(UFPart, out name);
            w.WriteLine("Loaded: " + name);
                
            int count;
            int i;
            int type;
            int norm_dir;
      
            Tag cyl_obj_id, face, feature_id, body;
            Tag face_id = Tag.Null;

            Tag[] face_list;
            double[] origin = {0.0, 0.0, 0.0};
            double[] direction = {0.0, 0.0, 1.0};
            double[] center= new double[3];
            double[] dir= new double[3];
            double[] box= new double[6];
            double radius;
            double rad_data;
            double[] location = {0.0,0.0,2.0};
            string height = "4.0";
            string diam   = "2.0";
            string gr_diam = "1.0";
            string width = "1.0";
      
            theUfSession.Modl.CreateList(out face_list);
            theUfSession.Modl.CreateCyl1(FeatureSigns.Nullsign,origin,height,diam,direction,
            out cyl_obj_id);
            theUfSession.Modl.AskFeatBody(cyl_obj_id, out body);
            w.WriteLine("Body is : {0}", body);
            theUfSession.Modl.AskBodyFaces(body,out face_list);
            w.WriteLine("Face_list is : {0}",face_list);
            theUfSession.Modl.AskListCount(face_list, out count);
            w.WriteLine("Count is: {0}", count);
            for(i = 0; i < count; i++) 
            {
                theUfSession.Modl.AskListItem(face_list,i,out face);
                w.WriteLine("face is : {0}", face);
                theUfSession.Modl.AskFaceData(face, out type, center, dir, box, out radius,
                out rad_data, out norm_dir);
                w.WriteLine("face data is: {0},{1},{2}", radius, rad_data, norm_dir);
                if(type == UFConstants.UF_cylinder_type) face_id = face;
            }
      
            theUfSession.Modl.CreateRectGroove(location,direction,gr_diam,width,
            face_id,out feature_id);

            theUfSession.Part.Save();
                    
            return 0;
        }

        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Modl_Create.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Modl_Create.prt") ) 
            {
                w.WriteLine("Remove EX_Modl_Create.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Modl_Create.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Modl_Create createGroove = new EX_Modl_Create();
                if (createGroove.Execute()==0)
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
