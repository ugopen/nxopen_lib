#ifndef NXOpen_CAE_RECIPECONVEXMESH_HXX_INCLUDED
#define NXOpen_CAE_RECIPECONVEXMESH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_RecipeConvexMesh.ja
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
        class RecipeConvexMesh;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class _RecipeConvexMeshBuilder;
        class RecipeConvexMeshImpl;
        /** Represents a convex mesh.  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ConvexMeshBuilder  NXOpen::CAE::ConvexMeshBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  RecipeConvexMesh : public NXOpen::CAE::Mesh
        {
            private: RecipeConvexMeshImpl * m_recipeconvexmesh_impl;
            private: friend class  _RecipeConvexMeshBuilder;
            protected: RecipeConvexMesh();
            public: ~RecipeConvexMesh();
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
