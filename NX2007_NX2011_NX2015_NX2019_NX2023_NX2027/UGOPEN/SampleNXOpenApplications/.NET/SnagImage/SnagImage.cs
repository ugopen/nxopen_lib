/*=============================================================================

                    Copyright (c) 2004 UGS PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: User Example
/*  */

using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;  
using System.IO;
using System.Runtime.InteropServices;

using NXOpen;
using NXOpen.Utilities;
using NXOpen.UF;

namespace SnagImage
{
	/// <summary>
	/// Summary description for SnagImage.
	/// </summary>
    public class SnagImage : System.Windows.Forms.Form
    {
        static Session             m_session		;
        static UI                  m_UI			    ;
        static UFSession           m_openSession	;

        string ext=".bmp";
        string ImageFileName="MyPart"; 

        UFDisp.ImageFormat image_format=UFDisp.ImageFormat.Bmp;
        UFDisp.BackgroundColor background_color=UFDisp.BackgroundColor.Original;

        private System.Windows.Forms.Button btnSnag;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.GroupBox gbImageType;
        private System.Windows.Forms.RadioButton rbBMP;
        private System.Windows.Forms.RadioButton rbGIF;
        private System.Windows.Forms.RadioButton rbPNG;
        private System.Windows.Forms.RadioButton rbTIFF;
        private System.Windows.Forms.RadioButton rbJPEG;
        private System.Windows.Forms.RadioButton rbComTIFF;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rbWhite;
        private System.Windows.Forms.RadioButton rbOriginal;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.Button btnExit;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.TextBox txtFileName;
        private System.Windows.Forms.Button btnSelectFile;
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.Container components = null;

        public static void Main(string[] args) 
        {
           SnagImage createImage= new SnagImage();
           createImage.Show();
        }
        public static int GetUnloadOption(string dummy) 
        {
            return UFConstants.UF_UNLOAD_SEL_DIALOG;
        }
        public SnagImage()
        {
            //                                                                            \
            // Required for Windows Form Designer support
            //
            InitializeComponent();

            //
            // TODO: Add any constructor code after InitializeComponent call
            //
            m_session		= Session.GetSession();
            m_UI			= UI.GetUI();
            m_openSession	= UFSession.GetUFSession();

            ImageFileName="MyPartImage";
            txtFileName.Text = ImageFileName + ext ;
            NXOpenUI.FormUtilities.SetApplicationIcon(this);
            NXOpenUI.FormUtilities.ReparentForm(this);

        }

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose( bool disposing )
        {
            if( disposing )
            {
                if(components != null)
                {
                    components.Dispose();
                }
            }
            base.Dispose( disposing );
        }

