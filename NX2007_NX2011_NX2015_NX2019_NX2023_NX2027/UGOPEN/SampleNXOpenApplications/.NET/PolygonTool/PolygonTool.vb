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
Option Strict On

Imports System
Imports System.Drawing
Imports System.Collections
Imports System.ComponentModel
Imports System.Data
Imports System.IO
Imports System.Windows.Forms

Imports NXOpen
Imports NXOpen.Utilities

Public Class PolygonTool
    Inherits System.Windows.Forms.Form

    Private Shared m_partFlag As Boolean = True ' Is there a work part?
    Private Shared m_OK As Boolean = False
    Private Shared m_frm As PolygonTool
    Private Const m_diameterTextFormat As String = "F2"

#Region " Windows Form Designer generated code "

    Private Declare Auto Sub SetParent Lib "USER32.DLL" _
        (ByVal child As IntPtr, ByVal newParent As IntPtr)

    Public Sub New()
        MyBase.New()

        'This call is required by the Windows Form Designer.
        InitializeComponent()

        'Add any initialization after the InitializeComponent() call

        ' Make this form a child of the NX frame
        Dim ufSession As NXOpen.UF.UFSession = NXOpen.UF.UFSession.GetUFSession()
        Dim parent As IntPtr = ufSession.Ui.GetDefaultParent()
        SetParent(Me.Handle, parent)

        Me.TopMost = True   ' Now make the top most form of application

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
    Friend WithEvents spnNoSides As System.Windows.Forms.NumericUpDown
    Friend WithEvents picBox As System.Windows.Forms.PictureBox
    Friend WithEvents txtDiameter As System.Windows.Forms.TextBox
    Friend WithEvents chkInscribed As System.Windows.Forms.CheckBox
    Friend WithEvents lblDiameter As System.Windows.Forms.Label
    Friend WithEvents lblNoSides As System.Windows.Forms.Label
    Friend WithEvents cmdCancel As System.Windows.Forms.Button
    Friend WithEvents cmdOK As System.Windows.Forms.Button

    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
Me.spnNoSides = New System.Windows.Forms.NumericUpDown
Me.picBox = New System.Windows.Forms.PictureBox
Me.txtDiameter = New System.Windows.Forms.TextBox
Me.chkInscribed = New System.Windows.Forms.CheckBox
Me.lblDiameter = New System.Windows.Forms.Label
Me.lblNoSides = New System.Windows.Forms.Label
Me.cmdCancel = New System.Windows.Forms.Button
Me.cmdOK = New System.Windows.Forms.Button
CType(Me.spnNoSides, System.ComponentModel.ISupportInitialize).BeginInit()
Me.SuspendLayout()
'
'spnNoSides
'
Me.spnNoSides.Location = New System.Drawing.Point(136, 8)
Me.spnNoSides.Name = "spnNoSides"
Me.spnNoSides.Size = New System.Drawing.Size(104, 20)
Me.spnNoSides.TabIndex = 17
'
'picBox
'
Me.picBox.Location = New System.Drawing.Point(136, 72)
Me.picBox.Name = "picBox"
Me.picBox.Size = New System.Drawing.Size(90, 90)
Me.picBox.TabIndex = 16
Me.picBox.TabStop = False
'
'txtDiameter
'
Me.txtDiameter.Location = New System.Drawing.Point(136, 40)
Me.txtDiameter.Name = "txtDiameter"
Me.txtDiameter.TabIndex = 15
Me.txtDiameter.Text = "0.0"
'
'chkInscribed
'
Me.chkInscribed.Location = New System.Drawing.Point(16, 72)
Me.chkInscribed.Name = "chkInscribed"
Me.chkInscribed.TabIndex = 14
Me.chkInscribed.Text = "Inscribed"
'
'lblDiameter
'
Me.lblDiameter.Location = New System.Drawing.Point(16, 40)
Me.lblDiameter.Name = "lblDiameter"
Me.lblDiameter.TabIndex = 13
Me.lblDiameter.Text = "Diameter"
'
'lblNoSides
'
Me.lblNoSides.Location = New System.Drawing.Point(16, 8)
Me.lblNoSides.Name = "lblNoSides"
Me.lblNoSides.TabIndex = 12
Me.lblNoSides.Text = "Number of sides"
'
'cmdCancel
'
Me.cmdCancel.Location = New System.Drawing.Point(168, 168)
Me.cmdCancel.Name = "cmdCancel"
Me.cmdCancel.RightToLeft = System.Windows.Forms.RightToLeft.Yes
Me.cmdCancel.TabIndex = 11
Me.cmdCancel.Text = "Cancel"
'
'cmdOK
'
Me.cmdOK.Location = New System.Drawing.Point(88, 168)
Me.cmdOK.Name = "cmdOK"
Me.cmdOK.TabIndex = 10
Me.cmdOK.Text = "OK"
'
'PolygonTool
'
Me.AutoScaleBaseSize = New System.Drawing.Size(5, 13)
Me.ClientSize = New System.Drawing.Size(264, 198)
Me.Controls.Add(Me.spnNoSides)
Me.Controls.Add(Me.picBox)
Me.Controls.Add(Me.txtDiameter)
Me.Controls.Add(Me.chkInscribed)
Me.Controls.Add(Me.lblDiameter)
Me.Controls.Add(Me.lblNoSides)
Me.Controls.Add(Me.cmdCancel)
Me.Controls.Add(Me.cmdOK)
Me.MaximizeBox = False
Me.Name = "PolygonTool"
Me.Text = "Create Polygon"
CType(Me.spnNoSides, System.ComponentModel.ISupportInitialize).EndInit()
Me.ResumeLayout(False)

    End Sub

