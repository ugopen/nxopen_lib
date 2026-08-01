Option Infer On
Imports Snap, Snap.Create

' This is a very simple example showing you how to use a Snap.UI.BlockForm
' to create a dialog. You may add and remove blocks to suit your needs.
' Please see SNAP Getting Started Guide for an introduction 
' to the related concepts.

Public Class Spokes : Inherits UI.BlockForm

   ' Declarations of the blocks on a Spokes dialog
   Dim menuBlock    As UI.Block.Enumeration
   Dim buttonBlock  As UI.Block.Button
   Dim integerBlock As UI.Block.Integer

   ' Class level variables
   Dim chosenItem  As String  = "item2"
   Dim inputNumber As Integer = 0

   ' Constructor for a Spokes dialog object
   Public Sub New()

      Me.Title = "Spokes"
      Me.Cue = "Please enter information"

      ' Create an option menu block
      menuBlock = New UI.Block.Enumeration()
      menuBlock.Label = "Please choose option"
      menuBlock.Items = {"Balls only", "With spokes"}

      ' Create an Integer block
      integerBlock = New UI.Block.Integer("Number of spokes")

      ' Add all the blocks to the BlockForm
      Me.AddBlocks(menuBlock, integerBlock)

   End Sub


   Public Shared Sub Main()

      ' Create and display a Spokes dialog
      Dim myForm = New Spokes()
      myForm.Show()

   End Sub

   Public Overrides Sub OnApply()
      Dim n = integerBlock.Value
      Dim delta = 360.0 / n
      For i = 0 To n - 1
         Dim x = Snap.Math.CosD(i * delta)
         Dim y = Snap.Math.SinD(i * delta)
         Sphere({x, y, 0}, 0.05)
         If menuBlock.SelectedItem = "With spokes" Then
            Cylinder({0, 0, 0}, {x, y, 0}, 0.02)
         End If
      Next
   End Sub


End Class
