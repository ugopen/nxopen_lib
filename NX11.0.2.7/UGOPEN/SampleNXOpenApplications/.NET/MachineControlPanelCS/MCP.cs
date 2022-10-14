/*
 ==============================================================================

             Copyright (c) 2013  UGS PLM Solutions
               Unpublished - All rights reserved

 ==============================================================================
 ******************************************************************************
  Description
    Class that provides the Winforms UI for the Machine Control Panel example

 */

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

using NXOpen;
using NXOpen.SIM;

namespace MCP_CSharp
{
    public partial class MCP : Form
    {
        private static Session theSession;
        private static IsvControlPanelBuilder theIsvControlPanelBuilder;

        private int isInHistoryBufferCallbackId;
        private int vncStatusCallbackId;
        private int simStopCallbackId;
        private bool isInHistoryBuffer = false;
        private bool isSimStop = false;
        //list of ui elements to toggle their visibility
        private List<Control> configuredUiControls;

        [DllImport("user32.dll")]
        private static extern IntPtr FindWindow(string strclassName, string strWindowName);

        [DllImport("user32.dll")]
        private static extern bool ShowWindow(IntPtr hwnd, int nCmdShow);

        //The settings that is used in ShowWindow method
        private const int SW_SHOWNOACTIVATE = 4; //Show Window
        private const int SW_MINIMIZE = 6;       //Minimize Window

        [DllImport("User32.dll")]
        static extern long SetForegroundWindow(IntPtr hwnd);

        //Return the HMI Window (either with vnck 4.4 or vnck 2.6)
        private static IntPtr FindHMIWindow()
        {
            IntPtr hWndHMI = IntPtr.Zero;

            //Search HMI window by title for Operate with VNCK 4.4.
            hWndHMI = FindWindow(null, "SINUMERIK Operate - Window Mode");

            //If VNCK 4.4 HMI window not founded then search VNCK 2.6 HMI window.
            if (hWndHMI == IntPtr.Zero)
                hWndHMI = FindWindow(null, "HMI SolutionLine - Window Mode");

            return hWndHMI;
        }

        public MCP()
        {
            InitializeComponent();
        }

        ~MCP()
        {
            if (!IsDisposed && !Disposing)
            {
                Dispose(true);
            }
        }

        private void MCP_Load(object sender, EventArgs e)
        {
            // Make the displayed window a child of the main NX window
            NXOpenUI.FormUtilities.ReparentForm(this);

            //Get the NX session
            theSession = Session.GetSession();

            //Create the Cam session
            theSession.CreateCamSession();

            //Get the KinematicConfigurator
            Part workPart = theSession.Parts.Work;
            KinematicConfigurator theKinematicConfigurator = workPart.KinematicConfigurator;

            //Get the IsvControlPanelBuilder
            theIsvControlPanelBuilder = theKinematicConfigurator.IsvControlPanelBuilder;

            //Set the Feed Rate Override maximum value
            int max = theIsvControlPanelBuilder.MachineControlGetFeedRateOverrideMaximumValue();
            FeedRateOverrideTrackBar.SetRange(0, max);
            FeedRateOverrideTrackBar.Value = Math.Min(100, max);
            FeedRateOverrideTrackBar.TickFrequency = 10;

            FeedRateOverrideValueLabel.Text = ": " + FeedRateOverrideTrackBar.Value.ToString() + " %";
            FeedRateOverrideMaxLabel.Text = max.ToString();

            //Set the machine control cyle time
            int ipoValue = theIsvControlPanelBuilder.MachineControlGetCycleTime();
            IPO.Text = "IPO: " + ipoValue.ToString() + " ms";

            #region insert ui controls
            //Collect all UI Controls to toggle enable/disable.
            configuredUiControls = new List<Control>(){
                NCStart,
                NCStop,
                NCReset,
                FeedRateOverrideTrackBar,
                SaveMachineData,
                ResetMachineData,
                NCDryRun,
                NCSingleBlockMode,
                NCClearAlarm,
                NCPartReset,
                NCFastReset,
                BootVNCK,
                ShutdownVNCK
            };
            #endregion

            //Add callback to get notified when the Historybuffer is entered or left.
            isInHistoryBufferCallbackId = theIsvControlPanelBuilder.AddIsInHistoryBuffer(new NXOpen.SIM.IsvControlPanelBuilder.IsInHistoryBufferCb(IsInHistoryBufferCallback));
            
            //Add callback to get notified when the VncStatus changed.
            vncStatusCallbackId = theIsvControlPanelBuilder.AddVncStatus(new NXOpen.SIM.IsvControlPanelBuilder.VncStatusCb(VncStatusCallback));

            //Add callback to get notified when the Simulation is freezed.
            simStopCallbackId = theIsvControlPanelBuilder.AddSimStop(new NXOpen.SIM.IsvControlPanelBuilder.SimStopCb(SimStopCallback));

            //Add Disposed Handler to remove the added callbacks.
            base.Disposed += MCP_Disposed;

            //Update UI to show the current Vnc Status.
            UpdateUI(theIsvControlPanelBuilder.VncStatus);
        }

