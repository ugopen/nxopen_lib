#ifndef NXOpen_CAM_MILLAREAGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MILLAREAGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MillAreaGeomBuilder.ja
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
#include <NXOpen/CAM_MillGeomBuilder.hxx>
#include <NXOpen/CAM_Geometry.hxx>
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
        class MillAreaGeomBuilder;
    }
    namespace CAM
    {
        class Geometry;
    }
    namespace CAM
    {
        class MillGeomBuilder;
    }
    namespace CAM
    {
        class _MillAreaGeomBuilderBuilder;
        class MillAreaGeomBuilderImpl;
        /** Represents a MillAreaGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateMillAreaGeomBuilder  CAM::NCGroupCollection::CreateMillAreaGeomBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MillAreaGeomBuilder : public CAM::MillGeomBuilder
        {
            private: MillAreaGeomBuilderImpl * m_millareageombuilder_impl;
            private: friend class  _MillAreaGeomBuilderBuilder;
            protected: MillAreaGeomBuilder();
            public: ~MillAreaGeomBuilder();
            /**Returns  the cut area geometry builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Geometry * CutAreaGeometry
            (
            );
            /**Returns  the wall geometry builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Geometry * WallGeometry
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