#ifndef NXOpen_TOOLING_SMARTSCREWUPDATEBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_SMARTSCREWUPDATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_SmartScrewUpdateBuilder.ja
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
#include <NXOpen/Tooling_SmartScrewUpdateBuilder.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class SmartScrewUpdateBuilder;
    }
    class Builder;
    namespace Tooling
    {
        class _SmartScrewUpdateBuilderBuilder;
        class SmartScrewUpdateBuilderImpl;
        /** Smart Screw Update of MW, PDW and EDW. No entity is returned. <br> To create a new instance of this class, use @link NXOpen::Tooling::ProgressiveDieManager::CreateSmartScrewUpdateBuilder  NXOpen::Tooling::ProgressiveDieManager::CreateSmartScrewUpdateBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  SmartScrewUpdateBuilder : public NXOpen::Builder
        {
            /** Specify the operation type. */
            public: enum Types
            {
                TypesUpdateSmartScrew/** update smart screw */ ,
                TypesCopyPartFamilyPart/** copy part family part */ ,
                TypesDeletePartFamilyPart/** delete part family part */ 
            };

            /** Specify the parent node. */
            public: enum ParentOption
            {
                ParentOptionNoParent/** no parent */ 
            };

            private: SmartScrewUpdateBuilderImpl * m_smartscrewupdatebuilder_impl;
            private: friend class  _SmartScrewUpdateBuilderBuilder;
            protected: SmartScrewUpdateBuilder();
            public: ~SmartScrewUpdateBuilder();
            /**Returns  the operation type of Tooling Part Family Part Tool. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SmartScrewUpdateBuilder::Types Type
            (
            );
            /**Sets  the operation type of Tooling Part Family Part Tool. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetType
            (
                NXOpen::Tooling::SmartScrewUpdateBuilder::Types type /** type */ 
            );
            /**Returns  the parent node 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SmartScrewUpdateBuilder::ParentOption ParentNode
            (
            );
            /**Sets  the parent node 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetParentNode
            (
                NXOpen::Tooling::SmartScrewUpdateBuilder::ParentOption parentNode /** parentnode */ 
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