'=============================================================================
'
'                   Copyright (c) 2008 Siemens PLM Software
'                    Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'

'==============================================================================
'  Purpose:  This TEMPLATE file contains VB.NET source to guide you in the
'  construction of your Block application dialog. The generation of your
'  dialog file (.dlx extension) is the first step towards dialog construction
'  within NX.  You must now create a NX Open application that
'  utilizes this file (.dlx).
'
'  The information in this file provides you with the following:
'
'  1.  Help on how to load and display your Block Styler dialog in NX
'      using APIs provided in NXOpen.BlockStyler namespace
'  2.  The empty callback methods (stubs) associated with your dialog items
'      have also been placed in this file. These empty methods have been
'      created simply to start you along with your coding requirements.
'      The method name, argument list and possible return values have already
'      been provided for you.
'==============================================================================

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
Public Class UpdateExample
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Public Shared theUpdateExample As UpdateExample
    Private theDialogName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private group0 As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private inputString As NXOpen.BlockStyler.UIBlock ' Block type: String
    Private includeNumber As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private number As NXOpen.BlockStyler.UIBlock ' Block type: Integer
    Private outputString As NXOpen.BlockStyler.UIBlock ' Block type: String
    Private group01 As NXOpen.BlockStyler.UIBlock' Block type: Group
    Private lockString As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    Private lockNumber As NXOpen.BlockStyler.UIBlock ' Block type: Toggle
    
