Imports NXOpen
Imports NXOpen.Features

Public Class FeatureTreeNode
    Inherits System.Windows.Forms.TreeNode

    Public Sub New(ByVal owningFeature As Feature)
        nxFeature = owningFeature
        'MyBase.Text = nxFeature.FeatureType & " (" & nxFeature.Timestamp & ")"
        MyBase.Text = nxFeature.JournalIdentifier
    End Sub

    Public ReadOnly Property OwningFeature() As Feature
        Get
            Return Me.nxFeature
        End Get
    End Property

    Public ReadOnly Property FeatureSurrogate() As FeatureSurrogate
        Get
            If (TypeOf Me.nxFeature Is BodyFeature) Then
                Return New BodyFeatureSurrogate(CType(Me.nxFeature, BodyFeature))
            Else
                Return New FeatureSurrogate(Me.nxFeature)
            End If
        End Get
    End Property

    Private nxFeature As Feature

End Class

