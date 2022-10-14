Option Explicit Off
Imports Snap, Snap.Create

Module SnapSample

   Public Sub Main()

      myCurve = BezierCurve(Point(0, 0), Point(1, 0), Point(1, 1))
      p1 = myCurve.Position(0.5 - 0.0001)          ' A tiny bit before the mid-point
      p2 = myCurve.Position(0.5)                   ' At the mid-point
      p3 = myCurve.Position(0.5 + 0.0001)          ' A tiny bit after the mid-point 

      u = p2 - p1       ' Vector from p1 to p2
      v = p3 - p1       ' Vector from p1 to p3
      uu = u * u        ' Dot product of u with itself
      uv = u * v
      vv = v * v
      det = uu * vv - uv * uv                      ' Determinant for solving linear equations 
      alpha = (uu * vv - uv * vv) / (2 * det)      ' Bad -- should check first that det is not zero !
      beta = (uu * vv - uu * uv) / (2 * det)
      rvec = alpha * u + beta * v                  ' Radius vector 
      radius = Vector.Norm(rvec)                   ' Radius is length (norm) of this vector 

      InfoWindow.WriteLine(radius)                 ' Output the radius to the Info window

   End Sub

End Module
