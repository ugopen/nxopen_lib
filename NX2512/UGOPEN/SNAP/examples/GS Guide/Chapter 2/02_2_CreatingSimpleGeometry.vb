Option Explicit Off
Imports Snap, Snap.Create

Module SnapSample

   Public Sub Main()

      p1 = Point(5, 7)  ' Create a point called p1 at x=5, y=7, z=0
      p2 = Point(9, 2)  ' Create a point called p2 at x=9, y=2, z=0
      Line(p1, p2)      ' Create a line between p1 and p2

   End Sub

End Module
