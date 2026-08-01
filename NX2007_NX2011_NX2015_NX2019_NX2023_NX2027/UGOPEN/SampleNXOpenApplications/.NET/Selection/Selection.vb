' ===================================================================
'
'                   Copyright (c) 2004 UGS
'               Unpublished - All rights reserved
'
'  
' ===================================================================
'*******************************************************************************
'DESCRIPTION
'This example demonstrates alternatives to the code recorded while performing a
''Select All' using various filtering methods before an operation.  The example
'shows how filtering by type, detailed type, layers, display attributes and color
'can be accomplished via automation. The example gets the datums on the work part
'that satisfy the filtering criteria and blanks the datums.  The code assumes that
'the example part file, datums.prt or a part with datums is already opened.
'*******************************************************************************
Option Strict Off
Imports System
Imports NXOpen
Imports System.Windows.Forms

Module Selection

    Sub Main()

        Dim marksRecycled As Boolean
        Dim undoUnavailable As Boolean
        Dim undoMark As Session.UndoMarkId
        Dim length As Int32

        Dim theSession As Session = Session.GetSession()

        ' FILTERING BY TYPE:
        ' Use in place of the journal code for "Select All" with filter
        ' type set to "Datums".
        undoMark = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Blank")
        Dim ddo() As DisplayableObject = theSession.Parts.Work.Datums.ToArray()

        theSession.DisplayManager.BlankObjects(ddo)

        theSession.DisplayManager.MakeUpToDate()
        MessageBox.Show(ddo.Length.ToString() + " datums were blanked.")

        theSession.UndoLastNVisibleMarks(1, marksRecycled, undoUnavailable)


        ' FILTERING BY DETAILED TYPE:
        ' Use in place of the journal code for "Select All" with detailed filter type
        ' set to "Datums - Datum Planes".
        undoMark = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Blank")

        length = 0
        For Each obj As DisplayableObject In theSession.Parts.Work.Datums
            If TypeOf obj Is DatumPlane Then
                obj.Blank()
                length = length + 1
            End If
        Next

        theSession.DisplayManager.MakeUpToDate()
        MessageBox.Show(length.ToString() + " datum planes were blanked.")

        theSession.UndoLastNVisibleMarks(1, marksRecycled, undoUnavailable)


        ' FILTERING BY LAYER:
        ' Use in place of the journal code for "Select All" with filter type
        ' set to "Layers - 10".
        undoMark = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Blank")

        length = 0
        For Each obj As DisplayableObject In theSession.Parts.Work.Datums
            If obj.Layer = 10 Then
                obj.Blank()
                length = length + 1
            End If
        Next

        theSession.DisplayManager.MakeUpToDate()
        MessageBox.Show(length.ToString() + " datums on layer 10 were blanked.")

        theSession.UndoLastNVisibleMarks(1, marksRecycled, undoUnavailable)


        ' FILTERING BY DISPLAY ATTRIBUTES:
        ' Use in place of the journal code for "Select All" with filter type
        ' set to "Display Attributes - Dashed, Thick Width".
        undoMark = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Blank")

        length = 0
        For Each obj As DisplayableObject In theSession.Parts.Work.Datums
            If obj.LineFont = DisplayableObject.ObjectFont.Dashed _
            And obj.LineWidth = DisplayableObject.ObjectWidth.Thick Then
                obj.Blank()
                length = length + 1
            End If
        Next

        theSession.DisplayManager.MakeUpToDate()
        MessageBox.Show(length.ToString() + " datums with dashed line font and thick width were blanked.")

        theSession.UndoLastNVisibleMarks(1, marksRecycled, undoUnavailable)

        ' FILTERING BY COLOR:
        ' Use in place of the journal code for "Select All" with filter type
        ' set to "Color - 134".
        undoMark = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Blank")

        length = 0
        For Each obj As DisplayableObject In theSession.Parts.Work.Datums
            If obj.Color = 134 Then
                obj.Blank()
                length = length + 1
            End If
        Next

        theSession.DisplayManager.MakeUpToDate()
        MessageBox.Show(length.ToString() + " datums with color 134 were blanked.")

        theSession.UndoLastNVisibleMarks(1, marksRecycled, undoUnavailable)
    End Sub

End Module
