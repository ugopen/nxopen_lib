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
    /// This example demonstrates how to open Listing Window device in using,
    /// theUfSession.Ui.OpenListingWindow() and prints data using, theUfSession.Ui.WriteListingWindow() method.
    /// The program will create EX_Ui_ListingWindow.prt file and prints the name of the feature created into the Listing Window device.
    public class EX_Ui_ListingWindow
    {
        public static UFSession theUfSession;
        private static Session theSession;

        public int Execute()
        {
             Tag UFPart;
             string part_name = "EX_Ui_ListingWindow";
             int units =2; 
             string name;

             theUfSession.Part.New(part_name, units, out UFPart);
             theUfSession.Part.AskPartName(UFPart, out name);
             theUfSession.Ui.WriteListingWindow("Loaded: " + name + "\n");
            
             //Example code
             double[] block_orig = {0.0,0.0,0.0};
             string[] block_len = {"1","2","3"};
             string feature_name = null;
             string tmp_str;
             Tag blk_obj;
             
             theUfSession.Modl.CreateBlock1(FeatureSigns.Nullsign, block_orig, block_len, out blk_obj);
             theUfSession.Modl.AskFeatName(blk_obj,out feature_name);
             tmp_str = "Feature Name is " + feature_name + "\n";
             theUfSession.Ui.WriteListingWindow(tmp_str);
             theUfSession.Part.Save();
             return 0;
        }

        public static void Main(string[] args)
        {
            theSession=Session.GetSession();
            theUfSession= UFSession.GetUFSession();

            /* Open Listing Window */
            theUfSession.Ui.OpenListingWindow();

            theUfSession.Ui.WriteListingWindow("Log Entry : \r\n");
            theUfSession.Ui.WriteListingWindow("--Log entry goes here--\n");

            if ( File.Exists("EX_Ui_ListingWindow.prt") ) 
            {
                theUfSession.Ui.WriteListingWindow("Remove EX_Ui_ListingWindow.prt file from <Project Folder> !!\n");
                theUfSession.Ui.WriteListingWindow("EX_Ui_ListingWindow.prt already exists. !!\n");
                return;
            }

            try
            {
                EX_Ui_ListingWindow curveTest1 = new EX_Ui_ListingWindow();
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
                 string tmp_str = "Exception is: " + e.Message + "\n";
                 theUfSession.Ui.WriteListingWindow(tmp_str);
                 theUfSession.Ui.WriteListingWindow("Remove EX_Ui_ListingWindow.prt file from <Project Folder> !!\n");
            }
            theUfSession.Ui.WriteListingWindow("End of Log File\n");
        }
        public static int GetUnloadOption(string dummy) 
        {
            return UFConstants.UF_UNLOAD_IMMEDIATELY;
        }
    }
}
