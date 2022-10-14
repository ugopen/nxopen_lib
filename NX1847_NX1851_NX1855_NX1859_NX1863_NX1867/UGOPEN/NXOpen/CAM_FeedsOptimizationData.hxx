#ifndef NXOpen_CAM_FEEDSOPTIMIZATIONDATA_HXX_INCLUDED
#define NXOpen_CAM_FEEDSOPTIMIZATIONDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FeedsOptimizationData.ja
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
#include <NXOpen/TaggedObject.hxx>
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
        class FeedsOptimizationData;
    }
    namespace CAM
    {
        class _FeedsOptimizationDataBuilder;
        class FeedsOptimizationDataImpl;
        /**
            Represents a @link NXOpen::CAM::FeedsOptimizationData NXOpen::CAM::FeedsOptimizationData@endlink 
            
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  FeedsOptimizationData : public NXOpen::TaggedObject
        {
            /** The Feed Rate Range options */
            public: enum FeedRateRangeType
            {
                FeedRateRangeTypePercent/** Percent */,
                FeedRateRangeTypeConstant/** Constant*/
            };

            private: FeedsOptimizationDataImpl * m_feedsoptimizationdata_impl;
            private: friend class  _FeedsOptimizationDataBuilder;
            protected: FeedsOptimizationData();
            public: ~FeedsOptimizationData();
            /**Returns  the nominal stepover 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double NominalStepover
            (
            );
            /**Sets  the nominal stepover 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetNominalStepover
            (
                double nominalStepover /** nominalstepover */ 
            );
            /**Returns  the nominal depth per cut 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double NominalDepthPerCut
            (
            );
            /**Sets  the nominal depth per cut 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetNominalDepthPerCut
            (
                double nominalDepthPerCut /** nominaldepthpercut */ 
            );
            /**Returns  the feed rate range 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::FeedsOptimizationData::FeedRateRangeType FeedRateRange
            (
            );
            /**Sets  the feed rate range 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFeedRateRange
            (
                NXOpen::CAM::FeedsOptimizationData::FeedRateRangeType feedRateRange /** feedraterange */ 
            );
            /**Returns  the percent of lower limit 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double PercentLowerLimit
            (
            );
            /**Sets  the percent of lower limit 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPercentLowerLimit
            (
                double lowerLimit /** lowerlimit */ 
            );
            /**Returns  the percent of upper limit 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double PercentUpperLimit
            (
            );
            /**Sets  the percent of upper limit 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPercentUpperLimit
            (
                double upperLimit /** upperlimit */ 
            );
            /**Returns  the constant lower limit 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double ConstantLowerLimit
            (
            );
            /**Sets  the constant lower limit 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetConstantLowerLimit
            (
                double lowerLimit /** lowerlimit */ 
            );
            /**Returns  the constant upper limit 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double ConstantUpperLimit
            (
            );
            /**Sets  the constant upper limit 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetConstantUpperLimit
            (
                double upperLimit /** upperlimit */ 
            );
            /**Returns  the length interval 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double LengthInterval
            (
            );
            /**Sets  the length interval 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLengthInterval
            (
                double lengthInterval /** lengthinterval */ 
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