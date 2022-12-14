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
        /** Represents a CircularCenterline centerline  <br> To create or edit an instance of this class, use @link NXOpen::Annotations::CircularCenterlineBuilder  NXOpen::Annotations::CircularCenterlineBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  CircularCenterline : public NXOpen::Annotations::CircleCenterline
        {
            private: CircularCenterlineImpl * m_circularcenterline_impl;
            private: friend class  _CircularCenterlineBuilder;
            protected: CircularCenterline();
            public: ~CircularCenterline();
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
