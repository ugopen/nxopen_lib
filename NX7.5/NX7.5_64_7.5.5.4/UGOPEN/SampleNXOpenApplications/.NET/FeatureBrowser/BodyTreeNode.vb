Imports NXOpen

Public Class BodyTreeNode
    Inherits System.Windows.Forms.TreeNode

    Public Sub New(ByVal owningBody As Body)
        nxBody = owningBody
        If (nxBody.IsSheetBody) Then
            MyBase.Text = "Sheet Body (" + nxBody.JournalIdentifier + ")"
        Else
            MyBase.Text = "Solid Body (" + nxBody.JournalIdentifier + ")"
        End If
    End Sub

    Public ReadOnly Property OwningBody() As Body
        Get
            Return Me.nxBody
        End Get
    End Property

    Private nxBody As Body

    Private Sub PopulateFaces()
        Try
            If (Not (Me.nxBody) Is Nothing) Then
                Dim faceList As System.Windows.Forms.TreeNode = _
                    New System.Windows.Forms.TreeNode("Faces")
                Dim faceNode As FaceTreeNode
                For Each myFace As Face In Me.OwningBody.GetFaces()
                    If (Not myFace Is Nothing) Then
                        faceNode = New FaceTreeNode(myFace)
                        faceList.Nodes.Add(faceNode)
                    End If
                Next myFace
                Me.Nodes.Add(faceList)
            End If
        Catch ex As System.Exception
            MessageBox.Show("PopulateFaces Exception: " & ex.Message)
        End Try
    End Sub

    Private Sub PopulateEdges()
        Try
            If (Not (Me.nxBody) Is Nothing) Then
                Dim edgeList As System.Windows.Forms.TreeNode = _
                    New System.Windows.Forms.TreeNode("Edges")
                Dim edgeNode As EdgeTreeNode
                For Each myEdge As Edge In Me.OwningBody.GetEdges()
                    If (Not myEdge Is Nothing) Then
                        edgeNode = New EdgeTreeNode(myEdge)
                        edgeList.Nodes.Add(edgeNode)
                    End If
                Next myEdge
                Me.Nodes.Add(edgeList)
            End If
        Catch ex As System.Exception
            MessageBox.Show("PopulateEdges Exception: " & ex.Message)
        End Try
    End Sub

    Public Sub Update()
        MyBase.Nodes.Clear()
        Me.PopulateFaces()
        Me.PopulateEdges()
    End Sub

End Class
