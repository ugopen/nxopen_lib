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

#include <sstream>
#include <string>
#include <vector>
#include <uf.h>

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
#include <NXOpen/Routing_Electrical_WireDevice.hxx>
#include <NXOpen/Routing_ISegment.hxx>
#include <NXOpen/Routing_ISegmentCollection.hxx>
#include <NXOpen/Routing_Port.hxx>
#include <NXOpen/Routing_PortConnection.hxx>
#include <NXOpen/Routing_SegmentManager.hxx>
#include <NXOpen/Routing_Stock.hxx>
#include <NXOpen/Routing_Wire.hxx>
#include <NXOpen/Session.hxx>

using namespace NXOpen;
using namespace NXOpen::Routing;

DesignRules* NXOpen::Routing::theDesignRules;

// Prototype for ufsta
extern "C" DllExport void ufsta( char* param , int* returncode, int param_len );

//--------------------------------------------------------------------------------------------------
DesignRules::DesignRules()
    : m_createPathRuleId( -1 ), m_subdivideSegmentRuleId( -1 )
{
    Session*       session                     = Session::GetSession();
    CustomManager* customManager               = session->RouteCustomManager();
    NXString       createPathName              = "Create Path";
    NXString       subdivideSegmentName        = "Subdivide Segment";
    NXString       createPathDescription       = "The Create Path design rule makes sure each segment on the path is not too long.";
    NXString       subdivideSegmentDescription = "The Subdivide Segment design rule makes sure each new segment is not too short.";

    m_createPathRuleId = customManager->AddDesignRule( CustomManager::DesignRuleReasonCreatePath,
                                                       createPathName, createPathDescription,
                                                       make_callback(this, &DesignRules::CreatePathDesignRule) );

    m_subdivideSegmentRuleId = customManager->AddDesignRule( CustomManager::DesignRuleReasonSubdivideSegment,
                                                             subdivideSegmentName, subdivideSegmentDescription,
                                                             make_callback(this, &DesignRules::SubdivideSegmentDesignRule) );
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
// Called when NX starts up to register the Design Rules using the DesignRules class constructor.
// Called when NX starts up to register the plugins using the Plugins class constructor.
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
