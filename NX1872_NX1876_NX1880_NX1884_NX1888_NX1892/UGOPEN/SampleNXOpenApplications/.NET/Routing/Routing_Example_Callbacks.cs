/*==================================================================================================
               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A C# class that implements example Routing callbacks.


==================================================================================================*/
using System;
using NXOpen;
using NXOpen.Routing;
using NXOpen.Routing.Electrical;

namespace Routing
{
    public class Callbacks
    {
        // Static class members
        static Session theSession = null;
        static ListingWindow listingWindow = null;

        //------------------------------------------------------------------------------------------
        // Called when NX starts up to register the callbacks.
        public static int Startup()
        {

            if (theSession == null)
                theSession = Session.GetSession();

            if (listingWindow == null)
                listingWindow = theSession.ListingWindow;

            RegisterCallbacks();

            return 0;
        }

        //------------------------------------------------------------------------------------------
        // Called from File->Execute->NX Open. Useful for testing.
        public static void Main()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (listingWindow == null)
                listingWindow = theSession.ListingWindow;

            RegisterCallbacks();
        }

        //------------------------------------------------------------------------------------------
        // Called by both Main and Startup to register the callbacks.
        private static void RegisterCallbacks()
        {
            CustomManager customManager = theSession.RouteCustomManager;

            customManager.AddCallback(CustomManager.CallbackReason.WireRouteAuto, AutorouteCallback);
            customManager.AddCallback(CustomManager.CallbackReason.WireUnroute, UnrouteCallback);
        }

        //------------------------------------------------------------------------------------------
        public static void AutorouteCallback
        (
            NXObject[] nxObjects
        )
        {
            Echo("\n*** C# AutorouteCallback called with " + nxObjects.Length.ToString() + " objects.");

            foreach (NXObject nxObject in nxObjects)
            {
                if (nxObject.GetType() != typeof(WireDevice))
                {
                    Echo("  NX Object (Tag " + nxObject.Tag.ToString() + ") is NOT a Wire Device.");
                    continue;
                }

                WireDevice wireDevice = (WireDevice)nxObject;

                Echo("  Wire Device (Tag " + wireDevice.Tag.ToString() + ") named " + wireDevice.Name + ".");
            }

            Echo("");
        }

        //------------------------------------------------------------------------------------------
        public static void UnrouteCallback
        (
            NXObject[] nxObjects
        )
        {
            Echo("\n*** C# UnrouteCallback called with " + nxObjects.Length.ToString() + " objects.");

            foreach (NXObject nxObject in nxObjects)
            {
                if (nxObject.GetType() != typeof(WireDevice))
                {
                    Echo("  NX Object (Tag " + nxObject.Tag.ToString() + ") is NOT a Wire Device.");
                    continue;
                }

                WireDevice wireDevice = (WireDevice)nxObject;

                Echo("  Wire Device (Tag " + wireDevice.Tag.ToString() + ") named " + wireDevice.Name + ".");
            }

            Echo("");
        }

        //------------------------------------------------------------------------------------------
        // Writes the given string to the Listing Window and the syslog.
        //
        // \param[in]
        //      stringToWrite
        //          The string to write.
        private static void Echo
        (
            string message
        )
        {
            if (!listingWindow.IsOpen)
                listingWindow.Open();

            listingWindow.WriteFullline(message);

            LogFile syslog = theSession.LogFile;
            syslog.WriteLine(message);
        }

        //------------------------------------------------------------------------------------------
        // Tells NX when to unload your application.
        // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
        public static int GetUnloadOption(string arg)
        {
            return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
        }
    }
}
