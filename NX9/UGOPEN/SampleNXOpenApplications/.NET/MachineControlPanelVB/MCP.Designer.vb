' ==============================================================================
'
'             Copyright (c) 2013  UGS PLM Solutions
'               Unpublished - All rights reserved
'
' ==============================================================================
' ******************************************************************************
'  Description
'    Class that provides the Winforms UI for the Machine Control Panel example
'
'   
'
' ******************************************************************************
<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class MCP
    Inherits System.Windows.Forms.Form

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
        Me.components = New System.ComponentModel.Container()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(MCP))
        Me.IPO = New System.Windows.Forms.Label()
        Me.ToolTip = New System.Windows.Forms.ToolTip(Me.components)
        Me.NCPartReset = New System.Windows.Forms.Button()
        Me.PictureBox1 = New System.Windows.Forms.PictureBox()
        Me.SaveMachineData = New System.Windows.Forms.Button()
        Me.NCDryRun = New System.Windows.Forms.CheckBox()
        Me.NCSingleBlockMode = New System.Windows.Forms.CheckBox()
        Me.NCClearAlarm = New System.Windows.Forms.Button()
        Me.NCStart = New System.Windows.Forms.Button()
        Me.NCReset = New System.Windows.Forms.Button()
        Me.NCStop = New System.Windows.Forms.Button()
        Me.NCFastReset = New System.Windows.Forms.Button()
        Me.GroupBoxOverride = New System.Windows.Forms.GroupBox()
        Me.FeedRateOverrideMaxLabel = New System.Windows.Forms.Label()
        Me.FeedRateOverrideMinLabel = New System.Windows.Forms.Label()
        Me.FeedRateOverrideValueLabel = New System.Windows.Forms.Label()
        Me.FeedRateOverrideTrackBar = New System.Windows.Forms.TrackBar()
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.GroupBoxOverride.SuspendLayout()
        CType(Me.FeedRateOverrideTrackBar, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'IPO
        '
        Me.IPO.AutoSize = True
        Me.IPO.Location = New System.Drawing.Point(429, 25)
        Me.IPO.Name = "IPO"
        Me.IPO.Size = New System.Drawing.Size(28, 13)
        Me.IPO.TabIndex = 9
        Me.IPO.Text = "IPO:"
        '
        'NCPartReset
        '
        Me.NCPartReset.Image = CType(resources.GetObject("NCPartReset.Image"), System.Drawing.Image)
        Me.NCPartReset.Location = New System.Drawing.Point(293, 12)
        Me.NCPartReset.Name = "NCPartReset"
        Me.NCPartReset.Size = New System.Drawing.Size(38, 38)
        Me.NCPartReset.TabIndex = 15
        Me.ToolTip.SetToolTip(Me.NCPartReset, "Part Reset")
        Me.NCPartReset.UseVisualStyleBackColor = True
        '
        'PictureBox1
        '
        Me.PictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        Me.PictureBox1.Image = CType(resources.GetObject("PictureBox1.Image"), System.Drawing.Image)
        Me.PictureBox1.Location = New System.Drawing.Point(11, 19)
        Me.PictureBox1.Name = "PictureBox1"
        Me.PictureBox1.Size = New System.Drawing.Size(30, 32)
        Me.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage
        Me.PictureBox1.TabIndex = 15
        Me.PictureBox1.TabStop = False
        Me.ToolTip.SetToolTip(Me.PictureBox1, "Feed Rate Override")
        '
        'SaveMachineData
        '
        Me.SaveMachineData.BackColor = System.Drawing.SystemColors.Control
        Me.SaveMachineData.ForeColor = System.Drawing.SystemColors.ControlText
        Me.SaveMachineData.Image = CType(resources.GetObject("SaveMachineData.Image"), System.Drawing.Image)
        Me.SaveMachineData.Location = New System.Drawing.Point(386, 12)
        Me.SaveMachineData.Name = "SaveMachineData"
        Me.SaveMachineData.Size = New System.Drawing.Size(38, 38)
        Me.SaveMachineData.TabIndex = 6
        Me.ToolTip.SetToolTip(Me.SaveMachineData, "Save Machine Data")
        Me.SaveMachineData.UseVisualStyleBackColor = False
        '
        'NCDryRun
        '
        Me.NCDryRun.Appearance = System.Windows.Forms.Appearance.Button
        Me.NCDryRun.AutoSize = True
        Me.NCDryRun.Image = CType(resources.GetObject("NCDryRun.Image"), System.Drawing.Image)
        Me.NCDryRun.Location = New System.Drawing.Point(244, 12)
        Me.NCDryRun.Name = "NCDryRun"
        Me.NCDryRun.Size = New System.Drawing.Size(38, 38)
        Me.NCDryRun.TabIndex = 5
        Me.ToolTip.SetToolTip(Me.NCDryRun, "Dry Run")
        Me.NCDryRun.UseVisualStyleBackColor = True
        '
        'NCSingleBlockMode
        '
        Me.NCSingleBlockMode.Appearance = System.Windows.Forms.Appearance.Button
        Me.NCSingleBlockMode.AutoSize = True
        Me.NCSingleBlockMode.Image = CType(resources.GetObject("NCSingleBlockMode.Image"), System.Drawing.Image)
        Me.NCSingleBlockMode.Location = New System.Drawing.Point(198, 12)
        Me.NCSingleBlockMode.Name = "NCSingleBlockMode"
        Me.NCSingleBlockMode.Size = New System.Drawing.Size(38, 38)
        Me.NCSingleBlockMode.TabIndex = 4
        Me.NCSingleBlockMode.Text = "" & Global.Microsoft.VisualBasic.ChrW(13) & Global.Microsoft.VisualBasic.ChrW(10)
        Me.ToolTip.SetToolTip(Me.NCSingleBlockMode, "Single Block Mode")
        Me.NCSingleBlockMode.UseVisualStyleBackColor = True
        '
        'NCClearAlarm
        '
        Me.NCClearAlarm.Image = CType(resources.GetObject("NCClearAlarm.Image"), System.Drawing.Image)
        Me.NCClearAlarm.Location = New System.Drawing.Point(152, 12)
        Me.NCClearAlarm.Name = "NCClearAlarm"
        Me.NCClearAlarm.Size = New System.Drawing.Size(38, 38)
        Me.NCClearAlarm.TabIndex = 3
        Me.ToolTip.SetToolTip(Me.NCClearAlarm, "Clear Alarms")
        Me.NCClearAlarm.UseVisualStyleBackColor = True
        '
        'NCStart
        '
        Me.NCStart.Image = CType(resources.GetObject("NCStart.Image"), System.Drawing.Image)
        Me.NCStart.Location = New System.Drawing.Point(14, 12)
        Me.NCStart.Name = "NCStart"
        Me.NCStart.Size = New System.Drawing.Size(38, 38)
        Me.NCStart.TabIndex = 0
        Me.NCStart.Text = "" & Global.Microsoft.VisualBasic.ChrW(13) & Global.Microsoft.VisualBasic.ChrW(10)
        Me.ToolTip.SetToolTip(Me.NCStart, "Play")
        Me.NCStart.UseVisualStyleBackColor = True
        '
        'NCReset
        '
        Me.NCReset.Image = CType(resources.GetObject("NCReset.Image"), System.Drawing.Image)
        Me.NCReset.Location = New System.Drawing.Point(106, 12)
        Me.NCReset.Name = "NCReset"
        Me.NCReset.Size = New System.Drawing.Size(38, 38)
        Me.NCReset.TabIndex = 2
        Me.ToolTip.SetToolTip(Me.NCReset, "Reset NC")
        Me.NCReset.UseVisualStyleBackColor = True
        '
        'NCStop
        '
        Me.NCStop.Image = CType(resources.GetObject("NCStop.Image"), System.Drawing.Image)
        Me.NCStop.Location = New System.Drawing.Point(60, 12)
        Me.NCStop.Name = "NCStop"
        Me.NCStop.Size = New System.Drawing.Size(38, 38)
        Me.NCStop.TabIndex = 1
        Me.ToolTip.SetToolTip(Me.NCStop, "Stop")
        Me.NCStop.UseVisualStyleBackColor = True
        '
        'NCFastReset
        '
        Me.NCFastReset.Image = CType(resources.GetObject("NCFastReset.Image"), System.Drawing.Image)
        Me.NCFastReset.Location = New System.Drawing.Point(338, 12)
        Me.NCFastReset.Name = "NCFastReset"
        Me.NCFastReset.Size = New System.Drawing.Size(38, 38)
        Me.NCFastReset.TabIndex = 16
        Me.ToolTip.SetToolTip(Me.NCFastReset, "Reset Machine")
        Me.NCFastReset.UseVisualStyleBackColor = True
        '
        'GroupBoxOverride
        '
        Me.GroupBoxOverride.Controls.Add(Me.PictureBox1)
        Me.GroupBoxOverride.Controls.Add(Me.FeedRateOverrideMaxLabel)
        Me.GroupBoxOverride.Controls.Add(Me.FeedRateOverrideMinLabel)
        Me.GroupBoxOverride.Controls.Add(Me.FeedRateOverrideValueLabel)
        Me.GroupBoxOverride.Controls.Add(Me.FeedRateOverrideTrackBar)
        Me.GroupBoxOverride.Location = New System.Drawing.Point(15, 69)
        Me.GroupBoxOverride.Name = "GroupBoxOverride"
        Me.GroupBoxOverride.Size = New System.Drawing.Size(473, 121)
        Me.GroupBoxOverride.TabIndex = 14
        Me.GroupBoxOverride.TabStop = False
        Me.GroupBoxOverride.Text = "Feed Rate Override"
        '
        'FeedRateOverrideMaxLabel
        '
        Me.FeedRateOverrideMaxLabel.AutoSize = True
        Me.FeedRateOverrideMaxLabel.Location = New System.Drawing.Point(433, 90)
        Me.FeedRateOverrideMaxLabel.Name = "FeedRateOverrideMaxLabel"
        Me.FeedRateOverrideMaxLabel.Size = New System.Drawing.Size(25, 13)
        Me.FeedRateOverrideMaxLabel.TabIndex = 17
        Me.FeedRateOverrideMaxLabel.Text = "100"
        '
        'FeedRateOverrideMinLabel
        '
        Me.FeedRateOverrideMinLabel.AutoSize = True
        Me.FeedRateOverrideMinLabel.Location = New System.Drawing.Point(14, 90)
        Me.FeedRateOverrideMinLabel.Name = "FeedRateOverrideMinLabel"
        Me.FeedRateOverrideMinLabel.Size = New System.Drawing.Size(13, 13)
        Me.FeedRateOverrideMinLabel.TabIndex = 16
        Me.FeedRateOverrideMinLabel.Text = "0"
        '
        'FeedRateOverrideValueLabel
        '
        Me.FeedRateOverrideValueLabel.AutoSize = True
        Me.FeedRateOverrideValueLabel.Location = New System.Drawing.Point(43, 29)
        Me.FeedRateOverrideValueLabel.Name = "FeedRateOverrideValueLabel"
        Me.FeedRateOverrideValueLabel.Size = New System.Drawing.Size(13, 13)
        Me.FeedRateOverrideValueLabel.TabIndex = 15
        Me.FeedRateOverrideValueLabel.Text = "0"
        '
        'FeedRateOverrideTrackBar
        '
        Me.FeedRateOverrideTrackBar.Location = New System.Drawing.Point(6, 57)
        Me.FeedRateOverrideTrackBar.Name = "FeedRateOverrideTrackBar"
        Me.FeedRateOverrideTrackBar.Size = New System.Drawing.Size(452, 45)
        Me.FeedRateOverrideTrackBar.TabIndex = 7
        '
        'MCP
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(505, 204)
        Me.ControlBox = False
        Me.Controls.Add(Me.NCFastReset)
        Me.Controls.Add(Me.NCPartReset)
        Me.Controls.Add(Me.GroupBoxOverride)
        Me.Controls.Add(Me.IPO)
        Me.Controls.Add(Me.SaveMachineData)
        Me.Controls.Add(Me.NCDryRun)
        Me.Controls.Add(Me.NCSingleBlockMode)
        Me.Controls.Add(Me.NCClearAlarm)
        Me.Controls.Add(Me.NCStart)
        Me.Controls.Add(Me.NCReset)
        Me.Controls.Add(Me.NCStop)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.KeyPreview = True
        Me.Name = "MCP"
        Me.Text = "Machine Control Panel"
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.GroupBoxOverride.ResumeLayout(False)
        Me.GroupBoxOverride.PerformLayout()
        CType(Me.FeedRateOverrideTrackBar, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents SaveMachineData As System.Windows.Forms.Button
    Friend WithEvents IPO As System.Windows.Forms.Label
    Friend WithEvents NCStop As System.Windows.Forms.Button
    Friend WithEvents NCStart As System.Windows.Forms.Button
    Friend WithEvents NCReset As System.Windows.Forms.Button
    Friend WithEvents NCClearAlarm As System.Windows.Forms.Button
    Friend WithEvents NCSingleBlockMode As System.Windows.Forms.CheckBox
    Friend WithEvents NCDryRun As System.Windows.Forms.CheckBox
    Friend WithEvents ToolTip As System.Windows.Forms.ToolTip
    Friend WithEvents GroupBoxOverride As System.Windows.Forms.GroupBox
    Friend WithEvents FeedRateOverrideMaxLabel As System.Windows.Forms.Label
    Friend WithEvents FeedRateOverrideMinLabel As System.Windows.Forms.Label
    Friend WithEvents FeedRateOverrideValueLabel As System.Windows.Forms.Label
    Friend WithEvents FeedRateOverrideTrackBar As System.Windows.Forms.TrackBar
    Friend WithEvents PictureBox1 As System.Windows.Forms.PictureBox
    Friend WithEvents NCPartReset As System.Windows.Forms.Button
    Friend WithEvents NCFastReset As System.Windows.Forms.Button
End Class
