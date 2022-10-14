Option Infer On
Imports Snap, Snap.Create

' This is a very simple example showing you how to use a Snap.UI.BlockForm
' to create a dialog. You may add and remove blocks to suit your needs.
' Please see SNAP Getting Started Guide for an introduction 
' to the related concepts.

Public Class BlockFormExample : Inherits Snap.UI.BlockForm

   ' Declarations of the blocks on a BlockFormExample dialog
   Dim menuBlock    As UI.Block.Enumeration
   Dim buttonBlock  As UI.Block.Button
   Dim integerBlock As UI.Block.Integer

   ' Constructor for a BlockFormExample dialog object
   Public Sub New()

      Me.Title = "BlockFormExample"           ' Text to be shown in title bar of dialog
      Me.Cue   = "Please enter information"   ' Text to be shown in cue line

      ' Create an Enumeration block (for example)
      menuBlock = New UI.Block.Enumeration()
      menuBlock.Label = "Please choose an item"
      menuBlock.Items = {"item1", "item2", "item3"}

      ' Create an Integer block (for example)
      integerBlock = New UI.Block.Integer("Enter number")

      ' Create a Button block (for example)
      buttonBlock = New UI.Block.Button("Click me")

      ' Create addition blocks here, as you wish, and delete
      ' any of the ones above, if you don¡¯t need them.

      ' Add all the blocks to the BlockForm
      Me.AddBlocks(menuBlock, integerBlock, buttonBlock)

   End Sub

   Public Shared Sub Main()

      ' Create and display a BlockFormExample dialog
      Dim myForm = New BlockFormExample()
      myForm.Show()

   End Sub

   Public Overrides Sub OnShow()
      ' Code for when dialog is displayed
   End Sub

   Public Overrides Sub OnOK()
      ' Code for when user clicks OK
   End Sub

   Public Overrides Sub OnApply()
      ' Code for when user clicks Apply
   End Sub

   Public Overrides Sub OnCancel()
      ' Code for when user clicks Cancel
   End Sub

   Public Overrides Sub OnUpdate(changedBlock As UI.Block.General)

      If changedBlock = menuBlock Then
         ' Code for when user chooses from the menu, for example ...
         InfoWindow.WriteLine("You chose " & menuBlock.SelectedItem)
      ElseIf changedBlock = integerBlock Then
         ' Code for when user enters a number, for example ...
         InfoWindow.WriteLine("You entered " & integerBlock.Value.ToString())
      ElseIf changedBlock = buttonBlock Then
         ' Code for when user clicks the button, for example ...
         InfoWindow.WriteLine("You clicked the button")
      End If

   End Sub

End Class