' ===================================================================
'
'             Copyright (c) 2004  UGS PLM Solutions
'               Unpublished - All rights reserved
'
' ===================================================================
' *******************************************************************
'  Description
'    Class that provides the Winforms UI for the example
'
'  
'
' *******************************************************************
Imports System
Imports System.Drawing
Imports System.Collections
Imports System.ComponentModel
Imports System.Windows.Forms
Imports System.IO

Imports NXOpen
Imports NXOpen.Utilities
Imports NXOpen.UF

Public Class SnagImageVB
    Inherits System.Windows.Forms.Form

#Region " Windows Form Designer generated code "

    Public Sub New()
        MyBase.New()

        'This call is required by the Windows Form Designer.
        InitializeComponent()

        'Add any initialization after the InitializeComponent() call
        ' Make this form a child of the NX frame
        Dim ufSession As UFSession = ufSession.GetUFSession()

        NXOpenUI.FormUtilities.SetApplicationIcon(Me)
        NXOpenUI.FormUtilities.ReparentForm(Me)

        m_session = Session.GetSession()
        m_UI = UI.GetUI()
        m_openSession = ufSession.GetUFSession()
        ImageFileName = m_session.Parts.Work.Name
        If ImageFileName = "" Then
            ImageFileName = "MyPartImage"
        End If
        txtFileName.Text = ImageFileName + ext
    End Sub

    'Form overrides dispose to clean up the component list.
    Protected Overloads Overrides Sub Dispose(ByVal disposing As Boolean)
        If disposing Then
            If Not (components Is Nothing) Then
                components.Dispose()
            End If
        End If
        MyBase.Dispose(disposing)
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    Friend WithEvents btnExit As System.Windows.Forms.Button
    Friend WithEvents folderBrowserDialog1 As System.Windows.Forms.FolderBrowserDialog
    Friend WithEvents saveFileDialog1 As System.Windows.Forms.SaveFileDialog
    Friend WithEvents openFileDialog1 As System.Windows.Forms.OpenFileDialog
    Friend WithEvents groupBox2 As System.Windows.Forms.GroupBox
    Friend WithEvents txtFileName As System.Windows.Forms.TextBox
    Friend WithEvents btnSelectFile As System.Windows.Forms.Button
    Friend WithEvents groupBox1 As System.Windows.Forms.GroupBox
    Friend WithEvents rbWhite As System.Windows.Forms.RadioButton
    Friend WithEvents rbOriginal As System.Windows.Forms.RadioButton
    Friend WithEvents gbImageType As System.Windows.Forms.GroupBox
    Friend WithEvents rbComTIFF As System.Windows.Forms.RadioButton
    Friend WithEvents rbJPEG As System.Windows.Forms.RadioButton
    Friend WithEvents rbTIFF As System.Windows.Forms.RadioButton
    Friend WithEvents rbPNG As System.Windows.Forms.RadioButton
    Friend WithEvents rbGIF As System.Windows.Forms.RadioButton
    Friend WithEvents rbBMP As System.Windows.Forms.RadioButton
    Friend WithEvents btnSnag As System.Windows.Forms.Button
    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
        Me.btnExit = New System.Windows.Forms.Button
        Me.folderBrowserDialog1 = New System.Windows.Forms.FolderBrowserDialog
        Me.saveFileDialog1 = New System.Windows.Forms.SaveFileDialog
        Me.openFileDialog1 = New System.Windows.Forms.OpenFileDialog
        Me.groupBox2 = New System.Windows.Forms.GroupBox
        Me.txtFileName = New System.Windows.Forms.TextBox
        Me.btnSelectFile = New System.Windows.Forms.Button
        Me.groupBox1 = New System.Windows.Forms.GroupBox
        Me.rbWhite = New System.Windows.Forms.RadioButton
        Me.rbOriginal = New System.Windows.Forms.RadioButton
        Me.gbImageType = New System.Windows.Forms.GroupBox
        Me.rbComTIFF = New System.Windows.Forms.RadioButton
        Me.rbJPEG = New System.Windows.Forms.RadioButton
        Me.rbTIFF = New System.Windows.Forms.RadioButton
        Me.rbPNG = New System.Windows.Forms.RadioButton
        Me.rbGIF = New System.Windows.Forms.RadioButton
        Me.rbBMP = New System.Windows.Forms.RadioButton
        Me.btnSnag = New System.Windows.Forms.Button
        Me.groupBox2.SuspendLayout()
        Me.groupBox1.SuspendLayout()
        Me.gbImageType.SuspendLayout()
        Me.SuspendLayout()
        '
        'btnExit
        '
        Me.btnExit.Location = New System.Drawing.Point(208, 318)
        Me.btnExit.Name = "btnExit"
        Me.btnExit.Size = New System.Drawing.Size(144, 32)
        Me.btnExit.TabIndex = 13
        Me.btnExit.Text = "Exit"
        '
        'groupBox2
        '
        Me.groupBox2.Controls.Add(Me.txtFileName)
        Me.groupBox2.Controls.Add(Me.btnSelectFile)
        Me.groupBox2.Location = New System.Drawing.Point(16, 230)
        Me.groupBox2.Name = "groupBox2"
        Me.groupBox2.Size = New System.Drawing.Size(376, 72)
        Me.groupBox2.TabIndex = 14
        Me.groupBox2.TabStop = False
        Me.groupBox2.Text = "Image File Name"
        '
        'txtFileName
        '
        Me.txtFileName.Location = New System.Drawing.Point(8, 24)
        Me.txtFileName.Name = "txtFileName"
        Me.txtFileName.Size = New System.Drawing.Size(304, 20)
        Me.txtFileName.TabIndex = 14
        Me.txtFileName.Text = "MyPart"
        '
        'btnSelectFile
        '
        Me.btnSelectFile.Location = New System.Drawing.Point(328, 24)
        Me.btnSelectFile.Name = "btnSelectFile"
        Me.btnSelectFile.Size = New System.Drawing.Size(32, 24)
        Me.btnSelectFile.TabIndex = 12
        Me.btnSelectFile.Text = "..."
        '
        'groupBox1
        '
        Me.groupBox1.Controls.Add(Me.rbWhite)
        Me.groupBox1.Controls.Add(Me.rbOriginal)
        Me.groupBox1.Location = New System.Drawing.Point(16, 158)
        Me.groupBox1.Name = "groupBox1"
        Me.groupBox1.Size = New System.Drawing.Size(376, 56)
        Me.groupBox1.TabIndex = 12
        Me.groupBox1.TabStop = False
        Me.groupBox1.Text = "Background Color"
        '
        'rbWhite
        '
        Me.rbWhite.Location = New System.Drawing.Point(224, 24)
        Me.rbWhite.Name = "rbWhite"
        Me.rbWhite.Size = New System.Drawing.Size(104, 24)
        Me.rbWhite.TabIndex = 4
        Me.rbWhite.Text = "White"
        '
        'rbOriginal
        '
        Me.rbOriginal.Location = New System.Drawing.Point(56, 24)
        Me.rbOriginal.Name = "rbOriginal"
        Me.rbOriginal.Size = New System.Drawing.Size(104, 24)
        Me.rbOriginal.TabIndex = 3
        Me.rbOriginal.Text = "Original"
        '
        'gbImageType
        '
        Me.gbImageType.Controls.Add(Me.rbComTIFF)
        Me.gbImageType.Controls.Add(Me.rbJPEG)
        Me.gbImageType.Controls.Add(Me.rbTIFF)
        Me.gbImageType.Controls.Add(Me.rbPNG)
        Me.gbImageType.Controls.Add(Me.rbGIF)
        Me.gbImageType.Controls.Add(Me.rbBMP)
        Me.gbImageType.Location = New System.Drawing.Point(16, 14)
        Me.gbImageType.Name = "gbImageType"
        Me.gbImageType.Size = New System.Drawing.Size(376, 128)
        Me.gbImageType.TabIndex = 11
        Me.gbImageType.TabStop = False
        Me.gbImageType.Text = "Image Format"
        '
        'rbComTIFF
        '
        Me.rbComTIFF.Location = New System.Drawing.Point(224, 88)
        Me.rbComTIFF.Name = "rbComTIFF"
        Me.rbComTIFF.Size = New System.Drawing.Size(136, 24)
        Me.rbComTIFF.TabIndex = 5
        Me.rbComTIFF.Text = "COMPRESSED TIFF"
        '
        'rbJPEG
        '
        Me.rbJPEG.Location = New System.Drawing.Point(64, 88)
        Me.rbJPEG.Name = "rbJPEG"
        Me.rbJPEG.Size = New System.Drawing.Size(104, 24)
        Me.rbJPEG.TabIndex = 4
        Me.rbJPEG.Text = "JPEG"
        '
        'rbTIFF
        '
        Me.rbTIFF.Location = New System.Drawing.Point(224, 56)
        Me.rbTIFF.Name = "rbTIFF"
        Me.rbTIFF.Size = New System.Drawing.Size(104, 24)
        Me.rbTIFF.TabIndex = 3
        Me.rbTIFF.Text = "TIFF"
        '
        'rbPNG
        '
        Me.rbPNG.Location = New System.Drawing.Point(224, 24)
        Me.rbPNG.Name = "rbPNG"
        Me.rbPNG.Size = New System.Drawing.Size(104, 24)
        Me.rbPNG.TabIndex = 2
        Me.rbPNG.Text = "PNG"
        '
        'rbGIF
        '
        Me.rbGIF.Location = New System.Drawing.Point(64, 56)
        Me.rbGIF.Name = "rbGIF"
        Me.rbGIF.Size = New System.Drawing.Size(104, 24)
        Me.rbGIF.TabIndex = 1
        Me.rbGIF.Text = "GIF"
        '
        'rbBMP
        '
        Me.rbBMP.Checked = True
        Me.rbBMP.Location = New System.Drawing.Point(64, 24)
        Me.rbBMP.Name = "rbBMP"
        Me.rbBMP.Size = New System.Drawing.Size(104, 24)
        Me.rbBMP.TabIndex = 0
        Me.rbBMP.TabStop = True
        Me.rbBMP.Text = "BMP"
        '
        'btnSnag
        '
        Me.btnSnag.Location = New System.Drawing.Point(64, 318)
        Me.btnSnag.Name = "btnSnag"
        Me.btnSnag.Size = New System.Drawing.Size(120, 32)
        Me.btnSnag.TabIndex = 10
        Me.btnSnag.Text = "Snag It"
        '
        'SnagImageVB
        '
        Me.AutoScaleBaseSize = New System.Drawing.Size(5, 13)
        Me.ClientSize = New System.Drawing.Size(408, 365)
        Me.Controls.Add(Me.gbImageType)
        Me.Controls.Add(Me.btnSnag)
        Me.Controls.Add(Me.btnExit)
        Me.Controls.Add(Me.groupBox2)
        Me.Controls.Add(Me.groupBox1)
        Me.Name = "SnagImageVB"
        Me.Text = "SnagImage: Grab a NX Graphics Windows Region"
        Me.groupBox2.ResumeLayout(False)
        Me.groupBox2.PerformLayout()
        Me.groupBox1.ResumeLayout(False)
        Me.gbImageType.ResumeLayout(False)
        Me.ResumeLayout(False)

    End Sub

