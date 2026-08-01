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


    This file implements a Routing Plugin that implements Tyco's Entry Size new bundling algorithm
    for routing wires in Routing Electrical.  The algorithm is taken from a PDF titled
    AdapterEntrySizeSelection.pdf on the Tyco Electronics' Raychem web site.

    ALGORITHM:

    For 61 or fewer wires of all the same size, use the Tyco table data to look up a bundle factor (F).
    The bundle diameter is computed as D = F * d, where d is the wire diameter.

    Otherwise use the formula,

        D = 1.2 * SQRT( SUM( d[i] * d[i] )

    where d[i] is the diameter for each wire in the bundle.


==================================================================================================*/
import java.rmi.RemoteException;
import java.lang.Math;

import nxopen.Arc;
import nxopen.Curve;
import nxopen.ListingWindow;
import nxopen.LogFile;
import nxopen.NXException;
import nxopen.Session;
import nxopen.SessionFactory;
import nxopen.routing.CrossSection;
import nxopen.routing.CustomManager;
import nxopen.routing.StockData;

//------------------------------------------------------------------------------------------------
public class Routing_Example_Bundle_Plugin 
    implements CustomManager.BundlePlugin
{
    static Routing_Example_Bundle_Plugin thePlugins = null;
    static Session theSession = null;
    static ListingWindow listingWindow = null;

    //------------------------------------------------------------------------------------------
    // Called when NX starts.
    // Creates a new instance of this Plugin class.
    public static void startup( String [] args ) throws NXException, java.rmi.RemoteException
    {
        if (theSession == null)
            theSession = (Session)SessionFactory.get("Session");

        if (listingWindow == null)
            listingWindow = theSession.listingWindow();

        thePlugins = new Routing_Example_Bundle_Plugin();
    }

    //------------------------------------------------------------------------------------------
    // The constructor for this class.
    // Registers the Plugin.
    public Routing_Example_Bundle_Plugin() throws RemoteException, NXException
    {        
        try
        {
            CustomManager customManager = theSession.routeCustomManager();
            
            customManager.setBundlePlugin(this);
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
    public double bundlePlugin( StockData[] stockDatas ) throws NXException, RemoteException 
    {
        double tolerance = 0.000001;

        // This table is used if all the wires are the same diameter.
        double[] bundleFactorTable = new double[]
        {
            0.00, 1.00, 1.64, 2.00, 2.41,
            2.70, 3.00, 3.00, 3.60, 4.00,
            4.00, 4.00, 4.00, 4.41, 4.41,
            4.70, 4.70, 5.00, 5.00, 5.00,
            5.31, 5.31, 5.61, 5.61, 5.61,
            6.00, 6.00, 6.00, 6.41, 6.41,
            6.41, 6.70, 6.70, 6.70, 7.00,
            7.00, 7.00, 7.00, 7.31, 7.31,
            7.31, 7.61, 7.61, 7.61, 7.61,
            8.00, 8.00, 8.00, 8.00, 8.41,
            8.41, 8.41, 8.41, 8.70, 8.70,
            8.70, 8.70, 9.00, 9.00, 9.00,
            9.00, 9.00
        };

        int sizeOfBundleFactorTable = bundleFactorTable.length;

        double sumOfDiameters = 0.0;
        double sumOfSquares = 0.0;
        double commonDiameter = -1.0;
        boolean equalDiameters = true;

        for ( int iStockDatas = 0; iStockDatas < stockDatas.length; ++iStockDatas )
        {
            CrossSection[] wireCrossSections = stockDatas[iStockDatas].getCrossSections();
            
            for ( int iWireCrossSections = 0; iWireCrossSections < wireCrossSections.length; ++iWireCrossSections )
            {
                Curve[] wireCrossSectionCurves = wireCrossSections[iWireCrossSections].getCrossCurves();
                if (wireCrossSectionCurves.length == 0)
                    continue;

                if ( !(wireCrossSectionCurves[0] instanceof Arc) )
                    continue;

                // Assume all the cross sections of this stock have the same diameter.
                Arc crossSectionArc = (Arc)wireCrossSectionCurves[0];

                double arcDiameter = crossSectionArc.radius() * 2.0;

                sumOfDiameters += arcDiameter;
                sumOfSquares   += arcDiameter * arcDiameter;

                if (commonDiameter < 0.0)
                {
                    commonDiameter = arcDiameter;
                }
                else if (equalDiameters && Math.abs(commonDiameter - arcDiameter) > tolerance)
                {
                    equalDiameters = false;
                }
            }
        }

        double diameter = 0.0;
        if (equalDiameters && stockDatas.length < sizeOfBundleFactorTable)
        {
            // If all the wires are the same size, use the Tyco table.
            diameter = bundleFactorTable[stockDatas.length] * commonDiameter;
        }
        else
        {
            // Otherwise use the the formula.
            diameter = 1.2 * Math.sqrt(sumOfSquares);
        }

        return diameter;
    }

    //------------------------------------------------------------------------------------------
    // Tells NX when to unload your application.
    // For Routing callbacks, plugins, and Design Rules, this MUST return AtTermination.
    public static int getUnloadOption(String arg)
    {
        return Session.LibraryUnloadOption.AT_TERMINATION;
    }
}
