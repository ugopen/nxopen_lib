/*
==============================================================================
 
        Copyright (c) 2017 Siemens Product Lifecycle Management Software Inc.
                         Unpublished - All rights reserved

==============================================================================

 Description
    TODO:


==============================================================================*/
using NXOpen;
using System;

namespace CAMSetupImport
{
    public class MessageUtils
    {
        public static void ShowError(String message)
        {
            NXOpen.UI.GetUI().NXMessageBox.Show("Import CAM Setup", NXMessageBox.DialogType.Error, message);
        }

        public static void AddToLogfile(String message)
        {
            Session.GetSession().LogFile.WriteLine("IMPORT CAM SETUP: " + message);
        }
    }
}
