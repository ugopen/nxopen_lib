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
using NXOpen.UF;
using NXOpen.PDM;

namespace RoutingCommon
{
    public class SpoolPlugins
    {
        // Static class members
        static Session       session       = null;
        static ListingWindow listingWindow = null;
        static CustomManager customManager = null;
        private static int spoolAssemblyCounter = 0;

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
            customManager.SetSpoolAssemblyNamePlugin( GenerateSpoolAssemblyName );

            session.LicenseManager.ReleaseAll( null );

            return 0;
        }

        //------------------------------------------------------------------------------------------
        // Called by the Spool dialog to create a name for the new spool.
        // 
        // The name this plugin generates is a combination of:
        // 
        //   - Spool description: See BuildSpoolDescription for more information.
        //   - Index:             An index one greater than the number of existing spools in the part.
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
            string generatedName = BuildSpoolDescription( spoolPart, spoolComponents );

            Spool[] spools = spoolPart.MechanicalRoutingCollectionsManager.Spools.ToArray();
            generatedName += spools.Length.ToString( "D2" );

            string message = generatedName;
            message += " was created.";
            listingWindow.Open();
            listingWindow.WriteFullline( message );

            return generatedName;
        }

        //------------------------------------------------------------------------------------------
        // Called by the Publish Spool Assemblies command to create a name for the new spool assembly part.
        //
        // The spool assembly name plugin is given a data object that needs to be filled out
        // completely, either for a native file or a Teamcenter item, in order for Routing to
        // create a new part for the spool.
        //
        // \param[in]
        //      spoolComponents
        //          The components of the spool that are to go in the new spool assembly.
        // 
        // \param[out]
        //      dataObject
        //          The data object that is to be filled out by the plugin.
        public static void GenerateSpoolAssemblyName
        (
            Component[]                           spoolComponents,
            NXOpen.Routing.AssemblyNamePluginData dataObject
        )
        {
            ++spoolAssemblyCounter;

            string assemblyName = "SpoolAssembly_" + spoolAssemblyCounter.ToString( "D4" );

            if (session.PdmSession == null )
            {
                dataObject.NativeFileName = assemblyName;
                dataObject.NativePath     = ""; // An empty path means the current directory.
                return;
            }

            UFUgmgr ugmgr = UFSession.GetUFSession().Ugmgr;

            Tag rootFolderTag;
            ugmgr.AskRootFolder( out rootFolderTag );

            // Find the home folder and then append the name of the folder that should hold the spool assembly.
            string homeFolder = "";
            ugmgr.AskFolderName( rootFolderTag, out homeFolder );
            dataObject.ManagedModeFolderName      = homeFolder + ":SpoolAssemblies";

            dataObject.ManagedModeItemName        = ""; // Return an empty item name to get the next available item ID.
            dataObject.ManagedModeItemRevision    = "A";
            dataObject.ManagedModeItemType        = "Item";
            dataObject.ManagedModeItemDescription = GetSpoolName( spoolComponents );
        }

        //------------------------------------------------------------------------------------------
        // Returns the name of the spool that owns the given components.
        //
        // This assumes all components belong to the same spool and only belong to one spool.
        //
        private static string GetSpoolName
        (
            Component[] spoolComponents
        )
        {
            if (spoolComponents.Length == 0)
                return "";

            Session         session         = Session.GetSession();
            Part            workPart        = session.Parts.Work;
            SpoolCollection spoolCollection = workPart.MechanicalRoutingCollectionsManager.Spools;

            Spool spool = spoolCollection.GetSpoolFromComponent( spoolComponents[0] );
            if ( spool == null )
                return "";

            return spool.Name;
        }

        //------------------------------------------------------------------------------------------
        // Builds a description of the spool that includes:
        // 
        //   - Prefix:        The spool Name Prefix defined in the Routed System Designer->Mechanical->Spools customer defaults.
        //   - Block:         The Block identifier is simply the name of the work part.
        //   - Specification: The specification assigned to the components.
        //   - Run ID:        The identifier of the run to which the components belong.
        //
        private static string BuildSpoolDescription
        (
            NXOpen.Part spoolPart,
            Component[] spoolComponents
        )
        {
            string prefix = session.OptionsManager.GetStringValue( "RSD_SpoolNamePrefix" );
            string blockName = GetBlock( spoolPart );

            string specification;
            string runId;
            GetSpecificationAndRun( spoolComponents, out specification, out runId );

            string description = "";
            if (!String.IsNullOrEmpty( prefix ))
                description = prefix;

            if (!String.IsNullOrEmpty( blockName ))
                description += blockName + " ";

            if (!String.IsNullOrEmpty( specification ))
                description += specification + " ";

            if (!String.IsNullOrEmpty( runId ))
                description += runId + " ";

            return description;
        }

        //------------------------------------------------------------------------------------------
        // Returns the spool part's name as the "Block" to add to the spool name.
        private static string GetBlock
        (
            NXOpen.Part spoolPart
        )
        {
            if ( spoolPart != null )
                return Path.GetFileName( spoolPart.Name );

            return "";
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
