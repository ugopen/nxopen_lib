' Example program that will convert a string
' into geometry using a true type font and
' extrude the result

Option Strict On

Imports System
Imports System.Drawing
Imports System.Drawing.Drawing2D
Imports System.Windows.Forms
Imports System.Collections
Imports NXOpen
Imports NXOpen.Features
Imports NXOpen.UF
Imports NXOpen.Utilities
Imports NXOpenUI

Module DrawText

    Private sess As Session
    Private ufSess As UFSession
    Private origin(2) As Double
    Private path As GraphicsPath
    Private text As String
    Private font As font
    Private curves As New ArrayList
    Private sketch As sketch
    Private thickness As String
    Private undoMarkId As Session.UndoMarkId

    ' Prompt the user to select a font.
    ' Return True if successful
    ' The Module level variable 'font' is set to the resulting font.
    Function SelectFont() As Boolean
        Dim fontDlg As FontDialog = New FontDialog

        SelectFont = False
        If fontDlg.ShowDialog() = DialogResult.OK Then
            font = fontDlg.Font
            SelectFont = True
        End If
    End Function
    ' Prompt the user to select a screen position
    ' Return True if successful
    ' The Module level variable 'origin' is set to the resulting point.
    Function SelectPosition() As Boolean
        Dim view As Tag
        Dim response As Integer

        ufSess.Ui.LockUgAccess(UFConstants.UF_UI_FROM_CUSTOM)
        SelectPosition = False
        Try
            ufSess.Ui.SpecifyScreenPosition("Pick location", Nothing, IntPtr.Zero, origin, view, response)
            If response = UFConstants.UF_UI_PICK_RESPONSE Then
                SelectPosition = True
            End If
        Finally
            ' Restore UI state always including in case of error.
            ufSess.Ui.UnlockUgAccess(UFConstants.UF_UI_FROM_CUSTOM)
        End Try
    End Function
    ' Prompt the user to input a text string to convert.
    ' Return True if successful
    ' The Module level variable 'text' is set to the resulting string.
    Function SelectText() As Boolean
        text = NXInputBox.GetInputString("Text", "Enter String To Convert")
        SelectText = False
        If text.Length <> 0 Then
            SelectText = True
        End If
    End Function
    ' Prompt the user to input an expresion text string to convert.
    ' Return True if successful
    ' The Module level variable 'thickness' is set to the resulting string.
    Function SelectThickness() As Boolean
        thickness = NXInputBox.GetInputString("Thickness expression", "Enter extrusion thickness")
        SelectThickness = False
        If text.Length <> 0 Then
            SelectThickness = True
        End If
    End Function
    ' Given a subset of the graphics path between the given indices 
    ' create lines between the points in the path.
    ' Assumes that caller has selected an appropriate section of the path.
    Sub CreateLinearPath(ByVal startIndex As Integer, ByVal endIndex As Integer)
        Dim j As Integer
        For j = startIndex To endIndex - 1
            Dim stpt As New Point3d
            Dim endpt As New Point3d
            stpt.x = path.PathPoints(j).X + origin(0)
            stpt.y = -path.PathPoints(j).Y + origin(1)
            stpt.z = 0
            endpt.x = path.PathPoints(j + 1).X + origin(0)
            endpt.y = -path.PathPoints(j + 1).Y + origin(1)
            endpt.z = 0
            curves.Add(sess.Parts.Work.Curves.CreateLine(stpt, endpt))
        Next
    End Sub
    ' Given a subset of the graphics path between the given indices 
    ' create splines between the points in the path.
    ' The path contains bezier segments and this converts then to B-splines.
    ' Assumes that caller has selected an appropriate section of the path.
    Sub CreateSplinePath(ByVal startIndex As Integer, ByVal endIndex As Integer)
        Dim j As Integer
        For j = startIndex To endIndex - 1 Step 3
            Dim poles(3, 3) As Double
            Dim k As Integer
            For k = 0 To 3
                poles(k, 0) = path.PathPoints(j + k).X + origin(0)
                poles(k, 1) = -path.PathPoints(j + k).Y + origin(1)
                poles(k, 2) = 0
                poles(k, 3) = 1
            Next
            Dim knots() As Double = {0, 0, 0, 0, 1, 1, 1, 1}
            Dim spl As UFCurve.Spline
            Dim spline As Tag
            Dim num_states As Integer
            Dim states() As UFCurve.State = Nothing
            spl.start_param = 0
            spl.end_param = 1
            spl.is_rational = 0
            spl.num_poles = 4
            spl.order = 4
            spl.knots = knots
            spl.poles = poles
            ufSess.Curve.CreateSpline(spl, spline, num_states, states)
            curves.Add(NXObjectManager.Get(spline))
        Next
    End Sub
    ' Create a sketch and add all curves we've created to it.
    ' Most of this was created by recording create a sketch and editting the result.
    ' Retries with different sketch names to avoid duplicate names.
    Sub CreateSketch()
        Dim point3d1 As Point3d = New Point3d(0, 0, 0)
        Dim matrix3x3_1 As Matrix3x3
        matrix3x3_1.xx = 1
        matrix3x3_1.xy = 0
        matrix3x3_1.xz = 0
        matrix3x3_1.yx = 0
        matrix3x3_1.yy = 1
        matrix3x3_1.yz = 0
        matrix3x3_1.zx = 0
        matrix3x3_1.zy = 0
        matrix3x3_1.zz = 1
        Dim datumPlane1 As DatumPlane
        datumPlane1 = sess.Parts.Work.Datums.CreateFixedDatumPlane(point3d1, matrix3x3_1)

        Dim point3d2 As Point3d = New Point3d(0, 0, 0)
        Dim point3d3 As Point3d = New Point3d(0, 1, 0)
        Dim datumAxis1 As DatumAxis
        datumAxis1 = sess.Parts.Work.Datums.CreateFixedDatumAxis(point3d2, point3d3)

        Dim point3d4 As Point3d = New Point3d(0, -3.61265461921692, 0)
        Dim point3d5 As Point3d = New Point3d(0, 3.61265461921692, 0)
        datumAxis1.SetEndPoints(point3d4, point3d5)

        Dim point3d6 As Point3d = New Point3d(0, 0, 0)
        Dim point3d7 As Point3d = New Point3d(1, 0, 0)
        Dim datumAxis2 As DatumAxis
        datumAxis2 = sess.Parts.Work.Datums.CreateFixedDatumAxis(point3d6, point3d7)

        Dim point3d8 As Point3d = New Point3d(-3.61265461921692, 0, 0)
        Dim point3d9 As Point3d = New Point3d(3.61265461921692, 0, 0)
        datumAxis2.SetEndPoints(point3d8, point3d9)

        Dim vector3d1 As Vector3d = New Vector3d(1, 0, 0)
        Dim nameCount As Integer = 0
        Do
            Dim name As String = "TEXT_SKETCH" + nameCount.ToString()
            Try
                sketch = sess.Parts.Work.Sketches.CreateSketch(name, datumPlane1, datumAxis2, vector3d1, AxisOrientation.Horizontal, Sense.Forward, PlaneNormalOrientation.Outward)
                Exit Do
            Catch ex As NXException
                If ex.ErrorCode <> 1720003 Then ' Name already exists
                    Throw
                End If
            End Try
            nameCount = nameCount + 1
        Loop

        sketch.Activate(sketch.ViewReorient.False)

        ' Inferring constraints and auto dimensions may take long time and is not really required for drawing text. 
        sess.ActiveSketch.CreateInferConstraintsSetting = sketch.CreateInferConstraintSetting.Off
        sess.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False

        Dim curve As DisplayableObject
        For Each curve In curves
            Try
                sess.ActiveSketch.AddGeometry(curve)
            Catch ex As Exception
                MessageBox.Show("Could not add: " + curve.ToString + " to sketch " + ex.Message)
            End Try
        Next

        sess.ActiveSketch.Deactivate(sketch.ViewReorient.False, sketch.UpdateLevel.Model)
    End Sub
    ' Extrude the sketch
    Sub CreateExtrusion()

        Dim nullFeature As Feature = Nothing

        Dim extrudeBuilder1 As Features.ExtrudeBuilder
        extrudeBuilder1 = sess.Parts.Work.Features.CreateExtrudeBuilder(nullFeature)

        Dim section1 As Section
        section1 = sess.Parts.Work.Sections.CreateSection(0.000001, 0.001, 0.5)

        Dim featureArray1(0) As Feature
        featureArray1(0) = sketch.Feature
        Dim curveFeatureRule1 As CurveFeatureRule
        curveFeatureRule1 = sess.Parts.Work.ScRuleFactory.CreateRuleCurveFeature(featureArray1)

        Dim rules(0) As SelectionIntentRule
        rules(0) = curveFeatureRule1
        Dim geoms() As NXObject = sketch.GetAllGeometry()
        Dim helpPoint As Point3d = New Point3d(0, 0, 0)
        section1.AddToSection(rules, geoms(0), Nothing, Nothing, helpPoint, Section.Mode.Create)

        extrudeBuilder1.Section = section1

        Dim direction1 As NXOpen.Direction
        direction1 = sess.Parts.Work.Directions.CreateDirection(sketch, Sense.Forward, SmartObject.UpdateOption.WithinModeling)
        extrudeBuilder1.Direction = direction1

        Dim limits1 As GeometricUtilities.Limits
        limits1 = extrudeBuilder1.Limits
        Dim linearLimits1 As GeometricUtilities.LinearLimits = CType(limits1, GeometricUtilities.LinearLimits)

        Dim extend1 As GeometricUtilities.Extend
        extend1 = linearLimits1.StartExtend
        extend1.SetValue("0")

        Dim extend2 As GeometricUtilities.Extend
        extend2 = linearLimits1.EndExtend
        extend2.SetValue(thickness)

        Dim featureOptions1 As GeometricUtilities.FeatureOptions
        featureOptions1 = extrudeBuilder1.FeatureOptions
        featureOptions1.BodyType = GeometricUtilities.FeatureOptions.BodyStyle.Solid

        Dim feature5 As Feature
        feature5 = extrudeBuilder1.CommitFeature()

        extrudeBuilder1.Destroy()

    End Sub
    ' Main routine for this journal
    Sub Main()
        sess = Session.GetSession()
        ufSess = UFSession.GetUFSession()

        If Not SelectFont() Then
            Return
        End If
        If Not SelectText() Then
            Return
        End If
        If Not SelectPosition() Then
            Return
        End If

        undoMarkId = sess.SetUndoMark(Session.MarkVisibility.Visible, "Create geometry from text")

        path = New GraphicsPath(FillMode.Alternate)
        Dim zero As New System.Drawing.Point(0, 0)
        Dim format As StringFormat = StringFormat.GenericDefault
        path.AddString(text, font.FontFamily, font.Style, font.SizeInPoints, zero, format)

        Dim bounds As RectangleF = path.GetBounds()
        Dim gpi As New GraphicsPathIterator(path)
        gpi.Rewind()

        origin(0) -= bounds.Left
        origin(1) += bounds.Bottom

        Dim iSubPath As Integer
        Dim subPathCount As Integer = gpi.SubpathCount

        For iSubPath = 0 To subPathCount - 1
            Dim mySubPaths As Integer
            Dim IsClosed As Boolean
            Dim subPathStartIndex, subPathEndIndex As Integer
            Dim stpt As New Point3d
            Dim endpt As New Point3d

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
                stpt.x = path.PathPoints(subPathStartIndex).X + origin(0)
                stpt.y = -path.PathPoints(subPathStartIndex).Y + origin(1)
                stpt.z = 0
                endpt.x = path.PathPoints(subPathEndIndex).X + origin(0)
                endpt.y = -path.PathPoints(subPathEndIndex).Y + origin(1)
                endpt.z = 0
                ' Do not create zero length lines
                If Math.Abs(stpt.x - endpt.x) > 0.000001 Or Math.Abs(stpt.y - endpt.y) > 0.000001 Then
                    curves.Add(sess.Parts.Work.Curves.CreateLine(stpt, endpt))
                End If
            End If
        Next
        If SelectThickness() Then
            CreateSketch()
            CreateExtrusion()
        End If
    End Sub
End Module


