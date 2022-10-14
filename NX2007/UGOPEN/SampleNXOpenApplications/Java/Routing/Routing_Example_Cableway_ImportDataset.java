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

    An example program that exports Cableway data from the work part and imports it into a Teamcenter dataset.


==================================================================================================*/
import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.rmi.RemoteException;

import nxopen.*;
import nxopen.mechanicalrouting.RoutingManager;
import nxopen.mechanicalrouting.RoutingManagerFactory;
import nxopen.pdm.FileManagement;
import nxopen.pdm.PdmSession;
import nxopen.uf.*;

public class Routing_Example_Cableway_ImportDataset
{
    //----------------------------------------------------------------------------------------------
    // Called from File->Execute->NX Open.
    public static void main(String[] argv) throws Exception
    {
        Session session = (Session)SessionFactory.get("Session");
        String cablewayXmlFile = null;

        try
        {
            UFSession ufSession = (UFSession)SessionFactory.get( "UFSession" );

            // Use the Teamcenter export directory to temporarily store the XML file.
            String exportFolder = ufSession.ugmgr().askExportDirectory( session.parts().work().tag() );

            String[] names = getWorkPartItemAndRevision();
            String item     = names[0];
            String revision = names[1];
            item = item.replace( ' ', '_' );
            
            cablewayXmlFile = exportFolder + "\\" + item + "_" + revision + "_cablewayData.xml";

            // Write out the cableway data to the temporary XML file.
            exportCablewaysData( cablewayXmlFile );

            // Then import that XML file into Teamcenter under the work part.
            importIntoDataset( cablewayXmlFile );

        }
        catch ( NXException ex)
        {
            session.logFile().writeLine( "\n\n\n***Error in Cableway Plugins constructor: " + ex.getMessage() );
        }
        catch (RemoteException ex)
        {
            session.logFile().writeLine( "\n\n\n***RemoteException in Cableway Plugins constructor: " + ex.getMessage() );
        }

        // Finally, delete the temporary XML file.
        File f = new File( cablewayXmlFile );
        f.delete();
    }

    //------------------------------------------------------------------------------------------
    // Exports any cableway and device data from the work part and below to the XML file.
    private static void exportCablewaysData
    (
        String cablewayXmlFile
    ) throws RemoteException, NXException
    {
        Session        session         = (Session)SessionFactory.get("Session");
        Part           workPart        = session.parts().work();
        RoutingManager routingMgr      = RoutingManagerFactory.GetRoutingManager( session );
        int            maxSearchLevels = 0; // Zero means search all levels of the assembly under the work part.

        routingMgr.exportCablewayToFile( workPart, cablewayXmlFile, "none", RoutingManager.DataType.ALL, maxSearchLevels );
    }

    //------------------------------------------------------------------------------------------
    // Imports the XML file into a dataset under the work part's item revision.
    private static void importIntoDataset
    (
        String cablewayXmlFile
    ) throws RemoteException, NXException
    {
        String[] names = getWorkPartItemAndRevision();
        String item     = names[0];
        String revision = names[1];
        
        int lastDelimiter = cablewayXmlFile.lastIndexOf( "\\" );
        String cablewayXmlFilePath = cablewayXmlFile.substring( 0, lastDelimiter );
        echo( "Cableway XML file path" );
        echo( cablewayXmlFilePath );

        // TODO: Fill these values in to match your Teamcenter configuration.
        String[]  itemIDs                  = { item  };
        String[]  itemRevisions            = { revision };
        String[]  datesetNames             = { "CapitalRouterData"  };
        String[]  datesetTypeNames         = { "NXRouting"          };
        String[]  datesetRelationTypeNames = { "IMAN_manifestation" };
        String[]  datasetToolNames         = { "" };
        boolean[] fileTypes                = { true };
        String[]  namedReferenceNames      = { "NXRout" };
        String[]  fileNames                = { cablewayXmlFilePath };
        String[]  directoryNames           = { cablewayXmlFile };

        PdmSession pdmSession = (PdmSession)SessionFactory.get( "PdmSession" );
        FileManagement fileManagement = pdmSession.newFileManagement();

        int[] results = fileManagement.importFilesAndCreateDatasets( itemIDs, itemRevisions, datesetNames,
                                                                     datesetTypeNames, datesetRelationTypeNames,
                                                                     datasetToolNames, fileTypes, namedReferenceNames,
                                                                     fileNames, directoryNames );
        if ( results[0] != 0 )
            throw ( NXException.create( results[0] ) );
    }
    
    //------------------------------------------------------------------------------------------
    // Splits the work part's name into its item and revision.
    private static String[] getWorkPartItemAndRevision()throws RemoteException, NXException
    {
        Session session  = (Session)SessionFactory.get("Session");
        Part    workPart = session.parts().work();

        // In managed mode, the work part name is the item/revision in the form "Zone/A;1".
        String[] nameParts     = workPart.name().split( "/" );
        String[] revisionParts = nameParts[1].split( ";" );

        String[] names = { nameParts[0], revisionParts[0] };
        return names;
    }
    
    //---------------------------------------------------------------------------------------------
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

    //---------------------------------------------------------------------------------------------
    public static int getUnloadOption(String arg)
    {
        // Unloads the image immediately after execution within NX
        return Session.LibraryUnloadOption.IMMEDIATELY;
    }
}
