/*
 ==============================================================================

             Copyright (c) 2013  UGS PLM Solutions
               Unpublished - All rights reserved

 ==============================================================================
 ******************************************************************************
  Description
    Class that provides the Winforms UI for the Machine Control Panel example

 */
namespace MCP_CSharp
{
    partial class MCP
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MCP));
            this.IPO = new System.Windows.Forms.Label();
            this.SaveMachineData = new System.Windows.Forms.Button();
            this.NCDryRun = new System.Windows.Forms.CheckBox();
            this.NCSingleBlockMode = new System.Windows.Forms.CheckBox();
            this.NCReset = new System.Windows.Forms.Button();
            this.NCClearAlarm = new System.Windows.Forms.Button();
            this.NCStart = new System.Windows.Forms.Button();
            this.ToolTip = new System.Windows.Forms.ToolTip(this.components);
            this.NCStop = new System.Windows.Forms.Button();
            this.NCPartReset = new System.Windows.Forms.Button();
            this.NCFastReset = new System.Windows.Forms.Button();
            this.ResetMachineData = new System.Windows.Forms.Button();
            this.BootVNCK = new System.Windows.Forms.Button();
            this.ShutdownVNCK = new System.Windows.Forms.Button();
            this.StatusTextBox = new System.Windows.Forms.TextBox();
            this.StatusLabel = new System.Windows.Forms.Label();
            this.FeedRateOverrideEdit = new System.Windows.Forms.NumericUpDown();
            this.FeedRateOverrideTitle = new System.Windows.Forms.Label();
            this.ConditionalStopBox = new System.Windows.Forms.CheckBox();
            this.SkipLevel0Box = new System.Windows.Forms.CheckBox();
            this.SkipLevel1Box = new System.Windows.Forms.CheckBox();
            this.SkipLevel2Box = new System.Windows.Forms.CheckBox();
            this.SkipLevel3Box = new System.Windows.Forms.CheckBox();
            this.SkipLevelLabel = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.FeedRateOverrideEdit)).BeginInit();
            this.SuspendLayout();
            // 
            // IPO
            // 
            this.IPO.AutoSize = true;
            this.IPO.Location = new System.Drawing.Point(188, 184);
            this.IPO.Margin = new System.Windows.Forms.Padding(3, 0, 36, 0);
            this.IPO.Name = "IPO";
            this.IPO.Size = new System.Drawing.Size(28, 13);
            this.IPO.TabIndex = 31;
            this.IPO.Text = "IPO:";
            // 
            // SaveMachineData
            // 
            this.SaveMachineData.BackColor = System.Drawing.SystemColors.Control;
            this.SaveMachineData.ForeColor = System.Drawing.SystemColors.ControlText;
            this.SaveMachineData.Image = ((System.Drawing.Image)(resources.GetObject("SaveMachineData.Image")));
            this.SaveMachineData.Location = new System.Drawing.Point(144, 57);
            this.SaveMachineData.Name = "SaveMachineData";
            this.SaveMachineData.Size = new System.Drawing.Size(38, 38);
            this.SaveMachineData.TabIndex = 8;
            this.ToolTip.SetToolTip(this.SaveMachineData, "Save Machine Data");
            this.SaveMachineData.UseVisualStyleBackColor = false;
            this.SaveMachineData.Click += new System.EventHandler(this.SaveMachineData_Click);
            // 
            // NCDryRun
            // 
            this.NCDryRun.Appearance = System.Windows.Forms.Appearance.Button;
            this.NCDryRun.AutoSize = true;
            this.NCDryRun.Image = ((System.Drawing.Image)(resources.GetObject("NCDryRun.Image")));
            this.NCDryRun.Location = new System.Drawing.Point(188, 8);
            this.NCDryRun.Name = "NCDryRun";
            this.NCDryRun.Size = new System.Drawing.Size(38, 38);
            this.NCDryRun.TabIndex = 4;
            this.ToolTip.SetToolTip(this.NCDryRun, "Dry Run");
            this.NCDryRun.UseVisualStyleBackColor = true;
            this.NCDryRun.CheckedChanged += new System.EventHandler(this.NCDryRun_CheckedChanged);
            // 
            // NCSingleBlockMode
            // 
            this.NCSingleBlockMode.Appearance = System.Windows.Forms.Appearance.Button;
            this.NCSingleBlockMode.AutoSize = true;
            this.NCSingleBlockMode.Image = ((System.Drawing.Image)(resources.GetObject("NCSingleBlockMode.Image")));
            this.NCSingleBlockMode.Location = new System.Drawing.Point(144, 8);
            this.NCSingleBlockMode.Name = "NCSingleBlockMode";
            this.NCSingleBlockMode.Size = new System.Drawing.Size(38, 38);
            this.NCSingleBlockMode.TabIndex = 3;
            this.NCSingleBlockMode.Text = "\r\n";
            this.ToolTip.SetToolTip(this.NCSingleBlockMode, "Single Block Mode");
            this.NCSingleBlockMode.UseVisualStyleBackColor = true;
            this.NCSingleBlockMode.CheckedChanged += new System.EventHandler(this.NCSingleBlockMode_CheckedChanged);
            // 
            // NCReset
            // 
            this.NCReset.Image = ((System.Drawing.Image)(resources.GetObject("NCReset.Image")));
            this.NCReset.Location = new System.Drawing.Point(100, 8);
            this.NCReset.Name = "NCReset";
            this.NCReset.Size = new System.Drawing.Size(38, 38);
            this.NCReset.TabIndex = 2;
            this.ToolTip.SetToolTip(this.NCReset, "NC Reset");
            this.NCReset.UseVisualStyleBackColor = true;
            this.NCReset.Click += new System.EventHandler(this.NCReset_Click);
            // 
            // NCClearAlarm
            // 
            this.NCClearAlarm.Image = ((System.Drawing.Image)(resources.GetObject("NCClearAlarm.Image")));
            this.NCClearAlarm.Location = new System.Drawing.Point(12, 57);
            this.NCClearAlarm.Name = "NCClearAlarm";
            this.NCClearAlarm.Size = new System.Drawing.Size(38, 38);
            this.NCClearAlarm.TabIndex = 5;
            this.ToolTip.SetToolTip(this.NCClearAlarm, "Clear Alarms");
            this.NCClearAlarm.UseVisualStyleBackColor = true;
            this.NCClearAlarm.Click += new System.EventHandler(this.NCClearAlarm_Click);
            // 
            // NCStart
            // 
            this.NCStart.Image = ((System.Drawing.Image)(resources.GetObject("NCStart.Image")));
            this.NCStart.Location = new System.Drawing.Point(12, 8);
            this.NCStart.Name = "NCStart";
            this.NCStart.Size = new System.Drawing.Size(38, 38);
            this.NCStart.TabIndex = 0;
            this.NCStart.Text = "\r\n";
            this.ToolTip.SetToolTip(this.NCStart, "NC Start");
            this.NCStart.UseVisualStyleBackColor = true;
            this.NCStart.Click += new System.EventHandler(this.NCStart_Click);
            // 
            // NCStop
            // 
            this.NCStop.Image = ((System.Drawing.Image)(resources.GetObject("NCStop.Image")));
            this.NCStop.Location = new System.Drawing.Point(56, 8);
            this.NCStop.Name = "NCStop";
            this.NCStop.Size = new System.Drawing.Size(38, 38);
            this.NCStop.TabIndex = 1;
            this.ToolTip.SetToolTip(this.NCStop, "NC Stop");
            this.NCStop.UseVisualStyleBackColor = true;
            this.NCStop.Click += new System.EventHandler(this.NCStop_Click);
            // 
            // NCPartReset
            // 
            this.NCPartReset.Image = ((System.Drawing.Image)(resources.GetObject("NCPartReset.Image")));
            this.NCPartReset.Location = new System.Drawing.Point(56, 57);
            this.NCPartReset.Name = "NCPartReset";
            this.NCPartReset.Size = new System.Drawing.Size(38, 38);
            this.NCPartReset.TabIndex = 6;
            this.ToolTip.SetToolTip(this.NCPartReset, "Part Reset");
            this.NCPartReset.UseVisualStyleBackColor = true;
            this.NCPartReset.Click += new System.EventHandler(this.NCPartReset_Click);
            // 
            // NCFastReset
            // 
            this.NCFastReset.Image = ((System.Drawing.Image)(resources.GetObject("NCFastReset.Image")));
            this.NCFastReset.Location = new System.Drawing.Point(100, 57);
            this.NCFastReset.Name = "NCFastReset";
            this.NCFastReset.Size = new System.Drawing.Size(38, 38);
            this.NCFastReset.TabIndex = 7;
            this.ToolTip.SetToolTip(this.NCFastReset, "Reset Machine");
            this.NCFastReset.UseVisualStyleBackColor = true;
            this.NCFastReset.Click += new System.EventHandler(this.NCFastReset_Click);
            // 
            // ResetMachineData
            // 
            this.ResetMachineData.BackColor = System.Drawing.SystemColors.Control;
            this.ResetMachineData.ForeColor = System.Drawing.SystemColors.ControlText;
            this.ResetMachineData.Image = ((System.Drawing.Image)(resources.GetObject("ResetMachineData.Image")));
            this.ResetMachineData.Location = new System.Drawing.Point(188, 57);
            this.ResetMachineData.Name = "ResetMachineData";
            this.ResetMachineData.Size = new System.Drawing.Size(38, 38);
            this.ResetMachineData.TabIndex = 9;
            this.ToolTip.SetToolTip(this.ResetMachineData, "Reset Machine Data\r\nSet SRAM data back to state of the machine tool and reboot VN" +
        "CK if currently running.");
            this.ResetMachineData.UseVisualStyleBackColor = false;
            this.ResetMachineData.Click += new System.EventHandler(this.ResetMachineData_Click);
            // 
            // BootVNCK
            // 
            this.BootVNCK.BackColor = System.Drawing.SystemColors.Control;
            this.BootVNCK.ForeColor = System.Drawing.SystemColors.ControlText;
            this.BootVNCK.Image = ((System.Drawing.Image)(resources.GetObject("BootVNCK.Image")));
            this.BootVNCK.Location = new System.Drawing.Point(245, 8);
            this.BootVNCK.Name = "BootVNCK";
            this.BootVNCK.Size = new System.Drawing.Size(38, 38);
            this.BootVNCK.TabIndex = 17;
            this.ToolTip.SetToolTip(this.BootVNCK, "Boot VNCK");
            this.BootVNCK.UseVisualStyleBackColor = false;
            this.BootVNCK.Click += new System.EventHandler(this.BootVNCK_Click);
            // 
            // ShutdownVNCK
            // 
            this.ShutdownVNCK.BackColor = System.Drawing.SystemColors.Control;
            this.ShutdownVNCK.ForeColor = System.Drawing.SystemColors.ControlText;
            this.ShutdownVNCK.Image = ((System.Drawing.Image)(resources.GetObject("ShutdownVNCK.Image")));
            this.ShutdownVNCK.Location = new System.Drawing.Point(245, 8);
            this.ShutdownVNCK.Name = "ShutdownVNCK";
            this.ShutdownVNCK.Size = new System.Drawing.Size(38, 38);
            this.ShutdownVNCK.TabIndex = 18;
            this.ToolTip.SetToolTip(this.ShutdownVNCK, "Shutdown VNCK");
            this.ShutdownVNCK.UseVisualStyleBackColor = false;
            this.ShutdownVNCK.Visible = false;
            this.ShutdownVNCK.Click += new System.EventHandler(this.ShutdownVNCK_Click);
            // 
            // StatusTextBox
            // 
            this.StatusTextBox.Location = new System.Drawing.Point(12, 204);
            this.StatusTextBox.Name = "StatusTextBox";
            this.StatusTextBox.ReadOnly = true;
            this.StatusTextBox.Size = new System.Drawing.Size(271, 20);
            this.StatusTextBox.TabIndex = 19;
            // 
            // StatusLabel
            // 
            this.StatusLabel.AutoSize = true;
            this.StatusLabel.Location = new System.Drawing.Point(12, 184);
            this.StatusLabel.Name = "StatusLabel";
            this.StatusLabel.Size = new System.Drawing.Size(37, 13);
            this.StatusLabel.TabIndex = 21;
            this.StatusLabel.Text = "Status";
            // 
            // FeedRateOverrideEdit
            // 
            this.FeedRateOverrideEdit.Increment = new decimal(new int[] {
            10,
            0,
            0,
            0});
            this.FeedRateOverrideEdit.Location = new System.Drawing.Point(100, 107);
            this.FeedRateOverrideEdit.Name = "FeedRateOverrideEdit";
            this.FeedRateOverrideEdit.Size = new System.Drawing.Size(48, 20);
            this.FeedRateOverrideEdit.TabIndex = 10;
            this.FeedRateOverrideEdit.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.FeedRateOverrideEdit.Value = new decimal(new int[] {
            100,
            0,
            0,
            0});
            this.FeedRateOverrideEdit.ValueChanged += new System.EventHandler(this.FeedRateOverrideEdit_ValueChanged_1);
            // 
            // FeedRateOverrideTitle
            // 
            this.FeedRateOverrideTitle.Location = new System.Drawing.Point(12, 104);
            this.FeedRateOverrideTitle.Name = "FeedRateOverrideTitle";
            this.FeedRateOverrideTitle.Size = new System.Drawing.Size(82, 26);
            this.FeedRateOverrideTitle.TabIndex = 22;
            this.FeedRateOverrideTitle.Text = "Feed Rate Override [%]";
            this.FeedRateOverrideTitle.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // ConditionalStopBox
            // 
            this.ConditionalStopBox.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.ConditionalStopBox.Location = new System.Drawing.Point(12, 134);
            this.ConditionalStopBox.Name = "ConditionalStopBox";
            this.ConditionalStopBox.Size = new System.Drawing.Size(102, 19);
            this.ConditionalStopBox.TabIndex = 11;
            this.ConditionalStopBox.Text = "Stop on M1";
            this.ConditionalStopBox.UseVisualStyleBackColor = true;
            this.ConditionalStopBox.CheckedChanged += new System.EventHandler(this.ConditionalStopBox_CheckedChanged);
            // 
            // SkipLevel0Box
            // 
            this.SkipLevel0Box.AutoSize = true;
            this.SkipLevel0Box.Location = new System.Drawing.Point(100, 159);
            this.SkipLevel0Box.Name = "SkipLevel0Box";
            this.SkipLevel0Box.Size = new System.Drawing.Size(31, 17);
            this.SkipLevel0Box.TabIndex = 13;
            this.SkipLevel0Box.Text = "/";
            this.SkipLevel0Box.UseVisualStyleBackColor = true;
            this.SkipLevel0Box.CheckedChanged += new System.EventHandler(this.SkipLevel0Box_CheckedChanged);
            // 
            // SkipLevel1Box
            // 
            this.SkipLevel1Box.AutoSize = true;
            this.SkipLevel1Box.Location = new System.Drawing.Point(144, 159);
            this.SkipLevel1Box.Name = "SkipLevel1Box";
            this.SkipLevel1Box.Size = new System.Drawing.Size(37, 17);
            this.SkipLevel1Box.TabIndex = 14;
            this.SkipLevel1Box.Text = "/1";
            this.SkipLevel1Box.UseVisualStyleBackColor = true;
            this.SkipLevel1Box.CheckedChanged += new System.EventHandler(this.SkipLevel1Box_CheckedChanged);
            // 
            // SkipLevel2Box
            // 
            this.SkipLevel2Box.AutoSize = true;
            this.SkipLevel2Box.Location = new System.Drawing.Point(188, 159);
            this.SkipLevel2Box.Name = "SkipLevel2Box";
            this.SkipLevel2Box.Size = new System.Drawing.Size(37, 17);
            this.SkipLevel2Box.TabIndex = 15;
            this.SkipLevel2Box.Text = "/2";
            this.SkipLevel2Box.UseVisualStyleBackColor = true;
            this.SkipLevel2Box.CheckedChanged += new System.EventHandler(this.SkipLevel2Box_CheckedChanged);
            // 
            // SkipLevel3Box
            // 
            this.SkipLevel3Box.AutoSize = true;
            this.SkipLevel3Box.Location = new System.Drawing.Point(232, 159);
            this.SkipLevel3Box.Name = "SkipLevel3Box";
            this.SkipLevel3Box.Size = new System.Drawing.Size(37, 17);
            this.SkipLevel3Box.TabIndex = 16;
            this.SkipLevel3Box.Text = "/3";
            this.SkipLevel3Box.UseVisualStyleBackColor = true;
            this.SkipLevel3Box.CheckedChanged += new System.EventHandler(this.SkipLevel3Box_CheckedChanged);
            // 
            // SkipLevelLabel
            // 
            this.SkipLevelLabel.AutoSize = true;
            this.SkipLevelLabel.Location = new System.Drawing.Point(13, 159);
            this.SkipLevelLabel.Name = "SkipLevelLabel";
            this.SkipLevelLabel.Size = new System.Drawing.Size(62, 13);
            this.SkipLevelLabel.TabIndex = 21;
            this.SkipLevelLabel.Text = "Skip Levels";
            // 
            // MCP
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.ClientSize = new System.Drawing.Size(294, 236);
            this.ControlBox = false;
            this.Controls.Add(this.SkipLevel3Box);
            this.Controls.Add(this.SkipLevel2Box);
            this.Controls.Add(this.SkipLevel1Box);
            this.Controls.Add(this.SkipLevel0Box);
            this.Controls.Add(this.ConditionalStopBox);
            this.Controls.Add(this.FeedRateOverrideTitle);
            this.Controls.Add(this.FeedRateOverrideEdit);
            this.Controls.Add(this.ResetMachineData);
            this.Controls.Add(this.SkipLevelLabel);
            this.Controls.Add(this.StatusLabel);
            this.Controls.Add(this.StatusTextBox);
            this.Controls.Add(this.NCFastReset);
            this.Controls.Add(this.NCPartReset);
            this.Controls.Add(this.IPO);
            this.Controls.Add(this.SaveMachineData);
            this.Controls.Add(this.NCSingleBlockMode);
            this.Controls.Add(this.NCReset);
            this.Controls.Add(this.NCClearAlarm);
            this.Controls.Add(this.NCStart);
            this.Controls.Add(this.NCStop);
            this.Controls.Add(this.NCDryRun);
            this.Controls.Add(this.BootVNCK);
            this.Controls.Add(this.ShutdownVNCK);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.KeyPreview = true;
            this.Location = new System.Drawing.Point(0, 520);
            this.Name = "MCP";
            this.StartPosition = System.Windows.Forms.FormStartPosition.Manual;
            this.Text = "Machine Control Panel";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MCP_Close);
            this.Load += new System.EventHandler(this.MCP_Load);
            this.VisibleChanged += new System.EventHandler(this.MCP_Visibility);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.MCP_KeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.FeedRateOverrideEdit)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        internal System.Windows.Forms.ToolTip ToolTip;
        internal System.Windows.Forms.Label IPO;
        internal System.Windows.Forms.Button SaveMachineData;
        internal System.Windows.Forms.CheckBox NCDryRun;
        internal System.Windows.Forms.CheckBox NCSingleBlockMode;
        internal System.Windows.Forms.Button NCReset;
        internal System.Windows.Forms.Button NCClearAlarm;
        internal System.Windows.Forms.Button NCStart;
        internal System.Windows.Forms.Button NCStop;
        internal System.Windows.Forms.Button NCPartReset;
        internal System.Windows.Forms.Button NCFastReset;
        private System.Windows.Forms.TextBox StatusTextBox;
        private System.Windows.Forms.Label StatusLabel;
        internal System.Windows.Forms.Button ResetMachineData;
        internal System.Windows.Forms.Button BootVNCK;
        internal System.Windows.Forms.Button ShutdownVNCK;
        private System.Windows.Forms.NumericUpDown FeedRateOverrideEdit;
        private System.Windows.Forms.Label FeedRateOverrideTitle;
        private System.Windows.Forms.CheckBox ConditionalStopBox;
        private System.Windows.Forms.CheckBox SkipLevel0Box;
        private System.Windows.Forms.CheckBox SkipLevel1Box;
        private System.Windows.Forms.CheckBox SkipLevel2Box;
        private System.Windows.Forms.CheckBox SkipLevel3Box;
        private System.Windows.Forms.Label SkipLevelLabel;
    }
}
