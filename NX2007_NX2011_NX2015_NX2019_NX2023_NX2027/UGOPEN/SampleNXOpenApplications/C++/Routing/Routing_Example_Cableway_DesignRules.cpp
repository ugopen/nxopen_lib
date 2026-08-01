/*==================================================================================================
                                       Copyright 2021 Siemens
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A C++ class that implements example Routing Cableway Design Rules.

    See Routing_Example_Cableway_DesignRules.hpp for the interface.


==================================================================================================*/
#include "Routing_Example_Cableway_DesignRules.hpp"

#include <algorithm>
#include <sstream>
#include <uf_defs.h>
#include <uf_ugopenint.h>

#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Routing_RouteManager.hxx>
#include <NXOpen/Routing_Stock.hxx>
#include <NXOpen/Routing_StockCollection.hxx>
#include <NXOpen/RoutingCommon_CustomManager.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>

using namespace NXOpen;
using namespace NXOpen::Routing;

constexpr char* tierCountAttributeName          = "TierCount";
constexpr char* hangerSegregationAttributeName  = "Cableway Hanger Segregation Code";
constexpr char* segmentSegregationAttributeName = "Cableway Segment Segregation";

DesignRules* NXOpen::Routing::theDesignRules;

// Prototype for ufsta
extern "C" DllExport void ufsta( char* param , int* returncode, int param_len );

using StlAttributeInformationVector = std::vector< NXObject::AttributeInformation >;
using StlBodyVector                 = std::vector< Body* >;
using StlCharxInfoVector            = std::vector< CharacteristicList::CharacteristicInformation >;
using StlComponentVector            = std::vector< Assemblies::Component* >;

//--------------------------------------------------------------------------------------------------
DesignRules::DesignRules()
{
    Session* session     = Session::GetSession();
    NXString name        = "Segregation Code";
    NXString description = "The Segregation Code design rule ensures no multi-tier "
                           "component has more segregation codes than tiers.";

    RoutingCommon::CustomManager* customManager = session->RoutingCustomManager();

    m_segregationCodeRuleId = customManager->AddDesignRule( CustomManager::DesignRuleReasonCablewayValidation,
                                                            name, description,
                                                            make_callback(this, &DesignRules::SegregationCodeDesignRule) );
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
    std::string ucAttributeName = convertStringToUpperCase( attributeName );

    for ( const auto& attribute : attributes )
    {
        NXString titleString = attribute.Title;

        // Watch out for attributes with no title.
        if ( titleString.GetLocaleText() == nullptr )
            continue;

        std::string title = convertStringToUpperCase( std::string( titleString.GetLocaleText() ) );

        std::string titleAlias;
        if ( attribute.TitleAlias.GetLocaleText() != nullptr )
            titleAlias = convertStringToUpperCase( std::string( attribute.TitleAlias.GetLocaleText() ) );

        if ( ( title == ucAttributeName || titleAlias == ucAttributeName ) )
        {
            attributeInformation = attribute;
            return true;
        }
    }

    return false;
}

//--------------------------------------------------------------------------------------------------
// Returns true and the attribute information object of the attribute if the attribute exists.
// Returns false if not.
static bool getAttributeFromObject
(
    const NXObject*                 nxObject,
    const std::string&              attributeName,
    NXObject::AttributeInformation& attributeInformation
)
{
    return getAttributeFromList( const_cast<NXObject*>( nxObject )->GetUserAttributes(), attributeName, attributeInformation );
}

//--------------------------------------------------------------------------------------------------
// Returns the stock body (e.g. the cable tray body) if the given component is a stock component.
// Returns the given component if the component is not a stock component.
static NXObject* getStockBodyInComponent
(
    Assemblies::Component* component
)
{
    auto* componentPart = dynamic_cast<Part*>( component->Prototype() );
    if ( componentPart == nullptr || !componentPart->IsFullyLoaded() )
        return component;

    StockCollection* stockCollection = componentPart->RouteManager()->Stocks();

    // Since all stock components have the same type of stock, we can return the first stock body.
    for ( auto* stock : *stockCollection )
    {
        StlBodyVector stockBodies = stock->GetBodies();
        if ( !stockBodies.empty() )
            return stockBodies[0];
    }

    // If there are no stock, return the given component.
    return component;
}

//--------------------------------------------------------------------------------------------------
// Returns the value of the tier count attribute if there is one. Returns zero if not.
static int getTierCount
(
    Assemblies::Component* component
)
{
    NXObject* nxObject = getStockBodyInComponent( component );

    NXObject::AttributeInformation attributeInformation;
    if ( !getAttributeFromObject( nxObject, tierCountAttributeName, attributeInformation ) )
        return 0;

    if ( attributeInformation.Type == NXObject::AttributeTypeInteger )
        return attributeInformation.IntegerValue;

    if ( attributeInformation.Type == NXObject::AttributeTypeReal )
        return (int)attributeInformation.RealValue;

    return 0;
}

