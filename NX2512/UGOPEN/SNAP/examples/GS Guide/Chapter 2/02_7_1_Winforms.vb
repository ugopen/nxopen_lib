Option Explicit Off
Imports Snap, Snap.Create, System.Drawing.Color

Module SnapSample
   Public Sub Main()

        myForm = New Snap.UI.WinForm()
        myForm.BackColor = Red
        myForm.Opacity = 0.5
        myForm.Text = "Hi there"
        myForm.ShowDialog()

    End Sub
End Module
