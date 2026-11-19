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

    A C# class that implements example Routing Cableway Design Rules.


==================================================================================================*/
using NXOpen;
using NXOpen.Assemblies;
using NXOpen.Routing;
using NXOpen.RoutingCommon;
using System;

namespace Routing
{
    public class DesignRules
    {
        // Static class members
        static Session theSession = null;
        static NXOpen.RoutingCommon.CustomManager customManager = null;
        static int segregationCodeRuleId = 0;
        static string tierCountAttributeName = "TierCount";
        static string hangerSegregationAttributeName = "Cableway Hanger Segregation Code";
        static string segmentSegregationAttributeName = "Cableway Segment Segregation";

        //------------------------------------------------------------------------------------------
        // Called when NX starts up to register the Design Rules.
        public static int Startup()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (customManager == null)
                customManager = theSession.RoutingCustomManager;

            RegisterDesignRules();

            return 0;
        }

        //------------------------------------------------------------------------------------------
        // Called from File->Execute->NX Open. Useful for testing.
        public static void Main()
        {
            if (theSession == null)
                theSession = Session.GetSession();

            if (customManager == null)
                customManager = theSession.RoutingCustomManager;

            RegisterDesignRules();
        }

        //------------------------------------------------------------------------------------------
        // Called by both Main and Startup to register the Design Rules.
        private static void RegisterDesignRules()
        {
            string name = "Segregation Code";
            string description = "The Segregation Code design rule ensures no multi-tier " +
                                 "component has more segregation codes than tiers.";

            segregationCodeRuleId = customManager.AddDesignRule( NXOpen.Routing.CustomManager.DesignRuleReason.CablewayValidation,
                                                                 name, description, SegregationCodeDesignRule );
        }

        //------------------------------------------------------------------------------------------
        // Returns true and the attribute information object of the attribute if the attribute is in the list.
        // Returns false if not.
        // NOTE: The attribute name comparison is case insensitive.
        private static bool getAttributeFromList
        (
            NXObject.AttributeInformation[] attributes,
            String attributeName,
            out NXObject.AttributeInformation attributeInformation
        )
        {
            attributeInformation = new NXObject.AttributeInformation();

            foreach (NXObject.AttributeInformation attribute in attributes)
            {
                String ucAttributeName = attributeName.ToUpper();
                String titleString = attribute.Title;

                // Watch out for attributes with no title.
                if (titleString.Length == 0)
                    continue;

                titleString = titleString.ToUpper();

                // NOTE: This does not look for aliases on the attribute titles.
                if (titleString == ucAttributeName)
                {
                    attributeInformation = attribute;
                    return true;
                }
            }

            return false;
        }

        //------------------------------------------------------------------------------------------
        // Returns true and the attribute information object of the attribute if the attribute exists.
        // Returns false if not.
        private static bool getAttributeFromObject
        (
            NXObject nxObject,
            String attributeName,
            out NXObject.AttributeInformation attributeInformation
        )
        {
            return getAttributeFromList( nxObject.GetUserAttributes(), attributeName, out attributeInformation );
        }

        //------------------------------------------------------------------------------------------
        // Returns the stock body (e.g. the cable tray body) if the given component is a stock component.
        // Returns the given component if the component is not a stock component.
        static NXObject getStockBodyInComponent
        (
            Component component
        )
        {
            Part componentPart = (Part)component.Prototype;
            if (componentPart == null || !componentPart.IsFullyLoaded)
                return component;

            StockCollection stockCollection = componentPart.RouteManager.Stocks;

            // Since all stock components have the same type of stock, we can return the first stock body.
            foreach (Stock stock in stockCollection)
            {
                Body[] stockBodies = stock.GetBodies();
                if (stockBodies.Length > 0)
                    return stockBodies[0];
            }

            // If there are no stock, return the given component.
            return component;
        }

        //------------------------------------------------------------------------------------------
        // Returns the value of the tier count attribute if there is one. Returns zero if not.
        static int getTierCount
        (
            Component component
        )
        {
            NXObject nxObject = getStockBodyInComponent( component );

            NXObject.AttributeInformation attributeInformation;
            if (!getAttributeFromObject( nxObject, tierCountAttributeName, out attributeInformation ))
                return 0;

            if (attributeInformation.Type == NXObject.AttributeType.Integer)
                return attributeInformation.IntegerValue;

            if (attributeInformation.Type == NXObject.AttributeType.Real)
                return (int)attributeInformation.RealValue;

            return 0;
        }

