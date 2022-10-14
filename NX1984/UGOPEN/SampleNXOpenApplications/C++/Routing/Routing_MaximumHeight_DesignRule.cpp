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

A C++ class that implements example Routing Design Rule.

See Routing_MaximumHeight_DesignRule.hpp for the interface.


==================================================================================================*/
#include "Routing_MaximumHeight_DesignRule.hpp"

#include <iomanip>
#include <math.h>
#include <sstream>
#include <string.h>
#include <string>

#include <uf.h>

#include <NXOpen/Curve.hxx>
#include <NXOpen/Scalar.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx> 
#include <NXOpen/Routing_CrossSection.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Routing_DesignRule.hxx>
#include <NXOpen/Routing_DesignRuleViolation.hxx>
#include <NXOpen/Routing_Electrical_CableDefinition.hxx>
#include <NXOpen/Routing_Electrical_CableDevice.hxx>
#include <NXOpen/Routing_Electrical_WireDevice.hxx>
#include <NXOpen/Routing_Electrical_ElectricalStockDeviceCollection.hxx>
#include <NXOpen/Routing_Electrical_ElectricalStockDefinition.hxx>
#include <NXOpen/Routing_Electrical_ConnectionCollection.hxx>
#include <NXOpen/Routing_Electrical_Connection.hxx>
#include <NXOpen/Routing_ISegment.hxx>
#include <NXOpen/Routing_ISegmentCollection.hxx>
#include <NXOpen/Routing_Overstock.hxx>
#include <NXOpen/Routing_OverstockApplication.hxx>
#include <NXOpen/Routing_OverstockApplicationCollection.hxx>
#include <NXOpen/Routing_RouteManager.hxx>
#include <NXOpen/Routing_SegmentManager.hxx>
#include <NXOpen/Routing_Stock.hxx>
#include <NXOpen/Routing_Wire.hxx>
#include <NXOpen/Routing_WireCollection.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/TaggedObject.hxx> 
#include <NXOpen/Preferences_RoutingApplicationView.hxx>
#include <NXOpen/Preferences_RoutingUserPreferences.hxx>
#include <NXOpen/Preferences_SessionPreferences.hxx>
#include <NXOpen/Routing_Port.hxx>
#include <NXOpen/Routing_PortConnection.hxx>

#include <vector>
#include <set>

using namespace std;
using namespace NXOpen;
using namespace NXOpen::Routing;

typedef vector<NXObject*>                                   ObjectVector;
typedef std::vector < NXObject::AttributeInformation>       StlAttributeInformationVector;
typedef std::set < Electrical::ElectricalStockDevice*>      StlElectricalStockDeviceSet;
typedef std::vector< Routing::ISegment*>                    StlSegmentVector;
typedef std::vector< Routing::Overstock*>                   StlOverstockVector;
typedef std::set< Routing::Overstock*>                      StlOverstockSet;
typedef std::set< Routing::ISegment*>                       StlSegmentSet;


// Macros for comparing doubles.
#define TOLERANCE 10e-5
#define IS_ZERO(s)        ( fabs( (s) )       <= (TOLERANCE) )
#define IS_GREATER(s, t)  ( (s)               > ( (t) + (TOLERANCE) ) )

MaxHeightDesignRules* maxHeightDesignRules;

//--------------------------------------------------------------------------------------------------
// Get the the double value from attribute
//
// \param[in]
//      attributeInfo
//         Attribute information from which double needs to be queried
//
// \return
//      Value of attribute as Double
static double convertToReal
(
    const NXObject::AttributeInformation& attribute
)
{
    switch (attribute.Type)
    {
    case NXObject::AttributeTypeReal:
        return attribute.RealValue;

    case NXObject::AttributeTypeInteger:
        return (double)attribute.IntegerValue;

    case NXObject::AttributeTypeString:
    {
        std::istringstream iss(attribute.StringValue.GetUTF8Text());
        double number = 0.0;
        iss >> number;
        return number;
    }

    case NXObject::AttributeTypeInvalid:
    case NXObject::AttributeTypeNull:
    case NXObject::AttributeTypeBoolean:
    case NXObject::AttributeTypeTime:
    case NXObject::AttributeTypeReference:
    case NXObject::AttributeTypeAny:
    default:
        throw NXException::Create("Unknown attribute type");
    }
}

