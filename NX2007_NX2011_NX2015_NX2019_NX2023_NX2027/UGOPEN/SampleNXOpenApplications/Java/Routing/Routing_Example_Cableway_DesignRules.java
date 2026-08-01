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

    A Java class that implements example Routing Cableway Design Rules.


==================================================================================================*/
import java.rmi.RemoteException;

import nxopen.Body;
import nxopen.ListingWindow;
import nxopen.NXException;
import nxopen.NXObject;
import nxopen.Part;
import nxopen.TaggedObjectCollection.Iterator;
import nxopen.UI;
import nxopen.routing.Stock;
import nxopen.routing.StockCollection;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.assemblies.Component;
import nxopen.routingcommon.CustomManager;
import nxopen.routing.CustomManager.DesignRuleReason;

//------------------------------------------------------------------------------------------------
public class Routing_Example_Cableway_DesignRules implements nxopen.routingcommon.CustomManager.DesignRule
{
    static Routing_Example_Cableway_DesignRules theDesignRules = null;
    static Session theSession = null;
    static ListingWindow listingWindow = null;
    static String tierCountAttributeName = "TierCount";
    static String hangerSegregationAttributeName = "Cableway Hanger Segregation Code";
    static String segmentSegregationAttributeName = "Cableway Segment Segregation";

    //------------------------------------------------------------------------------------------
    // Called when NX starts.
    // Creates a new instance of this Callbacks class.
    public static void startup( String [] args ) throws NXException, java.rmi.RemoteException
    {
        if (theSession == null)
            theSession = (Session)SessionFactory.get("Session");

        if (listingWindow == null)
            listingWindow = theSession.listingWindow();

        theDesignRules = new Routing_Example_Cableway_DesignRules();
    }

