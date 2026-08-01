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
import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;

import nxopen.Body;
import nxopen.ListingWindow;
import nxopen.NXException;
import nxopen.NXObject;
import nxopen.Part;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.assemblies.Component;
import nxopen.mechanicalrouting.ConnectivityService;
import nxopen.mechanicalrouting.RoutingManager;
import nxopen.mechanicalrouting.RoutingManagerFactory;
import nxopen.routing.CustomManager.DesignRuleReason;
import nxopen.routing.Port;
import nxopen.routing.ReuseLibrary;
import nxopen.routing.ReuseLibrary.SpecificationsGetConnectionCompatibilitiesData;
import nxopen.routing.RouteManager;
import nxopen.routing.Stock;
import nxopen.routing.StockPort;
import nxopen.routingcommon.CustomManager;

//--------------------------------------------------------------------------------------------------
public class Routing_Example_Compatibility_DesignRules implements nxopen.routingcommon.CustomManager.DesignRule
{

    static String              designRuleName        = "Connection Compatibility Design Rule";
    static Session             theSession            = null;
    static CustomManager       customManager         = null;
    static Map<String, String> compatibleConnections = new Hashtable<>();
    static String[]            connectionAttributes;

    //----------------------------------------------------------------------------------------------
    // Called when NX starts.
    // Creates a new instance of this design rule class.
    public static void startup(String[] args) throws NXException, java.rmi.RemoteException
    {
        if (theSession == null)
            theSession = (Session) SessionFactory.get("Session");

        if (customManager == null)
            customManager = theSession.routingCustomManager();

        new Routing_Example_Compatibility_DesignRules();

        theSession.licenseManager().releaseAll(null);
    }

    //----------------------------------------------------------------------------------------------
    // The constructor for this class.
    // Registers the Design Rules.
    public Routing_Example_Compatibility_DesignRules() throws RemoteException, NXException
    {
        String description = "The compatibility design rule ensures piping connections are valid.";

        CustomManager customManager = theSession.routingCustomManager();

        customManager.addDesignRule(DesignRuleReason.CONNECTION_COMPATIBILITY, designRuleName, description, this);
        customManager.addDesignRule(DesignRuleReason.PLACE_PART,               designRuleName, description, this);
    }

    //----------------------------------------------------------------------------------------------
    // The connection compatibility check is between two ports. Since connected ports are not
    // normally displayed, this method tries to find the stock or the component that owns the
    // port. These show up better when highlighted in the Design Rule Violation dialog.
    private void addPortObjects
    (
        Port                port,
        ArrayList<NXObject> objects
    ) throws RemoteException, NXException
    {
        if (port.isOccurrence())
        {
            objects.add( port.getComponent() );
            return;
        }

        if (port instanceof StockPort )
        {
            StockPort stockPort   = (StockPort)port;
            Stock     stock       = stockPort.getStock();
            Body[]    stockBodies = stock.getBodies();

            for ( int index = 0; index < stockBodies.length; ++index )
                objects.add( stockBodies[index] );

            return;
        }

        objects.add( port );
    }

    //----------------------------------------------------------------------------------------------
    // Creates a new violation for the two connected ports.
    private void createViolation
    (
        Port   port1,
        Port   port2,
        String violationDescription
    ) throws RemoteException, NXException
    {
        String message = "The two objects are incompatible due to:\n";
        message += violationDescription;

        // Try to use the components that contain the ports in the violation since it's much
        // easier to see highlighted components than highlighted ports.
        ArrayList<NXObject> objects = new ArrayList<NXObject>();
        addPortObjects( port1, objects );
        addPortObjects( port2, objects );
        if ( objects.isEmpty() )
            return;

        NXObject[] objectsArray = new NXObject[objects.size()];
        objects.toArray(objectsArray);

        // NOTE: The design rule name given on the violation must match the name given to the
        //       rule when registering.
        customManager.createViolationForReason( designRuleName,
                                                DesignRuleReason.CONNECTION_COMPATIBILITY,
                                                "Incompatible connection", message, objectsArray );
    }

