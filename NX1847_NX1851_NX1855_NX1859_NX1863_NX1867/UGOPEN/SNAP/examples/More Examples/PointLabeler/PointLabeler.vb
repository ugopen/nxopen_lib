Option Infer On 
Imports Snap, Snap.Create

Public Class PointLabeler : Inherits Snap.UI.BlockForm

   ' The various members of a PointLabeler dialog object
   Dim specifyPointBlock As UI.Block.SpecifyPoint   ' A SpecifyPoint Block to specify a point
   Dim csysChoiceBlock As UI.Block.Enumeration      ' Enumeration block to get current coordinate system
   Dim xBlock As UI.Block.Double                    ' Block to show x-coordinate of specified point
   Dim yBlock As UI.Block.Double                    ' Block to show y-coordinate of specified point
   Dim zBlock As UI.Block.Double                    ' Block to show z-coordinate of specified point   
   Dim createLabelButton As UI.Block.Button         ' Button block to create "label" (point, line, and note)
   Dim thePosition As Position                      ' The specified position

   ' Constructor to create a new PointLabeler dialog
   Public Sub New()

      Me.Title = "Point Labeler"

      ' A block to allow a point to be specified
      specifyPointBlock = New UI.Block.SpecifyPoint()
      specifyPointBlock.LabelString = "Specify Point"

      ' A toggle to choose which coordinate system to use for reporting
      csysChoiceBlock = New UI.Block.Enumeration("Coordinate System")
      csysChoiceBlock.Items = {"ACS", "WCS"}

      ' Blocks to report the coordinate values
      xBlock = New UI.Block.Double("X")   :   xBlock.ReadOnly = True
      yBlock = New UI.Block.Double("Y")   :   yBlock.ReadOnly = True
      zBlock = New UI.Block.Double("Z")   :   zBlock.ReadOnly = True

      ' Button to request creation of a label
      createLabelButton  = New UI.Block.Button("Create Label")

      ' Add all the blocks to the dialog
      Me.AddBlocks(specifyPointBlock, csysChoiceBlock, xBlock, yBlock, zBlock, createLabelButton)

   End Sub

   ' The main function
   Public Shared Sub Main()

      Dim labeler As New PointLabeler()    ' Create a dialog
      labeler.Show()                       ' Display it

   End Sub

   ' Function that gets called when user does anything in dialog
   Public Overrides Sub OnUpdate(changedBlock As UI.Block.General)

      If changedBlock = specifyPointBlock Then
         thePosition = specifyPointBlock.Position
         UpdateCoordinates()

      ElseIf changedBlock = csysChoiceBlock Then
         UpdateCoordinates()

      ElseIf changedBlock = createLabelButton Then
         CreateLabel()

      End If

   End Sub

   ' Function that gets called before the dialog is shown
   Public Overrides Sub OnShow()

      UpdateCoordinates()

   End Sub

   ' Utility function to update coordinates
   Private Sub UpdateCoordinates()

      Dim point As Position = thePosition
      If csysChoiceBlock.SelectedItem = "WCS"  Then
         point = NX.CoordinateSystem.MapAcsToWcs(thePosition)
      End If

      xBlock.Value = point.X
      yBlock.Value = point.Y
      zBlock.Value = point.Z

   End Sub

   ' Utility function to create the label
   Private Sub CreateLabel()
      
      Dim noteString = thePosition.ToString("F3")
      
      Dim offset As New Vector(10,10,5)
      Dim style As New Snap.NX.TextStyle()
      style.AlignmentPosition = NX.TextStyle.AlignmentPositions.BottomLeft
      Note(thePosition + offset, style, noteString)
      Point(thePosition)
      Line(thePosition, thePosition + 0.8*offset)

   End Sub

End Class