    //------------------------------------------------------------------------------------------
    // The constructor for this class.
    // Registers the Design Rules.
    public Routing_Example_Cableway_DesignRules() throws RemoteException, NXException
    {
        try
        {
            String name = "Segregation Code";
            String description = "The Segregation Code design rule ensures no multi-tier " +
                                 "component has more segregation codes than tiers.";

            CustomManager customManager = theSession.routingCustomManager();

            customManager.addDesignRule(DesignRuleReason.CABLEWAY_VALIDATION, name, description, this );

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

    //----------------------------------------------------------------------------------------------
    // Returns true and the attribute information object of the attribute if the attribute exists.
    // Returns false if not.
    private NXObject.AttributeInformation getAttributeFromObject
    (
        NXObject nxObject,
        String   attributeName

    ) throws RemoteException, NXException
    {
        NXObject.AttributeInformation attributeInformation = getAttributeFromList( nxObject.getUserAttributes(), attributeName );

        return attributeInformation;
    }

    //----------------------------------------------------------------------------------------------
    // Returns true and the attribute information object of the attribute if the attribute is in the list.
    // Returns false if not.
    // NOTE: The attribute name comparison is case insensitive.
    private NXObject.AttributeInformation getAttributeFromList
    (
        NXObject.AttributeInformation[] attributes,
        String                          attributeName
    ) throws RemoteException, NXException
    {
        for ( nxopen.NXObject.AttributeInformation attribute : attributes )
        {
            // Watch out for attributes with no title.
            if ( attribute.title.length() == 0 )
                continue;

            // NOTE: This does not look for aliases on the attribute titles.
            if ( attribute.title.compareToIgnoreCase( attributeName ) == 0 )
                return attribute;
        }

        return null;
    }

    //------------------------------------------------------------------------------------------
    // Returns the stock body (e.g. the cable tray body) if the given component is a stock component.
    // Returns the given component if the component is not a stock component.
    private NXObject getStockBodyInComponent
    (
        Component component
    ) throws RemoteException, NXException
    {
        Part componentPart = (Part)component.prototype();
        if (componentPart == null || !componentPart.isFullyLoaded() )
            return component;

        StockCollection stockCollection = componentPart.routeManager().stocks();

        // Since all stock components have the same type of stock, we can return the first stock body.
        for (Iterator stockItr = stockCollection.iterator(); stockItr.hasNext();)
        {
            Stock stock = (Stock) stockItr.next();
            Body[] stockBodies = stock.getBodies();
            if (stockBodies.length > 0)
                return stockBodies[0];
        }

        // If there are no stock, return the given component.
        return component;
    }

    //------------------------------------------------------------------------------------------
    // Returns the value of the tier count attribute if there is one. Returns zero if not.
    private int getTierCount
    (
        Component component
    ) throws RemoteException, NXException
    {
        NXObject nxObject = getStockBodyInComponent( component );

        NXObject.AttributeInformation attributeInformation = getAttributeFromObject( nxObject, tierCountAttributeName );
        if ( attributeInformation == null )
            return 0;

        if (attributeInformation.type == NXObject.AttributeType.INTEGER)
            return attributeInformation.integerValue;

        if (attributeInformation.type == NXObject.AttributeType.REAL)
            return (int)attributeInformation.realValue;

        return 0;
    }

    //--------------------------------------------------------------------------------------------------
    // Returns the number of elements in the segregation attribute array if it exists. Returns zero if not.
    private int getSegregationCount
    (
        Component component
    ) throws RemoteException, NXException
    {
        NXObject nxObject = getStockBodyInComponent( component );

        if (nxObject.hasUserAttribute( hangerSegregationAttributeName, NXObject.AttributeType.ANY, -1 ))
            return nxObject.getUserAttributeSize( hangerSegregationAttributeName, NXObject.AttributeType.ANY );

        return nxObject.getUserAttributeSize( segmentSegregationAttributeName, NXObject.AttributeType.ANY );
    }

    //------------------------------------------------------------------------------------------
    // Ensures the tier count is greater than or equal too the number of elements in the segregation
    // attribute array.
    //
    // In other words, ensures there are not more segregation codes than there are tiers.
    private void checkComponentTierCount
    (
        ListingWindow listingWindow,
        int indentation,
        Component component
    ) throws RemoteException, NXException
    {
        int tierCount = getTierCount( component );
        int nSegregationCodes = getSegregationCount( component );
        if (tierCount >= nSegregationCodes)
            return;

        indentation += 2;
        int stringLength = indentation + component.displayName().length();
        String debugMessage = String.format("%" + stringLength + "s", "TierCount = " + tierCount + "\n");
        debugMessage += String.format("%" + stringLength + "s", "Number of Segregation Codes = " + nSegregationCodes + "\n");
        listingWindow.writeFullline( debugMessage );

        NXObject[] objects = { component };

        String message = "Component " + component.displayName();
        message += " has only " + tierCount + " tiers";
        message += " but has " + nSegregationCodes + " segregation codes.\n";
        message += "The number of segregation codes cannot exceed the number of tiers.";

        theSession.routingCustomManager().createViolationForReason( "Segregation Code", DesignRuleReason.CABLEWAY_VALIDATION,
                                                                    "Too many segregation codes.", message, objects );
    }

    //------------------------------------------------------------------------------------------
    // Recursively walks down the assembly tree under the given component.
    private void walkDownAssemblyTree
    (
        ListingWindow listingWindow,
        int indentation,
        Component component
    ) throws RemoteException, NXException
    {
        if (component == null)
            return;

        int stringLength = indentation + component.displayName().length();
        String message = String.format("%" + stringLength + "s", component.displayName());
        listingWindow.writeFullline( message );

        // Verify that the segregation attribute array does not have more values than there are tiers.
        // This also works for stock components.
        checkComponentTierCount( listingWindow, indentation, component );

        indentation += 2;
        Component[] children = component.getChildren();
        for (Component child : children)
            walkDownAssemblyTree( listingWindow, indentation, child );
    }

    //---------------------------------------------------------------------------------------------
    // This is the Segregation Codes Design Rule.
    //
    // It creates a design rule violation if the number of segregation codes exceeds the number of tiers.
    public void designRule(DesignRuleReason reason, NXObject[] objects) throws NXException, RemoteException
    {
        if (reason != DesignRuleReason.CABLEWAY_VALIDATION && reason != DesignRuleReason.INTERACTIVE)
            return;

        UI theUI = (UI)SessionFactory.get("UI");

        try
        {
            Component rootComponent = theSession.parts().work().componentAssembly().rootComponent();
            listingWindow.open();

            int indentation = 0;
            walkDownAssemblyTree( listingWindow, indentation, rootComponent );
        }
        catch (NXException ex)
        {
            theSession.logFile().writeLine("NX Design Rule Error: " + ex.getMessage());
        }
        catch (RemoteException ex)
        {
            theSession.logFile().writeLine("Design Rule Remote Error: " + ex.getMessage());
        }
        catch (Exception ex)
        {
            theSession.logFile().writeLine("Design Rule Error: " + ex.getMessage());
        }
    }

    //------------------------------------------------------------------------------------------
    // Tells NX when to unload your application.
    // For Routing callbacks, plugins, and Design Rules, this MUST return AT_TERMINATION.
    public static int getUnloadOption(String arg)
    {
        return Session.LibraryUnloadOption.AT_TERMINATION;
    }
}


