//=============================================================================
//
//                   Copyright (c) 2008 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//

//==============================================================================
//  WARNING!!  This file is overwritten by the Block Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//==============================================================================

//------------------------------------------------------------------------------
//These imports are needed for the following template code
//------------------------------------------------------------------------------
import java.rmi.RemoteException;
import nxopen.*;
import nxopen.blockstyler.*;

//------------------------------------------------------------------------------
//Represents Block Styler application class
//------------------------------------------------------------------------------
public class ColoredBlock implements BlockDialog.Initialize, BlockDialog.DialogShown, BlockDialog.Apply
{
    //class members
    public static Session theSession = null;
    public static UI theUI = null;
    static ColoredBlock theColoredBlock;
    private String theDialogName;
    private nxopen.blockstyler.BlockDialog theDialog;
    private nxopen.blockstyler.UIBlock group0;// Block type: Group
    private nxopen.blockstyler.UIBlock blockHeight;// Block type: Double
    private nxopen.blockstyler.UIBlock blockWidth;// Block type: Double
    private nxopen.blockstyler.UIBlock blockLength;// Block type: Double
    private nxopen.blockstyler.UIBlock blockOrigin;// Block type: Specify Point
    private nxopen.blockstyler.UIBlock blockColor;// Block type: Color Picker

