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
            FeedRateOverrideTrackBar.Value = 100;
            FeedRateOverrideTrackBar.TickFrequency = 10;

            FeedRateOverrideValueLabel.Text = ": " + FeedRateOverrideTrackBar.Value.ToString() + " %";
            FeedRateOverrideMaxLabel.Text = max.ToString();

            //Set the machine control cyle time
            int ipoValue = theIsvControlPanelBuilder.MachineControlGetCycleTime();
            IPO.Text = "IPO: " + ipoValue.ToString() + " ms";
        }

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
