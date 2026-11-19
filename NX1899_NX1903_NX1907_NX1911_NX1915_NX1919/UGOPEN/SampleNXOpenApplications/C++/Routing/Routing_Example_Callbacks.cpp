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

    A C++ class that implements example Routing callbacks.

    See Routing_Example_Callbacks.hpp for the interface.


==================================================================================================*/
#include "Routing_Example_Callbacks.hpp"

#include <sstream>
#include <string>
#include <uf.h>
#include <vector>

#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Routing_Electrical_WireDevice.hxx>
#include <NXOpen/Routing_Port.hxx>
#include <NXOpen/Routing_PortConnection.hxx>
#include <NXOpen/Session.hxx>

using namespace NXOpen;
using namespace NXOpen::Routing;

Callbacks* NXOpen::Routing::theCallbacks;

// Prototype for ufsta
extern "C" DllExport void ufsta( char* param , int* returncode, int param_len );

//--------------------------------------------------------------------------------------------------
// Writes the given string to the Listing Window and the syslog.
//
// \param[in]
//      stringToWrite
//          The string to write.
static void echo
(
    const std::string& stringToWrite
)
{
    Session*       session       = Session::GetSession();
    ListingWindow* listingWindow = session->ListingWindow();

    if ( !listingWindow->IsOpen() )
        listingWindow->Open();

    listingWindow->WriteFullline( stringToWrite.c_str() );

    LogFile* syslog = session->LogFile();
    syslog->WriteLine( stringToWrite.c_str() );
}

//--------------------------------------------------------------------------------------------------
Callbacks::Callbacks()
{
    Session*       session = Session::GetSession();
    CustomManager* customManager = session->RouteCustomManager();

    customManager->AddCallback( CustomManager::CallbackReasonWireRouteAuto,        make_callback(this, &Callbacks::AutorouteCallback) );
    customManager->AddCallback( CustomManager::CallbackReasonWireUnroute,          make_callback(this, &Callbacks::UnrouteCallback) );
    customManager->AddCallback( CustomManager::CallbackReasonCreatePortConnection, make_callback(this, &Callbacks::CreateConnectionCallback) );
};

//--------------------------------------------------------------------------------------------------
void Callbacks::AutorouteCallback
(
    StlNXObjectVector objects
)
{
    std::stringstream message;
    message << "\n*** C++ AutorouteCallback called with " << objects.size() << " objects.";
    echo( message.str() );

    for ( NXObject* object : objects )
    {
        Electrical::WireDevice* wireDevice = dynamic_cast<Electrical::WireDevice*>( object );

        if ( wireDevice == nullptr )
        {
            message.str( "" );
            message << "  NX Object Tag " << object->Tag() << " is NOT a Wire Device.";
            throw NXException::Create( message.str().c_str() );
        }

        message.str( "" );
        message << "  Wire Device (Tag " << object->Tag() << ") named " << wireDevice->Name().GetLocaleText() << ".";
        echo( message.str() );
    }

    echo( "" );
};

//--------------------------------------------------------------------------------------------------
void Callbacks::UnrouteCallback
(
    StlNXObjectVector objects
)
{
    std::stringstream message;
    message << "\n*** C++ UnrouteCallback called with " << objects.size() << " objects.";
    echo( message.str() );

    for ( NXObject* object : objects )
    {
        Electrical::WireDevice* wireDevice = dynamic_cast<Electrical::WireDevice*>( object );

        if ( wireDevice == nullptr )
        {
            message.str( "" );
            message << "  NX Object Tag " << object->Tag() << " is NOT a Wire Device.";
            throw NXException::Create( message.str().c_str() );
        }

        message.str( "" );
        message << "  Wire Device (Tag " << object->Tag() << ") named " << wireDevice->Name().GetLocaleText() << ".";
        echo( message.str() );
    }

    echo( "" );
};

//--------------------------------------------------------------------------------------------------
void Callbacks::CreateConnectionCallback
(
    StlNXObjectVector objects
)
{
    std::stringstream message;
    message << "\n*** C++ CreateConnectionCallback called with " << objects.size() << " objects.";
    echo( message.str() );

    for ( NXObject* object : objects )
    {
        PortConnection* portConnection = dynamic_cast<PortConnection*>( object );

        if ( portConnection == nullptr )
        {
            message.str( "" );
            message << "  NX Object Tag " << object->Tag() << " is NOT a Port Connection.";
            throw NXException::Create( message.str().c_str() );
        }

        Port* port1 = nullptr;
        Port* port2 = nullptr;
        portConnection->GetPorts( &port1, &port2 );

        message.str( "" );
        message << "  Port Connection (Tag " << object->Tag();
        message << ") connects port " << port1->Name().GetLocaleText();
        message << " with port " << port2->Name().GetLocaleText();
        echo( message.str() );
    }

    echo( "" );
};

//--------------------------------------------------------------------------------------------------
// Called when NX starts up to register the callbacks using the Callbacks class constructor.
extern "C" DllExport void ufsta
(
    char* /*param*/,
    int*  retcod,
    int   /*param_len*/
)
{
    *retcod = 0;

    theCallbacks = new Callbacks();
}

//--------------------------------------------------------------------------------------------------
// Tells NX when to unload your application.
// For Routing callbacks, plugins, and Design Rules, this MUST return UF_UNLOAD_UG_TERMINATE.
extern int ufusr_ask_unload()
{
    return( UF_UNLOAD_UG_TERMINATE );
}
