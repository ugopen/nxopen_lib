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

    A C++ class that implements example Routing plugins.

    See Routing_Example_Plugins.hpp for the interface.


==================================================================================================*/
#include "Routing_Example_Plugins.hpp"

#include <algorithm>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <uf.h>
#include <uf_route.h>
#include <uf_ugmgr.h>
#include <uf_ui.h>
#include <uf_ui_types.h>

#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/Curve.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/Preferences_PartPreferences.hxx>
#include <NXOpen/Preferences_RoutingApplicationView.hxx>
#include <NXOpen/Preferences_RoutingElectrical.hxx>
#include <NXOpen/Preferences_RoutingPart.hxx>
#include <NXOpen/Preferences_RoutingPartLibrary.hxx>
#include <NXOpen/Preferences_SessionPreferences.hxx>
#include <NXOpen/Routing_ComponentNamePluginData.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Routing_Electrical_WireDevice.hxx>
#include <NXOpen/Routing_Port.hxx>
#include <NXOpen/Routing_PortConnection.hxx>
#include <NXOpen/Routing_Stock.hxx>
#include <NXOpen/Routing_Wire.hxx>
#include <NXOpen/Session.hxx>

using namespace NXOpen;
using namespace NXOpen::Routing;

Plugins* NXOpen::Routing::thePlugins;

// Prototype for ufsta
extern "C" DllExport void ufsta( char* param , int* returncode, int param_len );

//--------------------------------------------------------------------------------------------------
// Writes the given string to the Listing Window and the syslog.
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

    LogFile* syslog = session->LogFile();
    syslog->WriteLine( stringToWrite.c_str() );
}

//--------------------------------------------------------------------------------------------------
Plugins::Plugins()
{
    Session*       session       = Session::GetSession();
    CustomManager* customManager = session->RouteCustomManager();

    customManager->SetHrnPreImportPlugin(                      make_callback( this, &Plugins::ImportExportPlugin                      ) );
    customManager->SetHrnPostExportPlugin(                     make_callback( this, &Plugins::ImportExportPlugin                      ) );
    customManager->SetCmpPreImportPlugin(                      make_callback( this, &Plugins::ImportExportPlugin                      ) );
    customManager->SetCmpPostExportPlugin(                     make_callback( this, &Plugins::ImportExportPlugin                      ) );
    customManager->SetPlmXmlPreImportPlugin(                   make_callback( this, &Plugins::ImportExportPlugin                      ) );
    customManager->SetPlmXmlPostExportPlugin(                  make_callback( this, &Plugins::ImportExportPlugin                      ) );
    customManager->SetPlmXmlRouteNodeNamePlugin(               make_callback( this, &Plugins::RouteNodeNamePlugin                     ) );
    customManager->SetPlmXmlRouteSectionNamePlugin(            make_callback( this, &Plugins::RouteSectionNamePlugin                  ) );
    customManager->SetWrappedOverstockLengthCalculationPlugin( make_callback( this, &Plugins::WrappedOverstockLengthCalculationPlugin ) );
    customManager->SetFilterBlankingPlugin(                    make_callback( this, &Plugins::FilterBlankingPlugin                    ) );
    customManager->SetBomPlugin(                               make_callback( this, &Plugins::BomPlugin                               ) );
    customManager->SetAutoRoutePlugin(                         make_callback( this, &Plugins::AutoRoutePlugin                         ) );
    customManager->SetManualRoutePlugin(                       make_callback( this, &Plugins::ManualRoutePlugin                       ) );
    customManager->SetUnroutePlugin(                           make_callback( this, &Plugins::UnroutePlugin                           ) );
    customManager->SetNavigatorObjectSelectedPlugin(           make_callback( this, &Plugins::NavigatorObjectSelectedPlugin           ) );
    customManager->SetValidateFormboardPlugin(                 make_callback( this, &Plugins::ValidateFormboardPlugin                 ) );
    customManager->SetDisciplineChangedPlugin(                 make_callback( this, &Plugins::DisciplineChangedPlugin                 ) );
    customManager->SetSpecificationChangedPlugin(              make_callback( this, &Plugins::SpecificationChangedPlugin              ) );
    customManager->SetSortConnectionsPlugin(                   make_callback( this, &Plugins::SortConnectionsPlugin                   ) );
    customManager->SetChoosePartPlugin(                        make_callback( this, &Plugins::ChoosePartPlugin                        ) );
    customManager->SetPipingComponentFilePlugin(               make_callback( this, &Plugins::PipingComponentFilePlugin               ) );

    // Routing calls the stock component name plugin when creating permanent stock using the
    // Convert to Stock as Components command.
    customManager->SetStockComponentNamePlugin( make_callback( this, &Plugins::StockComponentNamePlugin ) );

    // Routing calls the temporary stock component name plugin when you are creating stocks
    // on the fly in Stock as Components mode.
    customManager->SetTemporaryStockComponentNamePlugin( make_callback( this, &Plugins::StockComponentNamePlugin ) );
};

