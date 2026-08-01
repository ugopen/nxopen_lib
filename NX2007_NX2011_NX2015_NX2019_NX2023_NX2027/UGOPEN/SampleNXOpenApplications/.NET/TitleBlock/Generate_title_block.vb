' NX 3.0.0.10
' Journal created by geolekas on Tue Mar 09 13:43:02 2004 Eastern Standard Time
Option Strict Off
Imports System
Imports System.IO
Imports NXOpen
Imports NXOpen.Drawings
Imports NXOpen.Annotations

' ----------------------------------------------
'   This automation journal imports a symbol that represents a simple
'  3 line title block.  It then adds in headers for the three lines (Part Name,
'  Author, and Date).  And then it addes in the values for thost lines.
'  While this is a simplistic title block, the goal is to show the process
'  of how to automatically generate a title block.
'  
'
'  The title block's text is associative; it will stay with the title block if 
'  if it is moved around.
' ----------------------------------------------

Module NXJournal
Sub Main

Dim theSession As Session = Session.GetSession()
Dim theUI As UI = UI.GetUI()
 
 
Dim PartNameString(0) As String
Dim AuthorString(0) As String
Dim DateString(0) As String
Dim TimeNote As DateTime
' ----------------------------------------------
'   Have the time field go to the local system time
' ----------------------------------------------
TimeNote = System.DateTime.Now()
DateString = TimeNote.GetDateTimeFormats() 

Dim integer1 As Integer

' ----------------------------------------------
'   Alter these strings here to change values
'   of strings
' ----------------------------------------------

Dim query_data As Form1 = new Form1()

if query_data.ShowDialog() <> query_data.DialogResult.OK then exit sub




PartNameString(0) = query_data.GetPartName()
AuthorString(0) = query_data.GetAuthorName()   

' ----------------------------------------------
'   Menu: Insert->Annotation...
' ----------------------------------------------
Dim session_UndoMarkId1 As Session.UndoMarkId
session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim letteringPreferences1 As LetteringPreferences
letteringPreferences1 = theSession.Parts.Work.Annotations.Preferences.GetLetteringPreferences()

' ----------------------------------------------
'   For this example, we need the set the lettering preferences so the
'   Text will align correctly in the title block
' ----------------------------------------------
Dim Annotations_Lettering1 As Annotations.Lettering
Annotations_Lettering1.size = 0.125
Annotations_Lettering1.CharacterSpaceFactor = 1
Annotations_Lettering1.AspectRatio = 1
Annotations_Lettering1.LineSpaceFactor = 1
Annotations_Lettering1.cfw.color = 2
Annotations_Lettering1.cfw.font = 1
Annotations_Lettering1.cfw.width = Annotations.LineWidth.Thin
letteringPreferences1.SetGeneralText(Annotations_Lettering1)

theSession.Parts.Work.Annotations.Preferences.SetLetteringPreferences(letteringPreferences1)






Dim userSymbolPreferences1 As UserSymbolPreferences
userSymbolPreferences1 = theSession.Parts.Work.Annotations.NewUserSymbolPreferences(UserSymbolPreferences.SizeType.ScaleAspectRatio, 1, 1)

' ----------------------------------------------
'   We need to load in the custom sybmol of the simple title block that has three lines
' ----------------------------------------------
Dim name As String
name = theSession.Parts.Work.FullPath

theSession.Parts.Work.Annotations.CurrentSbfFile = Path.Combine(Path.GetDirectoryName(name), "special.sbf")

Dim double1 As Double
Dim double2 As Double
Dim symbolFont1 As SymbolFont
symbolFont1 = theSession.Parts.Work.Annotations.LoadSymbolFontFromSbfFile("TITLE4  ", double1, double2)

' ----------------------------------------------
'   This creates adds the in the title block 
' ----------------------------------------------
Dim stringArray1(0) As String
stringArray1(0) = "<%TITLE4>"
Dim point3d1 As Point3d = New Point3d(12.9219405594406, 2.3166958041958, 0)
Dim note1 As Note
note1 = theSession.Parts.Work.Annotations.CreateNote(stringArray1, point3d1, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)



