#===================================================================================================
#
#    This material contains trade secrets or otherwise confidential information owned by
#    Siemens Industry Software Inc. or its affiliates (collectively, "SISW"), or its licensors.
#    Access to and use of this information is strictly limited as set forth in the Customer's
#    applicable agreements with SISW.
#
#    Unpublished work Copyright 2024 Siemens
#
#===================================================================================================
#
#    NOTE:  NX Development provides programming examples for illustration only.
#    NX Development assumes you are familiar with the programming language
#    demonstrated in these examples, and the tools used to create and debug NX/Open
#    programs. GTAC support professionals can help explain the functionality of
#    a particular procedure, but neither GTAC nor NX Development will modify
#    these examples to provide added functionality or construction procedures.
#
#File description:
#
#    Implements an example Routed System Design (RSD) Mechanical connection compatibility design rule.
#
#    This example design rule will handle an interactive check as well as a concurrent check after
#    placing a part.
#
#
#===================================================================================================
import NXOpen
import NXOpen.Routing
import NXOpen.MechanicalRouting

designRuleName        = "Connection Compatibility Design Rule"
theSession            = None
customManager         = None
compatibleConnections = {}
connectionAttributes  = []

#---------------------------------------------------------------------------------------------------
# The connection compatibility check is between two ports. Since connected ports are not
# normally displayed, this method tries to find the stock or the component that owns the
# port. These show up better when highlighted in the Design Rule Violation dialog.
def addPortObjects( port, objects ):

    if port.IsOccurrence:
        objects.append( port.GetComponent() )
        return

    if type( port ) is NXOpen.Routing.StockPort:
        stock       = port.GetStock();
        stockBodies = stock.GetBodies();

        for stockBody in stockBodies:
            objects.append( stockBody );
        return;

    objects.append( port );

#---------------------------------------------------------------------------------------------------
# Creates a new violation for the two connected ports.
def createViolation( port1, port2, violationDescription ):

    message = "The two objects are incompatible due to:\n"
    message += violationDescription

    # Try to use the components that contain the ports in the violation since it's much
    # easier to see highlighted components than highlighted ports.
    objects = []
    addPortObjects( port1, objects )
    addPortObjects( port2, objects )

    # NOTE: The design rule name given on the violation must match the name given to the
    #       rule when registering.
    customManager.CreateViolationForReason( designRuleName,
                                            NXOpen.Routing.CustomManager.DesignRuleReason.ConnectionCompatibility,
                                            "Incompatible connection", message, objects )

#---------------------------------------------------------------------------------------------------
# Finds the CONNECTION_TYPE attribute on each port and checks the values against the
# current specification's connection compatibility table to ensure the two values are
# compatible.
def validateConnectionType( port1, port2 ):

    if not port1.HasUserAttribute( "CONNECTION_TYPE", NXOpen.NXObject.AttributeType.String, -1 ):
        return;

    if not port2.HasUserAttribute( "CONNECTION_TYPE", NXOpen.NXObject.AttributeType.String, -1 ):
        return;

    port1ConnectionType = port1.GetUserAttributeAsString( "CONNECTION_TYPE", NXOpen.NXObject.AttributeType.String, -1 );
    port2ConnectionType = port2.GetUserAttributeAsString( "CONNECTION_TYPE", NXOpen.NXObject.AttributeType.String, -1 );

    if port1ConnectionType in compatibleConnections and port2ConnectionType == compatibleConnections[port1ConnectionType]:
        return;

    if port2ConnectionType in compatibleConnections and port1ConnectionType == compatibleConnections[port2ConnectionType]:
        return;

    violationDescription = "Invalid connection types " + port1ConnectionType + " and " + port2ConnectionType + ".";
    createViolation( port1, port2, violationDescription );

#---------------------------------------------------------------------------------------------------
# Validates that the values of the connection attributes listed in customer defaults are
# the same on the two ports.
def validateConnectionAttributes( port1, port2 ):

    for attribute in connectionAttributes:

        if not port1.HasUserAttribute( attribute, NXOpen.NXObject.AttributeType.Any, -1 ):
            continue

        if not port2.HasUserAttribute( attribute, NXOpen.NXObject.AttributeType.Any, -1 ):
            continue

        # Get the attribute values as strings.
        # NOTE: This check can be made more complex by finding out the attribute types and
        #       comparing the attribute values for each type of attribute.
        port1Value = port1.GetUserAttributeAsString( attribute, NXOpen.NXObject.AttributeType.Any, -1 )
        port2Value = port2.GetUserAttributeAsString( attribute, NXOpen.NXObject.AttributeType.Any, -1 )
        if  port1Value == port2Value:
            continue

        violationDescription = "Attribute " + attribute + " has different values (" + port1Value + " and " + port2Value + ")."
        createViolation( port1, port2, violationDescription )

