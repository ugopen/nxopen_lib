Imports Snap, Snap.Create

Public Class SnapWinForm

Private Sub Button1_Click( ByVal sender As System.Object,  ByVal e As System.EventArgs) Handles Button1.Click
      InfoWindow.WriteLine("Creating a sphere") 
      Sphere(0, 0, 0, 10)
End Sub
End Class