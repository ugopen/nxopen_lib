#===================================================================================================
#                                      Copyright 2020 Siemens
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
#    A python script that implements example Routing Cableway plugins.
#
#
#===================================================================================================
import NXOpen
import NXOpen.RoutingCommon
from time import localtime

#---------------------------------------------------------------------------------------------------
# Writes the given string to the Listing Window and the log file.
#
# \param[in]
#      stringToWrite
#          The string to write.
def echo( message ):
    logFile = NXOpen.Session.GetSession().LogFile
    logFile.WriteLine( message )

    listingWindow = NXOpen.Session.GetSession().ListingWindow
    listingWindow.Open()
    listingWindow.WriteLine( message )

#---------------------------------------------------------------------------------------------------
# Called before Routing exports a Cableway XML file to return the name of the XML file
# into which to write the Cableway data.
def CablewayXmlFileName():
    echo( "CablewayXmlFileName" )

    localTime = localtime()

    fileName = str( localTime.tm_year ) + "_" + str( localTime.tm_mon ).zfill(2) + "_" + str( localTime.tm_mday ).zfill(2)
    filename = fileName + "_" + str( localTime.tm_hour ).zfill(2) + "_" + str( localTime.tm_min ).zfill(2) + ".xml"

    return filename

#---------------------------------------------------------------------------------------------------
# Called while Routing exports a Cableway XML file to create a new, unique identifier
# for the given control point.
#
# \param[in]
#      areaName
#          The name of the area under which the cableway part and segment live.
#
# \param[in]
#      cablewaySubassembly
#          The cableway subassembly that owns the segment object.
#
# \param[in]
#      nodeObjectOccurrence
#          The control point or point occurrence that needs a unique ID
#
# \return
#      The unique ID for this control point.
def CablewayNodeName( areaName, cablewaySubassembly, nodeObjectOccurrence ):
    echo( "CablewayNodeName" )

    # If the node object occurrence already has a name, just return it.
    if not nodeObjectOccurrence.Name == None:
        return nodeObjectOccurrence.Name

    if not hasattr(CablewayNodeName, "counter"):
        CablewayNodeName.counter = 0  # it doesn't exist yet, so initialize it

    CablewayNodeName.counter += 1

    return str( nodeObject.Tag ) + "_" + str( CablewayNodeName.counter )

#---------------------------------------------------------------------------------------------------
# Called while Routing exports a Cableway XML file to create a new, unique identifier
# for the given segment.
#
# \param[in]
#      areaName
#          The name of the area under which the cableway part and segment live.
#
# \param[in]
#      cablewaySubassembly
#          The cableway subassembly that owns the segment object.
#
# \param[in]
#      segmentObject
#          The segment occurrence or hanger component that needs a unique ID.
#
# \return
#      The unique ID for this segment.
def CablewaySegmentName(areaName, cablewaySubassembly, segmentObject):
    echo("CablewaySegmentName")

    segmentPrototype = segmentObject.Prototype

    # When given the entity occurrence of a Routing segment or a curve, check the curve name for an
    # existing unique ID.
    if type(segmentPrototype) is NXOpen.Routing.ArcSegment    or \
       type(segmentPrototype) is NXOpen.Routing.LineSegment   or \
       type(segmentPrototype) is NXOpen.Routing.SplineSegment or \
       type(segmentPrototype) is NXOpen.Arc  or \
       type(segmentPrototype) is NXOpen.Line or \
       type(segmentPrototype) is NXOpen.Spline:
        uniqueID = segmentObject.Name
        if not uniqueID == None:
            return uniqueID

    # When given a hanger component that must be represented as a zero-length segment,
    # look for the CABLEWAY_HANGER_ID attribute on the component.
    if type(segmentPrototype) is NXOpen.Part:
        uniqueID = segmentObject.GetStringUserAttribute("CABLEWAY_HANGER_ID", -1)
        if not uniqueID == None:
            return uniqueID

    # Otherwise, create a new unique ID and return it.
    if not hasattr(CablewaySegmentName, "counter"):
        CablewaySegmentName.counter = 0

    CablewaySegmentName.counter += 1

    return str( segmentObject.Tag ) + "_" + str( CablewaySegmentName.counter )

#---------------------------------------------------------------------------------------------------
# Called while Routing exports a Cableway XML file to identify if the given component
# is a device that should be exported.
#
# \param[in]
#      component
#          The component to check.
#
# \return
#      The device ID to use for this component in the Cableway XML file.
#      Returns an empty string if this device should not be exported.
def CablewayDeviceIdentifier( component ):
    echo( "CablewayDeviceIdentifier" )

    deviceID = ""
    if component.HasUserAttribute( "Electrical_Device_ID", NXOpen.NXObject.AttributeType.String, -1 ):
        deviceID = component.GetStringUserAttribute( "Electrical_Device_ID", -1 )

    return deviceID

#---------------------------------------------------------------------------------------------------
# Called just after Routing exports a Cableway XML file.
#
# \param[in]
#      xmlFileName
#          The name of the XML file Routing just exported.
def CablewayPreExport( xmlFileName ):
    echo( "CablewayPreExport called with " + xmlFileName )

