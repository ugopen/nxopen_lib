'===============================================================================
'
'     Copyright 2010 Siemens Product Lifecycle Management Software Inc.
'                            All Rights Reserved.   
'
'  
'=================================================================================

Option Strict Off
Imports System
Imports NXOpen
Imports NXOpen.Drawings
Imports NXOpen.Annotations

' ----------------------------------------------
' This automation journal fills in a title block
' from the standard template for a C drawing.  The Following fields
' are querried from a form and filled in.
' Company Name
' Part Name
' Drawing Number
' Scale
' sheet # of sheets total (ex. 1 of 2)
' Contract Number
' Name and sign off date for the following fields
' Design, Lead, STR, ME
' ----------------------------------------------

Module NXJournal
Sub Main

Dim theSession As Session = Session.GetSession()
Dim theUI As UI = UI.GetUI()

' ----------------------------------------------
' Start up form to get data.  This form was 
' created using Microsoft Visual Studion .Net
' ----------------------------------------------
Dim query_data As Form1 = new Form1()
query_data.ShowDialog()


' ----------------------------------------------
'   Menu: Insert->Annotation...
' ----------------------------------------------
Dim session_UndoMarkId1 As Session.UndoMarkId
session_UndoMarkId1 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim letteringPreferences1 As LetteringPreferences
letteringPreferences1 = theSession.Parts.Work.Annotations.Preferences.GetLetteringPreferences()

Dim Annotations_Lettering1 As Annotations.Lettering
Annotations_Lettering1.size = 0.075
Annotations_Lettering1.CharacterSpaceFactor = 1
Annotations_Lettering1.AspectRatio = 1
Annotations_Lettering1.LineSpaceFactor = 1
Annotations_Lettering1.cfw.color = 2
Annotations_Lettering1.cfw.font = 1
Annotations_Lettering1.cfw.width = Annotations.LineWidth.Thin
letteringPreferences1.SetGeneralText(Annotations_Lettering1)

Dim userSymbolPreferences1 As UserSymbolPreferences
userSymbolPreferences1 = theSession.Parts.Work.Annotations.NewUserSymbolPreferences(UserSymbolPreferences.SizeType.ScaleAspectRatio, 1, 1)

Dim stringArray1(0) As String
stringArray1(0) = "<C1.750>" + query_data.m_CompanyName.Text() +"<C>"
Dim point3d1 As Point3d = New Point3d(3.5527136788005e-015, 0, 0)
Dim note1 As Note
note1 = theSession.Parts.Work.Annotations.CreateNote(stringArray1, point3d1, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId1, "Create Annotation", Session.MarkVisibility.Visible)

Dim annotation_AssociativeOriginData1 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData1.OriginType = Annotations.AssociativeOriginType.VerticallyAligned
annotation_AssociativeOriginData1.View = Nothing
annotation_AssociativeOriginData1.ViewofGeometry = Nothing
annotation_AssociativeOriginData1.pointongeometry = Nothing
annotation_AssociativeOriginData1.VertAnnotation = theSession.Parts.Work.FindObject("HANDLE R-1268")
annotation_AssociativeOriginData1.VertAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData1.HorizAnnotation = Nothing
annotation_AssociativeOriginData1.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData1.AlignedAnnotation = Nothing
annotation_AssociativeOriginData1.DimensionLine = 0
annotation_AssociativeOriginData1.AssociatedView = Nothing
annotation_AssociativeOriginData1.AssociatedPoint = Nothing
annotation_AssociativeOriginData1.OffsetAnnotation = Nothing
annotation_AssociativeOriginData1.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData1.XOffsetFactor = 0
annotation_AssociativeOriginData1.YOffsetFactor = 0
Dim point3d2 As Point3d = New Point3d(19.3770231112587, 2.42952204604062, 0)
note1.SetAssociativeOrigin(annotation_AssociativeOriginData1, point3d2)

Dim integer1 As Integer
integer1 = theSession.UpdateManager.DoUpdate(session_UndoMarkId1)

Dim session_UndoMarkId2 As Session.UndoMarkId
session_UndoMarkId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim stringArray3(0) As String
stringArray3(0) = "<C1.750>" + query_data.m_DrawingName.Text() +"<C>"
Dim point3d3 As Point3d = New Point3d(0, 0, 0)
Dim note2 As Note
note2 = theSession.Parts.Work.Annotations.CreateNote(stringArray3, point3d3, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId2, "Create Annotation", Session.MarkVisibility.Visible)