//--------------------------------------------------------------------------------------------------
// Gets the real value of the attribute on the given object, if any.
//
// \param[in]
//      object
//          The object to check for the attribute.
//
// \param[in]
//      attributeName
//          The name (a.k.a. title) of the attribute for which to look.
//
// \return
//          The value of the attribute, if found.
//
static double getAttributeValue
(
    NXObject*                object,
    const std::string        attributeNameString
)
{
    double attributeValue = 0.0;

    StlAttributeInformationVector attrInfoVector = object->GetUserAttributes();

    for (int index = 0; index < attrInfoVector.size(); ++index)
    {
        std::string attributeTitle(attrInfoVector[index].Title.GetText());

        if (attributeTitle == attributeNameString)
        {
            return convertToReal(attrInfoVector[index]);
        }
    }

    return attributeValue;
}

//--------------------------------------------------------------------------------------------------
// Queries the list of stock devices routing through the segment
//
// \param[in]
//      segment
//          Segment through which stock devices are routed.
//
// \param[in]
//      routeManager
//          RouteManager from the current work part
//
// \param[out]
//      stockDevices
//          List of stock stock devices referencing the segment
//
static void getStockDevicesRoutedThroughSegment
(
    ISegment*                          segment,
    RouteManager*                      routeManager, 
    StlElectricalStockDeviceSet&       wiresOnSelectedSegment
)
{
    Routing::Electrical::ElectricalStockDeviceCollection*          stockDevices = routeManager->ElectricalStockDevice();

    for (auto stockDevice : *stockDevices)
    {
        Electrical::WireDevice* wireDevice = dynamic_cast<Electrical::WireDevice*>(stockDevice);
        if (wireDevice == NULL) continue;

        Wire* wire = dynamic_cast<Wire*>(wireDevice->NxEquivalent());
        if (wire == NULL) continue;

        StlSegmentVector segmentVector = wire->GetSegments();
        StlSegmentSet    segmentSet(segmentVector.begin(), segmentVector.end());

        if (segmentSet.find(segment) != segmentSet.end())
        {
            wiresOnSelectedSegment.insert(stockDevice);
        }
    }
}

//-----------------------------------------------------------------------------------------------
// This method gives diameter of maximum size connection amongst the stock devices routing through the segment
//
// \param[in]
//      segment
//          Segment through which connections are routed
// \param[in]
//      stockDevicesOnSegment
//          List of stock devices routed through the segment
// \return
//          Maximum size diameter 
static double getValueToCheckMaxHeightViolationForStockDevice
(
    const ISegment*                               segment,
    const StlElectricalStockDeviceSet&            stockDevicesOnSegment
)
{
    double valueToCompare = 0.0;

    for (auto stockDevice : stockDevicesOnSegment)
    {
        double maxValue = 0.0;
        StockDefinition* stockDef = nullptr;
        Electrical::CableDefinition* cableDefinition =  stockDevice->FindTopmostCableDefinition();
        if (cableDefinition != nullptr)
        {
            Electrical::CableDevice* cableDevice = dynamic_cast<Electrical::CableDevice*>(cableDefinition->GetReferencingDevice());
            if (cableDevice == nullptr)
            {
                continue;
            }
            stockDef = cableDevice->StockDefinition();
        }
        else
        {
            stockDef = stockDevice->StockDefinition();
        }

        maxValue = stockDef->OuterDiameter();

        if (IS_GREATER(maxValue, valueToCompare))
        {
            valueToCompare = maxValue;
        }
    }

    return valueToCompare;
}

