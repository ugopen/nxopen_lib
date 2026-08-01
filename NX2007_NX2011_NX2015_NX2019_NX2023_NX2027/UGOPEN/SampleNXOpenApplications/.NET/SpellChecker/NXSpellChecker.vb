' ===================================================================
'
'             Copyright (c) 2004  UGS PLM Solutions
'               Unpublished - All rights reserved
'
' ===================================================================
' *******************************************************************
'
'  Description
'    Handles access to NX and delegates spell checking to the
'    WordSpellChecker class.  This class also defines the main
'    routine for the application and defines a routine that
'    NX looks for on how to handle the application after
'    execution.  In this example the application is setup to
'    unload immediately after execution within NX. 
'
'  
' *******************************************************************
Imports System
Imports NXOpen
Imports NXOpenUI
Imports NXOpen.UF


Public Class NXSpellChecker

    ' Description: Allows the selection of notes and labels
    '              and outputs them in an array of NXObjects.
    '              Objects are scoped to the work part. 
    Private Sub SelectNotesAndLabels(ByRef selectedObjects As TaggedObject())

        'Gateway to the NX User Interface
        Dim ui As UI = ui.GetUI

        Dim message As String = "Select notes and labels to spell check"
        Dim title As String = "Select notes and labels"

        Dim scope As Selection.SelectionScope = Selection.SelectionScope.WorkPart
        Dim keepHighlighted As Boolean = True
        Dim includeFeatures As Boolean = True
        Dim response As Selection.Response

        'Set selection filter to pick only notes and labels.
        Dim selectionAction As Selection.SelectionAction = _
         Selection.SelectionAction.ClearAndEnableSpecific
        Dim selectionMask_array(2) As Selection.MaskTriple
        With selectionMask_array(0)
            .Type = UFConstants.UF_drafting_entity_type
            .Subtype = UFConstants.UF_draft_note_subtype
            .SolidBodySubtype = 0
        End With
        With selectionMask_array(1)
            .Type = UFConstants.UF_drafting_entity_type
            .Subtype = UFConstants.UF_draft_label_subtype
            .SolidBodySubtype = 0
        End With

        Try

            response = ui.SelectionManager.SelectTaggedObjects(message, title, scope, _
               selectionAction, includeFeatures, _
               keepHighlighted, selectionMask_array, _
               selectedObjects)
            If response = Selection.Response.Cancel Or response = Selection.Response.Back Then
                Return
            End If

            Dim info As String = "Number of selected objects = "
            info = String.Concat(info, selectedObjects.Length)
            System.Diagnostics.Trace.WriteLine(info)

        Catch e As Exception

            System.Diagnostics.Trace.WriteLine("Problems selecting objects.")
            System.Diagnostics.Trace.WriteLine(e.ToString)

        End Try

    End Sub

    ' Description: Select notes and labels
    '              and perform the spelling check.
    Public Sub SpellCheck()

        'Gateway to the NX applications
        Dim session As Session = session.GetSession
        Dim ufsession As UFSession = ufsession.GetUFSession()

        'Select notes and labels in NX
        Dim selectedObjects() As TaggedObject = Nothing
        Me.SelectNotesAndLabels(selectedObjects)

        Try
            ufsession.Ui.SetPrompt("Make corrections in the Word window")
            ufsession.Ui.SetStatus("Use <Alt><Tab> to bring the Word window to the front")

            Dim sda As Annotations.SimpleDraftingAid
            For Each sda In selectedObjects

                Dim wd As WordSpellChecker = New WordSpellChecker
                Dim nxText() As String
                Dim line As String
                Dim undoText As String = "Update Note"
                Dim undoMark As Session.UndoMarkId
                Dim i As Integer = 0

                'Get the text from the note or label in NX
                nxText = sda.GetText

                For Each line In nxText

                    line = wd.CheckString(line)
                    nxText(i) = line
                    i += 1

                Next

                'Set the text for the note or label in NX
                sda.SetText(nxText)

                'Update so the text changes are applied to the system
                undoMark = session.SetUndoMark(session.MarkVisibility.Visible, undoText)
                session.UpdateManager.DoUpdate(undoMark)

            Next

        Catch e As Exception

            System.Diagnostics.Trace.WriteLine("Problem with traversing selected objects array")
            System.Diagnostics.Trace.WriteLine(e.ToString)

        Finally

            'Unhighlight the object in NX
            Dim dispObj As DisplayableObject
            For Each dispObj In selectedObjects

                dispObj.Unhighlight()

            Next

        End Try

    End Sub

    Public Shared Sub Main()

        Dim sp As NXSpellChecker
        sp = New NXSpellChecker
        sp.SpellCheck()

    End Sub

    'Unloads the image immediately after execution within NX
    Public Shared Function GetUnloadOption(ByVal dummy As String) As Integer

        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Immediately

    End Function

End Class