Dim annotation_AssociativeOriginData2 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData2.OriginType = Annotations.AssociativeOriginType.VerticallyAligned
annotation_AssociativeOriginData2.View = Nothing
annotation_AssociativeOriginData2.ViewofGeometry = Nothing
annotation_AssociativeOriginData2.pointongeometry = Nothing
annotation_AssociativeOriginData2.VertAnnotation = theSession.Parts.Work.FindObject("HANDLE R-1268")
annotation_AssociativeOriginData2.VertAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData2.HorizAnnotation = Nothing
annotation_AssociativeOriginData2.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData2.AlignedAnnotation = Nothing
annotation_AssociativeOriginData2.DimensionLine = 0
annotation_AssociativeOriginData2.AssociatedView = Nothing
annotation_AssociativeOriginData2.AssociatedPoint = Nothing
annotation_AssociativeOriginData2.OffsetAnnotation = Nothing
annotation_AssociativeOriginData2.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData2.XOffsetFactor = 0
annotation_AssociativeOriginData2.YOffsetFactor = 0
Dim point3d4 As Point3d = New Point3d(19.3770231112587, 1.78508590544269, 0)
note2.SetAssociativeOrigin(annotation_AssociativeOriginData2, point3d4)

Dim integer2 As Integer
integer2 = theSession.UpdateManager.DoUpdate(session_UndoMarkId2)

Dim session_UndoMarkId3 As Session.UndoMarkId
session_UndoMarkId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim stringArray5(0) As String
stringArray5(0) = query_data.m_DrawingNumber.Text()
Dim point3d5 As Point3d = New Point3d(0, 0, 0)
Dim note3 As Note
note3 = theSession.Parts.Work.Annotations.CreateNote(stringArray5, point3d5, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId3, "Create Annotation", Session.MarkVisibility.Visible)



Dim annotation_AssociativeOriginData3 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData3.OriginType = Annotations.AssociativeOriginType.VerticallyAligned
annotation_AssociativeOriginData3.View = Nothing
annotation_AssociativeOriginData3.ViewofGeometry = Nothing
annotation_AssociativeOriginData3.pointongeometry = Nothing
annotation_AssociativeOriginData3.VertAnnotation = theSession.Parts.Work.FindObject("HANDLE R-97")
annotation_AssociativeOriginData3.VertAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData3.HorizAnnotation = Nothing
annotation_AssociativeOriginData3.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData3.AlignedAnnotation = Nothing
annotation_AssociativeOriginData3.DimensionLine = 0
annotation_AssociativeOriginData3.AssociatedView = Nothing
annotation_AssociativeOriginData3.AssociatedPoint = Nothing
annotation_AssociativeOriginData3.OffsetAnnotation = Nothing
annotation_AssociativeOriginData3.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData3.XOffsetFactor = 0
annotation_AssociativeOriginData3.YOffsetFactor = 0
Dim point3d6 As Point3d = New Point3d(19.9682496681978, 1.20301455264456, 0)
note3.SetAssociativeOrigin(annotation_AssociativeOriginData3, point3d6)

Dim integer3 As Integer
integer3 = theSession.UpdateManager.DoUpdate(session_UndoMarkId3)

Dim session_UndoMarkId4 As Session.UndoMarkId
session_UndoMarkId4 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim stringArray7(0) As String
stringArray7(0) = query_data.m_sheet_no.Text() +" of " + query_data.m_sheet_no_of.Text()
Dim point3d7 As Point3d = New Point3d(3.5527136788005e-015, 0, 0)
Dim note4 As Note
note4 = theSession.Parts.Work.Annotations.CreateNote(stringArray7, point3d7, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId4, "Create Annotation", Session.MarkVisibility.Visible)



Dim point3d8 As Point3d = New Point3d(20.7831713732126, 0.870402351045622, 0)
note4.AnnotationOrigin = point3d8

Dim integer4 As Integer
integer4 = theSession.UpdateManager.DoUpdate(session_UndoMarkId4)

Dim session_UndoMarkId5 As Session.UndoMarkId
session_UndoMarkId5 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim stringArray9(0) As String
stringArray9(0) = query_data.m_Scale.Text()
Dim point3d9 As Point3d = New Point3d(3.5527136788005e-015, 0, 0)
Dim note5 As Note
note5 = theSession.Parts.Work.Annotations.CreateNote(stringArray9, point3d9, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId5, "Create Annotation", Session.MarkVisibility.Visible)


Dim annotation_AssociativeOriginData4 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData4.OriginType = Annotations.AssociativeOriginType.HorizontallyAligned
annotation_AssociativeOriginData4.View = Nothing
annotation_AssociativeOriginData4.ViewofGeometry = Nothing
annotation_AssociativeOriginData4.pointongeometry = Nothing
annotation_AssociativeOriginData4.VertAnnotation = Nothing
annotation_AssociativeOriginData4.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData4.HorizAnnotation = note4
annotation_AssociativeOriginData4.HorizAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData4.AlignedAnnotation = Nothing
annotation_AssociativeOriginData4.DimensionLine = 0
annotation_AssociativeOriginData4.AssociatedView = Nothing
annotation_AssociativeOriginData4.AssociatedPoint = Nothing
annotation_AssociativeOriginData4.OffsetAnnotation = Nothing
annotation_AssociativeOriginData4.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData4.XOffsetFactor = 0
annotation_AssociativeOriginData4.YOffsetFactor = 0
Dim point3d10 As Point3d = New Point3d(17.9351793970217, 0.870402351045622, 0)
note5.SetAssociativeOrigin(annotation_AssociativeOriginData4, point3d10)

