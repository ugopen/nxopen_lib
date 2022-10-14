#ifndef NXOpen_ANNOTATIONS_PMICUSTOMSYMBOL_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMICUSTOMSYMBOL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiCustomSymbol.ja
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
#include <NXOpen/Annotations_IPmi.hxx>
#include <NXOpen/Annotations_AssociatedObject.hxx>
#include <NXOpen/Annotations_BaseCustomSymbol.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiCustomSymbol;
    }
    namespace Annotations
    {
        class AssociatedObject;
    }
    namespace Annotations
    {
        class BaseCustomSymbol;
    }
    namespace Annotations
    {
        class BusinessModifier;
    }
    namespace Annotations
    {
        class IPmi;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _PmiCustomSymbolBuilder;
        class PmiCustomSymbolImpl;
        /** Represents a PMI custom symbol */
        class NXOPENCPPEXPORT  PmiCustomSymbol : public Annotations::BaseCustomSymbol, public virtual Annotations::IPmi
        {
            private: PmiCustomSymbolImpl * m_pmicustomsymbol_impl;
            private: friend class  _PmiCustomSymbolBuilder;
            protected: PmiCustomSymbol();
            public: ~PmiCustomSymbol();
        };
    }
}
#undef EXPORTLIBRARY
#endif