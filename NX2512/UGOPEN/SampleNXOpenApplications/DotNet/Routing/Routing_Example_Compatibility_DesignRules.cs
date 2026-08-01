/*==================================================================================================

    This material contains trade secrets or otherwise confidential information owned by
    Siemens Industry Software Inc. or its affiliates (collectively, "SISW"), or its licensors.
    Access to and use of this information is strictly limited as set forth in the Customer's
    applicable agreements with SISW.

    Unpublished work Copyright 2024 Siemens

====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    Implements an example Routed System Design (RSD) Mechanical connection compatibility design rule.

    This example design rule will handle an interactive check as well as a concurrent check after
    placing a part.


==================================================================================================*/
using NXOpen;
using NXOpen.Routing;
using NXOpen.MechanicalRouting;
using System;
using System.Collections.Generic;
using NXOpen.Assemblies;

namespace Routing
{
    public class DesignRules
    {
        // Static class members
        static string                             designRuleName        = "Connection Compatibility Design Rule";
        static Session                            theSession            = null;
        static NXOpen.RoutingCommon.CustomManager customManager         = null;
        static Dictionary<string, string>         compatibleConnections = new Dictionary<string, string>();
        static string[]                           connectionAttributes;

        //------------------------------------------------------------------------------------------
        // Called when NX starts up to register the Design Rules.
        public static int Startup()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (customManager == null)
                customManager = theSession.RoutingCustomManager;

            string description = "The compatibility design rule ensures piping connections are valid.";

            // Register the same design rule for connection compatibility, place part, and any other
            // commands where you want to check the compatibility of the connection you just
            // created.
            customManager.AddDesignRule( NXOpen.Routing.CustomManager.DesignRuleReason.ConnectionCompatibility, designRuleName, description, CompatibilityDesignRule );
            customManager.AddDesignRule( NXOpen.Routing.CustomManager.DesignRuleReason.PlacePart,               designRuleName, description, CompatibilityDesignRule );

            // Release any Routing licenses that were checked out when registering the design rule.
            theSession.LicenseManager.ReleaseAll( null );

            return 0;
        }

        //------------------------------------------------------------------------------------------
        // The connection compatibility check is between two ports. Since connected ports are not
        // normally displayed, this method tries to find the stock or the component that owns the
        // port. These show up better when highlighted in the Design Rule Violation dialog.
        private static void AddPortObjects
        (
            Port               port,
            ref List<NXObject> objects
        )
        {
            if (port.IsOccurrence)
            {
                objects.Add( port.GetComponent() );
                return;
            }

            if ( port.GetType() == typeof( StockPort ) )
            {
                StockPort stockPort   = (StockPort)port;
                Stock     stock       = stockPort.GetStock();
                Body[]    stockBodies = stock.GetBodies();

                foreach( Body stockBody in stockBodies )
                    objects.Add( stockBody );

                return;
            }

            objects.Add( port );
        }

        //------------------------------------------------------------------------------------------
        // Creates a new violation for the two connected ports.
        private static void CreateViolation
        (
            Port   port1,
            Port   port2,
            string violationDescription
        )
        {
            string message = "The two objects are incompatible due to:\n";
            message += violationDescription;

            // Try to use the components that contain the ports in the violation since it's much
            // easier to see highlighted components than highlighted ports.
            List<NXObject> objects = new List<NXObject>();
            AddPortObjects( port1, ref objects );
            AddPortObjects( port2, ref objects );

            // NOTE: The design rule name given on the violation must match the name given to the
            //       rule when registering.
            customManager.CreateViolationForReason( designRuleName,
                                                    NXOpen.Routing.CustomManager.DesignRuleReason.ConnectionCompatibility,
                                                    "Incompatible connection", message, objects.ToArray() );
        }

        //------------------------------------------------------------------------------------------
        // Finds the CONNECTION_TYPE attribute on each port and checks the values against the
        // current specification's connection compatibility table to ensure the two values are
        // compatible.
        private static void ValidateConnectionType
        (
            Port port1,
            Port port2
        )
        {
            if ( !port1.HasUserAttribute( "CONNECTION_TYPE", NXObject.AttributeType.String, -1 ) )
                return;

            if (!port2.HasUserAttribute( "CONNECTION_TYPE", NXObject.AttributeType.String, -1 ))
                return;

            string port1ConnectionType = port1.GetUserAttributeAsString( "CONNECTION_TYPE", NXObject.AttributeType.String, -1 );
            string port2ConnectionType = port2.GetUserAttributeAsString( "CONNECTION_TYPE", NXObject.AttributeType.String, -1 );

            if ( compatibleConnections.ContainsKey( port1ConnectionType ) &&
                 port2ConnectionType == compatibleConnections[port1ConnectionType] )
            {
                return;
            }

            if ( compatibleConnections.ContainsKey( port2ConnectionType ) &&
                 port1ConnectionType == compatibleConnections[port2ConnectionType])
            {
                return;
            }

            string violationDescription = "Invalid connection types " + port1ConnectionType + " and " + port2ConnectionType + ".";
            CreateViolation( port1, port2, violationDescription );
        }

