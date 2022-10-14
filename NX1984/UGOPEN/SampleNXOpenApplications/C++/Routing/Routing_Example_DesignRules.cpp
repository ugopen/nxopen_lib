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

    A C++ class that implements example Routing Design Rules.

    See Routing_Example_DesignRules.hpp for the interface.


==================================================================================================*/
#include "Routing_Example_DesignRules.hpp"

#include <map>
#include <set>
#include <sstream>
#include <string>
#include <uf.h>
#include <uf_rlist.h>
#include <vector>

#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Curve.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Preferences_RoutingApplicationView.hxx>
#include <NXOpen/Preferences_RoutingUserPreferences.hxx>
#include <NXOpen/Preferences_SessionPreferences.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Routing_Electrical_ConnectorDeviceCollection.hxx>
#include <NXOpen/Routing_Electrical_WireDevice.hxx>
#include <NXOpen/Routing_ISegment.hxx>
#include <NXOpen/Routing_ISegmentCollection.hxx>
#include <NXOpen/Routing_Port.hxx>
#include <NXOpen/Routing_PortCollection.hxx>
#include <NXOpen/Routing_PortConnection.hxx>
#include <NXOpen/Routing_PortConnectionCollection.hxx>
#include <NXOpen/Routing_RouteManager.hxx>
#include <NXOpen/Routing_SegmentManager.hxx>
#include <NXOpen/Routing_Stock.hxx>
#include <NXOpen/Routing_Wire.hxx>
#include <NXOpen/Session.hxx>

using namespace NXOpen;
using namespace NXOpen::Routing;
using namespace NXOpen::Routing::Electrical;

DesignRules* NXOpen::Routing::theDesignRules;

// Prototype for ufsta
extern "C" DllExport void ufsta( char* param , int* returncode, int param_len );

using StlCharxInfoVector = std::vector < CharacteristicList::CharacteristicInformation >;
using StlStringSet       = std::set< std::string >;
using StlPortVector      = std::vector< Port* >;

//--------------------------------------------------------------------------------------------------
DesignRules::DesignRules()
    : m_createPathRuleId( -1 ), m_subdivideSegmentRuleId( -1 )
{
    Session*       session                     = Session::GetSession();
    CustomManager* customManager               = session->RouteCustomManager();
    NXString       createPathName              = "Create Path";
    NXString       subdivideSegmentName        = "Subdivide Segment";
    NXString       modularConnectorName        = "Modular Connector";
    NXString       createPathDescription       = "The Create Path design rule makes sure each segment on the path is not too long.";
    NXString       subdivideSegmentDescription = "The Subdivide Segment design rule makes sure each new segment is not too short.";
    NXString       modularConnectorDescription = "The Modular Connector rule makes sure modular connectors are plugged into the correct position on the parent shell.";

    m_createPathRuleId = customManager->AddDesignRule( CustomManager::DesignRuleReasonCreatePath,
                                                       createPathName, createPathDescription,
                                                       make_callback(this, &DesignRules::CreatePathDesignRule) );

    m_subdivideSegmentRuleId = customManager->AddDesignRule( CustomManager::DesignRuleReasonSubdivideSegment,
                                                             subdivideSegmentName, subdivideSegmentDescription,
                                                             make_callback(this, &DesignRules::SubdivideSegmentDesignRule) );

    m_modularConnectorRuleId = customManager->AddDesignRule( CustomManager::DesignRuleReasonInteractive,
                                                             modularConnectorName, modularConnectorDescription,
                                                             make_callback(this, &DesignRules::ModularConnectorDesignRule) );
};

//--------------------------------------------------------------------------------------------------
// Checks the length of the given segment against the maximum allowed length.
//
// Creates a violation for the given reason if the segment is too long.
//
// \param[in]
//      customManager
//          Used to create a new violation for segments that are too long.
//
// \param[in]
//      maximumLength
//          The longest length allowed.
//
// \param[in]
//      segment
//          The segment to check.
static void checkForLongSegments
(
    CustomManager* customManager,
    NXString       designRuleName,
    double         maximumLength,
    ISegment*      segment
)
{
    if ( segment->Length() < maximumLength )
        return;

    std::vector<NXOpen::NXObject *> objects;
    objects.push_back( dynamic_cast<Curve*>( segment ) );

    customManager->CreateViolationForReason( designRuleName, 
                                             CustomManager::DesignRuleReasonCreatePath,
                                             "This path is too long.",
                                             "Long paths need to be broken up and supported by clamps.",
                                             objects );
}

