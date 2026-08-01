//==============================================================================
//
//      Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc. 
//                          All Rights Reserved.
//
//==============================================================================
// File description: Sample NX/Open Application for Block Styler
//==============================================================================
//

//==============================================================================
//  WARNING!!  This file is overwritten by the Block UI Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//==============================================================================

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

//------------------------------------------------------------------------------
//These imports are needed for the following template code
//------------------------------------------------------------------------------
import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;

import nxopen.BaseSession;
import nxopen.Face;
import nxopen.NXException;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.TaggedObject;
import nxopen.UI;
import nxopen.blockstyler.BlockDialog;
import nxopen.blockstyler.PropertyList;

//import nxopen.*;
//import nxopen.blockstyler.*;

//------------------------------------------------------------------------------
//Represents Block Styler application class
//------------------------------------------------------------------------------
public class ChangeFaceColor implements BlockDialog.Initialize, BlockDialog.DialogShown, BlockDialog.Apply,
        BlockDialog.Ok, BlockDialog.Cancel, BlockDialog.Update, BlockDialog.Filter, BlockDialog.FocusNotify,
        BlockDialog.KeyboardFocusNotify, BlockDialog.EnableOKButton {
    // class members
    public static Session theSession = null;
    public static UI theUI = null;
    private String theDlxFileName;
    private nxopen.blockstyler.BlockDialog theDialog;
    private nxopen.blockstyler.Group group0;// Block type: Group
    private nxopen.blockstyler.FaceCollector face_select0;// Block type: Face
                                                          // Collector
    private nxopen.blockstyler.ObjectColorPicker colorPicker0;// Block type:
                                                              // Color Picker

    // ------------------------------------------------------------------------------
    // Constructor for NX Styler class
    // ------------------------------------------------------------------------------
    public ChangeFaceColor() throws Exception, RemoteException {
        try {
            theSession = (Session)SessionFactory.get("Session");
            theUI = (UI)SessionFactory.get("UI");
            theDlxFileName = "ChangeFaceColor.dlx";
            theDialog = theUI.createDialog(theDlxFileName);
            theDialog.addApplyHandler(this);
            theDialog.addOkHandler(this);
            theDialog.addUpdateHandler(this);
            theDialog.addCancelHandler(this);
            theDialog.addFilterHandler(this);
            theDialog.addInitializeHandler(this);
            theDialog.addFocusNotifyHandler(this);
            theDialog.addKeyboardFocusNotifyHandler(this);
            theDialog.addEnableOKButtonHandler(this);
            theDialog.addDialogShownHandler(this);
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
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
    //            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR/ugii/menus/custom_dirs.dat
    //
    //    You can create the dialog using one of the following way:
    //
    //    1. USER EXIT
    //
    //        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    //        2) Invoke the Shared Library through File->Execute->NX Open menu.
    //
    //------------------------------------------------------------------------------
    public static void main(String[] argv) throws Exception {
        ChangeFaceColor theChangeFaceColor = null;
        try {
            theChangeFaceColor = new ChangeFaceColor();
            // The following method shows the dialog immediately
            theChangeFaceColor.show();
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        } finally {
            if (theChangeFaceColor != null) {
                theChangeFaceColor.dispose();
                theChangeFaceColor = null;
            }
        }
    }

    // ------------------------------------------------------------------------------
    // Method name: show_ChangeFaceColor
    // ------------------------------------------------------------------------------
    public static void show_ChangeFaceColor() throws NXException, RemoteException {
        ChangeFaceColor theChangeFaceColor = null;
        try {
            theChangeFaceColor = new ChangeFaceColor();
            // The following method shows the dialog immediately
            theChangeFaceColor.show();
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        } finally {
            if (theChangeFaceColor != null) {
                theChangeFaceColor.dispose();
                theChangeFaceColor = null;
            }
        }
    }

    // ------------------------------------------------------------------------------
    // This method specifies how a shared image is unloaded from memory
    // within NX. This method gives you the capability to unload an
    // internal NX Open application or user exit from NX. Specify any
    // one of the three constants as a return value to determine the type
    // of unload to perform:
    //
    //
    // Immediately : unload the library as soon as the automation program has
    // completed
    // Explicitly : unload the library from the "Unload Shared Image" dialog
    // AtTermination : unload the library when the NX session terminates
    //
    //
    // NOTE: A program which associates NX Open applications with the menubar
    // MUST NOT use this option since it will UNLOAD your NX Open application
    // image
    // from the menubar.
    // ------------------------------------------------------------------------------
    public static final int getUnloadOption() {
        // return BaseSession.LibraryUnloadOption.EXPLICITLY;
        return BaseSession.LibraryUnloadOption.IMMEDIATELY;
        // return BaseSession.LibraryUnloadOption.AT_TERMINATION;
    }

    // ------------------------------------------------------------------------------
    // Following method cleanup any housekeeping chores that may be needed.
    // This method is automatically called by NX.
    // ------------------------------------------------------------------------------
    public static void onUnload() throws NXException, RemoteException {
        try {
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }

    // ------------------------------------------------------------------------------
    // This method shows the dialog on the screen
    // ------------------------------------------------------------------------------
    public int show() throws NXException, RemoteException {
        try {
            theDialog.show();
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return 0;
    }

    // ------------------------------------------------------------------------------
    // Method Name: dispose
    // ------------------------------------------------------------------------------
    public void dispose() throws NXException, RemoteException {
        if (theDialog != null) {
            theDialog.dispose();
            theDialog = null;
        }
    }

    // ------------------------------------------------------------------------------
    // ---------------------Block UI Styler Callback
    // Functions--------------------------
    // ------------------------------------------------------------------------------

    // ------------------------------------------------------------------------------
    // Callback Name: initialize
    // ------------------------------------------------------------------------------
    public void initialize() throws NXException, RemoteException {
        try {
            group0 = (nxopen.blockstyler.Group) theDialog.topBlock().findBlock("group0");
            face_select0 = (nxopen.blockstyler.FaceCollector) theDialog.topBlock().findBlock("face_select0");
            colorPicker0 = (nxopen.blockstyler.ObjectColorPicker) theDialog.topBlock().findBlock("colorPicker0");

            theDialog.topBlock().setLabel("Change Face Color");
            group0.setLabel("Input Parameters");

            // Block Specific Properties for the Face Collector
            face_select0.setAllowConvergentObject(true);
            face_select0.setAutomaticProgression(false);
            face_select0.setBalloonTooltipText(
                    "Select the faces that you want to change the color. Use the Face Rules on the Top Border Bar to control the selection intent rules.");
            face_select0.setBlendVirtualCurveOverlay(false);
            face_select0.setCreateInterpartLink(false);
            face_select0.setInterpartSelectionAsString("Simple");
            // face_select0.setInterpartSelectionAsString("Non-associative
            // Interpart Copy Only");
            // face_select0.setInterpartSelectionAsString("Associative and
            // Non-associative Interpart Copy");
            // face_select0.setInterpartSelectionAsString("Associative Interpart
            // Copy");
            // Setting the Maximum Scope defines the maximum scope that is
            // available for
            // selection. It determines the options to be populated in the
            // Selection Scope
            // list in the Top Border Bar in NX. The user may select one of the
            // options in
            // this list to further restrict the Selection Scope.
            face_select0.setMaximumScopeAsString("Entire Assembly");
            // face_select0.setMaximumScopeAsString("Within Work Part and
            // Components");
            // face_select0.setMaximumScopeAsString("Within Work Part Only");
            // face_select0.setSelectModeAsString("Single");
            face_select0.setSelectModeAsString("Multiple");

            // Selection Intent Properties for the Face Collector
            face_select0.setFaceRules(specifyFaceRules());
            face_select0.setEntityType(specifyEntityType());
            face_select0.setDefaultFaceRulesAsString(defaultFaceRules());
            face_select0.setPopupMenuEnabled(true);

            // Block Specific Properties for the Object Color Picker
            colorPicker0.setNumberSelectable(1);
            colorPicker0.setValue(new int[] { 1 });
            colorPicker0.setBalloonTooltipText("Pick the new color for the selected faces.");

            // General Properties for the Object Color Picker
            colorPicker0.setLabel("New Color for Faces");
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }

    // ------------------------------------------------------------------------------
    // Callback Name: dialogShown
    // This callback is executed just before the dialog launch. Thus any value
    // set
    // here will take precedence and dialog will be launched showing that value.
    // ------------------------------------------------------------------------------
    public void dialogShown() throws NXException, RemoteException {
        try {
            // ---- Enter your callback code here -----
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }

    // ------------------------------------------------------------------------------
    // Callback Name: apply
    // Following callback is associated with the "theDialog" Block.
    // ------------------------------------------------------------------------------
    public int apply() throws NXException, RemoteException {
        int errorCode = 0;
        try {
            this.modifyColorOfFaces(this.getSelectedFaces(), this.getSelectedColor());
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            errorCode = 1;
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return errorCode;
    }

    // ------------------------------------------------------------------------------
    // Callback Name: update
    // Following callback is associated with the "theDialog" Block.
    // ------------------------------------------------------------------------------
    public int update(nxopen.blockstyler.UIBlock block) throws NXException, RemoteException {
        try {
            if (block == face_select0) {
                // ---------Enter your code here-----------
            } else if (block == colorPicker0) {
                // ---------Enter your code here-----------
            }
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return 0;
    }

    // ------------------------------------------------------------------------------
    // Callback Name: ok
    // ------------------------------------------------------------------------------
    public int ok() throws NXException, RemoteException {
        int errorCode = 0;
        try {
            // ---- Enter your callback code here -----
            errorCode = apply();
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            errorCode = 1;
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return errorCode;
    }

    // ------------------------------------------------------------------------------
    // Callback Name: cancel
    // Following callback is associated with the "theDialog" Block.
    // ------------------------------------------------------------------------------
    public int cancel() throws NXException, RemoteException {
        try {
            // ---- Enter your callback code here -----
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return 0;
    }

    // ------------------------------------------------------------------------------
    // Callback Name: filter
    // Following callback is associated with the "theDialog" Block.
    // ------------------------------------------------------------------------------
    public int filter(nxopen.blockstyler.UIBlock block, nxopen.TaggedObject selectedObject)
            throws NXException, RemoteException {
        return (nxopen.uf.UFConstants.UF_UI_SEL_ACCEPT);
    }

    // ------------------------------------------------------------------------------
    // Callback Name: focusNotify
    // This callback is executed when any block (except the ones which receive
    // keyboard entry such as Integer block) receives focus.
    // ------------------------------------------------------------------------------
    public void focusNotify(nxopen.blockstyler.UIBlock block, boolean focus) throws NXException, RemoteException {
        try {
            // ---- Enter your callback code here -----
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }

    // ------------------------------------------------------------------------------
    // Callback Name: keyboardFocusNotify
    // This callback is executed when block which can receive keyboard entry,
    // receives the focus.
    // ------------------------------------------------------------------------------
    public void keyboardFocusNotify(nxopen.blockstyler.UIBlock block, boolean focus)
            throws NXException, RemoteException {
        try {
            // ---- Enter your callback code here -----
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
    }

    // ------------------------------------------------------------------------------
    // Callback Name: enableOKButton
    // This callback allows the dialog to enable/disable the OK and Apply
    // button.
    // ------------------------------------------------------------------------------
    public boolean enableOKButton() throws NXException, RemoteException {
        try {
            // ---- Enter your callback code here -----
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return true;
    }

    // ------------------------------------------------------------------------------
    // Function Name: GetBlockProperties
    // ------------------------------------------------------------------------------
    public PropertyList getBlockProperties(String blockID) throws NXException, RemoteException {
        PropertyList plist = null;
        try {
            plist = theDialog.getBlockProperties(blockID);
        } catch (Exception ex) {
            // ---- Enter your exception handling code here -----
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        return plist;
    }

    private int getSelectedColor() throws NXException, RemoteException {
        return this.colorPicker0.getValue()[0];
    }

    private nxopen.Face[] getSelectedFaces() throws NXException, RemoteException {
        List<nxopen.Face> faces = new ArrayList<nxopen.Face>();
        try {
            TaggedObject[] objects = this.face_select0.getSelectedObjects();
            for (TaggedObject obj : objects) {
                if (obj instanceof Face) {
                    faces.add((Face) obj);
                }
            }
        } catch (Exception ex) {
            theUI.nxmessageBox().show("Block Styler", nxopen.NXMessageBox.DialogType.ERROR, ex.getMessage());
        }
        Face[] faceArray = new Face[0];
        return faces.toArray(faceArray);
    }

    // Define the allowed face rules for FaceRules in the Face Collector
    // control.
    // Use the Python bitwise operator to combine the desired face rule values,
    // then set the FaceRules property of the Face Collector to the result.
    // Documentation explaining the different rules is in the Selecting objects
    // section of the Fundamentals chapter of the NX Help Documentation.
    private int specifyFaceRules() {
        int face_rules = 0x1; // Single Face - Required
        face_rules |= 0x40; // Adjacent Faces
        // face_rules |= 0x100; // All Blend Faces
        face_rules |= 0x10; // Body Faces
        face_rules |= 0x800; // Boss and Pocket Faces
        // face_rules |= 0x80; // Connected Blend Faces
        face_rules |= 0x4000; // Face and Adjacent Faces
        face_rules |= 0x20; // Feature Faces
        // face_rules |= 0x1000; // Merged Rib Faces
        // face_rules |= 0x2000; // Region Boundary Faces
        face_rules |= 0x2; // Region Faces
        face_rules |= 0x200; // Rib Faces
        face_rules |= 0x400; // Slot Faces
        face_rules |= 0x4; // Tangent Faces
        face_rules |= 0x8; // Tangent Region Faces
        return face_rules;
    }

    // Pick one of the allowed face rules from SpecifyFaceRules
    // to be the default face rule. It is an enum so it has to be
    // set as the string value of the enum.
    private String defaultFaceRules() {
        String default_face_rules;
        // default_face_rules = "Single Face";
        // default_face_rules = "Adjacent Faces";
        // default_face_rules = "All Blend Faces";
        // default_face_rules = "Body Faces";
        // default_face_rules = "Boss and Pocket Faces";
        // default_face_rules = "Connected Blend Faces";
        // default_face_rules = "Face and Adjacent Faces";
        // default_face_rules = "Feature Faces";
        // default_face_rules = "Merged Rib Faces";
        // default_face_rules = "Region Boundary Faces";
        // default_face_rules = "Region Faces";
        // default_face_rules = "Rib Faces";
        // default_face_rules = "Slot Faces";
        default_face_rules = "Tangent Faces";
        // default_face_rules = "Tangent Region Faces";
        return default_face_rules;
    }

    // Define the allowed entities for EntityType in the Face Collector control.
    // Use the Python bitwise operator to combine the desired Entity Type
    // values,
    // then set the EntityType property of the Face Collector to the result.
    private int specifyEntityType() {
        int entity_type = 0;
        entity_type |= 0x10; // Allow Faces
        entity_type |= 0x20; // Allow Datums
        entity_type |= 0x40; // Allow Bodies
        return entity_type;
    }

    // Modify the color of the input faces using a DisplayModification object
    // from
    // the DisplayManager of the NX Session.
    private void modifyColorOfFaces(nxopen.Face[] faces, int color) throws NXException, RemoteException {
        if (faces.length > 0) {
            nxopen.DisplayModification dispMod = theSession.displayManager().newDisplayModification();
            dispMod.setNewColor(color);
            dispMod.apply(faces);
            dispMod.dispose();
        }
    }

}
