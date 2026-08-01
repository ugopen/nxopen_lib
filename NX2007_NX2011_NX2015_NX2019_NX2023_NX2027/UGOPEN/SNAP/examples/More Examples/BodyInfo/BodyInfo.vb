Imports Snap, Snap.Create, Snap.NX.ObjectTypes

Public Class BodyInfo : Inherits UI.BlockForm

    ' The various members of a BodyInfo dialog object
    Dim selectBodyBlock As UI.Block.SelectObject    ' Allows the user to select a body
    Dim bodyTypeBlock As UI.Block.String          ' Shows the body type
    Dim numberFacesBlock As UI.Block.Integer         ' Shows the number of faces in the selected body
    Dim numberEdgesBlock As UI.Block.Integer         ' Shows the number of edges in the selected body

    ' Constructor function to create a new BodyInfo dialog
    Public Sub New()

        Me.Title = "Body Information"     ' Title of dialog      

        ' A block to select a body
        selectBodyBlock = New UI.Block.SelectObject("Select a body", "Select a body")

        ' A block to report the body type
        bodyTypeBlock = New UI.Block.String("Selected body type is")
        bodyTypeBlock.ReadOnly = True
        bodyTypeBlock.PresentationStyle = UI.Block.StringPresentationStyle.Wide

        ' A block to report the number of faces in the selected body
        numberFacesBlock = New UI.Block.Integer("Number of faces")
        numberFacesBlock.ReadOnly = True

        ' A block to report the number of edges in the selected body
        numberEdgesBlock = New UI.Block.Integer("Number of edges")
        numberEdgesBlock.ReadOnly = True

        ' Add the four blocks to the dialog
        Me.AddBlocks(selectBodyBlock, bodyTypeBlock, numberFacesBlock, numberEdgesBlock)

    End Sub

    ' The main function
    Public Shared Sub Main()

        Dim bodyInfoDialog As New BodyInfo()     ' Create a dialog
        bodyInfoDialog.Show()                    ' Display it

    End Sub

    ' Function that gets called when user does anything in dialog
    Public Overrides Sub OnUpdate(changedBlock As Snap.UI.Block.General)

        Dim body As NX.Body = CType(selectBodyBlock.SelectedObjects(0), NX.Body)
        bodyTypeBlock.Value = body.ObjectSubType.ToString()
        numberFacesBlock.Value = body.Faces.Length
        numberEdgesBlock.Value = body.Edges.Length

        ' Unselect the body (remove it from the SelectedObjects array)
        selectBodyBlock.SelectedObjects = New NX.NXObject() {}

    End Sub

    ' Function that gets called immediately before your dialog is shown (displayed to the user).
    Public Overrides Sub OnShow()

        selectBodyBlock.SetFilter(Type.Body)

    End Sub

End Class
