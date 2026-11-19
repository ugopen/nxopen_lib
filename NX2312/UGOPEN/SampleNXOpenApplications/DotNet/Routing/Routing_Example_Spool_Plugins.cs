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

    A C# class that implements example Routing Spool plugins.


==================================================================================================*/
using System;
using System.IO;
using NXOpen;
using NXOpen.Assemblies;
using NXOpen.MechanicalRouting;
using NXOpen.RoutingCommon;
using NXOpen.Schematic.Mechanical;

namespace RoutingCommon
{
    public class SpoolPlugins
    {
        // Static class members
        static Session       session       = null;
        static ListingWindow listingWindow = null;
        static CustomManager customManager = null;

        //------------------------------------------------------------------------------------------
        // Called when NX starts up to register the plugins.
        public static int Startup()
        {
            if (session == null)
                session = Session.GetSession();

            if (listingWindow == null)
                listingWindow = session.ListingWindow;

            // Calling CreateRoutingSession is required before registering Routed System Designer (RSD)
            // plugins, callbacks, or design rules to ensure the Routing libraries are properly loaded.
            session.CreateRoutingSession();

            if (customManager == null)
                customManager = session.RoutingCustomManager;

            customManager.SetSpoolNamePlugin( GenerateSpoolName );

            session.LicenseManager.ReleaseAll( null );

            return 0;
        }

        //------------------------------------------------------------------------------------------
        // Called by the Spool dialog to create a name for the new spool.
        // 
        // The name this plugin generates is a combination of:
        // 
        //   - Prefix:        The spool Name Prefix defined in the Routed System Designer->Mechanical->Spools customer defaults.
        //   - Block:         The Block identifier is simply the name of the work part.
        //   - Specification: The specification assigned to the components.
        //   - Run ID:        The identifier of the run to which the components belong.
        //   - Index:         An index one greater than the number of existing spools in the part.
        //
        // \param[in]
        //      spoolPart
        //          The part in which the new spool is created.
        //
        // \param[in]
        //      spoolComponents
        //          The connected components that will make up the new spool.
        //
        // \return
        //      The name the Routing application will use for the new spool.
        public static string GenerateSpoolName
        (
            NXOpen.Part spoolPart,
            Component[] spoolComponents
        )
        {
            string prefix    = session.OptionsManager.GetStringValue( "RSD_SpoolNamePrefix" );
            string blockName = GetBlock( spoolPart );

            string specification;
            string runId;
            GetSpecificationAndRun( spoolComponents, out specification, out runId );

            Spool[] spools = spoolPart.MechanicalRoutingCollectionsManager.Spools.ToArray();
            int nSpools = spools.Length;

            string generatedName = "";
            if (!String.IsNullOrEmpty( prefix ))
                generatedName = prefix;

            if (!String.IsNullOrEmpty( blockName ))
                generatedName += blockName + " ";

            if (!String.IsNullOrEmpty( specification ))
                generatedName += specification + " ";

            if (!String.IsNullOrEmpty( runId ))
                generatedName += runId + " ";

            generatedName += nSpools.ToString( "D2" );

            string message = generatedName;
            message += " was created.";
            listingWindow.Open();
            listingWindow.WriteFullline( message );

            return generatedName;
        }

        //------------------------------------------------------------------------------------------
        // Returns the spool part's name as the "Block" to add to the spool name.
        private static string GetBlock
        (
            NXOpen.Part spoolPart
        )
        {
            return Path.GetFileName( spoolPart.Name );
        }

        //------------------------------------------------------------------------------------------
        // Gets the specification and the run from the components selected for the spool.
        private static void GetSpecificationAndRun
        (
            Component[] spoolComponents,
            out string  specification,
            out string  runId
        )
        {
            specification = "";
            runId         = "";

            RunsAssignmentManager runsManager = NXOpen.MechanicalRouting.RoutingManager.GetRoutingManager( session ).RunsAssignmentManager;

            foreach ( Component spoolComponent in spoolComponents )
            {
                string componentSpecification = GetStringAttributeValueFromObject( spoolComponent, "SPECIFICATION" );
                if (!String.IsNullOrEmpty( componentSpecification ))
                    specification = componentSpecification;

                string componentRun = GetRun( runsManager, spoolComponent );
                if (!String.IsNullOrEmpty( componentRun ))
                    runId = componentRun;

                if (!String.IsNullOrEmpty( componentSpecification ) && !String.IsNullOrEmpty( componentRun ))
                    break;
            }
        }

        //--------------------------------------------------------------------------------------------------
        // Uses the runs assignment manager to figure out which run this component belongs to.
        private static string GetRun
        (
            RunsAssignmentManager runsManager,
            Component             component
        )
        {
            if (runsManager == null)
                return "";

            Run[] runs = runsManager.GetAssignedRuns( component );
            foreach ( Run run in runs )
            {
                string runId = run.Identifier;
                if (!String.IsNullOrEmpty( runId ))
                    return runId;
            }

            return "";
        }

        //------------------------------------------------------------------------------------------
        private static String GetStringAttributeValueFromObject
        (
            NXObject nxObject,
            string   attributeName
        )
        {
            NXObject.AttributeInformation attributeInformation;

            if (GetAttributeFromObject( nxObject, attributeName, out attributeInformation ))
                return attributeInformation.StringValue;

            return null;
        }

        //------------------------------------------------------------------------------------------
        private static bool GetAttributeFromObject
        (
            NXObject                          nxObject,
            string                            attributeName,
            out NXObject.AttributeInformation attributeInformation
        )
        {
            return GetAttributeFromList( nxObject.GetUserAttributes(), attributeName, out attributeInformation );
        }

        //------------------------------------------------------------------------------------------
        private static bool GetAttributeFromList
        (
            NXObject.AttributeInformation[]   attributes,
            string                            attributeName,
            out NXObject.AttributeInformation attributeInformation
        )
        {
            attributeInformation = new NXObject.AttributeInformation();

            foreach (NXObject.AttributeInformation attribute in attributes)
            {
                string titleString = attribute.Title;

                // Watch out for attributes with no title.
                if (String.IsNullOrEmpty( titleString ))
                    continue;

                // NOTE: This does not look for aliases on the attribute titles.
                if (titleString == attributeName)
                {
                    attributeInformation = attribute;
                    return true;
                }
            }

            return false;
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
