#ifndef NXOpen_CAE_RECIPESURFACEWRAP_HXX_INCLUDED
#define NXOpen_CAE_RECIPESURFACEWRAP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_RecipeSurfaceWrap.ja
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
#include <NXOpen/CAE_Mesh.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class RecipeSurfaceWrap;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class _RecipeSurfaceWrapBuilder;
        class RecipeSurfaceWrapImpl;
        /** Represents 2d mesh associated to fluid domain body, all from surface wrapper.  <br> To create or edit an instance of this class, use @link NXOpen::CAE::FluidDomainBuilder  NXOpen::CAE::FluidDomainBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  RecipeSurfaceWrap : public NXOpen::CAE::Mesh
        {
            private: RecipeSurfaceWrapImpl * m_recipesurfacewrap_impl;
            private: friend class  _RecipeSurfaceWrapBuilder;
            protected: RecipeSurfaceWrap();
            public: ~RecipeSurfaceWrap();
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
