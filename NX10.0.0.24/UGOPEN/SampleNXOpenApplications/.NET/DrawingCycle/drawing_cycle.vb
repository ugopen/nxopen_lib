' NX 3.0.0.10
' Journal created by geolekas on Fri Mar 05 15:18:51 2004 Eastern Standard Time
Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.Drawings
Imports NXOpen.Annotations
Imports System.Text

Module NXJournal
Sub Main

' ----------------------------------------------
' This example opens up a part, cycles through
' all the sheets in the part. For each sheet, it updates
' all the views on it.  It then places a note in the upper left corner
' that has the current date on it.   And then it popups a message box.   
' the sheet.  (A programmer could add instructions to plot the sheet"
' And then it deletes the note just added to the sheet.  
'
' NOTE: This example is setup to place a note correctly for 
' an E size drawing.  
'
' If you do not want to delete the note that is created,  
' change the constant value of DO_NOT_DELETE_NOTE to be 1.  
' ----------------------------------------------
#Const DO_NOT_DELETE_NOTE = 0


Dim theSession As Session = Session.GetSession()


' ----------------------------------------------
'   Menu: File->Open...
' Fill in part location on the OpenDisplay line.
' ----------------------------------------------
Dim part1 As Part

part1 = theSession.Parts.Work



Dim drawingSheets As DrawingSheet()
Dim mySheet As DrawingSheet
drawingSheets = part1.DrawingSheets.ToArray

Dim dfviews() As DraftingView
Dim dfview As DraftingView

' ----------------------------------------------
' Here we loop through all the sheets in the part.
' For each sheet, we open the sheet, update all views in it,
' And then pop-up a message box listing the 
' views on the sheet.  This could be modified to plot out
' the sheets instead.
' ----------------------------------------------

For Each mySheet In drawingSheets ' Iterate through elements.

    Dim session_UndoMarkId1 As Session.UndoMarkId
    session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Open Drawing")
    mySheet.Open()


    ' ----------------------------------------------
    '   Menu: Edit->View->Update Views...
    ' ----------------------------------------------
    Dim session_UndoMarkId2 As Session.UndoMarkId
    session_UndoMarkId2 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Drawing View Update")
    'There are a couple of  ways to update all the views in the part
    ' we will use the update all views in sheet method, vs. building up
    ' an array of views to be used for update.
    theSession.Parts.Work.DraftingViews.UpdateViews(DraftingViewCollection.ViewUpdateOption.All,mySheet)


    ' ----------------------------------------------
    '   Menu: Insert->Annotation...
    ' ----------------------------------------------
    Dim session_UndoMarkId3 As Session.UndoMarkId
    session_UndoMarkId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

    Dim letteringPreferences1 As LetteringPreferences
    letteringPreferences1 = theSession.Parts.Work.Annotations.Preferences.GetLetteringPreferences()

    Dim userSymbolPreferences1 As UserSymbolPreferences
    userSymbolPreferences1 = theSession.Parts.Work.Annotations.NewUserSymbolPreferences(UserSymbolPreferences.SizeType.ScaleAspectRatio, 1, 1)

    Dim TimeNote As DateTime
    TimeNote = System.DateTime.Now()
    Dim TimeNoteString as String() = TimeNote.GetDateTimeFormats()

    Dim stringArray2(1) As String
    stringArray2(0) = "<c3.3.25> Printed on:"
    stringArray2(1) = TimeNoteString(0) + "<c>"
    Dim point3d1 As Point3d = New Point3d(40.8263111888112, 33.145541958042, 0)

    Dim note1 As Note
    note1 = theSession.Parts.Work.Annotations.CreateNote(stringArray2, point3d1, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

    theSession.SetUndoMarkVisibility(session_UndoMarkId3, "Create Annotation", Session.MarkVisibility.Visible)


    letteringPreferences1.Dispose()

    userSymbolPreferences1.Dispose()

    ' ----------------------------------------------
    '   Print will go here
    ' ----------------------------------------------
    dfviews = mySheet.GetDraftingViews()
    Dim sheet_name As String
    Dim view_names As StringBuilder = new StringBuilder()

    sheet_name = "Printing Sheet: " + mySheet.Name 
    
    view_names.append("Sheet contains the following views: ")

    For Each dfview in dfviews
       view_names.append(dfview.Name +" ")
    Next


    Windows.Forms.MessageBox.Show(view_names.ToString(), sheet_name)
#If DO_NOT_DELETE_NOTE = 0 Then

    ' ----------------------------------------------
    '   Menu: Edit->Delete...
    ' ----------------------------------------------
    theSession.UpdateManager.ClearErrorList()

    Dim session_UndoMarkId5 As Session.UndoMarkId
    session_UndoMarkId5 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Delete")

    Dim integer4 As Integer
    integer4 = theSession.UpdateManager.AddToDeleteList(note1)

    Dim integer5 As Integer
    integer5 = theSession.UpdateManager.DoUpdate(session_UndoMarkId5)
    
#End If
Next


End Sub
End Module










