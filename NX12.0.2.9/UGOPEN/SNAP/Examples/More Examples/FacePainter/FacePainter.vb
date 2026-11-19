Option Infer On
Imports Snap, Snap.Create

Public Class FacePainter : Inherits UI.BlockForm

    ' The various members of a FacePainter dialog
    Dim selectFaceBlock As UI.Block.SelectObject      ' A SelectObject Block to select faces
    Dim colorPickerBlock As UI.Block.RGBColorPicker   ' An RGBColorPicker to specify color

    ' Constructor to create a new FacePainter dialog
    Public Sub New()

        Me.Title = "Face Painter"

        selectFaceBlock = New UI.Block.SelectObject("Select faces", "Select faces")
        selectFaceBlock.AllowMultiple = True

        colorPickerBlock = New UI.Block.RGBColorPicker()
        colorPickerBlock.Label = "Choose Color"

        Me.AddBlocks(selectFaceBlock, colorPickerBlock)

    End Sub

    ' The main function
    Public Shared Sub Main()

        Dim facePainter As New FacePainter()    ' Create a new FacePainter dialog
        facePainter.Show()                      ' Display it

    End Sub

    ' Function that gets called immediately before your dialog is shown (displayed to the user).
    Public Overrides Sub OnShow()

        selectFaceBlock.SetFaceFilter()

    End Sub

    ' Function that gets called when user clicks the Apply button
    Public Overrides Sub OnApply()

        For Each face As NX.NXObject In selectFaceBlock.SelectedObjects
            face.Color = colorPickerBlock.Color
        Next

    End Sub

End Class
