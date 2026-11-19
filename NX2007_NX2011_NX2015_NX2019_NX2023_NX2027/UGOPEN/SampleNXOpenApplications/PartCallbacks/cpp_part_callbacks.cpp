//----------------------------------------------------------------------------
//                  Copyright (c) 2007 UGS Corp.
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//
// cpp_part_callbacks.cpp
//
// Description:
//     This simple demo registers part callbacks for every available reason
//     via the C++ language.
//
//     This file must be compiled with cpp_part_callbacks.h
//
//     After compiling and linking this demo program, the output library needs
//     to be placed in a folder called startup (for example c:\user_dir\startup).
//     Also the UGII_USER_DIR enviornment variable needs to point to the startup
//     directory's parent folder (for example: UGII_USER_DIR=c:\user_dir).
//     Once you have the startup directory and user dir environment variable
//     set up, start NX.  The part callbacks will be registered at startup.
//     Now anytime you create new, open, save, save as, close, modify, rename,
//     or change the workpart your callbacks will be executed.
//
//     To demo all of the available part callbacks at runtime - compile and link
//     execute_all_part_callbacks.c.
//     Then start NX and go to File->Execute->NX Open and select your compiled
//     execute_all_callbacks program.
//
//----------------------------------------------------------------------------


#include <NXOpen/UI.hxx>
#include <NXOpen/Selection.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/ListingWindow.hxx>
#include "cpp_part_callbacks.h"
#include <stdio.h>
#include <uf.h>
#undef CreateDialog

//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(CppPartCallbacks::theSession) = NULL;
int CppPartCallbacks::registered = 0;
int CppPartCallbacks::idPartCreated1 = 0;
int CppPartCallbacks::idPartOpened1 = 0;
int CppPartCallbacks::idPartSaved1 = 0;
int CppPartCallbacks::idPartSavedAs1 = 0;
int CppPartCallbacks::idPartClosed1 = 0;
int CppPartCallbacks::idPartModified1 = 0;
int CppPartCallbacks::idPartRenamed1 = 0;
int CppPartCallbacks::idWorkPartChanged1 = 0;
ListingWindow* CppPartCallbacks::lw = NULL;

CppPartCallbacks *theCppPartCallbacks;

//------------------------------------------------------------------------------
// Constructor for CppPartCallbacks class
//------------------------------------------------------------------------------
CppPartCallbacks::CppPartCallbacks()
{
    try
    {
        // Initialize the NX Open C++ API environment
        theSession = Session::GetSession();

        // Initialize the Open C API environment
        int errorCode = UF_initialize();
        if(0 != errorCode)
            throw NXOpen::NXException::Create(errorCode);

        if( lw == NULL )
        {
            lw = theSession->ListingWindow();
        }
        InitializeCallbacks();
    }
    catch (const NXOpen::NXException& ex)
    {
        std::cerr << "Caught exception" << ex.Message() << std::endl;
    }
    return;
}

//------------------------------------------------------------------------------
// Initialize Callbacks - registers the part callbacks with NX
//------------------------------------------------------------------------------
void CppPartCallbacks::InitializeCallbacks()
{
    try
    {
        if( registered == 0 )
        {
            idPartCreated1 = theSession->Parts()->AddPartCreatedHandler(make_callback(this, &CppPartCallbacks::PartCreated1));
            idPartOpened1 = theSession->Parts()->AddPartOpenedHandler(make_callback(this, &CppPartCallbacks::PartOpened1));
            idPartSaved1 = theSession->Parts()->AddPartSavedHandler(make_callback(this, &CppPartCallbacks::PartSaved1));
            idPartSavedAs1 = theSession->Parts()->AddPartSavedAsHandler(make_callback(this, &CppPartCallbacks::PartSavedAs1));
            idPartClosed1 = theSession->Parts()->AddPartClosedHandler(make_callback(this, &CppPartCallbacks::PartClosed1));
            idPartModified1 = theSession->Parts()->AddPartModifiedHandler(make_callback(this, &CppPartCallbacks::PartModified1));
            idPartRenamed1 = theSession->Parts()->AddPartRenamedHandler(make_callback(this, &CppPartCallbacks::PartRenamed1));
            idWorkPartChanged1 = theSession->Parts()->AddWorkPartChangedHandler(make_callback(this, &CppPartCallbacks::WorkPartChanged1));
            registered = 1;

        }
    }
    catch (const NXOpen::NXException& ex)
    {
        std::cerr << "Caught exception" << ex.Message() << std::endl;
    }
    return;
}

// Called when NX starts up
extern "C" DllExport void ufsta(char *param, int *retcod, int param_len)
{
    theCppPartCallbacks = new CppPartCallbacks();

    return;
} // ufsta ends

