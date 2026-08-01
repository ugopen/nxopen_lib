Option Explicit Off
Imports Snap, Snap.Create
Imports System, System.Windows.Forms, System.Drawing.Color

Module SnapSample

   Dim WithEvents myButton As Button        'A button for our form
   Dim rand As Random                       'A .NET random number generator

   Public Sub Main()
      rand = New Random()
      myForm = New Snap.UI.WinForm()
      myForm.Text = "Create Random Spheres"
      myButton = New Button()                   'Create a button
      myButton.BackColor = Yellow               'Color it yellow
      myButton.Text = "Click me"                'Put some text on it
      myForm.Controls.Add(myButton)             'Add it to our form
      myForm.ShowDialog()                       'Display our form
   End Sub

   Sub Handler(ByVal sender As Object, ByVal e As EventArgs) Handles myButton.Click
      x = rand.NextDouble()            'Get a random x-coordinate
      y = rand.NextDouble()            'Get a random y-coordinate
      Sphere(x, y, 0, 0.2)             'Create a sphere at (x,y,0) with diameter 0.2
   End Sub

End Module
