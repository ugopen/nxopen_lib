#ifndef NXOpen_ANNOTATIONS_CIRCULARCENTERLINE_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_CIRCULARCENTERLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CircularCenterline.ja
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
#include <NXOpen/Annotations_CircleCenterline.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class CircularCenterline;
    }
    namespace Annotations
    {
        class CircleCenterline;
    }
    namespace Annotations
    {
        class _CircularCenterlineBuilder;
        class CircularCenterlineImpl;
        /** Represents a CircularCenterline centerline */
        class NXOPENCPPEXPORT  CircularCenterline : public Annotations::CircleCenterline
        {
            private: CircularCenterlineImpl * m_circularcenterline_impl;
            private: friend class  _CircularCenterlineBuilder;
            protected: CircularCenterline();
            public: ~CircularCenterline();
        };
    }
}
#undef EXPORTLIBRARY
#endif
