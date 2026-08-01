#=============================================================================
#
#                   Copyright (c) 2014 Siemens PLM Solutions
#                    Unpublished - All rights reserved
#===============================================================================
#File description: Sample NX Open Python Application for Block Styler
#===============================================================================
#

#==============================================================================
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
#==============================================================================

#------------------------------------------------------------------------------
#These imports are needed for the following template code
#------------------------------------------------------------------------------
import NXOpen
import NXOpen.BlockStyler
import NXOpen.Features

#------------------------------------------------------------------------------
#Represents Block Styler application class
#------------------------------------------------------------------------------
class ColoredBlock:
    # ------------------------------------------------------------------------------
    # Bit Option for Property: SnapPointTypesEnabled
    # ------------------------------------------------------------------------------
    SnapPointTypesEnabled_UserDefined =     1
    SnapPointTypesEnabled_Inferred =     2
    SnapPointTypesEnabled_ScreenPosition =     4
    SnapPointTypesEnabled_EndPoint =     8
    SnapPointTypesEnabled_MidPoint =    16
    SnapPointTypesEnabled_ControlPoint =    32
    SnapPointTypesEnabled_Intersection =    64
    SnapPointTypesEnabled_ArcCenter =   128
    SnapPointTypesEnabled_QuadrantPoint =   256
    SnapPointTypesEnabled_ExistingPoint =   512
    SnapPointTypesEnabled_PointonCurve =  1024
    SnapPointTypesEnabled_PointonSurface =  2048
    SnapPointTypesEnabled_PointConstructor =  4096
    SnapPointTypesEnabled_TwocurveIntersection =  8192
    SnapPointTypesEnabled_TangentPoint = 16384
    SnapPointTypesEnabled_Poles = 32768
    # ------------------------------------------------------------------------------
    # Bit Option for Property: SnapPointTypesOnByDefault
    # ------------------------------------------------------------------------------
    SnapPointTypesOnByDefault_UserDefined =     1
    SnapPointTypesOnByDefault_Inferred =     2
    SnapPointTypesOnByDefault_ScreenPosition =     4
    SnapPointTypesOnByDefault_EndPoint =     8
    SnapPointTypesOnByDefault_MidPoint =    16
    SnapPointTypesOnByDefault_ControlPoint =    32
    SnapPointTypesOnByDefault_Intersection =    64
    SnapPointTypesOnByDefault_ArcCenter =   128
    SnapPointTypesOnByDefault_QuadrantPoint =   256
    SnapPointTypesOnByDefault_ExistingPoint =   512
    SnapPointTypesOnByDefault_PointonCurve =  1024
    SnapPointTypesOnByDefault_PointonSurface =  2048
    SnapPointTypesOnByDefault_PointConstructor =  4096
    SnapPointTypesOnByDefault_TwocurveIntersection =  8192
    SnapPointTypesOnByDefault_TangentPoint = 16384
    SnapPointTypesOnByDefault_Poles = 32768
    
    # ------------------------------------------------------------------------------
    # Constructor for NX Styler class
    # ------------------------------------------------------------------------------
    def __init__(self):
        # class members
        self.theSession = None
        self.theUI = None
        self.theDialogName = ""
        self.theDialog = None
        self.group0 = None # Block type: Group
        self.blockHeight = None # Block type: Double
        self.blockWidth = None # Block type: Double
        self.blockLength = None # Block type: Double
        self.blockOrigin = None # Block type: Specify Point
        self.blockColor = None # Block type: Color Picker
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.theDialogName = "ColoredBlock.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDialogName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            raise ex
    
    # ------------------------------------------------------------------------------
    # This method shows the dialog on the screen
    # ------------------------------------------------------------------------------
    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    
    # ------------------------------------------------------------------------------
    # Method Name: Dispose
    # ------------------------------------------------------------------------------
    def Dispose(self):
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None
    
    # ------------------------------------------------------------------------------
    # ---------------------Block Styler Callback defs--------------------------
    # ------------------------------------------------------------------------------
    
    # ------------------------------------------------------------------------------
    # Callback Name: initialize_cb
    # ------------------------------------------------------------------------------
    def initialize_cb(self):
        try:
            self.group0 = self.theDialog.TopBlock.FindBlock("group0")
            self.blockHeight = self.theDialog.TopBlock.FindBlock("blockHeight")
            self.blockWidth = self.theDialog.TopBlock.FindBlock("blockWidth")
            self.blockLength = self.theDialog.TopBlock.FindBlock("blockLength")
            self.blockOrigin = self.theDialog.TopBlock.FindBlock("blockOrigin")
            self.blockColor = self.theDialog.TopBlock.FindBlock("blockColor")

            #  Set the upper-limits and lower-limits
            self.blockHeight.MaximumValue = 100000.0
            self.blockHeight.MinimumValue = 0.001
            self.blockHeight.Value = 100.0
            
            self.blockWidth.MaximumValue = 100000.0
            self.blockWidth.MinimumValue = 0.001
            self.blockWidth.Value = 100.0
            
            self.blockLength.MaximumValue = 100000.0
            self.blockLength.MinimumValue = 0.001
            self.blockLength.Value = 100.0

        except Exception as ex:
        
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    
    # ------------------------------------------------------------------------------
    # Callback Name: dialogShown_cb
    # This callback is executed just before the dialog launch. Thus any value set 
    # here will take precedence and dialog will be launched showing that value. 
    # ------------------------------------------------------------------------------
    def dialogShown_cb(self):
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
        
            # ---- Enter your exception handling code here -----
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    
    # ------------------------------------------------------------------------------
    # Callback Name: apply_cb
    # ------------------------------------------------------------------------------
    def apply_cb(self):
        errorCode = 0
        blockFeatureBuilder1 = None

        try:
            workPart = self.theSession.Parts.Work

            # Get the values from UI Blocks
            theHeight = self.blockHeight.Value
            theWidth = self.blockWidth.Value
            theLength = self.blockLength.Value
            originPoint = self.blockOrigin.Point
            color = self.blockColor.GetValue()

            nullFeatures_Feature = NXOpen.Features.Feature.Null
            blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(nullFeatures_Feature)
            blockFeatureBuilder1.SetOriginAndLengths(
                originPoint, str(theLength), str(theHeight), str(theWidth))
            feature1 = blockFeatureBuilder1.CommitFeature()

            # Get the body from Feature
            bodyFeat = feature1
            bodies = bodyFeat.GetBodies()
            # Apply the color to feature body
            displayModification1 = self.theSession.DisplayManager.NewDisplayModification()
            displayModification1.ApplyToAllFaces = True
            displayModification1.NewColor = color[0]
            objects1 = []
            objects1.append(bodies[0])
            displayModification1.Apply(objects1)
            displayModification1.Dispose()

        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show("Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        finally:
            if not blockFeatureBuilder1 == None:
                blockFeatureBuilder1.Destroy()
        return errorCode
    
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
#             e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
# 
#     You can create the dialog using the following method:
# 
#     1. Journal Replay
# 
#         1) Replay this file through Tool->Journal->Play Menu.
# 
# ------------------------------------------------------------------------------
def main():
    try:
        theColoredBlock = ColoredBlock()
        #  The following method shows the dialog immediately
        theColoredBlock.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        NXOpen.UI.GetUI().NXMessageBox.Show(
            "Block Styler", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    finally:
        theColoredBlock.Dispose()

if __name__ == "__main__":
    main()


