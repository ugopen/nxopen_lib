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

    A C# class that implements Maximum Height Violation Routing Design Rule.


==================================================================================================*/
using System;
using NXOpen;
using NXOpen.Preferences;
using NXOpen.Routing;
using NXOpen.Routing.Electrical;
using System.Collections.Generic;

namespace Routing
{
    public class MaxHeightDesignRules
    {
        // Static class members
        static Session theSession = null;
        static ListingWindow listingWindow = null;
        static CustomManager customManager = null;

        static int m_maxHeightRuleForCreatePath;
        static int m_maxHeightRuleForHealPath;
        static int m_maxHeightRuleForAssignCorner;
        static int m_maxHeightRuleForAssignStock;
        static int m_maxHeightRuleForRemovePart;
        static int m_maxHeightRuleForAutoRoutePinLevel;
        static int m_maxHeightRuleForManualRoutePinLevel;
        static int m_maxHeightRuleForAutoRouteComponentLevel;
        static int m_maxHeightRuleForManualRouteComponentLevel;
        static int m_maxHeightRuleForInteractive;
        static int m_maxHeightRuleForTransformPath;
        static int m_maxHeightRuleForEditCharacteristic;

        //------------------------------------------------------------------------------------------
        // Called when NX starts up to register the Design Rules.
        public static int Startup()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (listingWindow == null)
                listingWindow = theSession.ListingWindow;

            if (customManager == null)
                customManager = theSession.RouteCustomManager;

            RegisterMaxHeightDesignRules();

            return 0;
        }

        //------------------------------------------------------------------------------------------
        // Called from File->Execute->NX Open. Useful for testing.
        public static void Main()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (listingWindow == null)
                listingWindow = theSession.ListingWindow;

            if (customManager == null)
                customManager = theSession.RouteCustomManager;

