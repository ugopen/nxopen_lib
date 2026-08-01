#===================================================================================================
#               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
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
#    A python script that implements example Routing Design Rules.
#
#
#===================================================================================================
import NXOpen
import NXOpen.UF
import NXOpen.Routing

#-----------------------------------------------------------------------------------------------
def echo( message ):
    try:
        syslog = NXOpen.Session.GetSession().LogFile
        syslog.WriteLine( message )

        listingWindow = NXOpen.Session.GetSession().ListingWindow
        listingWindow.Open()
        listingWindow.WriteLine( message )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

 
#-----------------------------------------------------------------------------------------------
def checkForLongSegments( designRuleName, maximumLength, segment ):
    try:    
        if segment.Length < maximumLength:
            return

        customManager = NXOpen.Session.GetSession().RouteCustomManager

        segmentList = [segment]

        customManager.CreateViolationForReason( designRuleName,
                                                NXOpen.Routing.CustomManager.DesignRuleReason.CreatePath,
                                                "This path is too long.",
                                                "Long paths need to be broken up and supported by clamps.",
                                                segmentList )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

 
#-----------------------------------------------------------------------------------------------
def createPathDesignRule( reason, objects ):
    try:
        createPathName = "Create Path"
        maximumLength = 1000.0

        if reason == NXOpen.Routing.CustomManager.DesignRuleReason.Interactive:
            # For interactive checks, check all the segments in the work part.
            segmentManager    = NXOpen.Session.GetSession().Parts.Work.SegmentManager
            segmentCollection = segmentManager.Segments

            for segment in segmentCollection:
                checkForLongSegments( createPathName, maximumLength, segment )

            return

        # Otherwise, check the segments in the given list of objects.
        for object in objects:
            if type( object ) is NXOpen.Routing.SplineSegment:
               checkForLongSegments( createPathName, maximumLength, object )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex
 

#-----------------------------------------------------------------------------------------------
def checkForShortSegments( designRuleName, minimumLength, segment ):
    try:    
        if segment.Length > minimumLength:
            return

        customManager = NXOpen.Session.GetSession().RouteCustomManager

        segmentList = [segment]

        customManager.CreateViolationForReason( designRuleName,
                                                NXOpen.Routing.CustomManager.DesignRuleReason.SubdivideSegment,
                                                "This path is too short.",
                                                "Short segments violate our design standards.",
                                                segmentList )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex


#-----------------------------------------------------------------------------------------------
def subdivideSegmentDesignRule( reason, objects ):
    try:
        subdivideSegmentName = "Subdivide Segment"
        userPreferences = NXOpen.Session.GetSession().Preferences.RoutingApplicationView.RoutingUserPreferences

        tuple = userPreferences.GetDoublePreference( "ROUTE_ELEC_MIN_STRAIGHT_LENGTH_COEFF" )

        minimumLength = tuple[1]
        if not tuple[0]:
            minimumLength = 10.0 # Use a default value in case the preferences wasn't defined.

        if reason == NXOpen.Routing.CustomManager.DesignRuleReason.Interactive:
            # For interactive checks, check all the segments in the work part.
            segmentManager    = NXOpen.Session.GetSession().Parts.Work.SegmentManager
            segmentCollection = segmentManager.Segments

            for segment in segmentCollection:
                checkForShortSegments( subdivideSegmentName, minimumLength, segment )

            return

        # Otherwise, check the segments in the given list of objects.
        for object in objects:
            if type( object ) is NXOpen.Routing.SplineSegment:
               checkForShortSegments( subdivideSegmentName, minimumLength, object )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#-----------------------------------------------------------------------------------------------
# Safely gets the value of a string characteristic if it exists on the route object.
#
# \param[in]
#      routeObject 
#          The object from which to get the characteristic.
#
# \param[in]
#      characteristicName 
#          The name of the characteristic to get.
#
# \return
#      The string value of the characteristic. Will be null if the characteristic does not exist
#      or is not a string.
def getCharacteristicFromObject( routeObject, characteristicName ):

    characteristics = routeObject.GetCharacteristics()
    characteristicsInfo = characteristics.GetCharacteristicTitlesByType( NXOpen.NXObject.AttributeType.Any )

    for characteristicInfo in characteristicsInfo:
        
        if characteristicName == characteristicInfo.Name and characteristicInfo.Type == NXOpen.NXObject.AttributeType.String:
            return characteristics.GetStringCharacteristic( characteristicName )

    return None

