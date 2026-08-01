'
'          Copyright (c) 2004 UGS PLM Solutions
'                  All rights reserved
'          Written by V.A.L.
'
'  
' ===================================================================
Option Strict On
Imports System
Imports System.Windows.Forms
Imports System.Environment
Imports NXOpen
Imports NXOpen.Annotations
Imports Microsoft.VisualBasic


Module NXJournal

    Dim nxopenSession As NXOpen.UF.UFSession

    Sub Main()

        Dim theSession As Session = Session.GetSession()
        Dim theUI As UI = UI.GetUI()
        nxopenSession = NXOpen.UF.UFSession.GetUFSession()

        theSession.SetUndoMark( Session.MarkVisibility.Visible, "Create notes")

        Dim form As UserSymbolForm = New UserSymbolForm(theSession, theUI)

        Do
            If form.ShowDialog() <> DialogResult.OK Then Exit Sub

            Dim letteringPrefs As LetteringPreferences = Nothing
            Dim userSymPrefs As UserSymbolPreferences = Nothing
            Dim noteText() As String = Nothing
            ' Get the note creation data that the user entered on the form
            If Not form.GetNoteCreationData(letteringPrefs, userSymPrefs, noteText) Then Exit Sub

            Dim workPart As Part = theSession.Parts.Work
            Dim response As Selection.DialogResponse
            ' Create notes at the position specified by the user, until the user cancels
            Do
                Dim cursor As Point3d
                Dim view As NXOpen.View = Nothing
                response = theUI.SelectionManager.SelectScreenPosition("Select location for new note", view, cursor)
                If response <> Selection.DialogResponse.Pick Then Exit Do
                workPart.Annotations.CreateNote(noteText, cursor, AxisOrientation.Horizontal, _
                    letteringPrefs, userSymPrefs)
            Loop

            If response <> Selection.DialogResponse.Back Then Exit Do
        Loop
        form.Close()

    End Sub

End Module