Dim integer5 As Integer
integer5 = theSession.UpdateManager.DoUpdate(session_UndoMarkId5)

Dim session_UndoMarkId6 As Session.UndoMarkId
session_UndoMarkId6 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim stringArray11(1) As String
stringArray11(0) = "Contract No."
stringArray11(1) = query_data.m_ContractNumber.Text()
Dim point3d11 As Point3d = New Point3d(3.5527136788005e-015, 0, 0)
Dim note6 As Note
note6 = theSession.Parts.Work.Annotations.CreateNote(stringArray11, point3d11, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId6, "Create Annotation", Session.MarkVisibility.Visible)

Dim point3d12 As Point3d = New Point3d(16.3033007829268, 2.57503988424, 0)
note6.AnnotationOrigin = point3d12

Dim integer6 As Integer
integer6 = theSession.UpdateManager.DoUpdate(session_UndoMarkId6)

Dim session_UndoMarkId7 As Session.UndoMarkId
session_UndoMarkId7 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")



' ----------------------------------------------
'   Menu: Insert->Annotation...
' ----------------------------------------------
Dim session_UndoMarkId8 As Session.UndoMarkId
session_UndoMarkId8 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

' ----------------------------------------------
'   Menu: View->Current Dialog
' ----------------------------------------------
theSession.SetUndoMarkVisibility(session_UndoMarkId8, "Create Annotation", Session.MarkVisibility.Visible)

Dim stringArray15(0) As String
stringArray15(0) = "<C0.75>ME : " + query_data.m_Me.Text() + "<C>"
Dim point3d15 As Point3d = New Point3d(15.8690005415459, 1.1187076082971, 0)
Dim note8 As Note
note8 = theSession.Parts.Work.Annotations.CreateNote(stringArray15, point3d15, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)


Dim integer9 As Integer
integer9 = theSession.UpdateManager.DoUpdate(session_UndoMarkId8)

Dim session_UndoMarkId9 As Session.UndoMarkId
session_UndoMarkId9 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim stringArray16(0) As String
stringArray16(0) = "<C0.75>STR: " + query_data.m_Str.Text() + "<C>"
Dim point3d16 As Point3d = New Point3d(0, 0, 0)
Dim note9 As Note
note9 = theSession.Parts.Work.Annotations.CreateNote(stringArray16, point3d16, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId9, "Create Annotation", Session.MarkVisibility.Visible)

Dim annotation_AssociativeOriginData5 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData5.OriginType = Annotations.AssociativeOriginType.VerticallyAligned
annotation_AssociativeOriginData5.View = Nothing
annotation_AssociativeOriginData5.ViewofGeometry = Nothing
annotation_AssociativeOriginData5.pointongeometry = Nothing
annotation_AssociativeOriginData5.VertAnnotation = note8
annotation_AssociativeOriginData5.VertAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData5.HorizAnnotation = Nothing
annotation_AssociativeOriginData5.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData5.AlignedAnnotation = Nothing
annotation_AssociativeOriginData5.DimensionLine = 0
annotation_AssociativeOriginData5.AssociatedView = Nothing
annotation_AssociativeOriginData5.AssociatedPoint = Nothing
annotation_AssociativeOriginData5.OffsetAnnotation = Nothing
annotation_AssociativeOriginData5.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData5.XOffsetFactor = 0
annotation_AssociativeOriginData5.YOffsetFactor = 0
Dim point3d17 As Point3d = New Point3d(15.8690005415459, 1.38024175993132, 0)
note9.SetAssociativeOrigin(annotation_AssociativeOriginData5, point3d17)

Dim integer10 As Integer
integer10 = theSession.UpdateManager.DoUpdate(session_UndoMarkId9)

Dim session_UndoMarkId10 As Session.UndoMarkId
session_UndoMarkId10 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim stringArray18(0) As String
stringArray18(0) = "<C0.75>Lead: " + query_data.m_Lead.Text() + "<C>"
Dim point3d18 As Point3d = New Point3d(0, 0, 0)
Dim note10 As Note
note10 = theSession.Parts.Work.Annotations.CreateNote(stringArray18, point3d18, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId10, "Create Annotation", Session.MarkVisibility.Visible)

