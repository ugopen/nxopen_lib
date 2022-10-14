#=============================================================================
#
#      Copyright 2013 Siemens Product Lifecycle Management Software Inc. 
#                          All Rights Reserved.
#
#===============================================================================
#File description: Sample NX/Open Application for Block Styler
#===============================================================================
#

#==============================================================================
#  WARNING!!  This file is overwritten by the Block Styler while generating
#  the automation code. Any modifications to this file will be lost after
#  generating the code again.
#==============================================================================
#------------------------------------------------------------------------------
# These imports are needed for the following template code
#------------------------------------------------------------------------------
import os.path
import sys
import traceback
import NXOpen
import NXOpen.BlockStyler

#------------------------------------------------------------------------------
# Represents Block Styler application class
#------------------------------------------------------------------------------
class EditExpression(object):

    #------------------------------------------------------------------------------
    # Constructor for NX Styler class
    #------------------------------------------------------------------------------
    def __init__(self):
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.theDialogName = "EditExpression.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDialogName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)
            self.GroupFeatureSelection = None # Block type: Group
            self.FeatureList = None # Block type: Set List
            self.GroupExpressionList = None # Block type: Group
            self.ButtonGetExpressions = None # Block type: Button
            self.ExpressionList = None # Block type: List Box
            self.GroupExpression = None # Block type: Group
            self.ExpressionName = None # Block type: String
            self.ExpressionValue = None # Block type: Double
            self.newBlock = None
            self.newFeatCol = [None] # NXOpen.TaggedObject list
            self.workPart = None
            self.expToEdit = None

        except Exception as ex:
            print(ex)

    #------------------------------------------------------------------------------
    # This method shows the dialog on the screen
    #------------------------------------------------------------------------------
    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            traceback.print_exc()

    #------------------------------------------------------------------------------
    # Method Name: Dispose
    #------------------------------------------------------------------------------
    def Dispose(self):
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None

    #------------------------------------------------------------------------------
    #---------------------Block Styler Callback Functions--------------------------
    #------------------------------------------------------------------------------

    #------------------------------------------------------------------------------
    # Callback Name: initialize_cb
    #------------------------------------------------------------------------------
    def initialize_cb(self):
        try:
            self.workPart = self.theSession.Parts.Work
            self.GroupFeatureSelection = self.theDialog.TopBlock.FindBlock("GroupFeatureSelection")
            self.FeatureList = self.theDialog.TopBlock.FindBlock("FeatureList")
            self.GroupExpressionList = self.theDialog.TopBlock.FindBlock("GroupExpressionList")
            self.ButtonGetExpressions = self.theDialog.TopBlock.FindBlock("ButtonGetExpressions")
            self.ExpressionList = self.theDialog.TopBlock.FindBlock("ExpressionList")
            self.GroupExpression = self.theDialog.TopBlock.FindBlock("GroupExpression")
            self.ExpressionName = self.theDialog.TopBlock.FindBlock("ExpressionName")
            self.ExpressionValue = self.theDialog.TopBlock.FindBlock("ExpressionValue")
            #user defined code
            self.newBlock = self.FeatureList.AddNewSet(True)
            self.FeatureList.SetAddHandler(self.add_handler)
            self.FeatureList.SetDeleteHandler(self.delete_handler)
            self.FeatureList.SetReorderObserver(self.reorder_handler)
            self.expToEdit = None
        except Exception as ex:
            traceback.print_exc()

    #------------------------------------------------------------------------------
    # Callback Name: dialogShown_cb
    #This callback is executed just before the dialog launch. Thus any value set 
    #here will take precedence and dialog will be launched showing that value. 
    #------------------------------------------------------------------------------
    def dialogShown_cb(self):
        try:
            pass
        except Exception as ex:
            traceback.print_exc()

    #------------------------------------------------------------------------------
    # Callback Name: apply_cb
    #------------------------------------------------------------------------------
    def apply_cb(self):
        errorCode = 0
        try:
            if self.expToEdit != None:
                editedValue = self.ExpressionValue.Value
                unit1 = self.workPart.UnitCollection.FindObject("MilliMeter")
                markId2 = self.theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Update Expression Data")
                self.workPart.Expressions.EditWithUnits(self.expToEdit, unit1, str(editedValue))
                nErrs1 = self.theSession.UpdateManager.DoUpdate(markId2)
                #Report any errors - normally the error list should be scanned and each error processed
                if nErrs1 > 0:
                    errorCode = 1
                    print("Update Errors: nErrs = %d" % nErrs1)
                self.theSession.DeleteUndoMark(markId2, "Update Expression Data")

        except Exception as ex:
            errorCode = 1
            traceback.print_exc()
        return errorCode

    #------------------------------------------------------------------------------
    # Callback Name: update_cb
    #------------------------------------------------------------------------------
    def update_cb(self, block):
        #updatedBlock = None
        try:
            if block == self.FeatureList:
                updatedBlock = self.FeatureList.FindUpdated()
                if updatedBlock != None:
                    subBlock = updatedBlock.FindBlock("select_feature0")
                    if subBlock != None:
                        featCol = subBlock.GetSelectedObjects()
                        if len(featCol) > 1:
                            self.newFeatCol[0] = featCol[-1]
                            subBlock.SetSelectedObjects(self.newFeatCol)
                        elif len(featCol) == 1:
                            self.newFeatCol[0] = featCol[0]
                        feature1 = self.newFeatCol[0]
                        featureIds = []
                        featureIds.append(feature1.JournalIdentifier)
                        self.FeatureList.SetItemText(updatedBlock, featureIds)

            elif block == self.ButtonGetExpressions:
                selectedBlocks = self.FeatureList.GetSelected()
                updatedBlock = None
                if len(selectedBlocks) > 0:
                    updatedBlock = selectedBlocks[0]
                if updatedBlock != None:
                    strings = self.FeatureList.GetItemText(updatedBlock)
                    if strings[0] != "":
                        feat = self.workPart.Features.FindObject(strings[0])
                        allExp = feat.GetExpressions()
                        allExpStr = []
                        for exp in allExp:
                            allExpStr.append("%s = %s - %s" % (str(exp.Name), str(exp.Value), str(exp.GetDescriptor())))
                        if len(allExpStr) > 0:
                            self.ExpressionList.SetListItems(allExpStr)
                        self.FeatureList.SetItemText(updatedBlock, strings)

            elif block == self.ExpressionList:
                listItems = self.ExpressionList.GetListItems()
                selItems = self.ExpressionList.GetSelectedItems()
                split_string = listItems[selItems[0]].split()

                ExpressionNameProperties = self.ExpressionName.GetProperties()
                self.ExpressionName.Value = split_string[0]

                self.expToEdit = self.workPart.Expressions.FindObject(split_string[0])

                self.ExpressionValue.Value = self.expToEdit.Value

        except Exception as ex:
            traceback.print_exc()
        
        return 0
    
    #------------------------------------------------------------------------------
    #----------------------------User defined Functions----------------------------
    #------------------------------------------------------------------------------
    def add_handler(self, list):
        newItem = list.AddNewSet(True)
        return 0

    def delete_handler(self, list, doomed):
        self.theSession.ListingWindow.Open()
        self.theSession.ListingWindow.WriteLine("Control is in delete_handler function")
        return 0
        
    def reorder_handler(self, list, moved, oldPos, newPos):
        self.theSession.ListingWindow.Open()
        self.theSession.ListingWindow.WriteLine("Moved list item No. " + str(oldPos + 1) + 
                                                " from " + str(oldPos + 1) + 
                                                " to " + str(newPos + 1) + ".")
        return 0

    
    def deletePropertyList(self, prop):
        prop.Dispose()
        prop = None