        //------------------------------------------------------------------------------------------
        // Validates that the values of the connection attributes listed in customer defaults are
        // the same on the two ports.
        private static void ValidateConnectionAttributes
        (
            Port port1,
            Port port2
        )
        {
            foreach ( string attribute in connectionAttributes )
            {
                if (!port1.HasUserAttribute( attribute, NXObject.AttributeType.Any, -1 ))
                    continue;

                if (!port2.HasUserAttribute( attribute, NXObject.AttributeType.Any, -1 ))
                    continue;

                // Get the attribute values as strings.
                // NOTE: This check can be made more complex by finding out the attribute types and
                //       comparing the attribute values for each type of attribute.
                string port1Value = port1.GetUserAttributeAsString( attribute, NXObject.AttributeType.Any, -1 );
                string port2Value = port2.GetUserAttributeAsString( attribute, NXObject.AttributeType.Any, -1 );
                if (port1Value == port2Value)
                    continue;

                string violationDescription = "Attribute " + attribute + " has different values (" + port1Value + " and " + port2Value + ").";
                CreateViolation( port1, port2, violationDescription );
            }
        }

        //------------------------------------------------------------------------------------------
        private static void ValidatePortPairs
        (
            HashSet<KeyValuePair<Port, Port>> portPairs
        )
        {
            foreach (KeyValuePair<Port, Port> portPair in portPairs)
            {
                ValidateConnectionType( portPair.Key, portPair.Value );
                ValidateConnectionAttributes( portPair.Key, portPair.Value );
            }
        }

        //------------------------------------------------------------------------------------------
        // For an interactive check, validates all the connected ports in the work part.
        private static void CheckConnectionsInWorkPart()
        {
            Part                workPart   = theSession.Parts.Work;
            RoutingManager      routingMgr = RoutingManager.GetRoutingManager( theSession );
            ConnectivityService service    = routingMgr.ConnectivityService;

            Port[] connectedPorts1;
            Port[] connectedPorts2;
            service.GetConnectedPorts( workPart, out connectedPorts1, out connectedPorts2 );

            HashSet<KeyValuePair<Port, Port>> portPairs = new HashSet<KeyValuePair<Port, Port>>();

            for ( int index = 0; index < connectedPorts1.Length; ++index )
            {
                portPairs.Add( new KeyValuePair<Port, Port>( connectedPorts1[index], connectedPorts2[index] ) );
            }

            if ( portPairs.Count > 0)
                ValidatePortPairs( portPairs );
        }

        //------------------------------------------------------------------------------------------
        // For concurrent check (e.g. after placing a part), validates the connection ports of the
        // given objects.
        private static void CheckConnections
        (
            NXObject[] nxObjects
        )
        {
            RoutingManager      routingMgr = RoutingManager.GetRoutingManager( theSession );
            ConnectivityService service    = routingMgr.ConnectivityService;

            HashSet<KeyValuePair<Port, Port>> portPairs = new HashSet<KeyValuePair<Port, Port>>();

            foreach (NXObject nxObject in nxObjects)
            {
                // TODO: Add a check for stock ports here.
                if (nxObject.GetType() != typeof( Component ))
                    continue;

                Component component = (Component)nxObject;

                Port[] connectedPorts1;
                Port[] connectedPorts2;
                service.GetConnectedPortsFromComponent( component, out connectedPorts1, out connectedPorts2 );

                // Because we can get duplicate port pairs from two connected components, add the port
                // pairs to a set to ensure we have unique pairs.
                for (int index = 0; index < connectedPorts1.Length; ++index)
                {
                    portPairs.Add( new KeyValuePair<Port, Port>( connectedPorts1[index], connectedPorts2[index] ) );
                }
            }

            if ( portPairs.Count > 0 )
                ValidatePortPairs( portPairs );
        }

        //------------------------------------------------------------------------------------------
        // Gets the connection compatibility pairs from the current specification, if any.
        // Returns false if no pairs were found.
        private static bool GetConnectionCompatibilities()
        {
            Part         workPart = theSession.Parts.Work;
            RouteManager routeMgr = workPart.RouteManager;
            ReuseLibrary library  = routeMgr.ReuseLibrary;

            string activeSpecification = library.SpecificationsGetCurrent();

            // If there is no specification, there's no reason to run the compatibility check.
            if (activeSpecification.Length == 0 || activeSpecification.Equals( "None" ))
                return false;

            string[] strings1;
            string[] strings2;
            library.SpecificationsGetConnectionCompatibilities( activeSpecification, out strings1, out strings2 );

            // If the specification doesn't define any connection compatibilities,
            // there's no reason to run the compatibility check.
            if (strings1.Length == 0 || strings2.Length == 0)
                return false;

            // Build a dictionary of string1/string2 and string2/string1 to make it easy to find
            // a valid pair of compatible CONNECTION_TYPE attributes values.
            for ( int index = 0; index < strings1.Length; ++index )
            {
                if (!compatibleConnections.ContainsKey( strings1[index] ))
                    compatibleConnections.Add( strings1[index], strings2[index] );

                if (!compatibleConnections.ContainsKey( strings2[index] ))
                    compatibleConnections.Add( strings2[index], strings1[index] );
            }

            return true;
        }

        //------------------------------------------------------------------------------------------
        // This is the method registered for the design rule.
        private static void CompatibilityDesignRule
        (
            NXOpen.Routing.CustomManager.DesignRuleReason reason,
            NXObject[]                                    nxObjects
        )
        {
            // If the current specification does not define a connection compatibility table,
            // do not proceed.
            if ( !GetConnectionCompatibilities() )
                return;

            // This is the list of attributes whose values must match in any port-to-port connection.
            connectionAttributes = theSession.OptionsManager.GetStringListValue( "RSD_ConnectionCompatibilityAttributes" );

            // For interactive checks, check all the connections in the work part.
            if (reason == NXOpen.Routing.CustomManager.DesignRuleReason.Interactive)
            {
                CheckConnectionsInWorkPart();
            }
            else
            {
                // Otherwise, check the connections among the given list of objects.
                CheckConnections( nxObjects );
            }
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
