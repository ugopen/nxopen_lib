Imports NXOpen
Imports NXOpen.Features

Public Class FeatureSurrogate

    Private nxFeature As Feature

    Public Sub New(ByVal featureRef As Feature)
        Me.nxFeature = featureRef
    End Sub

    Public ReadOnly Property Name() As String
        Get
            Return Me.nxFeature.JournalIdentifier
        End Get
    End Property

    Public ReadOnly Property FeatureType() As String
        Get
            Return Me.nxFeature.FeatureType
        End Get
    End Property

    Public ReadOnly Property Parents() As Feature()
        Get
            Return Me.nxFeature.GetParents()
        End Get
    End Property

    Public ReadOnly Property Children() As Feature()
        Get
            Return Me.nxFeature.GetChildren()
        End Get
    End Property

    Public ReadOnly Property Expressions() As Expression()
        Get
            Return Me.nxFeature.GetExpressions()
        End Get
    End Property

    Public ReadOnly Property Suppressed() As Boolean
        Get
            Return Me.nxFeature.Suppressed
        End Get
    End Property

    Public ReadOnly Property Timestamp() As Integer
        Get
            Return Me.nxFeature.Timestamp
        End Get
    End Property

End Class
