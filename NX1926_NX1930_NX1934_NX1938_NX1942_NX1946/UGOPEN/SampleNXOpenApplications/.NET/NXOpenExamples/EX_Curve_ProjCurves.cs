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
    /// This example will create EX_Curve_ProjCurves.prt, EX_Curve_ProjCurves.log files 
    /// and demonstrates curve projection functionality usung theUfSession.Curve.CreateProjCurves().
    /// The program prints the report to the log file called "EX_Curve_ProjCurves.log".
    public class EX_Curve_ProjCurves
    {
        private static FileStream fs; 
        private static StreamWriter w;
        private static UFSession theUfSession;
        private static Session theSession;

       
            
        public int Execute()
        {
            Tag UFPart;
            string part_name = "EX_Curve_ProjCurves";
            int units =2; 
            string name;


            theUfSession.Part.New(part_name, units, out UFPart);
            theUfSession.Part.AskPartName(UFPart, out name);
            w.WriteLine("Loaded: " + name);
            
            int num_faces,i,num_proj_curves;
            double[] origin={0.0,0.0,0.0};
            Tag block_tag;
            Tag[] curves_to_proj= new Tag[1];
            Tag proj_curve_feature;
            Tag[] proj_curves;
            Tag defining_feature,defining_target,defining_curve;
            String[] edge_lens={"300.0","25.0","150.0"};
            UFCurve.Line line_data= new UFCurve.Line();
            UFCurve.Proj proj_data = new UFCurve.Proj();
            Tag[] face_list;
            theUfSession.Modl.CreateBlock1(FeatureSigns.Nullsign,origin,edge_lens,out block_tag);
            
            line_data.start_point = new double[3];
            line_data.start_point[0] =  25.0;
            line_data.start_point[1] =  50.0;
            line_data.start_point[2] =  25.0;
            line_data.end_point = new double[3]; 
            line_data.end_point[0]   = 275.0;
            line_data.end_point[1]   =  50.0;
            line_data.end_point[2]   = 125.0;
            
            theUfSession.Curve.CreateLine(ref line_data, out curves_to_proj[0]);
            Console.WriteLine("curves to project tag = {0}\n",curves_to_proj[0]);
            theUfSession.Modl.AskFeatFaces(block_tag,out face_list);
            theUfSession.Modl.AskListCount(face_list, out num_faces);
            
            proj_data.proj_type = 3;
            proj_data.proj_vec = new Double[3];
            proj_data.proj_vec[0] = 0.0;
            proj_data.proj_vec[1] = 1.0;
            proj_data.proj_vec[2] = 0.0;
            proj_data.multiplicity = 2;
            theUfSession.Curve.CreateProjCurves(1,curves_to_proj,face_list.Length,face_list,3,ref proj_data,out proj_curve_feature);
            w.WriteLine("proj UFCurve feature tag = {0}\n",proj_curve_feature);
            theUfSession.Curve.AskProjCurves(proj_curve_feature,out num_proj_curves,out proj_curves);
            for (i = 0;i < num_proj_curves;i++)
            {
                theUfSession.Curve.AskProjCurveParents(proj_curves[i],out defining_feature,out defining_target,out defining_curve);
                w.WriteLine("proj_curves[{0}]\n",i);
                w.WriteLine("  belongs to feature tag = {0}\n",defining_feature);
                w.WriteLine("  was projected onto tag = {0}\n",defining_target);
                w.WriteLine("  was generated by UFCurve tag = {0}\n", defining_curve);
            }

            theUfSession.Part.Save();

            return 0;
        }
        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Curve_ProjCurves.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Curve_ProjCurves.prt") ) 
            {
                w.WriteLine("Remove EX_Curve_ProjCurves.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Curve_ProjCurves.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Curve_ProjCurves curveTest1 = new EX_Curve_ProjCurves();
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
