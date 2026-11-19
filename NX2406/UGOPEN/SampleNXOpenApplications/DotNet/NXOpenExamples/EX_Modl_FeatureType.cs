/*=============================================================================

                    Copyright (c) 2004 UGS PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: Example for Wrapped UFUNC (NXOpen.NET)

    This example program requires a work part with at least one feature. The
    example extracts the feature information of a given solid body via 
    theUfSession.Modl.AskFeatType(), theUfSession.Modl.AskMaster(), 
    theUfSession.Modl.AskFeatRelatives() etc. The program  prints a report 
    to the listing window.
 */
using System;
using System.IO;
using NXOpen;
using NXOpen.UF;

namespace NetExample
{
    /// This example program requires a work part with at least one feature. 
    /// The example extracts the feature information of a given solid body via theUfSession.Modl.AskFeatType(),
    /// theUfSession.Modl.AskMaster(), theUfSession.Modl.AskFeatRelatives() etc. 
    /// The program  prints a report to the listing window.
    public class EX_Modl_FeatureType
    {
        public static UFSession theUfSession;
        private static Session theSession;
        
        public int Execute()
         {
             
             int index, inx;
             int num_parents, num_children;
             int enttype;
             Tag feat1, master_feature;
             Tag[] parent_array, children_array;
             Tag part_tag;
             string feat_type = null;
             string tmp_text = null;
             feat1 = 0;
             master_feature = 0;
             index = 0;
             enttype = UFConstants.UF_feature_type; //UF_feature_type;
             double[] block_orig = {0.0,0.0,0.0};
             string[] block_len = {"1","2","3"};
            
             /* Get the tag of the work UFPart */
             part_tag = theUfSession.Assem.AskWorkPart();
             /* Cycle through all the features in the UFPart */
             do
             {
                 theUfSession.Obj.CycleObjsInPart(part_tag, enttype, ref feat1);
                 if(feat1 == Tag.Null) break;
                 /* Get the feature type */
                 theUfSession.Modl.AskFeatType(feat1,out feat_type);
                 tmp_text = " Feature "+ index + "  = " + feat1 + " is of type " + feat_type + "\n";
                 theUfSession.Ui.WriteListingWindow(tmp_text);
                 
                 ++index;
                 /* If the feature is an INSTANCE, then get the master feature and its type */
                 if (String.Compare(feat_type,"INSTANCE") == 0)
                 {
                     theUfSession.Modl.AskMaster(feat1,out master_feature);
                     theUfSession.Modl.AskFeatType(master_feature,out feat_type);
                     tmp_text = " Master Feature "+ master_feature + " is of type " + feat_type + "\n";
                     theUfSession.Ui.WriteListingWindow(tmp_text);
                 }
                 theUfSession.Modl.AskFeatRelatives(feat1,out num_parents,out parent_array,out num_children,
                     out children_array);

                 tmp_text =  "  Parent array for " + feat1 + " contains " + num_parents + " members:\n";
                 theUfSession.Ui.WriteListingWindow(tmp_text);
                 if(num_parents > 0)
                 {
                     for (inx = 0;inx < num_parents; inx++)
                     {
                         theUfSession.Modl.AskFeatType(parent_array[inx],out feat_type);
                         tmp_text =  "  Parent id " + inx + " = " + parent_array[inx] +
                                     " is of feature type " + feat_type + "\n";
                         theUfSession.Ui.WriteListingWindow(tmp_text);
                     }
                 }
                 
                 tmp_text = "  children array for feature " + feat1 + " contains " + num_children + "  members:\n";
                 theUfSession.Ui.WriteListingWindow(tmp_text);

                 if(num_children > 0)
                 {
                     for (inx = 0;inx < num_children; inx ++)
                     {
                         theUfSession.Modl.AskFeatType(children_array[inx],out feat_type);
                         tmp_text = "  child is " + inx + " = " + children_array[inx]
                                    + " is of feature type " + feat_type + "\n";
                         theUfSession.Ui.WriteListingWindow(tmp_text);
                     }
                 }

             }while(feat1 != 0);
             
            return 0;
        }

        public static void Main(string[] args)
        {
            string tmp_text = null;
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            /* Open Listing Window */
            theUfSession.Ui.OpenListingWindow();

            theUfSession.Ui.WriteListingWindow("Log Entry : \r\n");
            theUfSession.Ui.WriteListingWindow("--Log entry goes here--\n");
            
            try
            {
                EX_Modl_FeatureType curveTest1 = new EX_Modl_FeatureType();
                if (curveTest1.Execute()==0)
                {
                    theUfSession.Ui.WriteListingWindow("Successful\n");
                }
                else
                {
                    theUfSession.Ui.WriteListingWindow("Failed\n");
                }
            }
            catch(NXException e)
            {   
                tmp_text = "Exception is: " + e.Message + "\n";
                theUfSession.Ui.WriteListingWindow(tmp_text);
            }
            
            theUfSession.Ui.WriteListingWindow("End of Log File\n");
            //theUfSession.Ui.CloseListingWindow();
        }

        public static int GetUnloadOption(string dummy) 
        {
            return UFConstants.UF_UNLOAD_IMMEDIATELY;
        }
    }
}
