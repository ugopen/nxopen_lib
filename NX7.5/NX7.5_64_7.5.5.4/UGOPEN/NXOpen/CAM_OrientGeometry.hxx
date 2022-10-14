#ifndef NXOpen_CAM_ORIENTGEOMETRY_HXX_INCLUDED
#define NXOpen_CAM_ORIENTGEOMETRY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_OrientGeometry.ja
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
#include <NXOpen/CAM_NCGroup.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class OrientGeometry;
    }
    namespace CAM
    {
        class NCGroup;
    }
    namespace CAM
    {
        class _OrientGeometryBuilder;
        class OrientGeometryImpl;
        /** Represents a Orient Group*/
        class NXOPENCPPEXPORT  OrientGeometry : public CAM::NCGroup
        {
            private: OrientGeometryImpl * m_orientgeometry_impl;
            private: friend class  _OrientGeometryBuilder;
            protected: OrientGeometry();
            public: ~OrientGeometry();
        };
    }
}
#undef EXPORTLIBRARY
#endif