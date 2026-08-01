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

    An example program that gets and sets Globally Unique Identifiers (GUID) on control points
    and cableway network point occurrences.

    See Routing_Example_Cableway_GetSetGUIDs.hpp for the interface.


==================================================================================================*/
#include "Routing_Example_Cableway_GetSetGUIDs.hpp"

#include <algorithm>
#include <chrono>
#include <ctime>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <time.h>
#include <uf_object_types.h>
#include <uf_ugopenint.h>
#include <vector>

#include <NXOpen/Curve.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/MechanicalRouting_RoutingManager.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/Point.hxx>
#include <NXOpen/Routing_ArcSegment.hxx>
#include <NXOpen/Routing_ControlPoint.hxx>
#include <NXOpen/Routing_ISegment.hxx>
#include <NXOpen/Routing_LineSegment.hxx>
#include <NXOpen/Routing_Port.hxx>
#include <NXOpen/Routing_SplineSegment.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>

using namespace NXOpen;
using namespace NXOpen::Routing;
 
using StlAttributeInformationVector = std::vector < NXObject::AttributeInformation >;
using StlMaskTripleVector           = std::vector<Selection::MaskTriple>;

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
 
    for ( auto attribute : attributes )
    {
        NXString titleString = attribute.Title;
 
        // Watch out for attributes with no title.
        if ( titleString.GetLocaleText() == nullptr )
            continue;
 
        std::string title = convertStringToUpperCase( std::string( titleString.GetLocaleText() ) );
 
        std::string titleAlias;
        if ( attribute.TitleAlias.GetLocaleText() != nullptr )
            titleAlias = convertStringToUpperCase( std::string( attribute.TitleAlias.GetLocaleText() ) );
 
        if ( (title == ucAttributeName || titleAlias == ucAttributeName ) )
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
    const NXObject*                 object,
    const std::string&              attributeName,
    NXObject::AttributeInformation& attributeInformation
)
{
    return getAttributeFromList( const_cast<NXObject*>(object)->GetUserAttributes(), attributeName, attributeInformation );
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

    if ( getAttributeFromObject( object, attributeName, attributeInformation ) )
        return std::string( attributeInformation.StringValue.GetUTF8Text() );

    return std::string();
}

//--------------------------------------------------------------------------------------------------
static void addGuidToControlPoint( ControlPoint* controlPoint )
{
    if ( controlPoint->IsOccurrence() )
        controlPoint = dynamic_cast<ControlPoint*>( controlPoint->Prototype() );

    std::string originalGuid = controlPoint->Guid().GetUTF8Text();

    controlPoint->GenerateNewGuid();

    std::string newGuid = controlPoint->Guid().GetUTF8Text();

    UI::GetUI()->NXMessageBox()->Show( "Control Point", NXMessageBox::DialogTypeInformation, 
                                       "Control Point's original GUID was '" + originalGuid + "'\n" +
                                       "Changed it to '" + newGuid + "'" );
}

//--------------------------------------------------------------------------------------------------
static void addGuidToSegment( ISegment* segment )
{
    if ( segment->IsOccurrence() )
        segment = dynamic_cast<ISegment*>( segment->Prototype() );

    std::string originalGuid = segment->Guid().GetUTF8Text();

    segment->GenerateNewGuid();

    std::string newGuid = segment->Guid().GetUTF8Text();

    UI::GetUI()->NXMessageBox()->Show( "Segment", NXMessageBox::DialogTypeInformation, 
                                       "Segment's original GUID was '" + originalGuid + "'\n" +
                                       "Changed it to '" + newGuid + "'" );
}

//--------------------------------------------------------------------------------------------------
static void addGuidToObjectAttribute( NXObject* object, const char* attributeName )
{
    Session* session = Session::GetSession();
    MechanicalRouting::RoutingManager* routingMgr = MechanicalRouting::RoutingManager::GetRoutingManager( session );

    std::string originalGuid = getStringAttributeValueFromObject( object, attributeName );

    routingMgr->AddGuidToObjectAttribute( object, attributeName );
        
    std::string newGuid = getStringAttributeValueFromObject( object, attributeName );;
 
    UI::GetUI()->NXMessageBox()->Show( "Object Occurrence", NXMessageBox::DialogTypeInformation,
                                       "Object's original GUID was '" + originalGuid + "'\n" +
                                       "Changed it to '" + newGuid + "'" );
}

