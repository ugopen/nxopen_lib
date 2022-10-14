#ifndef NXOpen_CAM_MILLGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MILLGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MillGeomBuilder.ja
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
#include <NXOpen/CAM_Geometry.hxx>
#include <NXOpen/CAM_GeometryGroup.hxx>
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
        class MillGeomBuilder;
    }
    namespace CAM
    {
        class FeatureGeomBuilder;
    }
    namespace CAM
    {
        class Geometry;
    }
    namespace CAM
    {
        class GeometryGroup;
    }
    namespace CAM
    {
        class _MillGeomBuilderBuilder;
        class MillGeomBuilderImpl;
        /** Represents a MillGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateMillGeomBuilder  CAM::NCGroupCollection::CreateMillGeomBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MillGeomBuilder : public CAM::FeatureGeomBuilder
        {
            private: MillGeomBuilderImpl * m_millgeombuilder_impl;
            private: friend class  _MillGeomBuilderBuilder;
            protected: MillGeomBuilder();
            public: ~MillGeomBuilder();
            /**Returns  the part geometry builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Geometry * PartGeometry
            (
            );
            /**Returns  the blank geometry builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::GeometryGroup * BlankGeometry
            (
            );
            /**Returns  the check geometry builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Geometry * CheckGeometry
            (
            );
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