' A form for the user to input data for creating a note
' either by copying an existing note or from a user defined symbol
Public Class UserSymbolForm
    Inherits System.Windows.Forms.Form

    ''''''''''''
    '       PUBLIC METHODS
    ''''''''''''

    Public Sub New(ByVal session As Session, ByVal ui As UI)
        MyBase.New()
        m_session = session
        m_ui = ui

        'This call is required by the Windows Form Designer.
        InitializeComponent()

        'Add any initialization after the InitializeComponent() call
        Me.m_sbfFileNameTextBox.Text = ""
        Me.m_copyExistingRadioButton.Checked = True
        Me.EnableUserSymInputs(False)

    End Sub

    ' Returns the data for note creation selected on the form.
    ' All parameters are output parameters.
    '
    ' This function should only be called after this form has been
    ' shown to the user and only if the user did not cancel out of
    ' the form.
    Public Function GetNoteCreationData( _
        ByRef letteringPrefs As LetteringPreferences, _
        ByRef userSymPrefs As UserSymbolPreferences, _
        ByRef noteText() As String) As Boolean

        If Me.DialogResult <> DialogResult.OK Then _
            Throw New System.Exception("Illegal to call GetNoteCreationData if the form was canceled")

        If m_copyExistingRadioButton.Checked Then
            ' User selected Copy Existing Note

            ' Prompt user to select a note to copy
            Dim selected As TaggedObject = Nothing
            Dim cursor As Point3d
            Dim mask(1) As Selection.MaskTriple
            mask(0).type = NXOpen.UF.UFConstants.UF_drafting_entity_type
            mask(0).subtype = NXOpen.UF.UFConstants.UF_draft_note_subtype
            mask(1).type = NXOpen.UF.UFConstants.UF_drafting_entity_type
            mask(1).subtype = NXOpen.UF.UFConstants.UF_draft_label_subtype
            m_ui.SelectionManager.SelectTaggedObject("Select note to clone", "Select note to clone", Selection.SelectionScope.WorkPart, _
                Selection.SelectionAction.ClearAndEnableSpecific, False, False, mask, _
                selected, cursor)
            If selected Is Nothing Then Return False

            ' Send back the note's data
            Dim note As NoteBase = CType(selected, NoteBase)
            letteringPrefs = note.GetLetteringPreferences()
            userSymPrefs = note.GetUserSymbolPreferences()
            noteText = note.GetText()

        Else
            ' User selected Create From User Defined Symbol
            Dim double1 As Double
            Dim double2 As Double
            Dim selectedSymbol As String = Me.m_symbolNameComboBox.Text
            ' The symbol font must be loaded before it can be used
            m_session.Parts.Work.Annotations.LoadSymbolFontFromSbfFile(selectedSymbol, double1, double2)
            letteringPrefs = Nothing ' use the global lettering preferences
            userSymPrefs = m_session.Parts.Work.Annotations.NewUserSymbolPreferences(UserSymbolPreferences.SizeType.ScaleAspectRatio, _
                Me.m_scaleTextBox.Value, Me.m_aspectRatioTextBox.Value)
            selectedSymbol = selectedSymbol.Trim
            noteText = New String() {"<%" & selectedSymbol & ">"}

        End If

        Return True

    End Function

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
    'Inserted by the Windows Form Designer
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents m_createButton As System.Windows.Forms.Button
    Friend WithEvents m_copyExistingRadioButton As System.Windows.Forms.RadioButton
    Friend WithEvents m_userSymRadioButton As System.Windows.Forms.RadioButton
    Friend WithEvents LocationLabel As System.Windows.Forms.Label
    Friend WithEvents m_sbfFileNameTextBox As System.Windows.Forms.TextBox
    Friend WithEvents m_symbolNameComboBox As System.Windows.Forms.ComboBox
    Friend WithEvents m_cancelButton As System.Windows.Forms.Button
    Private WithEvents m_scaleTextBox As NumericTextBox
    Private WithEvents m_aspectRatioTextBox As NumericTextBox
    Friend WithEvents m_browseButton As System.Windows.Forms.Button
    Friend WithEvents m_sbfFileNamePanel As System.Windows.Forms.Panel
    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
        Me.Label1 = New System.Windows.Forms.Label
        Me.m_sbfFileNameTextBox = New System.Windows.Forms.TextBox
        Me.LocationLabel = New System.Windows.Forms.Label
        Me.m_symbolNameComboBox = New System.Windows.Forms.ComboBox
        Me.m_createButton = New System.Windows.Forms.Button
        Me.m_cancelButton = New System.Windows.Forms.Button
        Me.m_copyExistingRadioButton = New System.Windows.Forms.RadioButton
        Me.m_userSymRadioButton = New System.Windows.Forms.RadioButton
        Me.Label2 = New System.Windows.Forms.Label
        Me.m_scaleTextBox = New NumericTextBox(1.0)
        Me.Label3 = New System.Windows.Forms.Label
        Me.m_aspectRatioTextBox = New NumericTextBox(1.0)
        Me.m_browseButton = New System.Windows.Forms.Button
        Me.m_sbfFileNamePanel = New System.Windows.Forms.Panel
        Me.m_sbfFileNamePanel.SuspendLayout()
        Me.SuspendLayout()
        '
        'Label1
        '
        Me.Label1.Location = New System.Drawing.Point(8, 136)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(96, 16)
        Me.Label1.TabIndex = 5
        Me.Label1.Text = "Select symbol"
        '
        'm_sbfFileNameTextBox
        '
        Me.m_sbfFileNameTextBox.Location = New System.Drawing.Point(0, 0)
        Me.m_sbfFileNameTextBox.Name = "m_sbfFileNameTextBox"
        Me.m_sbfFileNameTextBox.Size = New System.Drawing.Size(208, 20)
        Me.m_sbfFileNameTextBox.TabIndex = 0
        Me.m_sbfFileNameTextBox.Text = ""
        '
        'LocationLabel
        '
        Me.LocationLabel.Location = New System.Drawing.Point(8, 72)
        Me.LocationLabel.Name = "LocationLabel"
        Me.LocationLabel.Size = New System.Drawing.Size(176, 23)
        Me.LocationLabel.TabIndex = 2
        Me.LocationLabel.Text = "Location of symbol font file"
        '
        'm_symbolNameComboBox
        '
        Me.m_symbolNameComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        Me.m_symbolNameComboBox.Location = New System.Drawing.Point(8, 160)
        Me.m_symbolNameComboBox.Name = "m_symbolNameComboBox"
        Me.m_symbolNameComboBox.Size = New System.Drawing.Size(121, 21)
        Me.m_symbolNameComboBox.TabIndex = 6
        '
        'm_createButton
        '
        Me.m_createButton.DialogResult = DialogResult.OK
        Me.m_createButton.Location = New System.Drawing.Point(8, 232)
        Me.m_createButton.Name = "m_createButton"
        Me.m_createButton.TabIndex = 11
        Me.m_createButton.Text = "Create"
        '
        'm_cancelButton
        '
        Me.m_cancelButton.Location = New System.Drawing.Point(176, 232)
        Me.m_cancelButton.Name = "m_cancelButton"
        Me.m_cancelButton.TabIndex = 12
        Me.m_cancelButton.Text = "Cancel"
        '
        'm_copyExistingRadioButton
        '
        Me.m_copyExistingRadioButton.Location = New System.Drawing.Point(16, 8)
        Me.m_copyExistingRadioButton.Name = "m_copyExistingRadioButton"
        Me.m_copyExistingRadioButton.Size = New System.Drawing.Size(160, 24)
        Me.m_copyExistingRadioButton.TabIndex = 0
        Me.m_copyExistingRadioButton.Text = "Copy existing symbol"
        '
        'm_userSymRadioButton
        '
        Me.m_userSymRadioButton.Location = New System.Drawing.Point(16, 32)
        Me.m_userSymRadioButton.Name = "m_userSymRadioButton"
        Me.m_userSymRadioButton.Size = New System.Drawing.Size(200, 24)
        Me.m_userSymRadioButton.TabIndex = 1
        Me.m_userSymRadioButton.Text = "Create from user defined symbol"
        '
        'Label2
        '
        Me.Label2.Location = New System.Drawing.Point(168, 144)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(40, 16)
        Me.Label2.TabIndex = 7
        Me.Label2.Text = "Scale"
        '
        'm_scaleTextBox
        '
        Me.m_scaleTextBox.Location = New System.Drawing.Point(224, 144)
        Me.m_scaleTextBox.Name = "m_scaleTextBox"
        Me.m_scaleTextBox.Size = New System.Drawing.Size(56, 20)
        Me.m_scaleTextBox.TabIndex = 9
        '
        'Label3
        '
        Me.Label3.Location = New System.Drawing.Point(168, 176)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(48, 32)
        Me.Label3.TabIndex = 8
        Me.Label3.Text = "Aspect ratio"
        '
        'm_aspectRatioTextBox
        '
        Me.m_aspectRatioTextBox.Location = New System.Drawing.Point(224, 176)
        Me.m_aspectRatioTextBox.Name = "m_aspectRatioTextBox"
        Me.m_aspectRatioTextBox.Size = New System.Drawing.Size(56, 20)
        Me.m_aspectRatioTextBox.TabIndex = 10
        '
        'm_browseButton
        '
        Me.m_browseButton.Location = New System.Drawing.Point(216, 0)
        Me.m_browseButton.Name = "m_browseButton"
        Me.m_browseButton.Size = New System.Drawing.Size(56, 23)
        Me.m_browseButton.TabIndex = 1
        Me.m_browseButton.Text = "Browse"
        '
        'm_sbfFileNamePanel
        '
        Me.m_sbfFileNamePanel.Controls.Add(Me.m_sbfFileNameTextBox)
        Me.m_sbfFileNamePanel.Controls.Add(Me.m_browseButton)
        Me.m_sbfFileNamePanel.Location = New System.Drawing.Point(8, 104)
        Me.m_sbfFileNamePanel.Name = "m_sbfFileNamePanel"
        Me.m_sbfFileNamePanel.Size = New System.Drawing.Size(272, 24)
        Me.m_sbfFileNamePanel.TabIndex = 2
        '
        'UserSymbolForm
        '
        Me.CancelButton = Me.m_cancelButton
        Me.AutoScaleBaseSize = New System.Drawing.Size(5, 13)
        Me.ClientSize = New System.Drawing.Size(292, 273)
        Me.Controls.Add(Me.m_aspectRatioTextBox)
        Me.Controls.Add(Me.m_scaleTextBox)
        Me.Controls.Add(Me.m_sbfFileNamePanel)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.m_userSymRadioButton)
        Me.Controls.Add(Me.m_copyExistingRadioButton)
        Me.Controls.Add(Me.m_cancelButton)
        Me.Controls.Add(Me.m_createButton)
        Me.Controls.Add(Me.m_symbolNameComboBox)
        Me.Controls.Add(Me.LocationLabel)
        Me.Controls.Add(Me.Label1)
        Me.Name = "UserSymbolForm"
        Me.Text = "Create note"
        Me.m_sbfFileNamePanel.ResumeLayout(False)
        Me.ResumeLayout(False)

    End Sub

    ' A TextBox that only accepts floating point numbers greater than 1.0e-5
    Private Class NumericTextBox
        Inherits TextBox

        Public Sub New(ByVal x As Double)
            MyBase.New()
            m_value = x
            Me.Text = x.ToString()
        End Sub

        Public ReadOnly Property Value() As Double
            Get
                Return m_value
            End Get
        End Property

        Public Overrides Property Text() As String
            Get
                Return MyBase.Text
            End Get
            Set(ByVal text As String)
                m_value = Double.Parse(text)
                MyBase.Text = text
            End Set
        End Property

        Protected Overrides Sub OnValidating(ByVal e As System.ComponentModel.CancelEventArgs)

            ' Accept the input only if it is a floating point number
            ' greater than 1.0e-5
            Dim valid As Boolean = False
            Dim value As Double
            Try
                value = Double.Parse(Me.Text)
                If value > 0.00001 Then valid = True
            Catch ex As Exception
            End Try
            If valid Then
                m_value = value
            Else
                Me.Text = m_value.ToString
                e.Cancel = True
                MessageBox.Show("Invalid Input" & NewLine & "A positive number greater than 1.0e-5 is required")
            End If
            MyBase.OnValidating(e)

        End Sub

        Protected Overrides Sub OnKeyPress(ByVal e As KeyPressEventArgs)
            ' If Enter is pressed, move to the next control
            ' (Attempting to move to the next control will automatically cause
            ' OnValidating to be called for this control, and the move will
            ' not be permitted if validation fails.)
            If e.KeyChar = Chr(13) Then
                Me.Parent.SelectNextControl(Me, True, False, False, True)
            End If
            MyBase.OnKeyPress(e)
        End Sub

        Private m_value As Double

    End Class

    ' Loads the symbol font names from the file named in the sbf file name text box.
    ' Returns true iff the sbf file was successfully loaded.
    ' Parameters:
    ' errMsg - (output) An error message if the load fails
    Private Function LoadSymbolNames(ByRef errMsg As String) As Boolean

        If Not System.IO.File.Exists(m_sbfFileNameTextBox.Text) Then
            errMsg = "File not found"
            Return False
        End If
        Dim symbolNames() As String
        Try
            m_session.Parts.Work.Annotations.CurrentSbfFile = m_sbfFileNameTextBox.Text
            symbolNames = m_session.Parts.Work.Annotations.ReadAllSymbolNamesFromSbfFile()
        Catch ex As NXException
            errMsg = "Error opening sbf file" & NewLine & ex.ToString()
            Return False
        End Try
        If symbolNames.Length = 0 Then
            errMsg = "No symbols in the sbf file"
            Return False
        End If

        ' Put the symbol names in the combobox
        m_symbolNameComboBox.Items.Clear()
        m_symbolNameComboBox.Items.AddRange(symbolNames)
        Me.m_symbolNameComboBox.Text = symbolNames(0)

        Return True

    End Function

    ' Returns true iff the file named in the sbf file name text box is a valid sbf file
    '
    ' If the file is valid, the symbol names are placed in the symbol name combobox
    ' If the file is not valid, the sbf file name text box is reverted to the name
    ' of the last valid sbf file (or m_noValidSbfFileMsg if no valid sbf file has
    ' ever been entered).
    Private Function ValidateSbfFileName() As Boolean
        ' If the text box has the "enter a file name" prompt, return false
        If Me.m_sbfFileNameTextBox.Text = m_noValidSbfFileMsg Then
            MessageBox.Show("Enter a file name")
            Return False
        End If

        ' Me.m_sbfFileNameTextBox.Tag is the name of the last valid sbf file

        ' If the text box matches the name of the last valid sbf file, no validation
        ' is needed because the sbf file has already been validated.  So, return true.
        If Me.m_sbfFileNameTextBox.Text = CType(Me.m_sbfFileNameTextBox.Tag, String) Then
            Return True
        End If
        Dim errMsg As String = Nothing

        ' Attempt to load the symbol names
        If Not LoadSymbolNames(errMsg) Then
            MessageBox.Show(errMsg)
            ' Revert the name in the text box to the name of the last valid sbf file
            Me.m_sbfFileNameTextBox.Text = CType(Me.m_sbfFileNameTextBox.Tag, String)
            Return False
        Else
            ' The sbf file is valid, so store the name in m_sbfFileNameTextBox.Tag
            Me.m_sbfFileNameTextBox.Tag = Me.m_sbfFileNameTextBox.Text
            Return True
        End If

    End Function


    ' Sets the enabled status of all user inputs relevant to user symbols
    Private Sub EnableUserSymInputs(ByVal enabled As Boolean)
        m_aspectRatioTextBox.Enabled = enabled
        m_scaleTextBox.Enabled = enabled
        m_sbfFileNameTextBox.Enabled = enabled
        m_symbolNameComboBox.Enabled = enabled
        m_browseButton.Enabled = enabled

    End Sub

    Private Sub CopyExistingRadioButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles m_copyExistingRadioButton.Click
        EnableUserSymInputs(False)
    End Sub

    Private Sub UserSymRadioButton_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles m_userSymRadioButton.Click
        EnableUserSymInputs(True)
        ' If the sbf file name text box is empty, set it to the default sbf file
        ' in the UGII_BASE_DIR directory, and attempt to load it
        If m_sbfFileNameTextBox.Text = "" Then
            m_sbfFileNameTextBox.Text = System.IO.Path.Combine( _
                    GetEnvironmentVariable("UGII_BASE_DIR"), "ugii\\ug_default.sbf" )
            m_sbfFileNameTextBox.Tag = m_noValidSbfFileMsg
            ' If validation fails, put focus on the sbf file name text box
            If Not ValidateSbfFileName() Then
                m_sbfFileNameTextBox.Focus()
            End If
        End If
    End Sub

    Private Sub BrowseButton_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles m_browseButton.Click
        ' Prompt user to select an sbf file via the Open File Dialog and
        ' then check that the selected file is valid
        Dim fileDialog As OpenFileDialog = New OpenFileDialog
        fileDialog.Filter = "sbf files (*.sbf)|*.sbf|All files (*.*)|*.*"
        fileDialog.FilterIndex = 1
        If fileDialog.ShowDialog() = DialogResult.OK Then
            Me.m_sbfFileNameTextBox.Text = fileDialog.FileName
            Me.ValidateSbfFileName()
        End If
    End Sub

    Private Sub SbfFileNameTextBox_KeyPress(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyPressEventArgs) Handles m_sbfFileNameTextBox.KeyPress
        ' If the user presses enter, go to the symbol name combobox
        ' Attempting to go to the symbol name combobox will trigger a
        ' sbf file name validate event
        If e.KeyChar = Chr(13) Then
            Me.m_symbolNameComboBox.Focus()
        End If
    End Sub

    Private Sub SbfFileNamePanel_Validating(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles m_sbfFileNamePanel.Validating
        ' Check that the sbf file name is valid
        ' unless the user pressed the cancel button or the user pressed
        ' the copy-existing radio button while the "enter a file name" prompt
        ' is in the sbf file name text box.
        If Not Me.m_cancelButton.Focused Then
            If Me.m_copyExistingRadioButton.Focused AndAlso Me.m_sbfFileNameTextBox.Text = m_noValidSbfFileMsg Then
                Me.m_sbfFileNameTextBox.Text = ""
                Me.m_sbfFileNameTextBox.Tag = Nothing
            ElseIf Not ValidateSbfFileName() Then
                e.Cancel = True
            End If
        End If
    End Sub

    ''''''''''
    '    PRIVATE DATA
    ''''''''''

    Private Shared ReadOnly m_noValidSbfFileMsg As String = "(enter sbf file location)"

    Private m_session As Session
    Private m_ui As UI

End Class


