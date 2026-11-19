' ===================================================================
'
'             Copyright (c) 2004  UGS PLM Solutions
'               Unpublished - All rights reserved
'
' ===================================================================
' *******************************************************************
'  Description
'    Class responsible for drawing the polygons in Sketcher.
'
'  
'
' *******************************************************************
Option Strict On

Imports System
Imports System.Collections
Imports System.Reflection
Imports System.Windows.Forms

Imports NXOpen
Imports NXOpen.Utilities
Imports NXOpen.UF

' Creates polygons in sketches
' The polygons may be inscribed, or circumscribed by a circle
Public NotInheritable Class PolygonDraw

     ' Initialize to some values. These should get reset in the constructor.
    Private m_numberOfSides As Integer = 0
    Private m_diameter As Double = 0.0
    Private m_cornerDistance As Double = 0.0
    Private m_segmentAngle As Double = 0.0
    Private m_startAngle As Double = 0.0

    Private m_polygonPoints As ArrayList = New ArrayList

    Private m_inscribed As Boolean = True

    Private m_session As Session
    Private m_ufSession As UFSession
    Private m_sketch As Sketch
    Private m_baseCircle As Arc
    Private m_polygonLines As ArrayList = New ArrayList

    ' Public methods

    Public Sub New(ByVal numberOfSides As Integer, ByVal diameter As Double, ByVal inscribed As Boolean)

        m_numberOfSides = numberOfSides
        m_diameter = diameter
        m_inscribed = inscribed

        m_segmentAngle = 360.0 / m_numberOfSides

        ' Get a handle to the session
        m_session = NXOpen.Session.GetSession()
        m_ufSession = NXOpen.UF.UFSession.GetUFSession()

        ' Get the active sketch
        If (m_session.ActiveSketch Is Nothing) Then
            ' There is no active sketch...
            Dim err As Exception = New Exception("No active sketch")
            Throw err
        Else
            m_sketch = m_session.ActiveSketch
        End If

        ' Sort out some default values...
        Dim even As Boolean = Me.EvenSidesCheck()

        If even Then
            ' First location is at angle/2 from x axis, so always get a flat
            ' crossing the x-axis, and a vertex on the y-axis. Note this puts
            ' a square at 45 degrees
            m_startAngle = m_segmentAngle / 2
        Else
            ' Always put a vertex on the y-axis
            ' For no_sides > 3, first location is 90 - angle, as angle will be
            ' less than 90 (but in radians, of course)
            If m_numberOfSides = 3 Then
                ' First location is below the x-axis
                m_startAngle = 360.0 - (m_segmentAngle - 90.0)
            Else
                ' First location is above the x-axis
                m_startAngle = 90.0 - m_segmentAngle
            End If
        End If

        ' The distance from the origin to the vertex
        If m_inscribed Then
            If even Then
                m_cornerDistance = (m_diameter / 2) / (Math.Cos(Math.PI * m_startAngle / 180.0))
            Else
                If m_numberOfSides = 3 Then
                    ' For a circumscribed triangle, the length of the vertex
                    ' from the origin is 
                    m_cornerDistance = (m_diameter / 2) / (Math.Sin((m_segmentAngle - 90) * Math.PI / 180.0))
                Else
                    ' For an inscribed triangle, the length of the vertex from
                    ' the origin is 
                    m_cornerDistance = (m_diameter / 2) / (Math.Sin(((90 - m_segmentAngle / 2) * Math.PI) / 180.0))
                End If
            End If
        Else
            m_cornerDistance = m_diameter / 2
        End If

    End Sub

    Public Sub Draw()
        Dim undoString As String = String.Concat("Create ", Me.m_numberOfSides.ToString, " sided polygon")
        Dim undoMark As Session.UndoMarkId = _
            Me.m_session.SetUndoMark(Session.MarkVisibility.Visible, undoString)

        Me.CreateBaseCircle()
        Me.CreatePolygonPointData()
        Me.CreatePolygonLines()
        Me.AddDimensionalConstraint()
        Me.m_session.ActiveSketch.Update()

    End Sub

    ' Private methods

    Private Function EvenSidesCheck() As Boolean

        ' Check if the number of sides is even or odd.  Return true if even
        Return ((Me.m_numberOfSides Mod 2) = 0)

    End Function

    Private Sub CreatePolygonPointData()

        ' This uses the m_polygonPoints ArrayList

        Dim angle As Double = 90.0 ' Start with a vertex on the y-axis
        Dim point As Point3d = New Point3d(0.0, 0.0, 0.0)

        For i As Integer = 0 To (m_numberOfSides - 1)
            ' Calculate the points and put them in the arraylist.        
            ' This is all 2D for now, from 0,0,0, and later gets transformed and
            ' rotated on the the active sketch plane
            point.x = m_cornerDistance * Math.Cos(angle * Math.PI / 180)
            point.y = m_cornerDistance * Math.Sin(angle * Math.PI / 180)
            point.z = 0.0

            m_polygonPoints.Add(point)

            angle += m_segmentAngle
        Next

        ' Now we have all the 'basic' data, transform it to the sketch orientation
        Me.TransformPolygonPointData()
    End Sub

    Private Sub CreateBaseCircle()
        Try

            ' FIX ME: Would be better to prompt user for center of arc rather than
            ' use the sketch origin
            m_baseCircle = m_session.Parts.Work.Curves.CreateArc( _
                m_sketch.Origin, m_sketch.Orientation, m_diameter / 2, 0, 2 * Math.PI)

            m_session.ActiveSketch.AddGeometry(m_baseCircle, _
                Sketch.InferConstraintsOption.InferCoincidentConstraints)

            ' Make the circle a reference curve
            ' FIX ME: Use JA API routine to do this when available
            m_ufSession.Sket.SetReferenceStatus(m_sketch.Tag, m_baseCircle.Tag, _
                UFSket.ReferenceStatus.Reference)
        Catch
            MessageBox.Show("Cannot create arc")
            Throw
        End Try
    End Sub

    Private Sub CreatePolygonLines()
        Try
            ' Now add the lines
            ' Watch the unboxing.  As the arraylist holds objects, these get boxed as they are added to the arraylist.
            ' As these are created in the class (in private members) or local, then we should be OK to unbox?
            ' otherwise should use "as" to check and unbox or "is" to check, and then unbox. 

            Dim i As Integer
            Dim line As Line
            For i = 0 To (m_polygonPoints.Count - 2)
                line = m_session.Parts.Work.Curves.CreateLine( _
                    CType(m_polygonPoints(i), Point3d), CType(m_polygonPoints(i + 1), Point3d))
                m_polygonLines.Add(line)
            Next
            line = m_session.Parts.Work.Curves.CreateLine( _
                CType(m_polygonPoints(i), Point3d), CType(m_polygonPoints(0), Point3d))
            m_polygonLines.Add(line)

            Me.MakeCoincidentConstraints()
            Me.MakeEqualLengthConstraints()

            If EvenSidesCheck() Then
                ' Add parallel constraints across the pairs
                Me.CreateParallelConstraints()
            Else
                ' Add a horizontal constraint to the bottom line, to anchor
                ' the(polygon). Get the number of the element to add the
                ' constraint to. If its odd, then the division remainder is
                ' .5, and the conversion should get the right number
                Dim n As Integer = CType(m_numberOfSides / 2, Integer)
                Me.CreateHorizontalConstaint(CType(m_polygonLines(n), Line))
            End If

            If m_inscribed Then
                Me.MakeTangentConstraints()
            Else
                Me.MakePointOnCurveConstraints()
            End If

            m_session.ActiveSketch.Update()
        Catch
            MessageBox.Show("Problem creating polygon lines")
        End Try
    End Sub

    Private Sub MakeTangentConstraints()
        ' Constrain each of the lines tangent to the base circle (m_baseCircle)
        ' make a point at the endpoint of each line as the helper point, then
        ' transform it to the correct location (ie the sketch plane)

        Dim skConstGeom1 As Sketch.ConstraintGeometry = _
            New Sketch.ConstraintGeometry(m_baseCircle, Sketch.ConstraintPointType.None, 0)

        Dim sketchConstraintGeometryHelp1 As Sketch.ConstraintGeometryHelp
        sketchConstraintGeometryHelp1.type = Sketch.ConstraintGeometryHelpType.Point
        sketchConstraintGeometryHelp1.parameter = 0

        Dim sketchConstraintGeometryHelp2 As Sketch.ConstraintGeometryHelp
        sketchConstraintGeometryHelp2.type = Sketch.ConstraintGeometryHelpType.Point
        sketchConstraintGeometryHelp2.parameter = 0

        For Each line As Line In m_polygonLines
            sketchConstraintGeometryHelp1.point = line.EndPoint
            sketchConstraintGeometryHelp2.point = line.EndPoint

            ' Needs to have the parallel constraints added to stop this causing
            ' a 'wobble' caused by the helper point (at the end of the straights...)
            Dim skConstGeom2 As Sketch.ConstraintGeometry = _
                New Sketch.ConstraintGeometry(line, Sketch.ConstraintPointType.None, 0)

            Dim sketchTangentConstraint As SketchTangentConstraint = _
                m_session.ActiveSketch.CreateTangentConstraint(skConstGeom1, _
                    sketchConstraintGeometryHelp1, skConstGeom2, sketchConstraintGeometryHelp2)
        Next

    End Sub

    ' Point methods
    Private Function TransformPoint(ByVal toPoint As Point3d, ByVal rotation As Matrix3x3, _
        ByVal fromPoint As Point3d) As Point3d

        Dim newPoint As Point3d

        newPoint.x = toPoint.x + rotation.xx * fromPoint.x + rotation.yx * fromPoint.y
        newPoint.y = toPoint.y + rotation.xy * fromPoint.x + rotation.yy * fromPoint.y
        newPoint.z = toPoint.z + rotation.xz * fromPoint.x + rotation.yz * fromPoint.y

        Return newPoint

    End Function

    Private Sub TransformPolygonPointData()
        ' Take all the point data in the polygon point arraylist and transform
        ' it to the sketch plane need to unbox the m_polygonPoints[0] object
        Dim polygonCenter As Point3d = m_baseCircle.CenterPoint
        Dim polygonOrientation As Matrix3x3 = m_sketch.Orientation.Element

        For i As Integer = 0 To (m_polygonPoints.Count - 1)
            m_polygonPoints(i) = TransformPoint(polygonCenter, polygonOrientation, _
                CType(m_polygonPoints(i), Point3d))
        Next
    End Sub

    ' String handling methods
    Private Function GetUniqueExpressionName(ByVal str As String) As String
        ' Takes the given expression name and sees if it exists.  If it does,
        ' then it appends an integer to the name to make it unique
        Dim i As Integer = 1
        Dim check As Boolean = False
        Do
            check = Me.CompareExpressionNames(str)
            If check Then
                i = i + 1
                str = str + i.ToString()
            End If
        Loop While check

        Return str
    End Function

    Private Function CompareExpressionNames(ByVal str As String) As Boolean

        ' Expression implements System.Collections.IEnumerable so we can
        ' loop over all the expressions in the work part
        For Each exp As Expression In m_session.Parts.Work.Expressions
            If String.Compare(str, exp.Name) = 0 Then
                Return True
            End If
        Next

        Return False
    End Function

    ' constraints methods
    Private Sub MakeEqualLengthConstraints()
        ' Get the first line in the m_polygonLines arraylist
        ' Need to unbox the m_polygonLines(0) object
        Dim skGeom1 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry( _
            CType(m_polygonLines(0), Line), Sketch.ConstraintPointType.None, 0)

        Dim skGeom2 As Sketch.ConstraintGeometry
        Dim skGeomConstraint As SketchGeometricConstraint

        Dim breakValue As Integer
        If m_numberOfSides > 9 Then
            breakValue = m_numberOfSides - 1
        Else
            breakValue = m_numberOfSides
        End If

        For i As Integer = 1 To (breakValue - 1)
            ' Need to unbox the m_polygonLines(i) object
            skGeom2 = New Sketch.ConstraintGeometry(CType(m_polygonLines(i), Line), _
                Sketch.ConstraintPointType.None, 0)
            ' Constraint each one in turn to the first in the list
            skGeomConstraint = m_session.ActiveSketch.CreateEqualLengthConstraint(skGeom1, skGeom2)
        Next

    End Sub


    Private Sub MakeCoincidentConstraints()
        ' Need to unbox the m_polygonLines(0) object
        For Each line As Line In m_polygonLines
            m_session.ActiveSketch.AddGeometry(line, _
                Sketch.InferConstraintsOption.InferCoincidentConstraints)
        Next
    End Sub

    Private Sub MakePointOnCurveConstraints()
        Dim skGeom1 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry( _
            m_baseCircle, Sketch.ConstraintPointType.None, 0)

        Dim skConstraintGeometryHelp As Sketch.ConstraintGeometryHelp
        skConstraintGeometryHelp.type = Sketch.ConstraintGeometryHelpType.Point
        Dim SketchHelpedGeometricConstraint As SketchHelpedGeometricConstraint

        For Each line As Line In m_polygonLines
            Dim skGeom2 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry( _
                line, Sketch.ConstraintPointType.EndVertex, 0)
            skConstraintGeometryHelp.point = line.StartPoint
            skConstraintGeometryHelp.parameter = 0

            SketchHelpedGeometricConstraint = _
                m_session.ActiveSketch.CreatePointOnCurveConstraint( _
                    skGeom1, skGeom2, skConstraintGeometryHelp)
        Next
    End Sub

    Private Sub CreateVerticalConstraint(ByVal line As Line)
        Dim skGeom As Sketch.ConstraintGeometry = New _
            Sketch.ConstraintGeometry(line, Sketch.ConstraintPointType.None, 0)
        Dim skGeomConstraint As SketchGeometricConstraint
        skGeomConstraint = m_session.ActiveSketch.CreateVerticalConstraint(skGeom)
    End Sub

    Private Sub CreateHorizontalConstaint(ByVal line As Line)
        Dim skGeom As Sketch.ConstraintGeometry = New _
            Sketch.ConstraintGeometry(line, Sketch.ConstraintPointType.None, 0)
        Dim skGeomConstraint As SketchGeometricConstraint
        skGeomConstraint = m_session.ActiveSketch.CreateHorizontalConstraint(skGeom)
    End Sub

    Private Sub CreateParallelConstraints()
        ' Add parallel constraints across the sides
        Dim interval As Integer = CType(m_numberOfSides / 2, Integer) ' Should be the same as m_polygonLines.Count

        ' If number of sides > 6, polygon goes overconstrained.  Check for this
        ' and set the 'break' value
        Dim breakValue As Integer = 0
        If (m_numberOfSides > 6) Then
            breakValue = interval - 1
        Else
            breakValue = interval
        End If

        For i As Integer = 0 To (breakValue - 1)
            Dim skGeom1 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry( _
                CType(m_polygonLines(i), Line), Sketch.ConstraintPointType.None, 0)
            Dim skGeom2 As Sketch.ConstraintGeometry = New Sketch.ConstraintGeometry( _
                CType(m_polygonLines(i + interval), Line), Sketch.ConstraintPointType.None, 0)

            Dim parallelConstraint As SketchGeometricConstraint = _
                m_session.ActiveSketch.CreateParallelConstraint(skGeom1, skGeom2)
        Next
    End Sub

    Private Sub AddDimensionalConstraint()
        ' Add dimensional constraint to the circle...
        Dim skDim As Sketch.DimensionGeometry = New Sketch.DimensionGeometry
        skDim.Geometry = m_baseCircle
        skDim.AssocType = Sketch.AssocType.Tangency
        skDim.AssocValue = 11

        Dim dimTextPoint As Point3d = New Point3d(0.0, 0.0, 0.0)

        ' Put the dimension at 45 degrees from the x-axis, at dia * something
        Dim factor As Double = 1.5 * (m_diameter / 2)
        dimTextPoint.x = factor * Math.Cos(45 * Math.PI / 180)
        dimTextPoint.y = factor * Math.Sin(45 * Math.PI / 180)

        dimTextPoint = TransformPoint(m_sketch.Origin, m_sketch.Orientation.Element, dimTextPoint)

        Dim expName As String = GetUniqueExpressionName("dia")
        expName = expName + " = " + m_diameter.ToString()

        Try
            Dim exp As Expression = m_session.Parts.Work.Expressions.Create(expName)
            Dim skDimConstraint As SketchDimensionalConstraint = _
                m_session.ActiveSketch.CreateDiameterDimension(skDim, dimTextPoint, exp)
        Catch
            ' Could not create the expression
        End Try

    End Sub

End Class
