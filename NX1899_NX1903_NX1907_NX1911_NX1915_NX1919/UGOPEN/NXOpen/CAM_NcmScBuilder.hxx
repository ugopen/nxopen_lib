#ifndef NXOpen_CAM_NCMSCBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NCMSCBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmScBuilder.ja
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
#include <NXOpen/CAM_NcmSubopBuilder.hxx>
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
        class NcmScBuilder;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    namespace CAM
    {
        class NcmAvoidancePointBuilder;
    }
    namespace CAM
    {
        class NcmClearanceBuilder;
    }
    namespace CAM
    {
        class NcmScEngRetBuilder;
    }
    namespace CAM
    {
        class NcmSmoothingBuilder;
    }
    namespace CAM
    {
        class NcmSubopBuilder;
    }
    namespace CAM
    {
        class NcmTransferBuilder;
    }
    namespace CAM
    {
        class _NcmScBuilderBuilder;
        class NcmScBuilderImpl;
        /**
            Represents a @link NXOpen::CAM::NcmScBuilder NXOpen::CAM::NcmScBuilder@endlink 
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  NcmScBuilder : public NXOpen::CAM::NcmSubopBuilder
        {
            /** Available options for smoothing behavior */
            public: enum SmoothingOptions
            {
                SmoothingOptionsOn/** transfer smoothing activated */,
                SmoothingOptionsOff/** transfer smoothing deactivated */
            };

            private: NcmScBuilderImpl * m_ncmscbuilder_impl;
            private: friend class  _NcmScBuilderBuilder;
            protected: NcmScBuilder();
            public: ~NcmScBuilder();
            /**Returns  the open area engage settings 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmScEngRetBuilder * EngageOpenAreaBuilder
            (
            );
            /**Returns  the against check engage settings 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmScEngRetBuilder * EngageAgainstCheckBuilder
            (
            );
            /**Returns  the initial engage settings 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmScEngRetBuilder * EngageInitialBuilder
            (
            );
            /**Returns  the open area retract settings 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmScEngRetBuilder * RetractOpenAreaBuilder
            (
            );
            /**Returns  the against check retract settings 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmScEngRetBuilder * RetractAgainstCheckBuilder
            (
            );
            /**Returns  the final retract settings 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmScEngRetBuilder * RetractFinalBuilder
            (
            );
            /**Returns  the region distance setting 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferRegionDistanceBuilder
            (
            );
            /**Returns  the part safe clearance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * PartSafeClearance
            (
            );
            /**Returns  the common clearance setting 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmClearanceBuilder * TransferCommonClearanceBuilder
            (
            );
            /**Returns  the transfer settings for within regions 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmTransferBuilder * TransferWithinRegionsBuilder
            (
            );
            /**Returns  the transfer settings for between regions 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmTransferBuilder * TransferBetweenRegionsBuilder
            (
            );
            /**Returns  the transfer settings for initial and final 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmTransferBuilder * TransferInitialFinalBuilder
            (
            );
            /**Returns  the max stepover setting 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * MaxStepoverBuilder
            (
            );
            /**Returns  the smoothing option 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::NcmScBuilder::SmoothingBuilder NXOpen::CAM::NcmScBuilder::SmoothingBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::NcmScBuilder::SmoothingBuilder instead.") NXOpen::CAM::NcmScBuilder::SmoothingOptions SmoothingOption
            (
            );
            /**Sets  the smoothing option 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::NcmScBuilder::SmoothingBuilder NXOpen::CAM::NcmScBuilder::SmoothingBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::NcmScBuilder::SmoothingBuilder instead.") void SetSmoothingOption
            (
                NXOpen::CAM::NcmScBuilder::SmoothingOptions newValue /** newvalue */ 
            );
            /**Returns  the max tool axis change 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::NcmScBuilder::SmoothingBuilder NXOpen::CAM::NcmScBuilder::SmoothingBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::NcmScBuilder::SmoothingBuilder instead.") double MaxToolAxisChange
            (
            );
            /**Sets  the max tool axis change 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::NcmScBuilder::SmoothingBuilder NXOpen::CAM::NcmScBuilder::SmoothingBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::NcmScBuilder::SmoothingBuilder instead.") void SetMaxToolAxisChange
            (
                double newValue /** the max tool axis change */
            );
            /**Returns  the smoothing radius settings 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::NcmScBuilder::SmoothingBuilder NXOpen::CAM::NcmScBuilder::SmoothingBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::NcmScBuilder::SmoothingBuilder instead.") NXOpen::CAM::InheritableToolDepBuilder * SmoothingRadiusBuilder
            (
            );
            /**Returns  the from point builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceFromBuilder
            (
            );
            /**Returns  the start point builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceStartBuilder
            (
            );
            /**Returns  the return point builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceReturnBuilder
            (
            );
            /**Returns  the gohome point builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceGohomeBuilder
            (
            );
            /**Returns  the smoothing builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmSmoothingBuilder * SmoothingBuilder
            (
            );
            /**Returns  the collision check activation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool CollisionCheck
            (
            );
            /**Sets  the collision check activation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCollisionCheck
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the contact data output activation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool OutputContactData
            (
            );
            /**Sets  the contact data output activation 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOutputContactData
            (
                bool newValue /** newvalue */ 
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
