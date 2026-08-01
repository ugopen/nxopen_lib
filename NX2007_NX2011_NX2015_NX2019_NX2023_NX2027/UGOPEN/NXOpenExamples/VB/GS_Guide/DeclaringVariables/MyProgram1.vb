Option Infer On 
Imports NXOpen

Public Class MyProgram

    Public Shared Sub Main()
        Dim selection = NXOpen.UI.GetUI().SelectionManager

        resp1 = selection.SelectScreenPosition("Specify first point", view1, p1)    ' Get first point from user
        resp2 = selection.SelectScreenPosition("Specify second point", view2, p2)   ' Get second point
        resp3 = selection.SelectScreenPosition("Specify third point", view3, p3)    ' Get third point

        Dim u = New Vector3d(p2.X - p1.X, p2.Y - p1.Y, p2.Z - p1.Z)  ' Vector3d from p1 to p2
        Dim v = New Vector3d(p3.X - p1.X, p3.Y - p1.Y, p3.Z - p1.Z)  ' Vector3d from p1 to p3

        Dim uu = u.X * u.X + u.Y * u.Y + u.Z * u.Z
        Dim uv = u.X * v.X + u.Y * v.Y + u.Z * v.Z
        Dim vv = v.X * v.X + v.Y * v.Y + v.Z * v.Z
        det = uu * vv - uv * uv                     ' Determinant for solving linear equations
        alpha = (uu * vv - uv * vv) / (2 * det)     ' Bad code !! Should check that det is not zero
        beta = (uu * vv - uu * uv) / (2 * det)
        rx = alpha * u.X + beta * v.X
        ry = alpha * u.Y + beta * v.Y
        rz = alpha * u.Z + beta * v.Z
        'rvec = alpha * u + beta * v                 ' Radius vector
        radius = Math.Sqrt(rx * rx + ry * ry + rz * rz)  ' Radius is length (norm) of this vector

        Guide.InfoWriteLine(radius)                ' Output to listing window

    End Sub

End Class