#---------------------------------------------------------------------------------------------------
def validatePortPairs( portPairs ):

    for port1, port2 in portPairs.items():
        validateConnectionType( port1, port2 )
        validateConnectionAttributes( port1, port2 )

#---------------------------------------------------------------------------------------------------
# For an interactive check, validates all the connected ports in the work part.
def checkConnectionsInWorkPart():

    workPart   = theSession.Parts.Work
    routingMgr = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager( theSession );
    service    = routingMgr.ConnectivityService

    connectedPorts1, connectedPorts2 = service.GetConnectedPorts( workPart )

    portPairs = {}
    for index in range(len(connectedPorts1)):
        portPairs[connectedPorts1[index]] = connectedPorts2[index]

    if portPairs:
        validatePortPairs( portPairs );

#---------------------------------------------------------------------------------------------------
# For concurrent check (e.g. after placing a part), validates the connection ports of the
# given objects.
def checkConnections( nxObjects ):

    routingMgr = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager( theSession );
    service    = routingMgr.ConnectivityService;

    portPairs = {}

    for nxObject in nxObjects:

        # TODO: Add a check for stock ports here.
        if type( nxObject ) is not NXOpen.Assemblies.Component:
            continue

        connectedPorts1, connectedPorts2 = service.GetConnectedPortsFromComponent( nxObject )

        # Because we can get duplicate port pairs from two connected components, add the port
        # pairs to a set to ensure we have unique pairs.
        for index in range(len(connectedPorts1)):
            if not connectedPorts1[index] in portPairs:
                portPairs[connectedPorts1[index]] = connectedPorts2[index]

    if len( portPairs ) > 0:
        validatePortPairs( portPairs )

#---------------------------------------------------------------------------------------------------
# Gets the connection compatibility pairs from the current specification, if any.
# Returns false if no pairs were found.
def getConnectionCompatibilities():

    global compatibleConnections

    workPart   = theSession.Parts.Work
    routeMgr   = workPart.RouteManager
    library    = routeMgr.ReuseLibrary

    activeSpecification = library.SpecificationsGetCurrent()

    # If there is no specification, there's no reason to run the compatibility check.
    if not activeSpecification or activeSpecification == "None":
        return False

    strings1, strings2 = library.SpecificationsGetConnectionCompatibilities( activeSpecification )

    # If the specification doesn't define any connection compatibilities,
    # there's no reason to run the compatibility check.
    if not strings1 or not strings2:
        return False

    # Build a dictionary of string1/string2 and string2/string1 to make it easy to find
    # a valid pair of compatible CONNECTION_TYPE attributes values.
    for index in range(len(strings1)):

        if not strings1[index] in compatibleConnections:
            compatibleConnections[strings1[index]] = strings2[index]

        if not strings2[index] in compatibleConnections:
            compatibleConnections[strings2[index]] = strings1[index]

    return True

#---------------------------------------------------------------------------------------------------
def compatibilityDesignRule( reason, nxObjects ):

    global connectionAttributes

    # If the current specification does not define a connection compatibility table,
    # do not proceed.
    if not getConnectionCompatibilities():
        return

    # This is the list of attributes whose values must match in any port-to-port connection.
    connectionAttributes = theSession.OptionsManager.GetStringListValue( "RSD_ConnectionCompatibilityAttributes" )

    # For interactive checks, check all the connections in the work part.
    if reason == NXOpen.Routing.CustomManager.DesignRuleReason.Interactive:
        checkConnectionsInWorkPart()
    else:
        # Otherwise, check the connections among the given list of objects.
        checkConnections( nxObjects )

#---------------------------------------------------------------------------------------------------
def startup( argc, args ):

    global theSession
    global customManager

    theSession    = NXOpen.Session.GetSession()
    customManager = theSession.RouteCustomManager

    description = "The compatibility design rule ensures piping connections are valid.";

    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.ConnectionCompatibility, designRuleName, description, compatibilityDesignRule)
    customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.PlacePart,               designRuleName, description, compatibilityDesignRule)

    theSession.LicenseManager().ReleaseAll( None );

    return 0 # No errors.