Dim annotation_AssociativeOriginData6 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData6.OriginType = Annotations.AssociativeOriginType.VerticallyAligned
annotation_AssociativeOriginData6.View = Nothing
annotation_AssociativeOriginData6.ViewofGeometry = Nothing
annotation_AssociativeOriginData6.pointongeometry = Nothing
annotation_AssociativeOriginData6.VertAnnotation = note9
annotation_AssociativeOriginData6.VertAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData6.HorizAnnotation = Nothing
annotation_AssociativeOriginData6.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData6.AlignedAnnotation = Nothing
annotation_AssociativeOriginData6.DimensionLine = 0
annotation_AssociativeOriginData6.AssociatedView = Nothing
annotation_AssociativeOriginData6.AssociatedPoint = Nothing
annotation_AssociativeOriginData6.OffsetAnnotation = Nothing
annotation_AssociativeOriginData6.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData6.XOffsetFactor = 0
annotation_AssociativeOriginData6.YOffsetFactor = 0
Dim point3d19 As Point3d = New Point3d(15.8690005415459, 1.63351693835603, 0)
note10.SetAssociativeOrigin(annotation_AssociativeOriginData6, point3d19)

Dim integer11 As Integer
integer11 = theSession.UpdateManager.DoUpdate(session_UndoMarkId10)

Dim session_UndoMarkId11 As Session.UndoMarkId
session_UndoMarkId11 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

Dim stringArray20(0) As String
stringArray20(0) = "<C0.75>Design: " + query_data.m_Design.Text() + "<C>"
Dim point3d20 As Point3d = New Point3d(0, 0, 0)
Dim note11 As Note
note11 = theSession.Parts.Work.Annotations.CreateNote(stringArray20, point3d20, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId11, "Create Annotation", Session.MarkVisibility.Visible)

Dim annotation_AssociativeOriginData7 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData7.OriginType = Annotations.AssociativeOriginType.VerticallyAligned
annotation_AssociativeOriginData7.View = Nothing
annotation_AssociativeOriginData7.ViewofGeometry = Nothing
annotation_AssociativeOriginData7.pointongeometry = Nothing
annotation_AssociativeOriginData7.VertAnnotation = note10
annotation_AssociativeOriginData7.VertAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData7.HorizAnnotation = Nothing
annotation_AssociativeOriginData7.HorizAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData7.AlignedAnnotation = Nothing
annotation_AssociativeOriginData7.DimensionLine = 0
annotation_AssociativeOriginData7.AssociatedView = Nothing
annotation_AssociativeOriginData7.AssociatedPoint = Nothing
annotation_AssociativeOriginData7.OffsetAnnotation = Nothing
annotation_AssociativeOriginData7.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData7.XOffsetFactor = 0
annotation_AssociativeOriginData7.YOffsetFactor = 0
Dim point3d21 As Point3d = New Point3d(15.8690005415459, 1.88403912571091, 0)
note11.SetAssociativeOrigin(annotation_AssociativeOriginData7, point3d21)

Dim integer12 As Integer
integer12 = theSession.UpdateManager.DoUpdate(session_UndoMarkId11)

Dim session_UndoMarkId12 As Session.UndoMarkId
session_UndoMarkId12 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")


Dim stringArray4(0) As String
stringArray4(0) = "<C0.750>" + query_data.m_DesignDate.Text() + "<C>"
point3d4 = New Point3d(0, 0, 0)
Dim note12 As Note
note12 = theSession.Parts.Work.Annotations.CreateNote(stringArray4, point3d4, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId12, "Create Annotation", Session.MarkVisibility.Visible)

Dim annotation_AssociativeOriginData8 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData8.OriginType = Annotations.AssociativeOriginType.HorizontallyAligned
annotation_AssociativeOriginData8.View = Nothing
annotation_AssociativeOriginData8.ViewofGeometry = Nothing
annotation_AssociativeOriginData8.pointongeometry = Nothing
annotation_AssociativeOriginData8.VertAnnotation = Nothing
annotation_AssociativeOriginData8.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData8.HorizAnnotation = note11
annotation_AssociativeOriginData8.HorizAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData8.AlignedAnnotation = Nothing
annotation_AssociativeOriginData8.DimensionLine = 0
annotation_AssociativeOriginData8.AssociatedView = Nothing
annotation_AssociativeOriginData8.AssociatedPoint = Nothing
annotation_AssociativeOriginData8.OffsetAnnotation = Nothing
annotation_AssociativeOriginData8.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData8.XOffsetFactor = 0
annotation_AssociativeOriginData8.YOffsetFactor = 0
point3d5  = New Point3d(16.8574927841817, 1.88403912571091, 0)
note12.SetAssociativeOrigin(annotation_AssociativeOriginData8, point3d5)


integer2 = theSession.UpdateManager.DoUpdate(session_UndoMarkId3)

session_UndoMarkId4 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

stringArray5(0) = "<C0.750>" + query_data.m_LeadDate.Text() + "<C>"
 point3d6  = New Point3d(0, 0, 0)
