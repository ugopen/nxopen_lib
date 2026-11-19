/*==================================================================================================

    This material contains trade secrets or otherwise confidential information owned by
    Siemens Industry Software Inc. or its affiliates (collectively, "SISW"), or its licensors.
    Access to and use of this information is strictly limited as set forth in the Customer's
    applicable agreements with SISW.

    Unpublished work Copyright 2023 Siemens

====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A C++ class that implements example Routing Spool plugins.

    See Routing_Example_Spool_Plugins.cpp for the interface.


==================================================================================================*/
#ifndef SPOOL_PLUGINS_HPP_INCLUDED
#define SPOOL_PLUGINS_HPP_INCLUDED

#pragma once

#include <uf_defs.h>

#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/RoutingCommon_CustomManager.hxx>

// Prototype for ufsta
extern "C" DllExport void ufsta( char* param, int* returncode, int param_len );

namespace NXOpen
{
    namespace RoutingCommon
    {
        using StlComponentVector = std::vector<Assemblies::Component*>;

        //------------------------------------------------------------------------------------------
        // This class contains example plugin(s) to show how to register C++ plugins with the
        // Routing Custom Manager plugin registry.
        class SpoolPlugins
        {
            //--------------------------------------------------------------------------------------
            // This default constructor currently does nothing. The ufsta routine registers the plugins
            // when NX starts.
            public: SpoolPlugins() = default;

            //--------------------------------------------------------------------------------------
            // Called by the Spool dialog to create a name for the new spool.
            // 
            // The name this plugin generates is a combination of:
            // 
            //   - Prefix:        The spool Name Prefix defined in the Routed System Designer->Mechanical->Spools customer defaults.
            //   - Block:         The Block identifier is simply the name of the work part.
            //   - Specification: The specification assigned to the components.
            //   - Run ID:        The identifier of the run to which the components belong.
            //   - Index:         An index one greater than the number of existing spools in the part.
            //
            // \param[in]
            //      spoolPart
            //          The part in which the new spool is created.
            //
            // \param[in]
            //      spoolComponents
            //          The connected components that will make up the new spool.
            //
            // \return
            //      The name the Routing application will use for the new spool.
            public: NXString GenerateSpoolName
            (
                Part*              spoolPart,
                StlComponentVector spoolComponents
            );
        };

        extern SpoolPlugins* theSpoolPlugins;
    }
}
#endif
