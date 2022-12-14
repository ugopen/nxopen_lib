#ifndef NXOpen_FEATURES_SHEETMETAL_MULTIHEIGHTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_MULTIHEIGHTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_MultiHeightBuilder.ja
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
#include <NXOpen/Features_SheetMetal_SheetmetalComponentBuilder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class MultiHeightBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        namespace SheetMetal
        {
            class SheetmetalComponentBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class _MultiHeightBuilderBuilder;
            class MultiHeightBuilderImpl;

            /// \cond NX_NO_DOC 
            /** 
             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  MultiHeightBuilder : public NXOpen::Features::SheetMetal::SheetmetalComponentBuilder
            {
                private: MultiHeightBuilderImpl * m_multiheightbuilder_impl;
                private: friend class  _MultiHeightBuilderBuilder;
                protected: MultiHeightBuilder();
                public: ~MultiHeightBuilder();
                /**Returns  
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXString ZoneName
                (
                );
                /**Sets  
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetZoneName
                (
                    const NXString & zoneName /** zonename */ 
                );
                /**Sets  
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                void SetZoneName
                (
                    const char * zoneName /** zonename */ 
                );
                /**Returns  
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Expression * FlangeLateralOffset
                (
                );
            };

            /// \endcond 
        }
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
