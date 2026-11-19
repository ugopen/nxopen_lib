#=============================================================================
#
#                   Copyright (c) 2016 Siemens Industry Software
#                    Unpublished - All rights reserved
#=============================================================================
#File description: Sample NX/Open Application for Custom feature 
#=============================================================================
#
#==============================================================================
#   Purpose:  This TEMPLATE file contains Python source to guide you in the
#   construction of your Block application dialog. The generation of your
#   dialog file (.dlx extension) is the first step towards dialog construction
#   within NX.  You must now create a NX Open application that
#   utilizes this file (.dlx).
# 
#   The information in this file provides you with the following:
# 
#   1.  Help on how to load and display your Block UI Styler dialog in NX
#       using APIs provided in NXOpen.BlockStyler namespace
#   2.  The empty callback methods (stubs) associated with your dialog items
#       have also been placed in this file. These empty methods have been
#       created simply to start you along with your coding requirements.
#       The method name, argument list and possible return values have already
#       been provided for you.
#==============================================================================

#------------------------------------------------------------------------------
# These imports are needed for the following template code
#------------------------------------------------------------------------------
import NXOpen
import NXOpen.BlockStyler
import NXOpen.Features

#------------------------------------------------------------------------------
# Represents Block Styler application class
#------------------------------------------------------------------------------
class CompositeCurveUI:
    # static class members
    theSession = None
    theUI = None
    
    #------------------------------------------------------------------------------
    # Constructor for NX Styler class
    #------------------------------------------------------------------------------
    def __init__(self):
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.workPart = self.theSession.Parts.Work
            self.theUI = NXOpen.UI.GetUI()
            self.theDlxFileName = "CompositeCurveUI.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)
            
            #Get custom feature manager from session
            self.cFMgr = self.theSession.CustomFeatureClassManager

            #Get custom feature class, Note that class name should match to value of FeatureClass in CustomFeatureConfiguration.xml 
            self.cFClass = self.cFMgr.GetClassFromName("NXOpen.CustomFeature.SampleCompositeCurve")

        except Exception as ex:
            # ---- Enter your exception handling code here -----
            raise ex
            
    # ------------------------------- DIALOG LAUNCHING ---------------------------------
    # 
    #     To run this application, you must have a part file open in an NX session.
    # 
    #     Make sure the dlx file is in one of the following locations:
    #         1.) From where NX session is launched
    #         2.) $UGII_USER_DIR/application
    #         3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    #             recommended. This variable is set to a full directory path to a file 
    #             containing a list of root directories for all custom applications.
    #             e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
    # 
    #     You can create the dialog using following way:
    # 
    #     Journal Replay
    # 
    #         Replay this file through Tool->Journal->Play Menu.
    # 
    #------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------
    # This method shows the dialog on the screen
    #------------------------------------------------------------------------------
    def Show(self):
        try:
            mode = NXOpen.BlockStyler.BlockDialog.DialogMode.Create
            if self.theSession.CustomFeatureClassManager.GetEditedCustomFeature() != None:
                mode = NXOpen.BlockStyler.BlockDialog.DialogMode.Edit
            self.theDialog.Show(mode)
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
            self.section0 = self.theDialog.TopBlock.FindBlock("section0")

            editedCustomFeature = self.cFMgr.GetEditedCustomFeature()

            if editedCustomFeature == None:
                
                # we are in create
                sectionObj = self.workPart.Sections.CreateSection(0.0095,0.01, 0.5)

                sectionObj.AllowSelfIntersection(True)

                selectedObjList = []

                selectedObjList.append(sectionObj)

                self.section0.SetSelectedObjects(selectedObjList)

            else:
                # we are in edit
                cFData = editedCustomFeature.FeatureData

                sectionAttrib = None
                if cFData.HasCustomAttribute("sectionAttrib", NXOpen.Features.CustomAttributeType.Tag):
                    sectionAttrib = cFData.CustomTagAttributeByName("sectionAttrib")

                    sectionObj = sectionAttrib.Value

                    objects = sectionObj.EvaluateAndAskOutputEntities()

                    selectedObjList = []

                    selectedObjList.append(sectionObj)

                    self.section0.SetSelectedObjects(selectedObjList)
                else:
                    pass
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
            editedCustomFeature = NXOpen.Features.CustomFeature.Null
            
            if (self.cFMgr.GetEditedCustomFeature() != None):
                editedCustomFeature = self.cFMgr.GetEditedCustomFeature()

            cfBuilder = self.workPart.Features.CreateCustomFeatureBuilder(editedCustomFeature)

            if (editedCustomFeature == NXOpen.Features.CustomFeature.Null):
                # We are in create
                selectedObjs = []
                selectedObjs = self.section0.GetSelectedObjects()
                if len(selectedObjs) == 1:                   
                    sectionObj = selectedObjs[0]
                    
                    attributeProperty = [NXOpen.Features.CustomAttribute.Property.MandatoryInput]
                    
                    sectionAttrib = self.workPart.Features.CustomAttributeCollection.CreateCustomTagAttribute("sectionAttrib", attributeProperty)
                    
                    sectionAttrib.Value = sectionObj

                    attributeList = []
                    
                    attributeList.append(sectionAttrib)

                    cFData = self.workPart.Features.CustomFeatureDataCollection.CreateData(self.cFClass, attributeList)

                    cfBuilder.FeatureData = cFData
                
            else:
                # we are in edit feature, nothing to be done in edit for this paticular feature as sectionattribute must be already defined.
                pass
            
            cfBuilder.CommitFeature()
            cfBuilder.Destroy()
            
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
            if block == self.section0:
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

    def WriteToListingWindow(self, string):
        self.theSession.ListingWindow.Open()
        self.theSession.ListingWindow.WriteLine(string)
        self.theSession.ListingWindow.Close()

        return None
    
def main():
    theCompositeCurveUI = None
    try:
        theCompositeCurveUI =  CompositeCurveUI()
        #  The following method shows the dialog immediately
        theCompositeCurveUI.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theCompositeCurveUI != None:
            theCompositeCurveUI.Dispose()
            theCompositeCurveUI = None
    
if __name__ == '__main__':
    main()
