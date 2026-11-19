Imports NXOpen

Public Class NXOpenWinForm
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Guide.InfoWriteLine("Creating a sphere")
        Guide.CreateSphere(0, 0, 0, 100)
    End Sub
End Class