#End Region

    Public m_session As Session
    Public m_UI As UI
    Public m_openSession As UFSession

    Public ext As String = ".bmp"
    Public ImageFileName As String = "MyPart"

    Dim image_format As UFDisp.ImageFormat = UFDisp.ImageFormat.Bmp
    Dim background_color As UFDisp.BackgroundColor = UFDisp.BackgroundColor.Original
    Public Shared createImage As SnagImageVB
    <STAThread()> _
    Public Shared Sub Main()
        createImage = New SnagImageVB
        createImage.ShowDialog()
    End Sub


    Public Shared Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = UFConstants.UF_UNLOAD_SEL_DIALOG
    End Function

    Public Sub SnagImageVB()

        '//                                                                            
        '// Required for Windows Form Designer support
        '//
        InitializeComponent()

        '//
        '// TODO: Add any constructor code after InitializeComponent call
        '//
        m_session = Session.GetSession()
        m_UI = UI.GetUI()
        m_openSession = UFSession.GetUFSession()
        ImageFileName = m_session.Parts.Work.Name
        If ImageFileName = "" Then
            ImageFileName = "MyPartImage"
        End If
        txtFileName.Text = ImageFileName + ext
    End Sub

    Private Sub btnSnag_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSnag.Click
        Dim filename As String = txtFileName.Text
        Dim imageFile As String = ImageFileName
        imageFile = path.ChangeExtension(imageFile, ext)
        Try
            Dim path As String = IO.Path.GetFullPath(imageFile)
            m_openSession.Disp.CreateImage(imageFile, image_format, background_color)
            MessageBox.Show("Image Generated at :-" & path, "Result", MessageBoxButtons.OK, MessageBoxIcon.Information)
        Catch ex As Exception
            MessageBox.Show("Image Generated Failed" + ex.Message, "Result", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End Try
    End Sub

    Private Sub btnExit_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnExit.Click
        createImage.Close()
    End Sub

    Private Sub btnSelectFile_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSelectFile.Click
        saveFileDialog1.FileName = ImageFileName
        saveFileDialog1.Title = "Select the Image File Name"
        Select Case image_format
            Case UFDisp.ImageFormat.Bmp
                saveFileDialog1.Filter = "Windows Bitmap(*.bmp)|*.bmp|All Files (*.*)|*.*"
            Case UFDisp.ImageFormat.Gif
                saveFileDialog1.Filter = "Graphics Interchange Format(*.gif)|*.gif|All Files (*.*)|*.*"

            Case UFDisp.ImageFormat.Jpeg
                saveFileDialog1.Filter = "JPG Interchange Format(*.jpg)|*.jpg|All Files (*.*)|*.*"

            Case UFDisp.ImageFormat.Tiff
                saveFileDialog1.Filter = "Tag Image File Format(*.tif)|*.tif|All Files (*.*)|*.*"

            Case UFDisp.ImageFormat.CompressedTiff
                saveFileDialog1.Filter = "Compressed Tiff(*.tiff)|*.tiff|All Files (*.*)|*.*"

            Case UFDisp.ImageFormat.Png
                saveFileDialog1.Filter = "Portable Network Graphics(*.png)|*.png|All Files (*.*)|*.*"

            Case Else
                saveFileDialog1.Filter = "Graphics Interchange Format(*.gif)|*.gif|Windows Bitmap(*.bmp)|*.bmp|JPG Interchange Format(*.jpg)|*.jpg|Tag Image File Format(*.tif)|*.tif|Compressed Tiff(*.tiff)|*.tiff|Portable Network Graphics(*.png)|*.png|All Files (*.*)|*.*"
        End Select
        If saveFileDialog1.ShowDialog() = DialogResult.OK Then
            ImageFileName = saveFileDialog1.FileName
            txtFileName.Text = ImageFileName
            ImageFileName = Path.GetDirectoryName(ImageFileName) & "\" & Path.GetFileNameWithoutExtension(ImageFileName)

            MessageBox.Show(ImageFileName)
        End If
    End Sub


    Sub extension(ByVal ext As String)

        If (txtFileName.TextLength > 0) Then
            If (Path.HasExtension(txtFileName.Text)) Then
                If (Path.GetDirectoryName(txtFileName.Text).Length > 0) Then
                    txtFileName.Text = Path.GetDirectoryName(txtFileName.Text) & "\" & Path.GetFileNameWithoutExtension(txtFileName.Text) & ext
                    ImageFileName = Path.GetDirectoryName(txtFileName.Text) & "\" & Path.GetFileNameWithoutExtension(txtFileName.Text)
                Else
                    txtFileName.Text = Path.GetFileNameWithoutExtension(txtFileName.Text) & ext
                    ImageFileName = Path.GetFileNameWithoutExtension(txtFileName.Text)
                End If
            Else

                txtFileName.Text = txtFileName.Text + ext
                ImageFileName = txtFileName.Text
            End If
        End If
    End Sub
    Private Sub rbPNG_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles rbPNG.CheckedChanged
        image_format = UFDisp.ImageFormat.Png
        ext = ".png"
        extension(ext)


    End Sub

    Private Sub rbBMP_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles rbBMP.CheckedChanged
        image_format = UFDisp.ImageFormat.Bmp
        ext = ".bmp"
        extension(ext)
    End Sub

    Private Sub rbGIF_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles rbGIF.CheckedChanged
        image_format = UFDisp.ImageFormat.Gif
        ext = ".gif"
        extension(ext)
    End Sub

    Private Sub rbTIFF_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles rbTIFF.CheckedChanged
        image_format = UFDisp.ImageFormat.Tiff
        ext = ".tif"
        extension(ext)
    End Sub

    Private Sub rbComTIFF_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles rbComTIFF.CheckedChanged
        image_format = UFDisp.ImageFormat.CompressedTiff
        ext = ".tif"
        extension(ext)
    End Sub

    Private Sub rbJPEG_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles rbJPEG.CheckedChanged
        image_format = UFDisp.ImageFormat.Jpeg
        ext = ".jpg"
        extension(ext)
    End Sub

    Private Sub rbOriginal_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles rbOriginal.CheckedChanged
        background_color = UFDisp.BackgroundColor.Original
    End Sub

    Private Sub rbWhite_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles rbWhite.CheckedChanged
        background_color = UFDisp.BackgroundColor.White
    End Sub

    Private Sub txtFileName_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles txtFileName.TextChanged
        ImageFileName = txtFileName.Text
    End Sub
End Class
