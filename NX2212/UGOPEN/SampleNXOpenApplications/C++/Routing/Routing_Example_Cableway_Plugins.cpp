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

    A C++ class that implements example Routing Cableway plugins.

    See Routing_Example_Cableway_Plugins.hpp for the interface.


==================================================================================================*/
#include "Routing_Example_Cableway_Plugins.hpp"

#include <ctime>
#include <iomanip>
#include <sstream>
#include <uf_defs.h>
#include <uf_ugopenint.h>

#include <NXOpen/Curve.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/Options_OptionsManager.hxx>
#include <NXOpen/Preferences_RoutingApplicationView.hxx>
#include <NXOpen/Preferences_RoutingStock.hxx>
#include <NXOpen/Preferences_SessionPreferences.hxx>
#include <NXOpen/Routing_ArcSegment.hxx>
#include <NXOpen/Routing_ComponentNamePluginData.hxx>
#include <NXOpen/Routing_LineSegment.hxx>
#include <NXOpen/Routing_SplineSegment.hxx>
#include <NXOpen/RoutingCommon_CustomManager.hxx>
#include <NXOpen/Session.hxx>

using namespace NXOpen;
using namespace NXOpen::RoutingCommon;

Plugins* NXOpen::RoutingCommon::thePlugins;

//--------------------------------------------------------------------------------------------------
// Writes the given string to the Listing Window and the log file.
//
// \param[in]
//      stringToWrite
//          The string to write.
static void echo( const std::string& stringToWrite )
{
    Session*       session       = Session::GetSession();
    ListingWindow* listingWindow = session->ListingWindow();

    if ( !listingWindow->IsOpen() )
        listingWindow->Open();

    listingWindow->WriteFullline( stringToWrite.c_str() );

    LogFile* logFile = session->LogFile();
    logFile->WriteLine( stringToWrite.c_str() );
}

//--------------------------------------------------------------------------------------------------
void Plugins::ApplicationEnter
(
    CustomManager::Application application
)
{
    echo( "C++ Application Enter" );

    if ( application == RoutingCommon::CustomManager::ApplicationElectrical )
    {
        echo( "Entering the Electrical application " );
    }
    else
    {
        // When entering the Mechanical application, register a "discipline changed" plugin to
        // watch for a change to the Cableway discipline.
        echo( "Entering the Mechanical application " );

        Routing::CustomManager* customManager = Session::GetSession()->RouteCustomManager();

        auto* thePlugins = new Plugins();
        customManager->SetDisciplineChangedPlugin( make_callback( thePlugins, &Plugins::DisciplineChanged ) );
    }
}

//--------------------------------------------------------------------------------------------------
void Plugins::ApplicationExit
(
    CustomManager::Application application
)
{
    echo( "C++ Application Exit" );
    if ( application == RoutingCommon::CustomManager::ApplicationElectrical )
    {
        echo( "Exiting the Electrical application " );
    }
    else
    {
        echo( "Exiting the Mechanical application " );
    }

    // When exiting any Routing application, remove the "discipline changed" plugin and the
    // "Cableways" plugins
    Session::GetSession()->RouteCustomManager()->RemoveDisciplineChangedPlugin();

    thePlugins->Deregister();

    delete thePlugins;
    thePlugins = nullptr;
}

//--------------------------------------------------------------------------------------------------
void Plugins::DisciplineChanged
(
    NXString previousDisciplineName,
    NXString newDisciplineName
)
{
    echo( "C++ DisciplineChanged" );

    Session* session = Session::GetSession();
    static std::string cablewayDisciplineName = session->OptionsManager()->GetStringValue( "RSD_Cableway_Discipline_Name" ).GetText();

    if ( thePlugins == nullptr )
        thePlugins = new Plugins();

    // Register all the Cableways plugins if the new discipline is the Cableways discipline.
    if ( cablewayDisciplineName == newDisciplineName.GetText() )
    {
        echo( "  Registering Cableway plugins." );
        thePlugins->Register();
    }
    else
    {
        echo( "  Deregistering Cableway plugins." );
        thePlugins->Deregister();
    }
}

