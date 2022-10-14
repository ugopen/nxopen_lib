#=============================================================================
#
#       Copyright 2014 Siemens Product Lifecycle Management Software Inc.
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

import traceback
import NXOpen
import NXOpen.BlockStyler
import NXOpen.Features
import NXOpen.UF

#-----------------------------------------------------------------------------
# Represents Block Styler application class
#-----------------------------------------------------------------------------
class SelectionExample:
    #-------------------------------------------------------------------------
    # Constructor for NX Styler class
    #-------------------------------------------------------------------------
    def __init__(self):
        # class members
        self.theSession = None
        self.theUI = None
        self.theDialogName = ""
        self.theDialog = None
        self.group0 = None # Block type: Group
        self.edgeSelect = None  # Block type: Curve Collector
        self.faceToggle = None  # Block type: Toggle
        self.angleDouble = None  # Block type: Double
        self.group01 = None # Block type: Group
        self.chamferSelect = None  # Block type: Select Feature
        self.angleToggle = None  # Block type: Toggle
        self.angleLimitDouble = None  # Block type: Double

        # NEW CODE
        self.limitingFace = None  # face to limit edge selection
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.theDialogName = "SelectionExample.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDialogName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddFilterHandler(self.filter_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
        except Exception as ex:
            #---- Enter your exception handling code here -----
            raise ex
    
    #-------------------------------------------------------------------------
    # This method shows the dialog on the screen
    #-------------------------------------------------------------------------
    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            #---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Show", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    
    #-------------------------------------------------------------------------
    # Method Name: Dispose
    #-------------------------------------------------------------------------
    def Dispose(self):
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None
    
    #-------------------------------------------------------------------------
    #---------------------Block Styler Callback Functions---------------------
    #-------------------------------------------------------------------------
    
    #-------------------------------------------------------------------------
    # Callback Name: initialize_cb
    #-------------------------------------------------------------------------
    def initialize_cb(self):
        try:
            self.group0 = self.theDialog.TopBlock.FindBlock("group0")
            self.edgeSelect = self.theDialog.TopBlock.FindBlock("edge_select0")
            self.faceToggle = self.theDialog.TopBlock.FindBlock("toggle0")
            self.angleDouble = self.theDialog.TopBlock.FindBlock("double0")
            self.group01 = self.theDialog.TopBlock.FindBlock("group01")
            self.chamferSelect = self.theDialog.TopBlock.FindBlock("select_feature0")
            self.angleToggle = self.theDialog.TopBlock.FindBlock("toggle01")
            self.angleLimitDouble = self.theDialog.TopBlock.FindBlock("double01")
            # NEW CODE
            self.limitingFace = None
        except Exception as ex:
            #---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("initialize_cb", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    
    #-------------------------------------------------------------------------
    # Callback Name: apply_cb
    #-------------------------------------------------------------------------
    def apply_cb(self):
        errorCode = 0
        try:
            #*****************************************************************
            # Add Chamfers to Selected Edges

            # Get the chamfer angle and edge selection list from the dialog
            creationAngle = self.angleDouble.Value
            edges = self.edgeSelect.GetSelectedObjects()

            # Add a chamfer to each selected edge
            for selectedEdge in edges:
                self.addChamfer(selectedEdge, creationAngle)

            #*****************************************************************
            # Remove Selected Chamfers

            # Get the selected chamfers from the dialog
            chamfers = self.chamferSelect.GetSelectedObjects()

            # Set an undo mark for update
            undoMark = self.theSession.SetUndoMark(
                NXOpen.Session.MarkVisibility.Visible, "Remove Chamfers")

            # Add the selected chamfers to the delete list
            for chamferObject in chamfers:
                errorCode = self.deleteObject(chamferObject)

            # Update the model to delete the chamfers
            nErrs = self.theSession.UpdateManager.DoUpdate(undoMark)

            # Report any errors - normally the error list should be scanned and each error processed
            if nErrs > 0:
                errorCode = 1
                self.theUI.NXMessageBox.Show(
                    "Update Errors", 
                    NXOpen.NXMessageBox.DialogType.Error, 
                    "nErrs = %d" % nErrs)

        except Exception as ex:
            #---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show(
                "Apply Error", NXOpen.NXMessageBox.DialogType.Error, str(ex))

        return errorCode
    
    #-------------------------------------------------------------------------
    # Callback Name: update_cb
    #-------------------------------------------------------------------------
    def update_cb(self, block):
        try:
            if block == self.edgeSelect:
                # When face filtering is on, establish a limiting face after two edges are selected
                if self.faceToggle.Value:
                    edges = self.edgeSelect.GetSelectedObjects()
                    if (len(edges) == 2):
                        limitingFace = self.sharedFace(edges[0], edges[1])
            elif block == self.faceToggle:
                # When the face filter is turned on...
                #  Clear the current edge selection list
                if self.faceToggle.Value:
                    edges = []
                    self.edgeSelect.SetSelectedObjects(edges)
                    limitingFace = None
            elif block == self.angleDouble:
                #---- Enter your code here -----
                pass
            elif block == self.chamferSelect:
                #---- Enter your code here -----
                pass
            elif block == self.angleToggle:
                # When the angle filter is turned on...
                #  1. Clear the current chamfer selection list
                #  2. Also, enable/disable the angle limit entry field
                if self.angleToggle.Value:
                    chamfers = []
                    self.chamferSelect.SetSelectedObjects(chamfers)
                    self.angleLimitDouble.Enable = True
                else:
                    self.angleLimitDouble.Enable = False
            elif block == self.angleLimitDouble:
                # When the angle limit value changes...
                #    Clear the current chamfer selection list
                chamfers = []
                self.chamferSelect.SetSelectedObjects(chamfers)
        except Exception as ex:
            #---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("update_cb", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return 0
    
    #-------------------------------------------------------------------------
    # Callback Name: ok_cb
    #-------------------------------------------------------------------------
    def ok_cb(self):
        errorCode = 0
        try:
            #---- Enter your callback code here -----
            errorCode = self.apply_cb()
        except Exception as ex:
            #---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show("ok_cb", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return errorCode
    
    #-------------------------------------------------------------------------
    # Callback Name: filter_cb
    #-------------------------------------------------------------------------
    def filter_cb(self, block, selectedObject):
        accept = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
        try:
            if block == self.edgeSelect:
                # Edge Select Filter
                if self.faceToggle.Value:
                    accept = self.faceFilter(selectedObject)
            elif block == self.chamferSelect:
                # Feature Selection Filter - limit selection to chamfer features
                featureObject = selectedObject
                if featureObject.FeatureType == "CHAMFER":
                    accept = self.angleFilter(featureObject)
                else:
                    accept = NXOpen.UF.UFConstants.UF_UI_SEL_REJECT
        except Exception as ex:
            #---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("filter_cb", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return accept

    #*************************************************************************
    # FACE FILTER

    def faceFilter(self, selectedEdge):
        accept = NXOpen.UF.UFConstants.UF_UI_SEL_REJECT

        #  If a limiting face has not been established...
        #  then use the first two selected edges to establish the limiting face 
        #  otherwise use the limiting face

        if self.limitingFace == None:
            # Limit faces to those of the first selected edge
            edges = self.edgeSelect.GetSelectedObjects()
            if len(edges) < 1:
                accept = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
            elif len(edges) == 1:
                if self.sharedFace(edges[0], selectedEdge) != None:
                    accept = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
        else:
            # Limit the edges to just those of the limiting face
            for faceObject in selectedEdge.GetFaces():
                if faceObject == limitingFace:
                    accept = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
                    break
        return accept

    #*************************************************************************
    # ANGLE FILTER

    def angleFilter(self, chamferFeature):
        accept = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT

        # If the angle filter toggle is ON...
        #  then only accept chamfers of the limiting angle

        if self.angleToggle.Value:
            workPart = self.theSession.Parts.Work
            chamferBuilder = workPart.Features.CreateChamferBuilder(chamferFeature)
            if chamferBuilder.AngleExp.Value != self.angleLimitDouble.Value:
                accept = NXOpen.UF.UFConstants.UF_UI_SEL_REJECT
            chamferBuilder.Destroy()
        return accept

    #*************************************************************************
    # SHARED FACE - return face shared between two edges
    def sharedFace(self, edge1, edge2):
        foundFace = None
        for face1 in edge1.GetFaces():
            for face2 in edge2.GetFaces():
                if face1 == face2:
                    foundFace = face1
                    break
            if foundFace != None:
                break
        return foundFace

    #*************************************************************************
    # ADD CHAMFER FEATURE of given angle to given edge

    def addChamfer(self, selectedEdge, angle):

        chamferBuilder1 = None

        try:
            workPart = self.theSession.Parts.Work
            nullFeatures_Feature = NXOpen.Features.Feature.Null

            chamferBuilder1 = workPart.Features.CreateChamferBuilder(nullFeatures_Feature)

            chamferBuilder1.Option = NXOpen.Features.ChamferBuilder.ChamferOption.OffsetAndAngle
            chamferBuilder1.Method = NXOpen.Features.ChamferBuilder.OffsetMethod.EdgesAlongFaces

            chamferBuilder1.FirstOffset = "15"
            chamferBuilder1.SecondOffset = "15"
            chamferBuilder1.Angle = str(angle)
            chamferBuilder1.Tolerance = 0.0254

            nullEdge = NXOpen.Edge.Null
            edgeTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeTangent(selectedEdge, nullEdge, False, 0.5, False)

            rules1 = [None]
            rules1[0] = edgeTangentRule1

            scCollector1 = workPart.ScCollectors.CreateCollector()

            scCollector1.ReplaceRules(rules1, False)

            chamferBuilder1.SmartCollector = scCollector1

            feature1 = chamferBuilder1.CommitFeature()

        except Exception as ex:
            raise ex
        finally:
            if not chamferBuilder1 == None:
                chamferBuilder1.Destroy()

    #*************************************************************************
    # DELETE OBJECT - add the given object to the delete list

    def deleteObject(self, selectedObject):

        ret = 0

        try:
            objects = [None]

            objects[0] = selectedObject

            nErrs = self.theSession.UpdateManager.AddToDeleteList(objects)

            # Report any errors - normally the error list should be scanned and each error processed
            if nErrs > 0:
                ret = 1
                self.theUI.NXMessageBox.Show(
                    "Add To Delete Errors", 
                    NXOpen.NXMessageBox.DialogType.Error, 
                    "nErrs = %d" % nErrs)

        except Exception as ex:
            raise ex
   
#------------------------------- DIALOG LAUNCHING ----------------------------
#
#    Before invoking this application one needs to open any part/empty part
#    in NX because of the behavior of the blocks.
#
#    Make sure the dlx file is in one of the following locations:
#        1.) From where NX session is launched
#        2.) $UGII_USER_DIR/application
#        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is 
#            highly recommended. This variable is set to a full directory 
#            path to a file containing a list of root directories for all 
#            custom applications, 
#            e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
#
#    You can create the dialog using the following method:
#
#    1. Journal Replay
#
#        1) Replay this file through Tool->Journal->Play Menu.
#
#
#-----------------------------------------------------------------------------
def main():
    theSelectionExample = None
    try:
        theSelectionExample = SelectionExample()
        # The following method shows the dialog immediately
        theSelectionExample.Show()
    except Exception as ex:
        #---- Enter your exception handling code here -----
        traceback.print_exc()
    finally:
        if theSelectionExample != None:
            theSelectionExample.Dispose()

if __name__ == "__main__":
    main()
