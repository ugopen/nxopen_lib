#ifndef NXOpen_TOOLING_STRIPPERVENTINGBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_STRIPPERVENTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_StripperVentingBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class StripperVentingBuilder;
    }
    class Builder;
    class Expression;
    class SelectEdgeList;
    class SelectNXObjectList;
    namespace Tooling
    {
        class _StripperVentingBuilderBuilder;
        class StripperVentingBuilderImpl;
        /** Stripper Venting Builder of PDW and EDW. A Body is returned by this builder.  <br> To create a new instance of this class, use @link NXOpen::Tooling::ProgressiveDieManager::CreateStripperVentingBuilder  NXOpen::Tooling::ProgressiveDieManager::CreateStripperVentingBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  StripperVentingBuilder : public NXOpen::Builder
        {
            /** Specifies the page type */
            public: enum Types
            {
                TypesCreate/** create */ ,
                TypesEdit/** edit */ 
            };

            private: StripperVentingBuilderImpl * m_stripperventingbuilder_impl;
            private: friend class  _StripperVentingBuilderBuilder;
            protected: StripperVentingBuilder();
            public: ~StripperVentingBuilder();
            /**Returns  the select edge for cutting venting hole 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectEdgeList * SelectEdge
            (
            );
            /**Returns  the selected object (either feature or face) that is to be edited. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectObject
            (
            );
            /**Returns  the width of venting hole 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Width
            (
            );
            /**Returns  the length of venting hole 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Length
            (
            );
            /**Returns  the blend radius of venting hole 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Radius
            (
            );
            /**Returns  the wizard type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: int WizardType
            (
            );
            /**Sets  the wizard type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetWizardType
            (
                int wizardType /** wizardtype */ 
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