//--------------------------------------------------------------------------------------------------
void Plugins::Register()
{
    echo( "C++ Register" );

    Session*       session       = Session::GetSession();
    CustomManager* customManager = session->RoutingCustomManager();

    customManager->SetCablewayXmlFileNamePlugin(       make_callback( this, &Plugins::CablewayXmlFileName      ) );
    customManager->SetCablewayUniqueNodeNamePlugin(    make_callback( this, &Plugins::CablewayNodeName         ) );
    customManager->SetCablewayUniqueSegmentNamePlugin( make_callback( this, &Plugins::CablewaySegmentName      ) );
    customManager->SetCablewayDeviceIdentifierPlugin(  make_callback( this, &Plugins::CablewayDeviceIdentifier ) );
    customManager->SetCablewayPreExportPlugin(         make_callback( this, &Plugins::CablewayPreExport        ) );
    customManager->SetCablewayPostExportPlugin(        make_callback( this, &Plugins::CablewayPostExport       ) );
    customManager->SetCablewayAreaNamePlugin(          make_callback( this, &Plugins::CablewayAreaName         ) );
};

//--------------------------------------------------------------------------------------------------
void Plugins::Deregister()
{
    echo( "C++ Deregister" );

    Session*       session       = Session::GetSession();
    CustomManager* customManager = session->RoutingCustomManager();

    customManager->RemoveCablewayXmlFileNamePlugin();
    customManager->RemoveCablewayUniqueNodeNamePlugin();
    customManager->RemoveCablewayUniqueSegmentNamePlugin();
    customManager->RemoveCablewayDeviceIdentifierPlugin();
    customManager->RemoveCablewayPreExportPlugin();
    customManager->RemoveCablewayPostExportPlugin();
    customManager->RemoveCablewayAreaNamePlugin();
};

//--------------------------------------------------------------------------------------------------
NXString Plugins::CablewayXmlFileName()
{
    echo( "C++ CablewayXmlFileName" );

    time_t now = time( nullptr );
    tm*    ltm = localtime( &now );

    std::stringstream fileName;
    fileName << "RoutingCablewayExport_";
    fileName << 1900 + ltm->tm_year << "_";
    fileName << std::setw( 2 ) << std::setfill( '0' ) << 1 + ltm->tm_mon << "_";
    fileName << std::setw( 2 ) << std::setfill( '0' ) << ltm->tm_mday << "_";
    fileName << std::setw( 2 ) << std::setfill( '0' ) << ltm->tm_hour << "_";
    fileName << std::setw( 2 ) << std::setfill( '0' ) << ltm->tm_min;
    fileName << ".xml";

    return NXString( fileName.str().c_str() );
};

//--------------------------------------------------------------------------------------------------
NXString Plugins::CablewayNodeName
(
    NXString               areaName,
    Assemblies::Component* cablewaySubassembly,
    NXObject*              nodeObjectOccurrence
)
{
    echo( "C++ CablewayNodeName" );

    // If the node object occurrence already has a name, just return it.
    if ( nodeObjectOccurrence->Name().GetText() == nullptr || strlen( nodeObjectOccurrence->Name().GetText() ) > 0 )
        return nodeObjectOccurrence->Name();

    static int nodeCounter = 0;
    ++nodeCounter;

    std::stringstream nodeName;
    nodeName << nodeObjectOccurrence->Tag() << "_" << nodeCounter;

    return NXString( nodeName.str().c_str() );
};

//--------------------------------------------------------------------------------------------------
NXString Plugins::CablewaySegmentName
(
    NXString               areaName,
    Assemblies::Component* cablewaySubassembly,
    NXObject*              segmentObject
)
{
    echo( "C++ CablewaySegmentName" );

    INXObject* segmentPrototype = segmentObject->Prototype();

    // When given the entity occurrence of a Routing segment or a curve, check the curve name for an
    // existing unique ID.
    if ( dynamic_cast<NXOpen::Routing::ArcSegment*>( segmentPrototype )    != nullptr ||
         dynamic_cast<NXOpen::Routing::LineSegment*>( segmentPrototype )   != nullptr ||
         dynamic_cast<NXOpen::Routing::SplineSegment*>( segmentPrototype ) != nullptr ||
         dynamic_cast<NXOpen::Arc*>( segmentPrototype )    != nullptr ||
         dynamic_cast<NXOpen::Line*>( segmentPrototype )   != nullptr ||
         dynamic_cast<NXOpen::Spline*>( segmentPrototype ) != nullptr )
    {
        NXString uniqueID = segmentObject->Name();
        if ( uniqueID.GetText() != nullptr && strlen( uniqueID.GetText() ) > 0 )
            return uniqueID;
    }

    // When given a hanger component that must be represented as a zero-length segment,
    // look for the CABLEWAY_HANGER_ID attribute on the component.
    if ( dynamic_cast<NXOpen::Part*>( segmentPrototype ) != nullptr )
    {
        NXString uniqueID = segmentObject->GetStringUserAttribute( "CABLEWAY_HANGER_ID", -1 );
        if ( uniqueID.GetText() != nullptr && strlen( uniqueID.GetText() ) > 0 )
            return uniqueID;
    }

    // Otherwise, create a new unique ID and return it.
    static int segmentCounter = 0;
    ++segmentCounter;

    std::stringstream segmentName;
    segmentName << segmentObject->Tag() << "_" << segmentCounter;

    return NXString( segmentName.str().c_str() );
};