//--------------------------------------------------------------------------------------------------
void DesignRules::CreatePathDesignRule
(
    CustomManager::DesignRuleReason reason,
    StlNXObjectVector               objects
)
{
    NXString       createPathName = "Create Path";
    Session*       session        = Session::GetSession();
    CustomManager* customManager  = session->RouteCustomManager();

    double maximumLength = 1000.0;

    if ( reason == CustomManager::DesignRuleReasonInteractive )
    {
        // For interactive checks, check all the segments in the work part.
        SegmentManager*     segmentManager    = session->Parts()->Work()->SegmentManager();
        ISegmentCollection* segmentCollection = segmentManager->Segments();

        for ( ISegment* segment : *segmentCollection )
            checkForLongSegments( customManager, createPathName, maximumLength, segment );

        return;
    }

    // Otherwise, check the segments in the given list of objects.
    for ( NXObject* object : objects )
    {
        ISegment* segment = dynamic_cast<ISegment*>( object );
        if ( segment != nullptr )
            checkForLongSegments( customManager, createPathName, maximumLength, segment );
    }
};

//--------------------------------------------------------------------------------------------------
// Checks the length of the given segment against the minimum allowed length.
//
// Creates a violation for the given reason if the segment is too short.
//
// \param[in]
//      customManager
//          Used to create a new violation for segments that are too short.
//
// \param[in]
//      minimumLength
//          The shortest length allowed.
//
// \param[in]
//      segment
//          The segment to check.
static void checkForShortSegments
(
    CustomManager* customManager,
    NXString       designRuleName,
    double         minimumLength,
    ISegment*      segment
)
{
    if ( segment->Length() > minimumLength )
        return;

    std::vector<NXOpen::NXObject *> objects;
    objects.push_back( dynamic_cast<Curve*>( segment ) );

    customManager->CreateViolationForReason( designRuleName,
                                             CustomManager::DesignRuleReasonSubdivideSegment,
                                             "This segment is too short.",
                                             "Short segments violate our design standards.",
                                             objects );
}

//--------------------------------------------------------------------------------------------------
void DesignRules::SubdivideSegmentDesignRule
(
    CustomManager::DesignRuleReason reason,
    StlNXObjectVector               objects
)
{
    NXString       subdivideSegmentName = "Subdivide Segment";
    Session*       session = Session::GetSession();
    CustomManager* customManager = session->RouteCustomManager();

    Preferences::RoutingUserPreferences* userPreferences = session->Preferences()->RoutingApplicationView()->RoutingUserPreferences();

    double minimumLength = 0.0;
    if ( !userPreferences->GetDoublePreference( "ROUTE_ELEC_MIN_STRAIGHT_LENGTH_COEFF", &minimumLength ) )
        minimumLength = 10.0;

    if ( reason == CustomManager::DesignRuleReasonInteractive )
    {
        // For interactive checks, check all the segments in the work part.
        SegmentManager*     segmentManager    = session->Parts()->Work()->SegmentManager();
        ISegmentCollection* segmentCollection = segmentManager->Segments();

        for ( ISegment* segment : *segmentCollection )
            checkForShortSegments( customManager, subdivideSegmentName, minimumLength, segment );

        return;
    }

    // Otherwise, check the segments in the given list of objects.
    for ( NXObject* object : objects )
    {
        ISegment* segment = dynamic_cast<ISegment*>( object );
        if ( segment != nullptr )
            checkForShortSegments( customManager, subdivideSegmentName, minimumLength, segment );
    }
}

//--------------------------------------------------------------------------------------------------
// Safely gets the value of a string characteristic if it exists on the route object.
//
// \param[in]
//      routeObject 
//          The object from which to get the characteristic.
//
// \param[in]
//      characteristicName 
//          The name of the characteristic to get.
//
// \return
//      The string value of the characteristic. Will be empty if the characteristic does not exist
//      or is not a string.
static std::string getCharacteristicFromObject
(
    const RouteObject* routeObject,
    const std::string& characteristicName
)
{
    CharacteristicList* characteristics     = const_cast<RouteObject*>( routeObject )->GetCharacteristics();
    StlCharxInfoVector  characteristicsInfo = characteristics->GetCharacteristicTitlesByType( NXObject::AttributeTypeAny );

    for ( const auto& characteristicInfo : characteristicsInfo )
    {
        if ( characteristicName           == characteristicInfo.Name.GetText() &&
             characteristicInfo.Type == NXObject::AttributeTypeString )
        {
            return std::string( characteristics->GetStringCharacteristic( characteristicName ).GetText() );
        }
    }

    return std::string();
}

