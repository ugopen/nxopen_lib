' ===================================================================
'
'             Copyright (c) 2008  Siemens PLM Software
'               Unpublished - All rights reserved
'
' ===================================================================
' *******************************************************************
' Description
'==============
'This example demonstartes usage of Block Styler Application in NX.
'The set of APIs designed for Block Styler application are property based. 
'While using these APIs one must be aware about the Block, its associated 
'properties and their datatype.

'This program uses UI Blocks like 
'- DoubleTable,    - Enumuration,    - Double, 
'- Toggle,         - SpecifyVector,  - AngularDim.

'Executing this example will launch a dialog which allows you to perform 
'Matrix operations like
'- Multiplication       - Addition            - Determinant   -Transpose   
'- OrthoNormalize       - RotateAboutAxis     - VectorMultiply
'- X-direction Vector   - Y-direction Vector  - Z-direction Vector

'This sample program uses UFwrappers (NXOpen.UF APIs) to perform matrix operations. 
'    
'
'
' *******************************************************************

'------------------------------------------------------------------------------
'These imports are needed for the following template code
'------------------------------------------------------------------------------
Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.BlockStyler

'------------------------------------------------------------------------------
'Represents Block Styler application class
'------------------------------------------------------------------------------
Public Class MatrixOperations
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Public Shared theMatrixOperations As MatrixOperations
    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private SelectOperationsGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private SelectOperation As NXOpen.BlockStyler.UIBlock' Block type: Enumeration
    Private Input As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private Matrix1Group As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private Matrix1 As NXOpen.BlockStyler.UIBlock' Block type: Double Table
    Private Matrix2Group As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private Matrix2 As NXOpen.BlockStyler.UIBlock' Block type: Double Table
    Private VectorGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private AllowSelection As NXOpen.BlockStyler.UIBlock' Block type: Toggle
    Private SelectVector As NXOpen.BlockStyler.UIBlock' Block type: Specify Vector
    Private Vector1 As NXOpen.BlockStyler.UIBlock' Block type: Double Table
    Private EnterAngle As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private Angle1 As NXOpen.BlockStyler.UIBlock' Block type: Angular Dim
    Private Angle As NXOpen.BlockStyler.UIBlock' Block type: Double
    Private ResultGroup As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private ResultMatrix As NXOpen.BlockStyler.UIBlock' Block type: Double Table
    Private ResultVector As NXOpen.BlockStyler.UIBlock' Block type: Double Table
    Private ResultDouble As NXOpen.BlockStyler.UIBlock' Block type: Double
    
