Option Explicit Off 
Imports Snap, Snap.Create

Public Class MyProgram

    Public Shared Sub Main()

      p1 = Snap.UI.Input.GetPosition("Specify first point")    ' Get first point from user
      p2 = Snap.UI.Input.GetPosition("Specify second point")   ' Get second point
      p3 = Snap.UI.Input.GetPosition("Specify third point")    ' Get third point

      u = p2.Position - p1.Position         ' Vector from p1 to p2
      v = p3.Position - p1.Position         ' Vector from p1 to p3
      uu = u * u                            ' Dot product of vectors
      uv = u * v
      vv = v * v
      det = uu * vv - uv * uv                     ' Determinant for solving linear equations
      alpha = (uu * vv - uv * vv) / (2 * det)     ' Bad code !! Should check that det is not zero
      beta  = (uu * vv - uu * uv) / (2 * det)
      rvec = alpha * u + beta * v                 ' Radius vector
      radius = Vector.Norm(rvec)                  ' Radius is length (norm) of this vector

      InfoWindow.WriteLine(radius)                ' Output to listing window

    End Sub

End Class
