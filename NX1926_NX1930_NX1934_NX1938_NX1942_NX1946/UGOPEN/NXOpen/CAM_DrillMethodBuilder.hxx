#ifndef NXOpen_CAM_DRILLMETHODBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DRILLMETHODBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DrillMethodBuilder.ja
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
#include <NXOpen/CAM_MethodBuilder.hxx>
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
        class DrillMethodBuilder;
    }
    namespace CAM
    {
        class FeedsBuilder;
    }
    namespace CAM
    {
        class MethodBuilder;
    }
    namespace CAM
    {
        class _DrillMethodBuilderBuilder;
        class DrillMethodBuilderImpl;
        /** Represents a Drill Method Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::NCGroupCollection::CreateDrillMethodBuilder  NXOpen::CAM::NCGroupCollection::CreateDrillMethodBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  DrillMethodBuilder : public NXOpen::CAM::MethodBuilder
        {
            private: DrillMethodBuilderImpl * m_drillmethodbuilder_impl;
            private: friend class  _DrillMethodBuilderBuilder;
            protected: DrillMethodBuilder();
            public: ~DrillMethodBuilder();
            /**Returns  the feeds builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::FeedsBuilder * FeedsBuilder
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