        #region Windows Form Designer generated code
        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnSnag = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.gbImageType = new System.Windows.Forms.GroupBox();
            this.rbComTIFF = new System.Windows.Forms.RadioButton();
            this.rbJPEG = new System.Windows.Forms.RadioButton();
            this.rbTIFF = new System.Windows.Forms.RadioButton();
            this.rbPNG = new System.Windows.Forms.RadioButton();
            this.rbGIF = new System.Windows.Forms.RadioButton();
            this.rbBMP = new System.Windows.Forms.RadioButton();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.rbWhite = new System.Windows.Forms.RadioButton();
            this.rbOriginal = new System.Windows.Forms.RadioButton();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.btnExit = new System.Windows.Forms.Button();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.txtFileName = new System.Windows.Forms.TextBox();
            this.btnSelectFile = new System.Windows.Forms.Button();
            this.gbImageType.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnSnag
            // 
            this.btnSnag.Location = new System.Drawing.Point(64, 320);
            this.btnSnag.Name = "btnSnag";
            this.btnSnag.Size = new System.Drawing.Size(120, 32);
            this.btnSnag.TabIndex = 0;
            this.btnSnag.Text = "Snag It";
            this.btnSnag.Click += new System.EventHandler(this.btnSnag_Click);
            // 
            // gbImageType
            // 
            this.gbImageType.Controls.Add(this.rbComTIFF);
            this.gbImageType.Controls.Add(this.rbJPEG);
            this.gbImageType.Controls.Add(this.rbTIFF);
            this.gbImageType.Controls.Add(this.rbPNG);
            this.gbImageType.Controls.Add(this.rbGIF);
            this.gbImageType.Controls.Add(this.rbBMP);
            this.gbImageType.Location = new System.Drawing.Point(16, 16);
            this.gbImageType.Name = "gbImageType";
            this.gbImageType.Size = new System.Drawing.Size(376, 128);
            this.gbImageType.TabIndex = 4;
            this.gbImageType.TabStop = false;
            this.gbImageType.Text = "Image Format";
            // 
            // rbComTIFF
            // 
            this.rbComTIFF.Location = new System.Drawing.Point(224, 88);
            this.rbComTIFF.Name = "rbComTIFF";
            this.rbComTIFF.Size = new System.Drawing.Size(136, 24);
            this.rbComTIFF.TabIndex = 5;
            this.rbComTIFF.Text = "COMPRESSED TIFF";
            this.rbComTIFF.CheckedChanged += new System.EventHandler(this.rbComTIFF_CheckedChanged);
            // 
            // rbJPEG
            // 
            this.rbJPEG.Location = new System.Drawing.Point(64, 88);
            this.rbJPEG.Name = "rbJPEG";
            this.rbJPEG.TabIndex = 4;
            this.rbJPEG.Text = "JPEG";
            this.rbJPEG.CheckedChanged += new System.EventHandler(this.rbJPEG_CheckedChanged);
            // 
            // rbTIFF
            // 
            this.rbTIFF.Location = new System.Drawing.Point(224, 56);
            this.rbTIFF.Name = "rbTIFF";
            this.rbTIFF.TabIndex = 3;
            this.rbTIFF.Text = "TIFF";
            this.rbTIFF.CheckedChanged += new System.EventHandler(this.rbTIFF_CheckedChanged);
            // 
            // rbPNG
            // 
            this.rbPNG.Location = new System.Drawing.Point(224, 24);
            this.rbPNG.Name = "rbPNG";
            this.rbPNG.TabIndex = 2;
            this.rbPNG.Text = "PNG";
            this.rbPNG.CheckedChanged += new System.EventHandler(this.rbPNG_CheckedChanged);
            // 
            // rbGIF
            // 
            this.rbGIF.Location = new System.Drawing.Point(64, 56);
            this.rbGIF.Name = "rbGIF";
            this.rbGIF.TabIndex = 1;
            this.rbGIF.Text = "GIF";
            this.rbGIF.CheckedChanged += new System.EventHandler(this.rbGIF_CheckedChanged);
            // 
            // rbBMP
            // 
            this.rbBMP.Checked = true;
            this.rbBMP.Location = new System.Drawing.Point(64, 24);
            this.rbBMP.Name = "rbBMP";
            this.rbBMP.TabIndex = 0;
            this.rbBMP.TabStop = true;
            this.rbBMP.Text = "BMP";
            this.rbBMP.CheckedChanged += new System.EventHandler(this.rbBMP_CheckedChanged);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rbWhite);
            this.groupBox1.Controls.Add(this.rbOriginal);
            this.groupBox1.Location = new System.Drawing.Point(16, 160);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(376, 56);
            this.groupBox1.TabIndex = 5;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Background Color";
            // 
            // rbWhite
            // 
            this.rbWhite.Location = new System.Drawing.Point(224, 24);
            this.rbWhite.Name = "rbWhite";
            this.rbWhite.TabIndex = 4;
            this.rbWhite.Text = "White";
            this.rbWhite.CheckedChanged += new System.EventHandler(this.rbWhite_CheckedChanged);
            // 
            // rbOriginal
            // 
            this.rbOriginal.Checked = true;
            this.rbOriginal.Location = new System.Drawing.Point(56, 24);
            this.rbOriginal.Name = "rbOriginal";
            this.rbOriginal.TabIndex = 3;
            this.rbOriginal.TabStop = true;
            this.rbOriginal.Text = "Original";
            this.rbOriginal.CheckedChanged += new System.EventHandler(this.rbOriginal_CheckedChanged);
            // 
            // btnExit
            // 
            this.btnExit.Location = new System.Drawing.Point(208, 320);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(144, 32);
            this.btnExit.TabIndex = 8;
            this.btnExit.Text = "Exit";
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.txtFileName);
            this.groupBox2.Controls.Add(this.btnSelectFile);
            this.groupBox2.Location = new System.Drawing.Point(16, 232);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(376, 72);
            this.groupBox2.TabIndex = 9;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Image File Name";
            // 
            // txtFileName
            // 
            this.txtFileName.Location = new System.Drawing.Point(8, 24);
            this.txtFileName.Name = "txtFileName";
            this.txtFileName.Size = new System.Drawing.Size(304, 20);
            this.txtFileName.TabIndex = 14;
            this.txtFileName.Text = "MyPart";
            this.txtFileName.TextChanged += new System.EventHandler(this.txtFileName_TextChanged);
            // 
            // btnSelectFile
            // 
            this.btnSelectFile.Location = new System.Drawing.Point(328, 24);
            this.btnSelectFile.Name = "btnSelectFile";
            this.btnSelectFile.Size = new System.Drawing.Size(32, 24);
            this.btnSelectFile.TabIndex = 12;
            this.btnSelectFile.Text = "...";
            this.btnSelectFile.Click += new System.EventHandler(this.btnSelectFile_Click_1);
            // 
            // SnagImage
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
            this.ClientSize = new System.Drawing.Size(408, 365);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.gbImageType);
            this.Controls.Add(this.btnSnag);
            this.Name = "SnagImage";
            this.Text = "Snag NX Graphics Window Image";
            this.Closed += new System.EventHandler(this.SnagImage_Closed);
            this.gbImageType.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

        }
        #endregion

  
        private void btnSnag_Click(object sender, System.EventArgs e)
        {
            string filename=txtFileName.Text;
            string imageFile=ImageFileName;
            imageFile = Path.ChangeExtension(imageFile,ext);
            try
            {
                string path = Path.GetFullPath(imageFile);
                m_openSession.Disp.CreateImage(imageFile,image_format,background_color);
                MessageBox.Show("Generated image is :- "+path,"Result",MessageBoxButtons.OK,MessageBoxIcon.Information);
            }
            catch(Exception ex)
            {
                MessageBox.Show("Image Generated Failed"+ex.Message,"Result",MessageBoxButtons.OK,MessageBoxIcon.Error);
            }
        }

        private void btnSelectFile_Click(object sender, System.EventArgs e)
        {
            saveFileDialog1.FileName=ImageFileName;
            saveFileDialog1.Title="Select the Image File Name";
            saveFileDialog1.Filter="Graphics Interchange Format(*.gif)|*.gif|Windows Bitmap(*.bmp)|*.bmp|JPG Interchange Format(*.jpg)|*.jpg|Tag Image File Format(*.tif)|*.tif|Compressed Tiff(*.tiff)|*.tiff|Portable Network Graphics(*.png)|*.png|All Files (*.*)|*.*";
            if (saveFileDialog1.ShowDialog() == DialogResult.OK) 
            {
                ImageFileName = saveFileDialog1.FileName;
                txtFileName.Text= ImageFileName;
            }
        }

        private void btnExit_Click(object sender, System.EventArgs e)
        {
            Close();
            Application.Exit();
        }

        private void rbPNG_CheckedChanged(object sender, System.EventArgs e)
        {
            image_format= UFDisp.ImageFormat.Png;
            ext=".png";
            txtFileName.Text=ImageFileName+ext;
        }

        private void rbBMP_CheckedChanged(object sender, System.EventArgs e)
        {
            image_format= UFDisp.ImageFormat.Bmp;
            ext=".bmp";
            txtFileName.Text=ImageFileName+ext;
        }

        private void rbGIF_CheckedChanged(object sender, System.EventArgs e)
        {
            image_format= UFDisp.ImageFormat.Gif;
            ext=".gif";
            txtFileName.Text=ImageFileName+ext;
        }

        private void rbJPEG_CheckedChanged(object sender, System.EventArgs e)
        {
            image_format= UFDisp.ImageFormat.Jpeg;
            ext=".jpg";
            txtFileName.Text=ImageFileName+ext;
        }

        private void rbTIFF_CheckedChanged(object sender, System.EventArgs e)
        {
            image_format= UFDisp.ImageFormat.Tiff;
            ext=".tif";
            txtFileName.Text=ImageFileName+ext;
        }

        private void rbComTIFF_CheckedChanged(object sender, System.EventArgs e)
        {
            image_format= UFDisp.ImageFormat.CompressedTiff;
            ext=".tiff";
            txtFileName.Text=ImageFileName+ext;
        }

        private void rbOriginal_CheckedChanged(object sender, System.EventArgs e)
        {
            background_color=UFDisp.BackgroundColor.Original;
        }

        private void rbWhite_CheckedChanged(object sender, System.EventArgs e)
        {
            background_color=UFDisp.BackgroundColor.White;
        }

        private void radioButton1_CheckedChanged(object sender, System.EventArgs e)
        {
            background_color=UFDisp.BackgroundColor.InvalidColor;
        }

        private void btnSelectFile_Click_1(object sender, System.EventArgs e)
        {
            saveFileDialog1.FileName=ImageFileName;
            saveFileDialog1.Title="Select the Image File Name";
            switch(image_format)
            {
                case UFDisp.ImageFormat.Bmp:
                    saveFileDialog1.Filter="Windows Bitmap(*.bmp)|*.bmp|All Files (*.*)|*.*";
                    break;
                case UFDisp.ImageFormat.Gif:
                    saveFileDialog1.Filter="Graphics Interchange Format(*.gif)|*.gif|All Files (*.*)|*.*";
                    break;
                case UFDisp.ImageFormat.Jpeg:
                    saveFileDialog1.Filter="JPG Interchange Format(*.jpg)|*.jpg|All Files (*.*)|*.*";
                    break;
                case UFDisp.ImageFormat.Tiff:
                    saveFileDialog1.Filter="Tag Image File Format(*.tif)|*.tif|All Files (*.*)|*.*";
                    break;
                case UFDisp.ImageFormat.CompressedTiff:
                    saveFileDialog1.Filter="Compressed Tiff(*.tiff)|*.tiff|All Files (*.*)|*.*";
                    break;
                case UFDisp.ImageFormat.Png:
                    saveFileDialog1.Filter="Portable Network Graphics(*.png)|*.png|All Files (*.*)|*.*";
                    break;
                default:
                    saveFileDialog1.Filter="Graphics Interchange Format(*.gif)|*.gif|Windows Bitmap(*.bmp)|*.bmp|JPG Interchange Format(*.jpg)|*.jpg|Tag Image File Format(*.tif)|*.tif|Compressed Tiff(*.tiff)|*.tiff|Portable Network Graphics(*.png)|*.png|All Files (*.*)|*.*";
                    break;
            }

            if (saveFileDialog1.ShowDialog() == DialogResult.OK) 
            {
                ImageFileName = saveFileDialog1.FileName;
                txtFileName.Text= ImageFileName;
                
            }
        }

        private void SnagImage_Closed(object sender, System.EventArgs e)
        {
            Application.Exit();
        }

        private void txtFileName_TextChanged(object sender, System.EventArgs e)
        {
            //Abhishek Mishra 22nd March 2006,Fix for PR#5428154
            ImageFileName = Path.GetFileNameWithoutExtension(txtFileName.Text);
        }

    }
}