Dim note13 As Note
note13 = theSession.Parts.Work.Annotations.CreateNote(stringArray5, point3d6, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId4, "Create Annotation", Session.MarkVisibility.Visible)


Dim annotation_AssociativeOriginData9 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData9.OriginType = Annotations.AssociativeOriginType.HorizontallyAligned
annotation_AssociativeOriginData9.View = Nothing
annotation_AssociativeOriginData9.ViewofGeometry = Nothing
annotation_AssociativeOriginData9.pointongeometry = Nothing
annotation_AssociativeOriginData9.VertAnnotation = Nothing
annotation_AssociativeOriginData9.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData9.HorizAnnotation = note10
annotation_AssociativeOriginData9.HorizAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData9.AlignedAnnotation = Nothing
annotation_AssociativeOriginData9.DimensionLine = 0
annotation_AssociativeOriginData9.AssociatedView = Nothing
annotation_AssociativeOriginData9.AssociatedPoint = Nothing
annotation_AssociativeOriginData9.OffsetAnnotation = Nothing
annotation_AssociativeOriginData9.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData9.XOffsetFactor = 0
annotation_AssociativeOriginData9.YOffsetFactor = 0
point3d7 = New Point3d(16.8574927841817, 1.63351693835603, 0)
note13.SetAssociativeOrigin(annotation_AssociativeOriginData9, point3d7)


integer3 = theSession.UpdateManager.DoUpdate(session_UndoMarkId4)


session_UndoMarkId5 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")

stringArray7(0) = "<C0.750>" + query_data.m_StrDate.Text() + "<C>"
point3d8 = New Point3d(0, 0, 0)
Dim note14 As Note
note14 = theSession.Parts.Work.Annotations.CreateNote(stringArray7, point3d8, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId5, "Create Annotation", Session.MarkVisibility.Visible)


Dim annotation_AssociativeOriginData10 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData10.OriginType = Annotations.AssociativeOriginType.HorizontallyAligned
annotation_AssociativeOriginData10.View = Nothing
annotation_AssociativeOriginData10.ViewofGeometry = Nothing
annotation_AssociativeOriginData10.pointongeometry = Nothing
annotation_AssociativeOriginData10.VertAnnotation = Nothing
annotation_AssociativeOriginData10.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData10.HorizAnnotation = note9
annotation_AssociativeOriginData10.HorizAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData10.AlignedAnnotation = Nothing
annotation_AssociativeOriginData10.DimensionLine = 0
annotation_AssociativeOriginData10.AssociatedView = Nothing
annotation_AssociativeOriginData10.AssociatedPoint = Nothing
annotation_AssociativeOriginData10.OffsetAnnotation = Nothing
annotation_AssociativeOriginData10.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData10.XOffsetFactor = 0
annotation_AssociativeOriginData10.YOffsetFactor = 0
point3d9 = New Point3d(16.8574927841817, 1.38024175993132, 0)
note14.SetAssociativeOrigin(annotation_AssociativeOriginData10, point3d9)

integer4 = theSession.UpdateManager.DoUpdate(session_UndoMarkId5)


session_UndoMarkId6 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Annotation")


stringArray9(0) = "<C0.750>" + query_data.m_MeDate.Text() + "<C>"
point3d10= New Point3d(0, 0, 0)
Dim note15 As Note
note15 = theSession.Parts.Work.Annotations.CreateNote(stringArray9, point3d10, AxisOrientation.Horizontal, letteringPreferences1, userSymbolPreferences1)

theSession.SetUndoMarkVisibility(session_UndoMarkId6, "Create Annotation", Session.MarkVisibility.Visible)

Dim annotation_AssociativeOriginData11 As Annotation.AssociativeOriginData
annotation_AssociativeOriginData11.OriginType = Annotations.AssociativeOriginType.HorizontallyAligned
annotation_AssociativeOriginData11.View = Nothing
annotation_AssociativeOriginData11.ViewofGeometry = Nothing
annotation_AssociativeOriginData11.pointongeometry = Nothing
annotation_AssociativeOriginData11.VertAnnotation = Nothing
annotation_AssociativeOriginData11.VertAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData11.HorizAnnotation = note8
annotation_AssociativeOriginData11.HorizAlignmentPosition = Annotations.AlignmentPosition.MidCenter
annotation_AssociativeOriginData11.AlignedAnnotation = Nothing
annotation_AssociativeOriginData11.DimensionLine = 0
annotation_AssociativeOriginData11.AssociatedView = Nothing
annotation_AssociativeOriginData11.AssociatedPoint = Nothing
annotation_AssociativeOriginData11.OffsetAnnotation = Nothing
annotation_AssociativeOriginData11.OffsetAlignmentPosition = Annotations.AlignmentPosition.TopLeft
annotation_AssociativeOriginData11.XOffsetFactor = 0
annotation_AssociativeOriginData11.YOffsetFactor = 0
point3d11 = New Point3d(16.8349491151104, 1.1187076082971, 0)
note15.SetAssociativeOrigin(annotation_AssociativeOriginData11, point3d11)


