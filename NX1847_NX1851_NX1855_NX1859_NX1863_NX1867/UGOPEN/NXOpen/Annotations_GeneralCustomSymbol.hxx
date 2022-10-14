#ifndef NXOpen_ANNOTATIONS_GENERALCUSTOMSYMBOL_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_GENERALCUSTOMSYMBOL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_GeneralCustomSymbol.ja
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
#include <NXOpen/Annotations_BaseCustomSymbol.hxx>
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
        class GeneralCustomSymbol;
    }
    namespace Annotations
    {
        class BaseCustomSymbol;
    }
    namespace Annotations
    {
        class _GeneralCustomSymbolBuilder;
        class GeneralCustomSymbolImpl;
        /** Represents a general custom symbol 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  GeneralCustomSymbol : public NXOpen::Annotations::BaseCustomSymbol
        {
            private: GeneralCustomSymbolImpl * m_generalcustomsymbol_impl;
            private: friend class  _GeneralCustomSymbolBuilder;
            protected: GeneralCustomSymbol();
            public: ~GeneralCustomSymbol();
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