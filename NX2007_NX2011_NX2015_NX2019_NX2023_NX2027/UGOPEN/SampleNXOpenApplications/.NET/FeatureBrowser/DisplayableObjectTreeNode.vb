Imports NXOpen

Public Class DisplayableObjectTreeNode
    Inherits System.Windows.Forms.TreeNode

    Public Sub New(ByVal nxObj As DisplayableObject)
        nxObjRef = nxObj
        MyBase.Text = nxObjRef.JournalIdentifier
    End Sub

    Public ReadOnly Property ObjRef() As DisplayableObject
        Get
            Return Me.nxObjRef
        End Get
    End Property

    Private nxObjRef As DisplayableObject

End Class