#-----------------------------------------------------------------------------------------------
# Returns the names of the ports to which the connector is connected through a port connection.
#
# \param[in]
#      connector 
#          The connector to check.
#
# \return
#      The names of the ports to which this connector is connected. Will be null if the connector
#      is not assigned to a component or if the component's ports are not connected to any other
#      ports.
def getConnectedPortNames( connector ):

    echo ( "getConnectedPortNames" )
    if not connector.IsAssigned():
        return None
    
    assignedComponent = connector.NxEquivalent
    if assignedComponent is None:
        return None

    routeManager = NXOpen.Session.GetSession().Parts.Work.RouteManager
    assignedComponentPorts = routeManager.Ports.GetComponentPorts( assignedComponent )
    if assignedComponentPorts is None:
        return None

    connectedPortNames = list()

    portConnections = routeManager.PortConnections
    for assignedComponentPort in assignedComponentPorts:
        portConnection = portConnections.GetConnectionFromPort( assignedComponentPort )
        if portConnection == None:
            continue

        port1, port2 = portConnection.GetPorts()

        # We know the port on the connector, so get the name from the other port in the connection.
        if assignedComponentPort == port1.Name:
            connectedPortNames.append( port2.Name )
        else:
            connectedPortNames.append( port2.Name )

    return connectedPortNames


#-----------------------------------------------------------------------------------------------
def modularConnectorDesignRule( reason, objects ):
    if reason != NXOpen.Routing.CustomManager.DesignRuleReason.Interactive:
        return
    
    try:
        customManager = NXOpen.Session.GetSession().RouteCustomManager
        routeManager = NXOpen.Session.GetSession().Parts.Work.RouteManager
        connectors = routeManager.ConnectorDevices

        for connector in connectors:
            if not connector.IsAssigned():
                continue

            parentConnectorName = getCharacteristicFromObject( connector, NXOpen.UF.UFConstants.UF_RLIST_PARENT_ID_NAME )
            if parentConnectorName == None:
                continue

            parentPortName = getCharacteristicFromObject( connector, NXOpen.UF.UFConstants.UF_RLIST_PARENT_POSITION_NAME )
            if parentPortName == None:
                continue

            connectedCorrectly = False
            portNamesForMessage = ""

            connectedPortNames = getConnectedPortNames( connector )

            for connectedPortName in connectedPortNames:
                portNamesForMessage += connectedPortName + ", "

                if connectedPortName == parentPortName:
                    connectedCorrectly = True;
                    break

            if not connectedCorrectly:
                objects = list()
                objects.append( connector.NxEquivalent )

                message = "Connector " + connector.Name;
                message += " is connected to port(s) " + portNamesForMessage;
                message += "but should be connected to port " + parentPortName;
                message += " on connector " + parentConnectorName + ".";

                customManager.CreateViolationForReason( "Modular Connector", reason,
                                                        "Component connected to wrong port.",
                                                        message, objects );

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

#-----------------------------------------------------------------------------------------------
def startup( argc, args ):
    try:
        customManager = NXOpen.Session.GetSession().RouteCustomManager

        createPathName = "Create Path"
        subdivideSegmentName = "Subdivide Segment"
        modularConnectorName = "Modular Connector"
        createPathDescription = "The Create Path design rule makes sure each segment on the path is not too long."
        subdivideSegmentDescription = "The Subdivide Segment design rule makes sure each new segment is not too short."
        modularConnectorDescription = "The Modular Connector design rule makes sure modular connectors are plugged into the correct position on the parent shell."

        createPathRuleId       = customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.CreatePath, createPathName, createPathDescription, createPathDesignRule)
        subdivideSegmentRuleId = customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.SubdivideSegment, subdivideSegmentName, subdivideSegmentDescription, subdivideSegmentDesignRule)
        modularConnectorRuleId = customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.Interactive, modularConnectorName, modularConnectorDescription, modularConnectorDesignRule )


    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXOpen.NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    return 0 # No errors.


