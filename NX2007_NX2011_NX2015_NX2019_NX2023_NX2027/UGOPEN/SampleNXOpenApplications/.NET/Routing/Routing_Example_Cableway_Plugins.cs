/*==================================================================================================
                                       Copyright 2020 Siemens
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A C# class that implements example Routing Cableway plugins.


==================================================================================================*/
using System;
using NXOpen;
using NXOpen.Assemblies;
using NXOpen.RoutingCommon;

namespace RoutingCommon
{
    public class Plugins
    {
        // Static class members
        static Session theSession = null;
        static ListingWindow listingWindow = null;
        static CustomManager customManager = null;
        private static int nodeCounter = 0;
        private static int segmentCounter = 0;

        //------------------------------------------------------------------------------------------
        // Called when NX starts up to register the plugins.
        public static int Startup()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (listingWindow == null)
                listingWindow = theSession.ListingWindow;

            // Calling CreateRoutingSession is required before registering Routed System Designer (RSD)
            // plugins, callbacks, or design rules to ensure the Routing libraries are properly loaded.
            theSession.CreateRoutingSession();

            if (customManager == null)
                customManager = theSession.RoutingCustomManager;

            customManager.SetRSDApplicationEnterPlugin( ApplicationEnter );
            customManager.SetRSDApplicationExitPlugin( ApplicationExit );

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

            // Calling CreateRoutingSession is required before registering Routed System Designer (RSD)
            // plugins, callbacks, or design rules to ensure the Routing libraries are properly loaded.
            theSession.CreateRoutingSession();

            if (customManager == null)
                customManager = theSession.RoutingCustomManager;

            customManager.SetRSDApplicationEnterPlugin( ApplicationEnter );
            customManager.SetRSDApplicationExitPlugin( ApplicationExit );
        }

        //------------------------------------------------------------------------------------------
        // Called when you enter one of the Routed System Designer (RSD) applications.
        // When entering the Mechanical application, registers the DisciplineChanged plugin.
        public static void ApplicationEnter
        (
            CustomManager.Application application
        )
        {
            Echo( "C++ Application Enter" );

            if (application == CustomManager.Application.Electrical)
            {
                Echo( "Entering the Electrical application " );
            }
            else
            {
                // When entering the Mechanical application, register a "discipline changed" plugin to
                // watch for a change to the Cableway discipline.
                Echo( "Entering the Mechanical application " );

                NXOpen.Routing.CustomManager routeCustomManager = theSession.RouteCustomManager;

                routeCustomManager.SetDisciplineChangedPlugin( DisciplineChanged );
            }
        }

        //------------------------------------------------------------------------------------------
        // Called when you enter one of the Routed System Designer (RSD) applications.
        // Unregisters the DisciplineChanged plugin.
        public static void ApplicationExit
        (
            CustomManager.Application application
        )
        {
            Echo( "C++ Application Exit" );
            if (application == CustomManager.Application.Electrical)
            {
                Echo( "Exiting the Electrical application " );
            }
            else
            {
                Echo( "Exiting the Mechanical application " );
            }

            // When exiting any Routing application, remove the "discipline changed" plugin and the
            // "Cableways" plugins
            theSession.RouteCustomManager.RemoveDisciplineChangedPlugin();

            DeregisterPlugins();
        }

        //------------------------------------------------------------------------------------------
        // Called when you change the discipline. Registers the Cableway plugins listed above
        // if the new discipline is the cableway discipline. Otherwise, it deregisters the plugins.
        public static void DisciplineChanged
        (
            string previousDisciplineName,
            string newDisciplineName
        )
        {
            Echo( "C++ DisciplineChanged" );

            string cablewayDisciplineName = theSession.OptionsManager.GetStringValue( "RSD_Cableway_Discipline_Name" );


            // Register all the Cableways plugins if the new discipline is the Cableways discipline.
            if (cablewayDisciplineName == newDisciplineName)
            {
                Echo( "  Registering Cableway plugins." );
                RegisterPlugins();
            }
            else
            {
                Echo( "  Deregistering Cableway plugins." );
                DeregisterPlugins();
            }
        }

