﻿'=============================================================================
'
'                   Copyright (c) 2016 Siemens PLM Solutions
'                     Unpublished - All rights reserved
'===============================================================================
'File description: Sample NX/Open Application for Block Styler
'===============================================================================
'
'==============================================================================
'  WARNING!!  This file is overwritten by the Block UI Styler while generating
'  the automation code. Any modifications to this file will be lost after
'  generating the code again.
'
'==============================================================================

'==============================================================================
'  Purpose:  This TEMPLATE file contains VB.NET source to guide you in the
'  construction of your Block application dialog. The generation of your
'  dialog file (.dlx extension) is the first step towards dialog construction
'  within NX.  You must now create a NX Open application that
'  utilizes this file (.dlx).
'
'  The information in this file provides you with the following:
'
'  1.  Help on how to load and display your Block UI Styler dialog in NX
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
Public Class TreeListWidthDemo
    'class members
    Private Shared theSession As Session
    Private Shared theUI As UI
    Private theDlxFileName As String
    Private theDialog As NXOpen.BlockStyler.BlockDialog
    Private group0 As NXOpen.BlockStyler.Group' Block type: Group
    Private tree_control0 As NXOpen.BlockStyler.Tree' Block type: Tree Control
    
#Region "Block Styler Dialog Designer generator code"
    '------------------------------------------------------------------------------
    'Constructor for NX Styler class
    '------------------------------------------------------------------------------
    Public Sub New()
        Try
        
            theSession = Session.GetSession()
            theUI = UI.GetUI()
            theDlxFileName = "TreeListWidthDemo.dlx"
            theDialog = theUI.CreateDialog(theDlxFileName)
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
    '    Make sure the dlx file is in one of the following locations:
    '        1.) From where NX session is launched
    '        2.) $UGII_USER_DIR/application
    '        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
    '            recommended. This variable is set to a full directory path to a file 
    '            containing a list of root directories for all custom applications.
    '            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
    '
    '    You can create the dialog using one of the following way:
    '
    '    1. Journal Replay
    '
    '        1) Replay this file through Tool->Journal->Play Menu.
    '
    '    2. USER EXIT
    '
    '        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
    '        2) Invoke the Shared Library through File->Execute->NX Open menu.
    '
    '------------------------------------------------------------------------------
    Public Shared Sub Main()
        Dim theTreeListWidthDemo As TreeListWidthDemo = Nothing
        Try
        
            theTreeListWidthDemo = New TreeListWidthDemo()
            ' The following method shows the dialog immediately
            theTreeListWidthDemo.Show()
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        Finally
            If theTreeListWidthDemo IsNot Nothing Then 
                theTreeListWidthDemo.Dispose()
                theTreeListWidthDemo = Nothing
            End If
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
    '---------------------Block UI Styler Callback Functions--------------------------
    '------------------------------------------------------------------------------
    
    '------------------------------------------------------------------------------
    'Callback Name: initialize_cb
    '------------------------------------------------------------------------------
    Public Sub initialize_cb()
        Try
        
            group0 = CType(theDialog.TopBlock.FindBlock("group0"), NXOpen.BlockStyler.Group)
            tree_control0 = CType(theDialog.TopBlock.FindBlock("tree_control0"), NXOpen.BlockStyler.Tree)

            tree_control0.width=500
            tree_control0.canStretchWidth = True

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
    'Callback Name: apply_cb
    '------------------------------------------------------------------------------
    Public Function apply_cb() As Integer
        Dim errorCode as Integer = 0
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
        Dim errorCode as Integer = 0
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
    'Function Name: GetBlockProperties
    'Returns the propertylist of the specified BlockID
    '------------------------------------------------------------------------------
    Public Function GetBlockProperties(ByVal blockID As String) As PropertyList
        GetBlockProperties = Nothing
        Try
        
            GetBlockProperties = theDialog.GetBlockProperties(blockID)
        
        Catch ex As Exception
        
            '---- Enter your exception handling code here -----
            theUI.NXMessageBox.Show("Block Styler", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Function
    
End Class