    //----------------------------------------------------------------------------------------------
    // Finds the CONNECTION_TYPE attribute on each port and checks the values against the
    // current specification's connection compatibility table to ensure the two values are
    // compatible.
    private void validateConnectionType
    (
        Port port1,
        Port port2
    ) throws RemoteException, NXException
    {
        if ( !port1.hasUserAttribute( "CONNECTION_TYPE", NXObject.AttributeType.STRING, -1 ) )
            return;

        if (!port2.hasUserAttribute( "CONNECTION_TYPE", NXObject.AttributeType.STRING, -1 ))
            return;

        String port1ConnectionType = port1.getUserAttributeAsString( "CONNECTION_TYPE", NXObject.AttributeType.STRING, -1 );
        String port2ConnectionType = port2.getUserAttributeAsString( "CONNECTION_TYPE", NXObject.AttributeType.STRING, -1 );

        if ( compatibleConnections.containsKey( port1ConnectionType ) &&
             port2ConnectionType.equals( compatibleConnections.get(port1ConnectionType) ) )
        {
            return;
        }

        if ( compatibleConnections.containsKey( port2ConnectionType ) &&
             port1ConnectionType.equals( compatibleConnections.get(port2ConnectionType) ) )
        {
            return;
        }

        String violationDescription = "Invalid connection types " + port1ConnectionType + " and " + port2ConnectionType + ".";
        createViolation( port1, port2, violationDescription );
    }

    //----------------------------------------------------------------------------------------------
    // Validates that the values of the connection attributes listed in customer defaults are
    // the same on the two ports.
    private void validateConnectionAttributes
    (
        Port port1,
        Port port2
    ) throws RemoteException, NXException
    {
        for ( String attribute : connectionAttributes )
        {
            if (!port1.hasUserAttribute( attribute, NXObject.AttributeType.ANY, -1 ))
                continue;

            if (!port2.hasUserAttribute( attribute, NXObject.AttributeType.ANY, -1 ))
                continue;

            // Get the attribute values as strings.
            // NOTE: This check can be made more complex by finding out the attribute types and
            //       comparing the attribute values for each type of attribute.
            String port1Value = port1.getUserAttributeAsString( attribute, NXObject.AttributeType.ANY, -1 );
            String port2Value = port2.getUserAttributeAsString( attribute, NXObject.AttributeType.ANY, -1 );
            if ( port1Value == port2Value )
                continue;

            String violationDescription = "Attribute " + attribute + " has different values (" + port1Value + " and " + port2Value + ").";
            createViolation( port1, port2, violationDescription );
        }
    }

    //----------------------------------------------------------------------------------------------
    private void validatePortPairs
    (
        Map<Port, Port> portPairs
    ) throws RemoteException, NXException
    {    
        for ( Map.Entry<Port, Port> portPair : portPairs.entrySet() )
        {
            validateConnectionType( portPair.getKey(), portPair.getValue() );
            validateConnectionAttributes( portPair.getKey(), portPair.getValue() );
        }
    }

    //----------------------------------------------------------------------------------------------
    // For an interactive check, validates all the connected ports in the work part.
    private void checkConnectionsInWorkPart() throws RemoteException, NXException
    {
        Part                  workPart   = theSession.parts().work();
        RoutingManager         routingMgr = RoutingManagerFactory.GetRoutingManager( theSession );
        ConnectivityService service    = routingMgr.connectivityService();

        ConnectivityService.ConnectedPortsData connectedPorts = service.getConnectedPorts( workPart );

        Map<Port, Port> portPairs = new HashMap<Port, Port>();
        
        for ( int index = 0; index < connectedPorts.connectedports1.length; ++index )
        {
            portPairs.put( connectedPorts.connectedports1[index], connectedPorts.connectedports2[index] );
        }

        if ( !portPairs.isEmpty() )
            validatePortPairs( portPairs );
    }

