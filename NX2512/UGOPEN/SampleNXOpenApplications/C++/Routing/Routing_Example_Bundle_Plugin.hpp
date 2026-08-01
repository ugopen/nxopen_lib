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

    The interface for a C++ class that implements an example bundling plugin.

    See Routing_Example_Bundle_Plugin.cpp for the implementation.


==================================================================================================*/
#ifndef Bundle_Plugin_HPP_INCLUDED
#define Bundle_Plugin_HPP_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

#include <uf_defs.h>
#include <NXOpen/Routing_StockData.hxx>

// Prototype for ufsta
extern "C" DllExport void ufsta( char* param , int* returncode, int param_len );

using StlStockDataVector = std::vector<NXOpen::Routing::StockData *>;

namespace NXOpen
{
    namespace Routing
    {
        //------------------------------------------------------------------------------------------
        // This class contains an example bundling plugin based on the Tyco algorithm.
        // This plugin is registered with the Routing Custom Manager plugin registry.
        class Tyco
        {
            //--------------------------------------------------------------------------------------
            // This default constructor registers every plugin listed below.
            public: Tyco();

            //--------------------------------------------------------------------------------------
            public: double BundlePlugin
            (
                StlStockDataVector stockDatas
            );
        };

        extern Tyco* thePlugin;
    }
}

#endif // Bundle_Plugin_HPP_INCLUDED