integer5 = theSession.UpdateManager.DoUpdate(session_UndoMarkId6)


letteringPreferences1.Dispose()

userSymbolPreferences1.Dispose()


query_data.dispose()

End Sub

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
    Friend WithEvents Button1 As System.Windows.Forms.Button
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents Label5 As System.Windows.Forms.Label
    Friend WithEvents Label6 As System.Windows.Forms.Label
    Friend WithEvents Label7 As System.Windows.Forms.Label
    Friend WithEvents Label9 As System.Windows.Forms.Label
    Friend WithEvents Label10 As System.Windows.Forms.Label
    Friend WithEvents Label11 As System.Windows.Forms.Label
    Friend WithEvents Label12 As System.Windows.Forms.Label
    Friend WithEvents Label13 As System.Windows.Forms.Label
    Friend WithEvents Label14 As System.Windows.Forms.Label
    Friend WithEvents Label15 As System.Windows.Forms.Label
    Friend WithEvents m_CompanyName As System.Windows.Forms.TextBox
    Friend WithEvents m_DrawingName As System.Windows.Forms.TextBox
    Friend WithEvents m_DrawingNumber As System.Windows.Forms.TextBox
    Friend WithEvents m_Scale As System.Windows.Forms.TextBox
    Friend WithEvents m_sheet_no As System.Windows.Forms.TextBox
    Friend WithEvents m_ContractNumber As System.Windows.Forms.TextBox
    Friend WithEvents m_Design As System.Windows.Forms.TextBox
    Friend WithEvents m_Lead As System.Windows.Forms.TextBox
    Friend WithEvents Label8 As System.Windows.Forms.Label
    Friend WithEvents m_Str As System.Windows.Forms.TextBox
    Friend WithEvents m_Me As System.Windows.Forms.TextBox
    Friend WithEvents m_DesignDate As System.Windows.Forms.TextBox
    Friend WithEvents m_LeadDate As System.Windows.Forms.TextBox
    Friend WithEvents m_StrDate As System.Windows.Forms.TextBox
    Friend WithEvents m_MeDate As System.Windows.Forms.TextBox
    Friend WithEvents m_sheet_no_of As System.Windows.Forms.TextBox
    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