#---------------------------------------------------------------------------------------------------
# Called just after Routing exports a Cableway XML file.
#
# \param[in]
#      xmlFileName
#          The name of the XML file Routing just exported.
def CablewayPostExport( xmlFileName ):
    echo( "CablewayPostExport called with " + xmlFileName )

#---------------------------------------------------------------------------------------------------
# Called during Cableway export to create an area name for a given component and all
# the components under it.
#
# \param[in]
#      component
#          The component to check.
#
# \return
#      The area name to use for all the devices, hangers, nodes, segments, etc., found
#      under this component.
def CablewayAreaName( component ):
    echo( "CablewayAreaName" )

    areaName = ""
    if component.HasUserAttribute( "Electrical_Device_Area", NXOpen.NXObject.AttributeType.String, -1 ):
        areaName = component.GetStringUserAttribute( "Electrical_Device_Area", -1 )

    return areaName

#---------------------------------------------------------------------------------------------------
def RegisterPlugins():
    echo( "Python Register Plugins" )

    customManager = NXOpen.Session.GetSession().RoutingCustomManager

    customManager.SetCablewayXmlFileNamePlugin( CablewayXmlFileName )
    customManager.SetCablewayUniqueNodeNamePlugin( CablewayNodeName )
    customManager.SetCablewayUniqueSegmentNamePlugin( CablewaySegmentName )
    customManager.SetCablewayDeviceIdentifierPlugin( CablewayDeviceIdentifier )
    customManager.SetCablewayPreExportPlugin( CablewayPreExport )
    customManager.SetCablewayPostExportPlugin( CablewayPostExport )
    customManager.SetCablewayAreaNamePlugin( CablewayAreaName )

#---------------------------------------------------------------------------------------------------
def DeregisterPlugins():
    echo( "Python Deregister Plugins" )

    customManager = NXOpen.Session.GetSession().RoutingCustomManager

    customManager.RemoveCablewayXmlFileNamePlugin()
    customManager.RemoveCablewayUniqueNodeNamePlugin()
    customManager.RemoveCablewayUniqueSegmentNamePlugin()
    customManager.RemoveCablewayDeviceIdentifierPlugin()
    customManager.RemoveCablewayPreExportPlugin()
    customManager.RemoveCablewayPostExportPlugin()
    customManager.RemoveCablewayAreaNamePlugin()

#---------------------------------------------------------------------------------------------------
# Called when you change the discipline. Registers the Cableway plugins listed above
# if the new discipline is the cableway discipline. Otherwise, it deregisters the plugins.
def DisciplineChanged( previousDisciplineName, newDisciplineName ):

    echo( "Python DisciplineChanged" )

    cablewayDisciplineName = NXOpen.Session.GetSession().OptionsManager.GetStringValue( "RSD_Cableway_Discipline_Name" )

    # Register all the Cableways plugins if the new discipline is the Cableways discipline.
    if cablewayDisciplineName == newDisciplineName:
        echo( "  Registering Cableway plugins." )
        RegisterPlugins()
    else:
        echo( "  Deregistering Cableway plugins." )
        DeregisterPlugins()

#---------------------------------------------------------------------------------------------------
# Called when you enter one of the Routed System Designer (RSD) applications.
# When entering the Mechanical application, registers the DisciplineChanged plugin.
def ApplicationEnter( application ):

    try:
        echo( "Python Application Enter" )

        if application == NXOpen.RoutingCommon.CustomManager.Application.Electrical:
            echo( "Entering the Electrical application " )
        else:
            # When entering the Mechanical application, register a "discipline changed" plugin to
            # watch for a change to the Cableway discipline.
            echo( "Entering the Mechanical application " )

            routeCustomManager = NXOpen.Session.GetSession().RouteCustomManager

            routeCustomManager.SetDisciplineChangedPlugin( DisciplineChanged )

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    except:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXMessageBox.DialogType.Error, "Unknown exception" )

#---------------------------------------------------------------------------------------------------
# Called when you enter one of the Routed System Designer (RSD) applications.
# Unregisters the DisciplineChanged plugin.
def ApplicationExit( application ):

    try:
        echo( "Python Application Exit" )

        if application == NXOpen.RoutingCommon.CustomManager.Application.Electrical:
            echo( "Exiting the Electrical application " )
        else:
            echo( "Exiting the Mechanical application " )

        # When exiting any Routing application, remove the "discipline changed" plugin and the
        # "Cableways" plugins.
        NXOpen.Session.GetSession().RouteCustomManager.RemoveDisciplineChangedPlugin()
        DeregisterPlugins();

    except Exception as ex:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXMessageBox.DialogType.Error, str( ex ) )
        raise ex

    except:
        NXOpen.UI.GetUI().NXMessageBox.Show( "Python", NXMessageBox.DialogType.Error, "Unknown exception" )

#---------------------------------------------------------------------------------------------------
def startup( argc, args ):

    NXOpen.Session.GetSession().CreateRoutingSession()

    customManager = NXOpen.Session.GetSession().RoutingCustomManager

    customManager.SetRSDApplicationEnterPlugin( ApplicationEnter )
    customManager.SetRSDApplicationExitPlugin(  ApplicationExit )

    return 0 # No errors.