// Called manually from File->Execute->NX Open
extern "C" DllExport void ufusr(char *param, int *retcod, int param_len)
{
    theCppPartCallbacks = new CppPartCallbacks();
} // User exit ends




//----------------------------------------------------
// Unload Handler
//     This function specifies when to unload your application from Unigraphics.
//     If your application registers a callback (from a MenuScript item or a
//     User Defined Object for example), this function MUST return
//     "AtTermination".
//
//  Available Options:
//  Immediately : unload the library as soon as the automation program has completed
//  Explicitly  : unload the library from the "Unload Shared Image" dialog
//  AtTermination : unload the library when the NX session terminates
//----------------------------------------------------
extern "C" DllExport int ufusr_ask_unload()
{
    return (int)Session::LibraryUnloadOptionAtTermination;
}

//------------------------------------------------------------------------------
// Method: ufusr_cleanup()
// You have the option of coding the cleanup routine to perform any housekeeping
// chores that may need to be performed. If you code the cleanup routine, it is
// automatically called by NX.
//------------------------------------------------------------------------------
extern "C" DllExport void ufusr_cleanup(void)
{
    // Add your cleanup code here
    return;
}


//------------------------------------------------------------------------------
//------------------------- Callback Functions ---------------------------------
//------------------------------------------------------------------------------

//-----------------------------------
// Called when a new part is created
// Prints the name of the created part
// to the listing window
//-----------------------------------
void CppPartCallbacks::PartCreated1( BasePart* p )
{
    char msg[256];
    lw->Open();
    sprintf( msg, "    CPP created: %s", p->FullPath().GetLocaleText() );
    lw->WriteLine( msg );
}

//-----------------------------------
// Called when a part is opened
// Prints the name of the opened part
// to the listing window
//-----------------------------------
void CppPartCallbacks::PartOpened1( BasePart* p )
{
    char msg[256];
    lw->Open();
    sprintf( msg, "    CPP opened: %s", p->FullPath().GetLocaleText() );
    lw->WriteLine( msg );
}

//-----------------------------------
// Called when a part is saved
// Prints the name of the saved part
// to the listing window
//-----------------------------------
void CppPartCallbacks::PartSaved1( BasePart* p )
{
    char msg[256];
    lw->Open();
    sprintf( msg, "    CPP saved: %s", p->FullPath().GetLocaleText() );
    lw->WriteLine( msg );
}

//-----------------------------------
// Called when a part is saved as
// Prints the name of the saved as part
// to the listing window
//-----------------------------------
void CppPartCallbacks::PartSavedAs1( BasePart* p )
{
    char msg[256];
    lw->Open();
    sprintf( msg, "    CPP saved as: %s", p->FullPath().GetLocaleText() );
    lw->WriteLine( msg );
}

//-----------------------------------
// Called when a part is closed
// Prints the name of the closed part
// to the listing window
//-----------------------------------
void CppPartCallbacks::PartClosed1( BasePart* p )
{
    char msg[256];
    lw->Open();
    sprintf( msg, "    CPP closed: %s", p->FullPath().GetLocaleText() );
    lw->WriteLine( msg );
}

//-----------------------------------
// Called when a part is modified
// (for the first time)
// Prints the name of the modified part
// to the listing window
//-----------------------------------
void CppPartCallbacks::PartModified1( BasePart* p )
{
    char msg[256];
    lw->Open();
    sprintf( msg, "    CPP modified: %s", p->FullPath().GetLocaleText() );
    lw->WriteLine( msg );
}

//-----------------------------------
// Called when a part is renamed
// Prints the name of the renamed part
// to the listing window
//-----------------------------------
void CppPartCallbacks::PartRenamed1( BasePart* p )
{
    char msg[256];
    lw->Open();
    sprintf( msg, "    CPP renamed: %s", p->FullPath().GetLocaleText() );
    lw->WriteLine( msg );
}

//-----------------------------------
// Called when the workpart changes
// Prints the name of old workpart and
// new workpart to the listing window
//-----------------------------------
void CppPartCallbacks::WorkPartChanged1( BasePart* p )
{
    char msg[256];
    lw->Open();
    lw->WriteLine("    CPP work part changed");

    if( p == NULL )
    {
        lw->WriteLine("        Old Work Part: NULL");
    }
    else
    {
        sprintf(msg,"        Old Work Part %s: ", p->FullPath().GetLocaleText());
        lw->WriteLine(msg);
    }

    if( theSession->Parts()->Work() == NULL )
    {
        lw->WriteLine("        New Work Part: NULL");
    }
    else
    {
        sprintf(msg,"        New Work Part %s: ", theSession->Parts()->Work()->FullPath().GetLocaleText());
        lw->WriteLine(msg);
    }
}

