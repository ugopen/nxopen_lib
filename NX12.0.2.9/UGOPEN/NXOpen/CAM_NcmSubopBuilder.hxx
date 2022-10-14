#ifndef NXOpen_CAM_NCMSUBOPBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NCMSUBOPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmSubopBuilder.ja
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
#include <NXOpen/CAM_BaseBuilder.hxx>
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
        class NcmSubopBuilder;
    }
    namespace CAM
    {
        class BaseBuilder;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    class Point;
    namespace CAM
    {
        class _NcmSubopBuilderBuilder;
        class NcmSubopBuilderImpl;
        /**
            Represents a @link NXOpen::CAM::NcmSubopBuilder NXOpen::CAM::NcmSubopBuilder@endlink 
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  NcmSubopBuilder : public NXOpen::CAM::BaseBuilder
        {
            /** Available types for default region start in subop milling */
            public: enum DefaultRegionStartTypes
            {
                DefaultRegionStartTypesMidPoint/** start at mid point */,
                DefaultRegionStartTypesCorner/** start_at_corners */
            };

            private: NcmSubopBuilderImpl * m_ncmsubopbuilder_impl;
            private: friend class  _NcmSubopBuilderBuilder;
            protected: NcmSubopBuilder();
            public: ~NcmSubopBuilder();
            /**Returns  the region start type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmSubopBuilder::DefaultRegionStartTypes DefaultRegionStartType
            (
            );
            /**Sets  the region start type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDefaultRegionStartType
            (
                NXOpen::CAM::NcmSubopBuilder::DefaultRegionStartTypes defaultRegionStartType /** defaultregionstarttype */ 
            );
            /** Returns region start points 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void GetRegionStartPoints
            (
                std::vector<NXOpen::Point *> & regionStartPoints /** The points */
            );
            /** Sets region start points 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRegionStartPoints
            (
                const std::vector<NXOpen::Point *> & regionStartPoints /** The points */
            );
            /**Returns  the start points use effective distance 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool StartPointsUseEffectDist
            (
            );
            /**Sets  the start points use effective distance 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStartPointsUseEffectDist
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the region start points effective distance builder (inheritable tool dep) 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * StartPointsEffectDistBuilder
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