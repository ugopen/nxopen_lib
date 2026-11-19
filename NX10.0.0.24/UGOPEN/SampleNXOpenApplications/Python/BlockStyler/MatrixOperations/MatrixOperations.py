# ===================================================================
#
#             Copyright (c) 2008  Siemens PLM Software
#               Unpublished - All rights reserved
#
# ===================================================================
# *******************************************************************
# Description
# ==============
# This example demonstrates the usage of Block Styler Application in NX.
# The set of APIs designed for Block Styler application are property based. 
# While using these APIs one must be aware about the Block, its associated 
# properties and their datatypes.

# This program uses UI Blocks like 
# - DoubleTable,    - Enumeration,    - Double, 
# - Toggle,         - SpecifyVector,  - AngularDim.

# Executing this example will launch a dialog which allows you to perform 
# Matrix operations like
# - Multiplication       - Addition            - Determinant   -Transpose   
# - OrthoNormalize       - RotateAboutAxis     - VectorMultiply
# - X-direction Vector   - Y-direction Vector  - Z-direction Vector

# This sample program uses UFwrappers (NXOpen.UF APIs) to perform matrix operations. 
#    
#
#
# *******************************************************************

# ------------------------------------------------------------------------------
# These imports are needed for the following template code
# ------------------------------------------------------------------------------
import os.path
import sys
import traceback
import NXOpen
import NXOpen.UF
import NXOpen.BlockStyler

