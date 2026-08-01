/*==================================================================================================

    This material contains trade secrets or otherwise confidential information owned by
    Siemens Industry Software Inc. or its affiliates (collectively, "SISW"), or its licensors.
    Access to and use of this information is strictly limited as set forth in the Customer's
    applicable agreements with SISW.

    Unpublished work Copyright 2023 Siemens

====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A C++ class that implements example Routing Spool plugins.

    See Routing_Example_Spool_Plugins.hpp for the interface.


==================================================================================================*/
#include "Routing_Example_Spool_Plugins.hpp"

#include <algorithm>
#include <array>
#include <ctime>
#include <filesystem>
#include <functional>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <uf.h>
#include <uf_defs.h>
#include <uf_ugmgr.h>
#include <uf_ugmgr_types.h>
#include <uf_ugopenint.h>

#include <NXOpen/LicenseManager.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/MechanicalRouting_CollectionsManager.hxx>
#include <NXOpen/MechanicalRouting_RoutingManager.hxx>
#include <NXOpen/MechanicalRouting_RunsAssignmentManager.hxx>
#include <NXOpen/MechanicalRouting_Spool.hxx>
#include <NXOpen/MechanicalRouting_SpoolCollection.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Options_OptionsManager.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Routing_AssemblyNamePluginData.hxx>
#include <NXOpen/RoutingCommon_CustomManager.hxx>
#include <NXOpen/Schematic_Mechanical_Run.hxx>
#include <NXOpen/Session.hxx>

using namespace NXOpen;
using namespace NXOpen::RoutingCommon;

SpoolPlugins* NXOpen::RoutingCommon::theSpoolPlugins;

using StlAttributeInformationVector = std::vector < NXObject::AttributeInformation >;

using NXOpen::MechanicalRouting::RunsAssignmentManager;
using NXOpen::MechanicalRouting::RoutingManager;
using NXOpen::MechanicalRouting::Spool;
using NXOpen::MechanicalRouting::SpoolCollection;
using NXOpen::Schematic::Mechanical::Run;

//--------------------------------------------------------------------------------------------------
// Returns true and the attribute information object of the attribute if the attribute is in the list.
// Returns false if not.
// NOTE: The attribute name comparison is case insensitive.
static bool getAttributeFromList
(
    const StlAttributeInformationVector& attributes,
    const std::string&                   attributeName,
    NXObject::AttributeInformation&      attributeInformation
)
{
    for ( const auto& attribute : attributes )
    {
        NXString titleString = attribute.Title;

        // Watch out for attributes with no title.
        if ( titleString.GetLocaleText() == nullptr )
            continue;

        std::string title( titleString.GetLocaleText() );

        std::string titleAlias;
        if ( attribute.TitleAlias.GetLocaleText() != nullptr )
            titleAlias = attribute.TitleAlias.GetLocaleText();

        if ( (title == attributeName || titleAlias == attributeName) )
        {
            attributeInformation = attribute;
            return true;
        }
    }

    return false;
}

//--------------------------------------------------------------------------------------------------
// Returns the string value of the attribute or an empty string if it does not exist.
static std::string getStringAttributeValueFromObject
(
    const NXObject*    object,
    const std::string& attributeName
)
{
    NXObject::AttributeInformation attributeInformation;

    if ( getAttributeFromList( const_cast<NXObject*>(object)->GetUserAttributes(), attributeName, attributeInformation ) )
        return std::string( attributeInformation.StringValue.GetUTF8Text() );

    return {};
}

//--------------------------------------------------------------------------------------------------
// Returns the spool part's name as the "Block" to add to the spool name.
static std::string getBlock
(
    Part* spoolPart
)
{
    if ( spoolPart == nullptr )
        return {};

    std::string partName( spoolPart->Name().GetUTF8Text() );

    size_t seperator = partName.find_last_of( "\\" );
    if ( seperator != std::string::npos )
        partName = partName.substr( seperator + 1, partName.size() - seperator - 1 );

    return partName;
}

//--------------------------------------------------------------------------------------------------
// Uses the runs assignment manager to figure out which run this component belongs to.
static std::string getRun
(
    RunsAssignmentManager* runsManager,
    Assemblies::Component* component
)
{
    std::vector<Run*> runs = runsManager->GetAssignedRuns( component );
    for ( Run* run : runs )
    {
        std::string runId( run->Identifier().GetUTF8Text() );
        if ( !runId.empty() )
            return runId;
    }
    
    return {};
}

//--------------------------------------------------------------------------------------------------
// Gets the specification and the run from the components selected for the spool.
static void getSpecificationAndRun
(
    StlComponentVector spoolComponents,
    std::string&       specification,
    std::string&       runId
)
{
    RunsAssignmentManager* runsManager = RoutingManager::GetRoutingManager( Session::GetSession() )->RunsAssignmentManager();

    for ( Assemblies::Component* spoolComponent : spoolComponents )
    {
        std::string componentSpecification = getStringAttributeValueFromObject( spoolComponent, "SPECIFICATION" );
        if ( !componentSpecification.empty() )
            specification = componentSpecification;

        std::string componentRun = getRun( runsManager, spoolComponent );
        if ( !componentRun.empty() )
            runId = componentRun;

        if ( !specification.empty() && !runId.empty() )
            break;
    }
}

