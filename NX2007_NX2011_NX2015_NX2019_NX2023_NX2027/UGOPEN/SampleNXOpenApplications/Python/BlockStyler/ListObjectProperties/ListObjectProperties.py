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
class ListObjectProperties(object):
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
            self.ufs = NXOpen.UF.UFSession.GetUFSession()
            self.theDlxFileName = "ListObjectProperties.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddCloseHandler(self.close_cb)
            self.theDialog.AddFilterHandler(self.filter_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddFocusNotifyHandler(self.focusNotify_cb)
            self.theDialog.AddKeyboardFocusNotifyHandler(self.keyboardFocusNotify_cb)
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
            self.selection0 = self.theDialog.TopBlock.FindBlock("selection0")
            self.button0 = self.theDialog.TopBlock.FindBlock("button0")
            self.list_box0 = self.theDialog.TopBlock.FindBlock("list_box0")
            #------------------------------------------------------------------------------
            # Registration of ListBox specific callbacks
            #------------------------------------------------------------------------------
            # self.list_box0.SetAddHandler(self.AddCallback)
            # self.list_box0.SetDeleteHandler(self.DeleteCallback)
            #------------------------------------------------------------------------------
            self.theDialog.TopBlock.Label = "List Object Properties"
            self.group0.Label = "Object Properties"
            self.button0.Label = "Clear Selection"

            # Set Select Object (selection0) Properties

            # Block Specific Properties
            self.selection0.AllowConvergentObject = False
            self.selection0.AutomaticProgression = False
            self.selection0.BalloonTooltipLayoutAsString = "Horizontal"
            self.selection0.BalloonTooltipLayoutAsString = "Vertical"
            self.selection0.BalloonTooltipText = \
                "Select objects to list their properties. You can apply selection filters to narrow the type of objects that can be selected."
            self.selection0.BlendVirtualCurveOverlay = False
            self.selection0.CreateInterpartLink = False
            self.selection0.Cue = "Select object to list its properties in the list box."
            # Setting the Maximum Scope defines the maximum scope that is available for
            # selection. It determines the options to be populated in the Selection Scope 
            # list in the Top Border Bar in NX. The user may select one of the options in
            # this list to further restrict the Selection Scope.
            self.selection0.MaximumScopeAsString = "Entire Assembly"
            #self.selection0.MaximumScopeAsString = "Within Work Part and Components"
            #self.selection0.MaximumScopeAsString = "Within Work Part Only"
            #self.selection0.SelectModeAsString = "Single"
            self.selection0.SelectModeAsString = "Multiple"
            if self.selection0.SelectModeAsString == "Single":
                self.selection0.LabelString = "Select Object"
            else:
                self.selection0.LabelString = "Select Objects"
            self.selection0.ToolTip = "List properties of selected objects."
            
            # Uncomment the following section and edit GetSelectionFilterMaskTriples to
            # use the mask triples to specify selecting only your desired object types.
            # ClearAndEnableSpecific clears the global selection list and sets the 
            # filter to the specified ones
            #maskAction = NXOpen.Selection.SelectionAction.ClearAndEnableSpecific
            # EnableSpecific just sets the filter to the specified one without 
            # clearing the global selection list.
            #maskAction = NXOpen.Selection.SelectionAction.EnableSpecific
            #maskTriples = self.GetSelectionFilterMaskTriples()
            #self.selection0.SetSelectionFilter(maskAction, maskTriples)
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
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
    
    #------------------------------------------------------------------------------
    # Callback Name: update_cb
    #------------------------------------------------------------------------------
    def update_cb(self, block):
        try:
            if block == self.selection0:
                list_info = []
                objects = self.GetSelectedObjects()
                if len(objects) > 10:
                    list_info.append("Number of selected objects is {0:d}".format(len(objects)))
                    list_info.append("")
                else:
                    for obj in objects:
                        list_info.extend(self.GetObjectInfo(obj))
                self.list_box0.SetListItems(list_info)
            elif block == self.button0:
                self.ClearDialog()
            elif block == self.list_box0:
                pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return 0
    
    #------------------------------------------------------------------------------
    # Callback Name: close_cb
    #------------------------------------------------------------------------------
    def close_cb(self):
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
    # ListBox specific callbacks
    #------------------------------------------------------------------------------
    # def AddCallback (self list_box):
    #     # ---- Enter your callback code here -----
    #     pass
    
    # def DeleteCallback(self, list_box):
    #     # ---- Enter your callback code here -----
    #     pass
    
    #------------------------------------------------------------------------------
    
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
        
    def ClearDialog(self):
        """
        Clears the collector and the list box by calling the set methods with empty lists. 
        """
        selObjs = []
        self.selection0.SetSelectedObjects(selObjs)
        info = []
        self.list_box0.SetListItems(info)
    
    def GetSelectionFilterMaskTriples(self):
        mask_triples = []
        # Special selection subtype
        obj_all_subtypes = NXOpen.UF.UFConstants.UF_all_subtype
        
        # Example selection filter mask types for points
        # Point object types
        #obj_type = NXOpen.UF.UFConstants.UF_point_type

        # Example selection filter mask types for components
        #obj_type = NXOpen.UF.UFConstants.UF_component_type
        # Component object subtypes
        #obj_subtype = NXOpen.UF.UFConstants.UF_component_subtype
        #obj_subtype = NXOpen.UF.UFConstants.UF_part_occurrence_subtype
        #obj_subtype = NXOpen.UF.UFConstants.UF_shadow_part_occ_subtype
        #obj_subtype = NXOpen.UF.UFConstants.UF_design_element_search_result_subtype
        # Detail subtype (SolidBodySubtype) only used for a select set 
        # of object types such as solid geometry, and FE nodes and elements
        obj_detail_subtype = 0
        
        # Add selection mask triple for all point type and subtypes
        obj_type = NXOpen.UF.UFConstants.UF_point_type
        obj_subtype = NXOpen.UF.UFConstants.UF_all_subtype
        mask_triples.append(NXOpen.Selection.MaskTriple(obj_type, obj_subtype, obj_detail_subtype))
        
        # Add selection mask triple for all directions
        obj_type = NXOpen.UF.UFConstants.UF_direction_type
        obj_subtype = NXOpen.UF.UFConstants.UF_part_occurrence_subtype
        mask_triples.append(NXOpen.Selection.MaskTriple(obj_type, obj_subtype, obj_detail_subtype))
        
        # Add selection mask triple for all occurrence instances
        obj_type = NXOpen.UF.UFConstants.UF_occ_instance_type
        obj_subtype = NXOpen.UF.UFConstants.UF_occ_instance_subtype
        mask_triples.append(NXOpen.Selection.MaskTriple(obj_type, obj_subtype, obj_detail_subtype))
        return mask_triples
        
    def GetSelectedObjects(self):
        try:
            return self.selection0.GetSelectedObjects()
        except Exception as ex:
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return []
    
    def GetObjectInfo(self, obj):
        info = []
        info.append("Object tag is {}".format(obj.Tag))
        obj_name = obj.Name
        if obj_name is not None and len(obj_name) > 0:
            info.append("Object name is {}".format(obj_name))
        info.append("Object Class {}".format(type(obj)))
        obj_type, obj_subtype = self.ufs.Obj.AskTypeAndSubtype(obj.Tag)
        info.append("Object type is {}, subtype is {}".format(obj_type, obj_subtype))
        info.append("")
        return info
        
        
def main():
    theListObjectProperties = None
    try:
        theListObjectProperties =  ListObjectProperties()
        #  The following method shows the dialog immediately
        theListObjectProperties.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theListObjectProperties != None:
            theListObjectProperties.Dispose()
            theListObjectProperties = None
    
if __name__ == '__main__':
    main()