//--------------------------------------------------------------------------------------------------
// Returns the names of the ports to which the connector is connected through a port connection.
//
// \param[in]
//      connector 
//          The connector to check.
//
// \return
//      The names of the ports to which this connector is connected. Will be empty if the connector
//      is not assigned to a component or if the component's ports are not connected to any other
//      ports.
static StlStringSet getConnectedPortNames
(
    ConnectorDevice* connector
)
{
    if ( !connector->IsAssigned() )
        return StlStringSet();

    auto assignedComponent = dynamic_cast<Assemblies::Component*>( connector->NxEquivalent() );
    if ( assignedComponent == nullptr )
        return StlStringSet();

    RouteManager* routeManager           = Session::GetSession()->Parts()->Work()->RouteManager();
    StlPortVector assignedComponentPorts = routeManager->Ports()->GetComponentPorts( assignedComponent );
    if ( assignedComponentPorts.empty() )
        return StlStringSet();

    StlStringSet connectedPortNames;

    PortConnectionCollection* portConnections = routeManager->PortConnections();
    for ( const auto& assignedComponentPort : assignedComponentPorts )
    {
        PortConnection* portConnection = portConnections->GetConnectionFromPort( assignedComponentPort );
        if ( portConnection == nullptr )
            continue;

        Port* port1 = nullptr;
        Port* port2 = nullptr;
        portConnection->GetPorts( &port1, &port2 );

        // We know the port on the connector, so get the name from the other port in the connection.
        connectedPortNames.insert( assignedComponentPort != port1 ? port1->Name().GetText() : port2->Name().GetText() );
    }

    return connectedPortNames;
}

//--------------------------------------------------------------------------------------------------
void DesignRules::ModularConnectorDesignRule
(
    CustomManager::DesignRuleReason reason,
    StlNXObjectVector               /*objects*/
)
{
    if ( reason != CustomManager::DesignRuleReasonInteractive )
        return;

    Session*                   session       = Session::GetSession();
    RouteManager*              routeManager  = session->Parts()->Work()->RouteManager();
    CustomManager*             customManager = session->RouteCustomManager();
    ConnectorDeviceCollection* connectors    = routeManager->ConnectorDevices();

    // For every Connector Device that is assigned and has a modular connector parent,
    // check that the assigned component is at the correct position (i.e. the correct port).
    for ( const auto& connector : *connectors )
    {
        if ( !connector->IsAssigned() )
            continue;

        std::string parentConnectorName = getCharacteristicFromObject( connector, UF_RLIST_PARENT_ID_NAME );
        if ( parentConnectorName.empty() )
            continue;

        std::string parentPortName  = getCharacteristicFromObject( connector, UF_RLIST_PARENT_POSITION_NAME );
        if ( parentPortName.empty() )
            continue;

        bool connectedCorrectly = false;
        std::string portNamesForMessage;
        StlStringSet connectedPortNames = getConnectedPortNames( connector );
        for ( const auto& connectedPortName : connectedPortNames )
        {
            portNamesForMessage += connectedPortName + ", ";

            if ( connectedPortName == parentPortName )
            {
                connectedCorrectly = true;
                break;
            }
        }

        if ( !connectedCorrectly )
        {
            StlNXObjectVector objects;
            objects.push_back( connector->NxEquivalent() );

            std::stringstream message;
            message << "Connector " << connector->Name().GetText();
            message << " is connected to port(s) " << portNamesForMessage;
            message << "but should be connected to port " << parentPortName;
            message << " on connector " << parentConnectorName << ".";

            customManager->CreateViolationForReason( "Modular Connector", reason,
                                                     "Component connected to wrong port.",
                                                     message.str().c_str(), objects );
        }
    }
}

//--------------------------------------------------------------------------------------------------
// Called when NX starts up to register the Design Rules using the DesignRules class constructor.
extern "C" DllExport void ufsta
(
    char* /*param*/,
    int*  retcod,
    int   /*param_len*/
)
{
    *retcod = 0;

    theDesignRules = new DesignRules();
}

//--------------------------------------------------------------------------------------------------
// Tells NX when to unload your application.
// For Routing callbacks, plugins, and Design Rules, this MUST return UF_UNLOAD_UG_TERMINATE.
extern int ufusr_ask_unload()
{
    return( UF_UNLOAD_UG_TERMINATE );
}
