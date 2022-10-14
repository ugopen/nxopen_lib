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
        Me.SaveMachineData = New System.Windows.Forms.Button()
        Me.NCDryRun = New System.Windows.Forms.CheckBox()
        Me.NCSingleBlockMode = New System.Windows.Forms.CheckBox()
        Me.NCClearAlarm = New System.Windows.Forms.Button()
        Me.NCStart = New System.Windows.Forms.Button()
        Me.NCReset = New System.Windows.Forms.Button()
        Me.NCStop = New System.Windows.Forms.Button()
        Me.NCFastReset = New System.Windows.Forms.Button()
        Me.ResetMachineData = New System.Windows.Forms.Button()
        Me.BootVNCK = New System.Windows.Forms.Button()
        Me.ShutdownVNCK = New System.Windows.Forms.Button()
        Me.StatusTextBox = New System.Windows.Forms.TextBox()
        Me.StatusLabel = New System.Windows.Forms.Label()
        Me.FeedRateOverrideTitle = New System.Windows.Forms.Label()
        Me.FeedRateOverrideEdit = New System.Windows.Forms.NumericUpDown()
        Me.SkipLevel3Box = New System.Windows.Forms.CheckBox()
        Me.SkipLevel2Box = New System.Windows.Forms.CheckBox()
        Me.SkipLevel1Box = New System.Windows.Forms.CheckBox()
        Me.SkipLevel0Box = New System.Windows.Forms.CheckBox()
        Me.ConditionalStopBox = New System.Windows.Forms.CheckBox()
        Me.SkipLevelLabel = New System.Windows.Forms.Label()
        CType(Me.FeedRateOverrideEdit, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'IPO
        '
        Me.IPO.AutoSize = True
        Me.IPO.Location = New System.Drawing.Point(188, 184)
        Me.IPO.Name = "IPO"
        Me.IPO.Size = New System.Drawing.Size(28, 13)
        Me.IPO.TabIndex = 20
        Me.IPO.Text = "IPO:"
        '
        'NCPartReset
        '
        Me.NCPartReset.Image = CType(resources.GetObject("NCPartReset.Image"), System.Drawing.Image)
        Me.NCPartReset.Location = New System.Drawing.Point(56, 57)
        Me.NCPartReset.Name = "NCPartReset"
        Me.NCPartReset.Size = New System.Drawing.Size(38, 38)
        Me.NCPartReset.TabIndex = 6
        Me.ToolTip.SetToolTip(Me.NCPartReset, "Part Reset")
        Me.NCPartReset.UseVisualStyleBackColor = True
        '
        'SaveMachineData
        '
        Me.SaveMachineData.BackColor = System.Drawing.SystemColors.Control
        Me.SaveMachineData.ForeColor = System.Drawing.SystemColors.ControlText
        Me.SaveMachineData.Image = CType(resources.GetObject("SaveMachineData.Image"), System.Drawing.Image)
        Me.SaveMachineData.Location = New System.Drawing.Point(144, 57)
        Me.SaveMachineData.Name = "SaveMachineData"
        Me.SaveMachineData.Size = New System.Drawing.Size(38, 38)
        Me.SaveMachineData.TabIndex = 8
        Me.ToolTip.SetToolTip(Me.SaveMachineData, "Save Machine Data")
        Me.SaveMachineData.UseVisualStyleBackColor = False
        '
        'NCDryRun
        '
        Me.NCDryRun.Appearance = System.Windows.Forms.Appearance.Button
        Me.NCDryRun.AutoSize = True
        Me.NCDryRun.Image = CType(resources.GetObject("NCDryRun.Image"), System.Drawing.Image)
        Me.NCDryRun.Location = New System.Drawing.Point(188, 8)
        Me.NCDryRun.Name = "NCDryRun"
        Me.NCDryRun.Size = New System.Drawing.Size(38, 38)
        Me.NCDryRun.TabIndex = 4
        Me.ToolTip.SetToolTip(Me.NCDryRun, "Dry Run")
        Me.NCDryRun.UseVisualStyleBackColor = True
        '
        'NCSingleBlockMode
        '
        Me.NCSingleBlockMode.Appearance = System.Windows.Forms.Appearance.Button
        Me.NCSingleBlockMode.AutoSize = True
        Me.NCSingleBlockMode.Image = CType(resources.GetObject("NCSingleBlockMode.Image"), System.Drawing.Image)
        Me.NCSingleBlockMode.Location = New System.Drawing.Point(144, 8)
        Me.NCSingleBlockMode.Name = "NCSingleBlockMode"
        Me.NCSingleBlockMode.Size = New System.Drawing.Size(38, 38)
        Me.NCSingleBlockMode.TabIndex = 3
        Me.NCSingleBlockMode.Text = "" & Global.Microsoft.VisualBasic.ChrW(13) & Global.Microsoft.VisualBasic.ChrW(10)
        Me.ToolTip.SetToolTip(Me.NCSingleBlockMode, "Single Block Mode")
        Me.NCSingleBlockMode.UseVisualStyleBackColor = True
        '
        'NCClearAlarm
        '
        Me.NCClearAlarm.Image = CType(resources.GetObject("NCClearAlarm.Image"), System.Drawing.Image)
        Me.NCClearAlarm.Location = New System.Drawing.Point(12, 57)
        Me.NCClearAlarm.Name = "NCClearAlarm"
        Me.NCClearAlarm.Size = New System.Drawing.Size(38, 38)
        Me.NCClearAlarm.TabIndex = 5
        Me.ToolTip.SetToolTip(Me.NCClearAlarm, "Clear Alarms")
        Me.NCClearAlarm.UseVisualStyleBackColor = True
        '
        'NCStart
        '
        Me.NCStart.Image = CType(resources.GetObject("NCStart.Image"), System.Drawing.Image)
        Me.NCStart.Location = New System.Drawing.Point(12, 8)
        Me.NCStart.Name = "NCStart"
        Me.NCStart.Size = New System.Drawing.Size(38, 38)
        Me.NCStart.TabIndex = 0
        Me.NCStart.Text = "" & Global.Microsoft.VisualBasic.ChrW(13) & Global.Microsoft.VisualBasic.ChrW(10)
        Me.ToolTip.SetToolTip(Me.NCStart, "NC Start")
        Me.NCStart.UseVisualStyleBackColor = True
        '
        'NCReset
        '
        Me.NCReset.Image = CType(resources.GetObject("NCReset.Image"), System.Drawing.Image)
        Me.NCReset.Location = New System.Drawing.Point(100, 8)
        Me.NCReset.Name = "NCReset"
        Me.NCReset.Size = New System.Drawing.Size(38, 38)
        Me.NCReset.TabIndex = 2
        Me.ToolTip.SetToolTip(Me.NCReset, "NC Reset")
        Me.NCReset.UseVisualStyleBackColor = True
        '
        'NCStop
        '
        Me.NCStop.Image = CType(resources.GetObject("NCStop.Image"), System.Drawing.Image)
        Me.NCStop.Location = New System.Drawing.Point(56, 8)
        Me.NCStop.Name = "NCStop"
        Me.NCStop.Size = New System.Drawing.Size(38, 38)
        Me.NCStop.TabIndex = 1
        Me.ToolTip.SetToolTip(Me.NCStop, "NC Stop")
        Me.NCStop.UseVisualStyleBackColor = True
        '
        'NCFastReset
        '
        Me.NCFastReset.Image = CType(resources.GetObject("NCFastReset.Image"), System.Drawing.Image)
        Me.NCFastReset.Location = New System.Drawing.Point(100, 57)
        Me.NCFastReset.Name = "NCFastReset"
        Me.NCFastReset.Size = New System.Drawing.Size(38, 38)
        Me.NCFastReset.TabIndex = 7
        Me.ToolTip.SetToolTip(Me.NCFastReset, "Reset Machine")
        Me.NCFastReset.UseVisualStyleBackColor = True
        '
        'ResetMachineData
        '
        Me.ResetMachineData.BackColor = System.Drawing.SystemColors.Control
        Me.ResetMachineData.ForeColor = System.Drawing.SystemColors.ControlText
        Me.ResetMachineData.Image = CType(resources.GetObject("ResetMachineData.Image"), System.Drawing.Image)
        Me.ResetMachineData.Location = New System.Drawing.Point(188, 57)
        Me.ResetMachineData.Name = "ResetMachineData"
        Me.ResetMachineData.Size = New System.Drawing.Size(38, 38)
        Me.ResetMachineData.TabIndex = 9
        Me.ToolTip.SetToolTip(Me.ResetMachineData, "Reset Machine Data" & Global.Microsoft.VisualBasic.ChrW(13) & Global.Microsoft.VisualBasic.ChrW(10) & "Set SRAM data back to state of the machine tool and reboot VN" &
        "CK if currently running.")
        Me.ResetMachineData.UseVisualStyleBackColor = False
        '
        'BootVNCK
        '
        Me.BootVNCK.BackColor = System.Drawing.SystemColors.Control
        Me.BootVNCK.ForeColor = System.Drawing.SystemColors.ControlText
        Me.BootVNCK.Image = CType(resources.GetObject("BootVNCK.Image"), System.Drawing.Image)
        Me.BootVNCK.Location = New System.Drawing.Point(245, 8)
        Me.BootVNCK.Name = "BootVNCK"
        Me.BootVNCK.Size = New System.Drawing.Size(38, 38)
        Me.BootVNCK.TabIndex = 17
        Me.ToolTip.SetToolTip(Me.BootVNCK, "Boot VNCK")
        Me.BootVNCK.UseVisualStyleBackColor = False
        '
        'ShutdownVNCK
        '
        Me.ShutdownVNCK.BackColor = System.Drawing.SystemColors.Control
        Me.ShutdownVNCK.ForeColor = System.Drawing.SystemColors.ControlText
        Me.ShutdownVNCK.Image = CType(resources.GetObject("ShutdownVNCK.Image"), System.Drawing.Image)
        Me.ShutdownVNCK.Location = New System.Drawing.Point(245, 8)
        Me.ShutdownVNCK.Name = "ShutdownVNCK"
        Me.ShutdownVNCK.Size = New System.Drawing.Size(38, 38)
        Me.ShutdownVNCK.TabIndex = 18
        Me.ToolTip.SetToolTip(Me.ShutdownVNCK, "Shutdown VNCK")
        Me.ShutdownVNCK.UseVisualStyleBackColor = False
        '
        'StatusTextBox
        '
        Me.StatusTextBox.Location = New System.Drawing.Point(12, 204)
        Me.StatusTextBox.Name = "StatusTextBox"
        Me.StatusTextBox.ReadOnly = True
        Me.StatusTextBox.Size = New System.Drawing.Size(271, 20)
        Me.StatusTextBox.TabIndex = 19
        '
        'StatusLabel
        '
        Me.StatusLabel.AutoSize = True
        Me.StatusLabel.Location = New System.Drawing.Point(12, 184)
        Me.StatusLabel.Name = "StatusLabel"
        Me.StatusLabel.Size = New System.Drawing.Size(37, 13)
        Me.StatusLabel.TabIndex = 21
        Me.StatusLabel.Text = "Status"
        '
        'FeedRateOverrideTitle
        '
        Me.FeedRateOverrideTitle.Location = New System.Drawing.Point(12, 104)
        Me.FeedRateOverrideTitle.Name = "FeedRateOverrideTitle"
        Me.FeedRateOverrideTitle.Size = New System.Drawing.Size(82, 26)
        Me.FeedRateOverrideTitle.TabIndex = 22
        Me.FeedRateOverrideTitle.Text = "Feed Rate Override [%]"
        '
        'FeedRateOverrideEdit
        '
        Me.FeedRateOverrideEdit.Increment = New Decimal(New Integer() {10, 0, 0, 0})
        Me.FeedRateOverrideEdit.Location = New System.Drawing.Point(100, 107)
        Me.FeedRateOverrideEdit.Name = "FeedRateOverrideEdit"
        Me.FeedRateOverrideEdit.Size = New System.Drawing.Size(48, 20)
        Me.FeedRateOverrideEdit.TabIndex = 10
        Me.FeedRateOverrideEdit.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
        Me.FeedRateOverrideEdit.Value = New Decimal(New Integer() {100, 0, 0, 0})
        '
        'SkipLevel3Box
        '
        Me.SkipLevel3Box.AutoSize = True
        Me.SkipLevel3Box.Location = New System.Drawing.Point(232, 159)
        Me.SkipLevel3Box.Name = "SkipLevel3Box"
        Me.SkipLevel3Box.Size = New System.Drawing.Size(37, 17)
        Me.SkipLevel3Box.TabIndex = 16
        Me.SkipLevel3Box.Text = "/3"
        Me.SkipLevel3Box.UseVisualStyleBackColor = True
        '
        'SkipLevel2Box
        '
        Me.SkipLevel2Box.AutoSize = True
        Me.SkipLevel2Box.Location = New System.Drawing.Point(188, 159)
        Me.SkipLevel2Box.Name = "SkipLevel2Box"
        Me.SkipLevel2Box.Size = New System.Drawing.Size(37, 17)
        Me.SkipLevel2Box.TabIndex = 15
        Me.SkipLevel2Box.Text = "/2"
        Me.SkipLevel2Box.UseVisualStyleBackColor = True
        '
        'SkipLevel1Box
        '
        Me.SkipLevel1Box.AutoSize = True
        Me.SkipLevel1Box.Location = New System.Drawing.Point(144, 159)
        Me.SkipLevel1Box.Name = "SkipLevel1Box"
        Me.SkipLevel1Box.Size = New System.Drawing.Size(37, 17)
        Me.SkipLevel1Box.TabIndex = 14
        Me.SkipLevel1Box.Text = "/1"
        Me.SkipLevel1Box.UseVisualStyleBackColor = True
        '
        'SkipLevel0Box
        '
        Me.SkipLevel0Box.AutoSize = True
        Me.SkipLevel0Box.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        Me.SkipLevel0Box.Location = New System.Drawing.Point(100, 159)
        Me.SkipLevel0Box.Name = "SkipLevel0Box"
        Me.SkipLevel0Box.Size = New System.Drawing.Size(31, 17)
        Me.SkipLevel0Box.TabIndex = 13
        Me.SkipLevel0Box.Text = "/"
        Me.SkipLevel0Box.UseVisualStyleBackColor = True
        '
        'ConditionalStopBox
        '
        Me.ConditionalStopBox.CheckAlign = System.Drawing.ContentAlignment.MiddleRight
        Me.ConditionalStopBox.Location = New System.Drawing.Point(12, 134)
        Me.ConditionalStopBox.Name = "ConditionalStopBox"
        Me.ConditionalStopBox.Size = New System.Drawing.Size(102, 19)
        Me.ConditionalStopBox.TabIndex = 11
        Me.ConditionalStopBox.Text = "Stop on M1"
        Me.ConditionalStopBox.UseVisualStyleBackColor = True
        '
        'SkipLevelLabel
        '
        Me.SkipLevelLabel.AutoSize = True
        Me.SkipLevelLabel.Location = New System.Drawing.Point(13, 159)
        Me.SkipLevelLabel.Name = "SkipLevelLabel"
        Me.SkipLevelLabel.Size = New System.Drawing.Size(62, 13)
        Me.SkipLevelLabel.TabIndex = 21
        Me.SkipLevelLabel.Text = "Skip Levels"
        '
        'MCP
        '
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None
        Me.ClientSize = New System.Drawing.Size(294, 236)
        Me.ControlBox = False
        Me.Controls.Add(Me.SkipLevel3Box)
        Me.Controls.Add(Me.SkipLevel2Box)
        Me.Controls.Add(Me.SkipLevel1Box)
        Me.Controls.Add(Me.SkipLevel0Box)
        Me.Controls.Add(Me.ConditionalStopBox)
        Me.Controls.Add(Me.FeedRateOverrideEdit)
        Me.Controls.Add(Me.FeedRateOverrideTitle)
        Me.Controls.Add(Me.ResetMachineData)
        Me.Controls.Add(Me.SkipLevelLabel)
        Me.Controls.Add(Me.StatusLabel)
        Me.Controls.Add(Me.StatusTextBox)
        Me.Controls.Add(Me.NCFastReset)
        Me.Controls.Add(Me.NCPartReset)
        Me.Controls.Add(Me.IPO)
        Me.Controls.Add(Me.SaveMachineData)
        Me.Controls.Add(Me.NCDryRun)
        Me.Controls.Add(Me.NCSingleBlockMode)
        Me.Controls.Add(Me.NCClearAlarm)
        Me.Controls.Add(Me.NCStart)
        Me.Controls.Add(Me.NCReset)
        Me.Controls.Add(Me.NCStop)
        Me.Controls.Add(Me.BootVNCK)
        Me.Controls.Add(Me.ShutdownVNCK)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow
        Me.KeyPreview = True
        Me.Location = New System.Drawing.Point(0, 520)
        Me.Name = "MCP"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.Manual
        Me.Text = "Machine Control Panel"
        CType(Me.FeedRateOverrideEdit, System.ComponentModel.ISupportInitialize).EndInit()
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
    Friend WithEvents NCPartReset As System.Windows.Forms.Button
    Friend WithEvents NCFastReset As System.Windows.Forms.Button
    Friend WithEvents BootVNCK As System.Windows.Forms.Button
    Friend WithEvents ShutdownVNCK As System.Windows.Forms.Button
    Private WithEvents StatusTextBox As System.Windows.Forms.TextBox
    Private WithEvents StatusLabel As System.Windows.Forms.Label
    Friend WithEvents ResetMachineData As System.Windows.Forms.Button
    Private WithEvents FeedRateOverrideTitle As Windows.Forms.Label
    Private WithEvents FeedRateOverrideEdit As Windows.Forms.NumericUpDown
    Private WithEvents SkipLevel3Box As Windows.Forms.CheckBox
    Private WithEvents SkipLevel2Box As Windows.Forms.CheckBox
    Private WithEvents SkipLevel1Box As Windows.Forms.CheckBox
    Private WithEvents SkipLevel0Box As Windows.Forms.CheckBox
    Private WithEvents ConditionalStopBox As Windows.Forms.CheckBox
    Private WithEvents SkipLevelLabel As Windows.Forms.Label
End Class