//--------------------------------------------------------------------------------------------------
void Plugins::ImportExportPlugin
(
    NXString fileName
)
{
    std::stringstream message;
    message << "\n*** C++ ImportExportPlugin called with " << fileName.GetLocaleText() << ".\n";
    echo( message.str() );
};

//--------------------------------------------------------------------------------------------------
NXString Plugins::RouteNodeNamePlugin()
{
    std::stringstream message;
    message << "\n*** C++ RouteNodeNamePlugin called";
    echo( message.str() );

    return NXString();
};

//--------------------------------------------------------------------------------------------------
NXString Plugins::RouteSectionNamePlugin()
{
    std::stringstream message;
    message << "\n*** C++ RouteSectionNamePlugin called";
    echo( message.str() );

    return NXString();
};

//--------------------------------------------------------------------------------------------------
double Plugins::WrappedOverstockLengthCalculationPlugin( Overstock* overstock )
{
    std::stringstream message;
    message << "\n*** C++ Wrapped Overstock Length Calculation plugin called with overstock tag ";
    message << overstock->Tag();
    echo( message.str() );

    return 10.0;
};

//--------------------------------------------------------------------------------------------------
// Converts the original string to an all upper case string.
// Useful for string insensitive comparisons.
static std::string convertStringToUpperCase
(
    const std::string& originalString
)
{
    std::string upperCaseString;

    std::transform( originalString.begin(), originalString.end(), std::back_inserter( upperCaseString ), ::toupper );

    return upperCaseString;
}

//--------------------------------------------------------------------------------------------------
bool Plugins::FilterBlankingPlugin
(
    NXObject* segmentOrComponent,
    NXString  logicalAttributeTitleNXString,
    NXString  logicalAttributeValueNXString,
    NXString  variableBuildStringNXString
)
{
    std::stringstream message;
    message << "\n*** C++ Filter Blanking plugin called with object tag ";
    message << segmentOrComponent->Tag() << std::endl;
    echo( message.str() );

    Session* session = Session::GetSession();
    Preferences::RoutingElectrical* electricalPreferences = session->Preferences()->RoutingApplicationView()->RoutingElectrical();

    std::string apvAttributeTitle( electricalPreferences->GetFilterBlankingAttribute().GetLocaleText() );
    std::string logicalAttributeTitle( logicalAttributeTitleNXString.GetLocaleText() );

    message.str( "" );
    message << "    APV Attribute Title    : " << apvAttributeTitle     << std::endl;
    message << "    Logical Attribute Title: " << logicalAttributeTitle << std::endl;
    echo( message.str() );

    if ( logicalAttributeTitle != apvAttributeTitle )
    {
        echo( "    (Not the same attribute titles. Ignoring this object.)" );
        return false;
    }

    std::string logicalAttributeValue( logicalAttributeValueNXString.GetLocaleText() );
    logicalAttributeValue = convertStringToUpperCase( logicalAttributeValue );

    bool blankTheObject = logicalAttributeValue == "YES"  ||
                          logicalAttributeValue == "TRUE" ||
                          logicalAttributeValue == "1";

    message.str( "" );
    message << "    Logical Attribute Value: " << logicalAttributeValue << std::endl;
    message << "    Variable Build String  : " << variableBuildStringNXString.GetLocaleText()   << std::endl;

    if ( blankTheObject )
        message << "    Blank the object!" << std::endl;

    echo( message.str() );

    return blankTheObject;
};

//--------------------------------------------------------------------------------------------------
void Plugins::BomPlugin()
{
    echo( "\n*** C++ Bill of Materials plugin called.\n" );
};

//--------------------------------------------------------------------------------------------------
int Plugins::AutoRoutePlugin
(
    StlConnectionVector connections
)
{
    std::stringstream message;
    message << "\n*** C++ AutoRoutePlugin called with " << connections.size() << " connections.\n";
    echo( message.str() );

    for ( auto connection : connections )
    {
        message.str( "" );
        message << "    Connection tag " << connection->Tag();
        echo( message.str() );
    }

    return 0;
}

