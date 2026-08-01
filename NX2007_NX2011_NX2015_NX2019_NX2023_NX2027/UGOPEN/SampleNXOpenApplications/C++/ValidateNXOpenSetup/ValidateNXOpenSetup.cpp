/*===================================================================================================
  
          Copyright (c) 2018 Siemens Product Lifecycle Management Software Inc. 
                              All Rights Reserved.
  
=====================================================================================================

  
      Code Description:
  
      A simple NX Open C++ application program that prints the full version number of installed  
      Siemens NX software in the system log file and the listing window. If the messages are 
      successfully printed, then NX Open software automation setup is validated.   
=====================================================================================================
  
      Note:  
     
      NX Development provides programming examples for illustration only.
      NX Development assumes you are familiar with the programming language
      demonstrated in these examples, and the tools used to create and debug NX/Open
      programs. GTAC support professionals can help explain the functionality of
      a particular procedure, but neither GTAC nor NX Development will modify
      these examples to provide added functionality or construction procedures.
=====================================================================================================
*/


// Mandatory UF Includes
#include <uf.h>
#include <uf_object_types.h>


// Internal+External Includes
#include <NXOpen/Annotations.hxx>
#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/BodyCollection.hxx>
#include <NXOpen/Face.hxx>
#include <NXOpen/Line.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>

// Std C++ Includes
#include <iostream>
#include <sstream>

using namespace NXOpen;
using std::string;
using std::exception;
using std::stringstream;
using std::endl;
using std::cout;
using std::cerr;

//------------------------------------------------------------------------------
// Open C error handling
//------------------------------------------------------------------------------
#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))
int report_error( char *file, int line, char *call, int code)
{
    if (code) 
    {

        stringstream errmsg;
        errmsg << "Error " << code << " in " << file << " at line " << line << endl;
        errmsg << call << endl;
        cerr << errmsg.str();
        throw NXOpen::NXException::Create(code);
    }
    return(code);
}

//------------------------------------------------------------------------------
// NXOpen c++ test class 
//------------------------------------------------------------------------------
class MyClass
{
    // class members
public:
    static Session *theSession;

    MyClass();
    ~MyClass();

    void do_it();
    void print(const NXString &);
    void print(const string &);
    void print(const char*);

private:
    BasePart *workPart, *displayPart;
};

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(MyClass::theSession) = NULL;

//------------------------------------------------------------------------------
// Constructor 
//------------------------------------------------------------------------------
MyClass::MyClass()
{
    // Initialize the Open C API environment */
    UF_CALL( UF_initialize() );

    // Initialize the NX Open C++ API environment
    MyClass::theSession = NXOpen::Session::GetSession();

    workPart = theSession->Parts()->BaseWork();
    displayPart = theSession->Parts()->BaseDisplay();
    
}

//------------------------------------------------------------------------------
// Destructor
//------------------------------------------------------------------------------
MyClass::~MyClass()
{
    UF_CALL( UF_terminate() );
}

//------------------------------------------------------------------------------
// Print string to listing window or stdout
//------------------------------------------------------------------------------
void MyClass::print(const NXString &msg)
{
    cout << msg.GetText() << endl;
}
void MyClass::print(const string &msg)
{
    cout << msg << endl;
}
void MyClass::print(const char * msg)
{
    cout << msg << endl;
}




//------------------------------------------------------------------------------
// Do something
//------------------------------------------------------------------------------
void MyClass::do_it()
{

    // TODO: add your code here
    
    // Get the listing window for this session
    NXOpen::ListingWindow *lw = theSession->ListingWindow( );
    
    // Open the listing window
    lw->Open( );
    
    // Get the system log file for this session    
    NXOpen::LogFile *logFile = theSession->LogFile( );
    
    // Get the name of the system log file
    NXOpen::NXString logFileName = logFile->FileName( );
    
    //Creating a string which is a merged string of string + NXString
    char *message = ( char * )malloc( 1 + strlen( "Log File Name: " ) + strlen( logFileName.GetText( ) ) + strlen( " created." ) );
    strcpy( message, "Log File Name: " );
    strcat( message, logFileName.GetText( ) );    
    strcat( message, " created." );
    
    // Write a line to the listing window
    lw->WriteFullline( message );
    
    // Get the full version name of the installed Siemens NX
    NXOpen::NXString NXFullVersion = theSession->GetEnvironmentVariableValue( "NX_FULL_VERSION" );
    
    // Convert NXString to string
    string sNXFullVersion = NXFullVersion.GetText( );
    
    if ( !sNXFullVersion.empty( ) )
    {
        //Creating a string which is a merged string of string + NXString
        char *message = ( char * )malloc( 1 + strlen( "NX Open software automation setup is validated for release: " ) + strlen( NXFullVersion.GetText( ) ) + strlen( "." ) );
        strcpy( message, "NX Open software automation setup is validated for release: ");
        strcat( message, NXFullVersion.GetText( ) );    
        strcat( message, "." );
        
        
        // Write a string to the system log file
        logFile->WriteLine( message );
        
        // Write a line to the listing window
        lw->WriteFullline( message );
    }
    else
    {
        // Write a string to the system log file
        logFile->WriteLine( "Siemens NX installation not verified." );
        
        // Write a line to the listing window
        lw->WriteFullline( "Siemens NX installation not verified." );        
    }

    // Close the stream to the listing window
    lw->Close( );
    
}

//------------------------------------------------------------------------------
// Entry point for unmanaged external NXOpen C/C++ programs
//------------------------------------------------------------------------------
int main(int argc, char* argv[])
{
    try
    {
        // Create NXOpen C++ class instance
        MyClass *theMyClass;
        theMyClass = new MyClass();
        theMyClass->do_it();
        delete theMyClass;
    }
    catch (const NXException& e1)
    {
        cerr << "NXException: " <<  e1.ErrorCode() << endl;
        cerr << e1.Message() << endl;
    }
    catch (const exception& e2)
    {
        cerr << "Exception: " <<  e2.what() << endl;
    }
    catch (...)
    {
        cerr << "Unknown Exception: " << endl;
    }
}



