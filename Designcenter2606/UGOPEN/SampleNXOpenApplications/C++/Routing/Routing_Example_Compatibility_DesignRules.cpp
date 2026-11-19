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
#include "Routing_Example_Compatibility_DesignRules.hpp"

#include <map>
#include <string>
#include <uf_defs.h>
#include <uf_ugopenint.h>
#include <vector>

#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/LicenseManager.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/MechanicalRouting_ConnectivityService.hxx>
#include <NXOpen/MechanicalRouting_RoutingManager.hxx>
#include <NXOpen/Options_OptionsManager.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Routing_ReuseLibrary.hxx>
#include <NXOpen/Routing_RouteManager.hxx>
#include <NXOpen/Routing_Stock.hxx>
#include <NXOpen/Routing_StockPort.hxx>
#include <NXOpen/RoutingCommon_CustomManager.hxx>
#include <NXOpen/Session.hxx>

using namespace NXOpen;
using namespace NXOpen::Routing;

ConnectionCompatibilityDesignRule* NXOpen::Routing::theDesignRule = nullptr;

// Prototype for ufsta
extern "C" DllExport void ufsta( char* param , int* returncode, int param_len );

using StlNXStringVector = std::vector< NXOpen::NXString >;
using StlStringMap      = std::map< std::string, std::string >;
using StlPortVector     = std::vector< NXOpen::Routing::Port* >;
using StlPortMap        = std::map< NXOpen::Routing::Port*, NXOpen::Routing::Port* >;
using StlBodyVector     = std::vector< NXOpen::Body* >;

static NXString                      designRuleName = "Connection Compatibility Design Rule";
static Session*                      theSession     = nullptr;
static RoutingCommon::CustomManager* customManager  = nullptr;
static StlStringMap                  compatibleConnections;
static StlNXStringVector             connectionAttributes;

//--------------------------------------------------------------------------------------------------
ConnectionCompatibilityDesignRule::ConnectionCompatibilityDesignRule()
{
    if ( theSession == nullptr )
        theSession = Session::GetSession();

    if ( customManager == nullptr )
        customManager = theSession->RoutingCustomManager();

    NXString description = "The compatibility design rule ensures piping connections are valid.";

    customManager->AddDesignRule( CustomManager::DesignRuleReasonConnectionCompatibility, designRuleName, description,
                                  make_callback( this, &ConnectionCompatibilityDesignRule::CompatibilityDesignRule ) );

    customManager->AddDesignRule( CustomManager::DesignRuleReasonPlacePart, designRuleName, description,
                                  make_callback( this, &ConnectionCompatibilityDesignRule::CompatibilityDesignRule ) );
};

//--------------------------------------------------------------------------------------------------
// The connection compatibility check is between two ports. Since connected ports are not
// normally displayed, this method tries to find the stock or the component that owns the
// port. These show up better when highlighted in the Design Rule Violation dialog.
static void addPortObjects
(
    Port*              port,
    StlNXObjectVector& objects
)
{
    if ( port->IsOccurrence() )
    {
        objects.emplace_back( port->GetComponent() );
        return;
    }

    auto* stockPort = dynamic_cast<StockPort*>( port );
    if ( stockPort != nullptr )
    {
        Stock*        stock       = stockPort->GetStock();
        StlBodyVector stockBodies = stock->GetBodies();

        for ( auto* stockBody : stockBodies )
            objects.emplace_back( stockBody );

        return;
    }

    objects.emplace_back( port );
}

//--------------------------------------------------------------------------------------------------
// Creates a new violation for the two connected ports.
static void createViolation
(
    Port*       port1,
    Port*       port2,
    std::string violationDescription
)
{
    std::string message = "The two objects are incompatible due to:\n";
    message += violationDescription;

    // Try to use the components that contain the ports in the violation since it's much
    // easier to see highlighted components than highlighted ports.
    StlNXObjectVector objects;
    addPortObjects( port1, objects );
    addPortObjects( port2, objects );

    // NOTE: The design rule name given on the violation must match the name given to the
    //       rule when registering.
    customManager->CreateViolationForReason( designRuleName,
                                             CustomManager::DesignRuleReasonConnectionCompatibility,
                                             "Incompatible connection", message, objects );
}

