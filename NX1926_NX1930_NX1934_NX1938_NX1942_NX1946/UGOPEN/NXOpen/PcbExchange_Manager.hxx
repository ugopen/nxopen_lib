#ifndef NXOpen_PCBEXCHANGE_MANAGER_HXX_INCLUDED
#define NXOpen_PCBEXCHANGE_MANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PcbExchange_Manager.ja
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
#include <NXOpen/PcbExchange_DesignRule.hxx>
#include <NXOpen/PcbExchange_DesignRuleBuilder.hxx>
#include <NXOpen/PcbExchange_EntityFilterBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class Manager;
    }
    class Session;
    class NXObject;
    namespace PcbExchange
    {
        class AreaAttributesBuilder;
    }
    namespace PcbExchange
    {
        class BoardAttributesBuilder;
    }
    namespace PcbExchange
    {
        class BoardSettingsBuilder;
    }
    namespace PcbExchange
    {
        class CompSettingsBuilder;
    }
    namespace PcbExchange
    {
        class CompareAndUpdateBuilder;
    }
    namespace PcbExchange
    {
        class ComponentAttributesBuilder;
    }
    namespace PcbExchange
    {
        class DesignRule;
    }
    namespace PcbExchange
    {
        class DesignRuleBuilder;
    }
    namespace PcbExchange
    {
        class EcadExportBuilder;
    }
    namespace PcbExchange
    {
        class EcadImportBuilder;
    }
    namespace PcbExchange
    {
        class EcadPanelImportBuilder;
    }
    namespace PcbExchange
    {
        class EntityFilter;
    }
    namespace PcbExchange
    {
        class EntityFilterBuilder;
    }
    namespace PcbExchange
    {
        class HoleAttributesBuilder;
    }
    namespace PcbExchange
    {
        class IdxCompareBuilder;
    }
    namespace PcbExchange
    {
        class IdxExportBuilder;
    }
    namespace PcbExchange
    {
        class IdxImportBuilder;
    }
    namespace PcbExchange
    {
        class PreferencesBuilder;
    }
    namespace PcbExchange
    {
        class ReportBuilder;
    }
    namespace PcbExchange
    {
        class ManagerImpl;
        /** Represents a @link NXOpen::PcbExchange::Manager NXOpen::PcbExchange::Manager@endlink   <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_PCBEXCHANGEEXPORT  Manager
        {
            private: ManagerImpl * m_manager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit Manager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static Manager* theManager;
            /** Returns the Manager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static Manager* GetManager(NXOpen::Session *owner);
            public: ~Manager();
            /** Method to create an instance of BoardAttributesBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::BoardAttributesBuilder * CreateBoardAttributesBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of ComponentAttributesBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::ComponentAttributesBuilder * CreateComponentAttributesBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of HoleAttributesBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::HoleAttributesBuilder * CreateHoleAttributesBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of AreaAttributesBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::AreaAttributesBuilder * CreateAreaAttributesBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of EcadImportBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::EcadImportBuilder * CreateEcadImportBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of EcadExportBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::EcadExportBuilder * CreateEcadExportBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of CompareAndUpdateBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::CompareAndUpdateBuilder * CreateCompareAndUpdateBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of IdxImportBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::IdxImportBuilder * CreateIdxImportBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of IdxExportBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::IdxExportBuilder * CreateIdxExportBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of IdxCompareBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::IdxCompareBuilder * CreateIdxCompareBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of BoardSettingsBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::BoardSettingsBuilder * CreateBoardSettingsBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of CompSettingsBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::CompSettingsBuilder * CreateCompSettingsBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to create an instance of EntityFilterBuilder  @return  created builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::EntityFilterBuilder * CreateEntityFilterBuilder
            (
                NXOpen::NXObject * part /** part */ ,
                NXOpen::PcbExchange::EntityFilter * entityFilter /** the entity filter to be edited */
            );
            /** Creates a @link PcbExchange::DesignRuleBuilder PcbExchange::DesignRuleBuilder@endlink  which creates a @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink  in the given part.  @return  created builder 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::DesignRuleBuilder * CreateDesignRuleBuilder
            (
                NXOpen::NXObject * part /** part */
            );
            /** Creates a @link PcbExchange::DesignRuleBuilder PcbExchange::DesignRuleBuilder@endlink  which edits a @link NXOpen::PcbExchange::DesignRule NXOpen::PcbExchange::DesignRule@endlink .  @return  created builder 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::DesignRuleBuilder * CreateDesignRuleBuilder
            (
                NXOpen::PcbExchange::DesignRule * ruleToEdit /** rule to edit */
            );
            /** Method to create an instance of EcadPanelImportBuilder  @return  created builder 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::EcadPanelImportBuilder * CreateEcadPanelImportBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
            /** Method to update components using library components 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: void ReplaceWithLibraryComponent
            (
                const std::vector<NXOpen::NXObject *> & components /** components */ 
            );
            /** Method to create an instance of ReportBuilder  @return  created builder 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_pcbx_xpedition ("PCB Exchange for Xpedition") OR ug_pcb_modeler ("PCB Modeler") OR ug_pcbx_zuken ("PCB Exchange for Zuken") */
            public: NXOpen::PcbExchange::ReportBuilder * CreateReportBuilder
            (
                NXOpen::NXObject * part /** part */
            );
            /** Method to create an instance of PcbExchangePreferencesBuilder  @return  created builder 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::PreferencesBuilder * CreatePreferencesBuilder
            (
                NXOpen::NXObject * part /** part */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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
