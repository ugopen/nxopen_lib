Option Infer On
Imports Snap, Snap.Create

' This is a very simple example showing you how to use a Snap.UI.BlockForm
' to create a dialog. You may add and remove blocks to suit your needs.
' Please see SNAP Getting Started Guide for an introduction 
' to the related concepts.

Public Class OrthoLines : Inherits UI.BlockForm

   ' Declarations of the blocks on a OrthoLines dialog
   Dim directionBlock   As UI.Block.Enumeration
   Dim offsetBlock      As UI.Block.Double
   Dim thinDashedButton As UI.Block.Button
   Dim thickSolidButton As UI.Block.Button

   ' Constructor for a OrthoLines dialog object
   Public Sub New()

      Me.Title = "Orthogonal Lines"    ' Text to be shown in title bar of dialog
      Me.Cue   = "Whatever"            ' Text to be shown in the cue line

      ' Create the direction choice block
      directionBlock = New HorizVertChoice()

      ' Create the offset distance block 
      offsetBlock = New UI.Block.Double("Enter offset distance")
      offsetBlock.PresentationStyle = UI.Block.NumberPresentationStyle.Spin

      ' Create the two buttons
      thinDashedButton = New UI.Block.Button("Thin dashed line")
      thickSolidButton = New UI.Block.Button("Thick solid line")

      ' Add the blocks to the BlockForm
      Me.AddBlocks(directionBlock, offsetBlock, thinDashedButton, thickSolidButton)

   End Sub

   Public Shared Sub Main()

      ' Create and display a OrthoLines dialog
      Dim myForm = New OrthoLines()
      myForm.Show()

   End Sub

   Public Overrides Sub OnUpdate(changedBlock As UI.Block.General)
      Dim myLine As NX.Line

      If changedBlock = thinDashedButton Then
         myLine = CreateLine()
         myLine.LineWidth = Globals.Width.Thin
         myLine.LineFont  = Globals.Font.Dashed
      End If

      If changedBlock = thickSolidButton Then
         myLine = CreateLine()
         myLine.LineWidth = Globals.Width.Thick
         myLine.LineFont  = Globals.Font.Solid
      End If
   End Sub

   Private Function CreateLine() As NX.Line
      Dim infinity As Double = 5000
      Dim d As Double = offsetBlock.Value
      If directionBlock.SelectedItem = "Horizontal" Then
         Return Line(-infinity, d, infinity, d)      ' Horizontal line
      Else
         Return Line(d, -infinity, d, infinity)      ' Vertical line
      End If
   End Function

End Class

Public Class HorizVertChoice  :  Inherits Snap.UI.Block.Enumeration
    Public Sub New()
        Me.Label = "Choose direction"
        Me.Items = {"Horizontal", "Vertical"}
        Me.PresentationStyle = UI.Block.EnumPresentationStyle.RadioBox
        Me.Layout = UI.Block.Layout.Horizontal
    End Sub
End Class