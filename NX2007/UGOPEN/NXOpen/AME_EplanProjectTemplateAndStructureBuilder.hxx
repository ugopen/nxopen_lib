#ifndef NXOpen_AME_EPLANPROJECTTEMPLATEANDSTRUCTUREBUILDER_HXX_INCLUDED
#define NXOpen_AME_EPLANPROJECTTEMPLATEANDSTRUCTUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_EplanProjectTemplateAndStructureBuilder.ja
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
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class EplanProjectTemplateAndStructureBuilder;
    }
    class Builder;
    namespace AME
    {
        class _EplanProjectTemplateAndStructureBuilderBuilder;
        class EplanProjectTemplateAndStructureBuilderImpl;
        /** JA class for the Eplan project template dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateEplanProjectTemplateAndStructureBuilder  NXOpen::AME::AMEManager::CreateEplanProjectTemplateAndStructureBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  EplanProjectTemplateAndStructureBuilder : public NXOpen::Builder
        {
            private: EplanProjectTemplateAndStructureBuilderImpl * m_eplanprojecttemplateandstructurebuilder_impl;
            private: friend class  _EplanProjectTemplateAndStructureBuilderBuilder;
            protected: EplanProjectTemplateAndStructureBuilder();
            public: ~EplanProjectTemplateAndStructureBuilder();
            /**Returns  the structure order index for function 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int StructureOrderFunctionIndex
            (
            );
            /**Sets  the structure order index for function 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStructureOrderFunctionIndex
            (
                int structureOrderFunctionState /** structureorderfunctionstate */ 
            );
            /**Returns  the structure order index for location 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int StructureOrderLocationIndex
            (
            );
            /**Sets  the structure order index for location 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStructureOrderLocationIndex
            (
                int structureOrderLocationState /** structureorderlocationstate */ 
            );
            /**Returns  the structure order index for functional assignment 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int StructureOrderFunctionalAssignmentIndex
            (
            );
            /**Sets  the structure order index for functional assignment 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStructureOrderFunctionalAssignmentIndex
            (
                int structureOrderFunctionalAssignmentState /** structureorderfunctionalassignmentstate */ 
            );
            /**Returns  the structure order index for installation site 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int StructureOrderInstallationSiteIndex
            (
            );
            /**Sets  the structure order index for installation site 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStructureOrderInstallationSiteIndex
            (
                int structureOrderInstallationSiteState /** structureorderinstallationsitestate */ 
            );
            /**Returns  the structure order index for document type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int StructureOrderDocumentTypeIndex
            (
            );
            /**Sets  the structure order index for document type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStructureOrderDocumentTypeIndex
            (
                int structureOrderDocumentTypeState /** structureorderdocumenttypestate */ 
            );
            /**Returns  the structure order index for user-defined structure 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int StructureOrderUserDefinedStructureIndex
            (
            );
            /**Sets  the structure order index for user-defined structure 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStructureOrderUserDefinedStructureIndex
            (
                int structureOrderUserDefinedStructureState /** structureorderuserdefinedstructurestate */ 
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