        //------------------------------------------------------------------------------------------
        // Called by both Main and ApplicationEnter to register the plugins.
        private static void RegisterPlugins()
        {
            customManager.SetCablewayXmlFileNamePlugin( CablewayXmlFileName );
            customManager.SetCablewayUniqueNodeNamePlugin( CablewayNodeName );
            customManager.SetCablewayUniqueSegmentNamePlugin( CablewaySegmentName );
            customManager.SetCablewayDeviceIdentifierPlugin( CablewayDeviceIdentifier );
            customManager.SetCablewayPreExportPlugin( CablewayPreExport );
            customManager.SetCablewayPostExportPlugin( CablewayPostExport );
            customManager.SetCablewayAreaNamePlugin( CablewayAreaName );
        }

        //------------------------------------------------------------------------------------------
        // Called by ApplicationExit to deregister the plugins.
        private static void DeregisterPlugins()
        {
            customManager.RemoveCablewayXmlFileNamePlugin();
            customManager.RemoveCablewayUniqueNodeNamePlugin();
            customManager.RemoveCablewayUniqueSegmentNamePlugin();
            customManager.RemoveCablewayDeviceIdentifierPlugin();
            customManager.RemoveCablewayPreExportPlugin();
            customManager.RemoveCablewayPostExportPlugin();
            customManager.RemoveCablewayAreaNamePlugin();
        }

        //------------------------------------------------------------------------------------------
        // Called before Routing exports a Cableway XML file to return the name of the XML file
        // into which to write the Cableway data.
        public static string CablewayXmlFileName()
        {
            Echo( "CablewayXmlFileName" );

            DateTime dt = new DateTime();
            string dateString = dt.Year.ToString() + "_" + dt.Month.ToString( "D2" ) + "_" + dt.Day.ToString( "D2" );
            string timeString = dt.Hour.ToString( "D2" ) + "_" + dt.Minute.ToString( "D2" );

            return "RoutingCablewayExport_" + dateString + "_" + timeString + ".xml";
        }

        //------------------------------------------------------------------------------------------
        // Called while Routing exports a Cableway XML file to create a new, unique identifier
        // for the given control point.
        //
        // \param[in]
        //      areaName
        //          The name of the area under which the cableway part and node object live.
        //
        // \param[in]
        //      cablewaySubassembly
        //          The cableway subassembly that owns the node object.
        //
        // \param[in]
        //      nodeObjectOccurrence
        //          The control point or point occurrence that needs a unique ID.
        //
        // \return
        //      The unique ID for this control point.
        public static string CablewayNodeName
        (
            string areaName,
            Component cablewaySubassembly,
            NXObject nodeObjectOccurrence
        )
        {
            Echo( "CablewayNodeName" );

            // If the node object occurrence already has a name, just return it.
            if (nodeObjectOccurrence.Name.Length > 0)
                return nodeObjectOccurrence.Name;

            nodeCounter += 1;

            return nodeObjectOccurrence.Tag.ToString() + "_" + nodeCounter.ToString();
        }

