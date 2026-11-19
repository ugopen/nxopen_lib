Imports NXOpen

Public Class EdgeTreeNode
    Inherits System.Windows.Forms.TreeNode

    Public Sub New(ByVal owningEdge As Edge)
        nxEdge = owningEdge
        MyBase.Text = nxEdge.ToString()
    End Sub

    Public ReadOnly Property OwningEdge() As Edge
        Get
            Return Me.nxEdge
        End Get
    End Property

    Private nxEdge As Edge

End Class
