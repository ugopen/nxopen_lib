#=============================================================================
#
#       Copyright 2024 Siemens Product Lifecycle Management Software Inc.
#
#                            All Rights Reserved.
#
#=============================================================================
# File description: Sample NX/Open Application for Block Styler
#=============================================================================
#
#
#=============================================================================
#  Purpose:  This TEMPLATE file contains Python source to guide you in the
#  construction of your Block application dialog. The generation of your
#  dialog file (.dlx extension) is the first step towards dialog construction
#  within NX.  You must now create a NX Open application that
#  utilizes this file (.dlx).
#
#  The information in this file provides you with the following:
#
#  1.  Help on how to load and display your Block Styler dialog in NX
#      using APIs provided in NXOpen.BlockStyler namespace
#  2.  The empty callback methods (stubs) associated with your dialog items
#      have also been placed in this file. These empty methods have been
#      created simply to start you along with your coding requirements.
#      The method name, argument list and possible return values have already
#      been provided for you.
#
#
#
#=============================================================================

import NXOpen
import NXOpen.BlockStyler

#------------------------------------------------------------------------------
# Represents Block Styler application cls
#------------------------------------------------------------------------------
class PostSelectionExample:
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
            self.theDlxFileName = "PostSelectionExample.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
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
    # This method launches the dialog to screen
    #------------------------------------------------------------------------------
    def Launch(self):
        dialogResponse = NXOpen.BlockStyler.BlockDialog.DialogResponse.Invalid
        try:
            dialogResponse = self.theDialog.Launch()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        
        return dialogResponse
    
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
            self.selectPostNodes0 = self.theDialog.TopBlock.FindBlock("selectPostNodes0")
            self.selectPostElements0 = self.theDialog.TopBlock.FindBlock("selectPostElements0")
            self.selectPostNodes01 = self.theDialog.TopBlock.FindBlock("selectPostNodes01")
            self.selectPostElements01 = self.theDialog.TopBlock.FindBlock("selectPostElements01")
            #------------------------------------------------------------------------------
            # Registration of SelectPostNodeBlock specific callbacks
            # By default, the main post view id will be used to initialize the post selection.
            # 1, If you keep this way, ignore the set post view id method.
            # 2, If you want to specify post view id, pass the post view id by the bellow method.
            # 
            # For more examples, refer to ../SampleNXOpenApplications/Python/BlockStyler
            #------------------------------------------------------------------------------
            # self.selectPostNodes0.PostViewId = 1

            # self.selectPostNodes01.PostViewId = 1

            self.selectPostNodes0.ShowSelection = True
            self.selectPostNodes0.LabelString = "Select Post Node"
            self.selectPostNodes0.Cue = "Post Node Selection"
            self.selectPostNodes0.Bitmap = "select_existing_node"

            self.selectPostNodes0.DisableSmartMethod(NXOpen.BlockStyler.PostSelectNode.SmartMethodType.NumberOfMaxValues)

            self.selectPostNodes01.SelectionMode = "Single"

            # If you want to launch the dialog with some nodes already selected, 
            # you can use this method to initialize the selection component.
            # self.selectPostNodes0.SetSelectedNodeLabels(nodeLabels)
            
            # If you want to automatically switch to next selection uicomponent when single selection mode is enabled,
            # you can set the automatic progression property as True.
            self.selectPostNodes01.AutomaticProgression = True
            
            #------------------------------------------------------------------------------
            #------------------------------------------------------------------------------
            # Registration of SelectPostElementBlock specific callbacks
            # By default, the main post view id will be used to initialize the post selection.
            # 1, If you keep this way, ignore the set post view id method.
            # 2, If you want to specify post view id, pass the post view id by bellow method.
            #------------------------------------------------------------------------------
            # self.selectPostElements0.PostViewId = 1
            # self.selectPostElements01.PostViewId = 1

            self.selectPostElements0.ShowSelection = True
            self.selectPostElements0.LabelString = "Select Post Element"
            self.selectPostElements0.Cue = "Post Element Selection"
            self.selectPostElements0.Bitmap = "select_existing_element"

            self.selectPostElements0.DisableSmartMethod(NXOpen.BlockStyler.PostSelectElement.SmartMethodType.NumberOfMinValues)

            self.selectPostElements01.SelectionMode = "Single"

            # If you want to launch the dialog with some elements already selected, 
            # you can use this method to initialize the selection component.
            #self.selectPostElements0.SetSelectedElementLabels(elemLabels)
            
            # If the selection is not required, you can set the step status option.
            # Three options available: "Required","Optional","Satisfied".
            self.selectPostElements01.StepStatusAsString = "Optional"

            #------------------------------------------------------------------------------
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
            pvid = NXOpen.Session.GetSession().Post.GetMainPostviewIdInActivePart()
            postGroupBuilder1 = self.theSession.Post.CreatePostGroupBuilder(pvid)
            postGroupBuilder1.NeedCreateGroupInCurrentWorkPart = False

            #The group name and label must be unique. If either the name or label (or both) have already been used by an existing group, an error will occur.
            #In that case, you will need to change the name, label, or both.
            postGroupBuilder1.Name = "PostSelectionExampleGroup1"
            postGroupBuilder1.Label = 200

            theLw = self.theSession.ListingWindow
            theLw.Open()

            #Print node indices
            nodeIndices = self.selectPostNodes0.GetSelectedNodeIndices()
            for nodeIndex in nodeIndices:
                theLw.WriteLine("Node Index: %d" %nodeIndex)

            nodeLabels = self.selectPostNodes0.GetSelectedNodeLabels()
            for nodeLabel in nodeLabels:
                theLw.WriteLine("Node Label: %d" %nodeLabel)
                postSelectionEntity1 = self.theSession.ResultManager.CreatePostSelectionEntity()
                postSelectionEntity1.NodeId = nodeLabel

                print(f'Object address: {id(postSelectionEntity1)}')
                postGroupBuilder1.SelectionEntityList.AddEntity(postSelectionEntity1)

            #Print element indices
            elementsIndices = self.selectPostElements0.GetSelectedElementIndices()
            for elementIndex in elementsIndices:
                theLw.WriteLine("Element Index: %d" %elementIndex)

            elementLabels = self.selectPostElements0.GetSelectedElementLabels()
            for elemLabel in elementLabels:
                theLw.WriteLine("Element Label: %d" %elemLabel)
                postSelectionEntity2 = self.theSession.ResultManager.CreatePostSelectionEntity()
                postSelectionEntity2.ElemId = elemLabel

                print(f'Object address: {id(postSelectionEntity2)}')
                postGroupBuilder1.SelectionEntityList.AddEntity(postSelectionEntity2)

            #Print node label in singe selection mode
            singleSelectionNodeLabels = self.selectPostNodes01.GetSelectedNodeLabels()
            for nodeLabel in singleSelectionNodeLabels:
                theLw.WriteLine("Node Label: %d" %nodeLabel)
                postSelectionEntity01 = self.theSession.ResultManager.CreatePostSelectionEntity()
                postSelectionEntity01.NodeId = nodeLabel

                print(f'Object address: {id(postSelectionEntity01)}')
                postGroupBuilder1.SelectionEntityList.AddEntity(postSelectionEntity01)

            #Print element label in singe selection mode
            singleSelectionElementLabels = self.selectPostElements01.GetSelectedElementLabels()
            for elemLabel in singleSelectionElementLabels:
                theLw.WriteLine("Element Label: %d" %elemLabel)
                postSelectionEntity02 = self.theSession.ResultManager.CreatePostSelectionEntity()
                postSelectionEntity02.ElemId = elemLabel

                print(f'Object address: {id(postSelectionEntity02)}')
                postGroupBuilder1.SelectionEntityList.AddEntity(postSelectionEntity02)
            
            theLw.Close()

            nXObject2 = postGroupBuilder1.Commit()

            postGroupBuilder1.Destroy()

        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

            theLw.Close()
        
        return errorCode
    
    #------------------------------------------------------------------------------
    # Callback Name: update_cb
    #------------------------------------------------------------------------------
    def update_cb(self, block):
        try:
            if block == self.selectPostNodes0:
                # ---- Enter your code here -----
                pass
            elif block == self.selectPostElements0:
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
    
def main():
    thePostSelectionExample = None
    try:
        thePostSelectionExample =  PostSelectionExample()
        #  The following method shows the dialog immediately
        thePostSelectionExample.Launch()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if thePostSelectionExample != None:
            thePostSelectionExample.Dispose()
            thePostSelectionExample = None
    
if __name__ == '__main__':
    main()

