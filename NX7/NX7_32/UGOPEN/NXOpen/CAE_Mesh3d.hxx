#ifndef NXOpen_CAE_MESH3D_HXX_INCLUDED
#define NXOpen_CAE_MESH3D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Mesh3d.ja
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
        class Mesh3d;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class _Mesh3dBuilder;
        /** Represents 3d Mesh */
        class NXOPENCPPEXPORT Mesh3d : public CAE::Mesh
        {
            private: friend class  _Mesh3dBuilder;
            protected: Mesh3d();
        };
    }
}
#undef EXPORTLIBRARY
#endif
