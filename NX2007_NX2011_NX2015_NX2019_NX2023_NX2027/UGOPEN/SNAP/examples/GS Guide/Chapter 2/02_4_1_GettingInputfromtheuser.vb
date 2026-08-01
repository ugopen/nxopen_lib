Option Explicit Off
Imports Snap, Snap.Create

Module SnapSample

   Public Sub Main()

      p1 = Point(0, 0) : p2 = Point(6, 0) : p3 = Point(6, 6) : p4 = Point(6, 6, 6)

      spine = BezierCurve(p1, p2, p3, p4) ' Create centerline of worm shape 

      cue    = "Please enter a growth factor"
      title  = "Worm Parameters"
      label  = "Factor"
      factor = Snap.UI.Input.GetDouble(cue, title, label, 1.05)

      For count = 0 To 10                 ' Step along spine curve 
         t = count * 0.1   
         p = spine.Position(t)            ' Calculate point on spine curve
         r = factor ^ count               ' Calculate radius 
         Sphere(p, 2 * r)                 ' Create sphere 
      Next

   End Sub

End Module
