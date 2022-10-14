#ifndef NXOpen_SAFETY_SURFACE_HXX_INCLUDED
#define NXOpen_SAFETY_SURFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Safety_Surface.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libsafetyopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Safety
    {
        class Surface;
    }
    class DisplayableObject;
    namespace Safety
    {
        class _SurfaceBuilder;
        class SurfaceImpl;
        /**  Represents the Safety Surface.     <br> To create or edit an instance of this class, use @link NXOpen::Safety::SurfaceBuilder  NXOpen::Safety::SurfaceBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class SAFETYOPENCPPEXPORT  Surface : public NXOpen::DisplayableObject
        {
            private: SurfaceImpl * m_surface_impl;
            private: friend class  _SurfaceBuilder;
            protected: Surface();
            public: ~Surface();
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