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

    A C# class that implements example Routing plugins.


==================================================================================================*/
using System;
using System.Windows.Forms;
using NXOpen;
using NXOpen.Preferences;
using NXOpen.Routing;
using NXOpen.Routing.Electrical;
using System.Collections.Generic;
using NXOpen.Utilities;

namespace Routing
{
    public class Plugins
    {
        // Static class members
        static Session theSession = null;
        static ListingWindow listingWindow = null;
        static CustomManager customManager = null;

        //------------------------------------------------------------------------------------------
        // Called when NX starts up to register the plugins.
        public static int Startup()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (listingWindow == null)
                listingWindow = theSession.ListingWindow;

            if (customManager == null)
                customManager = theSession.RouteCustomManager;

            RegisterPlugins();

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

            if (customManager == null)
                customManager = theSession.RouteCustomManager;

            RegisterPlugins();
        }

        //------------------------------------------------------------------------------------------
        // Called by both Main and Startup to register the plugins.
        private static void RegisterPlugins()
        {
            customManager.SetHrnPreImportPlugin(ImportExportPlugin);
            customManager.SetHrnPostExportPlugin(ImportExportPlugin);
            customManager.SetCmpPreImportPlugin(ImportExportPlugin);
            customManager.SetCmpPostExportPlugin(ImportExportPlugin);
            customManager.SetPlmXmlPreImportPlugin(ImportExportPlugin);
            customManager.SetPlmXmlPostExportPlugin(ImportExportPlugin);
            customManager.SetPlmXmlRouteNodeNamePlugin(RouteNodeNamePlugin);
            customManager.SetPlmXmlRouteSectionNamePlugin(RouteSectionNamePlugin);
            customManager.SetWrappedOverstockLengthCalculationPlugin(WrappedOverstockLengthCalculationPlugin);
            customManager.SetFilterBlankingPlugin(FilterBlankingPlugin);
            customManager.SetBomPlugin(BomPlugin);
            customManager.SetAutoRoutePlugin(AutoRoutePlugin);
            customManager.SetManualRoutePlugin(ManualRoutePlugin);
            customManager.SetUnroutePlugin(UnroutePlugin);
            customManager.SetNavigatorObjectSelectedPlugin(NavigatorObjectSelectedPlugin);
            customManager.SetValidateFormboardPlugin(ValidateFormboardPlugin);
            customManager.SetDisciplineChangedPlugin(DisciplineChangedPlugin);
            customManager.SetSpecificationChangedPlugin(SpecificationChangedPlugin);
            customManager.SetSortConnectionsPlugin(SortConnectionsPlugin);
            customManager.SetChoosePartPlugin(ChoosePartPlugin);
        }

        //------------------------------------------------------------------------------------------
        public static void ImportExportPlugin
        (
            string fileName
        )
        {
            Echo("*** C# ImportExportPlugin called with " + fileName + ".\n");
        }

        //------------------------------------------------------------------------------------------
        public static string RouteNodeNamePlugin()
        {
            Echo("*** C# RouteNodeNamePlugin called");

            return "RNx";
        }

        //------------------------------------------------------------------------------------------
        public static string RouteSectionNamePlugin()
        {
            Echo("*** C# RouteSectionNamePlugin called");

            return "RSx";
        }

        //------------------------------------------------------------------------------------------
        public static double WrappedOverstockLengthCalculationPlugin
        (
            Overstock overstock
        )
        {
            Echo("*** C# Wrapped Overstock Length Calculation plugin called with overstock tag " + overstock.Tag.ToString());

            return 10.0;
        }

        //------------------------------------------------------------------------------------------
        public static bool FilterBlankingPlugin
        (
            NXObject segmentOrComponent,
            string logicalAttributeTitle,
            string logicalAttributeValue,
            string variableBuildString
        )
        {
            Echo("*** C# Filter Blanking plugin called with object tag tag " + segmentOrComponent.Tag.ToString());

            RoutingElectrical electricalPreferences = theSession.Preferences.RoutingApplicationView.RoutingElectrical;

            string apvAttributeTitle = electricalPreferences.GetFilterBlankingAttribute();

            Echo("    APV Attribute Title    : " + apvAttributeTitle);
            Echo("    Logical Attribute Title: " + logicalAttributeTitle);

            if (logicalAttributeTitle != apvAttributeTitle)
            {
                Echo("    (Not the same attribute titles. Ignoring this object.)");
                return false;
            }

            logicalAttributeValue = logicalAttributeValue.ToUpper();

            bool blankTheObject = logicalAttributeValue == "YES" ||
                                  logicalAttributeValue == "TRUE" ||
                                  logicalAttributeValue == "1";

            Echo("    Logical Attribute Value: " + logicalAttributeValue);
            Echo("    Variable Build String  : " + variableBuildString);

            if (blankTheObject)
                Echo("    Blank the object!");

            Echo("");

            return blankTheObject;
        }

        //------------------------------------------------------------------------------------------
        public static void BomPlugin()
        {
            Echo("*** C# Bill of Materials plugin called.");
        }

        //------------------------------------------------------------------------------------------
        public static int AutoRoutePlugin
        (
            Connection[] connections
        )
        {
            Echo("\n*** C# Autoroute plugin called with " + connections.Length.ToString() + " connections.");

            foreach (Connection connection in connections)
                Echo("  Connection Tag " + connection.Tag.ToString());

            return 0;
        }