//-----------------------------------------------------------------------------------------------
// Queries the overstock referencing the segment
//
// \param[in]
//      segment
//         Segment from which referencing overstock needs to be queried.
// \param[in]
//      routeManager
//          RouteManager from the current work part
// \param[out]
//      overstockSet
//          set of overstocks referencing the segment
static void getOverstocksPresentOnTheSegment
(
    const ISegment*                    segment,
    RouteManager*                      routeManager,
    StlOverstockSet&                   overstocksOnSelectedSegment
)
{
    Routing::OverstockApplicationCollection* overstockApplications = routeManager->OverstockApplications();
    for (auto overstockApplication : *overstockApplications)
    {
        StlSegmentVector segmentsOfOverStockVector = overstockApplication->GetSegments();
        for (auto segmentOfOverstock : segmentsOfOverStockVector)
        {
            if (segmentOfOverstock != segment)
            {
                continue;
            }
            StlOverstockVector overstocks = overstockApplication->GetOverstocks();
            overstocksOnSelectedSegment.insert(overstocks[0]);
        }
    }
}

//-----------------------------------------------------------------------------------------------
// Check the maximum diameter of connection routing through given segment against the maximum allowed height.
//
// Creates a violation for the given reason if connection diameter exceeds specified Maximum Height value.
//
// \param[in]
//      routeManager
//          RouteManager from current work part
//
// \param[in]
//      customManager
//          CustomManager to create design Rule violation.
//
// \param[in]
//      segment
//          Routing Segment to be check for Maximum Height violation
//
// \param[in]
//      reason
//          Design Rule reason for which Maximum Height Violation needs to be checked.
static void checkForMaximumHeightViolation
(
    RouteManager*                       routeManager,
    CustomManager*                      customManager,
    ISegment*                           segment,
    CustomManager::DesignRuleReason     reason
)
{
    std::string maxHeightAttributeName("CABLETRAY_MAXHEIGHT");

    // Get value of allowed Maximum Height or Specified Maximum Height
    NXObject* segmentObject = dynamic_cast<NXObject*>(segment);
    double specifiedMaxHeightValue = getAttributeValue(segmentObject, maxHeightAttributeName);

    if (IS_ZERO(specifiedMaxHeightValue))
    {
        return;
    }

    // Get list of Stock Devices routing through the segment
    StlElectricalStockDeviceSet stockDevices;
    getStockDevicesRoutedThroughSegment(segment, routeManager, stockDevices);
    if (stockDevices.empty())
    {
        return;
    }

    // Get max value diameter of connection routing through the segment
    double valueToCompare = getValueToCheckMaxHeightViolationForStockDevice(segment, stockDevices);

    // Get Overstocks referencing the segment
    StlOverstockSet overstockReferencingTheSegment;
    getOverstocksPresentOnTheSegment(segment, routeManager, overstockReferencingTheSegment);

    // If Overstocks are present on segment, get maximum value of diameter including overstock
    if (!overstockReferencingTheSegment.empty())
    {
        double totalOverstockThickness = 0.0;
        for (auto overstock : overstockReferencingTheSegment)
        {
            totalOverstockThickness += overstock->GetThickness()->Value();
        }
        valueToCompare += (2 * totalOverstockThickness);
    }

    // If current value of diameter is greater than specified maximum height value then raise violation.
    if (IS_GREATER(valueToCompare, specifiedMaxHeightValue))
    {
        tag_t newViolation = NULL_TAG;
        std::stringstream description;

        description << "The stock exceeds the maximum height allowed for this segment. The current height is " << valueToCompare << ".The allowed height is " << specifiedMaxHeightValue << ".";
        ObjectVector objects;
        objects.push_back(segmentObject);

        customManager->CreateViolationForReason("Maximum Height Violation", reason,
            "The segment violates Maximum Height Rule", description.str(), objects);
    }
}

