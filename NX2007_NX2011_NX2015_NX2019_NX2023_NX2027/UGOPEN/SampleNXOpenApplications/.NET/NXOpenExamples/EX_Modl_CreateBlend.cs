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
    /// This example will create EX_Modl_CreateBlend.prt, EX_Modl_CreateBlend.log files and creates a block 1x2x3 units. 
    /// The four 3-unit edges are blended using method theUfSession.Modl.CreateBlend() with a variable radius.
    /// The program prints the report to the log file called "EX_Modl_CreateBlend.log".
    public class EX_Modl_CreateBlend
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
             string part_name = "EX_Modl_CreateBlend";
             int units =2; 
             string name;


             theUfSession.Part.New(part_name, units, out UFPart);
             theUfSession.Part.AskPartName(UFPart, out name);
             w.WriteLine("Loaded: " + name);
            
             Tag         block_tag;
             Tag[]       list1;
             double[]     corner_point= new double[3];
             string[]     edge_lengths = { "1.0", "2.0", "3.0" };
             Tag         block_feature_tag;
             UFFacet.Parameters faceting_params = new UFFacet.Parameters();
             int ecount;
             Tag         blend1;
             Tag[]       list2;
             double[]     pt1={0.0, 0.0, 0.0};
             double[]     pt2={0.0, 0.0, 0.0}; 

             int          allow_smooth = 0;
             int          allow_cliff = 0;
             int          allow_notch = 0;
             double       vrb_tol = 0.0;

             /* First create a UFPart in which we will initially create a
                block.*/
            
         
             theUfSession.Assem.SetWorkPart(UFPart);
             corner_point[0] = 0.0;
             corner_point[1] = 0.0;
             corner_point[2] = 0.0;

             theUfSession.Modl.CreateBlock1(FeatureSigns.Nullsign,
                 corner_point,
                 edge_lengths,
                 out block_feature_tag );

             theUfSession.Modl.AskFeatBody(block_feature_tag, out block_tag );

             /* Get the edges of the body.  Get the count of the edge list.
             * This will be used to get the four 'vertical' corners of the block for
             * blending. Check return codes.
             */
             theUfSession.Modl.AskBodyEdges(block_tag, out list1);
             theUfSession.Modl.AskListCount(list1, out ecount);

             ArrayList arr_list2 = new ArrayList();
             for(int i=0; i < ecount; i++) 
             {
                 Tag edge;               /* edge object */

                 int vcount;             /* count of vertices in edge */

                 /* Get the edge (list item) and check return code.  */
                 theUfSession.Modl.AskListItem(list1,i,out edge);

                 /* Get the edge vertices.  Check return code.  */
                 theUfSession.Modl.AskEdgeVerts(edge,pt1, pt2, out vcount);

                 if(System.Math.Abs(System.Math.Abs(pt1[2] - pt2[2]) - 3.0) < 0.001)
                 {
                     arr_list2.Add(edge);
                 }
                
             }
             list2 = (Tag [])arr_list2.ToArray(typeof(Tag));
             theUfSession.Modl.CreateBlend("0.009246", list2, allow_smooth,
                 allow_cliff, allow_notch, vrb_tol, out blend1);

             theUfSession.Part.Save();

             return 0;
        }

        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            fs = new FileStream("EX_Modl_CreateBlend.log", FileMode.Create, FileAccess.Write);
            w = new StreamWriter(fs); // create a stream writer 
            w.Write("Log Entry : \r\n");
            w.WriteLine("--Log entry goes here--"); 
            w.Flush(); // update underlying file

            if ( File.Exists("EX_Modl_CreateBlend.prt") ) 
            {
                w.WriteLine("Remove EX_Modl_CreateBlend.prt file from <Project Folder>\\bin\\Debug !!");
                w.WriteLine("EX_Modl_CreateBlend.prt already exists. !!");
                w.Close();
                return;
            }

            try
            {
                EX_Modl_CreateBlend curveTest1 = new EX_Modl_CreateBlend();
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
