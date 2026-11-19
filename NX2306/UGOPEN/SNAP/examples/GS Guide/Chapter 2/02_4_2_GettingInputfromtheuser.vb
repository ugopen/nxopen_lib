Option Explicit Off
Imports Snap, Snap.Create, Snap.UI.Input

Module SnapSample

   Public Sub Main()

      p1 = Point(0, 0) : p2 = Point(6, 0) : p3 = Point(6, 6) : p4 = Point(6, 6, 6)

      spine = BezierCurve(p1, p2, p3, p4) ' Create centerline of worm shape 

      factor = GetDouble("Please enter a growth factor", "Worm Parameters", "Factor", 1.05)

      If factor > 1.2 Then factor = 1.2

      For count = 0 To 10                 ' Step along spine curve 
         t = count * 0.1   
         p = spine.Position(t)            ' Calculate point on spine curve
         r = factor ^ count               ' Calculate radius 
         Sphere(p, 2 * r)                 ' Create sphere 
      Next

   End Sub

End Module