    //------------------------------------------------------------------------------
    //Constructor for NX Styler class
    //------------------------------------------------------------------------------
    public ColoredBlock() throws Exception, RemoteException
    {
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUI = (UI)SessionFactory.get("UI");
            theDialogName = "ColoredBlock.dlx";
            theDialog = theUI.createDialog(theDialogName);
            theDialog.addApplyHandler(this);
            theDialog.addInitializeHandler(this);
            theDialog.addDialogShownHandler(this);
 
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            throw new Exception(ex);
        }
    }
    //------------------------------- DIALOG LAUNCHING ---------------------------------
    //
    //    Before invoking this application one needs to open any part/empty part in NX
    //    because of the behavior of the blocks.
    //
    //    Make sure the dlx file is in one of the following locations:
    //        1.) From where NX session is launched
    //        2.) $UGII_USER_DIR/application
    //        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    //            recommended. This variable is set to a full directory path to a file 
    //            containing a list of root directories for all custom applications.
    //            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\\ugii\menus\custom_dirs.dat
    //
    //    You can create the dialog using one of the following way:
    //
    //    1. USER EXIT
    //
    //        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
    //        2) Invoke the Shared Library through File->Execute->NX Open menu.
    //
    //------------------------------------------------------------------------------
    public static void main(String [] argv) throws Exception
    {
        try
        {
            theColoredBlock = new ColoredBlock();
            // The following method shows the dialog immediately
            theColoredBlock.show();
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
             theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        finally
        {
            if(theColoredBlock != null)
            {
                theColoredBlock.dispose();
            }
        }
    }
    
    //------------------------------------------------------------------------------
    // This method specifies how a shared image is unloaded from memory
    // within NX. This method gives you the capability to unload an
    // internal NX Open application or user  exit from NX. Specify any
    // one of the three constants as a return value to determine the type
    // of unload to perform:
    //
    //
    //    Immediately : unload the library as soon as the automation program has completed
    //    Explicitly  : unload the library from the "Unload Shared Image" dialog
    //    AtTermination : unload the library when the NX session terminates
    //
    //
    // NOTE:  A program which associates NX Open applications with the menubar
    // MUST NOT use this option since it will UNLOAD your NX Open application image
    // from the menubar.
    //------------------------------------------------------------------------------
     public static final int getUnloadOption()
    {
        return BaseSession.LibraryUnloadOption.EXPLICITLY;
    }
    
    //------------------------------------------------------------------------------
    // Following method cleanup any housekeeping chores that may be needed.
    // This method is automatically called by NX.
    //------------------------------------------------------------------------------
    public static void onUnload() throws NXException, RemoteException
    {
        try
        {
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
             theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }
    
    //------------------------------------------------------------------------------
    //This method shows the dialog on the screen
    //------------------------------------------------------------------------------
    public int show() throws NXException, RemoteException
    {
        try
        {
            theDialog.show();
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
             theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return 0;
    }
    
    //------------------------------------------------------------------------------
    //Method Name: dispose
    //------------------------------------------------------------------------------
    public void dispose() throws NXException, RemoteException
    {
        if(theDialog != null)
        {
            theDialog.dispose();
            theDialog = null;
        }
    }
    
    //------------------------------------------------------------------------------
    //---------------------Block Styler Callback Functions--------------------------
    //------------------------------------------------------------------------------
    
    //------------------------------------------------------------------------------
    //Callback Name: initialize
    //------------------------------------------------------------------------------
    public void initialize() throws NXException, RemoteException
    {
        try
        {
            group0 = theDialog.topBlock().findBlock("group0");
            blockHeight = theDialog.topBlock().findBlock("blockHeight");
            blockWidth = theDialog.topBlock().findBlock("blockWidth");
            blockLength = theDialog.topBlock().findBlock("blockLength");
            blockOrigin = theDialog.topBlock().findBlock("blockOrigin");
            blockColor = theDialog.topBlock().findBlock("blockColor");

            // Set the upper-limits and lower-limits
            PropertyList blockHeightProps = blockHeight.getProperties();
            blockHeightProps.setDouble("MaximumValue", 100000.0);
            blockHeightProps.setDouble("MinimumValue", 0.001);
            blockHeightProps.setDouble("Value", 100.0);
            blockHeightProps.dispose();
            blockHeightProps = null;

            PropertyList blockWidthProps = blockWidth.getProperties();
            blockWidthProps.setDouble("MaximumValue", 100000.0);
            blockWidthProps.setDouble("MinimumValue", 0.001);
            blockWidthProps.setDouble("Value", 100.0);
            blockWidthProps.dispose();
            blockWidthProps = null;

            PropertyList blockLengthProps = blockLength.getProperties();
            blockLengthProps.setDouble("MaximumValue", 100000.0);
            blockLengthProps.setDouble("MinimumValue", 0.001);
            blockLengthProps.setDouble("Value", 100.0);
            blockLengthProps.dispose();
            blockLengthProps = null;

        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
             theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: dialogShown
    //This callback is executed just before the dialog launch. Thus any value set 
    //here will take precedence and dialog will be launched showing that value. 
    //------------------------------------------------------------------------------
    public void dialogShown() throws NXException, RemoteException
    {
        try
        {
            //---- Enter your callback code here -----
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
             theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: apply
    //Following callback is associated with the "theDialog" Block.
    //------------------------------------------------------------------------------
    public int apply() throws NXException, RemoteException
    {
        int errorCode = 0;
        try
        {
            Part workPart = theSession.parts().work();

                        //Get the values from UI Blocks
            PropertyList blockHeightProps = blockHeight.getProperties();
            double theHeight = blockHeightProps.getDouble("Value");
            blockHeightProps.dispose();
            blockHeightProps = null;

            PropertyList blockWidthProps = blockWidth.getProperties();
            double theWidth = blockWidthProps.getDouble("Value");
            blockWidthProps.dispose();
            blockWidthProps = null;

            PropertyList blockLengthProps = blockLength.getProperties();
            double theLength = blockLengthProps.getDouble("Value");
            blockLengthProps.dispose();
            blockLengthProps = null;

            PropertyList blockOriginProps = blockOrigin.getProperties();
            Point3d originPoint = blockOriginProps.getPoint("Point");
            blockOriginProps.dispose();
            blockOriginProps = null;

            PropertyList blockColorProps = blockColor.getProperties();
            int[] color = blockColorProps.getIntegerVector("Value");
            blockColorProps.dispose();
            blockColorProps = null;

            //Create the NX block
            nxopen.features.Feature nullFeatures_Feature = null;
            nxopen.features.BlockFeatureBuilder blockFeatureBuilder1;
            blockFeatureBuilder1 = workPart.features().createBlockFeatureBuilder(nullFeatures_Feature);

            blockFeatureBuilder1.setOriginAndLengths(originPoint, Double.toString(theLength), Double.toString(theHeight), Double.toString(theWidth));

            nxopen.features.Feature feature1;
            feature1 = blockFeatureBuilder1.commitFeature();
            blockFeatureBuilder1.destroy();

            // Get the body from Feature
            nxopen.features.BodyFeature bodyFeat = (nxopen.features.BodyFeature)feature1;
            Body[] bodies = new Body[1];
            bodies = bodyFeat.getBodies();
            // Apply the color to feature body
            DisplayModification displayModification1;
            displayModification1 = theSession.displayManager().newDisplayModification();
            displayModification1.setApplyToAllFaces(true);

            displayModification1.setNewColor(color[0]);
            DisplayableObject[] objects1 = new DisplayableObject[1];
            objects1[0] = bodies[0];
            displayModification1.apply(objects1);
            displayModification1.dispose();
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
             errorCode = 1;
             theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
        }
        return errorCode;
    }
    
}
