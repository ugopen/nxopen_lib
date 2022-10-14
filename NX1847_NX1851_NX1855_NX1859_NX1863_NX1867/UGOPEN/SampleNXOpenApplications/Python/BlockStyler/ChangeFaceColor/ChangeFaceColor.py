#==============================================================================
#
#      Copyright (c) 2016 Siemens Product Lifecycle Management Software Inc. 
#                          All Rights Reserved.
#
#==============================================================================
#File description: Sample NX/Open Application for Block Styler
#==============================================================================
#
#==============================================================================
#   WARNING!!  This file is overwritten by the Block UI Styler while generating
#   the automation code. Any modifications to this file will be lost after
#   generating the code again.
# 
#==============================================================================

import NXOpen
import NXOpen.BlockStyler
import NXOpen.UF

#------------------------------------------------------------------------------
# Represents Block Styler application cls
#------------------------------------------------------------------------------
class ChangeFaceColor:
    # static class members
    theSession = None
    theUI = None
    
    #------------------------------------------------------------------------------
    # Constructor for NX Styler class
    #------------------------------------------------------------------------------
    def __init__(self):
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.theDlxFileName = "ChangeFaceColor.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddCancelHandler(self.cancel_cb)
            self.theDialog.AddFilterHandler(self.filter_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddFocusNotifyHandler(self.focusNotify_cb)
            self.theDialog.AddKeyboardFocusNotifyHandler(self.keyboardFocusNotify_cb)
            self.theDialog.AddEnableOKButtonHandler(self.enableOKButton_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            raise ex
        
    
    # ------------------------------- DIALOG LAUNCHING ---------------------------------
    # 
    #     Before invoking this application one needs to open any part/empty part in NX
    #     because of the behavior of the blocks.
    # 
    #     Make sure the dlx file is in one of the following locations:
    #         1.) From where NX session is launched
    #         2.) $UGII_USER_DIR/application
    #         3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    #             recommended. This variable is set to a full directory path to a file 
    #             containing a list of root directories for all custom applications.
    #             e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
    # 
    #     You can create the dialog using one of the following way:
    # 
    #     1. Journal Replay
    # 
    #         1) Replay this file through Tool->Journal->Play Menu.
    # 
    #     2. USER EXIT
    # 
    #         1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    #         2) Invoke the Shared Library through File->Execute->NX Open menu.
    # 
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # This method shows the dialog on the screen
    #------------------------------------------------------------------------------
    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    
    #------------------------------------------------------------------------------
    # Method Name: Dispose
    #------------------------------------------------------------------------------
    def Dispose(self):
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None
    
    #------------------------------------------------------------------------------
    # ---------------------Block UI Styler Callback Functions--------------------------
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # Callback Name: initialize_cb
    #------------------------------------------------------------------------------
    def initialize_cb(self):
        try:
            self.group0 = self.theDialog.TopBlock.FindBlock("group0")
            self.face_select0 = self.theDialog.TopBlock.FindBlock("face_select0")
            self.colorPicker0 = self.theDialog.TopBlock.FindBlock("colorPicker0")

            self.theDialog.TopBlock.Label = "Change Face Color"
            self.group0.Label = "Input Parameters"

            # Block Specific Properties for the Face Collector
            self.face_select0.AllowConvergentObject = True  
            self.face_select0.AutomaticProgression = False
            self.face_select0.BalloonTooltipText = \
                "Select the faces that you want to change the color. Use the Face Rules on the Top Border Bar to control the selection intent rules."
            self.face_select0.BlendVirtualCurveOverlay = False
            self.face_select0.CreateInterpartLink = False
            self.face_select0.InterpartSelectionAsString = "Simple"
            #self.face_select0.InterpartSelectionAsString = "Non-associative Interpart Copy Only"
            #self.face_select0.InterpartSelectionAsString = "Associative and Non-associative Interpart Copy"
            #self.face_select0.InterpartSelectionAsString = "Associative Interpart Copy"
            # Setting the Maximum Scope defines the maximum scope that is available for
            # selection. It determines the options to be populated in the Selection Scope 
            # list in the Top Border Bar in NX. The user may select one of the options in
            # this list to further restrict the Selection Scope.
            self.face_select0.MaximumScopeAsString = "Entire Assembly"
            #self.face_select0.MaximumScopeAsString = "Within Work Part and Components"
            #self.face_select0.MaximumScopeAsString = "Within Work Part Only"
            #self.face_select0.SelectModeAsString = "Single"
            self.face_select0.SelectModeAsString = "Multiple"
            
            # Selection Intent Properties for the Face Collector
            self.face_select0.FaceRules = self.SpecifyFaceRules()
            self.face_select0.EntityType = self.SpecifyEntityType()
            self.face_select0.DefaultFaceRulesAsString = self.DefaultFaceRules()
            self.face_select0.PopupMenuEnabled = True
            
            # Block Specific Properties for the Object Color Picker
            self.colorPicker0.NumberSelectable = 1
            self.colorPicker0.SetValue([1])
            self.colorPicker0.BalloonTooltipText = "Pick the new color for the selected faces."
            
            # General Properties for the Object Color Picker
            self.colorPicker0.Label = "New Color for Faces"
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    
    #------------------------------------------------------------------------------
    # Callback Name: dialogShown_cb
    # This callback is executed just before the dialog launch. Thus any value set 
    # here will take precedence and dialog will be launched showing that value. 
    #------------------------------------------------------------------------------
    def dialogShown_cb(self):
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    
    #------------------------------------------------------------------------------
    # Callback Name: apply_cb
    #------------------------------------------------------------------------------
    def apply_cb(self):
        errorCode = 0
        try:
            self.ModifyColorOfFaces(self.GetSelectedFaces(), self.GetSelectedColor())
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return errorCode
    
    #------------------------------------------------------------------------------
    # Callback Name: update_cb
    #------------------------------------------------------------------------------
    def update_cb(self, block):
        try:
            if block == self.face_select0:
                # ---- Enter your code here -----
                pass
            elif block == self.colorPicker0:
                # ---- Enter your code here -----
                pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return 0
    
    #------------------------------------------------------------------------------
    # Callback Name: ok_cb
    #------------------------------------------------------------------------------
    def ok_cb(self):
        errorCode = 0
        try:
            # ---- Enter your callback code here -----
            errorCode = self.apply_cb()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return errorCode
    
    
    #------------------------------------------------------------------------------
    # Callback Name: cancel_cb
    #------------------------------------------------------------------------------
    def cancel_cb(self):
        errorCode = 0
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return errorCode
    
    #------------------------------------------------------------------------------
    # Callback Name: filter_cb
    #------------------------------------------------------------------------------
    def filter_cb(self, block, selectedObject):
        return NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
    
    #------------------------------------------------------------------------------
    # Callback Name: focusNotify_cb
    # This callback is executed when any block (except the ones which receive keyboard entry such  Integer block) receives focus.
    #------------------------------------------------------------------------------
    def focusNotify_cb(self, block,  focus):
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    
    #------------------------------------------------------------------------------
    # Callback Name: keyboardFocusNotify_cb
    # This callback is executed when block which can receive keyboard entry, receives the focus.
    #------------------------------------------------------------------------------
    def keyboardFocusNotify_cb(self, block,  focus):
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    
    #------------------------------------------------------------------------------
    # Callback Name: enableOKButton_cb
    # This callback allows the dialog to enable/disable the OK and Apply button.
    #------------------------------------------------------------------------------
    def enableOKButton_cb(self):
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return True
    
    #------------------------------------------------------------------------------
    # Function Name: GetBlockProperties
    # Returns the propertylist of the specified BlockID
    #------------------------------------------------------------------------------
    def GetBlockProperties(self, blockID):
        try:
            return self.theDialog.GetBlockProperties(blockID)
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return None
        
    def GetSelectedColor(self):
        return self.colorPicker0.GetValue()[0]
        
    def GetSelectedFaces(self):
        faces = []
        try:
            objects = self.face_select0.GetSelectedObjects()
            for obj in objects:
                if isinstance(obj, NXOpen.Face):
                    faces.append(obj)
        except Exception as ex:
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return faces

    # Define the allowed face rules for FaceRules in the Face Collector control.
    # Use the Python bitwise operator to combine the desired face rule values,
    # then set the FaceRules property of the Face Collector to the result.
    # Documentation explaining the different rules is in the Selecting objects 
    # section of the Fundamentals chapter of the NX Help Documentation.
    def SpecifyFaceRules(self):
        face_rules  = 0x1     # Single Face - Required
        face_rules |= 0x40    # Adjacent Faces
        #face_rules |= 0x100   # All Blend Faces
        face_rules |= 0x10    # Body Faces
        face_rules |= 0x800   # Boss and Pocket Faces
        #face_rules |= 0x80    # Connected Blend Faces
        face_rules |= 0x4000  # Face and Adjacent Faces
        face_rules |= 0x20    # Feature Faces
        #face_rules |= 0x1000  # Merged Rib Faces
        #face_rules |= 0x2000  # Region Boundary Faces
        face_rules |= 0x2     # Region Faces
        face_rules |= 0x200   # Rib Faces
        face_rules |= 0x400   # Slot Faces
        face_rules |= 0x4     # Tangent Faces
        face_rules |= 0x8     # Tangent Region Faces
        return face_rules

    # Pick one of the allowed face rules from SpecifyFaceRules
    # to be the default face rule. It is an enum so it has to be
    # set as the string value of the enum.
    def DefaultFaceRules(self):
        #default_face_rules  = "Single Face"
        #default_face_rules = "Adjacent Faces"
        #default_face_rules = "All Blend Faces"
        #default_face_rules = "Body Faces"
        #default_face_rules = "Boss and Pocket Faces"
        #default_face_rules = "Connected Blend Faces"
        #default_face_rules = "Face and Adjacent Faces"
        #default_face_rules = "Feature Faces"
        #default_face_rules = "Merged Rib Faces"
        #default_face_rules = "Region Boundary Faces"
        #default_face_rules = "Region Faces"
        #default_face_rules = "Rib Faces"
        #default_face_rules = "Slot Faces"
        default_face_rules = "Tangent Faces"
        #default_face_rules = "Tangent Region Faces"
        return default_face_rules

    # Define the allowed entities for EntityType in the Face Collector control.
    # Use the Python bitwise operator to combine the desired Entity Type values,
    # then set the EntityType property of the Face Collector to the result.
    def SpecifyEntityType(self):
        entity_type = 0
        entity_type |= 0x10  # Allow Faces
        entity_type |= 0x20  # Allow Datums
        entity_type |= 0x40  # Allow Bodies
        return entity_type

    # Modify the color of the input faces using a DisplayModification object from
    # the DisplayManager of the NX Session. 
    def ModifyColorOfFaces(self, faces, color):
        if len(faces) > 0:
            dispMod = self.theSession.DisplayManager.NewDisplayModification()
            dispMod.NewColor = color
            dispMod.Apply(faces)
            dispMod.Dispose()
    
def main():
    theChangeFaceColor = None
    try:
        theChangeFaceColor =  ChangeFaceColor()
        #  The following method shows the dialog immediately
        theChangeFaceColor.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theChangeFaceColor != None:
            theChangeFaceColor.Dispose()
            theChangeFaceColor = None
    
if __name__ == '__main__':
    main()

