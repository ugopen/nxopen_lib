Imports NXOpen

Public Class FaceTreeNode
    Inherits System.Windows.Forms.TreeNode

    Public Sub New(ByVal owningFace As Face)
        nxFace = owningFace
        MyBase.Text = nxFace.ToString()
    End Sub

    Public ReadOnly Property OwningFace() As Face
        Get
            Return Me.nxFace
        End Get
    End Property

    Private nxFace As Face

End Class
