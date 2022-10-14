' Converts a TrueType font string into curves, and then extrudes them

Option Infer On

Imports Snap, Snap.Create, Snap.UI.Input
Imports System
Imports System.Drawing
Imports System.Drawing.Drawing2D
Imports System.Windows.Forms
Imports System.Collections.Generic

Module MyProgram

   ' Global (module level) variables   
   Private origin As Position                 ' Position where extrusion will be located
   Private path As GraphicsPath               ' Graphics path holding the text string
   Private text As String                     ' The string to be extruded
   Private font As Font                       ' The Windows font to be used
   Private curves As New List(Of NX.Curve)    ' List of curves to be extruded
   Private thickness As Double                ' The thickness (distance) of the extrusion

   ' Prompt the user to select a font, returning True if successful
   ' The Module level variable 'font' is set to the resulting font.
   Function SelectFont() As Boolean
      Dim fontDlg As FontDialog = New FontDialog

      SelectFont = False
      If fontDlg.ShowDialog() = DialogResult.OK Then
         font = fontDlg.Font
         SelectFont = True
      End If
   End Function
   
   ' Prompt the user to specify a position, returning True if successful
   ' The Module level variable 'origin' is set to the resulting point.
   Function SelectPosition() As Boolean
      origin = GetPosition("Specify origin").Position
      SelectPosition = True
   End Function

   ' Prompt the user to input a text string to extrude, returning True if successful
   ' The Module level variable 'text' is set to the resulting string.
   Function SelectText() As Boolean
      text = GetString("Enter text to be extruded", "Enter Text", "Text", " ")
      SelectText = False
      If text.Length <> 0 Then
         SelectText = True
      End If
   End Function

   ' Prompt the user to input an extrusion thickness, returning True if successful
   ' The Module level variable 'thickness' is set to the resulting value.
   Function SelectThickness() As Boolean
       thickness = GetDouble ("Enter extrusion thickness", "Enter thickness", "Thickness", 1.0)
      SelectThickness = True
   End Function

   ' Given a subset of the graphics path between the given indices 
   ' create lines between the points in the path.
   ' Assumes that caller has selected an appropriate section of the path.
   Sub CreateLinearPath(ByVal startIndex As Integer, ByVal endIndex As Integer)
      For j = startIndex To endIndex - 1
         Dim p0 As Position = PathPointPosition(path.PathPoints(j))
         Dim p1 As Position = PathPointPosition(path.PathPoints(j+1))
         curves.Add(Line(p0, p1))
      Next
   End Sub

   Function PathPointPosition(point As System.Drawing.PointF) As Snap.Position
      Return New Position(point.X + origin.X, -point.Y + origin.Y)
   End Function

   ' Given a subset of the graphics path between the given indices 
   ' create splines (Bezier curves) between the points in the path.
   ' Assumes that caller has selected an appropriate section of the path.
   Sub CreateSplinePath(ByVal startIndex As Integer, ByVal endIndex As Integer)
      For j = startIndex To endIndex - 1 Step 3
         Dim poles(3) As Position
         For k = 0 To 3
            poles(k) =  PathPointPosition(path.PathPoints(j + k))
         Next
         curves.Add(BezierCurve(poles))
      Next
   End Sub
  
   ' Main routine for this application
   Public Sub Main()

      If Not SelectFont() Then
         Return
     End If
      If Not SelectText() Then
         Return
      End If
      If Not SelectPosition() Then
         Return
      End If

      path = New GraphicsPath(FillMode.Alternate)
      Dim zero As New System.Drawing.Point(0, 0)
      Dim format As StringFormat = StringFormat.GenericDefault
      path.AddString(text, font.FontFamily, font.Style, font.SizeInPoints, zero, format)

      Dim bounds As RectangleF = path.GetBounds()
      Dim gpi As New GraphicsPathIterator(path)
      gpi.Rewind()

      origin.X -= bounds.Left
      origin.Y += bounds.Bottom

      Dim subPathCount As Integer = gpi.SubpathCount

      For iSubPath = 0 To subPathCount - 1
         Dim mySubPaths As Integer
         Dim IsClosed As Boolean
         Dim subPathStartIndex, subPathEndIndex As Integer
         Dim stpt As New Position
         Dim endpt As New Position

         mySubPaths = gpi.NextSubpath(subPathStartIndex, subPathEndIndex, IsClosed)
         Dim pointTypeStartIndex, pointTypeEndIndex As Integer
         Do
            Dim subPathPointType As Byte
            Dim numPointsFound As Integer = gpi.NextPathType(subPathPointType, pointTypeStartIndex, pointTypeEndIndex)
            Dim type As PathPointType = CType(subPathPointType, PathPointType)

            If type = PathPointType.Line Then
               CreateLinearPath(pointTypeStartIndex, pointTypeEndIndex)
            ElseIf type = PathPointType.Bezier3 Then
               CreateSplinePath(pointTypeStartIndex, pointTypeEndIndex)
            End If
         Loop While subPathEndIndex <> pointTypeEndIndex
         If IsClosed Then
            stpt  =  PathPointPosition(path.PathPoints(subPathStartIndex))
            endpt =  PathPointPosition(path.PathPoints(subPathEndIndex))
            ' Do not create zero length lines
            If Position.Distance(stpt, endpt) > 0.000001 Then
               curves.Add(Line(stpt, endpt))
            End If
         End If
      Next
      If SelectThickness() Then 
         ExtrudeSheet(curves.ToArray, Vector.AxisZ, thickness)
      End If
   End Sub

   Public Function GetUnloadOption(ByVal dummy As String) As Integer
      Dim unloadOption As Integer = NXOpen.Session.LibraryUnloadOption.Immediately       ' After executing
      Return unloadOption
   End Function

End Module
