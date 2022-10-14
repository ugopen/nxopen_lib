#ifndef NXOpen_PCBEXCHANGE_DESIGNRULEBUILDER_HXX_INCLUDED
#define NXOpen_PCBEXCHANGE_DESIGNRULEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PcbExchange_DesignRuleBuilder.ja
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
#include <NXOpen/PcbExchange_Types.hxx>
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
        class DesignRuleBuilder;
    }
    class Builder;
    namespace PcbExchange
    {
        class _DesignRuleBuilderBuilder;
        class DesignRuleBuilderImpl;
        /** Creates or edits @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink .
                A call to @link NXOpen::Builder::Commit NXOpen::Builder::Commit@endlink  on this builder will only return NULL.
             <br> Use @link NXOpen::PcbExchange::Manager NXOpen::PcbExchange::Manager@endlink  to get an instance of this class.  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_PCBEXCHANGEEXPORT  DesignRuleBuilder : public NXOpen::Builder
        {
            /** Criteria for filtering entities of Component class. */
            public: enum ComponentFilter
            {
                ComponentFilterAny/** Accept any Pcb Components. */,
                ComponentFilterByPackage/** Filter Pcb Components by Package Name. */,
                ComponentFilterByOwner/** Filter Pcb Components by Owner. */,
                ComponentFilterByRefDes/** Filter Pcb Components by Reference Designator. */,
                ComponentFilterByPartNumber/** Filter Pcb Components by Part Number. */,
                ComponentFilterByCompType/** Filter Pcb Components by Type. */,
                ComponentFilterByPartName/** Filter Mechnanical entity by Part Name. */,
                ComponentFilterByAreaName/** Filter Area by Name. */,
                ComponentFilterByAreaSubtype/** Filter Area by Subtype. */,
                ComponentFilterByAreaOwner/** Filter Area by Owner. */,
                ComponentFilterByAreaLayer/** Filter Area by Layer. */,
                ComponentFilterSpecify/** Filter by selection. */
            };

            private: DesignRuleBuilderImpl * m_designrulebuilder_impl;
            private: friend class  _DesignRuleBuilderBuilder;
            protected: DesignRuleBuilder();
            public: ~DesignRuleBuilder();
            /**Returns  the rule name. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the rule name. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetName
            (
                const NXString & name /** The rule name */
            );
            /**Sets  the rule name. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            void SetName
            (
                const char * name /** The rule name */
            );
            /**Returns  the constraint type. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::DesignRuleType ConstraintType
            (
            );
            /**Sets  the constraint type. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetConstraintType
            (
                NXOpen::PcbExchange::DesignRuleType constraintType /** constrainttype */ 
            );
            /**Returns  the design rule severity. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::DesignRuleSeverity Severity
            (
            );
            /**Sets  the design rule severity. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetSeverity
            (
                NXOpen::PcbExchange::DesignRuleSeverity severity /** severity */ 
            );
            /** Gets the entity category for a given side of the constraint. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::EntityCategory GetEntityType
            (
                int filterIndex /** Index of the filter. */
            );
            /** Sets the entity category for a given side of the constraint. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetEntityType
            (
                int filterIndex /** Index of the filter. */,
                NXOpen::PcbExchange::EntityCategory entityType /** entitytype */ 
            );
            /** Gets the component filter criteria for a given side of the constraint. Only applicable when @link NXOpen::PcbExchange::EntityCategory NXOpen::PcbExchange::EntityCategory@endlink  is @link NXOpen::PcbExchange::EntityCategoryComponent NXOpen::PcbExchange::EntityCategoryComponent@endlink . 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::DesignRuleBuilder::ComponentFilter GetComponentFilter
            (
                int filterIndex /** Index of the filter. */
            );
            /** Sets the component filter criteria for a given side of the constraint. Only applicable when @link NXOpen::PcbExchange::EntityCategory NXOpen::PcbExchange::EntityCategory@endlink  is @link NXOpen::PcbExchange::EntityCategoryComponent NXOpen::PcbExchange::EntityCategoryComponent@endlink . 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetComponentFilter
            (
                int filterIndex /** Index of the filter. */,
                NXOpen::PcbExchange::DesignRuleBuilder::ComponentFilter componentFilter /** componentfilter */ 
            );
            /** Gets an optional string parameters for the component filter for a given side of the constraint. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetFilterData
            (
                int filterIndex /** Index of the filter. */
            );
            /** Sets an optional string parameter for the component filter for a given side of the constraint. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetFilterData
            (
                int filterIndex /** Index of the filter. */,
                const NXString & data /** data */ 
            );
            /** Sets an optional string parameter for the component filter for a given side of the constraint. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            void SetFilterData
            (
                int filterIndex /** Index of the filter. */,
                const char * data /** data */ 
            );
            /** Sets optional string parameters for the component filter for a given side of the constraint. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetFilterData
            (
                int filterIndex /** Index of the filter. */,
                const std::vector<NXString> & data /** data */ 
            );
            /** Gets an optional board side parameter for the component filter for a given side of the constraint. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::BoardSide GetBoardSide
            (
                int filterIndex /** Index of the filter. */
            );
            /** Sets an optional board side parameter for the component filter for a given side of the constraint. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetBoardSide
            (
                int filterIndex /** Index of the filter. */,
                NXOpen::PcbExchange::BoardSide side /** side */ 
            );
            /** Gets the clearance requirement in a given direction. The value is expressed in Part Units.  @return  The clearance value in Part Units. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double GetClearance
            (
                NXOpen::PcbExchange::DesignRuleMargin direction /** The direction. */
            );
            /** Sets the clearance requirement in a given direction. The value is expressed in Part Units. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void SetClearance
            (
                NXOpen::PcbExchange::DesignRuleMargin direction /** The direction. */,
                double clearance /** The clearance value in Part Units. */
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