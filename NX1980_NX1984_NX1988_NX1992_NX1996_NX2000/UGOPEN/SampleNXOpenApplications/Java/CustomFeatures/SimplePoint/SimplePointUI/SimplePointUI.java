//=============================================================================
//
//                   Copyright (c) 2018 Siemens Industry Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Custom feature 
//=============================================================================
//

//==============================================================================
//  Purpose:  This TEMPLATE file contains JAVA source to guide you in the
//  construction of your Block application dialog. The generation of your
//  dialog file (.dlx extension) is the first step towards dialog construction
//  within NX.  You must now create a NX Open application that
//  utilizes this file (.dlx).
//
//  The information in this file provides you with the following:
//
//  1.  Help on how to load and display your Block UI Styler dialog in NX
//      using APIs provided in NXOpen.BlockStyler namespace
//  2.  The empty callback methods (stubs) associated with your dialog items
//      have also been placed in this file. These empty methods have been
//      created simply to start you along with your coding requirements.
//      The method name, argument list and possible return values have already
//      been provided for you.
//==============================================================================

import java.rmi.RemoteException;
import nxopen.*;
import nxopen.blockstyler.*;
import nxopen.features.CustomAttribute;
import nxopen.features.CustomFeature;
import nxopen.features.CustomFeatureBuilder;
import nxopen.features.CustomFeatureData;
import nxopen.features.CustomDoubleAttribute;

//------------------------------------------------------------------------------
//Represents Block Styler application class
//------------------------------------------------------------------------------
public class SimplePointUI implements BlockDialog.Initialize, BlockDialog.DialogShown, BlockDialog.Apply, BlockDialog.Ok, BlockDialog.Update
{
    //class members
    public static Session theSession = null;
    public static UI theUI = null;
    private String theDlxFileName;
    private nxopen.blockstyler.BlockDialog theDialog;
    private nxopen.blockstyler.DoubleBlock pointX;// Block type: Double
    private nxopen.blockstyler.DoubleBlock pointZ;// Block type: Double
    private nxopen.blockstyler.DoubleBlock pointY;// Block type: Double
    
