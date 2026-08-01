Imports NXOpen
Imports NXOpen.Features

Public Class BodyFeatureSurrogate
    Inherits FeatureSurrogate

    Private nxBodyFeature As BodyFeature

    Public Sub New(ByVal featureRef As BodyFeature)
        MyBase.New(featureRef)
        Me.nxBodyFeature = featureRef
    End Sub

    Public ReadOnly Property Bodies() As Body()
        Get
            Return Me.nxBodyFeature.GetBodies()
        End Get
    End Property

    Public ReadOnly Property Faces() As Face()
        Get
            Return Me.nxBodyFeature.GetFaces()
        End Get
    End Property

    Public ReadOnly Property Edges() As Edge()
        Get
            Return Me.nxBodyFeature.GetEdges()
        End Get
    End Property
End Class
