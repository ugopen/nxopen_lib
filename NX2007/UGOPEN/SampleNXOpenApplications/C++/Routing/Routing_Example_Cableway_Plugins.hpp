/*==================================================================================================
                                       Copyright 2020 Siemens
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    The interface for a C++ class that implements example Routing Cableway plugins.

    See Routing_Example_Cableway_Plugins.cpp for the implementation.


==================================================================================================*/
#ifndef CABLEWAY_PLUGINS_HPP_INCLUDED
#define CABLEWAY_PLUGINS_HPP_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

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
        //------------------------------------------------------------------------------------------
        // This class contains several example plugins to show how to register C++ plugins with the
        // Routing Custom Manager plugin registry.
        class Plugins
        {
            //--------------------------------------------------------------------------------------
            // This default constructor currently does nothing. Call the Register method below
            // to register the plugins.
            public: Plugins() = default;

            //--------------------------------------------------------------------------------------
            // Registers every plugin listed below.
            public: void Register();

            //--------------------------------------------------------------------------------------
            // Removes all the plugins added in Register.
            public: void Deregister();

            //--------------------------------------------------------------------------------------
            // Called when you enter one of the Routed System Designer (RSD) applications.
            // When entering the Mechanical application, registers the DisciplineChanged plugin.
            public: void ApplicationEnter
            (
                CustomManager::Application application
            );

            //--------------------------------------------------------------------------------------
            // Called when you enter one of the Routed System Designer (RSD) applications.
            // Unregisters the DisciplineChanged plugin.
            public: void ApplicationExit
            (
                CustomManager::Application application
            );

            //--------------------------------------------------------------------------------------
            // Called when you change the discipline. Registers the Cableway plugins listed above
            // if the new discipline is the cableway discipline. Otherwise, it deregisters the plugins.
            public: void DisciplineChanged
            (
                NXString previousDisciplineName,
                NXString newDisciplineName
            );

            //--------------------------------------------------------------------------------------
            // Called before Routing exports a Cableway XML file to return the name of the XML file
            // into which to write the Cableway data.
            public: NXString CablewayXmlFileName();

            //--------------------------------------------------------------------------------------
            // Called while Routing exports a Cableway XML file to create a new, unique identifier
            // for the given control point.
            //
            // \param[in]
            //      areaName
            //          The name of the area under which the cableway part and node object live.
            //
            // \param[in]
            //      cablewaySubassembly
            //          The cableway subassembly that owns the node object.
            //
            // \param[in]
            //      nodeObjectOccurrence
            //          The control point or point occurrence that needs a unique ID.
            //
            // \return
            //      The unique ID for this control point.
            public: NXString CablewayNodeName
            (
                NXString               areaName,
                Assemblies::Component* cablewaySubassembly,
                NXObject*              nodeObjectOccurrence
            );

            //--------------------------------------------------------------------------------------
            // Called while Routing exports a Cableway XML file to create a new, unique identifier
            // for the given segment.
            //
            // \param[in]
            //      areaName
            //          The name of the area under which the cableway part and segment live.
            //
            // \param[in]
            //      cablewaySubassembly
            //          The cableway subassembly that owns the segment object.
            //
            // \param[in]
            //      segmentObject
            //          The segment occurrence or hanger component that needs a unique ID.
            //
            // \return
            //      The unique ID for this segment.
            public: NXString CablewaySegmentName
            (
                NXString               areaName,
                Assemblies::Component* cablewaySubassembly,
                NXObject*              segmentObject
            );

            //--------------------------------------------------------------------------------------
            // Called while Routing exports a Cableway XML file to identify if the given component
            // is a device that should be exported.
            //
            // \param[in]
            //      component
            //          The component to check.
            //
            // \return
            //      The device ID to use for this component in the Cableway XML file.
            //      Returns an empty string if this device should not be exported.
            public: NXString CablewayDeviceIdentifier
            (
                Assemblies::Component* component
            );

            //--------------------------------------------------------------------------------------
            // Called just before Routing exports a Cableway XML file.
            //
            // \param[in]
            //      xmlFileName
            //          The name of the XML file Routing will export.
            public: void CablewayPreExport
            (
                NXString xmlFileName
            );

            //--------------------------------------------------------------------------------------
            // Called just after Routing exports a Cableway XML file.
            //
            // \param[in]
            //      xmlFileName
            //          The name of the XML file Routing just exported.
            public: void CablewayPostExport
            (
                NXString xmlFileName
            );

            //--------------------------------------------------------------------------------------
            // Called during Cableway export to create an area name for a given component and all
            // the components under it.
            //
            // \param[in]
            //      component
            //          The component to check.
            //
            // \return
            //      The area name to use for all the devices, hangers, nodes, segments, etc., found
            //      under this component.
            public: NXString CablewayAreaName
            (
                Assemblies::Component* component
            );
        };

        extern Plugins* thePlugins;
    }
}

#endif
