/*==================================================================================================
                                       Copyright 2020 Siemens
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A Java class that implements example Routing Cableway plugins.


==================================================================================================*/
import java.rmi.RemoteException;
import java.text.SimpleDateFormat;
import java.util.Date;

import nxopen.INXObject;
import nxopen.ListingWindow;
import nxopen.LogFile;
import nxopen.NXException;
import nxopen.NXObject;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.assemblies.Component;
import nxopen.routing.CustomManager.DisciplineChangedPlugin;
import nxopen.routingcommon.CustomManager.Application;
import nxopen.routingcommon.CustomManager.CablewayAreaNamePlugin;
import nxopen.routingcommon.CustomManager.CablewayDeviceIdentifierPlugin;
import nxopen.routingcommon.CustomManager.CablewayPostExportPlugin;
import nxopen.routingcommon.CustomManager.CablewayPreExportPlugin;
import nxopen.routingcommon.CustomManager.CablewayUniqueNodeNamePlugin;
import nxopen.routingcommon.CustomManager.CablewayUniqueSegmentNamePlugin;
import nxopen.routingcommon.CustomManager.CablewayXmlFileNamePlugin;
import nxopen.routingcommon.CustomManager.RSDApplicationEnterPlugin;
import nxopen.routingcommon.CustomManager.RSDApplicationExitPlugin;

