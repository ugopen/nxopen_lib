'=============================================================================
'
'      Copyright (c) 2012 Siemens Product Lifecycle Management Software Inc
'                    Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'
'------------------------------------------------------------------------------
'These imports are needed for the following template code
'------------------------------------------------------------------------------
Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.BlockStyler

'------------------------------------------------------------------------------
'Represents Block Styler application class
'------------------------------------------------------------------------------
Public Class DimensionUDB
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Private theDlxFileName As String
    Private theUserDefinedUIBlock As NXOpen.BlockStyler.BlockDialog
    Private sensitiveFlag As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private Dimension As NXOpen.BlockStyler.UIBlock ' Block type: Double

#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try

            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDlxFileName = "DimensionUDB.dlx"
            theUserDefinedUIBlock = theUI.CreateDialog(theDlxFileName)
            theUserDefinedUIBlock.AddUpdateHandler(AddressOf update_cb)
            theUserDefinedUIBlock.AddInitializeHandler(AddressOf initialize_cb)
            theUserDefinedUIBlock.AddEnableOKButtonHandler(AddressOf enableOKButton_cb)
            theUserDefinedUIBlock.AddDialogShownHandler(AddressOf dialogShown_cb)

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            Throw ex
        End Try
    End Sub
#End Region

    '------------------------------------------------------------------------------

    '------------------------------------------------------------------------------
    'Method Name: Dispose
    '------------------------------------------------------------------------------
    Public Sub Dispose()
        If theUserDefinedUIBlock IsNot Nothing Then
            theUserDefinedUIBlock.Dispose()
            theUserDefinedUIBlock = Nothing
        End If
    End Sub

    '------------------------------------------------------------------------------
    '---------------------Block UI Styler Callback Functions--------------------------
    '------------------------------------------------------------------------------

    '------------------------------------------------------------------------------
    'Callback Name: initialize_cb
    '------------------------------------------------------------------------------
    Public Sub initialize_cb()
        Try

            sensitiveFlag = theUserDefinedUIBlock.TopBlock.FindBlock("sensitiveFlag")
            Dimension = theUserDefinedUIBlock.TopBlock.FindBlock("Dimension")

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

            '---- Enter your callback code here -----

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try

            If block Is sensitiveFlag Then
                '---- Enter your code here -----
                Dim prop As PropertyList = sensitiveFlag.GetProperties()
                Dim flag As Boolean = prop.GetLogical("Value")
                prop.Dispose()

                'Disable double block if toggle field is on
                Dim dimensionPropertyList As PropertyList = Dimension.GetProperties()
                dimensionPropertyList.SetLogical("Enable", Not flag)
                dimensionPropertyList.Dispose()

            ElseIf block Is Dimension Then
                '---- Enter your code here -----

            End If

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        update_cb = 0
    End Function

    '------------------------------------------------------------------------------
    'Callback Name: enableOKButton_cb
    'This callback allows the dialog to enable/disable the OK and Apply button.
    '
    '------------------------------------------------------------------------------
    Public Function enableOKButton_cb() As Boolean
        enableOKButton_cb = True
        Try

            '---- Enter your callback code here -----
            'If the dimension value is zero then do not enable the OK/Apply button
            Dim prop As PropertyList = Dimension.GetProperties()
            Dim value As Double = prop.GetDouble("Value")
            prop.Dispose()

            If value = 0 Then
                enableOKButton_cb = False
            End If

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Function

    '------------------------------------------------------------------------------
    'Function Name: RegisterUserDefinedUIBlock
    'Registers itself to the dialog which contains this block
    '------------------------------------------------------------------------------
    Public Shared Function RegisterUserDefinedUIBlock(ByVal parentDialog As NXOpen.BlockStyler.BlockDialog, ByVal blockID As String) As DimensionUDB
        Dim theDimensionUDB As DimensionUDB = New DimensionUDB()
        parentDialog.RegisterUserDefinedUIBlock(theDimensionUDB.theUserDefinedUIBlock, blockID)
        Return theDimensionUDB
    End Function

    '------------------------------------------------------------------------------
    'Property Name: TopBlock
    'ReadOnly property to give access to TopBlock
    '------------------------------------------------------------------------------
    Public ReadOnly Property TopBlock() As NXOpen.BlockStyler.CompositeBlock
        Get
            If theUserDefinedUIBlock IsNot Nothing Then
                Return theUserDefinedUIBlock.TopBlock
            Else
                Return Nothing
            End If
        End Get
    End Property

    '------------------------------------------------------------------------------
    'Function Name: SetLabel
    'Sets the label on the double block
    '------------------------------------------------------------------------------
    Public Sub SetLabel(ByVal label As String)
        Dim prop As PropertyList = Dimension.GetProperties()
        prop.SetString("Label", label)
        prop.Dispose()
    End Sub

    '------------------------------------------------------------------------------
    'Function Name: GetValue
    'Gets the value of the double block
    '------------------------------------------------------------------------------
    Public Function GetValue(val As String) As Double
        Dim prop As PropertyList = Dimension.GetProperties()
        Dim value As Double = prop.GetDouble("Value")
        prop.Dispose()
        Return value
    End Function
    '------------------------------------------------------------------------------
    'Function Name: SetValue
    'Sets the value of the double block
    '------------------------------------------------------------------------------
    Public Function SetValue(ByVal val As Double) As Boolean
        SetValue = True
        Dim prop As PropertyList = Dimension.GetProperties()
        prop.SetDouble("Value", val)
        prop.Dispose()
    End Function
    '------------------------------------------------------------------------------
    'Enables/Disables the double block based on toggle. If toggled on, the double-field is disabled
    '------------------------------------------------------------------------------
    Public Function EnableDimensionField() As Boolean
        EnableDimensionField = True
        Dim plist As PropertyList = sensitiveFlag.GetProperties()
        Dim flag As Boolean = plist.GetLogical("Value")
        plist.Dispose()
        plist = Dimension.GetProperties()
        If flag = True Then
            plist.SetLogical("Enable", False)
        Else
            plist.SetLogical("Enable", True)
        End If
        plist.Dispose()
    End Function
End Class
