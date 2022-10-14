#ifndef NXOpen_ANNOTATIONS_ORDINATEMARGIN_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ORDINATEMARGIN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_OrdinateMargin.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class OrdinateMargin;
    }
    class NXObject;
    namespace Annotations
    {
        class _OrdinateMarginBuilder;
        class OrdinateMarginImpl;
        /** Represents an ordinate margin */
        class NXOPENCPPEXPORT  OrdinateMargin : public NXObject
        {
            private: OrdinateMarginImpl * m_ordinatemargin_impl;
            private: friend class  _OrdinateMarginBuilder;
            protected: OrdinateMargin();
            public: ~OrdinateMargin();
        };
    }
}
#undef EXPORTLIBRARY
#endif