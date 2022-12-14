#ifndef NXOpen_ANNOTATIONS_MASTERCUSTOMSYMBOL_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_MASTERCUSTOMSYMBOL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_MasterCustomSymbol.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class MasterCustomSymbol;
    }
    namespace Annotations
    {
        class _MasterCustomSymbolBuilder;
        class MasterCustomSymbolImpl;
        /** Represents a custom symbol */
        class NXOPENCPPEXPORT  MasterCustomSymbol : public TaggedObject
        {
            private: MasterCustomSymbolImpl * m_mastercustomsymbol_impl;
            private: friend class  _MasterCustomSymbolBuilder;
            protected: MasterCustomSymbol();
            public: ~MasterCustomSymbol();
        };
    }
}
#undef EXPORTLIBRARY
#endif
