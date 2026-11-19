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

Module Module1

    '  Explicit Activation
    '      This entry point is used to activate the application explicitly
    Sub Main()

        Dim theSession As Session = Session.GetSession()

        ' TODO: Add your application code here 
        Dim form As New MCP()
        form.Show()

    End Sub


    Public Function GetUnloadOption(ByVal dummy As String) As Integer

        'Unloads the image when the NX session terminates
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination

        '----Other unload options-------
        'Unloads the image immediately after execution within NX
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Immediately

        'Unloads the image explicitly, via an unload dialog
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Explicitly
        '-------------------------------

    End Function

End Module

