#ifndef NXOpen_ANNOTATIONS_PMIEDGECONDITIONSYMBOL_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIEDGECONDITIONSYMBOL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiEdgeConditionSymbol.ja
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
#include <NXOpen/Annotations_BaseEdgeConditionSymbol.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class PmiEdgeConditionSymbol;
    }
    namespace Annotations
    {
        class BaseEdgeConditionSymbol;
    }
    namespace Annotations
    {
        class _PmiEdgeConditionSymbolBuilder;
        class PmiEdgeConditionSymbolImpl;

        /// \cond NX_NO_DOC 
        /** Represents PMI edge condition symbol  <br> To create or edit an instance of this class, use @link NXOpen::Annotations::PmiEdgeConditionSymbolBuilder  NXOpen::Annotations::PmiEdgeConditionSymbolBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiEdgeConditionSymbol : public NXOpen::Annotations::BaseEdgeConditionSymbol
        {
            private: PmiEdgeConditionSymbolImpl * m_pmiedgeconditionsymbol_impl;
            private: friend class  _PmiEdgeConditionSymbolBuilder;
            protected: PmiEdgeConditionSymbol();
            public: ~PmiEdgeConditionSymbol();
        };

        /// \endcond 
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