        //------------------------------------------------------------------------------------------
        public static int ManualRoutePlugin
        (
            Connection[] connections
        )
        {
            Echo("\n*** C# Manual Route plugin called with " + connections.Length.ToString() + " connections.");

            foreach (Connection connection in connections)
                Echo("  Connection Tag " + connection.Tag.ToString());

            return 0;
        }

        //------------------------------------------------------------------------------------------
        public static int UnroutePlugin
        (
            Connection[] connections
        )
        {
            Echo("\n*** C# Unroute plugin called with " + connections.Length.ToString() + " connections.");

            foreach (Connection connection in connections)
                Echo("  Connection Tag " + connection.Tag.ToString());

            return 0;
        }

        //------------------------------------------------------------------------------------------
        public static void NavigatorObjectSelectedPlugin
        (
            CustomManager.NavigatorType navigatorType,
            CustomManager.SelectionType selectionType,
            NXObject[] selectedObjects
        )
        {
            string message = "\n*** C# NavigatorObjectSelectedPlugin called with " + selectedObjects.Length.ToString();

            if (selectionType == CustomManager.SelectionType.Selected)
            {
                message += " selected";
            }
            else
            {
                message += " deselected";
            }

            if (navigatorType == CustomManager.NavigatorType.Connection)
            {
                message += " in the Connection Navigator.";
            }
            else
            {
                message += " in the Component Navigator.";
            }

            Echo(message);

            foreach (NXObject selectedObject in selectedObjects)
                Echo("    Object tag " + selectedObject.Tag.ToString());
        }

        //------------------------------------------------------------------------------------------
        public static bool ValidateFormboardPlugin
        (
            HarnessDevice[] harnessDevices
        )
        {
            Echo("\n*** C# Validate formboard plugin called with " + harnessDevices.Length.ToString() + " harness devices.\n");

            foreach (HarnessDevice harnessDevice in harnessDevices)
                Echo("  Harness Tag " + harnessDevice.Tag.ToString() + ".");

            return true;
        }

        //------------------------------------------------------------------------------------------
        public static void DisciplineChangedPlugin
        (
            string previousDisciplineName,
            string newDisciplineName
        )
        {
            Echo("\n*** C# Discipline Changed plugin called.");
            Echo("    Previous discipline name '" + previousDisciplineName + "'");
            Echo("    New discipline name      '" + newDisciplineName + "'");
        }

        //------------------------------------------------------------------------------------------
        public static void SpecificationChangedPlugin
        (
            string previousSpecificationName,
            string newSpecificationName
        )
        {
            Echo("\n*** C# Specification Changed plugin called.");
            Echo("    Previous specification name '" + previousSpecificationName + "'");
            Echo("    New specification name      '" + newSpecificationName + "'");
        }

        //------------------------------------------------------------------------------------------
        public static void SortConnectionsPlugin
        (
            SortConnectionsPluginData dataObject
        )
        {
            ElectricalStockDevice[] stockDevices;
            dataObject.GetStockDevicesToSort(out stockDevices);

            Echo("\n*** C# Sort Connections plugin called with " + stockDevices.Length.ToString() + " stock devices.\n");

            Tag[] stockDeviceTags = new Tag[stockDevices.Length];
            int index = 0;
            foreach (ElectricalStockDevice stockDevice in stockDevices)
            {
                Echo("  Stock Device Tag " + stockDevice.Tag.ToString() + ".");
                stockDeviceTags[index] = stockDevice.Tag;
                ++index;
            }

            // Implement your sorting method here.
            Array.Sort(stockDeviceTags);

            Echo("");
            ElectricalStockDevice[] sortedStockDevices = new ElectricalStockDevice[stockDevices.Length];

            index = 0;
            foreach (Tag stockDeviceTag in stockDeviceTags)
            {
                Echo("  Sorted Stock Device Tag " + stockDeviceTag.ToString() + ".");

                sortedStockDevices[index] = (ElectricalStockDevice)NXObjectManager.Get(stockDeviceTag);
                ++index;
            }

            dataObject.SetSortedStockDevices(sortedStockDevices);
        }

        //------------------------------------------------------------------------------------------
        // Implements an example Choose Part plugin that is used by the Place Part command.
        //
        // You will have to add a reference to the Assemblies Framework System.Windows.Forms to use
        // the OpenFileDialog class shown in this example.
        public static int ChoosePartPlugin
        (
            ChoosePartPluginData dataObject
        )
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();

            openFileDialog.Title = "Choose a part to place";
            openFileDialog.DefaultExt = "prt";
            openFileDialog.Filter = "part files (*.prt)|*.prt|All files (*.*)|*.*";
            openFileDialog.CheckFileExists = true;
            openFileDialog.CheckPathExists = true;

            DialogResult result = openFileDialog.ShowDialog();
            if (result == DialogResult.Cancel)
                return -1;

            string fullPath = openFileDialog.FileName;

            // At this point, you could open the part to get some of the part attributes from it.
            // For this example, we are just going to return a few default values to Routing.
            dataObject.SetPartName(fullPath);
            dataObject.SetPartNumber("ExamplePartNumber001");
            dataObject.SetMemberName(""); // No member name since this is not a member of a part family.

            // Some example attributes.
            CharacteristicList exampleCharacteristics = theSession.Preferences.RoutingApplicationView.PartPreferences.PartLibrary.CreateCriteria();
            exampleCharacteristics.SetCharacteristic("USER_CHARX_TITLE1", "User_charx_value1");
            exampleCharacteristics.SetCharacteristic("USER_CHARX_TITLE2", "User_charx_value2");

            dataObject.SetCharacteristics(exampleCharacteristics);

            return 0;
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
