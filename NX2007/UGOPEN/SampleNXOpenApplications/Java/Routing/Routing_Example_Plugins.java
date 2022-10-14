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

    A Java class that implements an example of the PLMXML post export plugin.


==================================================================================================*/
import java.rmi.RemoteException;
import java.util.ArrayList;

import javax.swing.JFileChooser;

import nxopen.ListingWindow;
import nxopen.LogFile;
import nxopen.NXException;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.Tag;
import nxopen.TaggedObjectManager;
import nxopen.UFSession;
import nxopen.routing.CharacteristicList;
import nxopen.routing.ChoosePartPluginData;
import nxopen.routing.ComponentNamePluginData;
import nxopen.routing.CustomManager;
import nxopen.routing.CustomManager.ComponentNamePlugin;
import nxopen.routing.electrical.ElectricalStockDevice;
import nxopen.routing.electrical.SortConnectionsPluginData;
import nxopen.uf.UFUgmgr;

//------------------------------------------------------------------------------------------------
public class Routing_Example_Plugins
    implements CustomManager.ImportExportPlugin, CustomManager.PlmxmlObjectNamePlugin,
               CustomManager.SortConnectionsPlugin, CustomManager.ChoosePartPlugin, ComponentNamePlugin
{
    static Routing_Example_Plugins thePlugins = null;
    static Session theSession = null;
    static ListingWindow listingWindow = null;
    private static int stockNumberCounter = 0;

    //------------------------------------------------------------------------------------------
    // Called when NX starts.
    // Creates a new instance of this Callbacks class.
    public static void startup( String [] args ) throws NXException, java.rmi.RemoteException
    {
        if (theSession == null)
            theSession = (Session)SessionFactory.get("Session");

        if (listingWindow == null)
            listingWindow = theSession.listingWindow();

        thePlugins = new Routing_Example_Plugins();
    }

    //------------------------------------------------------------------------------------------
    // The constructor for this class.
    // Registers the Plugins.
    public Routing_Example_Plugins() throws RemoteException, NXException
    {
        try
        {
            CustomManager customManager = theSession.routeCustomManager();

            customManager.setPlmXmlPostExportPlugin(this);
            customManager.setPlmXmlRouteNodeNamePlugin(this);
            customManager.setSortConnectionsPlugin( this );
            customManager.setChoosePartPlugin(this);

            // Routing calls the stock component name plugin when creating permanent stock using the
            // Convert to Stock as Components command.
            customManager.setStockComponentNamePlugin(this);

            // Routing calls the temporary stock component name plugin when you are creating stocks
            // on the fly in Stock as Components mode.
            customManager.setTemporaryStockComponentNamePlugin(this);
        }
        catch ( NXException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***Error in Plugins constructor: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in Plugins constructor: " + ex.getMessage() );
        }
    }

    //---------------------------------------------------------------------------------------------
    // This is the PLMXML Export plugin.
    //
    // It simply prints the given file name to the Listing Window and Log File.
    public void importExportPlugin(String fileName) throws NXException, RemoteException
    {
        echo( "\n\n*** Java PLMXML Export plugin called with '" + fileName + ".\n");

        echo("");
    }


    //---------------------------------------------------------------------------------------------
    // This is the Route Node Name plugin used during PLMXML Export.
    //
    // It simply prints a message to the Listing Window and Log File and returns the node name "RNx".
    public String plmxmlObjectNamePlugin() throws NXException, RemoteException
    {
        echo("\n\n*** Java RouteNodeNamePlugin called");
        return "RNx";
    }

    //------------------------------------------------------------------------------------------
    // This is the Sort Connections plugin used during Autoroute and Manual Route.
    //
    // It sorts the given Stock Devices in order of their tags.
    public void sortConnectionsPlugin(SortConnectionsPluginData dataObject)
            throws NXException, RemoteException
    {
        ElectricalStockDevice[] stockDevices = dataObject.getStockDevicesToSort();

        echo("*** Java Sort Connections plugin called with " + stockDevices.length + " stock devices.");

        ArrayList<Tag> stockDeviceTags = new ArrayList<Tag>();
        for ( int index = 0; index < stockDevices.length; ++index )
        {
            echo("  Stock Device " + stockDevices[index].tag() + ".");
            stockDeviceTags.add( stockDevices[index].tag() );
        }

        // TODO: Sort the stock devices here.

        TaggedObjectManager theTaggedObjectManager = theSession.taggedObjectManager();

        echo( "" );
        ElectricalStockDevice[] sortedStockDevices = new ElectricalStockDevice[ stockDeviceTags.size() ];
        for ( int index = 0; index < stockDeviceTags.size(); ++index )
        {
            echo("  Sorted Stock Device " + stockDeviceTags.get(index) + ".");
            sortedStockDevices[index] = (ElectricalStockDevice)theTaggedObjectManager.get( stockDeviceTags.get(index) );
        }

        dataObject.setSortedStockDevices( stockDevices );
    }

    //------------------------------------------------------------------------------------------
    // This is the Choose Part plugin called from Place Part to let you choose a part to place.
    public int choosePartPlugin(ChoosePartPluginData dataObject)
            throws NXException, RemoteException
    {
        final JFileChooser fc = new JFileChooser();

        int returnVal = fc.showOpenDialog( null );

         if (returnVal != JFileChooser.APPROVE_OPTION)
             return -1;

         String fileName = fc.getSelectedFile().getName();

         dataObject.setPartName( fileName );
         dataObject.setPartNumber("ExamplePartNumber001");
         dataObject.setMemberName(""); // No member name since this is not a member of a part family.

         // Some example attributes.
         CharacteristicList exampleCharacteristics = theSession.preferences().routingApplicationView().partPreferences().partLibrary().createCriteria();
         exampleCharacteristics.setCharacteristic("USER_CHARX_TITLE1", "User_charx_value1");
         exampleCharacteristics.setCharacteristic("USER_CHARX_TITLE2", "User_charx_value2");

         dataObject.setCharacteristics( exampleCharacteristics );

        return 0;
    }

    //------------------------------------------------------------------------------------------
    // The stock component name plugin is given a data object that needs to be filled out completely.
    public void componentNamePlugin(ComponentNamePluginData dataObject) throws NXException, RemoteException
    {
        echo( "StockComponentNamePlugin" );

        ++stockNumberCounter;

        String stockName = "StockComponent_" + String.valueOf( stockNumberCounter );
        String homeFolder = "";

        UFSession ufSession = ((UFSession)SessionFactory.get("UFSession"));
        boolean isManagedMode = ufSession.UF().isUgmanagerActive();
        if (isManagedMode)
        {
            UFUgmgr ugmgr = ufSession.ugmgr();

            Tag rootFolderTag = ugmgr.askRootFolder();
            homeFolder = ugmgr.askFolderName( rootFolderTag );
        }

        dataObject.setComponentName( stockName );
        dataObject.setRenameComponentPartFlag( true );

        dataObject.setNativeFileName( stockName );
        dataObject.setNativePath( "" ); // An empty path means the current directory.
        dataObject.setManagedModeFolderName( homeFolder + ":StockComponents" );
        dataObject.setManagedModeItemName( stockName );
        dataObject.setManagedModeItemRevision( "A" );
        dataObject.setManagedModeItemType( "Item" );
    }
    
    //------------------------------------------------------------------------------------------
    // Writes the given string to the Listing Window and the syslog.
    //
    // \param[in]
    //      stringToWrite
    //          The string to write.
    public void echo( String stringToWrite ) throws NXException, RemoteException
    {
        try
        {
            ListingWindow listingWindow = theSession.listingWindow();

            if (!listingWindow.isOpen())
                listingWindow.open();

            listingWindow.writeFullline(stringToWrite);

            LogFile syslog = theSession.logFile();
            syslog.writeLine(stringToWrite);
        }
        catch ( NXException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***NXException in Plugins.echo: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in Plugins.echo: " + ex.getMessage() );
        }
    }

    //------------------------------------------------------------------------------------------
    // Tells NX when to unload your application.
    // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
    public static int getUnloadOption(String arg)
    {
        return Session.LibraryUnloadOption.AT_TERMINATION;
    }
}
