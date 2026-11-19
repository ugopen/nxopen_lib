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

    The interface for a C++ class that implements example Routing callbacks.

    See Routing_Example_Callbacks.cpp for the implementation.


==================================================================================================*/
#ifndef CALLBACKS_HPP_INCLUDED
#define CALLBACKS_HPP_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

#include <sstream>
#include <string>
#include <uf.h>
#include <vector>

#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Session.hxx>

namespace NXOpen
{
    namespace Routing
    {
        typedef std::vector<NXObject *> StlNXObjectVector;

        //--------------------------------------------------------------------------------------------------
        // This class contains several example callbacks to show how to register C++ callbacks with the
        // Routing Custom Manager callback registry.
        class Callbacks
        {
            //----------------------------------------------------------------------------------------------
            // This default constructor registers every callback listed below.
            public: Callbacks();

            //----------------------------------------------------------------------------------------------
            // Called whenever the Autoroute command is used.
            //
            // \param[in]
            //      objects
            //          The array of Electrical WireDevices just routed.
            public: void AutorouteCallback
            (
                StlNXObjectVector objects
            );

            //----------------------------------------------------------------------------------------------
            // Called whenever the Unroute command is used.
            //
            // \param[in]
            //      objects
            //          The array of Electrical WireDevices just unrouted.
            public: void UnrouteCallback
            (
                StlNXObjectVector objects
            );

            //----------------------------------------------------------------------------------------------
            // Called whenever a port-to-port connection is made.
            //
            // \param[in]
            //      objects
            //          The PortConnection object just created between two ports.
            public: void CreateConnectionCallback
            (
                StlNXObjectVector objects
            );
        };

        extern Callbacks* theCallbacks;
    }
}

#endif // CALLBACKS_HPP_INCLUDED
