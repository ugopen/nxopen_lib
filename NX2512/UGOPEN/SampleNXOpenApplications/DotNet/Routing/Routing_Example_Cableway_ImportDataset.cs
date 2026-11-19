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
using System;
using System.IO;
using NXOpen;
using NXOpen.PDM;
using NXOpen.MechanicalRouting;
using NXOpen.UF;

namespace MechanicalRouting
{
    public class ImportDataSet
    {
        //------------------------------------------------------------------------------------------
        public static int Main( string[] args )
        {
            string cablewayXmlFile = null;

            try
            {
                Session   session   = Session.GetSession();
                UFSession ufSession = UFSession.GetUFSession();

                // Use the Teamcenter export directory to temporarily store the XML file.
                string exportFolder;
                ufSession.Ugmgr.AskExportDirectory( session.Parts.BaseWork.Tag, out exportFolder );

                string item;
                string revision;
                getWorkPartItemAndRevision( out item, out revision );
                item = item.Replace( ' ', '_' );

                cablewayXmlFile = exportFolder + "\\" + item + "_" + revision + "_cablewayData.xml";

                // Write out the cableway data to the temporary XML file.
                exportCablewaysData( cablewayXmlFile );

                // Then import that XML file into Teamcenter under the work part.
                importIntoDataset( cablewayXmlFile );
            }
            catch ( NXException ex )
            {
                UI.GetUI().NXMessageBox.Show( "Error", NXMessageBox.DialogType.Error, ex.Message );
            }
            catch ( Exception ex )
            {
                UI.GetUI().NXMessageBox.Show( "Error", NXMessageBox.DialogType.Error, ex.Message );
            }

            // Finally, delete the temporary XML file.
            if ( File.Exists( cablewayXmlFile ) )
            {
                File.Delete( cablewayXmlFile );
            }

            return 0;
        }

        //------------------------------------------------------------------------------------------
        // Exports any cableway and device data from the work part and below to the XML file.
        private static void exportCablewaysData
        (
            string cablewayXmlFile
        )
        {
            Session        session         = Session.GetSession();
            Part           workPart        = session.Parts.Work;
            RoutingManager routingMgr      = RoutingManager.GetRoutingManager( session );
            int            maxSearchLevels = 0; // Zero means search all levels of the assembly under the work part.

            routingMgr.ExportCablewayToFile( workPart, cablewayXmlFile, "none", RoutingManager.DataType.All, maxSearchLevels );
        }

        //------------------------------------------------------------------------------------------
        // Imports the XML file into a dataset under the work part's item revision.
        private static void importIntoDataset
        (
            string cablewayXmlFile
        )
        {
            string item;
            string revision;
            getWorkPartItemAndRevision( out item, out revision );

            // TODO: Fill these values in to match your Teamcenter configuration.
            string[] itemIDs                  = { item  };
            string[] itemRevisions            = { revision };
            string[] datesetNames             = { "CapitalRouterData"  };
            string[] datesetTypeNames         = { "NXRouting"          };
            string[] datesetRelationTypeNames = { "IMAN_manifestation" };
            string[] datasetToolNames         = { "" };
            bool[]   fileTypes                = { true };
            string[] namedReferenceNames      = { "NXRout" };
            string[] fileNames                = { Path.GetFileName( cablewayXmlFile ) };
            string[] directoryNames           = { cablewayXmlFile };

            Session        session        = Session.GetSession();
            FileManagement fileManagement = session.PdmSession.NewFileManagement();

            int[] results = fileManagement.ImportFilesAndCreateDatasets( itemIDs, itemRevisions, datesetNames,
                                                                         datesetTypeNames, datesetRelationTypeNames,
                                                                         datasetToolNames, fileTypes, namedReferenceNames,
                                                                         fileNames, directoryNames );
            if ( results[0] != 0 )
                throw ( NXException.Create( results[0] ) );
        }

        //------------------------------------------------------------------------------------------
        // Splits the work part's name into its item and revision.
        private static void getWorkPartItemAndRevision
        (
            out string item,
            out string revision
        )
        {
            Session  session   = Session.GetSession();
            Part     workPart  = session.Parts.Work;

            // In managed mode, the work part name is the item/revision in the form "Zone/A;1".
            string[] nameParts     = workPart.Name.Split( '/' );
            string[] revisionParts = nameParts[1].Split( ';' );

            item     = nameParts[0];
            revision = revisionParts[0];
        }

        //------------------------------------------------------------------------------------------
        public static int GetUnloadOption( string arg )
        {
            // Unloads the image immediately after execution within NX
            return System.Convert.ToInt32( Session.LibraryUnloadOption.Immediately );
        }
    }
}
