' ==============================================================================
'
'             Copyright (c) 2013  UGS PLM Solutions
'               Unpublished - All rights reserved
'
' ==============================================================================
' ******************************************************************************
'  Description
'    Class that provides the Winforms UI for the Machine Control Panel example
'
'   
'
' ******************************************************************************
Option Strict Off
Imports System
Imports NXOpen

Public Class Module1

    Public Shared theForm As MCP

    '  Explicit Activation
    '      This entry point is used to activate the application explicitly
    Public Shared Sub Main()

        Dim theSession As Session = Session.GetSession()

        theForm = New MCP()
        theForm.Show()

    End Sub

    Public Shared Function GetUnloadOption(ByVal dummy As String) As Integer

        'Unloads the image when the NX session terminates
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination

        '----Other unload options-------
        'Unloads the image immediately after execution within NX
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Immediately

        'Unloads the image explicitly, via an unload dialog
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Explicitly
        '-------------------------------

    End Function

    Public Shared Function UnloadLibrary(ByVal arg As String) As Integer
        ' Dispose the form explicitly here to make sure this happens in the
        ' main thread and not by the garbage collector in a separate thread
        theForm.Dispose()
        Return 0
    End Function

End Class