#End Region

    <STAThread()> _
    Public Shared Sub Main(ByVal args As String())
        PolygonTool.m_frm = New PolygonTool
        PolygonTool.m_frm.Show()

        If Not PolygonTool.m_partFlag Then
            MessageBox.Show("Tool only available when in a sketch", "Error", _
                MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
            PolygonTool.m_frm.Close()
        End If

    End Sub

    ' Set the unload behavior of this application in NX. This will get called
    ' by NX after the application has completed running.
    Public Shared Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = Session.LibraryUnloadOption.Explicitly
    End Function

    Private Sub SetDefaultDiameter(ByVal part As Part)
            If (part.PartUnits = part.Units.Millimeters) Then
                Me.txtDiameter.Text = (100.0).ToString(m_diameterTextFormat)
            Else
                Me.txtDiameter.Text = (4.0).ToString(m_diameterTextFormat)
            End If
    End Sub

    Private Sub PolygonTool_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        Dim session1 As Session
        Dim part As Part
        session1 = Session.GetSession
        Try
            part = session1.Parts.Work
            Me.SetDefaultDiameter(part)
            PolygonTool.m_partFlag = True
        Catch
            PolygonTool.m_partFlag = False
        End Try

        Me.spnNoSides.Value = New Decimal(6)

        Me.chkInscribed.Checked = True

    End Sub

    Private Sub chkInscribed_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles chkInscribed.CheckedChanged

        ' Change the bitmap displayed
        Dim bitmapResourceName As String = ""
        Try
            If Me.chkInscribed.Checked Then
                bitmapResourceName = "PolygonTool.across_flats.bmp"
            Else
                bitmapResourceName = "PolygonTool.across_corners.bmp"
            End If

            ' You can use this call to get the list of available resources embedded
            ' in the dll including the 
            'Dim resourceNames As String() = _
            '    System.Reflection.Assembly.GetExecutingAssembly.GetManifestResourceNames()

            ' The bitmap is an embedded resource in the dll. Retrieve this resource here
            Dim thisExe As System.Reflection.Assembly = _
                System.Reflection.Assembly.GetExecutingAssembly()
            Dim file As System.IO.Stream = _
                thisExe.GetManifestResourceStream(bitmapResourceName)
            Me.picBox.Image = Image.FromStream(file)

        Catch
            MessageBox.Show("Cannot find embedded bitmap: " & bitmapResourceName & _
                Environment.NewLine & Environment.NewLine & _
                "No bitmaps will appear in the dialog", "Cannot find bitmap", _
                MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
        End Try

    End Sub

    Private Sub cmdCancel_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmdCancel.Click
         PolygonTool.m_frm.Close()
    End Sub

    Private Sub cmdOK_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmdOK.Click
            ' Get values fom the dialog
            Dim noSides As Integer = CType(Me.spnNoSides.Value, Integer)
            Dim diameter As Double = System.Convert.ToDouble(Me.txtDiameter.Text)
            Dim inscribed As Boolean = Me.chkInscribed.Checked

            Dim polygon As PolygonDraw
            ' Can be inside the try block - as the class is instantiated inside the try block, 
            ' trying to call it elsewhere results in a compile error
            Try
                polygon = New PolygonDraw(noSides, diameter, inscribed) ' Will throw an exception if there is no sketch
                polygon.Draw()
            Catch ex As System.Exception
                ' Caught something...
                MessageBox.Show(ex.GetType.ToString & Environment.NewLine & ex.Message)
            End Try

            PolygonTool.m_frm.Close()

    End Sub

    Private Sub txtDiameter_Leave(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles txtDiameter.Leave

        Try
            Me.txtDiameter.Text = (Double.Parse(Me.txtDiameter.Text)).ToString(m_diameterTextFormat)
        Catch
            Me.SetDefaultDiameter(Session.GetSession().Parts.Work)
            MessageBox.Show("Enter valid numerical value for diameter", "Invalid diameter", _
                MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
        End Try

    End Sub

    Private Sub spnNoSides_ValueChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles spnNoSides.ValueChanged

        ' Make sure that we cannot get less than 3 sides...
        If Me.spnNoSides.Value < 3 Then
            MessageBox.Show("Must have at least three sides!", "Input Error", _
                MessageBoxButtons.OK, MessageBoxIcon.Information)
            Me.spnNoSides.Value = 3
        End If
    End Sub

End Class
