#ifndef NXOpen_CAM_FEEDSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_FEEDSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_FeedsBuilder.ja
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
        class FeedsBuilder;
    }
    namespace CAM
    {
        class FeedsOptimizationData;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class InheritableFeedBuilder;
    }
    namespace CAM
    {
        class InheritableFeedModeBuilder;
    }
    namespace CAM
    {
        class InheritableIntBuilder;
    }
    namespace CAM
    {
        class InheritableTextBuilder;
    }
    namespace CAM
    {
        class _FeedsBuilderBuilder;
        class FeedsBuilderImpl;
        /** Represents a feeds Builder 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  FeedsBuilder : public NXOpen::TaggedObject
        {
            /** The recalculation based on attribute
             <br>  Created in NX8.0.0.  <br>  
            */
            public: enum RecalcuateBasedOn
            {
                RecalcuateBasedOnSurfaceSpeed/** surface speed*/,
                RecalcuateBasedOnSpindleSpeed/** spindle speed*/,
                RecalcuateBasedOnFeedPerTooth/** feed per tooth*/,
                RecalcuateBasedOnCutFeedRate/** cut feed rate*/
            };

            private: FeedsBuilderImpl * m_feedsbuilder_impl;
            private: friend class  _FeedsBuilderBuilder;
            protected: FeedsBuilder();
            public: ~FeedsBuilder();
            /**Returns  the surface_speed builder (inheritable Double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * SurfaceSpeedBuilder
            (
            );
            /**Returns  the feed_per_tooth builder (inheritable Double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * FeedPerToothBuilder
            (
            );
            /**Returns  the spindle_rpm builder (inheritable Double) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * SpindleRpmBuilder
            (
            );
            /**Returns  the spindle_mode builder (inheritable Int) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableIntBuilder * SpindleModeBuilder
            (
            );
            /**Returns  the tool_direction builder (inheritable Int) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableIntBuilder * ToolDirectionBuilder
            (
            );
            /**Returns  the spindle_range builder (inheritable Text) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableTextBuilder * SpindleRangeBuilder
            (
            );
            /**Returns  the spindle_text builder (inheritable Text) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableTextBuilder * SpindleTextBuilder
            (
            );
            /**Returns  the feed_rapid builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedRapidBuilder
            (
            );
            /**Returns  the feed_approach builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedApproachBuilder
            (
            );
            /**Returns  the feed_engage builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedEngageBuilder
            (
            );
            /**Returns  the feed_first_cut builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedFirstCutBuilder
            (
            );
            /**Returns  the feed_last_cut builder (inheritable Feed) 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedLastCutBuilder
            (
            );
            /**Returns  the feed_stepover builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedStepoverBuilder
            (
            );
            /**Returns  the feed_crossover builder (inheritable Feed) 
             <br>  Created in NX10.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedCrossoverBuilder
            (
            );
            /**Returns  the feed_cut builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedCutBuilder
            (
            );
            /**Returns  the feed_traversal builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedTraversalBuilder
            (
            );
            /**Returns  the feed_retract builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedRetractBuilder
            (
            );
            /**Returns  the feed_departure builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedDepartureBuilder
            (
            );
            /**Returns  the feed_return builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedReturnBuilder
            (
            );
            /**Returns  the feed_side_cut builder (inheritable Feed) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedBuilder * FeedSideCutBuilder
            (
            );
            /** Set machining data 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMachiningData
            (
            );
            /**Returns  the optimize feed rate when generating 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool OptimizeFeedRateWhenGenerating
            (
            );
            /**Sets  the optimize feed rate when generating 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOptimizeFeedRateWhenGenerating
            (
                bool isOptimize /** is optimize */ 
            );
            /**Returns  the feeds optimize data 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::FeedsOptimizationData * FeedsOptimizationData
            (
            );
            /**Returns  the spindle_rpm_toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int SpindleRpmToggle
            (
            );
            /**Sets  the spindle_rpm_toggle 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSpindleRpmToggle
            (
                int status /** the spindle rpm toggle status */
            );
            /**Returns  the feed rapid output builder (inheritable Enum) 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableFeedModeBuilder * FeedRapidOutput
            (
            );
            /** Recalculate speeds and feeds 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void RecalculateData
            (
                NXOpen::CAM::FeedsBuilder::RecalcuateBasedOn type /** the recalculation based on attribute */
            );
            /**Returns  the Laser Pierce Power 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * PierceLaserPower
            (
            );
            /**Returns  the Laser Pierce Frequency 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * PierceLaserFrequency
            (
            );
            /**Returns  the Laser Pierce Delay 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * PierceLaserDelay
            (
            );
            /**Returns  the Pierce Gas Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableIntBuilder * PierceGasType
            (
            );
            /**Returns  the Pierce Gas Pressure 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * PierceGasPressure
            (
            );
            /**Returns  the Laser Cut Power 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * CutLaserPower
            (
            );
            /**Returns  the Laser Cut Frequency 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * CutLaserFrequency
            (
            );
            /**Returns  the Laser Cut Delay 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * CutLaserDelay
            (
            );
            /**Returns  the Cut Gas Type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableIntBuilder * CutGasType
            (
            );
            /**Returns  the Cut Gas Pressure 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * CutGasPressure
            (
            );
            /**Returns  the Retract Speed Toggle 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int RetractSpeedToggle
            (
            );
            /**Sets  the Retract Speed Toggle 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractSpeedToggle
            (
                int status /** the retract spindle  toggle status */
            );
            /**Returns  the Retract Speed 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableDoubleBuilder * RetractSpeed
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