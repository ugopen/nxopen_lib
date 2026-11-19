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
            this.GroupBoxOverride = new System.Windows.Forms.GroupBox();
            this.PictureBox1 = new System.Windows.Forms.PictureBox();
            this.FeedRateOverrideMaxLabel = new System.Windows.Forms.Label();
            this.FeedRateOverrideMinLabel = new System.Windows.Forms.Label();
            this.FeedRateOverrideValueLabel = new System.Windows.Forms.Label();
            this.FeedRateOverrideTrackBar = new System.Windows.Forms.TrackBar();
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
            this.GroupBoxOverride.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.PictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.FeedRateOverrideTrackBar)).BeginInit();
            this.SuspendLayout();
            // 
            // GroupBoxOverride
            // 
            this.GroupBoxOverride.Controls.Add(this.PictureBox1);
            this.GroupBoxOverride.Controls.Add(this.FeedRateOverrideMaxLabel);
            this.GroupBoxOverride.Controls.Add(this.FeedRateOverrideMinLabel);
            this.GroupBoxOverride.Controls.Add(this.FeedRateOverrideValueLabel);
            this.GroupBoxOverride.Controls.Add(this.FeedRateOverrideTrackBar);
            this.GroupBoxOverride.Location = new System.Drawing.Point(12, 65);
            this.GroupBoxOverride.Name = "GroupBoxOverride";
            this.GroupBoxOverride.Size = new System.Drawing.Size(465, 121);
            this.GroupBoxOverride.TabIndex = 32;
            this.GroupBoxOverride.TabStop = false;
            this.GroupBoxOverride.Text = "Feed Rate Override";
            // 
            // PictureBox1
            // 
            this.PictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.PictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("PictureBox1.Image")));
            this.PictureBox1.Location = new System.Drawing.Point(11, 19);
            this.PictureBox1.Name = "PictureBox1";
            this.PictureBox1.Size = new System.Drawing.Size(30, 32);
            this.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.PictureBox1.TabIndex = 15;
            this.PictureBox1.TabStop = false;
            this.ToolTip.SetToolTip(this.PictureBox1, "Feed Rate Override");
            // 
            // FeedRateOverrideMaxLabel
            // 
            this.FeedRateOverrideMaxLabel.AutoSize = true;
            this.FeedRateOverrideMaxLabel.Location = new System.Drawing.Point(432, 90);
            this.FeedRateOverrideMaxLabel.Name = "FeedRateOverrideMaxLabel";
            this.FeedRateOverrideMaxLabel.Size = new System.Drawing.Size(25, 13);
            this.FeedRateOverrideMaxLabel.TabIndex = 17;
            this.FeedRateOverrideMaxLabel.Text = "100";
            // 
            // FeedRateOverrideMinLabel
            // 
            this.FeedRateOverrideMinLabel.AutoSize = true;
            this.FeedRateOverrideMinLabel.Location = new System.Drawing.Point(14, 90);
            this.FeedRateOverrideMinLabel.Name = "FeedRateOverrideMinLabel";
            this.FeedRateOverrideMinLabel.Size = new System.Drawing.Size(13, 13);
            this.FeedRateOverrideMinLabel.TabIndex = 16;
            this.FeedRateOverrideMinLabel.Text = "0";
            // 
            // FeedRateOverrideValueLabel
            // 
            this.FeedRateOverrideValueLabel.AutoSize = true;
            this.FeedRateOverrideValueLabel.Location = new System.Drawing.Point(43, 29);
            this.FeedRateOverrideValueLabel.Name = "FeedRateOverrideValueLabel";
            this.FeedRateOverrideValueLabel.Size = new System.Drawing.Size(13, 13);
            this.FeedRateOverrideValueLabel.TabIndex = 15;
            this.FeedRateOverrideValueLabel.Text = "0";
            // 
            // FeedRateOverrideTrackBar
            // 
            this.FeedRateOverrideTrackBar.Location = new System.Drawing.Point(6, 57);
            this.FeedRateOverrideTrackBar.Name = "FeedRateOverrideTrackBar";
            this.FeedRateOverrideTrackBar.Size = new System.Drawing.Size(453, 45);
            this.FeedRateOverrideTrackBar.TabIndex = 7;
            this.FeedRateOverrideTrackBar.Scroll += new System.EventHandler(this.FeedRateOverrideTrackBar_Scroll);
            // 
            // IPO
            // 
            this.IPO.AutoSize = true;
            this.IPO.Location = new System.Drawing.Point(416, 25);
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
            this.SaveMachineData.Location = new System.Drawing.Point(366, 12);
            this.SaveMachineData.Name = "SaveMachineData";
            this.SaveMachineData.Size = new System.Drawing.Size(38, 38);
            this.SaveMachineData.TabIndex = 30;
            this.ToolTip.SetToolTip(this.SaveMachineData, "Save Machine Data");
            this.SaveMachineData.UseVisualStyleBackColor = false;
            this.SaveMachineData.Click += new System.EventHandler(this.SaveMachineData_Click);
            // 
            // NCDryRun
            // 
            this.NCDryRun.Appearance = System.Windows.Forms.Appearance.Button;
            this.NCDryRun.AutoSize = true;
            this.NCDryRun.Image = ((System.Drawing.Image)(resources.GetObject("NCDryRun.Image")));
            this.NCDryRun.Location = new System.Drawing.Point(231, 12);
            this.NCDryRun.Name = "NCDryRun";
            this.NCDryRun.Size = new System.Drawing.Size(38, 38);
            this.NCDryRun.TabIndex = 29;
            this.ToolTip.SetToolTip(this.NCDryRun, "Dry Run");
            this.NCDryRun.UseVisualStyleBackColor = true;
            this.NCDryRun.CheckedChanged += new System.EventHandler(this.NCDryRun_CheckedChanged);
            // 
            // NCSingleBlockMode
            // 
            this.NCSingleBlockMode.Appearance = System.Windows.Forms.Appearance.Button;
            this.NCSingleBlockMode.AutoSize = true;
            this.NCSingleBlockMode.Image = ((System.Drawing.Image)(resources.GetObject("NCSingleBlockMode.Image")));
            this.NCSingleBlockMode.Location = new System.Drawing.Point(187, 12);
            this.NCSingleBlockMode.Name = "NCSingleBlockMode";
            this.NCSingleBlockMode.Size = new System.Drawing.Size(38, 38);
            this.NCSingleBlockMode.TabIndex = 28;
            this.NCSingleBlockMode.Text = "\r\n";
            this.ToolTip.SetToolTip(this.NCSingleBlockMode, "Single Block Mode");
            this.NCSingleBlockMode.UseVisualStyleBackColor = true;
            this.NCSingleBlockMode.CheckedChanged += new System.EventHandler(this.NCSingleBlockMode_CheckedChanged);
            // 
            // NCReset
            // 
            this.NCReset.Image = ((System.Drawing.Image)(resources.GetObject("NCReset.Image")));
            this.NCReset.Location = new System.Drawing.Point(99, 12);
            this.NCReset.Name = "NCReset";
            this.NCReset.Size = new System.Drawing.Size(38, 38);
            this.NCReset.TabIndex = 26;
            this.ToolTip.SetToolTip(this.NCReset, "Reset NC");
            this.NCReset.UseVisualStyleBackColor = true;
            this.NCReset.Click += new System.EventHandler(this.NCReset_Click);
            // 
            // NCClearAlarm
            // 
            this.NCClearAlarm.Image = ((System.Drawing.Image)(resources.GetObject("NCClearAlarm.Image")));
            this.NCClearAlarm.Location = new System.Drawing.Point(143, 12);
            this.NCClearAlarm.Name = "NCClearAlarm";
            this.NCClearAlarm.Size = new System.Drawing.Size(38, 38);
            this.NCClearAlarm.TabIndex = 27;
            this.ToolTip.SetToolTip(this.NCClearAlarm, "Clear Alarms");
            this.NCClearAlarm.UseVisualStyleBackColor = true;
            this.NCClearAlarm.Click += new System.EventHandler(this.NCClearAlarm_Click);
            // 
            // NCStart
            // 
            this.NCStart.Image = ((System.Drawing.Image)(resources.GetObject("NCStart.Image")));
            this.NCStart.Location = new System.Drawing.Point(12, 12);
            this.NCStart.Name = "NCStart";
            this.NCStart.Size = new System.Drawing.Size(38, 38);
            this.NCStart.TabIndex = 24;
            this.NCStart.Text = "\r\n";
            this.ToolTip.SetToolTip(this.NCStart, "Play");
            this.NCStart.UseVisualStyleBackColor = true;
            this.NCStart.Click += new System.EventHandler(this.NCStart_Click);
            // 
            // NCStop
            // 
            this.NCStop.Image = ((System.Drawing.Image)(resources.GetObject("NCStop.Image")));
            this.NCStop.Location = new System.Drawing.Point(55, 12);
            this.NCStop.Name = "NCStop";
            this.NCStop.Size = new System.Drawing.Size(38, 38);
            this.NCStop.TabIndex = 25;
            this.ToolTip.SetToolTip(this.NCStop, "Stop");
            this.NCStop.UseVisualStyleBackColor = true;
            this.NCStop.Click += new System.EventHandler(this.NCStop_Click);
            // 
            // NCPartReset
            // 
            this.NCPartReset.Image = ((System.Drawing.Image)(resources.GetObject("NCPartReset.Image")));
            this.NCPartReset.Location = new System.Drawing.Point(278, 12);
            this.NCPartReset.Name = "NCPartReset";
            this.NCPartReset.Size = new System.Drawing.Size(38, 38);
            this.NCPartReset.TabIndex = 33;
            this.ToolTip.SetToolTip(this.NCPartReset, "Part Reset");
            this.NCPartReset.UseVisualStyleBackColor = true;
            this.NCPartReset.Click += new System.EventHandler(this.NCPartReset_Click);
            // 
            // NCFastReset
            // 
            this.NCFastReset.Image = ((System.Drawing.Image)(resources.GetObject("NCFastReset.Image")));
            this.NCFastReset.Location = new System.Drawing.Point(322, 12);
            this.NCFastReset.Name = "NCFastReset";
            this.NCFastReset.Size = new System.Drawing.Size(38, 38);
            this.NCFastReset.TabIndex = 34;
            this.ToolTip.SetToolTip(this.NCFastReset, "Reset Machine");
            this.NCFastReset.UseVisualStyleBackColor = true;
            this.NCFastReset.Click += new System.EventHandler(this.NCFastReset_Click);
            // 
            // MCP
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(489, 198);
            this.ControlBox = false;
            this.Controls.Add(this.NCFastReset);
            this.Controls.Add(this.NCPartReset);
            this.Controls.Add(this.GroupBoxOverride);
            this.Controls.Add(this.IPO);
            this.Controls.Add(this.SaveMachineData);
            this.Controls.Add(this.NCDryRun);
            this.Controls.Add(this.NCSingleBlockMode);
            this.Controls.Add(this.NCReset);
            this.Controls.Add(this.NCClearAlarm);
            this.Controls.Add(this.NCStart);
            this.Controls.Add(this.NCStop);
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
            this.GroupBoxOverride.ResumeLayout(false);
            this.GroupBoxOverride.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.PictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.FeedRateOverrideTrackBar)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.GroupBox GroupBoxOverride;
        internal System.Windows.Forms.PictureBox PictureBox1;
        internal System.Windows.Forms.ToolTip ToolTip;
        internal System.Windows.Forms.Label FeedRateOverrideMaxLabel;
        internal System.Windows.Forms.Label FeedRateOverrideMinLabel;
        internal System.Windows.Forms.Label FeedRateOverrideValueLabel;
        internal System.Windows.Forms.TrackBar FeedRateOverrideTrackBar;
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

    }
}
