Imports NXOpen
Imports NXOpen.Features

Public Class BodySurrogate

    Private nxBody As Body

    Public Sub New(ByVal bodyRef As Body)
        Me.nxBody = bodyRef
    End Sub

    Public ReadOnly Property Name() As String
        Get
            Return Me.nxBody.JournalIdentifier
        End Get
    End Property

    Public ReadOnly Property Features() As Feature()
        Get
            Return Me.nxBody.GetFeatures()
        End Get
    End Property

    Public ReadOnly Property Edges() As Edge()
        Get
            Return Me.nxBody.GetEdges()
        End Get
    End Property

    Public ReadOnly Property Faces() As Face()
        Get
            Return Me.nxBody.GetFaces()
        End Get
    End Property

    Public ReadOnly Property SolidDensity() As Double
        Get
            Return Me.nxBody.Density
        End Get
    End Property

End Class
