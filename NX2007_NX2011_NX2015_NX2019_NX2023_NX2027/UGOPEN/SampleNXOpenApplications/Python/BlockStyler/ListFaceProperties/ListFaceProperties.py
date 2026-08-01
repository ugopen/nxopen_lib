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
class ListFaceProperties(object):
    # static class members
    theSession = None
    theUI = None

    FaceTypeUserNames = {
        16 : 'cylinder', 17 : 'cone', 18 : 'sphere', 19 : 'revolved (toroidal)', 20 : 'extruded',
        22 : 'bounded plane', 23 : 'fillet (blend)', 43 : 'b-surface', 65 : 'offset surface',
        66 : 'foreign surface', 67 : 'convergent surface'
        }
     
    #------------------------------------------------------------------------------
    # Constructor for NX Styler class
    #------------------------------------------------------------------------------
    def __init__(self):
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.ufs = NXOpen.UF.UFSession.GetUFSession()
            self.theDlxFileName = "ListFaceProperties.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddFilterHandler(self.filter_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
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
            self.button0 = self.theDialog.TopBlock.FindBlock("button0")
            self.list_box0 = self.theDialog.TopBlock.FindBlock("list_box0")
            #------------------------------------------------------------------------------
            # Registration of ListBox specific callbacks
            #------------------------------------------------------------------------------
            # self.list_box0.SetAddHandler(self.AddCallback)
            # self.list_box0.SetDeleteHandler(self.DeleteCallback)
            #------------------------------------------------------------------------------

            self.theDialog.TopBlock.Label = "List Face Properties"
            self.group0.Label = "Face Properties"
            self.button0.Label = "Clear Selection"

            # Face Collector Options

            self.face_select0.AllowConvergentObject = False  # Do not allow selecting convergent faces
            # Setting the Maximum Scope defines the maximum scope that is available for
            # selection. It determines the options to be populated in the Selection Scope 
            # list in the Top Border Bar in NX. The user may select one of the options in
            # this list to further restrict the Selection Scope.
            self.face_select0.MaximumScopeAsString = "Entire Assembly"
            #self.face_select0.MaximumScopeAsString = "Within Work Part and Components"
            #self.face_select0.MaximumScopeAsString = "Within Work Part Only"
            self.face_select0.FaceRules = self.SpecifyFaceRules()
            self.face_select0.EntityType = self.SpecifyEntityType()
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
            if block == self.face_select0:
                list_info = []
                objs = self.GetSelectedObjects()
                for obj in objs:
                    if isinstance(obj, NXOpen.DatumPlane):
                        list_info.extend(self.GetDatumInfo(obj))
                    elif isinstance(obj, NXOpen.Face):
                        list_info.extend(self.GetFaceInfo(obj))
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
    # Callback Name: filter_cb
    #------------------------------------------------------------------------------
    def filter_cb(self, block, selectedObject):
        return NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
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
        selObjs = []
        self.face_select0.SetSelectedObjects(selObjs)
        info = []
        self.list_box0.SetListItems(info)
        
    def GetSelectedObjects(self):
        try:
            return self.face_select0.GetSelectedObjects()
        except Exception as ex:
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return []

    def GetDatumInfo(self, datum):
        info = []
        info.append("Datum tag is {0:d}".format(datum.Tag))
        info.append("")
        return info
            
    def GetFaceInfo(self, face):
        info = []
        faceType, point, dirInfo, box, radius, rad_data, norm_dir = self.ufs.Modeling.AskFaceData(face.Tag)
        info.append("Face tag is {0:d}".format(face.Tag))
        info.append("Face type is {0}".format(self.GetFaceTypeString(faceType)))
        info.append("Direction information is {0}".format(dirInfo))
        info.append("Face boundary is {0}".format(box))
        info.append("Radius is {0:g}".format(radius))
        info.append("")
        return info

    def GetFaceTypeString(self, face_type):
        type_string = ListFaceProperties.FaceTypeUserNames[face_type]
        if not type_string:
            type_string = "unknown face type"
        return type_string

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
        #face_rules |= 0x4000  # Face and Adjacent Faces
        face_rules |= 0x20    # Feature Faces
        #face_rules |= 0x1000  # Merged Rib Faces
        #face_rules |= 0x2000  # Region Boundary Faces
        face_rules |= 0x2     # Region Faces
        face_rules |= 0x200   # Rib Faces
        face_rules |= 0x400   # Slot Faces
        face_rules |= 0x4     # Tangent Faces
        face_rules |= 0x8     # Tangent Region Faces
        return face_rules

    # Define the allowed entities for EntityType in the Face Collector control.
    # Use the Python bitwise operator to combine the desired Entity Type values,
    # then set the EntityType property of the Face Collector to the result.
    def SpecifyEntityType(self):
        entity_type = 0
        entity_type |= 0x10  # Allow Faces
        entity_type |= 0x20  # Allow Datums
        entity_type |= 0x40  # Allow Bodies
        return entity_type

def main():
    theListFaceProperties = None
    try:
        theListFaceProperties =  ListFaceProperties()
        #  The following method shows the dialog immediately
        theListFaceProperties.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theListFaceProperties != None:
            theListFaceProperties.Dispose()
            theListFaceProperties = None
    
if __name__ == '__main__':
    main()

