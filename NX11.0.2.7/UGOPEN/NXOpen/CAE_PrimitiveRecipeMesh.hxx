#ifndef NXOpen_CAE_PRIMITIVERECIPEMESH_HXX_INCLUDED
#define NXOpen_CAE_PRIMITIVERECIPEMESH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PrimitiveRecipeMesh.ja
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
        class PrimitiveRecipeMesh;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class _PrimitiveRecipeMeshBuilder;
        class PrimitiveRecipeMeshImpl;
        /** Represents a primitive recipe mesh.  <br> To create or edit an instance of this class, use @link NXOpen::CAE::PrimitiveRecipeMeshBuilder  NXOpen::CAE::PrimitiveRecipeMeshBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PrimitiveRecipeMesh : public NXOpen::CAE::Mesh
        {
            private: PrimitiveRecipeMeshImpl * m_primitiverecipemesh_impl;
            private: friend class  _PrimitiveRecipeMeshBuilder;
            protected: PrimitiveRecipeMesh();
            public: ~PrimitiveRecipeMesh();
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