# ------------------------------------------------------------------------------
# Represents Block Styler application class
# ------------------------------------------------------------------------------
class MatrixOperations:
    
    # ------------------------------------------------------------------------------
    # Constructor for NX Styler class
    # ------------------------------------------------------------------------------
    def __init__(self):
        self.theSession = None
        self.theUI = None
        self.theUfSession = None
        self.theDialogName = ""
        self.theDialog = None
        self.SelectOperationsGroup = None #  Block type: Group
        self.SelectOperation = None #  Block type: Enumeration
        self.Input = None #  Block type: Group
        self.Matrix1Group = None #  Block type: Group
        self.Matrix1 = None #  Block type: Double Table
        self.Matrix2Group = None #  Block type: Group
        self.Matrix2 = None #  Block type: Double Table
        self.VectorGroup = None #  Block type: Group
        self.AllowSelection = None #  Block type: Toggle
        self.SelectVector = None #  Block type: Specify Vector
        self.Vector1 = None #  Block type: Double Table
        self.EnterAngle = None #  Block type: Group
        self.Angle1 = None #  Block type: Angular Dim
        self.Angle = None #  Block type: Double
        self.ResultGroup = None #  Block type: Group
        self.ResultMatrix = None #  Block type: Double Table
        self.ResultVector = None #  Block type: Double Table
        self.ResultDouble = None #  Block type: Double
        try:
            self.theSession = NXOpen.Session.GetSession()
            self.theUI = NXOpen.UI.GetUI()
            self.theUfSession = NXOpen.UF.UFSession.GetUFSession()
            self.theDialogName = "MatrixOperations.dlx"
            self.theDialog = self.theUI.CreateDialog(self.theDialogName)
            self.theDialog.AddApplyHandler(self.apply_cb)
            self.theDialog.AddOkHandler(self.ok_cb)
            self.theDialog.AddUpdateHandler(self.update_cb)
            self.theDialog.AddInitializeHandler(self.initialize_cb)
            self.theDialog.AddDialogShownHandler(self.dialogShown_cb)
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            print(ex)
    
    # ------------------------------------------------------------------------------
    # This method shows the dialog on the screen
    # ------------------------------------------------------------------------------
    def Show(self):
        try:
            self.theDialog.Show()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
             self.theUI.NXMessageBox.Show("Show", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    
    # ------------------------------------------------------------------------------
    # Method Name: Dispose
    # ------------------------------------------------------------------------------
    def Dispose(self):
        if self.theDialog != None:
            self.theDialog.Dispose()
            self.theDialog = None
    
    # ------------------------------------------------------------------------------
    # ---------------------Block Styler Callback Functions--------------------------
    # ------------------------------------------------------------------------------
    
    # ------------------------------------------------------------------------------
    # Callback Name: initialize_cb
    # ------------------------------------------------------------------------------
    def initialize_cb(self):
        try:
            self.SelectOperationsGroup = self.theDialog.TopBlock.FindBlock("SelectOperationsGroup")
            self.SelectOperation = self.theDialog.TopBlock.FindBlock("SelectOperation")
            self.Input = self.theDialog.TopBlock.FindBlock("Input")
            self.Matrix1Group = self.theDialog.TopBlock.FindBlock("Matrix1Group")
            self.Matrix1 = self.theDialog.TopBlock.FindBlock("Matrix1")
            self.Matrix2Group = self.theDialog.TopBlock.FindBlock("Matrix2Group")
            self.Matrix2 = self.theDialog.TopBlock.FindBlock("Matrix2")
            self.VectorGroup = self.theDialog.TopBlock.FindBlock("VectorGroup")
            self.AllowSelection = self.theDialog.TopBlock.FindBlock("AllowSelection")
            self.SelectVector = self.theDialog.TopBlock.FindBlock("SelectVector")
            self.Vector1 = self.theDialog.TopBlock.FindBlock("Vector1")
            self.EnterAngle = self.theDialog.TopBlock.FindBlock("EnterAngle")
            self.Angle1 = self.theDialog.TopBlock.FindBlock("Angle1")
            self.Angle = self.theDialog.TopBlock.FindBlock("Angle")
            self.ResultGroup = self.theDialog.TopBlock.FindBlock("ResultGroup")
            self.ResultMatrix = self.theDialog.TopBlock.FindBlock("ResultMatrix")
            self.ResultVector = self.theDialog.TopBlock.FindBlock("ResultVector")
            self.ResultDouble = self.theDialog.TopBlock.FindBlock("ResultDouble")
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("initialize_cb", NXOpen.NXMessageBox.DialogType.Error, str(ex))

    # ------------------------------------------------------------------------------
    # Callback Name: dialogShown_cb
    # This callback is executed just before the dialog launch. Thus any value set 
    # here will take precedence and dialog will be launched showing that value. 
    # ------------------------------------------------------------------------------
    def dialogShown_cb(self):
        try:	  
            self.UpdateDialog()
            # ---- Enter your callback code here -----
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("dialogShown_cb", NXOpen.NXMessageBox.DialogType.Error, str(ex))
    
    # ------------------------------------------------------------------------------
    # Callback Name: apply_cb
    # ------------------------------------------------------------------------------
    def apply_cb(self):
        errorCode = 0
        try:
            # ---- Enter your callback code here -----
            pass
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            traceback.print_exc()
            errorCode = 1
            self.theUI.NXMessageBox.Show("apply_cb", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return errorCode
    
    # ------------------------------------------------------------------------------
    # Callback Name: update_cb
    # ------------------------------------------------------------------------------
    def update_cb(self, block):
        try:
            # ---- Enter your code here -----
            AllowSelectionProperties = self.AllowSelection.GetProperties()
            SelectVectorProperties = self.SelectVector.GetProperties()
            Vector1Properties = self.Vector1.GetProperties()
            SelectedVec = NXOpen.Vector3d()
            vector1values = []

            if block == self.AllowSelection:
                vector1values = Vector1Properties.GetDoubleMatrix("Values", 1, 3)
                SelectedVec.X = vector1values[0]
                SelectedVec.Y = vector1values[1]
                SelectedVec.Z = vector1values[2]
                SelectVectorProperties.SetVector("Vector", SelectedVec)
                SelectVectorProperties.SetLogical("Show", AllowSelectionProperties.GetLogical("Value"))
            elif block == self.SelectVector:
                SelectedVec = SelectVectorProperties.GetVector("Vector")
                vector1values[0] = SelectedVec.X
                vector1values[1] = SelectedVec.Y
                vector1values[2] = SelectedVec.Z
                Vector1Properties.SetDoubleMatrix("Values", 1, 3, vector1values) # vector1values)

            self.UpdateDialog()

            # Dispose the properties once use is over
            AllowSelectionProperties.Dispose()
            SelectVectorProperties.Dispose()
            Vector1Properties.Dispose()

        except Exception as ex:
            # ---- Enter your exception handling code here -----
            traceback.print_exc()
            self.theUI.NXMessageBox.Show("update_cb", NXOpen.NXMessageBox.DialogType.Error, str(ex))

        return 0
    
    # ------------------------------------------------------------------------------
    # Callback Name: ok_cb
    # ------------------------------------------------------------------------------
    def ok_cb(self):
        errorCode = 0
        try:
            # ---- Enter your callback code here -----
            errorCode = self.apply_cb()
        except Exception as ex:
            # ---- Enter your exception handling code here -----
            errorCode = 1
            self.theUI.NXMessageBox.Show("ok_cb", NXOpen.NXMessageBox.DialogType.Error, str(ex))
        return errorCode

    # This subroutine updates the dialog 
    def UpdateDialog(self):

        #theUfSession = UFSession.GetUFSession()

        Matrix1GroupProperties = self.Matrix1Group.GetProperties()
        Matrix2GroupProperties = self.Matrix2Group.GetProperties()
        EnterAngleProperties = self.EnterAngle.GetProperties()
        VectorGroupProperties = self.VectorGroup.GetProperties()

        Matrix1Properties = self.Matrix1.GetProperties()
        Matrix2Properties = self.Matrix2.GetProperties()
        Vector1Properties = self.Vector1.GetProperties()
        AngleProperties = self.Angle1.GetProperties()

        ResultMatrixProperties = self.ResultMatrix.GetProperties()
        ResultVectorProperties = self.ResultVector.GetProperties()
        ResultDoubleProperties = self.ResultDouble.GetProperties()

        #matrix1values = Matrix1Properties.GetDoubleMatrix("Values", 3, 3)
        #matrix2values = Matrix2Properties.GetDoubleMatrix("Values", 3, 3)
        #vector1values = Vector1Properties.GetDoubleMatrix("Values", 1, 3)
        matrix1values, nRows1, nCols1 = Matrix1Properties.GetDoubleMatrix("Values")
        matrix2values, nRows2, nCols2 = Matrix2Properties.GetDoubleMatrix("Values")
        vector1values, nVecRows, nVecCols = Vector1Properties.GetDoubleMatrix("Values")
        anglevalue = AngleProperties.GetDouble("Value")

        matrixResultValues = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        vectorResultValues = [0.0, 0.0, 0.0]

        determinant = 0.0

        SelectOperationProperties = self.SelectOperation.GetProperties()
        matrixOperation = SelectOperationProperties.GetEnumAsString("Value")

        if matrixOperation == "Multiplication":

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", True)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            matrixResultValues = self.theUfSession.Mtx3.Multiply(matrix1values, matrix2values)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrixResultValues)

        elif matrixOperation == "Addition":

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", True)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            matrixResultValues = self.MatrixAddition3x3(matrix1values, matrix2values)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrixResultValues)

        elif matrixOperation == "Determinant":

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", True)

            determinant = self.theUfSession.Mtx3.Determinant(matrix1values)
            ResultDoubleProperties.SetDouble("Value", determinant)

        elif matrixOperation == "Transpose":
            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            matrixResultValues = self.theUfSession.Mtx3.Transpose(matrix1values)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrixResultValues)

        elif matrixOperation == "OrthoNormalize":

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            matrix1values = self.theUfSession.Mtx3.OrthoNormalize(matrix1values)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrix1values)

        elif matrixOperation == "RotateAboutAxis":

            Matrix1GroupProperties.SetLogical("Show", False)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", True)
            VectorGroupProperties.SetLogical("Show", True)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            matrixResultValues = self.theUfSession.Mtx3.RotateAboutAxis(vector1values, anglevalue)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrixResultValues)

        elif matrixOperation == "VectorMultiply":

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", True)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", True)
            ResultDoubleProperties.SetLogical("Show", False)

            vectorResultValues = self.theUfSession.Mtx3.VecMultiply(vector1values, matrix1values)
            ResultVectorProperties.SetDoubleMatrix("Values", 1, 3, vectorResultValues)

        elif matrixOperation == "X-direction Vector":

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", True)
            ResultDoubleProperties.SetLogical("Show", False)

            vectorResultValues = self.theUfSession.Mtx3.XVec(matrix1values)
            ResultVectorProperties.SetDoubleMatrix("Values", 1, 3, vectorResultValues)

        elif matrixOperation == "Y-direction Vector":

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", True)
            ResultDoubleProperties.SetLogical("Show", False)

            vectorResultValues = self.theUfSession.Mtx3.YVec(matrix1values)
            ResultVectorProperties.SetDoubleMatrix("Values", 1, 3, vectorResultValues)

        elif matrixOperation == "Z-direction Vector":

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", True)
            ResultDoubleProperties.SetLogical("Show", False)

            vectorResultValues = self.theUfSession.Mtx3.ZVec(matrix1values)
            ResultVectorProperties.SetDoubleMatrix("Values", 1, 3, vectorResultValues)

        SelectOperationProperties.Dispose()

        Matrix1GroupProperties.Dispose()
        Matrix2GroupProperties.Dispose()
        EnterAngleProperties.Dispose()
        VectorGroupProperties.Dispose()

        Matrix1Properties.Dispose()
        Matrix2Properties.Dispose()
        Vector1Properties.Dispose()
        AngleProperties.Dispose()

        ResultMatrixProperties.Dispose()
        ResultVectorProperties.Dispose()
        ResultDoubleProperties.Dispose()

    #def MatrixAddition3x3(ByVal matrix1 As Double(), ByVal matrix2 As Double()) As Double()
    def MatrixAddition3x3(self, matrix1, matrix2):
        additionMatrix = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        for ii in range(9):
            additionMatrix[ii] = matrix1[ii] + matrix2[ii]
        return additionMatrix
    
# ------------------------------- DIALOG LAUNCHING ---------------------------------
# 
#     Before invoking this application one needs to open any part/empty part in NX
#     because of the behavior of the blocks.
# 
#     Make sure that dlx file should exist at one of following location
#        1.) From where NX session is launched
#        2.) $UGII_USER_DIR/application
#        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
#            recommended. This variable is set to a full directory path to a file 
#            containing a list of root directories for all custom applications.
#            e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
#     You can create the dialog using one of the following way:
# 
#     1. Journal Replay
# 
#         1) Replay this file through Tool->Journal->Play Menu.
# 
#     2. USER EXIT
# 
#         1) Create the Shared Library -- Refer "Block Styler programmer# s guide"
#         2) Invoke the Shared Library through File->Execute->NX Open menu.
# 
# ------------------------------------------------------------------------------
def main():
    try:
        theMatrixOperations = MatrixOperations()
        #  The following method shows the dialog immediately
        theMatrixOperations.Show()
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        traceback.print_exc()
        print(ex)
    finally:
        theMatrixOperations.Dispose()

if __name__ == '__main__':
    main()


