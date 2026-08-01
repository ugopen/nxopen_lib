/*=============================================================================
 Copyright (c) 2004 UGS Corp.
 All rights reserved
 ===============================================================================
 File2Points.cpp
 
 Description: Contains Unigraphics entry points for the application.
 
  
 =============================================================================*/

#ifdef WIN32
#define USE_MFC
#endif

#ifdef USE_MFC
#include <afxdlgs.h>
#include <afx.h>
#endif

#include <NXOpen/Session.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Point.hxx>
#include <NXOpen/PointCollection.hxx>

#include <fstream>
#ifdef USE_MFC
#include <tchar.h>
#endif
using namespace NXOpen;
using namespace std;

/* Include files */
#include <uf.h>
#include <uf_ui.h>
#include <uf_exit.h>
#include <uf.h>
#include <uf_exit.h>
#include <uf_ui.h>

#   include <sstream>
#   include <iostream>
using std::ostringstream;
using std::endl;    
using std::ends;
using std::cerr;

static void PrintErrorMessage( int errorCode );
static void PrintErrorMessage( const char* msg );

static int create_filebox(char* prompt, char* filename )
{
    // We could have used UF_UI_create_filebox on both Windows and Unix.
    // The ONLY reason that we use MFC instead of UF_UI_create_filebox on Windows
    // is for the purpose of demonstrating how MFC can be used inside an NX Open application.
#ifdef USE_MFC
    
    const TCHAR* Filters = _T("txt files (*.txt)|*.txt|All files (*.*)|*.*||");
    
    // Create an Open dialog; the default file name extension is ".my".
    CFileDialog fileDialog (TRUE, NULL, NULL, OFN_FILEMUSTEXIST | OFN_HIDEREADONLY, Filters);
    
    UF_UI_set_prompt( prompt );
    INT_PTR response = fileDialog.DoModal();
    
    if ( response == IDOK)
    {
        TCHAR* tmpFileName = (TCHAR*)(fileDialog.GetPathName().GetBuffer(fileDialog.GetPathName().GetLength()));
        
        USES_CONVERSION;
        strcpy_s(filename, fileDialog.GetPathName().GetLength()+1,T2A(tmpFileName));
    }
    return response == IDOK ? UF_UI_OK : UF_UI_CANCEL;
#else    
    int response;
    char filter[ MAX_FSPEC_BUFSIZE ] = "*.txt";
    UF_UI_create_filebox( prompt,
                          "Select point data file",
                         filter, NULL,
                         filename, &response );
    return response;
#endif
}

/*****************************************************************************
 **  Activation Methods
 *****************************************************************************/
/*  Explicit Activation
 **      This entry point is used to activate the application explicitly, as in
 **      "File->Execute UG/Open->User Function..." */
extern DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    /* Initialize the API environment */
    int errorCode = UF_initialize();
    
    Session *theSession = Session::GetSession();
    
    Session::UndoMarkId markId1 = theSession->SetUndoMark(Session::MarkVisibilityVisible, "Create Points");      
    
    Part *workPart = theSession->Parts()->Work();
    if ( workPart == NULL )
        workPart = theSession->Parts()->NewDisplay("File2Points", Part::UnitsMillimeters);
    
    char fileName[ MAX_FSPEC_BUFSIZE ];
    char prompt[] = "Select file that contains the point coordinate data";

    if ( create_filebox( prompt, fileName ) == UF_UI_OK )
    { 
        ifstream file1;
        
        file1.open(fileName);
        
        if ( !file1.is_open() )
            PrintErrorMessage( "Could not open file\n" );
        else
        {
            double x,y,z;
            char c;
            while(!file1.eof())
            {
                file1 >> x >> c >> y >> c >> z;
                if(!file1)
                {
                    PrintErrorMessage("File format error:\n   The input file does not have the expected format\n");
                    break;
                }                
                NXOpen::Point3d point3d11(x,y,z);
                Point *point1;
                point1 = workPart->Points()->CreatePoint(point3d11);
                // The point is invisible when initially created
                point1->SetVisibility(NXOpen::SmartObject::VisibilityOptionVisible);
                
                // Check for end of file
                file1 >> c;
                if ( !file1.eof() )
                    file1.unget();
            }
            file1.close();
            file1.clear();
        }
        
        /* To save work part using NXOpen automation APIs */
        /*NXOpen::PartSaveStatus *partSaveStatus;
         part1->Save(NXOpen::Part::SaveComponentsTrue, NXOpen::Part::CloseAfterSaveTrue, &partSaveStatus);*/
        
        int nErrs = theSession->UpdateManager()->DoUpdate(markId1);
        if (nErrs > 0)
            PrintErrorMessage( "Error occured during update.\n" );
    }
    
    /* Terminate the API environment */
    errorCode = UF_terminate();
    
    /* Print out any error messages */
    PrintErrorMessage( errorCode );
}

/*****************************************************************************
 **  Utilities
 *****************************************************************************/

/* Unload Handler
 **     This function specifies when to unload your application from Unigraphics.
 **     If your application registers a callback (from a MenuScript item or a
 **     User Defined Object for example), this function MUST return
 **     "UF_UNLOAD_UG_TERMINATE". */
extern int ufusr_ask_unload( void )
{
    return(UF_UNLOAD_IMMEDIATELY);
}
/* PrintErrorMessage
 **
 **     Prints error messages to standard error and the Unigraphics status
 **     line. 
 */
static void PrintErrorMessage( int errorCode )
{
    if ( 0 != errorCode )
    {
        /* Retrieve the associated error message  */
        char message[133];
        UF_get_fail_message( errorCode, message );
        
        /* Print out the message  */
        UF_UI_set_status( message );
        /* Construct a buffer to hold the text. */ 
        ostringstream error_message;
        
        /* Initialize the buffer with the required text.  */
        error_message << "Error:" << endl
        << message
        << endl << endl << ends;
        
        /* Write the message to standard error 
         errtxt necessary, as the buffer cannot be passed
         directly into PrintErrorMessage */
        std::string errtxt = error_message.str();
        PrintErrorMessage(errtxt.c_str());
    }
}

static void PrintErrorMessage( const char* msg )
{
#ifdef WIN32
    static bool consoleInitialized = false;
    if ( !consoleInitialized )
    {
        AllocConsole();
        FILE *stream;
        freopen_s(&stream,"conout$", "w", stdout);
        freopen_s(&stream,"conout$", "w", stderr);
        consoleInitialized = true;
    }
#endif
    cerr << msg;
}