        private void MCP_Disposed(object sender, EventArgs e)
        {
            //Remove all callbacks.
            theIsvControlPanelBuilder.RemoveIsInHistoryBuffer(isInHistoryBufferCallbackId);
            theIsvControlPanelBuilder.RemoveVncStatus(vncStatusCallbackId);
            theIsvControlPanelBuilder.RemoveSimStop(simStopCallbackId);
        }

        private void UpdateUI(IsvControlPanelBuilder.VncMode vncMode)
        {
            //Update the Status Text.
            PrintStatus(vncMode);
            //Enable/disable UI controls depending on the Vnc Status.
            MCP_UIElementsConfiguration(vncMode);
        }

        private void PrintStatus(IsvControlPanelBuilder.VncMode vncMode)
        {
            String statusText = String.Empty;

            if (isInHistoryBuffer)
            {
                statusText = "Simulation is in History Buffer. MCP is disabled.";
            }
            else
            {
                switch (vncMode)
                {
                    case IsvControlPanelBuilder.VncMode.Error:
                        statusText = "Error";
                        break;

                    case IsvControlPanelBuilder.VncMode.Notconnected:
                        statusText = "Not connected";
                        break;

                    case IsvControlPanelBuilder.VncMode.Connected:
                        statusText = "Connected";
                        break;

                    case IsvControlPanelBuilder.VncMode.Booted:
                        statusText = "Booted";
                        break;

                    case IsvControlPanelBuilder.VncMode.Configured:
                        statusText = "Configured";
                        break;

                    case IsvControlPanelBuilder.VncMode.Initialized:
                        statusText = "Initialized";
                        break;

                    case IsvControlPanelBuilder.VncMode.ProgramsLoaded:
                        statusText = "Programs loaded";
                        break;

                    case IsvControlPanelBuilder.VncMode.Reset:
                        statusText = "NC Reset";
                        break;

                    case IsvControlPanelBuilder.VncMode.Stop:
                        statusText = "NC Stop";
                        break;

                    case IsvControlPanelBuilder.VncMode.Start:
                        statusText = "NC Start";
                        break;

                    default:
                        statusText = "other " + vncMode;
                        break;
                }
            }

            StatusTextBox.Text = statusText;
        }

        private void MCP_UIElementsConfiguration(IsvControlPanelBuilder.VncMode vncMode)
        {
            if (isInHistoryBuffer 
                || vncMode == IsvControlPanelBuilder.VncMode.Connected
                || vncMode == IsvControlPanelBuilder.VncMode.Booted
                || vncMode == IsvControlPanelBuilder.VncMode.Configured
                || vncMode == IsvControlPanelBuilder.VncMode.Initialized)
            {
                //Disable all UI Controls when the Simulation is in History Buffer Mode.
                //Or while booting.
                configuredUiControls.ForEach(elem => elem.Enabled = false);
            }
            else if(vncMode == IsvControlPanelBuilder.VncMode.Notconnected)
            {
                configuredUiControls.ForEach(elem => elem.Enabled = false);
                ShutdownVNCK.Visible = false;
                BootVNCK.Visible = true;
                BootVNCK.Enabled = true;
            }
            else
            {
                configuredUiControls.ForEach(elem => elem.Enabled = true);
                ShutdownVNCK.Visible = true;
                BootVNCK.Visible = false;
                BootVNCK.Enabled = false;
                
                if (vncMode == IsvControlPanelBuilder.VncMode.Start)
                {
                    configuredUiControls.Where(elem =>
                    (elem == NCPartReset && !isSimStop)||
                    elem == NCSingleBlockMode ||
                    elem == NCDryRun ||
                    elem == SaveMachineData ||
                    elem == ResetMachineData).ToList().ForEach(e => e.Enabled = false);
                }
                else if (vncMode != IsvControlPanelBuilder.VncMode.Reset)
                {
                    SaveMachineData.Enabled = false;
                }
            }
        }

        #region callback implementations
        private void IsInHistoryBufferCallback(bool isInHistoryBuffer)
        {
            //Set flag and Update UI when History Buffer is entered or left.
            this.isInHistoryBuffer = isInHistoryBuffer;
            UpdateUI(theIsvControlPanelBuilder.VncStatus);
        }

