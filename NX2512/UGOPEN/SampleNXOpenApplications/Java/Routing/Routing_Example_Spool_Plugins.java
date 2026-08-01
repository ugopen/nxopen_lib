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

    A Java class that implements example Routing Spool plugins.


==================================================================================================*/
import java.rmi.RemoteException;

import nxopen.NXException;
import nxopen.NXObject;
import nxopen.Part;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.Tag;
import nxopen.UFSession;
import nxopen.assemblies.Component;
import nxopen.mechanicalrouting.*;
import nxopen.routing.AssemblyNamePluginData;
import nxopen.routingcommon.CustomManager.SpoolAssemblyNamePlugin;
import nxopen.routingcommon.CustomManager.SpoolNamePlugin;
import nxopen.schematic.mechanical.Run;
import nxopen.uf.UFUgmgr;

public class Routing_Example_Spool_Plugins
    implements SpoolNamePlugin, SpoolAssemblyNamePlugin
{
    static Routing_Example_Spool_Plugins thePlugins              = null;
    static Session                       session                 = null;
    static UFSession                     ufSession            = null;
    static int                           spoolAssemblyCounter = 0;

    //----------------------------------------------------------------------------------------------
    // Called when NX starts.
    // Creates a new instance of this Callbacks class.
    public static void startup( String [] args ) throws NXException, java.rmi.RemoteException
    {
        if (session == null)
            session = (Session)SessionFactory.get("Session");
        
        if ( ufSession == null )
            ufSession = (UFSession)SessionFactory.get("UFSession");
        
        // Calling CreateRoutingSession is required before registering Routed System Designer (RSD)
        // plugins, callbacks, or design rules to ensure the Routing libraries are properly loaded.
        session.createRoutingSession();
    
        thePlugins = new Routing_Example_Spool_Plugins();
    
        session.licenseManager().releaseAll( null );
    }
    
    //----------------------------------------------------------------------------------------------
    // The constructor for this class.
    // Registers the Spool Plugins.
    public Routing_Example_Spool_Plugins() throws RemoteException, NXException
    {
        nxopen.routingcommon.CustomManager customManager = session.routingCustomManager();
    
        customManager.setSpoolNamePlugin( this );
        customManager.setSpoolAssemblyNamePlugin( this );
    }
    
    //----------------------------------------------------------------------------------------------
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
    public String spoolNamePlugin
    (
        Part        spoolPart,
        Component[] spoolComponents
    ) throws NXException, RemoteException
    {
        String prefix    = session.optionsManager().getStringValue( "RSD_SpoolNamePrefix" );
        String blockName = getBlock( spoolPart );
        
        String strings[]     = getSpecificationAndRun( spoolComponents );
        String specification = strings[0];
        String runId         = strings[1];
    
        int nSpools = 0;
        SpoolCollection.Iterator spoolsIterator = spoolPart.mechanicalRoutingCollectionsManager().spools().iterator();
        while (spoolsIterator.hasNext())
        {
            ++nSpools;
            spoolsIterator.next();
        }
        
        String generatedName = "";
        if ( prefix != null && !prefix.isEmpty() )
            generatedName = prefix;
    
        if ( blockName != null && !blockName.isEmpty() )
            generatedName += blockName + " ";
    
        if ( specification != null && !specification.isEmpty() )
            generatedName += specification + " ";
    
        if ( runId != null && !runId.isEmpty() )
            generatedName += runId + " ";
    
        generatedName += String.format("%02d", nSpools);
        
        return generatedName;
    }

    //----------------------------------------------------------------------------------------------
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
    public void spoolAssemblyNamePlugin
    (
        Component[]            spoolComponents,
        AssemblyNamePluginData dataObject
    ) throws NXException, RemoteException
    {
        ++spoolAssemblyCounter;

        String assemblyName = "SpoolAssembly_" + String.format("%02d", spoolAssemblyCounter );

        if (session.pdmSession() == null )
        {
            dataObject.setNativeFileName( assemblyName );
            dataObject.setNativePath( "" ); // An empty path means the current directory.
            return;
        }

        UFUgmgr ugmgr = ufSession.ugmgr();

        Tag rootFolderTag = ugmgr.askRootFolder();

        // Find the home folder and then append the name of the folder that should hold the spool assembly.
        String homeFolder = ugmgr.askFolderName( rootFolderTag );
        dataObject.setManagedModeFolderName( homeFolder + ":SpoolAssemblies" );

        dataObject.setManagedModeItemName(       "" ); // Return an empty item name to get the next available item ID.
        dataObject.setManagedModeItemRevision(   "A" );
        dataObject.setManagedModeItemType(       "Item" );
        dataObject.setManagedModeItemDescription( getSpoolName( spoolComponents ) );
    }

    //------------------------------------------------------------------------------------------
    // Returns the name of the spool that owns the given components.
    //
    // This assumes all components belong to the same spool and only belong to one spool.
    //
    private String getSpoolName
    (
        Component[] spoolComponents
    ) throws RemoteException, NXException
    {
        if (spoolComponents.length == 0)
            return "";

        Part            workPart        = session.parts().work();
        SpoolCollection spoolCollection = workPart.mechanicalRoutingCollectionsManager().spools();

        Spool spool = spoolCollection.getSpoolFromComponent( spoolComponents[0] );
        if ( spool == null )
            return "";

        return spool.name();
    }
    
    //----------------------------------------------------------------------------------------------
    // Returns the spool part's name as the "Block" to add to the spool name.
    private String getBlock
    (
        Part spoolPart
    ) throws RemoteException, NXException
    {
        return spoolPart.name();
    }
    
    //----------------------------------------------------------------------------------------------
    // Gets the specification and the run from the components selected for the spool.
    private String[] getSpecificationAndRun
    (
        Component[] spoolComponents
    ) throws RemoteException, NXException
    {
        String specification = "";
        String runId = "";
        
        RunsAssignmentManager runsManager = RoutingManagerFactory.GetRoutingManager( session ).runsAssignmentManager();
    
        for ( Component spoolComponent : spoolComponents )
        {
            String componentSpecification = getStringAttributeValueFromObject( spoolComponent, "SPECIFICATION" );
            if ( componentSpecification != null && !componentSpecification.isEmpty() )
                specification = componentSpecification;
            
            String componentRun = getRun( runsManager, spoolComponent );
            if (componentRun != null && !componentRun.isEmpty() )
                runId = componentRun;
            
            if (specification != null && !specification.isEmpty() &&
                runId         != null && !runId.isEmpty() )
            {
                break;
            }
        }
        
        String[] strings = new String[2];
        strings[0] = specification;
        strings[1] = runId;
    
        return strings;
    }
    
    //----------------------------------------------------------------------------------------------
    // Uses the runs assignment manager to figure out which run this component belongs to.
    private static String getRun
    (
        RunsAssignmentManager runsManager,
        Component             component
    ) throws RemoteException, NXException
    {
        if (runsManager == null)
            return "";
    
        Run[] runs = runsManager.getAssignedRuns( component );
        for( Run run : runs )
        {
            String runId = run.identifier();
            if (runId != null && !runId.isEmpty() )
                return runId;
        }
    
        return "";
    }
    
    //----------------------------------------------------------------------------------------------
    // Returns the string value of the attribute or null if it does not exist.
    private static String getStringAttributeValueFromObject
    (
        NXObject nxObject,
        String   attributeName
    ) throws RemoteException, NXException
    {
        NXObject.AttributeInformation attributeInformation = getAttributeFromObject( nxObject, attributeName );
        if ( attributeInformation == null || attributeInformation.type != NXObject.AttributeType.STRING )
            return null;
    
        return attributeInformation.stringValue;
    }
    
    //----------------------------------------------------------------------------------------------
    // Returns true and the attribute information object of the attribute if the attribute exists.
    // Returns false if not.
    private static NXObject.AttributeInformation getAttributeFromObject
    (
        NXObject nxObject,
        String   attributeName
    ) throws RemoteException, NXException
    {
        return getAttributeFromList( nxObject.getUserAttributes(), attributeName );
    }
    
    //----------------------------------------------------------------------------------------------
    // Returns true and the attribute information object of the attribute if the attribute is in the list.
    // Returns false if not.
    // NOTE: The attribute name comparison is case insensitive.
    private static NXObject.AttributeInformation getAttributeFromList
    (
        NXObject.AttributeInformation[] attributes,
        String                          attributeName
    )
    {
        for ( nxopen.NXObject.AttributeInformation attribute : attributes )
        {
            // Watch out for attributes with no title.
            if ( attribute.title.length() == 0 )
                continue;
    
            // NOTE: This does not look for aliases on the attribute titles.
            if ( attribute.title.compareToIgnoreCase( attributeName ) == 0 )
            {
                return attribute;
            }
        }
    
        return null;
    }
    
    //----------------------------------------------------------------------------------------------
    // Tells NX when to unload your application.
    // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
    public static int getUnloadOption(String arg)
    {
        return Session.LibraryUnloadOption.AT_TERMINATION;
    }
}
