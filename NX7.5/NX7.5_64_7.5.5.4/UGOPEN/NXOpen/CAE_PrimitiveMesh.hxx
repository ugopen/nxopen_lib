#ifndef NXOpen_CAE_PRIMITIVEMESH_HXX_INCLUDED
#define NXOpen_CAE_PRIMITIVEMESH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PrimitiveMesh.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class PrimitiveMesh;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class _PrimitiveMeshBuilder;
        class PrimitiveMeshImpl;
        /** Represents Primitive Mesh */
        class NXOPENCPPEXPORT  PrimitiveMesh : public CAE::Mesh
        {
            private: PrimitiveMeshImpl * m_primitivemesh_impl;
            private: friend class  _PrimitiveMeshBuilder;
            protected: PrimitiveMesh();
            public: ~PrimitiveMesh();
        };
    }
}
#undef EXPORTLIBRARY
#endif