    //----------------------------------------------------------------------------------------------
    // For concurrent check (e.g. after placing a part), validates the connection ports of the
    // given objects.
    private void checkConnections
    (
        NXObject[] nxObjects
    ) throws RemoteException, NXException
    {
        RoutingManager         routingMgr = RoutingManagerFactory.GetRoutingManager( theSession );
        ConnectivityService service    = routingMgr.connectivityService();

        Map<Port, Port> portPairs = new HashMap<Port, Port>();

        for ( int iNxObjects = 0; iNxObjects < nxObjects.length; ++iNxObjects )
        {
            // TODO: Add a check for stock ports here.
            if ( nxObjects[iNxObjects].getClass() == Component.class )
                continue;

            Component component = (Component)nxObjects[iNxObjects];

            ConnectivityService.ConnectedPortsData connectedPorts = null;
            connectedPorts = service.getConnectedPortsFromComponent( component );

            // Because we can get duplicate port pairs from two connected components, add the port
            // pairs to a set to ensure we have unique pairs.
            for (int iConnectedPorts = 0; iConnectedPorts < connectedPorts.connectedports1.length; ++iConnectedPorts)
            {
                portPairs.put( connectedPorts.connectedports1[iConnectedPorts],
                               connectedPorts.connectedports2[iConnectedPorts] );
            }
        }

        if ( !portPairs.isEmpty() )
            validatePortPairs( portPairs );
    }

    //----------------------------------------------------------------------------------------------
    // Gets the connection compatibility pairs from the current specification, if any.
    // Returns false if no pairs were found.
    private boolean getConnectionCompatibilities() throws RemoteException, NXException
    {
        Part         workPart = theSession.parts().work();
        RouteManager routeMgr = workPart.routeManager();
        ReuseLibrary library  = routeMgr.reuseLibrary();

        String activeSpecification = library.specificationsGetCurrent();

        ListingWindow lw = theSession.listingWindow();
        
        // If there is no specification, there's no reason to run the compatibility check.
        if (activeSpecification.length() == 0 || activeSpecification.equals("None"))
            return false;

        SpecificationsGetConnectionCompatibilitiesData cocoPairs;
        cocoPairs = library.specificationsGetConnectionCompatibilities(activeSpecification);

        // If the specification doesn't define any connection compatibilities,
        // there's no reason to run the compatibility check.
        if (cocoPairs.connectiontypesone.length == 0 || cocoPairs.connectiontypestwo.length == 0)
            return false;

        // Build a dictionary of string1/string2 and string2/string1 to make it easy to find
        // a valid pair of compatible CONNECTION_TYPE attributes values.
        for ( int index = 0; index < cocoPairs.connectiontypesone.length; ++index )
        {
            compatibleConnections.put( cocoPairs.connectiontypesone[index],
                                       cocoPairs.connectiontypestwo[index] );

            compatibleConnections.put( cocoPairs.connectiontypestwo[index],
                                       cocoPairs.connectiontypesone[index] );
        }

        return true;
    }

    //----------------------------------------------------------------------------------------------
    // This is the method registered for the design rule.
    @Override
    public void designRule(DesignRuleReason reason, NXObject[] nxObjects) throws NXException, RemoteException
    {
        // If the current specification does not define a connection compatibility table,
        // do not proceed.
        if (!getConnectionCompatibilities())
            return;
        
        
        // This is the list of attributes whose values must match in any port-to-port connection.
        connectionAttributes = theSession.optionsManager().getStringListValue( "RSD_ConnectionCompatibilityAttributes" );

        // For interactive checks, check all the connections in the work part.
        if (reason == DesignRuleReason.INTERACTIVE)
        {
            checkConnectionsInWorkPart();
        }
        else
        {
            // Otherwise, check the connections among the given list of objects.
            checkConnections( nxObjects );
        }
    }

    //----------------------------------------------------------------------------------------------
    // Tells NX when to unload your application.
    // For Routing callbacks, plugins, and Design Rules, this MUST return
    // AT_TERMINATION.
    public static int getUnloadOption(String arg)
    {
        return Session.LibraryUnloadOption.AT_TERMINATION;
    }
}
