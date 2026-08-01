' ===================================================================
'
'             Copyright (c) 2004  UGS PLM Solutions
'               Unpublished - All rights reserved
'
' ===================================================================
' *******************************************************************
'
'  Description
'    Sets up access to the Microsoft Word application and uses
'    the spell checking functionality.
'
'  
' *******************************************************************
Imports System
Imports System.Runtime.InteropServices
'----------------------------------------

Imports Microsoft.Office.Interop.Word
Imports Microsoft.Office.Interop


<ComImport(), Guid("00000016-0000-0000-C000-000000000046"), _
InterfaceTypeAttribute(ComInterfaceType.InterfaceIsIUnknown)> _
Friend Interface IOleMessageFilter
    <PreserveSig()> _
    Function HandleInComingCall(ByVal dwCallType As Integer, ByVal hTaskCaller As IntPtr, _
                                ByVal dwTickCount As Integer, ByVal lpInterfaceInfo As IntPtr) As Integer

    <PreserveSig()> _
    Function RetryRejectedCall(ByVal hTaskCallee As IntPtr, ByVal dwTickCount As Integer, _
                               ByVal dwRejectType As Integer) As Integer

    <PreserveSig()> _
    Function MessagePending(ByVal hTaskCallee As IntPtr, ByVal dwTickCount As Integer, _
                            ByVal dwPendingType As Integer) As Integer
End Interface

Public Class WordSpellChecker

    <DllImport("ole32.dll", CallingConvention:=CallingConvention.StdCall)> _
    Private Shared Function CoRegisterMessageFilter(ByVal newFilter As IOleMessageFilter, ByRef oldFilter As IOleMessageFilter) As Integer

    End Function

    ' Description: Performs spell checking on an input string
    '              Returns the string validated by the Word
    '              spell checker.
    Public Function CheckString(ByRef str As String) As String

        Dim app As Application = New Word.Application
        Dim doc As Document = app.Documents.Add
        app.Selection.Text = str

        Try

            Dim dlg As Word.Dialog
            dlg = app.Dialogs.Item(Word.WdWordDialog.wdDialogToolsSpellingAndGrammar)

            Dim oldFilter As IOleMessageFilter = Nothing
            Dim nullFilter As IOleMessageFilter = Nothing
            CoRegisterMessageFilter(nullFilter, oldFilter)
            Try
                dlg.Show()
            Finally
                CoRegisterMessageFilter(oldFilter, oldFilter)
            End Try

            app.Visible = False

            Dim docRange As Range = doc.Content

            str = docRange.Text

            str = str.TrimEnd(Environment.NewLine)

        Catch e As Exception

            System.Diagnostics.Trace.WriteLine("Spell checking...")
            System.Diagnostics.Trace.WriteLine(e.ToString)

        Finally

            doc.Close(WdSaveOptions.wdDoNotSaveChanges)
            app.Quit()

        End Try

        Return str

    End Function

End Class
