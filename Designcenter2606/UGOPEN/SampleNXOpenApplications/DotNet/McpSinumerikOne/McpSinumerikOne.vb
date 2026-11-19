
' ==============================================================================
'
'             Copyright (c) 2022  Siemens Industry Software
'                     All rights reserved
'
' ==============================================================================
' ******************************************************************************
'  Description
'    Class that provides the Winforms UI for the Machine Control Panel example
'    for Sinumerik One machine models.
'
'   
'
' ******************************************************************************
Imports System
Imports System.Windows.Forms
Imports System.Linq
Imports NXOpen
Imports NXOpen.SIM

Public Class McpSinumerikOne
    Private Shared theSession As Session
    Private Shared theIsvControlPanelBuilder As SIM.IsvControlPanelBuilder

    Private isInHistoryBufferCallbackId As Integer
    Private vncStatusCallbackId As Integer
    Private simStartCallbackId As Integer
    Private simStopCallbackId As Integer
    Private isInHistoryBuffer = False
    Private isSimStop = False

    ' List of UI elements to toggle their visibility
    Private configuredUiControls As List(Of Control)

    Private Declare Function FindWindow Lib "user32" _
        Alias "FindWindowA" (
        ByVal lpClassName As String,
        ByVal lpWindowName As String) As Long

    Private Declare Function ShowWindow Lib "user32" (
        ByVal hwnd As Integer,
        ByVal nCmdShow As Integer) As Integer

    Private Declare Function SetForegroundWindow Lib "user32" (ByVal hwnd As Long) As Long

    ' The settings that is used in ShowWindow method
    Private Const SW_SHOWNOACTIVATE = 4 'Show Window
    Private Const SW_MINIMIZE = 6 'Minimize Window

    ' Symbolic names of PLC I/O bits used in this file. These are the ones used in the 6.15 templates.
    ' Modify these if different symbolic names are used (check <ncu-dir>\data\public\OfflineData.xml).
    ' When no symbolic names are available, the following format can be used for PLC I/O bits:
    ' PLC.%[IEQA]<byte-address>.<bit>
    ' like PLC.%E0.0
    Private Const PLC_IN_SBLMODE = "PLC.Symbols.mcpIn.singleBlock"
    Private Const PLC_OUT_SBLMODE = "PLC.Symbols.mcpOut.singleBlock"
    Private Const PLC_IN_FEEDRATE_BIT0 = "PLC.Symbols.mcpIn.feedrateOvrA"
    Private Const PLC_IN_FEEDRATE_BIT1 = "PLC.Symbols.mcpIn.feedrateOvrB"
    Private Const PLC_IN_FEEDRATE_BIT2 = "PLC.Symbols.mcpIn.feedrateOvrC"
    Private Const PLC_IN_FEEDRATE_BIT3 = "PLC.Symbols.mcpIn.feedrateOvrD"
    Private Const PLC_IN_FEEDRATE_BIT4 = "PLC.Symbols.mcpIn.feedrateOvrE"
    Private Const PLC_IN_FEEDRATE_START = "PLC.Symbols.mcpIn.feedrateStart"

    ' Table of Gray Codes for Feed Rate Override
    Private ReadOnly grayCodeOf() As Integer =
        {1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28}
    ' The displayed values in the dropdown listbox have to be defined in the 
    ' properties of the UI control.
    ' Gray  Feed Rate  Dropdown
    ' Code  Override   Index
    '  1  =  0%     0
    '  3 =   1%     1
    '  2 =   2%     2
    '  6 =   4%     3
    '  7 =   6%     4
    '  5 =   8%     5
    '  4 =  10%     6
    ' 12 =  20%     7
    ' 13 =  30%     8
    ' 15 =  40%     9
    ' 14 =  50%    10
    ' 10 =  60%    11
    ' 11 =  70%    12
    '  9 =  75%    13
    '  8 =  80%    14
    ' 24 =  85%    15
    ' 25 =  90%    16
    ' 27 =  95%    17
    ' 26 = 100%    18
    ' 30 = 105%    19
    ' 31 = 110%    20
    ' 29 = 115%    21
    ' 28 = 120%    22

    ' Return the HMI Window
    Private Function FindHMIWindow() As Long

        Dim hWndHMI As Long

        'Search HMI window by title for Sinumerik One.
        hWndHMI = FindWindow(vbNullString, "Siemens.Automation.Sinumerik.One.VMx.Open.HMI")

        Return hWndHMI

    End Function

    Protected Overrides Sub Finalize()
        ' Destructor
        If (Not IsDisposed And Not Disposing) Then
            Dispose(True)
        End If
    End Sub

    Private Sub MCPSinumerikOneVB_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        ' Make the displayed window a child of the main NX window
        NXOpenUI.FormUtilities.ReparentForm(Me)

        ' Get the NX session
        theSession = Session.GetSession()

        ' Create the Cam session
        If Not theSession.IsCamSessionInitialized() Then
            theSession.CreateCamSession()
        End If

        'Get the KinematicConfigurator
        Dim workPart As Part = theSession.Parts.Work
        Dim kinematicConfigurator As SIM.KinematicConfigurator = workPart.KinematicConfigurator

        ' Get the IsvControlPanelBuilder
        theIsvControlPanelBuilder = kinematicConfigurator.IsvControlPanelBuilder

        '#Region "insert ui controls"
        ' Collect all UI Controls to toggle enable/disable.
        configuredUiControls = New List(Of Control) From {
            NCStart,
            NCStop,
            NCReset,
            FeedRateOverrideTitle,
            FeedRateOverrideEdit,
            SaveMachineData,
            ResetMachineData,
            NCSingleBlockMode,
            NCPartReset,
            BootVNCK,
            ShutdownVNCK
        }
        '#End Region

        ' Add callback to get notified when the history buffer is entered or left.
        isInHistoryBufferCallbackId = theIsvControlPanelBuilder.AddIsInHistoryBuffer(New IsvControlPanelBuilder.IsInHistoryBufferCb(AddressOf IsInHistoryBufferCallback))

        ' Add callback to get notified when the VncStatus changed.
        vncStatusCallbackId = theIsvControlPanelBuilder.AddVncStatus(New IsvControlPanelBuilder.VncStatusCb(AddressOf VncStatusCallback))

        ' Add callback to get notified when the Simulation is started after a freeze.
        simStartCallbackId = theIsvControlPanelBuilder.AddSimStart(New IsvControlPanelBuilder.SimStartCb(AddressOf SimStartCallback))

        ' Add callback to get notified when the Simulation is frozen.
        simStopCallbackId = theIsvControlPanelBuilder.AddSimStop(New IsvControlPanelBuilder.SimStopCb(AddressOf SimStopCallback))

        SyncMcpAndMyVirtualMachine()

    End Sub

    Private Sub MCPSinumerikOneVB_Disposed(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Disposed
        ' Remove all callbacks.
        theIsvControlPanelBuilder.RemoveIsInHistoryBuffer(isInHistoryBufferCallbackId)
        theIsvControlPanelBuilder.RemoveVncStatus(vncStatusCallbackId)
        theIsvControlPanelBuilder.RemoveSimStart(simStartCallbackId)
        theIsvControlPanelBuilder.RemoveSimStop(simStopCallbackId)
    End Sub

    Private Sub UpdateCycleTime()
        Dim ipoValue As Integer = theIsvControlPanelBuilder.MachineControlGetCycleTime
        IPO.Text = "IPO: " + ipoValue.ToString() + " ms"

    End Sub

    Private Sub UpdateFeedRateOverrideValue()
        If (IsNothing(theIsvControlPanelBuilder)) Then
            Return
        End If

        Dim nGrayCode As Integer
        nGrayCode = 0
        GetFeedRateOverride(nGrayCode)

        If (Not (nGrayCode = 0)) Then
            ' Seek the appropriate index and select it.
            If (grayCodeOf.Contains(nGrayCode)) Then
                For i = 0 To grayCodeOf.Count() - 1
                    If (grayCodeOf.GetValue(i) = nGrayCode) Then
                        FeedRateOverrideEdit.SelectedIndex = i
                        FeedRateOverrideEdit.Invalidate()
                    End If
                Next
            End If
        End If
    End Sub

    Private Sub UpdateUI(ByVal vncMode As IsvControlPanelBuilder.VncMode)

        ' Update the Status Text.
        PrintStatus(vncMode)
        ' Enable/disable UI controls depending on the VncStatus.
        MCPSinumerikOneVB_UIElementsConfiguration(vncMode)
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
        ' colors to get the changed foreground color correctly displayed.
        StatusTextBox.ForeColor = color
        StatusTextBox.BackColor = StatusTextBox.BackColor
        StatusTextBox.Invalidate()
        StatusTextBox.Update()

    End Sub

    Private Sub MCPSinumerikOneVB_UIElementsConfiguration(ByVal vncMode As IsvControlPanelBuilder.VncMode)

        If (isInHistoryBuffer Or
            vncMode = IsvControlPanelBuilder.VncMode.Connected Or
            vncMode = IsvControlPanelBuilder.VncMode.Booted Or
            vncMode = IsvControlPanelBuilder.VncMode.Configured Or
            vncMode = IsvControlPanelBuilder.VncMode.Initialized) Then
            ' Disable all UI Controls when the simulation is in history buffer mode
            ' or while booting.
            configuredUiControls.ForEach(Sub(elem As Control) elem.Enabled = False)
        ElseIf (vncMode = IsvControlPanelBuilder.VncMode.Notconnected) Then
            ' If not yet connected disable all except the boot button and hide
            ' the shutdown button
            configuredUiControls.ForEach(Sub(elem As Control) elem.Enabled = False)
            ShutdownVNCK.Visible = False
            BootVNCK.Visible = True
            BootVNCK.Enabled = True
        Else
            ' In all other cases enable all controls except the boot button and
            ' hide the boot button but show the shutdown button.
            configuredUiControls.ForEach(Sub(elem As Control) elem.Enabled = True)
            ShutdownVNCK.Visible = True
            BootVNCK.Visible = False
            BootVNCK.Enabled = False

            NCPartReset.Enabled = isSimStop

            ' If simulation has started disable Reset Machine Data.
            If (vncMode = IsvControlPanelBuilder.VncMode.Start) Then
                ResetMachineData.Enabled = False
            End If

            ' If status is not Reset disable Save Machine Data.
            If (vncMode <> IsvControlPanelBuilder.VncMode.Reset) Then
                SaveMachineData.Enabled = False
            End If
        End If
    End Sub

#Region "callback implementations"
    Private Sub IsInHistoryBufferCallback(ByVal isInHistoryBuffer As Boolean)
        ' Set flag and Update UI when History Buffer is entered or left.
        Me.isInHistoryBuffer = isInHistoryBuffer
        UpdateUI(theIsvControlPanelBuilder.VncStatus)
    End Sub

    Private Sub VncStatusCallback(vncMode As IsvControlPanelBuilder.VncMode)
        ' Update UI when VNC Status changed.
        If (vncMode = IsvControlPanelBuilder.VncMode.Start) Then
            isSimStop = False
        End If

        UpdateUI(vncMode)
    End Sub

    Private Sub SimStartCallback()
        ' Update UI when Simulation is continued.
        If (isSimStop) Then
            isSimStop = False
            UpdateUI(theIsvControlPanelBuilder.VncStatus)
        End If
    End Sub

    Private Sub SimStopCallback()
        ' Update UI and set Status Text when Simulation was stopped.
        isSimStop = True
        UpdateUI(theIsvControlPanelBuilder.VncStatus)
        StatusTextBox.Text += " - SIM Stop"
        StatusTextBox.Invalidate()
        StatusTextBox.Update()
    End Sub
#End Region

    Private Sub MCPSinumerikOneVB_Close(ByVal sender As System.Object, ByVal e As System.Windows.Forms.FormClosingEventArgs) Handles MyBase.FormClosing

        ' Disable Alt F4
        If (e.CloseReason = CloseReason.UserClosing) Then
            e.Cancel = True
        End If

    End Sub

    Private Sub NCStart_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCStart.Click

        Dim vncMode As IsvControlPanelBuilder.VncMode = theIsvControlPanelBuilder.VncStatus

        ' When the controller starts running, PlayForward is triggered automatically.
        ' If the controller is already running, StartNc doesn't need to be executed so PlayForward should be called directly.
        If (vncMode <> IsvControlPanelBuilder.VncMode.Start And vncMode <> IsvControlPanelBuilder.VncMode.Run) Then
            theIsvControlPanelBuilder.MachineControlStartNc()
        Else
            theIsvControlPanelBuilder.PlayForward()
        End If

    End Sub

    Private Sub NCStop_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCStop.Click

        theIsvControlPanelBuilder.MachineControlStopNc()

    End Sub

    Private Sub NCReset_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCReset.Click

        theIsvControlPanelBuilder.MachineControlResetNc()

    End Sub

    Private Sub NCSingleBlockMode_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCSingleBlockMode.CheckedChanged

        Dim singleBlockOn = ReadPlcBit(PLC_OUT_SBLMODE)

        If (NCSingleBlockMode.Checked Xor singleBlockOn) Then
            PulsePlcBit(PLC_IN_SBLMODE, True)
        End If

    End Sub

    Private Sub NCPartReset_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles NCPartReset.Click

        theIsvControlPanelBuilder.MachineControlResetPart()

    End Sub

    Private Sub SaveMachineData_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles SaveMachineData.Click

        theIsvControlPanelBuilder.MachineControlSaveMachineData()

        ' PLC was rebooted, PLC I/Os can have changed
        SyncMcpAndMyVirtualMachine()

    End Sub

    Private Sub ResetMachineData_Click(sender As Object, e As EventArgs) Handles ResetMachineData.Click

        theIsvControlPanelBuilder.MachineControlResetMachineData()

        ' As the machine is now freshly booted we need to do this again.
        SyncMcpAndMyVirtualMachine()

    End Sub

    Private Sub MCPSinumerikOneVB_KeyDown(ByVal sender As System.Object, ByVal e As System.Windows.Forms.KeyEventArgs) Handles MyBase.KeyDown

        Dim hWndHMI As Long

        ' We only consider shift+F10, F10 and F11 to be worth to be forwarded to HMI.
        If e.Shift And e.KeyCode = Keys.F10 OrElse e.KeyCode = Keys.F10 OrElse e.KeyCode = Keys.F11 Then
            ' Return the HMI Window
            hWndHMI = FindHMIWindow()
        End If

        If (Not hWndHMI.Equals(IntPtr.Zero)) Then

            ' Set the focus on the HMI window
            SetForegroundWindow(hWndHMI)

            If e.Shift And e.KeyCode = Keys.F10 Then
                ' Switch to the Machine Panel in HMI.
                SendKeys.SendWait("+{F10}")
            ElseIf e.KeyCode = Keys.F10 Then
                ' Switch to the main menu in HMI.
                SendKeys.SendWait("{F10}")
            ElseIf e.KeyCode = Keys.F11 Then
                ' Switch to the current channel in HMI.
                SendKeys.SendWait("{F11}")
            End If

        End If

    End Sub

    Private Sub MCPSinumerikOneVB_Visibility(sender As Object, e As EventArgs) Handles MyBase.VisibleChanged

        Dim hWndHMI As Long
        ' Return the HMI Window
        hWndHMI = FindHMIWindow()

        If (Not hWndHMI.Equals(IntPtr.Zero)) Then
            ' Set the focus on the HMI window
            SetForegroundWindow(hWndHMI)

            If (Me.Visible = True) Then
                ' Restore the HMI Window
                ShowWindow(hWndHMI, SW_SHOWNOACTIVATE)
            Else
                ' Minimize the HMI Window
                ShowWindow(hWndHMI, SW_MINIMIZE)
            End If
        End If
    End Sub

    Private Sub BootVNCK_Click(sender As Object, e As EventArgs) Handles BootVNCK.Click
        BootVNCK.Enabled = False
        Cursor.Current = Cursors.WaitCursor
        Try
            StatusTextBox.Text = "Booting"
            StatusTextBox.Invalidate()
            StatusTextBox.Update()

            theIsvControlPanelBuilder.MachineControlBootVnck()
        Finally
            Cursor.Current = Cursors.Default

            SyncMcpAndMyVirtualMachine()

        End Try
    End Sub

    Private Sub SyncMcpAndMyVirtualMachine()
        ' Update CycleTime after the Sinumerik One Is booted.
        UpdateCycleTime()

        UpdateFeedRateOverrideValue()

        Dim currentStatus As IsvControlPanelBuilder.VncMode = theIsvControlPanelBuilder.VncStatus

        If (currentStatus >= IsvControlPanelBuilder.VncMode.ProgramsLoaded) Then
            NCSingleBlockMode.Checked = ReadPlcBit(PLC_OUT_SBLMODE)
        End If

        UpdateUI(currentStatus)
    End Sub

    Private Sub ShutdownVNCK_Click(sender As Object, e As EventArgs) Handles ShutdownVNCK.Click

        Cursor.Current = Cursors.WaitCursor
        MCPSinumerikOneVB_UIElementsConfiguration(IsvControlPanelBuilder.VncMode.Notconnected)
        BootVNCK.Enabled = False
        Try
            theIsvControlPanelBuilder.MachineControlShutdownVnck()
        Finally
            Cursor.Current = Cursors.Default
            UpdateUI(theIsvControlPanelBuilder.VncStatus)
        End Try
    End Sub

    Private Sub FeedRateOverrideEdit_SelectedIndexChanged(sender As Object, e As EventArgs) Handles FeedRateOverrideEdit.SelectedIndexChanged

        SetFeedRateOverride(grayCodeOf.GetValue(FeedRateOverrideEdit.SelectedIndex))

    End Sub

    Private Sub SetFeedRateOverride(ByVal nGrayCode As Integer)

        If (IsNothing(theIsvControlPanelBuilder)) Then
            Return
        End If

        WritePlcBit(PLC_IN_FEEDRATE_BIT0, (nGrayCode And 1) = 1)
        WritePlcBit(PLC_IN_FEEDRATE_BIT1, (nGrayCode And 2) = 2)
        WritePlcBit(PLC_IN_FEEDRATE_BIT2, (nGrayCode And 4) = 4)
        WritePlcBit(PLC_IN_FEEDRATE_BIT3, (nGrayCode And 8) = 8)
        WritePlcBit(PLC_IN_FEEDRATE_BIT4, (nGrayCode And 16) = 16)
        PulsePlcBit(PLC_IN_FEEDRATE_START, True)

    End Sub
    Private Sub GetFeedRateOverride(ByRef nGrayCode As Integer)

        If (IsNothing(theIsvControlPanelBuilder)) Then
            Return
        End If

        nGrayCode = 0

        If (ReadPlcBit(PLC_IN_FEEDRATE_BIT0)) Then
            nGrayCode = 1
        End If

        If (ReadPlcBit(PLC_IN_FEEDRATE_BIT1)) Then
            nGrayCode += 2
        End If

        If (ReadPlcBit(PLC_IN_FEEDRATE_BIT2)) Then
            nGrayCode += 4
        End If

        If (ReadPlcBit(PLC_IN_FEEDRATE_BIT3)) Then
            nGrayCode += 8
        End If

        If (ReadPlcBit(PLC_IN_FEEDRATE_BIT4)) Then
            nGrayCode += 16
        End If

    End Sub

    Private Sub WritePlcBit(plcIoAddress As String, value As Boolean)
        ' PLC IOs are channel independent - just provide a non-empty string as channel
        ' to make sure this is executed only once.
        ' (Nothing or "" would execute it once for each channel that exist e.g. twice for a 2-channel-machine)
        '
        ' The variable type is ignored here as the variable type can be derived from the address
        theIsvControlPanelBuilder.MachineControlWriteVariable("ANY",
                                                              plcIoAddress,
                                                              value,
                                                              "")
    End Sub

    Private Sub PulsePlcBit(plcIoAddress As String, value As Boolean)
        ' PLC IOs are channel independent - just provide a non-empty string as channel
        ' to make sure this is executed only once.
        ' (Nothing or "" would execute it once for each channel that exist e.g. twice for a 2-channel-machine)
        '
        ' The variable type "PLC_PULSE_SIGNAL" causes an automatic reset of this PLC IO address
        ' to the previous value after one OB1 cycle.
        theIsvControlPanelBuilder.MachineControlWriteVariable("ANY",
                                                              plcIoAddress,
                                                              value,
                                                              "PLC_PULSE_SIGNAL")
    End Sub

    Private Function ReadPlcBit(plcIoAddress As String) As Boolean

        Dim strValue As String
        strValue = ""
        Dim strType As String
        strType = ""

        ' PLC IOs are channel independent - just provide a non-empty string as channel
        ' to make sure this is executed only once.
        ' (Nothing or "" would execute it once for each channel that exist e.g. twice for a 2-channel-machine)
        If (theIsvControlPanelBuilder.MachineControlReadVariable("ANY",
                                                                 plcIoAddress,
                                                                 strValue,
                                                                 strType)) Then
            Return strValue.ToUpper() = "TRUE"
        End If

        Return False

    End Function


End Class
