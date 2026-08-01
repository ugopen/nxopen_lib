'=============================================================================
'                  Copyright (c) 2009 Siemens
'                      All rights reserved
'===============================================================================
'
'Description: VB application 
'
' 
'=============================================================================*/
 Imports System
 Imports System.IO
 Imports System.Windows.Forms
 Imports NXOpen
 Imports NXOpen.UF
 Imports InteropCallCFromDotNet.wrappers

' Standard Entry Points called from NX

Module VBapp
    Public theNXsession As Session
    Public theUFsession As UFSession

    Public Sub Main()
        Try
            Dim value As Integer = 88
            Dim ret1 As Integer = 0
            Dim ret2 As Integer = 0

            theNXsession = Session.GetSession
            theUFsession = UFSession.GetUFSession

            theNXsession.LogFile.WriteLine("BEGIN VBapp (Running from File->Execute)")

            ' Call Functions in UFLegacyApp 
            ret1 = UFappFunction1()
            ret2 = UFappFunction2(88, "This string is from VBapp")

            theNXsession.LogFile.WriteLine("funtions1:" & ret1.ToString & " " & _
                            "function2:" & ret2.ToString)

            theNXsession.LogFile.WriteLine("END VBapp")
        Catch ex As Exception
            UI.GetUI.NXMessageBox.Show("NXOpen automation example", NXMessageBox.DialogType.Error, ex.ToString)
        End Try
    End Sub

    Public Function GetUnloadOption(ByVal arg As String) As Integer
        Return Session.LibraryUnloadOption.Immediately
    End Function

    Public Function UnloadLibrary(ByVal arg As String) As Integer
        Session.GetSession().LogFile.WriteLine("VBapp: UnloadLibrary")
        Return 0
    End Function
End Module

