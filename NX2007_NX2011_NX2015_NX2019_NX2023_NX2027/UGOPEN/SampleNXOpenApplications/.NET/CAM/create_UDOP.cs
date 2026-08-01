/*=============================================================================

                    Copyright (c) 2009 Siemens PLM Software 
                    Unpublished - All rights reserved

===============================================================================
 
=============================================================================
File description: Sample NX/Open Application

This is basic example of how to write a UDOP entry in CS
To use this after you build the dll as cs_udop.dll
1) Put the dll in a folder - for example c:\my_udops\
2) Create an system environment variable MYCORP_UDOP_2 and set it to
   c:\my_udops\cs_udop.dll
3) Now in NX CAM create a MILL_USER and in the UI enter MYCORP_UDOP_2
   for the "CAM API Exit Name in the user interface
   press either "User Parameters" or "Generate" to see the results

===============================================================================
*/

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Globalization;
using NXOpen;
using NXOpen.UF;
using NXOpen.UIStyler;

namespace test1
{
    public class Class1
    {

        //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        //       SESSION ATTRIBUTES
        //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        // Native .NET Session
        internal static NXOpen.Session Nts = Session.GetSession();
        // User Function Session
        internal static NXOpen.UF.UFSession Ufs = UFSession.GetUFSession();
        // Native UI Session
        internal static NXOpen.UI Uis = UI.GetUI();
        // Native CAM Session
        internal static NXOpen.CAM.CAMSession Cams = Nts.CAMSession;
        // Native Remote Utilities Session
        internal static NXOpen.RemoteUtilities Rus = RemoteUtilities.GetRemoteUtilities();


        //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        //       SESSION OBJECT ATTRIBUTES
        //''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        // Native Listing Window
        internal static NXOpen.ListingWindow LW = Nts.ListingWindow;
        // Native Message Box
        internal static NXOpen.NXMessageBox MBox = Uis.NXMessageBox;
        // WorkPart
        internal static NXOpen.Part WorkPart = Nts.Parts.Work;

        // ************************************************************************************

        public static void Main()
        {

        }

        public static int udop(string inString)
        {
            IntPtr udopPtr = IntPtr.Zero;
            IntPtr operPtr = IntPtr.Zero;
            UFUdop.Purpose purpose;
            string operName = string.Empty;
            IntPtr pathPtr = IntPtr.Zero;

            Ufs.Udop.AskUdop(IntPtr.Zero, out udopPtr);
            Ufs.Udop.AskOper(udopPtr, out operPtr);
            Ufs.Udop.AskPurpose(udopPtr, out purpose);
            Ufs.Oper.AskName(operPtr, out operName);
            Ufs.Oper.AskPath(operPtr, out pathPtr);

            if (purpose == UFUdop.Purpose.UserParams)
            {
                MBox.Show("User Params", NXMessageBox.DialogType.Information, "User Params");
            }

            if (purpose == UFUdop.Purpose.Generate)
            {
                Ufs.Path.InitToolPath(pathPtr);

                UFPath.LinearMotion linearMotion;
                linearMotion.feed_value = 0;
                linearMotion.type = UFPath.MotionType.MotionTypeCut;
                linearMotion.feed_unit = UFPath.FeedUnit.FeedUnitNone;
                double[] pos = { 0, 0, 0 };
                linearMotion.position = pos;
                double[] tAxis = { 0, 0, 1 };
                linearMotion.tool_axis = tAxis;
                Ufs.Path.CreateLinearMotion(pathPtr, ref linearMotion);

                linearMotion.position[0] = 0;
                linearMotion.position[1] = 0.707;
                linearMotion.position[2] = 0.707;
                linearMotion.tool_axis[0] = 0;
                linearMotion.tool_axis[1] = 1;
                linearMotion.tool_axis[2] = 0;
                Ufs.Path.CreateLinearMotion(pathPtr, ref linearMotion);

                linearMotion.position[0] = 1;
                linearMotion.position[1] = 0;
                linearMotion.position[2] = 0;
                linearMotion.tool_axis[0] = 0;
                linearMotion.tool_axis[1] = 1;
                linearMotion.tool_axis[2] = 1;
                Ufs.Path.CreateLinearMotion(pathPtr, ref linearMotion);

                Ufs.Path.EndToolPath(pathPtr);

            }
            return 0;
        }

        // ************************************************************************************

        public static int GetUnloadOption(string arg)
        {
            return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);
        }
    }
}

