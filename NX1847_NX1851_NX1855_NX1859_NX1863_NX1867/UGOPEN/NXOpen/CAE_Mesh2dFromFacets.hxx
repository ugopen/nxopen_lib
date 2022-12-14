#ifndef NXOpen_CAE_MESH2DFROMFACETS_HXX_INCLUDED
#define NXOpen_CAE_MESH2DFROMFACETS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Mesh2dFromFacets.ja
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
        class Mesh2dFromFacets;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class _Mesh2dFromFacetsBuilder;
        class Mesh2dFromFacetsImpl;
        /** Represents 2d Mesh From Facets  <br> This is an abstract class  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  Mesh2dFromFacets : public NXOpen::CAE::Mesh
        {
            private: Mesh2dFromFacetsImpl * m_mesh2dfromfacets_impl;
            private: friend class  _Mesh2dFromFacetsBuilder;
            protected: Mesh2dFromFacets();
            public: ~Mesh2dFromFacets();
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