theSession.SetUndoMarkVisibility(session_UndoMarkId1, "Create Annotation", Session.MarkVisibility.Visible)


' ----------------------------------------------
'   This adds in the note for the Part Name title entry
'   
'  We set up an association, to the title block note, so 
'  when the title block is moved the text will travel with it
' ----------------------------------------------
stringArray1(0) = "<C3.250>Part Name<C>"
point3d1 = New Point3d(0, 0, 0)
Dim note3 As Note
note3 = theSession.Parts.Work.Annotations.CreateNote(stringArray1, point3d1, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

' ----------------------------------------------
'   Menu: Edit->Placement->Origin Tool
' ----------------------------------------------
theSession.SetUndoMarkVisibility(session_UndoMarkId1, "Create Annotation", Session.MarkVisibility.Visible)

Dim annotation_AssociativeOriginData2 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData2.OriginType = Annotations.AssociativeOriginType.OffsetFromText
annotation_AssociativeOriginData2.View = Nothing
annotation_AssociativeOriginData2.ViewOfGeometry = Nothing
annotation_AssociativeOriginData2.PointOnGeometry = Nothing
annotation_AssociativeOriginData2.VertAnnotation = Nothing
annotation_AssociativeOriginData2.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData2.HorizAnnotation = Nothing
annotation_AssociativeOriginData2.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData2.AlignedAnnotation = Nothing
annotation_AssociativeOriginData2.DimensionLine = 0
annotation_AssociativeOriginData2.AssociatedView = Nothing
annotation_AssociativeOriginData2.AssociatedPoint = Nothing
annotation_AssociativeOriginData2.OffsetAnnotation = note1
annotation_AssociativeOriginData2.OffsetAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData2.XOffsetFactor = -70
annotation_AssociativeOriginData2.YOffsetFactor = 8
Dim point3d6 As Point3d = New Point3d(2.54694055944056, 3.3166958041958, 0)
note3.SetAssociativeOrigin(annotation_AssociativeOriginData2, point3d6)


integer1 = theSession.UpdateManager.DoUpdate(session_UndoMarkId1)

session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

' ----------------------------------------------
'   This adds in the note for the Author title entry
'   
'  We set up an association, to the title block note, so 
'  when the title block is moved the text will travel with it
' ----------------------------------------------

stringArray1(0) = "<C3.250>Author<C>"
point3d1  = New Point3d(0, 0, 0)
Dim note4 As Note
note4 = theSession.Parts.Work.Annotations.CreateNote(stringArray1, point3d1, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

' ----------------------------------------------
'   Menu: Edit->Placement->Origin Tool
' ----------------------------------------------
theSession.SetUndoMarkVisibility(session_UndoMarkId1, "Create Annotation", Session.MarkVisibility.Visible)


Dim annotation_AssociativeOriginData3 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData3.OriginType = Annotations.AssociativeOriginType.OffsetFromText
annotation_AssociativeOriginData3.View = Nothing
annotation_AssociativeOriginData3.ViewOfGeometry = Nothing
annotation_AssociativeOriginData3.PointOnGeometry = Nothing
annotation_AssociativeOriginData3.VertAnnotation = Nothing
annotation_AssociativeOriginData3.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData3.HorizAnnotation = Nothing
annotation_AssociativeOriginData3.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData3.AlignedAnnotation = Nothing
annotation_AssociativeOriginData3.DimensionLine = 0
annotation_AssociativeOriginData3.AssociatedView = Nothing
annotation_AssociativeOriginData3.AssociatedPoint = Nothing
annotation_AssociativeOriginData3.OffsetAnnotation = note1
annotation_AssociativeOriginData3.OffsetAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData3.XOffsetFactor = -70
annotation_AssociativeOriginData3.YOffsetFactor = 1
Dim point3d8 As Point3d = New Point3d(1.92194055944056, 2.4416958041958, 0)
note4.SetAssociativeOrigin(annotation_AssociativeOriginData3, point3d8)


integer1 = theSession.UpdateManager.DoUpdate(session_UndoMarkId1)

session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")


' ----------------------------------------------
'   This adds in the note for the Date title entry
'   
'  We set up an association, to the title block note, so 
'  when the title block is moved the text will travel with it
' ----------------------------------------------
stringArray1(0) = "<C3.250>Revision Date<C>"
point3d1 = New Point3d(0, 0, 0)
Dim note8 As Note
note8 = theSession.Parts.Work.Annotations.CreateNote(stringArray1, point3d1, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

' ----------------------------------------------
'   Menu: Edit->Placement->Origin Tool
' ----------------------------------------------
theSession.SetUndoMarkVisibility(session_UndoMarkId1, "Create Annotation", Session.MarkVisibility.Visible)

Dim annotation_AssociativeOriginData5 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData5.OriginType = Annotations.AssociativeOriginType.OffsetFromText
annotation_AssociativeOriginData5.View = Nothing
annotation_AssociativeOriginData5.ViewOfGeometry = Nothing
annotation_AssociativeOriginData5.PointOnGeometry = Nothing
annotation_AssociativeOriginData5.VertAnnotation = Nothing
annotation_AssociativeOriginData5.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData5.HorizAnnotation = Nothing
annotation_AssociativeOriginData5.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData5.AlignedAnnotation = Nothing
annotation_AssociativeOriginData5.DimensionLine = 0
annotation_AssociativeOriginData5.AssociatedView = Nothing
annotation_AssociativeOriginData5.AssociatedPoint = Nothing
annotation_AssociativeOriginData5.OffsetAnnotation = note1
annotation_AssociativeOriginData5.OffsetAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData5.XOffsetFactor = -70
annotation_AssociativeOriginData5.YOffsetFactor = -7
Dim point3d14 As Point3d = New Point3d(3.42194055944056, 1.4416958041958, 0)
note8.SetAssociativeOrigin(annotation_AssociativeOriginData5, point3d14)


integer1 = theSession.UpdateManager.DoUpdate(session_UndoMarkId1)

session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")



session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")


' ----------------------------------------------
'   This adds in the note for the Part name
'   
'  We set up an association, to the title block note, so 
'  when the title block is moved the text will travel with it
' ----------------------------------------------
stringArray1(0) = "<C3.250>" + PartNameString(0) + "<C>"
point3d1 = New Point3d(0, 0, 0)
Dim note9 As Note
note9 = theSession.Parts.Work.Annotations.CreateNote(stringArray1, point3d1, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

' ----------------------------------------------
'   Menu: Edit->Placement->Origin Tool
' ----------------------------------------------
theSession.SetUndoMarkVisibility(session_UndoMarkId1, "Create Annotation", Session.MarkVisibility.Visible)

Dim annotation_AssociativeOriginData11 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData11.OriginType = Annotations.AssociativeOriginType.OffsetFromText
annotation_AssociativeOriginData11.View = Nothing
annotation_AssociativeOriginData11.ViewOfGeometry = Nothing
annotation_AssociativeOriginData11.PointOnGeometry = Nothing
annotation_AssociativeOriginData11.VertAnnotation = Nothing
annotation_AssociativeOriginData11.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData11.HorizAnnotation = Nothing
annotation_AssociativeOriginData11.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData11.AlignedAnnotation = Nothing
annotation_AssociativeOriginData11.DimensionLine = 0
annotation_AssociativeOriginData11.AssociatedView = Nothing
annotation_AssociativeOriginData11.AssociatedPoint = Nothing
annotation_AssociativeOriginData11.OffsetAnnotation = note1
annotation_AssociativeOriginData11.OffsetAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData11.XOffsetFactor = 40
annotation_AssociativeOriginData11.YOffsetFactor = 8
Dim point3d2 As Point3d = New Point3d(33.1533828382838, 3.8529702970297, 0)
note9.SetAssociativeOrigin(annotation_AssociativeOriginData11, point3d2)


integer1 = theSession.UpdateManager.DoUpdate(session_UndoMarkId1)


session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

' ----------------------------------------------
'   This adds in the note for the Author name
'   
'  We set up an association, to the title block note, so 
'  when the title block is moved the text will travel with it
' ----------------------------------------------
stringArray1(0) = "<C3.250>" + AuthorString(0) + "<C>"
point3d1 = New Point3d(0, 0, 0)
Dim note10 As Note
note10 = theSession.Parts.Work.Annotations.CreateNote(stringArray1, point3d1, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

' ----------------------------------------------
'   Menu: Edit->Placement->Origin Tool
' ----------------------------------------------
theSession.SetUndoMarkVisibility(session_UndoMarkId1, "Create Annotation", Session.MarkVisibility.Visible)


Dim annotation_AssociativeOriginData12 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData12.OriginType = Annotations.AssociativeOriginType.OffsetFromText
annotation_AssociativeOriginData12.View = Nothing
annotation_AssociativeOriginData12.ViewOfGeometry = Nothing
annotation_AssociativeOriginData12.PointOnGeometry = Nothing
annotation_AssociativeOriginData12.VertAnnotation = Nothing
annotation_AssociativeOriginData12.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData12.HorizAnnotation = Nothing
annotation_AssociativeOriginData12.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData12.AlignedAnnotation = Nothing
annotation_AssociativeOriginData12.DimensionLine = 0
annotation_AssociativeOriginData12.AssociatedView = Nothing
annotation_AssociativeOriginData12.AssociatedPoint = Nothing
annotation_AssociativeOriginData12.OffsetAnnotation = note1
annotation_AssociativeOriginData12.OffsetAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData12.XOffsetFactor = 40
annotation_AssociativeOriginData12.YOffsetFactor = 1
Dim point3d4 As Point3d = New Point3d(33.1533828382838, 2.9779702970297, 0)
note10.SetAssociativeOrigin(annotation_AssociativeOriginData12, point3d4)

integer1 = theSession.UpdateManager.DoUpdate(session_UndoMarkId1)

session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

' ----------------------------------------------
'   This adds in the note for the Date name
'   
'  We set up an association, to the title block note, so 
'  when the title block is moved the text will travel with it
' ----------------------------------------------
stringArray1(0) = "<C3.250>" + DateString(0) + "<C>"
point3d1  = New Point3d(0, 0, 0)
Dim note11 As Note
note11 = theSession.Parts.Work.Annotations.CreateNote(stringArray1, point3d1, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

Dim annotation_AssociativeOriginData13 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData13.OriginType = Annotations.AssociativeOriginType.OffsetFromText
annotation_AssociativeOriginData13.View = Nothing
annotation_AssociativeOriginData13.ViewOfGeometry = Nothing
annotation_AssociativeOriginData13.PointOnGeometry = Nothing
annotation_AssociativeOriginData13.VertAnnotation = Nothing
annotation_AssociativeOriginData13.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData13.HorizAnnotation = Nothing
annotation_AssociativeOriginData13.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData13.AlignedAnnotation = Nothing
annotation_AssociativeOriginData13.DimensionLine = 0
annotation_AssociativeOriginData13.AssociatedView = Nothing
annotation_AssociativeOriginData13.AssociatedPoint = Nothing
annotation_AssociativeOriginData13.OffsetAnnotation = note1
annotation_AssociativeOriginData13.OffsetAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData13.XOffsetFactor = 40
annotation_AssociativeOriginData13.YOffsetFactor = -7
point3d1 = New Point3d(33.1533828382838, 1.9779702970297, 0)
note11.SetAssociativeOrigin(annotation_AssociativeOriginData13, point3d1)


integer1 = theSession.UpdateManager.DoUpdate(session_UndoMarkId1)

session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

' ----------------------------------------------
'   Menu: Edit->Placement->Origin Tool
' ----------------------------------------------
theSession.SetUndoMarkVisibility(session_UndoMarkId1, "Create Annotation", Session.MarkVisibility.Visible)

letteringPreferences1.Dispose()

userSymbolPreferences1.Dispose()

' ----------------------------------------------
'   Menu: Tools->Journal->Stop
' ----------------------------------------------


query_data.dispose()


End Sub

' ----------------------------------------------
'   The following code for the form was generated 
'   using Microsoft Visual Studio .Net
' ----------------------------------------------

Public Class Form1
    Inherits System.Windows.Forms.Form

#Region " Windows Form Designer generated code "

    Public Sub New()
        MyBase.New()

        'This call is required by the Windows Form Designer.
        InitializeComponent()

        'Add any initialization after the InitializeComponent() call

    End Sub

    'Form overrides dispose to clean up the component list.
    Protected Overloads Overrides Sub Dispose(ByVal disposing As Boolean)
        If disposing Then
            If Not (components Is Nothing) Then
                components.Dispose()
            End If
        End If
        MyBase.Dispose(disposing)
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents m_partNameTextBox As System.Windows.Forms.TextBox
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Button1 As System.Windows.Forms.Button
    Friend WithEvents m_authorNameTextBox As System.Windows.Forms.TextBox
    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
Me.Label1 = New System.Windows.Forms.Label
Me.m_partNameTextBox = New System.Windows.Forms.TextBox
Me.Label2 = New System.Windows.Forms.Label
Me.m_authorNameTextBox = New System.Windows.Forms.TextBox
Me.Button1 = New System.Windows.Forms.Button
Me.SuspendLayout()
'
'Label1
'
Me.Label1.Location = New System.Drawing.Point(16, 24)
Me.Label1.Name = "Label1"
Me.Label1.TabIndex = 0
Me.Label1.Text = "Part name"
'
'm_partNameTextBox
'
Me.m_partNameTextBox.Location = New System.Drawing.Point(16, 56)
Me.m_partNameTextBox.Name = "m_partNameTextBox"
Me.m_partNameTextBox.Size = New System.Drawing.Size(232, 20)
Me.m_partNameTextBox.TabIndex = 1
Me.m_partNameTextBox.Text = ""
Me.m_partNameTextBox.MaxLength = 30
'
'Label2
'
Me.Label2.Location = New System.Drawing.Point(16, 96)
Me.Label2.Name = "Label2"
Me.Label2.TabIndex = 2
Me.Label2.Text = "Author name"
'
'm_authorNameTextBox
'
Me.m_authorNameTextBox.Location = New System.Drawing.Point(16, 128)
Me.m_authorNameTextBox.Name = "m_authorNameTextBox"
Me.m_authorNameTextBox.Size = New System.Drawing.Size(232, 20)
Me.m_authorNameTextBox.TabIndex = 3
Me.m_authorNameTextBox.Text = ""
Me.m_authorNameTextBox.MaxLength = 30
'
'Button1
'
Me.Button1.Location = New System.Drawing.Point(112, 168)
Me.Button1.Name = "Button1"
Me.Button1.TabIndex = 4
Me.Button1.Text = "Ok"
Me.Button1.DialogResult = DialogResult.OK
'
'Form1
'
Me.AutoScaleBaseSize = New System.Drawing.Size(5, 13)
Me.ClientSize = New System.Drawing.Size(292, 205)
Me.Controls.Add(Me.Button1)
Me.Controls.Add(Me.m_authorNameTextBox)
Me.Controls.Add(Me.Label2)
Me.Controls.Add(Me.m_partNameTextBox)
Me.Controls.Add(Me.Label1)
Me.Name = "GenerateTitleBlock"
Me.Text = "GenerateTitleBlock"
Me.ResumeLayout(False)

    End Sub

#End Region

Public Function GetPartName() As String
    Return Me.m_partNameTextBox.Text()
End Function

Public Function GetAuthorName() As String
    Return Me.m_authorNameTextBox.Text()
End Function

End Class

End Module