    //------------------------------------------------------------------------------
    //Constructor for NX Styler class
    //------------------------------------------------------------------------------
    public SimplePointUI() throws Exception, RemoteException
    {
        try
        {
            theSession = (Session)SessionFactory.get("Session");
            theUI = (UI)SessionFactory.get("UI");
            theDlxFileName = "SimplePointUI.dlx";
            theDialog = theUI.createDialog(theDlxFileName);
            theDialog.addApplyHandler(this);
            theDialog.addOkHandler(this);
            theDialog.addUpdateHandler(this);
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
    //        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    //        2) Invoke the Shared Library through File->Execute->NX Open menu.
    //
    //------------------------------------------------------------------------------
    public static void main(String [] argv) throws Exception
    {
        SimplePointUI theSimplePointUI = null;
        try
        {
            theSimplePointUI = new SimplePointUI();
            // The following method shows the dialog immediately
            theSimplePointUI.show();
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        finally
        {
            if(theSimplePointUI != null)
            {
                theSimplePointUI.dispose();
                theSimplePointUI = null;
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
        //return BaseSession.LibraryUnloadOption.EXPLICITLY;
         return BaseSession.LibraryUnloadOption.IMMEDIATELY;
        // return BaseSession.LibraryUnloadOption.AT_TERMINATION;
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
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }
    
    //------------------------------------------------------------------------------
    //This method shows the dialog on the screen
    //------------------------------------------------------------------------------
    public int show() throws NXException, RemoteException
    {
        try
        {
            nxopen.features.CustomFeatureClassManager cfMgr = theSession.customFeatureClassManager();
            nxopen.features.CustomFeatureClass cfClass = cfMgr.getClassFromName("NXOpen::CustomFeature::SimplePoint");
            nxopen.features.CustomFeature theCustomFeature = cfMgr.getEditedCustomFeature();
            nxopen.features.CustomFeatureData cfData = null;
            
            BlockDialog.DialogMode mode = BlockDialog.DialogMode.CREATE ;
            if(theCustomFeature != null)
            {
                mode = BlockDialog.DialogMode.EDIT;
            }
            theDialog.show(mode);
        }
        catch(Exception ex)
        {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
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
    //---------------------Block UI Styler Callback Functions--------------------------
    //------------------------------------------------------------------------------
    
    //------------------------------------------------------------------------------
    //Callback Name: initialize
    //------------------------------------------------------------------------------
    public void initialize() throws NXException, RemoteException
    {
        try
        {
            pointX = (nxopen.blockstyler.DoubleBlock)theDialog.topBlock().findBlock("pointX");
            pointZ = (nxopen.blockstyler.DoubleBlock)theDialog.topBlock().findBlock("pointZ");
            pointY = (nxopen.blockstyler.DoubleBlock)theDialog.topBlock().findBlock("pointY");
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
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
            // Let's populate dialog with data from edited feature..
            nxopen.features.CustomFeatureClassManager cfMgr = theSession.customFeatureClassManager();
            nxopen.features.CustomFeatureClass cfClass = cfMgr.getClassFromName("NXOpen::CustomFeature::SimplePoint");
            nxopen.features.CustomFeature theCustomFeature = cfMgr.getEditedCustomFeature();
            nxopen.features.CustomFeatureData cfData = null;
            
            if(theCustomFeature != null)
            {
                cfData = theCustomFeature.featureData();
                CustomDoubleAttribute pointXAttribute = cfData.customDoubleAttributeByName("PointX");
                pointX.setValue(pointXAttribute.value());
                                
                CustomDoubleAttribute pointYAttribute = cfData.customDoubleAttributeByName("PointY");
                pointY.setValue(pointYAttribute.value());
                                
                CustomDoubleAttribute pointZAttribute = cfData.customDoubleAttributeByName("PointZ");
                pointZ.setValue(pointZAttribute.value());
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
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
            nxopen.Part workPart = theSession.parts().work();
            nxopen.features.CustomFeatureClassManager cfMgr = theSession.customFeatureClassManager();
            nxopen.features.CustomFeatureClass cfClass = cfMgr.getClassFromName("NXOpen::CustomFeature::SimplePoint");
            nxopen.features.CustomFeature theCustomFeature = cfMgr.getEditedCustomFeature();
            nxopen.features.CustomFeatureData cfData = null;
            
            if (theCustomFeature == null)
            {
                // There is no edited custom feature, thus this is create scenario
                
                // Create attributes to store input received in UI
                CustomAttribute[] cfAttributes =  new CustomAttribute[3];
                
                nxopen.features.FeatureCollection featureCollection = workPart.features();
                nxopen.features.CustomAttributeCollection attribCollection = featureCollection.customAttributeCollection();
                
                nxopen.features.CustomAttribute.Property[] attributeProperties = new nxopen.features.CustomAttribute.Property[0];
                
                CustomDoubleAttribute pointXAttribute = (nxopen.features.CustomDoubleAttribute)attribCollection.createCustomDoubleAttribute("PointX", attributeProperties);
                pointXAttribute.setValue(pointX.value());
                cfAttributes[0] = pointXAttribute;
                
                CustomDoubleAttribute pointYAttribute = (nxopen.features.CustomDoubleAttribute)attribCollection.createCustomDoubleAttribute("PointY", attributeProperties);
                pointYAttribute.setValue(pointY.value());
                cfAttributes[1] = pointYAttribute;
                
                CustomDoubleAttribute pointZAttribute = (nxopen.features.CustomDoubleAttribute)attribCollection.createCustomDoubleAttribute("PointZ", attributeProperties);
                pointZAttribute.setValue(pointZ.value());
                cfAttributes[2] = pointZAttribute;
                
                cfData = workPart.features().customFeatureDataCollection().createData(cfClass, cfAttributes);
            }
            else
            {
                // This is edit scenario, lets update values in attributes if edited custom feature
                cfData = theCustomFeature.featureData();
                CustomDoubleAttribute pointXAttribute = cfData.customDoubleAttributeByName("PointX");
                pointXAttribute.setValue(pointX.value());
                                
                CustomDoubleAttribute pointYAttribute = cfData.customDoubleAttributeByName("PointY");
                pointYAttribute.setValue(pointY.value());
                                
                CustomDoubleAttribute pointZAttribute = cfData.customDoubleAttributeByName("PointZ");
                pointZAttribute.setValue(pointZ.value());
            }
            
            CustomFeatureBuilder cfBuilder = workPart.features().createCustomFeatureBuilder(theCustomFeature);
            
            cfBuilder.setFeatureData(cfData);
            
            theCustomFeature = (CustomFeature)cfBuilder.commitFeature();
            
            cfBuilder.destroy();
            cfBuilder = null;
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            errorCode = 1;
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return errorCode;
    }
    //------------------------------------------------------------------------------
    //Callback Name: update
    //Following callback is associated with the "theDialog" Block.
    //------------------------------------------------------------------------------
    public int update( nxopen.blockstyler.UIBlock block) throws NXException, RemoteException
    {
        try
        {
            if(block == pointX)
            {
            //---------Enter your code here-----------
            }
            else if(block == pointZ)
            {
            //---------Enter your code here-----------
            }
            else if(block == pointY)
            {
            //---------Enter your code here-----------
            }
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return 0;
    }
    
    //------------------------------------------------------------------------------
    //Callback Name: ok
    //------------------------------------------------------------------------------
    public int ok() throws NXException, RemoteException
    {
        int errorCode = 0;
        try
        {
            //---- Enter your callback code here -----
            errorCode = apply();
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            errorCode = 1;
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return errorCode;
    }
    
    //------------------------------------------------------------------------------
    //Function Name: GetBlockProperties
    //------------------------------------------------------------------------------
    public PropertyList getBlockProperties(String blockID) throws NXException, RemoteException
    {
        PropertyList plist = null;
        try
        {
            plist = theDialog.getBlockProperties(blockID);
        }
        catch(Exception ex)
        {
            //---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return plist;
    }
    
}