//--------------------------------------------------------------------------------------------------
int Plugins::ManualRoutePlugin
(
    StlConnectionVector connections
)
{
    std::stringstream message;
    message << "\n*** C++ ManualRoutePlugin called with " << connections.size() << " connections.\n";
    echo( message.str() );

    for ( auto connection : connections )
    {
        message.str( "" );
        message << "    Connection tag " << connection->Tag();
        echo( message.str() );
    }

    return 0;
}

//--------------------------------------------------------------------------------------------------
int Plugins::UnroutePlugin
(
    StlConnectionVector connections
)
{
    std::stringstream message;
    message << "\n*** C++ UnroutePlugin called with " << connections.size() << " connections.\n";
    echo( message.str() );

    for ( auto connection : connections )
    {
        message.str( "" );
        message << "    Connection tag " << connection->Tag();
        echo( message.str() );
    }

    return 0;
}

//--------------------------------------------------------------------------------------------------
void Plugins::NavigatorObjectSelectedPlugin
(
    CustomManager::NavigatorType navigatorType,
    CustomManager::SelectionType selectionType,
    StlNXObjectVector            selectedObjects
)
{
    std::stringstream message;
    message << "\n*** C++ NavigatorObjectSelectedPlugin called with " << selectedObjects.size();

    if ( selectionType == CustomManager::SelectionTypeSelected )
    {
        message << " selected";
    }
    else
    {
        message << " deselected";
    }

    if ( navigatorType == CustomManager::NavigatorTypeConnection )
    {
        message << " in the Connection Navigator.";
    }
    else
    {
        message << " in the Component Navigator.";
    }

    echo( message.str() );

    for ( auto selectedObject : selectedObjects )
    {
        message.str( "" );
        message << "    Object tag " << selectedObject->Tag();
        echo( message.str() );
    }
}

//--------------------------------------------------------------------------------------------------
bool Plugins::ValidateFormboardPlugin
(
    StlHarnessDeviceVector harnessDevices
)
{
    std::stringstream message;
    message << "\n*** C++ Validate formboard plugin called with " << harnessDevices.size() << " harness devices.\n";
    echo( message.str() );

    for ( auto harnessDevice : harnessDevices )
    {
        message.str( "" );
        message << "  Harness Tag " << harnessDevice->Tag() << ".";
        echo( message.str() );
    }

    return true;
};

//--------------------------------------------------------------------------------------------------
void Plugins::DisciplineChangedPlugin
(
    NXString previousDisciplineName,
    NXString newDisciplineName
)
{
    std::stringstream message;

    echo("\n*** C++ Discipline Changed plugin called.");

    message << "    Previous discipline name '" << previousDisciplineName.GetLocaleText() << "'";
    echo( message.str() );

    message.str( "" );
    message << "    New discipline name      '" << newDisciplineName.GetLocaleText() << "'";
    echo( message.str() );
}

//--------------------------------------------------------------------------------------------------
void Plugins::SpecificationChangedPlugin
(
    NXString previousSpecificationName,
    NXString newSpecificationName
)
{
    std::stringstream message;

    echo("\n*** C++ Specification Changed plugin called.");

    message << "    Previous specification name '" << previousSpecificationName.GetLocaleText() << "'";
    echo( message.str() );

    message.str( "" );
    message << "    New specification name      '" << newSpecificationName.GetLocaleText() << "'";
    echo( message.str() );
}

//--------------------------------------------------------------------------------------------------
void Plugins::SortConnectionsPlugin
(
    Electrical::SortConnectionsPluginData* dataObject
)
{
    StlStockDeviceVector stockDevices;
    dataObject->GetStockDevicesToSort( stockDevices );

    std::stringstream message;
    message << "\n*** C++ Sort Connections plugin called with " << stockDevices.size() << " stock devices.\n";
    echo( message.str() );

    StlTagVector stockDeviceTags;
    for ( auto stockDevice : stockDevices )
    {
        message.str( "" );
        message << "  Stock Device Tag " << stockDevice->Tag() << ".";
        echo( message.str() );

        stockDeviceTags.push_back( stockDevice->Tag() );
    }

    // Implement your sorting method here.
    std::sort( stockDeviceTags.begin(), stockDeviceTags.end() );

    echo("");
    StlStockDeviceVector sortedStockDevices;
    for ( tag_t stockDeviceTag : stockDeviceTags )
    {
        message.str( "" );
        message << "  Sorted Stock Device Tag " << stockDeviceTag << ".";
        echo( message.str() );

        sortedStockDevices.push_back( dynamic_cast<Electrical::ElectricalStockDevice*>( NXObjectManager::Get( stockDeviceTag ) ) );
    }

    dataObject->SetSortedStockDevices( sortedStockDevices );
}

