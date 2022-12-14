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
#include <NXOpen/CAM_Boundary.hxx>
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
        class MillBoundaryGeomBuilder;
    }
    namespace CAM
    {
        class Boundary;
    }
    namespace CAM
    {
        class FeatureGeomBuilder;
    }
    namespace CAM
    {
        class _MillBoundaryGeomBuilderBuilder;
        class MillBoundaryGeomBuilderImpl;
        /** Represents a MillBoundaryGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateMillBoundaryGeomBuilder  CAM::NCGroupCollection::CreateMillBoundaryGeomBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MillBoundaryGeomBuilder : public CAM::FeatureGeomBuilder
        {
            private: MillBoundaryGeomBuilderImpl * m_millboundarygeombuilder_impl;
            private: friend class  _MillBoundaryGeomBuilderBuilder;
            protected: MillBoundaryGeomBuilder();
            public: ~MillBoundaryGeomBuilder();
            /**Returns  the part boundary 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Boundary * PartBoundary
            (
            );
            /**Returns  the blank boundary 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Boundary * BlankBoundary
            (
            );
            /**Returns  the check boundary 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Boundary * CheckBoundary
            (
            );
            /**Returns  the trim boundary 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Boundary * TrimBoundary
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