#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        
            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDialogName = "UpdateExample.dlx"
            theDialog = theUI.CreateDialog(theDialogName)
            theDialog.AddApplyHandler(AddressOf apply_cb)
            theDialog.AddOkHandler(AddressOf ok_cb)
            theDialog.AddUpdateHandler(AddressOf update_cb)
            theDialog.AddCancelHandler(AddressOf cancel_cb)
            theDialog.AddFilterHandler(AddressOf filter_cb)
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
    '    Make sure the dlx file is in one of the following locations:
    '        1.) From where NX session is launched
    '        2.) $UGII_USER_DIR/application
    '        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    '            recommended. This variable is set to a full directory path to a file 
    '            containing a list of root directories for all custom applications.
    '            e.g., UGII_CUSTOM_DIRECTORY_FILE=<NX install directory>\ugii\menus\custom_dirs.dat
    '
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

            theUpdateExample = New UpdateExample()
            ' The following method shows the dialog immediately
            theUpdateExample.Show()

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            theUpdateExample.Dispose()
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

            theDialog.Show()

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

            group0 = theDialog.TopBlock.FindBlock("group0")
            inputString = theDialog.TopBlock.FindBlock("string0")
            includeNumber = theDialog.TopBlock.FindBlock("toggle0")
            number = theDialog.TopBlock.FindBlock("integer0")
            outputString = theDialog.TopBlock.FindBlock("string01")
            group01 = theDialog.TopBlock.FindBlock("group01")
            lockString = theDialog.TopBlock.FindBlock("toggle01")
            lockNumber = theDialog.TopBlock.FindBlock("toggle02")

            Dim inputStringProps As PropertyList = inputString.GetProperties()
            inputStringProps.SetString("Label", "Input String")
            inputStringProps.Dispose()
            inputStringProps = Nothing

            Dim outputStringProps As PropertyList = outputString.GetProperties()
            outputStringProps.SetString("Label", "Output String")
            outputStringProps.Dispose()
            outputStringProps = Nothing

            Dim lockStringProps As PropertyList = lockString.GetProperties()
            lockStringProps.SetString("Label", "Lock Input String")
            lockStringProps.Dispose()
            lockStringProps = Nothing


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
            Dim numberProps As PropertyList = number.GetProperties()
            Dim lockNumberProps As PropertyList = lockNumber.GetProperties()
            Dim includeNumberProps As PropertyList = includeNumber.GetProperties()
            numberProps.SetLogical("Enable", Not lockNumberProps.GetLogical("Value"))
            includeNumberProps.SetLogical("Enable", Not lockNumberProps.GetLogical("Value"))
            numberProps.Dispose()
            includeNumberProps.Dispose()
            lockNumberProps.Dispose()
            numberProps = Nothing
            includeNumberProps = Nothing
            lockNumberProps = Nothing

            Dim inputStringProps1 As PropertyList = inputString.GetProperties()
            Dim lockStringProps1 As PropertyList = lockString.GetProperties()
            inputStringProps1.SetLogical("Enable", Not lockStringProps1.GetLogical("Value"))
            inputStringProps1.Dispose()
            lockStringProps1.Dispose()
            inputStringProps1 = Nothing
            lockStringProps1 = Nothing


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

    '--------------------------------------------------------------------------------
    ' updateOutputString() - copies the input string to the output string and
    '                        optionally concatenates the number to the output string
    '--------------------------------------------------------------------------------
    Public Sub updateOutputString()
        Try
            'Get the input string and establish an empty number string

            Dim inputStringProps As PropertyList = inputString.GetProperties()
            Dim inputText As String = inputStringProps.GetString("Value")
            inputStringProps.Dispose()
            inputStringProps = Nothing

            Dim numberText As String = ""

            'If the include number toggle is ON (true)
            '  then get the number and create a string for it

            Dim includeNumberProps As PropertyList = includeNumber.GetProperties()
            If includeNumberProps.GetLogical("Value") Then
                Dim numberProps As PropertyList = number.GetProperties()
                Dim numberValue As Integer = numberProps.GetInteger("Value")
                numberText = " - " & numberValue.ToString
                numberProps.Dispose()
                numberProps = Nothing
            End If
            includeNumberProps.Dispose()
            includeNumberProps = Nothing

            'Set the output string to the concatenated input string and optional number string

            Dim outputStringProps = outputString.GetProperties()
            outputStringProps.SetString("Value", inputText & numberText)
            outputStringProps.Dispose()
            outputStringProps = Nothing

        Catch ex As Exception
            theUI.NXMessageBox.Show("Error Updating Output String", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    '------------------------------------------------------------------------------
    'Callback Name: update_cb
    '------------------------------------------------------------------------------
    Public Function update_cb(ByVal block As NXOpen.BlockStyler.UIBlock) As Integer
        Try
            'Any changes to the input string, number, or the include number toggle
            ' could result in a new output string

            If block Is inputString Then

                updateOutputString()

            ElseIf block Is includeNumber Then

                updateOutputString()

            ElseIf block Is number Then

                updateOutputString()

            ElseIf block Is outputString Then
                'The output string block is disabled and only used for display

            ElseIf block Is lockString Then
                'Enable or disable the input string block based on the state
                'of the string lock toggle block


                Dim inputStringProps As PropertyList = inputString.GetProperties()
                Dim lockStringProps As PropertyList = lockString.GetProperties()

                inputStringProps.SetLogical("Enable", _
                       Not lockStringProps.GetLogical("Value"))

                inputStringProps.Dispose()
                inputStringProps = Nothing
                lockStringProps.Dispose()
                lockStringProps = Nothing

            ElseIf block Is lockNumber Then
                'Enable or disable the number block based on the state
                'of the number lock toggle block

                Dim numberProps As PropertyList = number.GetProperties()
                Dim lockNumberProps As PropertyList = lockNumber.GetProperties()
                Dim includeNumberProps As PropertyList =includeNumber.GetProperties()

                numberProps.SetLogical("Enable", _
                       Not lockNumberProps.GetLogical("Value"))
                
                includeNumberProps.SetLogical("Enable", _
                       Not lockNumberProps.GetLogical("Value"))

                numberProps.Dispose()
                numberProps = Nothing
                lockNumberProps.Dispose()
                lockNumberProps = Nothing
                includeNumberProps.Dispose()
                includeNumberProps = Nothing

            End If
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

    '------------------------------------------------------------------------------
    'Callback Name: cancel_cb
    '------------------------------------------------------------------------------
    Public Function cancel_cb() As Integer
        Try

            '---- Enter your callback code here -----

        Catch ex As Exception

            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
        cancel_cb = 0
    End Function

    '------------------------------------------------------------------------------
    'Callback Name: filter_cb
    '------------------------------------------------------------------------------
    Public Function filter_cb(ByVal block As NXOpen.BlockStyler.UIBlock, ByVal selectedObject As NXOpen.TaggedObject) As Integer
        filter_cb = NXOpen.UF.UFConstants.UF_UI_SEL_ACCEPT
    End Function

End Class