//--------------------------------------------------------------------------------------------------
// Returns the number of elements in the segregation attribute array if it exists. Returns zero if not.
static int getSegregationCount
(
    Assemblies::Component* component
)
{
    NXObject* nxObject = getStockBodyInComponent( component );

    if ( nxObject->HasUserAttribute( hangerSegregationAttributeName, NXObject::AttributeTypeAny, -1 ) )
        return nxObject->GetUserAttributeSize( hangerSegregationAttributeName, NXObject::AttributeTypeAny );

    return nxObject->GetUserAttributeSize( segmentSegregationAttributeName, NXObject::AttributeTypeAny );
}

//--------------------------------------------------------------------------------------------------
// Ensures the tier count is greater than or equal too the number of elements in the segregation
// attribute array.
//
// In other words, ensures there are not more segregation codes than there are tiers.
static void checkComponentTierCount
(
    ListingWindow*         listingWindow,
    int                    indentation,
    Assemblies::Component* component
)
{
    int tierCount         = getTierCount( component );
    int nSegregationCodes = getSegregationCount( component );
    if ( tierCount >= nSegregationCodes )
        return;

    indentation += 2;
    std::stringstream debugMessage;
    debugMessage << std::string( indentation, ' ' ) << "TierCount = " << tierCount << std::endl;
    debugMessage << std::string( indentation, ' ' ) << "Number of Segregation Codes = " << nSegregationCodes << std::endl;
    listingWindow->WriteFullline( debugMessage.str().c_str() );

    StlNXObjectVector objects;
    objects.push_back( component );

    std::stringstream message;
    message << "Component " << component->DisplayName().GetText();
    message << " has only " << tierCount << " tiers";
    message << " but has " << nSegregationCodes << " segregation codes." << std::endl;
    message << "The number of segregation codes cannot exceed the number of tiers.";

    RoutingCommon::CustomManager* customManager = Session::GetSession()->RoutingCustomManager();
    customManager->CreateViolationForReason( "Segregation Code", CustomManager::DesignRuleReasonCablewayValidation,
                                             "Too many segregation codes.",
                                             message.str().c_str(), objects );
}

//--------------------------------------------------------------------------------------------------
// Recursively walks down the assembly tree under the given component.
static void walkDownAssemblyTree
(
    ListingWindow*         listingWindow,
    int                    indentation,
    Assemblies::Component* component
)
{
    if ( component == nullptr )
        return;

    std::stringstream message;
    message << std::string( indentation, ' ' ) << component->DisplayName().GetText() << std::endl;
    listingWindow->WriteFullline( message.str().c_str() );

    // Verify that the segregation attribute array does not have more values than there are tiers.
    // This also works for stock components.
    checkComponentTierCount( listingWindow, indentation, component );

    indentation += 2;
    StlComponentVector children = component->GetChildren();
    for ( auto* child : children )
        walkDownAssemblyTree( listingWindow, indentation, child );
}

//--------------------------------------------------------------------------------------------------
void DesignRules::SegregationCodeDesignRule
(
    CustomManager::DesignRuleReason reason,
    StlNXObjectVector               /*objects*/
)
{
    if ( reason != CustomManager::DesignRuleReasonCablewayValidation &&
         reason != CustomManager::DesignRuleReasonInteractive )
    {
        return;
    }

    try
    {
        Session*               session    = Session::GetSession();
        Session::UndoMarkId    undoMarkId = session->SetUndoMark( Session::MarkVisibilityInvisible, "SegregationCodeDesignRule" );
        Assemblies::Component* rootComponent = session->Parts()->Work()->ComponentAssembly()->RootComponent();

        ListingWindow* listingWindow = Session::GetSession()->ListingWindow();
        listingWindow->Open();

        int indentation = 0;
        walkDownAssemblyTree( listingWindow, indentation, rootComponent );

        session->UpdateManager()->DoUpdate( undoMarkId );
    }
    catch ( const NXException& ex )
    {
        UI::GetUI()->NXMessageBox()->Show( "Segregation Code Design Rule Error",
                                           NXOpen::NXMessageBox::DialogTypeError,
                                           ex.Message() );
    }
    catch ( ... )
    {
        UI::GetUI()->NXMessageBox()->Show( "Segregation Code Design Rule Error",
                                           NXOpen::NXMessageBox::DialogTypeError,
                                           "Unknown error while executing AutoRoute plugin." );
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
