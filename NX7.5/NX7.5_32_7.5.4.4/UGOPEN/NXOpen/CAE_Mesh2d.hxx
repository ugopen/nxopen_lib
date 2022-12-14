#ifndef NXOpen_CAE_MESH2D_HXX_INCLUDED
#define NXOpen_CAE_MESH2D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Mesh2d.ja
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
        class Mesh2d;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class _Mesh2dBuilder;
        class Mesh2dImpl;
        /** Represents 2d Mesh  <br> This is an abstract class <br> */
        class NXOPENCPPEXPORT  Mesh2d : public CAE::Mesh
        {
            private: Mesh2dImpl * m_mesh2d_impl;
            private: friend class  _Mesh2dBuilder;
            protected: Mesh2d();
            public: ~Mesh2d();
        };
    }
}
#undef EXPORTLIBRARY
#endif
