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

    See Routing_Example_Cableway_ImportDataset.hpp for the interface.


==================================================================================================*/
#include "Routing_Example_Cableway_ImportDataset.hpp"

#include <algorithm>
#include <cstdio>
#include <fstream>
#include <sstream>
#include <uf.h>
#include <uf_ugmgr.h>
#include <uf_ugopenint.h>
#include <vector>

#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/MechanicalRouting_RoutingManager.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/PDM_PdmSession.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>

using namespace NXOpen;

#define UF_CALL(X) ( throwError( __FILE__, __LINE__, #X, (X) ) )

using StlNXStringVector = std::vector< NXOpen::NXString >;
using StlBoolVector     = std::vector< bool >;
using StlIntVector      = std::vector< int >;

//--------------------------------------------------------------------------------------------------
// Used with the UF_CALL macro to throw a message describing the error code returned from a UF routine.
static void throwError
(
    const char* file,
    const int   line,
    const char* ufRoutine,
    const int   error
)
{
    if ( error == ERROR_OK )
        return;

    char tempString[133] = "";
    UF_get_fail_message( error, tempString );
    std::string errorMessage( tempString );

    if ( strlen( tempString ) == 0 )
    {
        std::stringstream temp;
        temp << "Unknown error code: " << error;
        errorMessage = temp.str();
    }

    std::stringstream message;
    message << "Error at line " << line << " in " << ufRoutine << " in file " << file << "." << std::endl;
    message << errorMessage;

    NXException nxException = NXException::Create( message.str().c_str() );
    throw nxException;
}

//------------------------------------------------------------------------------------------
// Splits the work part's name into its item and revision.
static void getWorkPartItemAndRevision
(
    std::string& item,
    std::string& revision
)
{
    Session* session  = Session::GetSession();
    Part*    workPart = session->Parts()->Work();

    // In managed mode, the work part name is the item/revision in the form "Zone/A;1".
    std::string workPartName( workPart->Name().GetText() );
    auto delimiterPos = workPartName.find( '/' );
    auto semicolonPos = workPartName.find( ';' );

    item     = workPartName.substr( 0, delimiterPos );
    revision = workPartName.substr( delimiterPos+1, workPartName.length() - semicolonPos-1 );
}

//------------------------------------------------------------------------------------------
// Exports any cableway and device data from the work part and below to the XML file.
static void exportCablewaysData
(
    const std::string& cablewayXmlFile
)
{
    Session* session = Session::GetSession();
    Part*    workPart = session->Parts()->Work();

    MechanicalRouting::RoutingManager* routingMgr = MechanicalRouting::RoutingManager::GetRoutingManager( session );
    
    int maxSearchLevels = 0; // Zero means search all levels of the assembly under the work part.

    routingMgr->ExportCablewayToFile( workPart, cablewayXmlFile, "none", MechanicalRouting::RoutingManager::DataTypeAll, maxSearchLevels );
}

//------------------------------------------------------------------------------------------
// Imports the XML file into a dataset under the work part's item revision.
static void importIntoDataset
(
    const std::string& cablewayXmlFile
)
{
    std::string item;
    std::string revision;
    getWorkPartItemAndRevision( item, revision );

    std::string cablewayXmlFilePath( cablewayXmlFile );
    auto lastDelimiter = cablewayXmlFilePath.find_last_of( '\\' );
    cablewayXmlFilePath.erase( lastDelimiter );

    // TODO: Fill these values in to match your Teamcenter configuration.
    StlNXStringVector itemIDs                   = { item };
    StlNXStringVector itemRevisions             = { revision };
    StlNXStringVector datesetNames              = { "CapitalRouterData" };
    StlNXStringVector datesetTypeNames          = { "NXRouting" };
    StlNXStringVector datesetRelationTypeNames  = { "IMAN_manifestation" };
    StlNXStringVector datasetToolNames          = { "" };
    StlBoolVector     fileTypes                 = { true };
    StlNXStringVector namedReferenceNames       = { "NXRout" };
    StlNXStringVector fileNames                 = { cablewayXmlFilePath };
    StlNXStringVector directoryNames            = { cablewayXmlFile };

    Session*             session        = Session::GetSession();
    PDM::FileManagement* fileManagement = session->PdmSession()->NewFileManagement();

    StlIntVector results = fileManagement->ImportFilesAndCreateDatasets( itemIDs, itemRevisions, datesetNames,
                                                                         datesetTypeNames, datesetRelationTypeNames,
                                                                         datasetToolNames, fileTypes, namedReferenceNames,
                                                                         fileNames, directoryNames );
    if ( results[0] != 0 )
        throw ( NXException::Create( results[0] ) );
}

//--------------------------------------------------------------------------------------------------
// Called from File->Execute->NX Open. Useful for testing.
extern "C" DllExport void ufusr
(
    char* /*param*/,
    int*  retcod,
    int   /*param_len*/
)
{
    *retcod = 0;

    std::string cablewayXmlFile;

    try
    {
        Session* session = Session::GetSession();
        
        char exportFolder[MAX_FSPEC_BUFSIZE] = "";
        UF_CALL( UF_initialize() );
        UF_CALL( UF_UGMGR_ask_export_directory( session->Parts()->Work()->Tag(), exportFolder ) );

        std::string item;
        std::string revision;
        getWorkPartItemAndRevision( item, revision );
        std::replace( item.begin(), item.end(), ' ', '_' );

        cablewayXmlFile  = exportFolder;
        cablewayXmlFile += "\\" + item + "_" + revision + "_cablewayData.xml";

        // Write out the cableway data to the temporary XML file.
        exportCablewaysData( cablewayXmlFile );

        // Then import that XML file into Teamcenter under the work part.
        importIntoDataset( cablewayXmlFile );
    }
    catch ( const NXException& ex )
    {
        UI::GetUI()->NXMessageBox()->Show( "NXException", NXMessageBox::DialogTypeError, ex.Message() );
    }
    catch ( const std::exception& ex )
    {
        UI::GetUI()->NXMessageBox()->Show( "Exception", NXMessageBox::DialogTypeError, ex.what() );
    }
    catch ( ... )
    {
        UI::GetUI()->NXMessageBox()->Show( "Exception", NXMessageBox::DialogTypeError, "Unknown Exception." );
    }

    // Finally, delete the temporary XML file.
    std::ifstream fileStream( cablewayXmlFile.c_str() );
    if ( fileStream.good() )
        remove( cablewayXmlFile.c_str() );

    UF_terminate();
}

//--------------------------------------------------------------------------------------------------
extern int ufusr_ask_unload()
{
    // Unloads the image immediately after execution within NX
    return UF_UNLOAD_IMMEDIATELY;
}
