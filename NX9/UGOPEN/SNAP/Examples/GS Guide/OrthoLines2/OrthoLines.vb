Imports Snap, Snap.Create

Partial Public Class OrthoLines
   Inherits Snap.UI.BlockDialog
   Public Shared Sub Main()

      ' Specify the filename (pathname) of the dlx file
      Dim theDlxFileName As String = "OrthoLines.dlx"
      theOrthoLines = New OrthoLines(theDlxFileName)
      theOrthoLines.Show()
      theOrthoLines.Dispose()

   End Sub

   Public Shared Function GetUnloadOption() As Integer
      'Return CType(NXOpen.Session.LibraryUnloadOption.Explicitly, Integer)      ' By using File-->Utilities-->Unload
      Return CType(NXOpen.Session.LibraryUnloadOption.Immediately, Integer)      ' Immediately after executing
      ' Return CType(NXOpen.Session.LibraryUnloadOption.AtTermination, Integer)  ' When NX is terminated
   End Function

   Public Sub InitializeCallback()
      directionBlock = Snap.UI.Block.Enumeration.GetBlock(Me.NXOpenBlockDialog, "directionBlock")
      directionBlock.Label = "Choose direction"
      directionBlock.Items = {"Horizontal", "Vertical"}
      directionBlock.PresentationStyle = UI.Block.EnumPresentationStyle.RadioBox
      directionBlock.Layout = UI.Block.Layout.Horizontal

      offsetBlock = Snap.UI.Block.Double.GetBlock(Me.NXOpenBlockDialog, "offsetBlock")
      offsetBlock.Label = "Enter offset distance"
      offsetBlock.PresentationStyle = UI.Block.NumberPresentationStyle.Spin

      thinDashedButton = Snap.UI.Block.Button.GetBlock(Me.NXOpenBlockDialog, "thinDashedButton")
      thinDashedButton.Label = "Thin dashed line"

      thickSolidButton = Snap.UI.Block.Button.GetBlock(Me.NXOpenBlockDialog, "thickSolidButton")
      thickSolidButton.Label = "Thick solid line"
   End Sub

   Public Sub DialogShownCallback()
   End Sub

   Public Function ApplyCallback() As Integer
      ApplyCallback = 0
   End Function

   Public Function UpdateCallback(block As NXOpen.BlockStyler.UIBlock) As Integer
      Dim myLine As NX.Line
      If block Is thinDashedButton.NXOpenBlock Then
         myLine = CreateLine()
         myLine.LineWidth = Globals.Width.Thin
         myLine.LineFont = Globals.Font.Dashed

      ElseIf block Is thickSolidButton.NXOpenBlock Then
         myLine = CreateLine()
         myLine.LineWidth = Globals.Width.Thick
         myLine.LineFont = Globals.Font.Solid
      End If
      UpdateCallback = 0
   End Function

   Public Function OkCallback() As Integer
      OkCallback = 0
      OkCallback = ApplyCallback()
   End Function

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
