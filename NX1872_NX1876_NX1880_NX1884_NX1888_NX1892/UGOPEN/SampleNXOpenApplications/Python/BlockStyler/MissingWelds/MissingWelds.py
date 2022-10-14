#=============================================================================
#
#                   Copyright (c) 2015 Siemens PLM Software
#                    Unpublished - All rights reserved
#=============================================================================
#File description: Sample NX/Open Application for Block Styler
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
import NXOpen.Assemblies
import NXOpen.BlockStyler
import NXOpen.Features
from os.path import dirname, join

#------------------------------------------------------------------------------
# Represents Block Styler application cls
#------------------------------------------------------------------------------
class MissingWelds:
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
            self.theDlxFileName = "MissingWelds.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDlxFileName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)
            
            self.theClearanceSet = NXOpen.Assemblies.ClearanceSet.Null
            self.wasSubNodeCreated = False
            
            # contains all the components in the assembly, except root component
            self.allObjects = []
            # contains a pair of objects for each checked sub node
            self.checkedSubNodeObjects = []
            # contains a pair of objects for each missing weld, indexed by subNodeId
            self.missingWelds = {}
            # temporarily hold the two displayable objects for the selected missing weld
            # for access by update_cb, apply_cb, and StepNotifyPreCallback methods
            self.selectedMissingWeldObjects = [NXOpen.DisplayableObject.Null] * 2
            
            self.selectedMissingWeldObjects[0] = None
            self.selectedMissingWeldObjects[1] = None
            
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
            self.missingWeldWizard = self.theDialog.TopBlock.FindBlock("missingWeldWizard")
            self.clearanceSetStep = self.theDialog.TopBlock.FindBlock("clearanceSetStep")
            self.compSelection = self.theDialog.TopBlock.FindBlock("compSelection")
            self.resultsStep = self.theDialog.TopBlock.FindBlock("resultsStep")
            self.compDisplay = self.theDialog.TopBlock.FindBlock("compDisplay")
            self.missingWeldObjectsListBox = self.theDialog.TopBlock.FindBlock("missingWeldObjectsListBox")
            #------------------------------------------------------------------------------
            # Registration of ListBox specific callbacks
            #------------------------------------------------------------------------------
            # self.missingWeldObjectsListBox.SetAddHandler(self.AddCallback)
            
            # self.missingWeldObjectsListBox.SetDeleteHandler(self.DeleteCallback)
            
            #------------------------------------------------------------------------------
            #------------------------------------------------------------------------------
            # Registration of Wizard, missingWeldWizard specific callbacks
            #------------------------------------------------------------------------------
            self.missingWeldWizard.SetStepNotifyPreHandler(self.StepNotifyPreCallback)
            
            # self.missingWeldWizard.SetStepNotifyPostHandler(self.StepNotifyPostCallback)
            
            self.missingWeldWizard.SetIsStepOkayHandler(self.IsStepOkayCallback)
            
            self.missingWeldWizard.SetOnSubNodeHandler(self.OnSubNodeCallback)
            
            self.missingWeldWizard.SetOnMenuHandler(self.OnMenuCallback)
            
            self.missingWeldWizard.SetOnMenuSelectionHandler(self.OnMenuSelectionCallback)


            self.compSelection.AddFilter(NXOpen.BlockStyler.SelectObject.FilterType.Components.value)

            # Load all the components included in the assembly except the root component
            if self.theSession.Parts.Display != None:
                rootComponent = self.theSession.Parts.Display.ComponentAssembly.RootComponent
                self.AddChildren(rootComponent)
                
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
            
            # Show all bodies and unhighlight all objects
            self.theSession.DisplayManager.ShowByType("SHOW_HIDE_TYPE_SOLID_BODIES", NXOpen.DisplayManagerShowHideScope.AnyInAssembly)
                
            if self.selectedMissingWeldObjects[0] != None:
                self.selectedMissingWeldObjects[0].Unhighlight()
            if self.selectedMissingWeldObjects[1] != None:
                self.selectedMissingWeldObjects[1].Unhighlight()
                
            self.theSession.Parts.Work.ModelingViews.WorkView.Fit()
            
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
            if block == self.compSelection:
                # ---- Enter your code here -----
                pass
            elif block == self.compDisplay:
                theWorkPart = self.theSession.Parts.Work
                theWorkView = theWorkPart.ModelingViews.WorkView
                
                # Get value of compDisplay enum
                compDisplayProps = self.compDisplay.GetProperties()
                compDisplayValue = compDisplayProps.GetEnum("Value")
                compDisplayProps.Dispose()
                compDisplayProps = None
                
                # "Blank" has the enum value of 0
                if compDisplayValue == 0:
                    if self.selectedMissingWeldObjects[0] != None and self.selectedMissingWeldObjects[1] != None:
                        
                        # Unhighlight the objects and show only those two objects
                        self.selectedMissingWeldObjects[0].Unhighlight()
                        self.selectedMissingWeldObjects[1].Unhighlight()
                        
                        self.theSession.DisplayManager.HideByType("SHOW_HIDE_TYPE_SHEET_BODIES", NXOpen.DisplayManager.ShowHideScope.AnyInAssembly)
                    
                        for weldFeature in theWorkPart.Features.WeldManager:
                            weldFeature.HideBody()
                    
                        for d in self.allObjects:
                            if d != self.selectedMissingWeldObjects[0] and d != self.selectedMissingWeldObjects[1]:
                                d.Blank()
                    
                        theWorkView.Fit()
                
                # "Highlight" has the enum value of 1
                if compDisplayValue == 1:
                    if self.selectedMissingWeldObjects[0] != None and self.selectedMissingWeldObjects[1] != None:
                        
                        # Unblank all bodies and highlight the two objects
                        for weldFeature in theWorkPart.Features.WeldManager:
                            weldFeature.ShowBody(True)
                    
                        for d in self.allObjects:
                            if d != self.selectedMissingWeldObjects[0] and d != self.selectedMissingWeldObjects[1]:
                                d.Unblank()
                    
                        theWorkView.Fit()
                                           
                        self.selectedMissingWeldObjects[0].Highlight()
                        self.selectedMissingWeldObjects[1].Highlight()
                        
            elif block == self.missingWeldObjectsListBox:
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
    # Wizard specific callbacks
    #------------------------------------------------------------------------------
    def StepNotifyPreCallback(self, wizard, nextStep):
        try:
            theWorkPart = self.theSession.Parts.Work
            theWorkView = theWorkPart.ModelingViews.WorkView
            
            if nextStep == 0:
                
                # Clear list box
                listBoxMessage = [""]
                self.missingWeldObjectsListBox.SetListItems(listBoxMessage)
                listBoxMessage.clear()
                
                # Show all bodies and unhighlight all objects
                self.theSession.DisplayManager.ShowByType("SHOW_HIDE_TYPE_SOLID_BODIES", NXOpen.DisplayManagerShowHideScope.AnyInAssembly)
                
                self.selectedMissingWeldObjects = list(self.selectedMissingWeldObjects)
                if self.selectedMissingWeldObjects[0] != None:
                    self.selectedMissingWeldObjects[0].Unhighlight()
                    self.selectedMissingWeldObjects[0] = None
                if self.selectedMissingWeldObjects[1] != None:
                    self.selectedMissingWeldObjects[1].Unhighlight()
                    self.selectedMissingWeldObjects[1] = None
                
                for key in self.missingWelds.keys():
                    wizard.RemoveStepSubNode(key)
                 
                if self.theClearanceSet != None:
                    self.theClearanceSet.Delete()
                    self.theClearanceSet = None
                 
                self.wasSubNodeCreated = False
                self.missingWelds.clear()
                self.checkedSubNodeObjects.clear()
                 
                theWorkView.Fit()
                
            elif nextStep == 1:
                clearanceAnalysisBuilder1 = theWorkPart.AssemblyManager.CreateClearanceAnalysisBuilder(NXOpen.Assemblies.ClearanceSet.Null)
                
                # Set parameters
                clearanceAnalysisBuilder1.ClearanceSetName = "Missing Weld Clearance Set"
                clearanceAnalysisBuilder1.CollectionOneRange = NXOpen.Assemblies.ClearanceAnalysisBuilder.CollectionRange.SelectedObjects
                  
                # Add selected components to CollectionOneObjects
                for tagObj in self.compSelection.GetSelectedObjects():
                    clearanceAnalysisBuilder1.CollectionOneObjects.Add(tagObj)
                  
                nXObject1 = clearanceAnalysisBuilder1.Commit()
                clearanceAnalysisBuilder1.Destroy()
                self.theClearanceSet = nXObject1 # holds the clearance set created by the wizard
                self.theClearanceSet.PerformAnalysis(NXOpen.Assemblies.ClearanceSet.ReanalyzeOutOfDateExcludedPairs.FalseValue)
                
                # Store the list of welds
                weldObjects = [] # holds the pair of tagged objects involved in each weld feature
                for weldFeature in theWorkPart.Features.WeldManager:
                    connectPartsInfo = self.theSession.WeldCustomManager.AskConnectedParts(weldFeature)
                    # We assume that there are exactly two sets for the weld, with one object in each set
                    id1 = connectPartsInfo.GetSetInformation(0)
                    id2 = connectPartsInfo.GetSetInformation(1)
                    weldObjects.append( (id1[0], id2[0]) )
                
                # Create a subNode for each missing weld and store the pair of objects involved in the weld.
                # NOTE: The interfering objects in the clearance set, and the objects involved in the weld feature
                # must be components when compared with each other.
                (interferenceComponent1, interferenceComponent2) = self.theClearanceSet.GetNextInterference(NXOpen.DisplayableObject.Null, NXOpen.DisplayableObject.Null)
                
                i = 1
                 
                while interferenceComponent1 != None:
                    isMissingWeld = True
                    for weldPair in weldObjects:                       
                        weldComponent1 = weldPair[0].OwningComponent
                        weldComponent2 = weldPair[1].OwningComponent
                        if ((weldComponent1 == interferenceComponent1 and weldComponent2 == interferenceComponent2)
                            or (weldComponent2 == interferenceComponent1 and weldComponent1 == interferenceComponent2)):
                                isMissingWeld = False
                                break
                     
                    if isMissingWeld:
                        missingWeldName = "Missing weld " + str(i)
                        i += 1
                        subNodeID = wizard.CreateStepSubNode(1, missingWeldName, "", True, True)
                        self.missingWelds[subNodeID] = (interferenceComponent1, interferenceComponent2)
                        self.checkedSubNodeObjects.append( (interferenceComponent1, interferenceComponent2) )
                        self.wasSubNodeCreated = True
                      
                    (interferenceComponent1, interferenceComponent2) = self.theClearanceSet.GetNextInterference(interferenceComponent1, interferenceComponent2)
                 
                if not self.wasSubNodeCreated:
                    listBoxMessage = ["There are no missing welds."]
                    self.missingWeldObjectsListBox.SetListItems(listBoxMessage)
                  
                theWorkView.Fit()
                 
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

        return 0
     
    
    # def StepNotifyPostCallback(self, wizard, previousStep):
    # 
    # 
    
    def IsStepOkayCallback(self, wizard,  wizardStep):
        try:
            if wizard.CurrentStep == 0:
                if len(self.compSelection.GetSelectedObjects()) > 0:
                    return True
                else:
                    return False
            elif wizard.CurrentStep == 1:
                return True
            
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))

        return False
     
    
    def OnSubNodeCallback(self, wizard,  wizardStep,  subNodeId,  action):
        try:
            theWorkPart = self.theSession.Parts.Work
            theWorkView = theWorkPart.ModelingViews.WorkView
            
            # Store the pair of objects from the missing weld associated with this sub node
            # for access by update_cb, apply_cb, and StepNotifyPreCallback methods
            self.selectedMissingWeldObjects = self.missingWelds[subNodeId]
            
            if action == NXOpen.BlockStyler.Wizard.SubNodeAction.Select:
                # Add the missing weld's objects to list box
                listBoxMessage = [self.selectedMissingWeldObjects[0].Name, self.selectedMissingWeldObjects[1].Name]
                self.missingWeldObjectsListBox.SetListItems(listBoxMessage)
                listBoxMessage.clear()
                
                # Get value of compDisplay enum
                compDisplayProps = self.compDisplay.GetProperties()
                compDisplayValue = compDisplayProps.GetEnum("Value")
                compDisplayProps.Dispose()
                compDisplayProps = None
                
                # "Blank" has the enum value of 0
                if compDisplayValue == 0:
                    
                    # Show only the two objects
                    self.theSession.DisplayManager.HideByType("SHOW_HIDE_TYPE_SHEET_BODIES", NXOpen.DisplayManager.ShowHideScope.AnyInAssembly)
                    
                    for weldFeature in theWorkPart.Features.WeldManager:
                        weldFeature.HideBody()
                    
                    for d in self.allObjects:
                        if d != self.selectedMissingWeldObjects[0] and d != self.selectedMissingWeldObjects[1]:
                            d.Blank()
                    
                    theWorkView.Fit()
                
                # "Highlight" has the enum value of 1
                if compDisplayValue == 1:
                    theWorkView.Fit()
                    
                    self.selectedMissingWeldObjects[0].Highlight()
                    self.selectedMissingWeldObjects[1].Highlight()
                
            elif action == NXOpen.BlockStyler.Wizard.SubNodeAction.Deselect:
                
                # Clear list box
                listBoxMessage = [""]
                self.missingWeldObjectsListBox.SetListItems(listBoxMessage)
                listBoxMessage.clear()
                
                # Unhighlight and unblank all bodies
                self.selectedMissingWeldObjects[0].Unhighlight()
                self.selectedMissingWeldObjects[1].Unhighlight()
                
                for weldFeature in theWorkPart.Features.WeldManager:
                    weldFeature.ShowBody(True)
                
                for d in self.allObjects:
                    if d != self.selectedMissingWeldObjects[0] and d != self.selectedMissingWeldObjects[1]:
                        d.Unblank()
                        
                # Release this pair of objects when the sub node is deselected
                self.selectedMissingWeldObjects = list(self.selectedMissingWeldObjects)
                self.selectedMissingWeldObjects[0] = None
                self.selectedMissingWeldObjects[1] = None
            
            elif action == NXOpen.BlockStyler.Wizard.SubNodeAction.Check:
                self.checkedSubNodeObjects.append(self.selectedMissingWeldObjects)
            
            elif action == NXOpen.BlockStyler.Wizard.SubNodeAction.Uncheck:
                self.checkedSubNodeObjects.remove(self.selectedMissingWeldObjects)
            
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
     
    
    def OnMenuCallback(self, wizard,  item,  wizardStep,  subNodeId):
        try:
            subNodeMenu = self.missingWeldWizard.CreateMenu()
            if item == NXOpen.BlockStyler.Wizard.TaskNavigatorItem.Step:
                if self.wasSubNodeCreated:
                    subNodeMenu.AddMenuItem(0, "Generate Report for Selected Missing Welds")
                    self.missingWeldWizard.SetMenu(subNodeMenu)
            
            elif item == NXOpen.BlockStyler.Wizard.TaskNavigatorItem.SubNode:
                subNodeMenu.AddMenuItem(1, "Export Image to PDF")
                self.missingWeldWizard.SetMenu(subNodeMenu)
                
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
     
    
    def OnMenuSelectionCallback(self, wizard,  item,  wizardStep,  subNodeId,  commandIndex):
        try:
            theWorkPart = self.theSession.Parts.Work
            
            if commandIndex == 0:
                reportWindow = self.theSession.ListingWindow
                reportWindow.Open()
                reportWindow.WriteLine("Missing Welds for " + self.theSession.Parts.Display.ComponentAssembly.RootComponent.DisplayName + "\n\n");
                reportWindow.WriteLine(str(len(self.checkedSubNodeObjects)) + " of " + str(len(self.missingWelds)) + " missing welds selected\n\n");
                reportWindow.WriteLine("     Part 1\t\tPart 2\n\n");
                
                # Format spacing in report
                # Assumes no more than 999 missing weld pairs
                i = 1
                for weldPair in self.checkedSubNodeObjects:
                    if i <= 9:
                        reportWindow.WriteLine(str(i) + ")   " + weldPair[0].Name + "\t" + weldPair[1].Name)
                        i += 1
                    elif i <= 99:
                        reportWindow.WriteLine(str(i) + ")  " + weldPair[0].Name + "\t" + weldPair[1].Name)
                        i += 1
                    else:
                        reportWindow.WriteLine(str(i) + ") " + weldPair[0].Name + "\t" + weldPair[1].Name)
                        i += 1
                        
            elif commandIndex == 1:
                
                # Get value of compDisplay enum
                compDisplayProps = self.compDisplay.GetProperties()
                compDisplayValue = compDisplayProps.GetEnum("Value")

                # If Highlight is selected, automatically select Blank before creating image
                # "Highlight" has the enum value of 1
                if compDisplayValue == 1:
                    
                    # "Blank" has the enum value of 0
                    compDisplayProps.SetEnum("Value", 0)
                    
                    # Unhighlight the objects and show only those two objects
                    self.selectedMissingWeldObjects[0].Unhighlight()
                    self.selectedMissingWeldObjects[1].Unhighlight()
                        
                    self.theSession.DisplayManager.HideByType("SHOW_HIDE_TYPE_SHEET_BODIES", NXOpen.DisplayManager.ShowHideScope.AnyInAssembly)
                    
                    for weldFeature in theWorkPart.Features.WeldManager:
                        weldFeature.HideBody()
                    
                    for d in self.allObjects:
                        if d != self.selectedMissingWeldObjects[0] and d != self.selectedMissingWeldObjects[1]:
                            d.Blank()
                    
                    theWorkPart.ModelingViews.WorkView.Fit()
                    
                compDisplayProps.Dispose()
                compDisplayProps = None
                
                
                printPDFBuilder1 = theWorkPart.PlotManager.CreatePrintPdfbuilder()
                
                sheets1 = [NXOpen.NXObject.Null] * 1
                sheets1[0] = NXOpen.NXObject.Null
                printPDFBuilder1.SourceBuilder.SetSheets(sheets1)
                
                # Set pdf path to same directory as work part
                path = dirname(theWorkPart.FullPath)
                filename = "MissingWeld_" + self.selectedMissingWeldObjects[0].Name + "_" + self.selectedMissingWeldObjects[1].Name + ".pdf"
                printPDFBuilder1.Filename = join(path, filename)
                
                
                nXObject1 = printPDFBuilder1.Commit()
                printPDFBuilder1.Destroy()
                
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))


    #-------------------------------------------------------------------------------
    #Function Name: AddChildren
    #Recursive function used to add the children of the current component tree
    #node to allObjects
    #-------------------------------------------------------------------------------
    def AddChildren(self, component):
        try:
            childComponents = component.GetChildren()
            for i in childComponents:
                self.allObjects.append(i)
                self.AddChildren(i)
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))


def main():
    theMissingWelds = None
    try:
        theMissingWelds =  MissingWelds()
        #  The following method shows the dialog immediately
        theMissingWelds.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        if theMissingWelds != None:
            theMissingWelds.Dispose()
            theMissingWelds = None
    
if __name__ == '__main__':
    main()