Me.Button1 = New System.Windows.Forms.Button
Me.m_CompanyName = New System.Windows.Forms.TextBox
Me.Label1 = New System.Windows.Forms.Label
Me.Label2 = New System.Windows.Forms.Label
Me.m_DrawingName = New System.Windows.Forms.TextBox
Me.Label3 = New System.Windows.Forms.Label
Me.m_DrawingNumber = New System.Windows.Forms.TextBox
Me.Label4 = New System.Windows.Forms.Label
Me.m_Scale = New System.Windows.Forms.TextBox
Me.Label5 = New System.Windows.Forms.Label
Me.m_sheet_no = New System.Windows.Forms.TextBox
Me.Label6 = New System.Windows.Forms.Label
Me.m_ContractNumber = New System.Windows.Forms.TextBox
Me.Label7 = New System.Windows.Forms.Label
Me.m_Design = New System.Windows.Forms.TextBox
Me.m_Lead = New System.Windows.Forms.TextBox
Me.Label8 = New System.Windows.Forms.Label
Me.m_Str = New System.Windows.Forms.TextBox
Me.Label9 = New System.Windows.Forms.Label
Me.m_Me = New System.Windows.Forms.TextBox
Me.Label10 = New System.Windows.Forms.Label
Me.Label11 = New System.Windows.Forms.Label
Me.m_DesignDate = New System.Windows.Forms.TextBox
Me.m_LeadDate = New System.Windows.Forms.TextBox
Me.Label12 = New System.Windows.Forms.Label
Me.m_StrDate = New System.Windows.Forms.TextBox
Me.Label13 = New System.Windows.Forms.Label
Me.m_MeDate = New System.Windows.Forms.TextBox
Me.Label14 = New System.Windows.Forms.Label
Me.Label15 = New System.Windows.Forms.Label
Me.m_sheet_no_of = New System.Windows.Forms.TextBox
Me.SuspendLayout()
'
'Button1
'
Me.Button1.Location = New System.Drawing.Point(184, 320)
Me.Button1.Name = "Button1"
Me.Button1.TabIndex = 0
Me.Button1.Text = "OK"
'
'm_CompanyName
'
Me.m_CompanyName.Location = New System.Drawing.Point(8, 32)
Me.m_CompanyName.Name = "m_CompanyName"
Me.m_CompanyName.Size = New System.Drawing.Size(192, 20)
Me.m_CompanyName.TabIndex = 1
Me.m_CompanyName.Text = ""
'
'Label1
'
Me.Label1.Location = New System.Drawing.Point(8, 8)
Me.Label1.Name = "Label1"
Me.Label1.Size = New System.Drawing.Size(192, 23)
Me.Label1.TabIndex = 2
Me.Label1.Text = "Company Name"
'
'Label2
'
Me.Label2.Location = New System.Drawing.Point(8, 64)
Me.Label2.Name = "Label2"
Me.Label2.Size = New System.Drawing.Size(192, 23)
Me.Label2.TabIndex = 3
Me.Label2.Text = "Drawing Name"
'
'm_DrawingName
'
Me.m_DrawingName.Location = New System.Drawing.Point(8, 88)
Me.m_DrawingName.Name = "m_DrawingName"
Me.m_DrawingName.Size = New System.Drawing.Size(192, 20)
Me.m_DrawingName.TabIndex = 4
Me.m_DrawingName.Text = ""
'
'Label3
'
Me.Label3.Location = New System.Drawing.Point(8, 120)
Me.Label3.Name = "Label3"
Me.Label3.Size = New System.Drawing.Size(192, 23)
Me.Label3.TabIndex = 5
Me.Label3.Text = "Drawing Number"
'
'm_DrawingNumber
'
Me.m_DrawingNumber.Location = New System.Drawing.Point(8, 152)
Me.m_DrawingNumber.Name = "m_DrawingNumber"
Me.m_DrawingNumber.Size = New System.Drawing.Size(192, 20)
Me.m_DrawingNumber.TabIndex = 6
Me.m_DrawingNumber.Text = ""
'
'Label4
'
Me.Label4.Location = New System.Drawing.Point(8, 184)
Me.Label4.Name = "Label4"
Me.Label4.Size = New System.Drawing.Size(192, 23)
Me.Label4.TabIndex = 7
Me.Label4.Text = "Scale"
'
'm_Scale
'
Me.m_Scale.Location = New System.Drawing.Point(8, 216)
Me.m_Scale.Name = "m_Scale"
Me.m_Scale.Size = New System.Drawing.Size(192, 20)
Me.m_Scale.TabIndex = 8
Me.m_Scale.Text = ""
'
'Label5
'
Me.Label5.Location = New System.Drawing.Point(8, 248)
Me.Label5.Name = "Label5"
Me.Label5.Size = New System.Drawing.Size(192, 23)
Me.Label5.TabIndex = 9
Me.Label5.Text = "Sheet Number "
'
'm_sheet_no
'
Me.m_sheet_no.Location = New System.Drawing.Point(8, 272)
Me.m_sheet_no.Name = "m_sheet_no"
Me.m_sheet_no.Size = New System.Drawing.Size(56, 20)
Me.m_sheet_no.TabIndex = 10
Me.m_sheet_no.Text = ""
'
'Label6
'
Me.Label6.Location = New System.Drawing.Point(232, 8)
Me.Label6.Name = "Label6"
Me.Label6.TabIndex = 11
Me.Label6.Text = "Contract Number"
'
'm_ContractNumber
'
Me.m_ContractNumber.Location = New System.Drawing.Point(232, 32)
Me.m_ContractNumber.Name = "m_ContractNumber"
Me.m_ContractNumber.Size = New System.Drawing.Size(208, 20)
Me.m_ContractNumber.TabIndex = 12
Me.m_ContractNumber.Text = ""
'
'Label7
'
Me.Label7.Location = New System.Drawing.Point(232, 64)
Me.Label7.Name = "Label7"
Me.Label7.TabIndex = 13
Me.Label7.Text = "Design"
'
'm_Design
'
Me.m_Design.Location = New System.Drawing.Point(232, 88)
Me.m_Design.Name = "m_Design"
Me.m_Design.TabIndex = 14
Me.m_Design.Text = ""
'
'm_Lead
'
Me.m_Lead.Location = New System.Drawing.Point(232, 152)
Me.m_Lead.Name = "m_Lead"
Me.m_Lead.TabIndex = 16
Me.m_Lead.Text = ""
'
'Label8
'
Me.Label8.Location = New System.Drawing.Point(232, 128)
Me.Label8.Name = "Label8"
Me.Label8.TabIndex = 15
Me.Label8.Text = "Lead"
'
'm_Str
'
Me.m_Str.Location = New System.Drawing.Point(232, 216)
Me.m_Str.Name = "m_Str"
Me.m_Str.TabIndex = 18
Me.m_Str.Text = ""
'
'Label9
'
Me.Label9.Location = New System.Drawing.Point(232, 192)
Me.Label9.Name = "Label9"
Me.Label9.TabIndex = 17
Me.Label9.Text = "STR"
'
'm_Me
'
Me.m_Me.Location = New System.Drawing.Point(232, 272)
Me.m_Me.Name = "m_Me"
Me.m_Me.TabIndex = 20
Me.m_Me.Text = ""
'
'Label10
'
Me.Label10.Location = New System.Drawing.Point(232, 248)
Me.Label10.Name = "Label10"
Me.Label10.TabIndex = 19
Me.Label10.Text = "ME"
'
'Label11
'
Me.Label11.Location = New System.Drawing.Point(336, 64)
Me.Label11.Name = "Label11"
Me.Label11.TabIndex = 21
Me.Label11.Text = "Signoff Date"
'
'm_DesignDate
'
Me.m_DesignDate.Location = New System.Drawing.Point(336, 88)
Me.m_DesignDate.Name = "m_DesignDate"
Me.m_DesignDate.TabIndex = 22
Me.m_DesignDate.Text = ""
'
'm_LeadDate
'
Me.m_LeadDate.Location = New System.Drawing.Point(336, 152)
Me.m_LeadDate.Name = "m_LeadDate"
Me.m_LeadDate.TabIndex = 24
Me.m_LeadDate.Text = ""
'
'Label12
'
Me.Label12.Location = New System.Drawing.Point(336, 128)
Me.Label12.Name = "Label12"
Me.Label12.TabIndex = 23
Me.Label12.Text = "Signoff Date"
'
'm_StrDate
'
Me.m_StrDate.Location = New System.Drawing.Point(336, 216)
Me.m_StrDate.Name = "m_StrDate"
Me.m_StrDate.TabIndex = 26
Me.m_StrDate.Text = ""
'
'Label13
'
Me.Label13.Location = New System.Drawing.Point(336, 192)
Me.Label13.Name = "Label13"
Me.Label13.TabIndex = 25
Me.Label13.Text = "Signoff Date"
'
'm_MeDate
'
Me.m_MeDate.Location = New System.Drawing.Point(336, 272)
Me.m_MeDate.Name = "m_MeDate"
Me.m_MeDate.TabIndex = 28
Me.m_MeDate.Text = ""
'
'Label14
'
Me.Label14.Location = New System.Drawing.Point(336, 248)
Me.Label14.Name = "Label14"
Me.Label14.TabIndex = 27
Me.Label14.Text = "Signoff Date"
'
'Label15
'
Me.Label15.Location = New System.Drawing.Point(80, 272)
Me.Label15.Name = "Label15"
Me.Label15.Size = New System.Drawing.Size(24, 23)
Me.Label15.TabIndex = 29
Me.Label15.Text = "of"
'
'm_sheet_no_of
'
Me.m_sheet_no_of.Location = New System.Drawing.Point(120, 272)
Me.m_sheet_no_of.Name = "m_sheet_no_of"
Me.m_sheet_no_of.Size = New System.Drawing.Size(64, 20)
Me.m_sheet_no_of.TabIndex = 30
Me.m_sheet_no_of.Text = ""
'
'Form1
'
Me.AutoScaleBaseSize = New System.Drawing.Size(5, 13)
Me.ClientSize = New System.Drawing.Size(472, 349)
Me.Controls.Add(Me.m_sheet_no_of)
Me.Controls.Add(Me.Label15)
Me.Controls.Add(Me.m_MeDate)
Me.Controls.Add(Me.Label14)
Me.Controls.Add(Me.m_StrDate)
Me.Controls.Add(Me.Label13)
Me.Controls.Add(Me.m_LeadDate)
Me.Controls.Add(Me.Label12)
Me.Controls.Add(Me.m_DesignDate)
Me.Controls.Add(Me.Label11)
Me.Controls.Add(Me.m_Me)
Me.Controls.Add(Me.Label10)
Me.Controls.Add(Me.m_Str)
Me.Controls.Add(Me.Label9)
Me.Controls.Add(Me.m_Lead)
Me.Controls.Add(Me.Label8)
Me.Controls.Add(Me.m_Design)
Me.Controls.Add(Me.Label7)
Me.Controls.Add(Me.m_ContractNumber)
Me.Controls.Add(Me.Label6)
Me.Controls.Add(Me.m_sheet_no)
Me.Controls.Add(Me.Label5)
Me.Controls.Add(Me.m_Scale)
Me.Controls.Add(Me.Label4)
Me.Controls.Add(Me.m_DrawingNumber)
Me.Controls.Add(Me.Label3)
Me.Controls.Add(Me.m_DrawingName)
Me.Controls.Add(Me.Label2)
Me.Controls.Add(Me.Label1)
Me.Controls.Add(Me.m_CompanyName)
Me.Controls.Add(Me.Button1)
Me.Name = "Form1"
Me.Text = "Fillout Title Block"
Me.ResumeLayout(False)

    End Sub

#End Region

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
           Me.Hide()
    End Sub

End Class

End Module