//--------------------------------------------------------------------------------------------------
NXString Plugins::CablewayDeviceIdentifier
(
    Assemblies::Component* component
)
{
    echo( "C++ CablewayDeviceIdentifier" );

    // Get the name of the device ID attribute from the customer defaults.
    std::string deviceIDAttribute = Session::GetSession()->OptionsManager()->GetStringValue( "RSD_Cableway_Device_ID_Attribute" ).GetText();

    // If the component has a device ID, then it must be a device.
    NXString deviceID;
    if ( component->HasUserAttribute( deviceIDAttribute, NXObject::AttributeTypeString, -1 ) )
        deviceID = component->GetStringUserAttribute( deviceIDAttribute, -1 );

    return deviceID.GetText();
};

//--------------------------------------------------------------------------------------------------
void Plugins::CablewayPreExport
(
    NXString xmlFileName
)
{
    std::stringstream message;
    message << "C++ CablewayPreExport called with " << xmlFileName.GetText();

    echo( message.str() );
}

//--------------------------------------------------------------------------------------------------
void Plugins::CablewayPostExport
(
    NXString xmlFileName
)
{
    std::stringstream message;
    message << "C++ CablewayPostExport called with " << xmlFileName.GetText();

    echo( message.str() );
}

//--------------------------------------------------------------------------------------------------
NXString Plugins::CablewayAreaName
(
    Assemblies::Component* component
)
{
    echo( "C++ CablewayAreaName" );

    std::string areaNameAttribute = Session::GetSession()->OptionsManager()->GetStringValue( "RSD_Cableway_Area_Attribute" ).GetText();

    NXString areaName;
    if ( component->HasUserAttribute( areaNameAttribute, NXObject::AttributeTypeAny, -1 ) )
        areaName = component->GetUserAttributeAsString( areaNameAttribute, NXObject::AttributeTypeAny, -1 );

    return areaName;
}

//--------------------------------------------------------------------------------------------------
// Called from File->Execute->NX Open. Useful for testing.
extern "C" DllExport void ufusr
(
    char* /*param*/,
    int*  retcod,
    int   /*param_len*/
)
{
    *retcod = 0;

    Session* session = Session::GetSession();

    // Calling CreateRoutingSession is required before registering Routed System Designer (RSD)
    // plugins, callbacks, or design rules to ensure the Routing libraries are properly loaded.
    session->CreateRoutingSession();

    CustomManager* customManager = Session::GetSession()->RoutingCustomManager();

    thePlugins = new Plugins();
    customManager->SetRSDApplicationEnterPlugin( make_callback( thePlugins, &Plugins::ApplicationEnter ) );
    customManager->SetRSDApplicationExitPlugin(  make_callback( thePlugins, &Plugins::ApplicationExit ) );
}

//--------------------------------------------------------------------------------------------------
// Called by NX at startup. Registers the "enter" and "exit" application plugins.
extern "C" DllExport void ufsta
(
    char* /*param*/,
    int* retcod,
    int   /*param_len*/
)
{
    *retcod = 0;

    Session* session = Session::GetSession();

    // Calling CreateRoutingSession is required before registering Routed System Designer (RSD)
    // plugins, callbacks, or design rules to ensure the Routing libraries are properly loaded.
    session->CreateRoutingSession();

    CustomManager* customManager = session->RoutingCustomManager();

    thePlugins = new Plugins();
    customManager->SetRSDApplicationEnterPlugin( make_callback( thePlugins, &Plugins::ApplicationEnter ) );
    customManager->SetRSDApplicationExitPlugin(  make_callback( thePlugins, &Plugins::ApplicationExit  ) );
}

//--------------------------------------------------------------------------------------------------
// Tells NX when to unload your application.
// For Routing callbacks, plugins, and Design Rules, this MUST return UF_UNLOAD_UG_TERMINATE.
extern int ufusr_ask_unload()
{
    return( UF_UNLOAD_UG_TERMINATE );
}
