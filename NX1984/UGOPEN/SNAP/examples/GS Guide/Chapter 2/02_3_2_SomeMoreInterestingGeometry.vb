Option Explicit Off
Imports Snap, Snap.Create

Module SnapSample

   Public Sub Main()

      p1 = Point(0, 0) : p2 = Point(6, 0) : p3 = Point(6, 6) : p4 = Point(6, 6, 6)

      spine = BezierCurve(p1, p2, p3, p4) ' Create centerline of worm shape 

      factor = 1.1                        ' The "growth factor" for the worm shape 

      n = 50
      For index = 0 To n
         t = index * (1.0/n)
         spinePoint = spine.Position(t)
         spineTangent = spine.Tangent(t)
         power = 10*t
         radius = factor^power
         Circle(spinePoint, spineTangent, radius)
      Next

   End Sub

End Module
