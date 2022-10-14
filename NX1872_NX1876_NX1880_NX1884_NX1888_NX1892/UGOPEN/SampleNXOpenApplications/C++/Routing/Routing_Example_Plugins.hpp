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

    The interface for a C++ class that implements example Routing plugins.

    See Routing_Example_Plugins.cpp for the implementation.


==================================================================================================*/
#ifndef PLUGINS_HPP_INCLUDED
#define PLUGINS_HPP_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

#include <NXOpen/NXString.hxx>
#include <NXOpen/Routing_Anchor.hxx>
#include <NXOpen/Routing_ChoosePartPluginData.hxx>
#include <NXOpen/Routing_CrossSection.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Routing_Electrical_Connection.hxx>
#include <NXOpen/Routing_Electrical_ElectricalStockDevice.hxx>
#include <NXOpen/Routing_Electrical_HarnessDevice.hxx>
#include <NXOpen/Routing_Electrical_SortConnectionsPluginData.hxx>
#include <NXOpen/Routing_Overstock.hxx>
#include <NXOpen/Routing_StockData.hxx>
#include <NXOpen/Routing_Wire.hxx>

namespace NXOpen
{
    namespace Routing
    {
        using StlTagVector           = std::vector<tag_t>;
        using StlNXObjectVector      = std::vector<NXObject *>;
        using StlConnectionVector    = std::vector<Electrical::Connection *>;
        using StlStockDeviceVector   = std::vector<Electrical::ElectricalStockDevice*>;
        using StlHarnessDeviceVector = std::vector<Electrical::HarnessDevice *>;
        using StlWireVector          = std::vector<Wire *>;
        using StlCrossSectionVector  = std::vector<CrossSection *>;
        using StlStockDataVector     = std::vector<StockData *>;
        using StlAnchorVector        = std::vector<Anchor *>;
        using StlComponentVector     = std::vector<Assemblies::Component *>;

        //------------------------------------------------------------------------------------------
        // This class contains several example plugins to show how to register C++ plugins with the
        // Routing Custom Manager plugin registry.
        class Plugins
        {
            //--------------------------------------------------------------------------------------
            // This default constructor registers every plugin listed below.
            public: Plugins();

            //--------------------------------------------------------------------------------------
            // Called just after Routing exports an PLMXML file.
            //
            // \param[in]
            //      fileName
            //          The name of the file Routing just exported.
            public: void ImportExportPlugin
            (
                NXString fileName
            );

            //--------------------------------------------------------------------------------------
            // Called anytime Routing export PLMXML needs a new name for a Route Node.
            //
            // \return
            //      The new name created for the Route Node.
            public: NXString RouteNodeNamePlugin();

            //--------------------------------------------------------------------------------------
            // Called anytime Routing export PLMXML needs a new name for a Route Section.
            //
            // \return
            //      The new name created for the Route Node.
            public: NXString RouteSectionNamePlugin();

            //--------------------------------------------------------------------------------------
            // Called called by Routing to calculate the length of a wrapped overstock
            public: double WrappedOverstockLengthCalculationPlugin( Overstock* overstock );

            //--------------------------------------------------------------------------------------
            // Called called by Routing to determine if the segment or component should be blanked.
            // This example returns true if the attribute's title matches the Rlist_Filter_Blanking_Attribute
            // in the Application View (APV) file and it's value is "positive" (e.g. "true", "yes", "1").
            public: bool FilterBlankingPlugin
            (
                NXObject* segmentOrComponent,
                NXString  logicalAttributeTitle,
                NXString  logicalAttributeValue,
                NXString  variableBuildString
            );

            //--------------------------------------------------------------------------------------
            // Called just after Routing creates a bill of materials (BOM).
            //
            // The intent is that the plugin can then add stocks to Teamcenter's Product Structure.
            public: void BomPlugin();

            //--------------------------------------------------------------------------------------
            // Called instead of the internal Routing autoroute method.
            //
            // \param[in]
            //      connections
            //          The vector connections to route.
            //
            // \return
            //      The number of connections successfully routed.
            public: int AutoRoutePlugin
            (
                StlConnectionVector connections
            );

            //--------------------------------------------------------------------------------------
            // Called instead of the internal Routing manual route method.
            //
            // \param[in]
            //      connections
            //          The vector connections to route.
            //
            // \return
            //      The number of connections successfully routed.
            public: int ManualRoutePlugin
            (
                StlConnectionVector connections
            );

            //--------------------------------------------------------------------------------------
            // Called instead of the internal Routing unroute method.
            //
            // \param[in]
            //      connections
            //          The vector connections to unroute.
            //
            // \return
            //      The number of connections successfully unrouted.
            public: int UnroutePlugin
            (
                StlConnectionVector connections
            );

            //--------------------------------------------------------------------------------------
            // Called whenever an object on the Component or Connection Navigator is selected or deselected.
            //
            // \param[in]
            //      navigatorType
            //          The navigator in which the objects were selected.
            //
            // \param[in]
            //      selectionType
            //          Whether the objects were selected or deselected.
            //
            // \param[in]
            //      selectedObjects
            //          The objects themselves.
            public: void NavigatorObjectSelectedPlugin
            (
                CustomManager::NavigatorType navigatorType,
                CustomManager::SelectionType selectionType,
                StlNXObjectVector            selectedObjects
            );

            //--------------------------------------------------------------------------------------
            // Called by Routing Formboard to validate the given harnesses on the formboard.
            public: bool ValidateFormboardPlugin
            (
                StlHarnessDeviceVector harnessDevices
            );

            //--------------------------------------------------------------------------------------
            // Called by Routing when the user changes the discipline in the Routing Preferences dialog.
            public: void DisciplineChangedPlugin
            (
                NXString previousDisciplineName,
                NXString newDisciplineName
            );

            //--------------------------------------------------------------------------------------
            // Called by Routing when the user changes the active specification in the Reuse Library.
            public: void SpecificationChangedPlugin
            (
                NXString previousSpecificationName,
                NXString newSpecificationName
            );

            //--------------------------------------------------------------------------------------
            // Called by Routing just before routing the connections along their paths.
            public: void SortConnectionsPlugin
            (
                Electrical::SortConnectionsPluginData* dataObject
            );

            //--------------------------------------------------------------------------------------
            // Called by Place Part command to let you choose a part.
            public: int ChoosePartPlugin
            (
                ChoosePartPluginData* dataObject
            );

            //--------------------------------------------------------------------------------------
            public: void PipingComponentFilePlugin
            (
                NXString                                  fileName,
                StlComponentVector                        components,
                CustomManager::PipingComponentFileOptions options
            );
        };

        extern Plugins* thePlugins;
    }
}

#endif // PLUGINS_HPP_INCLUDED