//--------------------------------------------------------------------------------------------------
// Finds the CONNECTION_TYPE attribute on each port and checks the values against the
// current specification's connection compatibility table to ensure the two values are
// compatible.
static void validateConnectionType
(
    Port* port1,
    Port* port2
)
{
    if ( !port1->HasUserAttribute( "CONNECTION_TYPE", NXObject::AttributeTypeString, -1 ) )
        return;

    if ( !port2->HasUserAttribute( "CONNECTION_TYPE", NXObject::AttributeTypeString, -1 ) )
        return;

    std::string port1ConnectionType( port1->GetUserAttributeAsString( "CONNECTION_TYPE", NXObject::AttributeTypeString, -1 ).GetLocaleText() );
    std::string port2ConnectionType( port2->GetUserAttributeAsString( "CONNECTION_TYPE", NXObject::AttributeTypeString, -1 ).GetLocaleText() );

    if ( compatibleConnections.contains( port1ConnectionType ) &&
         port2ConnectionType == compatibleConnections[port1ConnectionType] )
    {
        return;
    }

    if ( compatibleConnections.contains( port2ConnectionType ) &&
         port1ConnectionType == compatibleConnections[port2ConnectionType] )
    {
        return;
    }

    std::string violationDescription = "Invalid connection types " + port1ConnectionType + " and " + port2ConnectionType + ".";
    createViolation( port1, port2, violationDescription );
}

//--------------------------------------------------------------------------------------------------
// Validates that the values of the connection attributes listed in customer defaults are
// the same on the two ports.
static void validateConnectionAttributes
(
    Port* port1,
    Port* port2
)
{
    for ( auto& attribute : connectionAttributes )
    {
        if ( !port1->HasUserAttribute( attribute, NXObject::AttributeTypeAny, -1 ) )
            continue;

        if ( !port2->HasUserAttribute( attribute, NXObject::AttributeTypeAny, -1 ) )
            continue;

        // Get the attribute values as strings.
        // NOTE: This check can be made more complex by finding out the attribute types and
        //       comparing the attribute values for each type of attribute.
        std::string port1Value( port1->GetUserAttributeAsString( attribute, NXObject::AttributeTypeAny, -1 ).GetLocaleText() );
        std::string port2Value( port2->GetUserAttributeAsString( attribute, NXObject::AttributeTypeAny, -1 ).GetLocaleText() );
        if ( port1Value == port2Value )
            continue;

        std::string violationDescription = "Attribute ";
        violationDescription += attribute.GetLocaleText();
        violationDescription += " has different values (" + port1Value + " and " + port2Value + ").";
        createViolation( port1, port2, violationDescription );
    }
}

//--------------------------------------------------------------------------------------------------
static void validatePortPairs
(
    StlPortMap portPairs
)
{
    for ( auto& portPair : portPairs )
    {
        validateConnectionType( portPair.first, portPair.second );
        validateConnectionAttributes( portPair.first, portPair.second );
    }
}

//--------------------------------------------------------------------------------------------------
// For an interactive check, validates all the connected ports in the work part.
static void checkConnectionsInWorkPart()
{
    Part*                                   workPart   = theSession->Parts()->Work();
    MechanicalRouting::RoutingManager*      routingMgr = MechanicalRouting::RoutingManager::GetRoutingManager( theSession );
    MechanicalRouting::ConnectivityService* service    = routingMgr->ConnectivityService();

    StlPortVector connectedPorts1;
    StlPortVector connectedPorts2;
    service->GetConnectedPorts( workPart, connectedPorts1, connectedPorts2 );

    StlPortMap portPairs;

    for ( int index = 0; index < connectedPorts1.size(); ++index )
        portPairs[connectedPorts1[index]] = connectedPorts2[index];

    if ( !portPairs.empty() )
        validatePortPairs( portPairs );
}

