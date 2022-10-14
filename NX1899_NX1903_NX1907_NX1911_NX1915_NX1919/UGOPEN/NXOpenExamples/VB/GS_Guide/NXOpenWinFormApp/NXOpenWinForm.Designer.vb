<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class NXOpenWinForm
   Inherits System.Windows.Forms.Form

    Public Sub New()
        InitializeComponent()
        NXOpenUI.FormUtilities.SetApplicationIcon(Me)
        NXOpenUI.FormUtilities.ReparentForm(Me)
    End Sub

   'Form overrides dispose to clean up the component list.
   <System.Diagnostics.DebuggerNonUserCode()> _
   Protected Overrides Sub Dispose(ByVal disposing As Boolean)
      Try
         If disposing AndAlso components IsNot Nothing Then
            components.Dispose()
         End If
      Finally
         MyBase.Dispose(disposing)
      End Try
   End Sub

   'Required by the Windows Form Designer
   Private components As System.ComponentModel.IContainer

   'NOTE: The following procedure is required by the Windows Form Designer
   'It can be modified using the Windows Form Designer.  
   'Do not modify it using the code editor.
   <System.Diagnostics.DebuggerStepThrough()> _
   Private Sub InitializeComponent()
      Me.Button1 = New System.Windows.Forms.Button()
      Me.SuspendLayout()
      '
      'Button1
      '
      Me.Button1.BackColor = System.Drawing.Color.Yellow
      Me.Button1.Font = New System.Drawing.Font("Times New Roman", 18.0!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
      Me.Button1.Location = New System.Drawing.Point(40, 22)
      Me.Button1.Name = "Button1"
      Me.Button1.Size = New System.Drawing.Size(191, 85)
      Me.Button1.TabIndex = 0
      Me.Button1.Text = "Click me"
      Me.Button1.UseVisualStyleBackColor = False
      '
      'SnapWinForm
      '
      Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
      Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
      Me.ClientSize = New System.Drawing.Size(275, 142)
      Me.Controls.Add(Me.Button1)
      Me.Name = "NXOpenWinForm"
      Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent
      Me.Text = "Create Sphere"
      Me.ResumeLayout(False)

   End Sub
   Friend WithEvents Button1 As System.Windows.Forms.Button
End Class