//--------------------------------------------------------------------------------------------------
// Builds a description of the spool that includes:
// 
//   - Prefix:        The spool Name Prefix defined in the Routed System Designer->Mechanical->Spools customer defaults.
//   - Block:         The Block identifier is simply the name of the work part.
//   - Specification: The specification assigned to the components.
//   - Run ID:        The identifier of the run to which the components belong.
//
static std::string buildSpoolDescription
(
    Part*              spoolPart,
    StlComponentVector spoolComponents
)
{
    Session*    session   = Session::GetSession();
    std::string prefix    = session->OptionsManager()->GetStringValue( "RSD_SpoolNamePrefix" ).GetText();
    std::string blockName = getBlock( spoolPart );

    std::string specification;
    std::string runId;
    getSpecificationAndRun( spoolComponents, specification, runId );

    std::stringstream description;
    if ( !prefix.empty() )
        description << prefix;

    if ( !blockName.empty() )
        description << blockName + " ";

    if ( !specification.empty() )
        description << specification + " ";

    if ( !runId.empty() )
        description << runId + " ";

    return description.str();
}

//--------------------------------------------------------------------------------------------------
// Returns the name of the spool that owns the given components.
//
// This assumes all components belong to the same spool and only belong to one spool.
//
static std::string getSpoolName
(
    StlComponentVector spoolComponents
)
{
    if ( spoolComponents.empty() )
        return {};

    Session*         session           = Session::GetSession();
    Part*            workPart          = session->Parts()->Work();
    SpoolCollection* spoolCollection   = workPart->MechanicalRoutingCollectionsManager()->Spools();

    Spool* spool = spoolCollection->GetSpoolFromComponent( spoolComponents[0] );
    if ( spool == nullptr )
        return {};

    return std::string( spool->Name().GetText() );
}

//--------------------------------------------------------------------------------------------------
NXString SpoolPlugins::GenerateSpoolName
(
    Part*              spoolPart,
    StlComponentVector spoolComponents
)
{
    SpoolCollection* spools = spoolPart->MechanicalRoutingCollectionsManager()->Spools();
    int nSpools = 0;
    for ( Spool* spool : *spools )
        ++nSpools;

    std::stringstream generatedName;
    generatedName << buildSpoolDescription( spoolPart, spoolComponents );
    generatedName << std::setw( 3 ) << std::setfill( '0' ) << nSpools;

    std::string message( generatedName.str() );
    message += " was created.";
    ListingWindow* listingWindow = Session::GetSession()->ListingWindow();
    listingWindow->Open();
    listingWindow->WriteFullline( message.c_str() );

    return { generatedName.str().c_str() };
}

//-------------------------------------------------------------------------------------------------
void SpoolPlugins::GenerateSpoolAssemblyName
(
    StlComponentVector               spoolComponents,
    Routing::AssemblyNamePluginData* dataObject
)
{
    // This example simply uses a static counter to create a name for the new assembly.
    static int spoolAssemblyCounter = 0;
    ++spoolAssemblyCounter;

    std::stringstream assemblyName;
    assemblyName << "SpoolAssembly_" << std::setw( 4 ) << std::setfill( '0' ) << spoolAssemblyCounter;

    if ( Session::GetSession()->PdmSession() == nullptr )
    {
        dataObject->SetNativeFileName( assemblyName.str().c_str() );
        dataObject->SetNativePath( "" ); // An empty path means the current directory.
        return;
    }

    // Find the home folder and then append the name of the folder that should hold the spool assembly.
    char homeFolder[UF_UGMGR_NAME_BUFSIZE] = "";

    UF_initialize();

    tag_t rootFolderTag;
    UF_UGMGR_ask_root_folder( &rootFolderTag );
    UF_UGMGR_ask_folder_name( rootFolderTag, homeFolder );

    std::stringstream managedModeFolderName;
    managedModeFolderName << homeFolder << ":SpoolAssembly";

    dataObject->SetManagedModeFolderName( managedModeFolderName.str().c_str() );
    dataObject->SetManagedModeItemName( "" ); // Return an empty item name to get the next available item ID.
    dataObject->SetManagedModeItemRevision( "A" );
    dataObject->SetManagedModeItemType( "Item" );
    dataObject->SetManagedModeItemDescription( getSpoolName( spoolComponents ) );

    UF_terminate();
}

//--------------------------------------------------------------------------------------------------
// Called when NX starts up to register the plugins using the SpoolPlugins class constructor.
extern "C" DllExport void ufsta
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

    RoutingCommon::CustomManager* customManager = session->RoutingCustomManager();

    theSpoolPlugins = new SpoolPlugins();
    customManager->SetSpoolNamePlugin(         make_callback( theSpoolPlugins, &SpoolPlugins::GenerateSpoolName         ) );
    customManager->SetSpoolAssemblyNamePlugin( make_callback( theSpoolPlugins, &SpoolPlugins::GenerateSpoolAssemblyName ) );
}

//--------------------------------------------------------------------------------------------------
// Tells NX when to unload your application.
// For Routing callbacks, plugins, and Design Rules, this MUST return UF_UNLOAD_UG_TERMINATE.
extern int ufusr_ask_unload()
{
    return( UF_UNLOAD_UG_TERMINATE );
}