//--------------------------------------------------------------------------------------------------
static void processSelection( TaggedObject* selectedTaggedObject )
{
    // Depending on the object selected, there are various means of changing the GUID.
    //
    //  Cableways:
    //      Control Point     - Call GenerateNewGuid.
    //      Segment           - Call GenerateNewGuid.
    //
    //  Equipment (e.g. tee or elbow):
    //      Point occurrence  - Call AddGuidToObjectAttribute with CABLEWAY_EQUIPMENT_POINT_GUID.
    //      Curve occurrence  - Call AddGuidToObjectAttribute with CABLEWAY_EQUIPMENT_SEGMENT_GUID.
    //
    //  Hanger:
    //      Port occurrence   - Call AddGuidToObjectAttribute with CABLEWAY_HANGER_SEGMENT_GUID.

    auto* selectedObject = dynamic_cast<NXObject*>( selectedTaggedObject );

    if ( selectedObject == nullptr )
    {
        UI::GetUI()->NXMessageBox()->Show( "Wrong Object Type", NXMessageBox::DialogTypeInformation, 
                                           "This program does not handle objects of that type." );
    }

    auto* controlPoint = dynamic_cast<ControlPoint*>( selectedObject );
    auto* segment      = dynamic_cast<ISegment*>( selectedObject );
    auto* port         = dynamic_cast<Port*>( selectedObject );
    auto* point        = dynamic_cast<Point*>( selectedObject );
    auto* curve        = dynamic_cast<Curve*>( selectedObject );

    if ( controlPoint != nullptr )
    {
        // The GUID for a control point can be accessed directly through the GUID property.
        addGuidToControlPoint( controlPoint );
    }
    else if ( segment != nullptr )
    {
        // The GUID for a segment can be accessed directly through the GUID property.
        addGuidToSegment( segment );
    }
    else if ( point != nullptr )
    {
        // The GUID for a point from a component with qualified cableway network curves
        // (e.g. a tee or elbow) is stored as an attribute on the point occurrence
        // named CABLEWAY_EQUIPMENT_POINT_GUID.
        addGuidToObjectAttribute( point, "CABLEWAY_EQUIPMENT_POINT_GUID" );
    }
    else if ( curve != nullptr )
    {
        // The GUID for a curve from a component with qualified cableway network curves
        // (e.g. a tee or elbow) is stored as an attribute on the curve occurrence
        // named CABLEWAY_EQUIPMENT_SEGMENT_GUID.
        addGuidToObjectAttribute( curve, "CABLEWAY_EQUIPMENT_SEGMENT_GUID" );
    }
    else if ( port != nullptr )
    {
        // The GUID for a port of a hanger is stored as an attribute on the port occurrence
        // named CABLEWAY_HANGER_SEGMENT_GUID since a hanger is represented as a
        // zero length segment in Capital Router.
        addGuidToObjectAttribute( port, "CABLEWAY_HANGER_SEGMENT_GUID" );
    }
    else
    {
        UI::GetUI()->NXMessageBox()->Show( "Wrong Object Type", NXMessageBox::DialogTypeInformation, 
                                           "This program does not handle objects of this type." );
    }
}

//--------------------------------------------------------------------------------------------------
// Sets up the selection entity masks to allow:
//
//  - Control Points
//  - Segments
//  - Points
//  - Curves
//  - Ports
static StlMaskTripleVector setupEntityMasks()
{
    StlMaskTripleVector entityMasks;

    Selection::MaskTriple entityMask;
    entityMask.Type             = UF_route_control_point_type;
    entityMask.Subtype          = 0;
    entityMask.SolidBodySubtype = 0;
    entityMasks.emplace_back( entityMask );

    entityMask.Type             = UF_point_type;
    entityMask.Subtype          = UF_point_subtype;
    entityMask.SolidBodySubtype = 0;
    entityMasks.emplace_back( entityMask );

    entityMask.Type             = UF_line_type;
    entityMask.Subtype          = UF_line_normal_subtype;
    entityMask.SolidBodySubtype = 0;
    entityMasks.emplace_back( entityMask );

    entityMask.Type             = UF_circle_type;
    entityMask.Subtype          = 0;
    entityMask.SolidBodySubtype = 0;
    entityMasks.emplace_back( entityMask );

    entityMask.Type             = UF_route_port_type;
    entityMask.Subtype          = 0;
    entityMask.SolidBodySubtype = 0;
    entityMasks.emplace_back( entityMask );

    return entityMasks;
}

//--------------------------------------------------------------------------------------------------
// Called from File->Execute->NX Open.
extern "C" DllExport void ufusr
(
    char* /*param*/,
    int*  retcod,
    int   /*param_len*/
)
{
    *retcod = 0;

    UI* ui = UI::GetUI();

    try
    {
        StlMaskTripleVector entityMasks = setupEntityMasks();

        TaggedObject* selectedObject = nullptr;
        Point3d       position;
        Selection::Response response = ui->SelectionManager()->SelectTaggedObject( "Select a control point, segment, point, curve, or port", "Selection",
                                                                                   Selection::SelectionScope::SelectionScopeAnyInAssembly,
                                                                                   Selection::SelectionAction::SelectionActionClearAndEnableSpecific,
                                                                                   false, false, entityMasks,
                                                                                   &selectedObject, &position );
        if ( response == Selection::Response::ResponseOk ||
             response == Selection::Response::ResponseObjectSelected ||
             response == Selection::Response::ResponseObjectSelectedByName )
        {
            processSelection( selectedObject );
        }
    }
    catch ( const NXException& ex )
    {
        UI::GetUI()->NXMessageBox()->Show( "NXException", NXMessageBox::DialogTypeError, ex.Message() );
    }
    catch ( const std::exception& ex )
    {
        UI::GetUI()->NXMessageBox()->Show( "Exception", NXMessageBox::DialogTypeError, ex.what() );
    }
    catch ( ... )
    {
        UI::GetUI()->NXMessageBox()->Show( "Exception", NXMessageBox::DialogTypeError, "Unknown Exception." );
    }
}

//--------------------------------------------------------------------------------------------------
extern int ufusr_ask_unload()
{
    // Unloads the image immediately after execution within NX
    return UF_UNLOAD_IMMEDIATELY;
}
