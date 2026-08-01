
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

    A Java class that implements an example of the Create Path Design Rule.


==================================================================================================*/
import java.rmi.RemoteException;

import nxopen.ListingWindow;
import nxopen.LogFile;
import nxopen.NXException;
import nxopen.NXObject;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.routing.CustomManager;
import nxopen.routing.CustomManager.DesignRuleReason;

//------------------------------------------------------------------------------------------------
public class DesignRules implements nxopen.routing.CustomManager.DesignRule
{
    static DesignRules theDesignRules = null;
    static Session theSession = null;
    static ListingWindow listingWindow = null;

    //------------------------------------------------------------------------------------------
    // Called when NX starts.
    // Creates a new instance of this Callbacks class.
    public static void startup( String [] args ) throws NXException, java.rmi.RemoteException
    {
        if (theSession == null)
            theSession = (Session)SessionFactory.get("Session");

        if (listingWindow == null)
            listingWindow = theSession.listingWindow();

        theDesignRules = new DesignRules();
    }

    //------------------------------------------------------------------------------------------
    // The constructor for this class.
    // Registers the Design Rules.
    public DesignRules() throws RemoteException, NXException
    {        
        try
        {
            String name = "Create Path";
            String description = "This example Create Path design rule simply prints out the objects it has been given.";
            CustomManager customManager = theSession.routeCustomManager();
            
            customManager.addDesignRule(DesignRuleReason. CREATE_PATH, name, description, this );
        }
        catch ( NXException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***Error in DesignRules constructor: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in DesignRules constructor: " + ex.getMessage() );
        }        
    }

    //---------------------------------------------------------------------------------------------
    // This is the Create Path Design Rule.
    //
    // It simply prints the tags of the given object to the Listing Window and Log File.
    public void designRule(DesignRuleReason reason, NXObject[] objects) throws NXException, RemoteException 
    {    
        echo( "\n\n*** Java Create Path Design Rule called with " + objects.length + " objects for reason " + reason.toString() + ".\n");
        
        for ( int index = 0; index < objects.length; ++index )
        {
            echo("  NX Object " + objects[index].tag().toString() );
        }

        echo("");
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
            theSession.logFile().writeLine( "\n\n\n***NXException in DesignRules.echo: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine( "\n\n\n***RemoteException in DesignRules.echo: " + ex.getMessage() );
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


