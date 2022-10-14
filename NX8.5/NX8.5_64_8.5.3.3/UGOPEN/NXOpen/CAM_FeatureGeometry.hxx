#ifndef NXOpen_CAM_FEATUREGEOMETRY_HXX_INCLUDED
#define NXOpen_CAM_FEATUREGEOMETRY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FeatureGeometry.ja
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
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class FeatureGeometry;
    }
    namespace CAM
    {
        class NCGroup;
    }
    namespace CAM
    {
        class _FeatureGeometryBuilder;
        class FeatureGeometryImpl;
        /** Represents a  Base Geometry Group <br> To create or edit an instance of this class, use @link CAM::FeatureGeomBuilder  CAM::FeatureGeomBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  FeatureGeometry : public CAM::NCGroup
        {
            private: FeatureGeometryImpl * m_featuregeometry_impl;
            private: friend class  _FeatureGeometryBuilder;
            protected: FeatureGeometry();
            public: ~FeatureGeometry();
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