#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        
            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDialogName = "MatrixOperations.dlx"
            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddOkHandler(AddressOf ok_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddInitializeHandler(AddressOf initialize_cb)
            theDialog.AddDialogShownHandler(AddressOf dialogShown_cb)
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            Throw ex
        End Try
    End Sub
#End Region
    
    '------------------------------- DIALOG LAUNCHING ---------------------------------
    '
    '    Before invoking this application one needs to open any part/empty part in NX
    '    because of the behavior of the blocks.
    '
    '    Make sure that dlx file should exist at one of following location
    '       1.) From where NX session is launched
    '       2.) $UGII_USER_DIR/application
    '       3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    '           recommended. This variable is set to a full directory path to a file 
    '           containing a list of root directories for all custom applications.
    '           e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
    '    You can create the dialog using one of the following way:
    '
    '    1. Journal Replay
    '
    '        1) Replay this file through Tool->Journal->Play Menu.
    '
    '    2. USER EXIT
    '
    '        1) Create the Shared Library -- Refer "Block Styler programmer's guide"
    '        2) Invoke the Shared Library through File->Execute->NX Open menu.
    '
    '------------------------------------------------------------------------------
    Public Shared Sub Main()
        Try

            theMatrixOperations = New MatrixOperations()
            ' The following method shows the dialog immediately
            theMatrixOperations.Show()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            theMatrixOperations.Dispose()
        End Try
    End Sub
    '------------------------------------------------------------------------------
    ' This method specifies how a shared image is unloaded from memory
    ' within NX. This method gives you the capability to unload an
    ' internal NX Open application or user  exit from NX. Specify any
    ' one of the three constants as a return value to determine the type
    ' of unload to perform:
    '
    '
    '    Immediately : unload the library as soon as the automation program has completed
    '    Explicitly  : unload the library from the "Unload Shared Image" dialog
    '    AtTermination : unload the library when the NX session terminates
    '
    '
    ' NOTE:  A program which associates NX Open applications with the menubar
    ' MUST NOT use this option since it will UNLOAD your NX Open application image
    ' from the menubar.
    '------------------------------------------------------------------------------
    Public Shared Function GetUnloadOption(ByVal arg As String) As Integer
        'Return CType(Session.LibraryUnloadOption.Explicitly, Integer)
         Return CType(Session.LibraryUnloadOption.Immediately, Integer)
        ' Return CType(Session.LibraryUnloadOption.AtTermination, Integer)
    End Function
    '------------------------------------------------------------------------------
    ' Following method cleanup any housekeeping chores that may be needed.
    ' This method is automatically called by NX.
    '------------------------------------------------------------------------------
    Public Shared Sub UnloadLibrary(ByVal arg As String)
        Try


        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'This method shows the dialog on the screen
    '------------------------------------------------------------------------------
    Public Sub Show()
        Try
        
            theDialog.Show
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Method Name: Dispose
    '------------------------------------------------------------------------------
    Public Sub Dispose()
        If theDialog IsNot Nothing Then 
            theDialog.Dispose()
            theDialog = Nothing
        End If
    End Sub
    
    '------------------------------------------------------------------------------
    '---------------------Block Styler Callback Functions--------------------------
    '------------------------------------------------------------------------------
    
    '------------------------------------------------------------------------------
    'Callback Name: initialize_cb
    '------------------------------------------------------------------------------
    Public Sub initialize_cb()
        Try
        
            SelectOperationsGroup = theDialog.TopBlock.FindBlock("SelectOperationsGroup")
            SelectOperation = theDialog.TopBlock.FindBlock("SelectOperation")
            Input = theDialog.TopBlock.FindBlock("Input")
            Matrix1Group = theDialog.TopBlock.FindBlock("Matrix1Group")
            Matrix1 = theDialog.TopBlock.FindBlock("Matrix1")
            Matrix2Group = theDialog.TopBlock.FindBlock("Matrix2Group")
            Matrix2 = theDialog.TopBlock.FindBlock("Matrix2")
            VectorGroup = theDialog.TopBlock.FindBlock("VectorGroup")
            AllowSelection = theDialog.TopBlock.FindBlock("AllowSelection")
            SelectVector = theDialog.TopBlock.FindBlock("SelectVector")
            Vector1 = theDialog.TopBlock.FindBlock("Vector1")
            EnterAngle = theDialog.TopBlock.FindBlock("EnterAngle")
            Angle1 = theDialog.TopBlock.FindBlock("Angle1")
            Angle = theDialog.TopBlock.FindBlock("Angle")
            ResultGroup = theDialog.TopBlock.FindBlock("ResultGroup")
            ResultMatrix = theDialog.TopBlock.FindBlock("ResultMatrix")
            ResultVector = theDialog.TopBlock.FindBlock("ResultVector")
            ResultDouble = theDialog.TopBlock.FindBlock("ResultDouble")


        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub		
    '------------------------------------------------------------------------------
    'Callback Name: dialogShown_cb
    'This callback is executed just before the dialog launch. Thus any value set 
    'here will take precedence and dialog will be launched showing that value. 
    '------------------------------------------------------------------------------
    Public Sub dialogShown_cb()
        Try	  
            UpdateDialog()
        
            '---- Enter your callback code here -----
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
             theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub
    
    '------------------------------------------------------------------------------
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer

        Dim errorCode As Integer = 0

        Try

            '---- Enter your callback code here -----

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

        apply_cb = errorCode

    End Function
    
    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try

            '---- Enter your code here -----
            Dim AllowSelectionProperties As BlockStyler.PropertyList = AllowSelection.GetProperties()
            Dim SelectVectorProperties As BlockStyler.PropertyList = SelectVector.GetProperties()
            Dim Vector1Properties As BlockStyler.PropertyList = Vector1.GetProperties()
            Dim SelectedVec As Vector3d = New Vector3d
            Dim vector1values(2) As Double

            If block Is AllowSelection Then
                vector1values = Vector1Properties.GetDoubleMatrix("Values", 1, 3)
                SelectedVec.X = vector1values(0)
                SelectedVec.Y = vector1values(1)
                SelectedVec.Z = vector1values(2)
                SelectVectorProperties.SetVector("Vector", SelectedVec)
                SelectVectorProperties.SetLogical("Show", AllowSelectionProperties.GetLogical("Value"))
            ElseIf block Is SelectVector Then
                SelectedVec = SelectVectorProperties.GetVector("Vector")
                vector1values(0) = SelectedVec.X
                vector1values(1) = SelectedVec.Y
                vector1values(2) = SelectedVec.Z
                Vector1Properties.SetDoubleMatrix("Values", 1, 3, vector1values) 'vector1values)
            End If

            UpdateDialog()

            'Dispose the properties once use is over
            AllowSelectionProperties.Dispose()
            SelectVectorProperties.Dispose()
            Vector1Properties.Dispose()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        update_cb = 0
    End Function
    
    '------------------------------------------------------------------------------
    'Callback Name: ok_cb
    '------------------------------------------------------------------------------
    Public Function ok_cb() As Integer

        Dim errorCode As Integer = 0

        Try

            '---- Enter your callback code here -----
            errorCode = apply_cb()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            errorCode = 1
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try

        ok_cb = errorCode

    End Function

 

    'This subroutine updates the dailog 
    Public Sub UpdateDialog()

        Dim theUfSession As UFSession = UFSession.GetUFSession()

        Dim Matrix1GroupProperties As BlockStyler.PropertyList = Matrix1Group.GetProperties()
        Dim Matrix2GroupProperties As BlockStyler.PropertyList = Matrix2Group.GetProperties()
        Dim EnterAngleProperties As BlockStyler.PropertyList = EnterAngle.GetProperties()
        Dim VectorGroupProperties As BlockStyler.PropertyList = VectorGroup.GetProperties()

        Dim Matrix1Properties As BlockStyler.PropertyList = Matrix1.GetProperties()
        Dim Matrix2Properties As BlockStyler.PropertyList = Matrix2.GetProperties()
        Dim Vector1Properties As BlockStyler.PropertyList = Vector1.GetProperties()
        Dim AngleProperties As BlockStyler.PropertyList = Angle1.GetProperties()

        Dim ResultMatrixProperties As BlockStyler.PropertyList = ResultMatrix.GetProperties()
        Dim ResultVectorProperties As BlockStyler.PropertyList = ResultVector.GetProperties()
        Dim ResultDoubleProperties As BlockStyler.PropertyList = ResultDouble.GetProperties()

        Dim matrix1values() As Double = Matrix1Properties.GetDoubleMatrix("Values", 3, 3)
        Dim matrix2values() As Double = Matrix2Properties.GetDoubleMatrix("Values", 3, 3)
        Dim vector1values() As Double = Vector1Properties.GetDoubleMatrix("Values", 1, 3)
        Dim anglevalue As Double = AngleProperties.GetDouble("Value")

        Dim matrixResultValues() As Double
        matrixResultValues = New Double() {0, 0, 0, 0, 0, 0, 0, 0, 0}

        Dim vectorResultValues() As Double
        vectorResultValues = New Double() {0, 0, 0}

        Dim determinant As Double = 0.0

        Dim SelectOperationProperties As BlockStyler.PropertyList = SelectOperation.GetProperties
        Dim matrixOperation As String = SelectOperationProperties.GetEnumAsString("Value")

        If matrixOperation.Equals("Multiplication") Then

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", True)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            theUfSession.Mtx3.Multiply(matrix1values, matrix2values, matrixResultValues)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrixResultValues)

        ElseIf matrixOperation.Equals("Addition") Then

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", True)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            matrixResultValues = MatrixAddition3x3(matrix1values, matrix2values)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrixResultValues)

        ElseIf matrixOperation.Equals("Determinant") Then

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", True)

            theUfSession.Mtx3.Determinant(matrix1values, determinant)
            ResultDoubleProperties.SetDouble("Value", determinant)

        ElseIf matrixOperation.Equals("Transpose") Then
            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            theUfSession.Mtx3.Transpose(matrix1values, matrixResultValues)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrixResultValues)

        ElseIf matrixOperation.Equals("OrthoNormalize") Then

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            theUfSession.Mtx3.OrthoNormalize(matrix1values)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrix1values)

        ElseIf matrixOperation.Equals("RotateAboutAxis") Then

            Matrix1GroupProperties.SetLogical("Show", False)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", True)
            VectorGroupProperties.SetLogical("Show", True)

            ResultMatrixProperties.SetLogical("Show", True)
            ResultVectorProperties.SetLogical("Show", False)
            ResultDoubleProperties.SetLogical("Show", False)

            theUfSession.Mtx3.RotateAboutAxis(vector1values, anglevalue, matrixResultValues)
            ResultMatrixProperties.SetDoubleMatrix("Values", 3, 3, matrixResultValues)


        ElseIf matrixOperation.Equals("VectorMultiply") Then

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", True)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", True)
            ResultDoubleProperties.SetLogical("Show", False)

            theUfSession.Mtx3.VecMultiply(vector1values, matrix1values, vectorResultValues)
            ResultVectorProperties.SetDoubleMatrix("Values", 1, 3, vectorResultValues)

        ElseIf matrixOperation.Equals("X-direction Vector") Then

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", True)
            ResultDoubleProperties.SetLogical("Show", False)

            theUfSession.Mtx3.XVec(matrix1values, vectorResultValues)
            ResultVectorProperties.SetDoubleMatrix("Values", 1, 3, vectorResultValues)

        ElseIf matrixOperation.Equals("Y-direction Vector") Then

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", True)
            ResultDoubleProperties.SetLogical("Show", False)

            theUfSession.Mtx3.YVec(matrix1values, vectorResultValues)
            ResultVectorProperties.SetDoubleMatrix("Values", 1, 3, vectorResultValues)

        ElseIf matrixOperation.Equals("Z-direction Vector") Then

            Matrix1GroupProperties.SetLogical("Show", True)
            Matrix2GroupProperties.SetLogical("Show", False)
            EnterAngleProperties.SetLogical("Show", False)
            VectorGroupProperties.SetLogical("Show", False)

            ResultMatrixProperties.SetLogical("Show", False)
            ResultVectorProperties.SetLogical("Show", True)
            ResultDoubleProperties.SetLogical("Show", False)

            theUfSession.Mtx3.ZVec(matrix1values, vectorResultValues)
            ResultVectorProperties.SetDoubleMatrix("Values", 1, 3, vectorResultValues)

        End If

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

    End Sub

    Public Function MatrixAddition3x3(ByVal matrix1 As Double(), ByVal matrix2 As Double()) As Double()
        Dim additionMatrix As Double() = {0, 0, 0, 0, 0, 0, 0, 0, 0}
        For I As Integer = 0 To 8
            additionMatrix(I) = matrix1(I) + matrix2(I)
        Next
        Return additionMatrix
    End Function

End Class