#------------------------------- DIALOG LAUNCHING ---------------------------------
#
#    Before invoking this application one needs to open any part/empty part in NX
#    because of the behavior of the blocks.
#
#    Make sure the dlx file is in one of the following locations:
#        1.) From where NX session is launched
#        2.) $UGII_USER_DIR/application
#        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
#            recommended. This variable is set to a full directory path to a file 
#            containing a list of root directories for all custom applications.
#            e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
#
#    You can create the dialog using one of the following way:
#
#    1. Journal Replay
#
#        1) Replay this file through Tool->Journal->Play Menu.
#
#    2. USER EXIT
#
#        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
#        2) Invoke the Shared Library through File->Execute->NX Open menu.
#
#------------------------------------------------------------------------------
def main():
    theEditExpression = None
    try:
        theEditExpression = EditExpression()
        # The following method shows the dialog immediately
        theEditExpression.Show()
    except Exception as ex:
        print(ex)
    finally:
        theEditExpression.Dispose()

def GetUnloadOption(arg):
    return NXOpen.Session.LibraryUnloadOption.Immediately

#------------------------------------------------------------------------------
# Following method cleanup any housekeeping chores that may be needed.
# This method is automatically called by NX.
#------------------------------------------------------------------------------
def UnloadLibrary(arg):
    try:
        pass
    except Exception as ex:
        print(ex)
    
if __name__ == '__main__':
    main()



