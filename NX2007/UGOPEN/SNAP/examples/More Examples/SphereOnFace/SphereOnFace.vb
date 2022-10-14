Option Infer On
Option Strict Off
Imports Snap, Snap.Create, Snap.NX.ObjectTypes

Partial Public Class SphereOnFace : Inherits UI.BlockForm

    ' Member variables of a SphereOnFace object
    Dim selectionBlock As Snap.UI.Block.SelectObject
    Dim diameterBlock As Snap.UI.Block.Double
    Dim flipButton As New Snap.UI.Block.Button
    Dim diameter As Double = 10.0
    Dim flip As Double = 1.0

    'Creates a new SphereOnFace dialog 
    Public Sub New()

        Me.Title = "Sphere On Face"    ' Title of dialog

        ' Create a selection block
        selectionBlock = New Snap.UI.Block.SelectObject()
        selectionBlock.LabelString = "Select target face"
        selectionBlock.Cue = "Please select a face"

        ' Create a double block to enter diameter
        diameterBlock = New Snap.UI.Block.Double("Sphere diameter")
        diameterBlock.Value = 10

        ' Create a button to flip sides
        flipButton = New Snap.UI.Block.Button("Flip sides")

        ' Add the three blocks to the BlockForm
        Me.AddBlocks(selectionBlock, diameterBlock, flipButton)

    End Sub

    Public Shared Sub Main()

        Dim myForm As New SphereOnFace()    ' Create a dialog
        myForm.Show()                       ' Display it

    End Sub

    Public Overrides Sub OnShow()

        selectionBlock.SetFaceFilter()

    End Sub

    Public Overrides Sub OnUpdate(changedBlock As Snap.UI.Block.General)

        If changedBlock = selectionBlock Then
            diameter = diameterBlock.Value
            Dim pickPoint = selectionBlock.PickPoint
            Dim selectedFace = selectionBlock.SelectedObjects(0)
            CreateSphere(pickPoint, selectedFace)
            selectedFace.IsHighlighted = False

        ElseIf changedBlock = flipButton Then
            flip = -flip

        End If

    End Sub

    Private Sub CreateSphere(point As Position, surface As NX.Face)

        Dim uv = surface.Parameters(point)
        Dim u = uv(0)
        Dim v = uv(1)
        Dim surfPoint = surface.Position(u, v)
        Dim surfNormal = surface.Normal(u, v)
        Dim center = surfPoint + flip * 0.5 * diameter * surfNormal
        Sphere(center, diameter)

    End Sub

End Class
