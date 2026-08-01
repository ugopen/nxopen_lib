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
class ListComponentProperties(object):
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
            self.theDlxFileName = "ListObjectProperties.dlx"
            self.ufs = NXOpen.UF.UFSession.GetUFSession()
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
            self.theDialog.TopBlock.Label = "List Component Properties"
            self.group0.Label = "Component Properties"
            self.button0.Label = "Clear Selection"
            
            #self.selection0.SelectModeAsString = "Single"
            #self.selection0.LabelString = "Select Component"
            self.selection0.SelectModeAsString = "Multiple"
            self.selection0.LabelString = "Select Components"
            
            self.selection0.MaximumScopeAsString = "Entire Assembly"
            #self.selection0.MaximumScopeAsString = "Within Work Part and Components"
            #self.selection0.MaximumScopeAsString = "Within Work Part Only"
            
            # Use component mask triples in GetSelectionFilterMaskTriples to 
            # filter the selection to components.
            maskAction = NXOpen.Selection.SelectionAction.ClearAndEnableSpecific
            #maskAction = NXOpen.Selection.SelectionAction.EnableSpecific
            maskTriples = self.GetSelectionFilterMaskTriples()
            self.selection0.SetSelectionFilter(maskAction, maskTriples)
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
                components = self.GetSelectedComponents()
                for component in components:
                    list_info.extend(self.GetComponentInfo(component))
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
    # 
    # 
    
    # def DeleteCallback(self, list_box):
    # 
    # 
    
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
        """
        Returns an array of mask triples, set to the values for components and 
        various types of part occurrences. Design element search results are also
        included for installations running 4GD.
        """
        mask_triples = []
        # Assembly object types
        #obj_type = NXOpen.UF.UFConstants.UF_component_type
        # Assembly object subtypes
        #obj_subtype = NXOpen.UF.UFConstants.UF_component_subtype
        #obj_subtype = NXOpen.UF.UFConstants.UF_part_occurrence_subtype
        #obj_subtype = NXOpen.UF.UFConstants.UF_shadow_part_occ_subtype
        #obj_subtype = NXOpen.UF.UFConstants.UF_design_element_search_result_subtype
        # Detail subtype (SolidBodySubtype) not used in assembly
        obj_detail_subtype = 0
        
        obj_type = NXOpen.UF.UFConstants.UF_component_type
        
        # Add selection mask triple for components
        obj_subtype = NXOpen.UF.UFConstants.UF_component_subtype
        mask_triples.append(NXOpen.Selection.MaskTriple(obj_type, obj_subtype, obj_detail_subtype))

        # Add selection mask triple for part occurrences
        obj_subtype = NXOpen.UF.UFConstants.UF_part_occurrence_subtype
        mask_triples.append(NXOpen.Selection.MaskTriple(obj_type, obj_subtype, obj_detail_subtype))

        # Add selection mask triple for shadow part occurrences
        obj_subtype = NXOpen.UF.UFConstants.UF_shadow_part_occ_subtype
        mask_triples.append(NXOpen.Selection.MaskTriple(obj_type, obj_subtype, obj_detail_subtype))
        
        # Add selection mask triple for design element search results
        obj_subtype = NXOpen.UF.UFConstants.UF_design_element_search_result_subtype
        mask_triples.append(NXOpen.Selection.MaskTriple(obj_type, obj_subtype, obj_detail_subtype))

        return mask_triples
        
    def GetSelectedComponents(self):
        try:
            return self.selection0.GetSelectedObjects()
        except Exception as ex:
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return []
    
    def GetComponentInfo(self, component):
        info = []
        # NX Open Python methods that have multiple output parameters, or a result value plus one or more
        # output parameters, return those parameters as a tuple. In Python, you can assign another tuple
        # containing the same number of parameters to the tuple containing the return and output parameters
        # of the method you are calling. So for the GetPosition method below, the return tuple contains the 
        # position vector as an NXOpen.Point3d structure and the orientation matrix as an NXOpen.Matrix3x3 
        # structure. Setting that return tuple to the tuple "pt, mtx" will automatically assign the position 
        # NXOpen.Point3d structure to the variable, "pt", and likewise for the orientation matrix.
        pt, mtx = component.GetPosition()
        info.append("Component name is {}".format(component.DisplayName))
        info.append("Component reference set is {}".format(component.ReferenceSet))
        info.append("  Entire part refset is {}".format(component.EntirePartRefsetName))
        info.append("  Empty part refset is {}".format(component.EmptyPartRefsetName))
        info.append("Component is fixed: {}".format(component.IsFixed))
        info.append("Component is suppressed: {}".format(component.IsSuppressed))
        info.append("Component origin is [{}, {}, {}]".format(pt.X, pt.Y, pt.Z))
        info.append("Component orientation is")
        info.append("   [({}, {}, {})".format(mtx.Xx, mtx.Xy, mtx.Xz))
        info.append("    ({}, {}, {})".format(mtx.Yx, mtx.Yy, mtx.Yz))
        info.append("    ({}, {}, {})]".format(mtx.Zx, mtx.Zy, mtx.Zz))
        info.append("Number of first level children is {}".format(len(component.GetChildren())))
        # Example code accessing a query method from NX Open UF Assembly API
        #part_name, refset_name, instance_name, origin, csys_matrix, transform = self.ufs.Assem.AskComponentData(component.Tag)
        #info.append("Component info from NXOpen.UF.UFAssem.AskComponentData")
        #info.append("  Component tag is {}".format(component.Tag))
        #info.append("  Component part_name is {}".format(part_name))
        #info.append("  Component refset_name is {}".format(refset_name))
        #info.append("  Component instance_name is {}".format(instance_name))
        #info.append("  Component origin is {}".format(origin))
        #info.append("  Component csys_matrix is {}".format(csys_matrix))
        #info.append("  Component transform is {}".format(transform))
        info.append("")
        return info
    
def main():
    theListComponentProperties = None
    try:
        theListComponentProperties =  ListComponentProperties()
        #  The following method shows the dialog immediately
        theListComponentProperties.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theListComponentProperties != None:
            theListComponentProperties.Dispose()
            theListComponentProperties = None
    
if __name__ == '__main__':
    main()


