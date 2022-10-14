#ifndef NXOpen_CAM_MILLBOUNDARYGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MILLBOUNDARYGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MillBoundaryGeomBuilder.ja
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
#include <NXOpen/CAM_FeatureGeomBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MillBoundaryGeomBuilder;
    }
    namespace CAM
    {
        class FeatureGeomBuilder;
    }
    namespace CAM
    {
        class _MillBoundaryGeomBuilderBuilder;
        class MillBoundaryGeomBuilderImpl;
        /** Represents a MillBoundaryGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateMillBoundaryGeomBuilder CAM::NCGroupCollection::CreateMillBoundaryGeomBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  MillBoundaryGeomBuilder : public CAM::FeatureGeomBuilder
        {
            private: MillBoundaryGeomBuilderImpl * m_millboundarygeombuilder_impl;
            private: friend class  _MillBoundaryGeomBuilderBuilder;
            protected: MillBoundaryGeomBuilder();
            public: ~MillBoundaryGeomBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif