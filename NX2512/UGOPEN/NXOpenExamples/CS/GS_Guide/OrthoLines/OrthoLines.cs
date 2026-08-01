/*=============================================================================
                   Copyright (c) 2022 Siemens PLM Solutions
                   
                    Unpublished - All rights reserved
                    

===============================================================================

------------------------------------------------------------------------------
These imports are needed for the following template code
------------------------------------------------------------------------------*/
using System;
using NXOpen;
using NXOpen.BlockStyler;

/*------------------------------------------------------------------------------
Represents Block Styler application class
------------------------------------------------------------------------------*/

namespace OrthoLines
{
    public class Ortho
    {
        // Class members
        private static Session theSession;
        private static UI theUI;
        private string theDlxFileName;
        private NXOpen.BlockStyler.BlockDialog theDialog;
        private NXOpen.BlockStyler.Enumeration directionBlock;  // Block type: Enumeration
        private NXOpen.BlockStyler.DoubleBlock offsetBlock;     // Block type: Double

        /*------------------------------------------------------------------------------
        Constructor for NX Styler class
        ------------------------------------------------------------------------------*/

        public Ortho()
        {
            try
            {
                theSession = Session.GetSession();
                theUI = UI.GetUI();
                theDlxFileName = "OrthoLines.dlx";
                theDialog = theUI.CreateDialog(theDlxFileName);
                theDialog.AddApplyHandler(apply_cb);
                theDialog.AddOkHandler(ok_cb);
                theDialog.AddUpdateHandler(update_cb);
                theDialog.AddInitializeHandler(initialize_cb);
                theDialog.AddDialogShownHandler(dialogShown_cb);
            }
            catch (Exception ex)
            {
                // ---- Enter your exception handling code here -----
                throw ex;
            }
        }

        /*------------------------------- DIALOG LAUNCHING ---------------------------------

    Before invoking this application one needs to open any part/empty part in NX
    because of the behavior of the blocks.

    Make sure the dlx file is in one of the following locations:
        1.) From where NX session is launched
        2.) $UGII_USER_DIR/application
        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
            recommended. This variable is set to a full directory path to a file 
            containing a list of root directories for all custom applications.
            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_ROOT_DIR\menus\custom_dirs.dat

    You can create the dialog using one of the following way:

    1. Journal Replay

        1) Replay this file through Tool->Journal->Play Menu.

    2. USER EXIT

        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
        2) Invoke the Shared Library through File->Execute->NX Open menu.

------------------------------------------------------------------------------*/

        public static void Main()
        {
            Ortho theOrthoLines = null; // TODO Change to default(_) if this is not a reference type
            try
            {
                theOrthoLines = new Ortho();
                // The following method shows the dialog immediately
                theOrthoLines.Launch();
            }
            catch (Exception ex)
            {

                // ---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
            }
            finally
            {
                if (theOrthoLines != null)
                {
                    theOrthoLines.Dispose();
                    theOrthoLines = null; // TODO Change to default(_) if this is not a reference type
                }
            }
        }

        /*------------------------------------------------------------------------------
         This method specifies how a shared image is unloaded from memory
         within NX. This method gives you the capability to unload an
         internal NX Open application or user  exit from NX. Specify any
         one of the three constants as a return value to determine the type
         of unload to perform:


            Immediately : unload the library as soon as the automation program has completed
            Explicitly  : unload the library from the "Unload Shared Image" dialog
            AtTermination : unload the library when the NX session terminates


         NOTE:  A program which associates NX Open applications with the menubar
         MUST NOT use this option since it will UNLOAD your NX Open application image
         from the menubar.
        '------------------------------------------------------------------------------*/
        public static int GetUnloadOption(string arg)
        {
            // Return CType(Session.LibraryUnloadOption.Explicitly, Integer)
            return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);
        }

        /*------------------------------------------------------------------------------
            Following method cleanup any housekeeping chores that may be needed.
            This method is automatically called by NX.
        ------------------------------------------------------------------------------*/
        public static void UnloadLibrary(string arg)
        {
            try
            {
            }

            catch (Exception ex)
            {

                // ---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
            }
        }
        /*------------------------------------------------------------------------------
        This method launches the dialog to screen
        ------------------------------------------------------------------------------*/
        public NXOpen.BlockStyler.BlockDialog.DialogResponse Launch()
        {
            NXOpen.BlockStyler.BlockDialog.DialogResponse DialogResponse = NXOpen.BlockStyler.BlockDialog.DialogResponse.Invalid;
            try
            {
                DialogResponse = theDialog.Launch();
            }
            catch (Exception ex)
            {

                // ---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
            }
            return DialogResponse;
        }
        /*------------------------------------------------------------------------------
        Method Name: Dispose
        ------------------------------------------------------------------------------*/
        public void Dispose()
        {
            if (theDialog != null)
            {
                theDialog.Dispose();
                theDialog = null;
            }
        }
        /*------------------------------------------------------------------------------
        ---------------------Block UI Styler Callback Functions--------------------------
        ------------------------------------------------------------------------------
    
        ------------------------------------------------------------------------------
        Callback Name: initialize_cb
        ------------------------------------------------------------------------------*/
        public void initialize_cb()
        {
            try
            {
                directionBlock = (NXOpen.BlockStyler.Enumeration)theDialog.TopBlock.FindBlock("directionBlock");
                offsetBlock = (NXOpen.BlockStyler.DoubleBlock)theDialog.TopBlock.FindBlock("offsetBlock");
            }
            catch (Exception ex)
            {

                // ---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
            }
        }
        /*------------------------------------------------------------------------------
        Callback Name: dialogShown_cb
        This callback is executed just before the dialog launch. Thus any value set 
        here will take precedence and dialog will be launched showing that value. 
        ------------------------------------------------------------------------------*/
        public void dialogShown_cb()
        {
            try
            {
            }

            // ---- Enter your callback code here -----

            catch (Exception ex)
            {

                // ---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
            }
        }
        /*------------------------------------------------------------------------------
        Callback Name: apply_cb
        ------------------------------------------------------------------------------*/
        public int apply_cb()
        {
            int errorCode = 0;
            try
            {
                // ---- Enter your callback code here -----
                CreateLine();
            }
            catch (Exception ex)
            {

                // ---- Enter your exception handling code here -----
                errorCode = 1;
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
            }
            return errorCode;
        }
        /*------------------------------------------------------------------------------
        Callback Name: update_cb
        ------------------------------------------------------------------------------*/

        public int update_cb(NXOpen.BlockStyler.UIBlock block)
        {
            try
            {
                if (block == directionBlock)
                {
                }
                else if (block == offsetBlock)
                {
                }
            }
            catch (Exception ex)
            {

                // ---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
            }
            return 0;
        }


        /*------------------------------------------------------------------------------
        Callback Name: ok_cb
        ------------------------------------------------------------------------------*/
        public int ok_cb()
        {
            int errorCode = 0;
            try
            {

                // ---- Enter your callback code here -----
                // errorCode = apply_cb();
            }
            catch (Exception ex)
            {
                // ---- Enter your exception handling code here -----
                errorCode = 1;
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
            }
            return errorCode;
        }
        /*------------------------------------------------------------------------------
        Function Name: GetBlockProperties
        Returns the propertylist of the specified BlockID
        ------------------------------------------------------------------------------*/
        public PropertyList GetBlockProperties(string blockID)
        {
            PropertyList GetBlockProperties = null; // TODO Change to default(_) if this is not a reference type
            try
            {
                GetBlockProperties = theDialog.GetBlockProperties(blockID);
                return GetBlockProperties;
            }
            catch (Exception ex)
            {

                // ---- Enter your exception handling code here -----
                theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString());
            }
            return GetBlockProperties;
        }

        private Line CreateLine()
        {
            double infinity = 50000;
            double d = offsetBlock.Value;
            if (directionBlock.ValueAsString == "Horizontal")
                return Guide.CreateLine(-infinity, d, 0, infinity, d, 0);  // Horizontal line
            else
                return Guide.CreateLine(d, -infinity, 0, d, infinity, 0);// Vertical line
        }
    }
 }

