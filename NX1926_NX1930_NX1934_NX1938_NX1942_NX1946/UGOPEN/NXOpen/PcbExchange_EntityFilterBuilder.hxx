#ifndef NXOpen_PCBEXCHANGE_ENTITYFILTERBUILDER_HXX_INCLUDED
#define NXOpen_PCBEXCHANGE_ENTITYFILTERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PcbExchange_EntityFilterBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_pcbexchange_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PcbExchange
    {
        class EntityFilterBuilder;
    }
    class Builder;
    namespace PcbExchange
    {
        class _EntityFilterBuilderBuilder;
        class EntityFilterBuilderImpl;
        /** Represents a @link NXOpen::PcbExchange::EntityFilterBuilder NXOpen::PcbExchange::EntityFilterBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateEntityFilterBuilder  NXOpen::PcbExchange::Manager::CreateEntityFilterBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        ComponentMaxHeight </term> <description> 
         
        999 </description> </item> 

        <item><term> 
         
        ComponentMaxSize </term> <description> 
         
        999 </description> </item> 

        <item><term> 
         
        ComponentMinHeight </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        ComponentMinSize </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        HoleMaxDiameter </term> <description> 
         
        999 </description> </item> 

        <item><term> 
         
        HoleMaxSize </term> <description> 
         
        999 </description> </item> 

        <item><term> 
         
        HoleMinDiameter </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        HoleMinSize </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        LengthUnits </term> <description> 
         
        Millimeters </description> </item> 

        <item><term> 
         
        RemoveBlindBuriedViaHoles </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveComponentsWithHeight </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveComponentsWithSize </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveEcadComponents </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveHolesWithDiameter </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveHolesWithSize </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveMcadComponents </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveMountingHoles </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveOtherHoles </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveOtherKeepoutAreas </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemovePinHoles </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemovePlacedComponents </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemovePlacementGroupKeepinAreas </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemovePlacementKeepinAreas </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemovePlacementKeepoutAreas </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveRoutingKeepinAreas </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveRoutingKeepoutAreas </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveToolingHoles </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveUnplacedComponents </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveViaHoles </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RemoveViaKeepoutAreas </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_PCBEXCHANGEEXPORT  EntityFilterBuilder : public NXOpen::Builder
        {
            /** This enum defines the length unit options. */
            public: enum LengthUnitsEnum
            {
                LengthUnitsEnumMillimeters/** millimeters */ ,
                LengthUnitsEnumInches/** inches */ 
            };

            private: EntityFilterBuilderImpl * m_entityfilterbuilder_impl;
            private: friend class  _EntityFilterBuilderBuilder;
            protected: EntityFilterBuilder();
            public: ~EntityFilterBuilder();
            /**Returns  the length units 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::EntityFilterBuilder::LengthUnitsEnum LengthUnits
            (
            );
            /**Sets  the length units 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetLengthUnits
            (
                NXOpen::PcbExchange::EntityFilterBuilder::LengthUnitsEnum lengthUnits /** lengthunits */ 
            );
            /**Returns  the remove holes with diameter 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveHolesWithDiameter
            (
            );
            /**Sets  the remove holes with diameter 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveHolesWithDiameter
            (
                bool removeHolesWithDiameter /** removeholeswithdiameter */ 
            );
            /**Returns  the hole min diameter 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double HoleMinDiameter
            (
            );
            /**Sets  the hole min diameter 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetHoleMinDiameter
            (
                double holeMinDiameter /** holemindiameter */ 
            );
            /**Returns  the hole max diameter 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double HoleMaxDiameter
            (
            );
            /**Sets  the hole max diameter 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetHoleMaxDiameter
            (
                double holeMaxDiameter /** holemaxdiameter */ 
            );
            /**Returns  the remove holes with size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveHolesWithSize
            (
            );
            /**Sets  the remove holes with size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveHolesWithSize
            (
                bool removeHolesWithSize /** removeholeswithsize */ 
            );
            /**Returns  the hole min size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double HoleMinSize
            (
            );
            /**Sets  the hole min size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetHoleMinSize
            (
                double holeMinSize /** holeminsize */ 
            );
            /**Returns  the hole max size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double HoleMaxSize
            (
            );
            /**Sets  the hole max size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetHoleMaxSize
            (
                double holeMaxSize /** holemaxsize */ 
            );
            /**Returns  the remove via holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveViaHoles
            (
            );
            /**Sets  the remove via holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveViaHoles
            (
                bool removeViaHoles /** removeviaholes */ 
            );
            /**Returns  the remove pin holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemovePinHoles
            (
            );
            /**Sets  the remove pin holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemovePinHoles
            (
                bool removePinHoles /** removepinholes */ 
            );
            /**Returns  the remove mounting holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveMountingHoles
            (
            );
            /**Sets  the remove mounting holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveMountingHoles
            (
                bool removeMountingHoles /** removemountingholes */ 
            );
            /**Returns  the remove tooling holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveToolingHoles
            (
            );
            /**Sets  the remove tooling holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveToolingHoles
            (
                bool removeToolingHoles /** removetoolingholes */ 
            );
            /**Returns  the remove other holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveOtherHoles
            (
            );
            /**Sets  the remove other holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveOtherHoles
            (
                bool removeOtherHoles /** removeotherholes */ 
            );
            /**Returns  the remove blind buried via holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveBlindBuriedViaHoles
            (
            );
            /**Sets  the remove blind buried via holes 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveBlindBuriedViaHoles
            (
                bool removeBlindBuriedViaHoles /** removeblindburiedviaholes */ 
            );
            /**Returns  the component min height 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double ComponentMinHeight
            (
            );
            /**Sets  the component min height 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetComponentMinHeight
            (
                double componentMinHeight /** componentminheight */ 
            );
            /**Returns  the component max height 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double ComponentMaxHeight
            (
            );
            /**Sets  the component max height 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetComponentMaxHeight
            (
                double componentMaxHeight /** componentmaxheight */ 
            );
            /**Returns  the component min size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double ComponentMinSize
            (
            );
            /**Sets  the component min size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetComponentMinSize
            (
                double componentMinSize /** componentminsize */ 
            );
            /**Returns  the component max size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double ComponentMaxSize
            (
            );
            /**Sets  the component max size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetComponentMaxSize
            (
                double componentMaxSize /** componentmaxsize */ 
            );
            /**Returns  the remove components with height 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveComponentsWithHeight
            (
            );
            /**Sets  the remove components with height 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveComponentsWithHeight
            (
                bool removeComponentsWithHeight /** removecomponentswithheight */ 
            );
            /**Returns  the remove components with size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveComponentsWithSize
            (
            );
            /**Sets  the remove components with size 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveComponentsWithSize
            (
                bool removeComponentsWithSize /** removecomponentswithsize */ 
            );
            /**Returns  the remove unplaced components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveUnplacedComponents
            (
            );
            /**Sets  the remove unplaced components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveUnplacedComponents
            (
                bool removeUnplacedComponents /** removeunplacedcomponents */ 
            );
            /**Returns  the remove placed components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemovePlacedComponents
            (
            );
            /**Sets  the remove placed components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemovePlacedComponents
            (
                bool removePlacedComponents /** removeplacedcomponents */ 
            );
            /**Returns  the remove ecad components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveEcadComponents
            (
            );
            /**Sets  the remove ecad components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveEcadComponents
            (
                bool removeEcadComponents /** removeecadcomponents */ 
            );
            /**Returns  the remove mcad components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveMcadComponents
            (
            );
            /**Sets  the remove mcad components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveMcadComponents
            (
                bool removeMcadComponents /** removemcadcomponents */ 
            );
            /**Returns  the remove routing keepin areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveRoutingKeepinAreas
            (
            );
            /**Sets  the remove routing keepin areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveRoutingKeepinAreas
            (
                bool removeRoutingKeepinAreas /** removeroutingkeepinareas */ 
            );
            /**Returns  the remove placement keepin areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemovePlacementKeepinAreas
            (
            );
            /**Sets  the remove placement keepin areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemovePlacementKeepinAreas
            (
                bool removePlacementKeepinAreas /** removeplacementkeepinareas */ 
            );
            /**Returns  the remove placement group keepin areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemovePlacementGroupKeepinAreas
            (
            );
            /**Sets  the remove placement group keepin areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemovePlacementGroupKeepinAreas
            (
                bool removePlacementGroupKeepinAreas /** removeplacementgroupkeepinareas */ 
            );
            /**Returns  the remove routing keepout areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveRoutingKeepoutAreas
            (
            );
            /**Sets  the remove routing keepout areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveRoutingKeepoutAreas
            (
                bool removeRoutingKeepoutAreas /** removeroutingkeepoutareas */ 
            );
            /**Returns  the remove placement keepout areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemovePlacementKeepoutAreas
            (
            );
            /**Sets  the remove placement keepout areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemovePlacementKeepoutAreas
            (
                bool removePlacementKeepoutAreas /** removeplacementkeepoutareas */ 
            );
            /**Returns  the remove via keepout areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveViaKeepoutAreas
            (
            );
            /**Sets  the remove via keepout areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveViaKeepoutAreas
            (
                bool removeViaKeepoutAreas /** removeviakeepoutareas */ 
            );
            /**Returns  the remove other keepout areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveOtherKeepoutAreas
            (
            );
            /**Sets  the remove other keepout areas 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetRemoveOtherKeepoutAreas
            (
                bool removeOtherKeepoutAreas /** removeotherkeepoutareas */ 
            );
            /** Method to set user-definied filter 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetUserDefiniedFilters
            (
                std::vector<NXString> & filters /** filters */ 
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