// Prototype for ufsta
extern "C" DllExport void ufsta(char* param, int* returncode, int param_len);

//--------------------------------------------------------------------------------------------------
MaxHeightDesignRules::MaxHeightDesignRules()
{
    Session*       session = Session::GetSession();
    CustomManager* customManager = session->RouteCustomManager();
    NXString       maxHeightViolationTitle = "Maximum Height Violation";
    NXString       maxHeightViolationDescription = 
        "The Maximum Height design rule makes sure the diameter of each individual connection is within the permissible limit of value specified by attribute CABLETRAY_MAXHEIGHT.";


    m_maxHeightRuleForCreatePath = customManager->AddDesignRule(CustomManager::DesignRuleReasonCreatePath,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForHealPath   = customManager->AddDesignRule(CustomManager::DesignRuleReasonHealPath,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForAssignCorner = customManager->AddDesignRule(CustomManager::DesignRuleReasonAssignCorner,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForAssignStock = customManager->AddDesignRule(CustomManager::DesignRuleReasonAssignStock,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForRemovePart = customManager->AddDesignRule(CustomManager::DesignRuleReasonRemovePart,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForAutoRoutePinLevel = customManager->AddDesignRule(CustomManager::DesignRuleReasonAutoRoutePinLevel,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForManualRoutePinLevel = customManager->AddDesignRule(CustomManager::DesignRuleReasonManualRoutePinLevel,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForAutoRouteComponentLevel = customManager->AddDesignRule(CustomManager::DesignRuleReasonAutoRouteComponentLevel,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForManualRouteComponentLevel = customManager->AddDesignRule(CustomManager::DesignRuleReasonManualRouteComponentLevel,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForInteractive = customManager->AddDesignRule(CustomManager::DesignRuleReasonInteractive,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForTransformPath = customManager->AddDesignRule(CustomManager::DesignRuleReasonTransformPath,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));

    m_maxHeightRuleForEditCharacteristic = customManager->AddDesignRule(CustomManager::DesignRuleReasonEditCharacteristic,
                                                        maxHeightViolationTitle, maxHeightViolationDescription,
                                                        make_callback(this, &MaxHeightDesignRules::CreateMaximumHeightDesignRule));
};

void MaxHeightDesignRules::CreateMaximumHeightDesignRule
(
    CustomManager::DesignRuleReason     reason,
    StlNXObjectVector                   objects
)
{
    // Get the current NX session.
    Session*    theSession = Session::GetSession();
    Part*       workPart = theSession->Parts()->Work();
    CustomManager* customManager = theSession->RouteCustomManager();
    RouteManager* routeManager = theSession->Parts()->Work()->RouteManager();

    if (workPart == NULL)
        return;

    if (reason == CustomManager::DesignRuleReasonInteractive)
    {
        // For interactive checks, check all the segments in the work part.
        SegmentManager*     segmentManager = theSession->Parts()->Work()->SegmentManager();
        ISegmentCollection* segmentCollection = segmentManager->Segments();

        for (ISegment* segment : *segmentCollection)
        {
            checkForMaximumHeightViolation(routeManager, customManager, segment, reason);
        }
        return;
    }

    // Otherwise, check the segments in the given list of objects.
    for (NXObject* object : objects)
    {
        ISegment* segment = dynamic_cast<ISegment*>(object);
        if (segment != nullptr)
        {
            checkForMaximumHeightViolation(routeManager, customManager, segment, reason);
        }
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

    maxHeightDesignRules = new MaxHeightDesignRules();
}

//--------------------------------------------------------------------------------------------------
// Tells NX when to unload your application.
// For Routing callbacks, plugins, and Design Rules, this MUST return UF_UNLOAD_UG_TERMINATE.
extern int ufusr_ask_unload()
{
    return(UF_UNLOAD_UG_TERMINATE);
}
