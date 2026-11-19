Option Infer On
Imports System.Collections.Generic
Imports Snap, Snap.Create

Public Class DeleteCategory : Inherits Snap.UI.BlockForm

    ' The various members of a DeleteCategory dialog object
    Dim categoryListBlock As UI.Block.ListBox            ' A ListBox block to show all categories in work part
    Dim deleteAllButton As UI.Block.Button               ' Button to delete all categories
    Dim deleteSelectedButton As UI.Block.Button          ' Button to delete selected categories

    ' Constructor to create a DeleteCategory dialog
    Public Sub New()

        Me.Title = "Delete Category"     ' Title of dialog

        ' List box to show category names for selection
        categoryListBlock = New UI.Block.ListBox()
        categoryListBlock.Height = 6
        UpdateCategoryList()

        ' Button to delete selected categories
        deleteSelectedButton = New UI.Block.Button("Delete Selected")

        ' Button to delete all categories
        deleteAllButton = New UI.Block.Button("Delete All")

        ' Add all the blocks to the dialog
        Me.AddBlocks(categoryListBlock, deleteSelectedButton, deleteAllButton)

    End Sub

    ' The main function
    Public Shared Sub Main()

        Dim deleteCategory As New DeleteCategory()     ' Create a dialog
        deleteCategory.Show()                          ' Display it

    End Sub

    ' Function that gets called when user does anything in dialog
    Public Overrides Sub OnUpdate(changedBlock As Snap.UI.Block.General)

        If changedBlock = deleteSelectedButton Then
            For Each item In categoryListBlock.SelectedItems
                Dim catName As String = categoryListBlock.ListItems(item)
                NX.Category.Delete(NX.Category.FindByName(catName))
            Next
            UpdateCategoryList()

        ElseIf changedBlock = deleteAllButton Then
            NX.Category.Delete(Globals.WorkPart.Categories)
            UpdateCategoryList()
        End If

    End Sub

    ' Update categories shown in list box
    Private Sub UpdateCategoryList()

        Dim list As New List(Of String)
        For Each cat In Globals.WorkPart.Categories
            list.Add(cat.Name)
        Next
        categoryListBlock.ListItems = list.ToArray()

    End Sub

End Class