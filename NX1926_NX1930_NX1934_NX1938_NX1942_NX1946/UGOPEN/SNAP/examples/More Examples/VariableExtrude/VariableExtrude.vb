Option Infer On
Imports Snap, Snap.Create, Snap.NX.ObjectTypes

Public Class VariableExtrude : Inherits UI.BlockForm

    ' The various members of a VariableExtrude object
    Dim selectCurveBlock As UI.Block.SelectObject
    Dim directionBlock As UI.Block.SpecifyVector
    Dim distanceAtStartBlock As UI.Block.Double
    Dim distanceAtEndBlock As UI.Block.Double

    ' Constructor to create a VariableExtrude object
    Public Sub New()

        Me.Title = "Extrusion Curve"

        selectCurveBlock = New UI.Block.SelectObject("Please select a curve to be extruded", "Select Curve")

        directionBlock = New UI.Block.SpecifyVector
        directionBlock.Label = "Specify Vector"
        directionBlock.Direction = Vector.AxisZ

        distanceAtStartBlock = New UI.Block.Double("Distance at the start of curve", 10)

        distanceAtEndBlock = New UI.Block.Double("Distance at the end of curve", 20)

        Me.AddBlocks(selectCurveBlock, directionBlock, distanceAtStartBlock, distanceAtEndBlock)

    End Sub

    ' The main function
    Public Shared Sub Main()

        Dim variableExtrude As New VariableExtrude()    ' Create a dialog
        variableExtrude.Show()                          ' Display it

    End Sub

    ' Function that gets called immediately before your dialog is shown (displayed to the user).
    Public Overrides Sub OnShow()

        selectCurveBlock.SetCurveFilter()

    End Sub

    ' Function that gets called when user clicks OK
    Public Overrides Sub OnOK()

        OnApply()

    End Sub

    ' Function that gets called when user clicks Apply
    Public Overrides Sub OnApply()

        Dim nxObj As NX.NXObject = selectCurveBlock.SelectedObjects(0)
        Dim curve As NX.Curve = CType(nxObj, NX.Curve)
        CreateVariableExtrude(curve, directionBlock.Direction, distanceAtStartBlock.Value, distanceAtEndBlock.Value)

    End Sub

    ''' <summary>Creates a "Variable Extrusion"</summary>
    ''' <param name="generator">Generator curve -- curve to be extruded</param>
    ''' <param name="direction">Extrusion direction</param>
    ''' <param name="d0">Distance to extrude at start of curve</param>
    ''' <param name="d1">Distance to extrude at end of curve</param>
    ''' <returns>Extruded body (a sheet body)</returns>
    Private Shared Function CreateVariableExtrude(generator As NX.Curve, direction As Vector, d0 As Double, d1 As Double) As NX.Body

        Dim n = 9                      ' Arbitrary choice of how many points to use
        Dim minU = generator.MinU
        Dim maxU = generator.MaxU
        Dim stepU = (maxU - minU) / n
        Dim s, t, u As Double
        Dim curvePoint As Position
        Dim unitOffset = Vector.Unit(direction)
        Dim offsetPoints As Position() = New Position(n) {}
        Dim offsetDistance As Double

        ' Step along generator curve, computing "offset" points
        For i = 0 To n
            u = minU + i * stepU
            curvePoint = generator.Position(u)
            t = (u - minU) / (maxU - minU)              ' Unitized parameter
            s = t * t * (3 - 2 * t)                     ' Blending function (Hermite cubic)
            offsetDistance = (1 - s) * d0 + s * d1
            offsetPoints(i) = curvePoint + offsetDistance * unitOffset
        Next

        ' Construct spline through the offset points
        Dim startTangent = generator.Tangent(minU)
        Dim endTangent = generator.Tangent(maxU)
        Dim offsetCurve = SplineThroughPoints(offsetPoints, startTangent, endTangent)

        ' Create a ruled feature and get its body
        Dim ruledFeature As NX.Ruled = Ruled(generator, offsetCurve)
        Dim ruledBody As NX.Body = ruledFeature.Body

        NX.Feature.Orphan(ruledFeature)
        NX.NXObject.Delete(offsetCurve)

        Return ruledBody

    End Function

End Class