Imports System
Imports System.IO
Imports System.Windows.Forms
Imports NXOpen

Module Test

    Sub Main
        Try
           Dim openFileDialog1 As New OpenFileDialog()
       
            openFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*"
            openFileDialog1.FilterIndex = 1
            openFileDialog1.RestoreDirectory = True
       
            If openFileDialog1.ShowDialog() = DialogResult.OK Then
                Dim session As Session = Session.GetSession()
                Dim sr As StreamReader = new StreamReader(openFileDialog1.FileName)
                Dim line As String

                Try
                    line = sr.ReadLine()
                    While Not line is Nothing
                        Dim pt As Point3d
                        Dim delim As Char () = { ","C }
                        Dim strings As String () = line.Split(delim)
                        pt.x = Double.Parse(strings(0))
                        pt.y = Double.Parse(strings(1))
                        pt.z = Double.Parse(strings(2))
                        Dim p As Point
                        p = session.Parts.Work.Points.CreatePoint(pt)
                        p.SetVisibility(SmartObject.VisibilityOption.Visible)
                        line = sr.ReadLine()
                    End While
                Finally
                    sr.Close()
                End Try
            End If
        Catch E As Exception
            MessageBox.Show(E.Message)
        End Try
    End Sub
End Module
                