//--------------------------------------------------------------------------------------------------
// Implements an example Choose Part plugin that is used by the Place Part command.
int Plugins::ChoosePartPlugin
(
    ChoosePartPluginData* dataObject
)
{
    UF_initialize();

    char fileName[UF_ATTR_MAX_STRING_BUFSIZE] = "";
    bool unused = true;

    int response = UF_UI_OK;
    int error = UF_UI_ask_open_part_filename( fileName, &unused, &response );

    if ( error != ERROR_OK || response == UF_UI_CANCEL )
       return -1;

    dataObject->SetPartName( fileName );
    dataObject->SetPartNumber("ExamplePartNumber001");
    dataObject->SetMemberName(""); // No member name since this is not a member of a part family.

    // Some example attributes.
    CharacteristicList* exampleCharacteristics = Session::GetSession()->Preferences()->RoutingApplicationView()->PartPreferences()->PartLibrary()->CreateCriteria();
    exampleCharacteristics->SetCharacteristic("USER_CHARX_TITLE1", "User_charx_value1");
    exampleCharacteristics->SetCharacteristic("USER_CHARX_TITLE2", "User_charx_value2");

    dataObject->SetCharacteristics( exampleCharacteristics );

    return 0;
}

//--------------------------------------------------------------------------------------------------
void Plugins::PipingComponentFilePlugin
(
    NXString                                  fileName,
    StlComponentVector                        components,
    CustomManager::PipingComponentFileOptions options
)
{
    UF_ROUTE_pcf_gen_data_t pcfGenData = { 0 };
    pcfGenData.filename = fileName.GetLocaleText();
    pcfGenData.options  = options;

    pcfGenData.nComponents = components.size();
    pcfGenData.components  = new tag_t( components.size() );

    for ( int iComponents = 0; iComponents < components.size(); ++iComponents )
        pcfGenData.components[iComponents] = components[iComponents]->Tag();

    // TODO: Call this to create the actual PCF file.
    //UFD_Routing_CreatePipingComponentFile( &pcfGenData );

    delete pcfGenData.components;
}

//--------------------------------------------------------------------------------------------------
void Plugins::StockComponentNamePlugin
(
    ComponentNamePluginData* dataObject
)
{
    echo( "StockComponentNamePlugin" );

    static int stockNumberCounter = 0;
    ++stockNumberCounter;

    std::stringstream stockName;
    stockName << "StockComponent_" << std::setw( 4 ) << std::setfill( '0' ) << stockNumberCounter;


    char homeFolder[UF_UGMGR_NAME_BUFSIZE] = "";

    UF_initialize();
    bool isManagedMode = false;
    UF_is_ugmanager_active( &isManagedMode );
    if ( isManagedMode )
    {
        tag_t rootFolderTag;
        UF_UGMGR_ask_root_folder( &rootFolderTag );
        UF_UGMGR_ask_folder_name( rootFolderTag, homeFolder );
    }

    std::stringstream managedModeFolderName;
    managedModeFolderName << homeFolder << ":StockComponents";

    dataObject->SetComponentName( stockName.str().c_str() );
    dataObject->SetRenameComponentPartFlag( true );

    dataObject->SetNativeFileName( stockName.str().c_str() );
    dataObject->SetNativePath( "" ); // An empty path means the current directory.
    dataObject->SetManagedModeFolderName( managedModeFolderName.str().c_str() );
    dataObject->SetManagedModeItemName( stockName.str().c_str() );
    dataObject->SetManagedModeItemRevision( "A" );
    dataObject->SetManagedModeItemType( "Item" );

    UF_terminate();
}

//--------------------------------------------------------------------------------------------------
// Called when NX starts up to register the plugins using the Plugins class constructor.
extern "C" DllExport void ufsta
(
    char* /*param*/,
    int*  retcod,
    int   /*param_len*/
)
{
    *retcod = 0;

    thePlugins = new Plugins();
}

//--------------------------------------------------------------------------------------------------
// Tells NX when to unload your application.
// For Routing callbacks, plugins, and Design Rules, this MUST return UF_UNLOAD_UG_TERMINATE.
extern int ufusr_ask_unload()
{
    return( UF_UNLOAD_UG_TERMINATE );
}
