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
Imports System
Imports System.Windows.Forms
Imports System.Linq
Imports NXOpen
Imports NXOpen.SIM

Public Class MCP
    Private Shared theSession As Session
    Private Shared theIsvControlPanelBuilder As SIM.IsvControlPanelBuilder

    Private isInHistoryBufferCallbackId As Integer
    Private vncStatusCallbackId As Integer
    Private simStopCallbackId As Integer
    Private isInHistoryBuffer = False
    Private isSimStop = False

    ' List of ui elements to toggle their visibility
    Private configuredUiControls As List(Of Control)

    Private Declare Function FindWindow Lib "user32" _
        Alias "FindWindowA" (
        ByVal lpClassName As String,
        ByVal lpWindowName As String) As Long

    Private Declare Function ShowWindow Lib "user32" (
        ByVal hwnd As Integer,
        ByVal nCmdShow As Integer) As Integer

    'The settings that is used in ShowWindow method
    Private Const SW_SHOWNOACTIVATE = 4 'Show Window
    Private Const SW_MINIMIZE = 6 'Minimize Window

    Private Declare Function SetForegroundWindow Lib "user32" (
        ByVal hwnd As Long) As Long

    'Return the HMI Window (either with vnck 4.4 or vnck 2.6)
    Private Function FindHMIWindow() As Long

        Dim hWndHMI As Long

        'Search HMI window by title for Operate with VNCK 4.4.
        hWndHMI = FindWindow(vbNullString, "SINUMERIK Operate - Window Mode")

        'If VNCK 4.4 HMI window not founded then search VNCK 2.6 HMI window.
        If hWndHMI = IntPtr.Zero Then
            hWndHMI = FindWindow(vbNullString, "HMI SolutionLine - Window Mode")
        End If

        Return hWndHMI

    End Function

    Protected Overrides Sub Finalize()
        ' Destructor
        If (Not IsDisposed And Not Disposing) Then
            Dispose(True)
        End If
    End Sub

    Private Sub MCP_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        'Make the displayed window a child of the main NX window
        NXOpenUI.FormUtilities.ReparentForm(Me)

        'Get the NX session
        theSession = Session.GetSession()

        'Create the Cam session
        theSession.CreateCamSession()

        'Get the KinematicConfigurator
        Dim workPart As Part = theSession.Parts.Work
        Dim kinematicConfigurator As SIM.KinematicConfigurator = workPart.KinematicConfigurator

        'Get the IsvControlPanelBuilder
        theIsvControlPanelBuilder = kinematicConfigurator.IsvControlPanelBuilder

        '#Region "insert ui controls"
        'Collect all UI Controls to toggle enable/disable.
        configuredUiControls = New List(Of Control) From {
            NCStart,
            NCStop,
            NCReset,
            FeedRateOverrideTitle,
            FeedRateOverrideEdit,
            SaveMachineData,
            ResetMachineData,
            NCDryRun,
            NCSingleBlockMode,
            NCClearAlarm,
            NCPartReset,
            NCFastReset,
            BootVNCK,
            ShutdownVNCK,
            ConditionalStopBox,
            SkipLevel0Box,
            SkipLevel1Box,
            SkipLevel2Box,
            SkipLevel3Box,
            SkipLevelLabel
        }
        '#End Region

        'Set the Feed Rate Override maximum value
        UpdateFeedRateOverrideMaximum()
        UpdateFeedRateOverrideValue()

        'Set the machine control cyle time
        UpdateCycleTime()

        'Read the current settings from VNCK if available.
        UpdateConditionalStop()
        UpdateSkipLevels()

        'Add callback to get notified when the Historybuffer is entered or left.
        isInHistoryBufferCallbackId = theIsvControlPanelBuilder.AddIsInHistoryBuffer(New NXOpen.SIM.IsvControlPanelBuilder.IsInHistoryBufferCb(AddressOf IsInHistoryBufferCallback))

        'Add callback to get notified when the VncStatus changed.
        vncStatusCallbackId = theIsvControlPanelBuilder.AddVncStatus(New NXOpen.SIM.IsvControlPanelBuilder.VncStatusCb(AddressOf VncStatusCallback))

        'Add callback to get notified when the Simulation is frozen.
        simStopCallbackId = theIsvControlPanelBuilder.AddSimStop(New NXOpen.SIM.IsvControlPanelBuilder.SimStopCb(AddressOf SimStopCallback))

        'Update UI to show the current VncStatus.
        UpdateUI(theIsvControlPanelBuilder.VncStatus)
    End Sub

    Private Sub MCP_Disposed(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Disposed
        'Remove all callbacks.
        theIsvControlPanelBuilder.RemoveIsInHistoryBuffer(isInHistoryBufferCallbackId)
        theIsvControlPanelBuilder.RemoveVncStatus(vncStatusCallbackId)
        theIsvControlPanelBuilder.RemoveSimStop(simStopCallbackId)
    End Sub

    Private Sub UpdateCycleTime()
        Dim ipoValue As Integer = theIsvControlPanelBuilder.MachineControlGetCycleTime
        IPO.Text = "IPO: " + ipoValue.ToString() + " ms"
    End Sub

    Private Sub UpdateFeedRateOverrideMaximum()
        Dim max As Integer = theIsvControlPanelBuilder.MachineControlGetFeedRateOverrideMaximumValue
        FeedRateOverrideEdit.Maximum = Math.Max(max, 100)
        FeedRateOverrideEdit.Minimum = 0
        FeedRateOverrideEdit.Value = Math.Min(FeedRateOverrideEdit.Value, max)
    End Sub

    Private Sub UpdateFeedRateOverrideValue()
        If (Not (IsNothing(theIsvControlPanelBuilder))) Then
            Dim strValue As String
            strValue = ""
            Dim strType As String
            strType = ""
            If (theIsvControlPanelBuilder.MachineControlReadVariable(vbNullString,
                                                                     "VDI_VARTYPE_PATH_OVERRIDE_ACTIVATE",
                                                                     strValue,
                                                                     strType)) Then
                If (strValue.Equals("VDI_VARVALUE_SWITCH_OFF")) Then
                    FeedRateOverrideEdit.Value = 100
                Else
                    If (theIsvControlPanelBuilder.MachineControlReadVariable(vbNullString,
                                                                             "VDI_VARTYPE_PATH_OVERRIDE",
                                                                             strValue,
                                                                             strType)) Then
                        FeedRateOverrideEdit.Value = System.Convert.ToDecimal(strValue)
                    End If
                End If
            Else
                FeedRateOverrideEdit.Value = 100
            End If
        End If

    End Sub

    Private Sub UpdateConditionalStop()
        If (Not (IsNothing(theIsvControlPanelBuilder))) Then
            Dim strValue As String
            strValue = ""
            Dim strType As String
            strType = ""
            If (theIsvControlPanelBuilder.MachineControlReadVariable(vbNullString,
                                                                     "VDI_VARTYPE_ACTIVATE_M1",
                                                                     strValue,
                                                                     strType)) Then
                ConditionalStopBox.Checked = strValue.Equals("VDI_VARVALUE_SWITCH_ON")
            End If
        Else
            ConditionalStopBox.Checked = False
        End If

    End Sub

    Private Sub UpdateSkipLevels()
        If (Not (IsNothing(theIsvControlPanelBuilder))) Then
            Dim strValue As String
            strValue = ""
            Dim strType As String
            strType = ""
            ' Read all the individual Skip Level settings and update their check boxes.
            If (theIsvControlPanelBuilder.MachineControlReadVariable(vbNullString,
                                                                     "VDI_VARTYPE_MODIFY_SKIP",
                                                                     strValue,
                                                                     strType)) Then
                If (SkipLevel0Box.Checked.Equals(Not (strValue.Equals("VDI_VARVALUE_SWITCH_ON")))) Then
                    SkipLevel0Box.Checked = strValue.Equals("VDI_VARVALUE_SWITCH_ON")
                End If
            End If
            If (theIsvControlPanelBuilder.MachineControlReadVariable(vbNullString,
                                                                     "VDI_VARTYPE_MODIFY_SKIP1",
                                                                     strValue,
                                                                     strType)) Then
                If (SkipLevel1Box.Checked.Equals(Not (strValue.Equals("VDI_VARVALUE_SWITCH_ON")))) Then
                    SkipLevel1Box.Checked = strValue.Equals("VDI_VARVALUE_SWITCH_ON")
                End If
            End If
            If (theIsvControlPanelBuilder.MachineControlReadVariable(vbNullString,
                                                                     "VDI_VARTYPE_MODIFY_SKIP2",
                                                                     strValue,
                                                                     strType)) Then
                If (SkipLevel2Box.Checked.Equals(Not (strValue.Equals("VDI_VARVALUE_SWITCH_ON")))) Then
                    SkipLevel2Box.Checked = strValue.Equals("VDI_VARVALUE_SWITCH_ON")
                End If
            End If
            If (theIsvControlPanelBuilder.MachineControlReadVariable(vbNullString,
                                                                     "VDI_VARTYPE_MODIFY_SKIP3",
                                                                     strValue,
                                                                     strType)) Then
                If (SkipLevel3Box.Checked.Equals(Not (strValue.Equals("VDI_VARVALUE_SWITCH_ON")))) Then
                    SkipLevel3Box.Checked = strValue.Equals("VDI_VARVALUE_SWITCH_ON")
                End If
            End If
        Else
            SkipLevel0Box.Checked = False
            SkipLevel1Box.Checked = False
            SkipLevel2Box.Checked = False
            SkipLevel3Box.Checked = False
        End If

    End Sub

    Private Sub UpdateUI(ByVal vncMode As IsvControlPanelBuilder.VncMode)

        ' Update the Status Text.
        PrintStatus(vncMode)
        ' Update CycleTime, Feed Rate Override Maximum, Conditional Stop and
        ' Skip Level settings after the VNCK Is booted.
        If vncMode = IsvControlPanelBuilder.VncMode.ProgramsLoaded Then
            UpdateCycleTime()
            UpdateFeedRateOverrideMaximum()
            UpdateFeedRateOverrideValue()
            UpdateConditionalStop()
            UpdateSkipLevels()
        End If
        'Enable/disable UI controls depending on the VncStatus.
        MCP_UIElementsConfiguration(vncMode)
    End Sub

    Private Sub PrintStatus(vncMode As IsvControlPanelBuilder.VncMode)

        Dim color As Drawing.Color
        color = Drawing.Color.Black

        Dim statusText As String
        statusText = String.Empty

        If (isInHistoryBuffer) Then
            statusText = "Simulation is in History Buffer. MCP is disabled."
        Else
            Select Case (vncMode)
                Case IsvControlPanelBuilder.VncMode.Error
                    statusText = "Error"
                Case IsvControlPanelBuilder.VncMode.Notconnected
                    statusText = "Not connected"
                    color = Drawing.Color.Red
                Case IsvControlPanelBuilder.VncMode.Connected
                    statusText = "Connected"
                Case IsvControlPanelBuilder.VncMode.Booted
                    statusText = "Booted"
                Case IsvControlPanelBuilder.VncMode.Configured
                    statusText = "Configured"
                Case IsvControlPanelBuilder.VncMode.Initialized
                    statusText = "Initialized"
                Case IsvControlPanelBuilder.VncMode.ProgramsLoaded
                    statusText = "Programs loaded"
                Case IsvControlPanelBuilder.VncMode.Reset
                    statusText = "NC Reset"
                Case IsvControlPanelBuilder.VncMode.Stop
                    statusText = "NC Stop"
                Case IsvControlPanelBuilder.VncMode.Start
                    statusText = "NC Start"
            End Select
        End If
        StatusTextBox.Text = statusText
        ' Because this text box has the read only flag set we have to set both
        ' colors to get the changed forecolor correctly displayed.
        StatusTextBox.ForeColor = color
        StatusTextBox.BackColor = StatusTextBox.BackColor

    End Sub

    Private Sub MCP_UIElementsConfiguration(ByVal vncMode As IsvControlPanelBuilder.VncMode)

        If (isInHistoryBuffer Or
            vncMode = IsvControlPanelBuilder.VncMode.Connected Or
            vncMode = IsvControlPanelBuilder.VncMode.Booted Or
            vncMode = IsvControlPanelBuilder.VncMode.Configured Or
            vncMode = IsvControlPanelBuilder.VncMode.Initialized) Then

            'Disable all UI Controls when the Simulation is in History Buffer Mode.
            'Or while booting.
            configuredUiControls.ForEach(Sub(elem As Control) elem.Enabled = False)
        ElseIf (vncMode = IsvControlPanelBuilder.VncMode.Notconnected) Then

            configuredUiControls.ForEach(Sub(elem As Control) elem.Enabled = False)
            ShutdownVNCK.Visible = False
            BootVNCK.Visible = True
            BootVNCK.Enabled = True
        Else
            configuredUiControls.ForEach(Sub(elem As Control) elem.Enabled = True)
            ShutdownVNCK.Visible = True
            BootVNCK.Visible = False
            BootVNCK.Enabled = False

            If (vncMode = IsvControlPanelBuilder.VncMode.Start) Then
                configuredUiControls.Where(Function(elem As Control) (elem Is NCPartReset And Not isSimStop) Or
                                                                      elem Is NCSingleBlockMode Or
                                                                      elem Is NCDryRun Or
                                                                      elem Is SaveMachineData Or
                                                                      elem Is ResetMachineData Or
                                                                      (elem Is ConditionalStopBox And Not isSimStop) Or
                                                                      (elem Is SkipLevel0Box And Not isSimStop) Or
                                                                      (elem Is SkipLevel1Box And Not isSimStop) Or
                                                                      (elem Is SkipLevel2Box And Not isSimStop) Or
                                                                      (elem Is SkipLevel3Box And Not isSimStop) Or
                                                                      (elem Is SkipLevelLabel And Not isSimStop)).ToList().ForEach(Sub(e As Control) e.Enabled = False)
            ElseIf (vncMode <> IsvControlPanelBuilder.VncMode.Reset) Then
                SaveMachineData.Enabled = False
            End If
        End If
    End Sub

#Region "callback implementations"
    Private Sub IsInHistoryBufferCallback(ByVal isInHistoryBuffer As Boolean)
        'Set flag and Update UI when History Buffer is entered or left.
        Me.isInHistoryBuffer = isInHistoryBuffer
        UpdateUI(theIsvControlPanelBuilder.VncStatus)
    End Sub

    Private Sub VncStatusCallback(vncMode As IsvControlPanelBuilder.VncMode)
        'Update UI when Vnc Status changed.
        If (vncMode = IsvControlPanelBuilder.VncMode.Start) Then
            isSimStop = False
        End If

        UpdateUI(vncMode)
    End Sub

    Private Sub SimStopCallback()
        'Update UI and set Status Text when Simulation was stopped.
        isSimStop = True
        UpdateUI(theIsvControlPanelBuilder.VncStatus)
        StatusTextBox.Text += " - SIM Stop"
    End Sub
#End Region

    Private Sub MCP_Close(ByVal sender As System.Object, ByVal e As System.Windows.Forms.FormClosingEventArgs) Handles MyBase.FormClosing

        'Disable Alt F4
        If (e.CloseReason = CloseReason.UserClosing) Then
            e.Cancel = True
        End If

    End Sub

    Private Sub NCStart_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCStart.Click

        Dim channels() As String = theIsvControlPanelBuilder.MachineControlGetChannels()
        theIsvControlPanelBuilder.MachineControlStartNc(channels)
        theIsvControlPanelBuilder.PlayForward()
        Erase channels

    End Sub

    Private Sub NCStop_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCStop.Click

        Dim channels() As String = theIsvControlPanelBuilder.MachineControlGetChannels()
        theIsvControlPanelBuilder.MachineControlStopNc(channels)
        Erase channels

    End Sub

    Private Sub NCReset_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCReset.Click

        theIsvControlPanelBuilder.MachineControlResetNc()

    End Sub

    Private Sub NCClearAlarm_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCClearAlarm.Click

        theIsvControlPanelBuilder.MachineControlClearAlarm()

    End Sub

    Private Sub NCSingleBlockMode_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCSingleBlockMode.CheckedChanged

        theIsvControlPanelBuilder.MachineControlSingleBlockMode(NCSingleBlockMode.Checked)

    End Sub

    Private Sub NCDryRun_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCDryRun.CheckedChanged

        theIsvControlPanelBuilder.MachineControlDryRun(NCDryRun.Checked)

    End Sub

    Private Sub NCPartReset_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCPartReset.Click

        theIsvControlPanelBuilder.MachineControlResetPart()

    End Sub

    Private Sub NCFastReset_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCFastReset.Click

        theIsvControlPanelBuilder.MachineControlResetMachine()

    End Sub

    Private Sub SaveMachineData_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SaveMachineData.Click

        theIsvControlPanelBuilder.MachineControlSaveMachineData()

    End Sub

    Private Sub ResetMachineData_Click(sender As Object, e As EventArgs) Handles ResetMachineData.Click

        theIsvControlPanelBuilder.MachineControlResetMachineData()

    End Sub

    Private Sub MCP_KeyDown(ByVal sender As System.Object, ByVal e As System.Windows.Forms.KeyEventArgs) Handles MyBase.KeyDown

        Dim hWndHMI As Long

        'We only consider shift+F10, F10 and F11 to be worth to be forwarded to HMI.
        If e.Shift And e.KeyCode = Keys.F10 OrElse e.KeyCode = Keys.F10 OrElse e.KeyCode = Keys.F11 Then
            'Return the HMI Window (either with vnck 4.4 or vnck 2.6)
            hWndHMI = FindHMIWindow()
        End If

        If (Not hWndHMI.Equals(IntPtr.Zero)) Then

            'Set the HMI Window in focus
            SetForegroundWindow(hWndHMI)

            If e.Shift And e.KeyCode = Keys.F10 Then
                'Switch to the Machine Panel in HMI.
                SendKeys.SendWait("+{F10}")
            ElseIf e.KeyCode = Keys.F10 Then
                'Switch to the main menu in HMI.
                SendKeys.SendWait("{F10}")
            ElseIf e.KeyCode = Keys.F11 Then
                'Switch to the current channel in HMI.
                SendKeys.SendWait("{F11}")
            End If

        End If

    End Sub

    Private Sub MCP_Visibility(sender As Object, e As EventArgs) Handles MyBase.VisibleChanged

        Dim hWndHMI As Long
        'Return the HMI Window (either with vnck 4.4 or vnck 2.6)
        hWndHMI = FindHMIWindow()

        If (Not hWndHMI.Equals(IntPtr.Zero)) Then
            'Make the HMI Window in focus
            SetForegroundWindow(hWndHMI)

            If (Me.Visible = True) Then
                'Restore the HMI Window
                ShowWindow(hWndHMI, SW_SHOWNOACTIVATE)
            Else
                'Minimize the HMI Window
                ShowWindow(hWndHMI, SW_MINIMIZE)
            End If
        End If
    End Sub

    Private Sub BootVNCK_Click(sender As Object, e As EventArgs) Handles BootVNCK.Click
        BootVNCK.Enabled = False
        Cursor.Current = Cursors.WaitCursor
        Try
            StatusTextBox.Text = "Booting"
            theIsvControlPanelBuilder.MachineControlBootVnck()
        Finally
            Cursor.Current = Cursors.Default
            UpdateUI(theIsvControlPanelBuilder.VncStatus)
        End Try
    End Sub

    Private Sub ShutdownVNCK_Click(sender As Object, e As EventArgs) Handles ShutdownVNCK.Click

        Cursor.Current = Cursors.WaitCursor
        MCP_UIElementsConfiguration(IsvControlPanelBuilder.VncMode.Notconnected)
        BootVNCK.Enabled = False
        Try
            theIsvControlPanelBuilder.MachineControlShutdownVnck()
        Finally
            Cursor.Current = Cursors.Default
            UpdateUI(theIsvControlPanelBuilder.VncStatus)
        End Try
    End Sub

    Private Sub FeedRateOverrideEdit_ValueChanged(sender As Object, e As EventArgs) Handles FeedRateOverrideEdit.ValueChanged

        If (Not (IsNothing(theIsvControlPanelBuilder))) Then
            theIsvControlPanelBuilder.MachineControlFeedRateOverride(FeedRateOverrideEdit.Value)
        End If

    End Sub

    Private Sub ConditionalStopBox_CheckedChanged(sender As Object, e As EventArgs) Handles ConditionalStopBox.CheckedChanged

        Dim strValue As String
        If (ConditionalStopBox.Checked) Then
            strValue = "VDI_VARVALUE_SWITCH_ON"
        Else
            strValue = "VDI_VARVALUE_SWITCH_OFF"
        End If

        theIsvControlPanelBuilder.MachineControlWriteVariable(vbNullString,
                                                              "VDI_VARTYPE_ACTIVATE_M1",
                                                              strValue,
                                                              "VDI_SWITCH")

    End Sub

    Private Sub SkipLevel0Box_CheckedChanged(sender As Object, e As EventArgs) Handles SkipLevel0Box.CheckedChanged

        Dim strValue As String
        If (SkipLevel0Box.Checked) Then
            strValue = "VDI_VARVALUE_SWITCH_ON"
        Else
            strValue = "VDI_VARVALUE_SWITCH_OFF"
        End If

        theIsvControlPanelBuilder.MachineControlWriteVariable(vbNullString,
                                                              "VDI_VARTYPE_MODIFY_SKIP",
                                                              strValue,
                                                              "VDI_SWITCH")

    End Sub

    Private Sub SkipLevel1Box_CheckedChanged(sender As Object, e As EventArgs) Handles SkipLevel1Box.CheckedChanged

        Dim strValue As String
        If (SkipLevel1Box.Checked) Then
            strValue = "VDI_VARVALUE_SWITCH_ON"
        Else
            strValue = "VDI_VARVALUE_SWITCH_OFF"
        End If

        theIsvControlPanelBuilder.MachineControlWriteVariable(vbNullString,
                                                              "VDI_VARTYPE_MODIFY_SKIP1",
                                                              strValue,
                                                              "VDI_SWITCH")

    End Sub

    Private Sub SkipLevel2Box_CheckedChanged(sender As Object, e As EventArgs) Handles SkipLevel2Box.CheckedChanged

        Dim strValue As String
        If (SkipLevel2Box.Checked) Then
            strValue = "VDI_VARVALUE_SWITCH_ON"
        Else
            strValue = "VDI_VARVALUE_SWITCH_OFF"
        End If

        theIsvControlPanelBuilder.MachineControlWriteVariable(vbNullString,
                                                              "VDI_VARTYPE_MODIFY_SKIP2",
                                                              strValue,
                                                              "VDI_SWITCH")

    End Sub

    Private Sub SkipLevel3Box_CheckedChanged(sender As Object, e As EventArgs) Handles SkipLevel3Box.CheckedChanged

        Dim strValue As String
        If (SkipLevel3Box.Checked) Then
            strValue = "VDI_VARVALUE_SWITCH_ON"
        Else
            strValue = "VDI_VARVALUE_SWITCH_OFF"
        End If

        theIsvControlPanelBuilder.MachineControlWriteVariable(vbNullString,
                                                              "VDI_VARTYPE_MODIFY_SKIP3",
                                                              strValue,
                                                              "VDI_SWITCH")

    End Sub

End Class