//--------------------------------------------------------------------------------------------------
// For concurrent check (e.g. after placing a part), validates the connection ports of the
// given objects.
static void checkConnections
(
    StlNXObjectVector nxObjects
)
{
    MechanicalRouting::RoutingManager*      routingMgr = MechanicalRouting::RoutingManager::GetRoutingManager( theSession );
    MechanicalRouting::ConnectivityService* service    = routingMgr->ConnectivityService();

    StlPortMap portPairs;

    for ( auto& nxObject : nxObjects )
    {
        // TODO: Add a check for stock ports here.
        auto* component = dynamic_cast<Assemblies::Component*>( nxObject );
        if ( component == nullptr )
            continue;

        StlPortVector connectedPorts1;
        StlPortVector connectedPorts2;
        service->GetConnectedPortsFromComponent( component, connectedPorts1, connectedPorts2 );

        // Because we can get duplicate port pairs from two connected components, add the port
        // pairs to a set to ensure we have unique pairs.
        for ( int index = 0; index < connectedPorts1.size(); ++index )
            portPairs[connectedPorts1[index]] = connectedPorts2[index];
    }

    if ( !portPairs.empty() )
        validatePortPairs( portPairs );
}

//--------------------------------------------------------------------------------------------------
// Gets the connection compatibility pairs from the current specification, if any.
// Returns false if no pairs were found.
static bool getConnectionCompatibilities()
{
    Part*         workPart = theSession->Parts()->Work();
    RouteManager* routeMgr = workPart->RouteManager();
    ReuseLibrary* library  = routeMgr->ReuseLibrary();

    std::string activeSpecification( library->SpecificationsGetCurrent().GetLocaleText() );

    // If there is no specification, there's no reason to run the compatibility check.
    if ( activeSpecification.empty() || activeSpecification == "None" )
        return false;

    StlNXStringVector strings1;
    StlNXStringVector strings2;
    library->SpecificationsGetConnectionCompatibilities( activeSpecification, strings1, strings2 );

    // If the specification doesn't define any connection compatibilities,
    // there's no reason to run the compatibility check.
    if ( strings1.empty() || strings2.empty() )
        return false;

    // Build a dictionary of string1/string2 and string2/string1 to make it easy to find
    // a valid pair of compatible CONNECTION_TYPE attributes values.
    for ( int index = 0; index < strings1.size(); ++index )
    {
        if ( !compatibleConnections.contains( strings1[index].GetLocaleText() ) )
            compatibleConnections[strings1[index].GetLocaleText()] = strings2[index].GetLocaleText();

        if ( !compatibleConnections.contains( strings2[index].GetLocaleText() ) )
            compatibleConnections[strings2[index].GetLocaleText()] = strings1[index].GetLocaleText();
    }

    return true;
}

//--------------------------------------------------------------------------------------------------
void ConnectionCompatibilityDesignRule::CompatibilityDesignRule
(
    CustomManager::DesignRuleReason reason,
    StlNXObjectVector               nxObjects
)
{
    // If the current specification does not define a connection compatibility table,
    // do not proceed.
    if ( !getConnectionCompatibilities() )
        return;

    // This is the list of attributes whose values must match in any port-to-port connection.
    connectionAttributes = theSession->OptionsManager()->GetStringListValue( "RSD_ConnectionCompatibilityAttributes" );

    // For interactive checks, check all the connections in the work part.
    if ( reason == CustomManager::DesignRuleReasonInteractive )
    {
        checkConnectionsInWorkPart();
    }
    else
    {
        // Otherwise, check the connections among the given list of objects.
        checkConnections( nxObjects );
    }
}

//--------------------------------------------------------------------------------------------------
// Called when NX starts up to register the Design Rules using the ConnectionCompatibilityDesignRule class constructor.
extern "C" DllExport void ufsta
(
    char* /*param*/,
    int*  retcod,
    int   /*param_len*/
)
{
    *retcod = 0;

    theDesignRule = new ConnectionCompatibilityDesignRule();

    Session::GetSession()->LicenseManager()->ReleaseAll( nullptr );
}

//--------------------------------------------------------------------------------------------------
// Tells NX when to unload your application.
// For Routing callbacks, plugins, and Design Rules, this MUST return UF_UNLOAD_UG_TERMINATE.
extern int ufusr_ask_unload()
{
    return( UF_UNLOAD_UG_TERMINATE );
}
