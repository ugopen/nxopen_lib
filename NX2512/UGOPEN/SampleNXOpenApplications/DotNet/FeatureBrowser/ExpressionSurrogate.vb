Imports NXOpen

Public Class ExpressionSurrogate

    Private nxExpression As Expression

    Public Sub New(ByVal expr As Expression)
        Me.nxExpression = expr
    End Sub

    Public Property Name() As String
        Get
            Return Me.nxExpression.Name
        End Get
        Set(ByVal Value As String)
            Me.nxExpression.SetName(Value)
        End Set
    End Property

    Public ReadOnly Property Equation() As String
        Get
            Return Me.nxExpression.Equation
        End Get
    End Property

    Public Property RightHandSide() As String
        Get
            Return Me.nxExpression.RightHandSide
        End Get
        Set(ByVal Value As String)
            Me.nxExpression.RightHandSide = Value
        End Set
    End Property

    Public ReadOnly Property Value() As Double
        Get
            Return Me.nxExpression.Value
        End Get
    End Property

End Class
