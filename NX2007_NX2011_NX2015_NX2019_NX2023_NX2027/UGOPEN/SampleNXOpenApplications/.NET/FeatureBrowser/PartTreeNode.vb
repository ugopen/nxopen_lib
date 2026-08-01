Imports NXOpen
Imports NXOpen.Features

Public Class PartTreeNode
    Inherits System.Windows.Forms.TreeNode

    Private featureList As System.Windows.Forms.TreeNode

    Private bodyList As System.Windows.Forms.TreeNode

    Public Sub New(ByVal owningPart As Part)
        Me.nxPart = owningPart
        MyBase.Tag = Me.nxPart
    End Sub

    Private Sub PopulateFeatures()
        Try
            Dim features As FeatureCollection
            Dim featureNode As FeatureTreeNode
            If (Not (Me.nxPart) Is Nothing) Then
                features = Me.nxPart.Features
                featureList = New System.Windows.Forms.TreeNode("Features")
                For Each myFeature As Feature In features
                    featureNode = New FeatureTreeNode(myFeature)
                    featureList.Nodes.Add(featureNode)
                Next myFeature
                If (featureList.Nodes.Count > 0) Then
                    Me.Nodes.Add(featureList)
                Else
                    featureList = Nothing
                End If
            End If
        Catch ex As System.Exception
            MessageBox.Show("PopulateNode Exception: " & ex.Message)
        End Try
    End Sub

    Private Sub PopulateBodies()
        Try
            Dim bodies As BodyCollection
            Dim bodyNode As BodyTreeNode
            If (Not (Me.nxPart) Is Nothing) Then
                bodies = Me.nxPart.Bodies
                bodyList = New System.Windows.Forms.TreeNode("Bodies")
                For Each myBody As Body In bodies
                    bodyNode = New BodyTreeNode(myBody)
                    bodyNode.Update()
                    bodyList.Nodes.Add(bodyNode)
                Next myBody
                If (bodyList.Nodes.Count > 0) Then
                    Me.Nodes.Add(bodyList)
                Else
                    bodyList = Nothing
                End If
            End If
        Catch ex As System.Exception
            MessageBox.Show("PopulateNode Exception: " & ex.Message)
        End Try
    End Sub

    Public Sub Update()
        MyBase.Nodes.Clear()
        Me.PopulateFeatures()
        Me.PopulateBodies()
    End Sub

    Public ReadOnly Property OwningPart() As Part
        Get
            Return Me.nxPart
        End Get
    End Property

    Private nxPart As Part
End Class
