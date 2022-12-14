#ifndef NXOpen_CAE_SWEPTMESH_HXX_INCLUDED
#define NXOpen_CAE_SWEPTMESH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SweptMesh.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAE_Mesh.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class SweptMesh;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class _SweptMeshBuilder;
        /** Represents swept Mesh */
        class NXOPENCPPEXPORT SweptMesh : public CAE::Mesh
        {
            private: friend class  _SweptMeshBuilder;
            protected: SweptMesh();
        };
    }
}
#undef EXPORTLIBRARY
#endif