        private void VncStatusCallback(IsvControlPanelBuilder.VncMode vncMode)
        {
            //Update UI when Vnc Status changed.
            if (vncMode == IsvControlPanelBuilder.VncMode.Start)
            {
                isSimStop = false;
            }

            UpdateUI(vncMode);
        }

        private void SimStopCallback()
        {
            //Update UI and set Status Text when Simulation was stopped.
            isSimStop = true;
            UpdateUI(theIsvControlPanelBuilder.VncStatus);
            StatusTextBox.Text += " - SIM Stop";
        }
        #endregion

        private void MCP_Close(object sender, FormClosingEventArgs e)
        {
            //Disable Alt F4
            if (e.CloseReason == CloseReason.UserClosing)
                e.Cancel = true;
        }

        private void NCStart_Click(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlStartNc();
            theIsvControlPanelBuilder.PlayForward();
        }

        private void NCStop_Click(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlStopNc();
        }

        private void NCReset_Click(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlResetNc();
        }

        private void NCClearAlarm_Click(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlClearAlarm();
        }

        private void NCSingleBlockMode_CheckedChanged(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlSingleBlockMode(NCSingleBlockMode.Checked);
        }

        private void NCDryRun_CheckedChanged(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlDryRun(NCDryRun.Checked);
        }

        private void NCPartReset_Click(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlResetPart();
        }

        private void NCFastReset_Click(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlResetMachine();
        }

        private void SaveMachineData_Click(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlSaveMachineData();
        }

        private void ResetMachineData_Click(object sender, EventArgs e)
        {
            theIsvControlPanelBuilder.MachineControlResetMachineData();
        }

        private void BootVNCK_Click(object sender, EventArgs e)
        {
            BootVNCK.Enabled = false;
            Cursor.Current = Cursors.WaitCursor;
            try
            {
                theIsvControlPanelBuilder.MachineControlBootVnck();
            }
            finally
            {
                Cursor.Current = Cursors.Default;
                UpdateUI(theIsvControlPanelBuilder.VncStatus);
            }
        }

        private void ShutdownVNCK_Click(object sender, EventArgs e)
        {
            Cursor.Current = Cursors.WaitCursor;
            MCP_UIElementsConfiguration(IsvControlPanelBuilder.VncMode.Notconnected);
            BootVNCK.Enabled = false;
            try
            {
                theIsvControlPanelBuilder.MachineControlShutdownVnck();
            }
            finally
            {
                Cursor.Current = Cursors.Default;
                UpdateUI(theIsvControlPanelBuilder.VncStatus);
            }
        }

        private void FeedRateOverrideTrackBar_Scroll(object sender, EventArgs e)
        {
            FeedRateOverrideValueLabel.Text = ": " + FeedRateOverrideTrackBar.Value.ToString() + " %";
            theIsvControlPanelBuilder.MachineControlFeedRateOverride(FeedRateOverrideTrackBar.Value);
        }

        private void MCP_KeyDown(object sender, KeyEventArgs e)
        {
            IntPtr hWndHMI = IntPtr.Zero;

            //We only consider shift+F10, F10 and F11 to be worth to be forwarded to HMI.
            if ((e.KeyCode == Keys.Shift && e.KeyCode == Keys.F10) || (e.KeyCode == Keys.F10) || (e.KeyCode == Keys.F11))
            {
                //Return the HMI Window (either with vnck 4.4 or vnck 2.6)
                hWndHMI = FindHMIWindow();

                if(hWndHMI != IntPtr.Zero)
                {
                    //Set the HMI Window in focus
                    SetForegroundWindow(hWndHMI);

                    if (e.KeyCode == Keys.Shift && e.KeyCode == Keys.F10)
                    {
                        //Switch to the Machine Panel in HMI.
                        SendKeys.SendWait("+{F10}");
                    }
                    else if (e.KeyCode == Keys.F10)
                    {
                        //Switch to the main menu in HMI.
                        SendKeys.SendWait("{F10}");
                    }
                    else
                    {
                        //Switch to the current channel in HMI.
                        SendKeys.SendWait("{F11}");
                    }
                }
            }
        }

        private void MCP_Visibility(object sender, EventArgs e)
        {
            IntPtr hWndHMI = FindHMIWindow();

            if(hWndHMI != IntPtr.Zero)
            {
                //Make the HMI Window in focus
                SetForegroundWindow(hWndHMI);

                if (this.Visible == true)
                {
                    //Restore the HMI Window
                    ShowWindow(hWndHMI, SW_SHOWNOACTIVATE);
                }
                else
                {
                    //Minimize the HMI Window
                    ShowWindow(hWndHMI, SW_MINIMIZE);
                }
            }
        }
    }
}