        //--------------------------------------------------------------------------------------------------
        // Returns the number of elements in the segregation attribute array if it exists. Returns zero if not.
        static int getSegregationCount
        (
            Component component
        )
        {
            NXObject nxObject = getStockBodyInComponent( component );

            if (nxObject.HasUserAttribute( hangerSegregationAttributeName, NXObject.AttributeType.Any, -1 ))
                return nxObject.GetUserAttributeSize( hangerSegregationAttributeName, NXObject.AttributeType.Any );

            return nxObject.GetUserAttributeSize( segmentSegregationAttributeName, NXObject.AttributeType.Any );
        }

        //------------------------------------------------------------------------------------------
        // Ensures the tier count is greater than or equal too the number of elements in the segregation
        // attribute array. 
        // 
        // In other words, ensures there are not more segregation codes than there are tiers.
        static void checkComponentTierCount
        (
            ListingWindow listingWindow,
            int indentation,
            Component component
        )
        {
            int tierCount = getTierCount( component );
            int nSegregationCodes = getSegregationCount( component );
            if (tierCount >= nSegregationCodes)
                return;

            indentation += 2;
            string debugMessage = "".PadLeft( indentation ) + "TierCount = " + tierCount + "\n";
            debugMessage += "".PadLeft( indentation ) + "Number of Segregation Codes = " + nSegregationCodes + "\n";
            listingWindow.WriteFullline( debugMessage );

            NXObject[] objects = { component };

            string message = "Component " + component.DisplayName;
            message += " has only " + tierCount + " tiers";
            message += " but has " + nSegregationCodes + " segregation codes.\n";
            message += "The number of segregation codes cannot exceed the number of tiers.";

            customManager.CreateViolationForReason( "Segregation Code", NXOpen.Routing.CustomManager.DesignRuleReason.CablewayValidation,
                                                    "Too many segregation codes.", message, objects );
        }

        //------------------------------------------------------------------------------------------
        // Recursively walks down the assembly tree under the given component.
        static void walkDownAssemblyTree
        (
            ListingWindow listingWindow,
            int indentation,
            Component component
        )
        {
            if (component == null)
                return;

            string message = "".PadLeft( indentation ) + component.DisplayName;
            listingWindow.WriteFullline( message );

            // Verify that the segregation attribute array does not have more values than there are tiers.
            // This also works for stock components.
            checkComponentTierCount( listingWindow, indentation, component );

            indentation += 2;
            Component[] children = component.GetChildren();
            foreach (Component child in children)
                walkDownAssemblyTree( listingWindow, indentation, child );
        }

        //------------------------------------------------------------------------------------------
        static void SegregationCodeDesignRule
        (
            NXOpen.Routing.CustomManager.DesignRuleReason reason,
            NXObject[] nxObjects
        )
        {
            if (reason != NXOpen.Routing.CustomManager.DesignRuleReason.CablewayValidation &&
                 reason != NXOpen.Routing.CustomManager.DesignRuleReason.Interactive)
            {
                return;
            }

            try
            {
                Session session = Session.GetSession();
                Component rootComponent = session.Parts.Work.ComponentAssembly.RootComponent;

                ListingWindow listingWindow = Session.GetSession().ListingWindow;
                listingWindow.Open();

                int indentation = 0;
                walkDownAssemblyTree( listingWindow, indentation, rootComponent );

            }
            catch (NXException ex)
            {
                UI.GetUI().NXMessageBox.Show( "Segregation Code Design Rule Error", NXMessageBox.DialogType.Error, ex.Message );
            }
            catch (Exception ex)
            {
                UI.GetUI().NXMessageBox.Show( "Segregation Code Design Rule Error", NXMessageBox.DialogType.Error, ex.Message );
            }
        }

        //------------------------------------------------------------------------------------------
        // Tells NX when to unload your application.
        // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
        public static int GetUnloadOption( string arg )
        {
            return System.Convert.ToInt32( Session.LibraryUnloadOption.AtTermination );
        }
    }
}
