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
    Private sketch1 As sketch
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
        Dim theSession As Session = Session.GetSession()
        Dim workPart As Part = theSession.Parts.Work
        Dim displayPart As Part = theSession.Parts.Display

        Dim markId1 As Session.UndoMarkId
        markId1 = theSession.SetUndoMark(Session.MarkVisibility.Visible, "Start")

        Dim nullSketch As Sketch = Nothing

        Dim sketchInPlaceBuilder1 As SketchInPlaceBuilder
        sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(nullSketch)

        Dim unit1 As Unit = CType(workPart.UnitCollection.FindObject("Inch"), Unit)

        Dim expression1 As Expression
        expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

        Dim expression2 As Expression
        expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)

        theSession.SetUndoMarkName(markId1, "'Create Sketch Dialog")

        Dim markId2 As Session.UndoMarkId
        markId2 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Sketch")

        theSession.DeleteUndoMark(markId2, Nothing)

        Dim markId3 As Session.UndoMarkId
        markId3 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "Create Sketch")

        ' Inferring constraints and auto dimensions may take long time and is not really required for drawing text. 
        theSession.Preferences.Sketch.CreateInferredConstraints = False
        theSession.Preferences.Sketch.ContinuousAutoDimensioning = False
        theSession.Preferences.Sketch.DimensionLabel = Preferences.SketchPreferences.DimensionLabelType.Expression
        theSession.Preferences.Sketch.TextSizeFixed = True
        theSession.Preferences.Sketch.FixedTextSize = 0.12
        theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
        theSession.Preferences.Sketch.DisplayObjectColor = False
        theSession.Preferences.Sketch.DisplayObjectName = False

        Dim nXObject1 As NXObject
        nXObject1 = sketchInPlaceBuilder1.Commit()
        sketch1 = CType(nXObject1, Sketch)

        Dim markId4 As Session.UndoMarkId
        markId4 = theSession.SetUndoMark(Session.MarkVisibility.Invisible, "update")

        Dim nErrs1 As Integer
        nErrs1 = theSession.UpdateManager.DoUpdate(markId4)

        sketch1.Activate(sketch.ViewReorient.False)

        Dim curve As DisplayableObject
        For Each curve In curves
            Try
                sess.ActiveSketch.AddGeometry(curve)
            Catch ex As Exception
                MessageBox.Show("Could not add: " + curve.ToString + " to sketch " + ex.Message)
            End Try
        Next

        sess.ActiveSketch.Deactivate(sketch.ViewReorient.False, sketch.UpdateLevel.Model)

        theSession.DeleteUndoMark(markId3, Nothing)
        theSession.SetUndoMarkName(markId1, "Create Sketch")
        sketchInPlaceBuilder1.Destroy()

        Try
            ' 'Expression is still in use.
            workPart.Expressions.Delete(expression2)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

        Try
            ' 'Expression is still in use.
            workPart.Expressions.Delete(expression1)
        Catch ex As NXException
            ex.AssertErrorCode(1050029)
        End Try

    End Sub
    ' Extrude the sketch
    Sub CreateExtrusion()

        Dim nullFeature As Feature = Nothing

        Dim extrudeBuilder1 As Features.ExtrudeBuilder
        extrudeBuilder1 = sess.Parts.Work.Features.CreateExtrudeBuilder(nullFeature)

        Dim section1 As Section
        section1 = sess.Parts.Work.Sections.CreateSection(0.000001, 0.001, 0.5)

        Dim featureArray1(0) As Feature
        featureArray1(0) = sketch1.Feature
        Dim curveFeatureRule1 As CurveFeatureRule
        curveFeatureRule1 = sess.Parts.Work.ScRuleFactory.CreateRuleCurveFeature(featureArray1)

        Dim rules(0) As SelectionIntentRule
        rules(0) = curveFeatureRule1
        Dim geoms() As NXObject = sketch1.GetAllGeometry()
        Dim helpPoint As Point3d = New Point3d(0, 0, 0)
        section1.AddToSection(rules, geoms(0), Nothing, Nothing, helpPoint, Section.Mode.Create)

        extrudeBuilder1.Section = section1

        Dim direction1 As NXOpen.Direction
        direction1 = sess.Parts.Work.Directions.CreateDirection(sketch1, Sense.Forward, SmartObject.UpdateOption.WithinModeling)
        extrudeBuilder1.Direction = direction1

        extrudeBuilder1.Limits.StartExtend.Value.RightHandSide = "0"
        extrudeBuilder1.Limits.EndExtend.Value.RightHandSide = thickness

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