        //------------------------------------------------------------------------------------------
        // Called while Routing exports a Cableway XML file to create a new, unique identifier
        // for the given segment.
        //
        // \param[in]
        //      areaName
        //          The name of the area under which the cableway part and segment live.
        //
        // \param[in]
        //      cablewaySubassembly
        //          The cableway subassembly that owns the segment object.
        //
        // \param[in]
        //      segmentObject
        //          The segment occurrence or hanger component that needs a unique ID.
        //
        // \return
        //      The unique ID for this segment.
        public static string CablewaySegmentName
        (
            string areaName,
            Component cablewaySubassembly,
            NXObject segmentObject
        )
        {
            Echo( "CablewaySegmentName" );

            INXObject segmentPrototype = segmentObject.Prototype;

            // When given the entity occurrence of a Routing segment or a curve, check the curve name for an
            // existing unique ID.
            if (segmentPrototype.GetType() == typeof( NXOpen.Routing.ArcSegment ) ||
                 segmentPrototype.GetType() == typeof( NXOpen.Routing.LineSegment ) ||
                 segmentPrototype.GetType() == typeof( NXOpen.Routing.SplineSegment ) ||
                 segmentPrototype.GetType() == typeof( NXOpen.Arc ) ||
                 segmentPrototype.GetType() == typeof( NXOpen.Line ) ||
                 segmentPrototype.GetType() == typeof( NXOpen.Spline ))
            {
                string uniqueID = segmentObject.Name;
                if (uniqueID.Length > 0)
                    return uniqueID;
            }

            // When given a hanger component that must be represented as a zero-length segment,
            // look for the CABLEWAY_HANGER_ID attribute on the component.
            if (segmentPrototype.GetType() == typeof( NXOpen.Part ))
            {
                string uniqueID = segmentObject.GetStringUserAttribute( "CABLEWAY_HANGER_ID", -1 );
                if (uniqueID.Length > 0)
                    return uniqueID;
            }

            // Otherwise, create a new unique ID and return it.
            segmentCounter += 1;
            return segmentObject.Tag.ToString() + "_" + segmentCounter.ToString();
        }

        //------------------------------------------------------------------------------------------
        // Called while Routing exports a Cableway XML file to identify if the given component
        // is a device that should be exported.
        //
        // \param[in]
        //      component
        //          The component to check.
        //
        // \return
        //      The device ID to use for this component in the Cableway XML file.
        //      Returns an empty string if this device should not be exported.
        public static string CablewayDeviceIdentifier
        (
            Component component
        )
        {
            Echo( "CablewayDeviceIdentifier" );

            string deviceID = "";
            if (component.HasUserAttribute( "Electrical_Device_ID", NXObject.AttributeType.String, -1 ))
                deviceID = component.GetStringUserAttribute( "Electrical_Device_ID", -1 );

            return deviceID;
        }

        //------------------------------------------------------------------------------------------
        // Called just after Routing exports a Cableway XML file.
        //
        // \param[in]
        //      xmlFileName
        //          The name of the XML file Routing just exported.
        public static void CablewayPreExport
        (
            string xmlFileName
        )
        {
            string message = "CablewayPreExport called with ";
            message += xmlFileName;

            Echo( message );
        }
        //------------------------------------------------------------------------------------------
        // Called just after Routing exports a Cableway XML file.
        //
        // \param[in]
        //      xmlFileName
        //          The name of the XML file Routing just exported.
        public static void CablewayPostExport
        (
            string xmlFileName
        )
        {
            string message = "CablewayPostExport called with ";
            message += xmlFileName;

            Echo( message );
        }

        //------------------------------------------------------------------------------------------
        // Called during Cableway export to create an area name for a given component and all
        // the components under it.
        //
        // \param[in]
        //      component
        //          The component to check.
        //
        // \return
        //      The area name to use for all the devices, hangers, nodes, segments, etc., found
        //      under this component.
        public static string CablewayAreaName
        (
            Component component
        )
        {
            Echo( "CablewayAreaName" );

            string areaName = "";
            if (component.HasUserAttribute( "Electrical_Device_Area", NXObject.AttributeType.String, -1 ))
                areaName = component.GetStringUserAttribute( "Electrical_Device_Area", -1 );

            return areaName;
        }

        //------------------------------------------------------------------------------------------
        // Writes the given string to the Listing Window and the log file.
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

            listingWindow.WriteFullline( message );

            LogFile logFile = theSession.LogFile;
            logFile.WriteLine( message );
        }

        //------------------------------------------------------------------------------------------
        // Tells NX when to unload your application.
        // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
        public static int GetUnloadOption( string arg )
        {
            return System.Convert.ToInt32( Session.LibraryUnloadOption.AtTermination );
        }
    }
}
