#ifndef NXOpen_DISPLAY_TRUESHADING_HXX_INCLUDED
#define NXOpen_DISPLAY_TRUESHADING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_TrueShading.ja
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
#include <NXOpen/libnxopencpp_display_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Display
    {
        class TrueShading;
    }
    class NXObject;
    namespace Display
    {
        class _TrueShadingBuilder;
        class TrueShadingImpl;
        /** Represents a True Shading object  <br> TrueShading is not supported in KF.  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  TrueShading : public NXOpen::NXObject
        {
            private: TrueShadingImpl * m_trueshading_impl;
            private: friend class  _TrueShadingBuilder;
            protected: TrueShading();
            public: ~TrueShading();
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
