Option Strict Off
Imports Snap, Snap.Create, Snap.NX.ObjectTypes

Public Class HoleInfo : Inherits UI.BlockForm

    ' The various members of a HoleInformation object
    Dim selectHoleBlock As UI.Block.SelectObject   ' A SelectObject block to select a hole
    Dim diameterBlock As UI.Block.Double           ' Block to show the hole diameter

    ' Constructor to create a HoleInfo object
    Public Sub New()

        Me.Title = "Hole Information"

        ' Set up selection filter
        Dim arcEdgeCombo As New TypeCombo(Type.Edge, SubType.EdgeCircle)
        Dim ellipseEdgeCombo As New TypeCombo(Type.Edge, SubType.EdgeEllipse)
        Dim cylinderFaceCombo As New TypeCombo(Type.Face, SubType.FaceCylinder)
        Dim typeCombos As TypeCombo() = {arcEdgeCombo, ellipseEdgeCombo, cylinderFaceCombo}

        ' A selection block to provide selection of a "hole"
        Dim cue As String = "Select a circular or elliptical curve, or a cylindrical face"
        Dim label As String = "Select a hole"
        selectHoleBlock = New UI.Block.SelectObject(cue, label)
        selectHoleBlock.SetFilter(typeCombos)

        ' Block to report the diameter of the hole
        diameterBlock = New UI.Block.Double("Diameter")
        diameterBlock.ReadOnly = True

        ' Add the two block to the dialog
        Me.AddBlocks(selectHoleBlock, diameterBlock)

    End Sub

    ' The main function
    Public Shared Sub Main()

        Dim holeInfo As New HoleInfo()     ' Create a dialog
        holeInfo.Show()                    ' Display it

    End Sub

    ' Function that gets called when user does anything in dialog
    Public Overrides Sub OnUpdate(changedBlock As Snap.UI.Block.General)

        Dim obj As Object = selectHoleBlock.SelectedObjects(0)

        ' Circular edge
        If obj.ObjectSubType = SubType.EdgeCircle Then
            diameterBlock.Value = obj.Geometry.Radius * 2

            ' Elliptical edge
        ElseIf obj.ObjectSubType = SubType.EdgeEllipse Then
            diameterBlock.Value = obj.Geometry.RadiusY * 2

            ' Cylindrical face
        ElseIf obj.ObjectType = Type.Face And obj.ObjectSubType = SubType.FaceCylinder Then
            diameterBlock.Value = obj.Geometry.Diameter
        End If

        ' Unselect the object (remove it from the SelectedObjects array)
        selectHoleBlock.SelectedObjects = New NX.NXObject() {}

    End Sub

End Class