            RegisterMaxHeightDesignRules();
        }

        //--------------------------------------------------------------------------------------------------
        // Get the the double value from attribute
        //
        // \param[in]
        //      attributeInfo
        //         Attribute information from which double needs to be queried
        //
        // \return
        //      Value of attribute as Double
        //
        private static double convertToReal
        (
            ref NXObject.AttributeInformation attribute
        )
        {
            switch (attribute.Type)
            {
                case NXObject.AttributeType.Real:
                {
                    return attribute.RealValue;
                }
                case NXObject.AttributeType.Integer:
                {
                    return (double)attribute.IntegerValue;
                }
                case NXObject.AttributeType.String:
                {
                    return Convert.ToDouble(attribute.StringValue);
                }

                case NXObject.AttributeType.Invalid:
                case NXObject.AttributeType.Null:
                case NXObject.AttributeType.Boolean:
                case NXObject.AttributeType.Time:
                case NXObject.AttributeType.Reference:
                case NXObject.AttributeType.Any:
                default:
                    throw NXException.Create(1);
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
        private static double getAttributeValue
        (
            ref NXObject      nxObject,
            string            attributeNameString
        )
        {
            NXObject.AttributeInformation[] attrInfoVector;
            attrInfoVector = nxObject.GetUserAttributes();

            foreach (NXObject.AttributeInformation attribute in attrInfoVector)
            {
                NXObject.AttributeInformation attributeInfo = attribute;

                if (attributeInfo.Title == attributeNameString)
                {
                    return convertToReal(ref attributeInfo);
                }
            }

            return 0.0;
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
        // \return
        //          List of stock stock devices referencing the segment
        //
        private static List<StockDevice> getStockDevicesRoutedThroughSegment
        (
            ref ISegment              segment,
            ref RouteManager          routeManager
        )
        {
            List<StockDevice> stockDevicesOnSegment = new List<StockDevice>();

            ElectricalStockDeviceCollection stockDevices = routeManager.ElectricalStockDevice;

            foreach (StockDevice stockDevice in stockDevices)
            {
                Wire wire = (Wire)stockDevice.NxEquivalent;
                if (wire == null) continue;

                ISegment[] stockDeviceSegments = wire.GetSegments();

                foreach (ISegment singleSegment in stockDeviceSegments)
                {
                    if (singleSegment != segment)
                    {
                        continue;
                    }
                    if(!stockDevicesOnSegment.Contains(stockDevice))
                    {
                        stockDevicesOnSegment.Add(stockDevice);
                    }
                }
            }

            return stockDevicesOnSegment;
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
        // \return
        //          Set of overstocks referencing the segment
        static SortedSet<Overstock> getOverstocksPresentOnTheSegment
        (
            ref ISegment                     segment,
            ref RouteManager                 routeManager
        )
        {
            SortedSet<Overstock> overstockOnSegment = new SortedSet<Overstock>();

            OverstockApplicationCollection overstockApplications = routeManager.OverstockApplications;

            foreach(OverstockApplication overstockApplication in overstockApplications)
            {
                ISegment[] segmentsOfOverstockApplication = overstockApplication.GetSegments();

                foreach (ISegment currentSegment in segmentsOfOverstockApplication)
                {
                    if (currentSegment != segment)
                    {
                        continue;
                    }

                    Overstock[] overstocks = overstockApplication.GetOverstocks();
                    overstockOnSegment.Add(overstocks[0]);
                }
            }

            return overstockOnSegment;
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
            ref ISegment                      segment,
            ref List <StockDevice>            stockDevicesOnSegment
        )
        {
            double valueToCompare = 0.0;

            foreach (StockDevice stockDevice in stockDevicesOnSegment)
            {
                double maxValue = 0.0;
                StockDefinition stockDef = null;
                ElectricalStockDevice electricalStockDevice = stockDevice as ElectricalStockDevice;
                if(electricalStockDevice == null)
                {
                    continue;
                }

                CableDefinition cableDefinition = electricalStockDevice.FindTopmostCableDefinition();
                if (cableDefinition != null)
                {
                    CableDevice cableDevice = cableDefinition.GetReferencingDevice() as CableDevice;
                    if (cableDevice == null)
                    {
                        continue;
                    }
                    stockDef = cableDevice.StockDefinition;
                }
                else
                {
                    stockDef = stockDevice.StockDefinition;
                }

                maxValue = stockDef.OuterDiameter;

                if (maxValue > (valueToCompare + 1E-05))
                {
                    valueToCompare = maxValue;
                }
            }
            return valueToCompare;
        }

        //------------------------------------------------------------------------------------------
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
            ref RouteManager                        routeManager,
            ref CustomManager                       customManager,
            ref ISegment                            segment,
            CustomManager.DesignRuleReason          reason
        )
        {
            string maxHeightAttributeName = "CABLETRAY_MAXHEIGHT";

            // Get value of allowed Maximum Height or Specified Maximum Height
            NXObject segmentObject = (NXObject)segment;

            double specifiedMaxHeightValue = getAttributeValue(ref segmentObject, maxHeightAttributeName);
            if (Math.Abs(specifiedMaxHeightValue) < 1E-05)
            {
                return;
            }

            // Get list of Stock Devices routing through the segment
            List<StockDevice> stockDevices = getStockDevicesRoutedThroughSegment(ref segment, ref routeManager);
            if (stockDevices.Count == 0)
            {
                return;
            }

            // Get max value diameter of connection routing through the segment
            double valueToCompare = getValueToCheckMaxHeightViolationForStockDevice(ref segment, ref stockDevices);            

            // Get Overstocks referencing the segment
            SortedSet<Overstock> overstocksReferencingTheSegment = getOverstocksPresentOnTheSegment(ref segment, ref routeManager);

            // If Overstocks are present on segment, get maximum value of diameter including overstock
            if (overstocksReferencingTheSegment.Count > 0)
            {
                double totalOverstockThickness = 0.0;
                foreach(Overstock overstock in overstocksReferencingTheSegment)
                {
                    totalOverstockThickness += overstock.GetThickness().Value;
                }
                valueToCompare += (2 * totalOverstockThickness);
            }

            // If current value of diameter is greater than specified maximum height value then raise violation.
            if (valueToCompare > (specifiedMaxHeightValue + 1E-05))
            {
                string description = "The stock exceeds the maximum height allowed for this segment. The current height is " + valueToCompare + ".The allowed height is " + specifiedMaxHeightValue + ".";

                NXObject[] objects = {(NXObject)segment };
                customManager.CreateViolationForReason("Maximum Height Violation", reason,"The segment violates Maximum Height Rule", description, objects );
            }

            stockDevices.Clear();
            overstocksReferencingTheSegment.Clear();
        }

        //------------------------------------------------------------------------------------------
        // Called by both Main and Startup to register the Design Rules.
        private static void RegisterMaxHeightDesignRules()
        {
            string maxHeightViolationTitle = "Maximum Height Violation";
            string maxHeightViolationDescription = "The Maximum Height design rule makes sure the diameter of each individual connection is within the permissible limit of value specified by attribute CABLETRAY_MAXHEIGHT.";

            m_maxHeightRuleForCreatePath = customManager.AddDesignRule(CustomManager.DesignRuleReason.CreatePath, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForHealPath = customManager.AddDesignRule(CustomManager.DesignRuleReason.HealPath, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForAssignCorner = customManager.AddDesignRule(CustomManager.DesignRuleReason.AssignCorner, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForAssignStock = customManager.AddDesignRule(CustomManager.DesignRuleReason.AssignStock, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForRemovePart = customManager.AddDesignRule(CustomManager.DesignRuleReason.RemovePart, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForAutoRoutePinLevel = customManager.AddDesignRule(CustomManager.DesignRuleReason.AutoRoutePinLevel, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForManualRoutePinLevel = customManager.AddDesignRule(CustomManager.DesignRuleReason.ManualRoutePinLevel, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForAutoRouteComponentLevel = customManager.AddDesignRule(CustomManager.DesignRuleReason.AutoRouteComponentLevel, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForManualRouteComponentLevel = customManager.AddDesignRule(CustomManager.DesignRuleReason.ManualRouteComponentLevel, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForInteractive = customManager.AddDesignRule(CustomManager.DesignRuleReason.Interactive, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForTransformPath = customManager.AddDesignRule(CustomManager.DesignRuleReason.TransformPath, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
            m_maxHeightRuleForEditCharacteristic = customManager.AddDesignRule(CustomManager.DesignRuleReason.EditCharacteristic, maxHeightViolationTitle, maxHeightViolationDescription, CreateMaximumHeightDesignRule);
        }

        //------------------------------------------------------------------------------------------
        private static void CreateMaximumHeightDesignRule
        (
            CustomManager.DesignRuleReason reason,
            NXObject[] nxObjects
        )
        {
            // For interactive checks, check all the segments in the work part.
            SegmentManager segmentManager = theSession.Parts.Work.SegmentManager;
            ISegmentCollection segmentCollection = segmentManager.Segments;
            RouteManager routeManager = theSession.Parts.Work.RouteManager;

            if (reason == CustomManager.DesignRuleReason.Interactive)
            {
                foreach (ISegment segmentItr in segmentCollection)
                {
                    ISegment segment = segmentItr;
                    checkForMaximumHeightViolation(ref routeManager, ref customManager, ref segment, reason);
                }
                return;
            }

            // Otherwise, check the segments in the given list of objects.
            foreach (NXObject nxObject in nxObjects)
            {
                if(nxObject is ISegment)
                {
                    ISegment segment = (ISegment)nxObject;
                    checkForMaximumHeightViolation(ref routeManager, ref customManager, ref segment, reason);
                }
            }
        }

        //------------------------------------------------------------------------------------------
        // Tells NX when to unload your application.
        // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
        public static int GetUnloadOption(string arg)
        {
            return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
        }
    }
}