//--------------------------------------------------------------------------------------------------
public class Routing_Example_Cableway_Plugins
    implements CablewayXmlFileNamePlugin, CablewayUniqueNodeNamePlugin,
    CablewayUniqueSegmentNamePlugin, CablewayDeviceIdentifierPlugin,
    CablewayPreExportPlugin, CablewayPostExportPlugin,
    CablewayAreaNamePlugin, RSDApplicationExitPlugin, RSDApplicationEnterPlugin, DisciplineChangedPlugin
{
    static Routing_Example_Cableway_Plugins thePlugins = null;
    static Session theSession = null;
    static ListingWindow listingWindow = null;
    private static int nodeCounter = 0;
    private static int segmentCounter = 0;

    //----------------------------------------------------------------------------------------------
    // Called when NX starts.
    // Creates a new instance of this Callbacks class.
    public static void startup( String [] args ) throws NXException, java.rmi.RemoteException
    {
        if (theSession == null)
            theSession = (Session)SessionFactory.get("Session");

        if (listingWindow == null)
            listingWindow = theSession.listingWindow();

        // Calling CreateRoutingSession is required before registering Routed System Designer (RSD)
        // plugins, callbacks, or design rules to ensure the Routing libraries are properly loaded.
        theSession.createRoutingSession();

        thePlugins = new Routing_Example_Cableway_Plugins();
    }

    //----------------------------------------------------------------------------------------------
    // Called when NX starts.
    // Called from File->Execute->NX Open. Useful for testing.
    public static void main(String[] argv) throws Exception
    {
        if (theSession == null)
            theSession = (Session)SessionFactory.get("Session");

        if (listingWindow == null)
            listingWindow = theSession.listingWindow();

        // Calling CreateRoutingSession is required before registering Routed System Designer (RSD)
        // plugins, callbacks, or design rules to ensure the Routing libraries are properly loaded.
        theSession.createRoutingSession();

        thePlugins = new Routing_Example_Cableway_Plugins();
    }

    //----------------------------------------------------------------------------------------------
    // The constructor for this class.
    // Registers the Plugins.
    public Routing_Example_Cableway_Plugins() throws RemoteException, NXException
    {
        try
        {
            nxopen.routingcommon.CustomManager customManager = theSession.routingCustomManager();

            customManager.setRSDApplicationEnterPlugin( this );
            customManager.setRSDApplicationExitPlugin( this );
        }
        catch ( NXException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***Error in Cableway Plugins constructor: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in Cableway Plugins constructor: " + ex.getMessage() );
        }
    }

    //----------------------------------------------------------------------------------------------
    public void rsdapplicationEnterPlugin(Application application) throws NXException, RemoteException
    {
        try
        {
            if (application == Application.ELECTRICAL)
            {
                echo( "Entering the Electrical application " );
            }
            else
            {
                // When entering the Mechanical application, register a "discipline changed" plugin to
                // watch for a change to the Cableway discipline.
                nxopen.routing.CustomManager routeCustomManager = theSession.routeCustomManager();

                routeCustomManager.setDisciplineChangedPlugin( this );
            }
        }
        catch ( NXException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***Error in Cableway Plugins constructor: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in Cableway Plugins constructor: " + ex.getMessage() );
        }
    }

    //----------------------------------------------------------------------------------------------
    public void rsdapplicationExitPlugin(Application application) throws NXException, RemoteException
    {
        echo( "Java Application Exit" );

        if (application == Application.ELECTRICAL)
        {
            echo( "Exiting the Electrical application " );
        }
        else
        {
            echo( "Exiting the Mechanical application " );
        }

        // When exiting any Routing application, remove the "discipline changed" plugin and the
        // "Cableways" plugins
        nxopen.routing.CustomManager routeCustomManager = theSession.routeCustomManager();
        routeCustomManager.removeDisciplineChangedPlugin();

        deregisterPlugins();
    }

    //----------------------------------------------------------------------------------------------
    public void disciplineChangedPlugin(String previousDisciplineName, String newDisciplineName) throws NXException, RemoteException
    {
        echo( "Java DisciplineChanged" );

        String cablewayDisciplineName = theSession.optionsManager().getStringValue("RSD_Cableway_Discipline_Name");

        // Register all the Cableways plugins if the new discipline is the Cableways discipline.
        if (cablewayDisciplineName.equals( newDisciplineName ) )
        {
            echo( "  Registering Cableway plugins." );
            registerPlugins();
        }
        else
        {
            echo( "  Deregistering Cableway plugins." );
            deregisterPlugins();
        }
    }

    //----------------------------------------------------------------------------------------------
    // Registers the Plugins.
    public void registerPlugins() throws RemoteException, NXException
    {
        try
        {
            echo( "Java registerPlugins" );

            nxopen.routingcommon.CustomManager customManager = theSession.routingCustomManager();

            customManager.setCablewayXmlFileNamePlugin( this );
            customManager.setCablewayUniqueNodeNamePlugin( this );
            customManager.setCablewayUniqueSegmentNamePlugin( this );
            customManager.setCablewayDeviceIdentifierPlugin( this );
            customManager.setCablewayPreExportPlugin( this );
            customManager.setCablewayPostExportPlugin( this );
            customManager.setCablewayAreaNamePlugin( this );
        }
        catch ( NXException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***Error in Cableway Plugins constructor: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in Cableway Plugins constructor: " + ex.getMessage() );
        }
    }

    //----------------------------------------------------------------------------------------------
    // Deregisters the Plugins.
    public void deregisterPlugins() throws RemoteException, NXException
    {
        try
        {
            echo( "Java deregisterPlugins" );

            nxopen.routingcommon.CustomManager customManager = theSession.routingCustomManager();

            customManager.removeCablewayXmlFileNamePlugin();
            customManager.removeCablewayUniqueNodeNamePlugin();
            customManager.removeCablewayUniqueSegmentNamePlugin();
            customManager.removeCablewayDeviceIdentifierPlugin();
            customManager.removeCablewayPreExportPlugin();
            customManager.removeCablewayPostExportPlugin();
            customManager.removeCablewayAreaNamePlugin();
        }
        catch ( NXException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***Error in Cableway Plugins constructor: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in Cableway Plugins constructor: " + ex.getMessage() );
        }
    }

    //----------------------------------------------------------------------------------------------
    // Called before Routing exports a Cableway XML file to return the name of the XML file
    // into which to write the Cableway data.
    public String cablewayXmlFileNamePlugin() throws NXException, RemoteException
    {
        echo( "Java cablewayXmlFileName" );

        SimpleDateFormat formatter = new SimpleDateFormat("yyyy_MM_dd_HH_mm");
        Date date = new Date();
        String formattedDate = formatter.format(date);

        return "RoutingCablewayExport_" + formattedDate + ".xml";
    }

    //----------------------------------------------------------------------------------------------
    // Called while Routing exports a Cableway XML file to create a new, unique identifier
    // for the given control point.
    //
    // \param[in]
    //      areaName
    //          The name of the area under which the cableway part and node object live.
    //
    // \param[in]
    //      cablewaySubassembly
    //          The cableway subassembly that owns the node object.
    //
    // \param[in]
    //      nodeObjectOccurrence
    //          The control point or point occurrence that needs a unique ID.
    //
    // \return
    //      The unique ID for this control point.
    public String cablewayUniqueNodeNamePlugin( String areaName, Component cablewaySubassembly, NXObject nodeObjectOccurrence) throws NXException, RemoteException
    {
        echo( "Java cablewayUniqueNodeNamePlugin");

        // If the node object occurrence already has a name, just return it.
        if ( !nodeObjectOccurrence.name().isEmpty() )
            return nodeObjectOccurrence.name();

        nodeCounter += 1;

        return nodeObjectOccurrence.tag().toString() + "_" + String.valueOf( nodeCounter );
    }

    //----------------------------------------------------------------------------------------------
    // Called while Routing exports a Cableway XML file to create a new, unique identifier
    // for the given segment.
    //
    // \param[in]
    //      areaName
    //          The name of the area under which the cableway part and segment live.
    //
    // \param[in]
    //      cablewaySubassembly
    //          The cableway subassembly that owns the segment object.
    //
    // \param[in]
    //      segmentObject
    //          The segment occurrence or hanger component that needs a unique ID.
    //
    // \return
    //      The unique ID for this segment.
    public String cablewayUniqueSegmentNamePlugin(String areaName, Component cablewaySubassembly, NXObject segmentObject) throws NXException, RemoteException
    {
        echo( "Java cablewayUniqueSegmentNamePlugin");

        INXObject segmentPrototype = segmentObject.prototype();

        // When given the entity occurrence of a Routing segment or a curve, check the curve name for an
        // existing unique ID.
        if ( segmentPrototype instanceof nxopen.routing.ArcSegment    ||
             segmentPrototype instanceof nxopen.routing.LineSegment   ||
             segmentPrototype instanceof nxopen.routing.SplineSegment ||
             segmentPrototype instanceof nxopen.Arc    ||
             segmentPrototype instanceof nxopen.Line   ||
             segmentPrototype instanceof nxopen.Spline )
        {
            String uniqueID = segmentObject.name();
            if (uniqueID.length() > 0)
                return uniqueID;
        }

        // When given a hanger component that must be represented as a zero-length segment,
        // look for the CABLEWAY_HANGER_ID attribute on the component.
        if ( segmentPrototype instanceof nxopen.Part )
        {
           String uniqueID = segmentObject.getStringUserAttribute( "CABLEWAY_HANGER_ID", -1 );
            if (uniqueID.length() > 0)
                return uniqueID;
        }

        // Otherwise, create a new unique ID and return it.
        segmentCounter += 1;
        return segmentObject.tag().toString() + "_" + String.valueOf( segmentCounter );
    }

    //----------------------------------------------------------------------------------------------
    // Called while Routing exports a Cableway XML file to identify if the given component
    // is a device that should be exported.
    //
    // \param[in]
    //      component
    //          The component to check.
    //
    // \return
    //      The device ID to use for this component in the Cableway XML file.
    //      Returns an empty string if this device should not be exported.
    public String cablewayDeviceIdentifierPlugin( Component component ) throws NXException, RemoteException
    {
        echo( "Java cablewayDeviceIdentifier");

        String deviceID = "";
        if (component.hasUserAttribute( "Electrical_Device_ID", NXObject.AttributeType.STRING, -1 ))
            deviceID = component.getStringUserAttribute( "Electrical_Device_ID", -1 );

        return deviceID;
    }

    //----------------------------------------------------------------------------------------------
    // Called just after Routing exports a Cableway XML file.
    //
    // \param[in]
    //      xmlFileName
    //          The name of the XML file Routing just exported.
    public void cablewayPreExportPlugin( String xmlFileName ) throws NXException, RemoteException
    {
        echo( "Java cablewayPreExportPlugin called with " + xmlFileName );
    }

    //----------------------------------------------------------------------------------------------
    // Called just after Routing exports a Cableway XML file.
    //
    // \param[in]
    //      xmlFileName
    //          The name of the XML file Routing just exported.
    public void cablewayPostExportPlugin( String xmlFileName ) throws NXException, RemoteException
    {
        echo( "Java cablewayPostExportPlugin called with " + xmlFileName );
    }

    //------------------------------------------------------------------------------------------
    // Called during Cableway export to create an area name for a given component and all
    // the components under it.
    //
    // \param[in]
    //      component
    //          The component to check.
    //
    // \return
    //      The area name to use for all the devices, hangers, nodes, segments, etc., found
    //      under this component.
    public String cablewayAreaNamePlugin( Component component ) throws NXException, RemoteException
    {
        echo( "Java cablewayAreaName" );

        String areaName = "";
        if (component.hasUserAttribute( "Electrical_Device_Area", NXObject.AttributeType.STRING, -1 ))
            areaName = component.getStringUserAttribute( "Electrical_Device_Area", -1 );

        return areaName;
    }

    //----------------------------------------------------------------------------------------------
    // Writes the given string to the Listing Window and the log file.
    //
    // \param[in]
    //      stringToWrite
    //          The string to write.
    public static void echo( String stringToWrite ) throws NXException, RemoteException
    {
        try
        {
            ListingWindow listingWindow = theSession.listingWindow();

            if (!listingWindow.isOpen())
                listingWindow.open();

            listingWindow.writeFullline(stringToWrite);

            LogFile logFile = theSession.logFile();
            logFile.writeLine(stringToWrite);
        }
        catch ( NXException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***NXException in Plugins echo: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in Plugins echo: " + ex.getMessage() );
        }
    }

    //----------------------------------------------------------------------------------------------
    // Tells NX when to unload your application.
    // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
    public static int getUnloadOption(String arg)
    {
        return Session.LibraryUnloadOption.AT_TERMINATION;
    }
}
