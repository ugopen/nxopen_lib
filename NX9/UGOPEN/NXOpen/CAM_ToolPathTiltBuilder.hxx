#ifndef NXOpen_CAM_TOOLPATHTILTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TOOLPATHTILTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ToolPathTiltBuilder.ja
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
#include <NXOpen/Builder.hxx>
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
        class ToolPathTiltBuilder;
    }
    class Builder;
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    namespace CAM
    {
        class ToolPathTiltAvoidance;
    }
    namespace CAM
    {
        class ToolPathTiltClearance;
    }
    namespace CAM
    {
        class ToolPathTiltMachine;
    }
    namespace CAM
    {
        class ToolPathTiltTilting;
    }
    namespace CAM
    {
        class _ToolPathTiltBuilderBuilder;
        class ToolPathTiltBuilderImpl;
        /** Represents a Tool Path Tilt Builder  <br> To create a new instance of this class, use @link CAM::CAMSetup::CreateToolPathTiltBuilder  CAM::CAMSetup::CreateToolPathTiltBuilder @endlink  <br> 
         <br>  Created in NX7.5.2.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ToolPathTiltBuilder : public Builder
        {
            private: ToolPathTiltBuilderImpl * m_toolpathtiltbuilder_impl;
            private: friend class  _ToolPathTiltBuilderBuilder;
            protected: ToolPathTiltBuilder();
            public: ~ToolPathTiltBuilder();
            /**Returns  the fan distance 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltAvoidance::FanDistance NXOpen::CAM::ToolPathTiltAvoidance::FanDistance@endlink  instead. <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltAvoidance::FanDistance instead.") NXOpen::CAM::InheritableToolDepBuilder * FanDistance
            (
            );
            /**Returns  the maximum tilt angle 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltMachine::MaxTiltAngle NXOpen::CAM::ToolPathTiltMachine::MaxTiltAngle@endlink  instead. <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltMachine::MaxTiltAngle instead.") double MaxTiltAngle
            (
            );
            /**Sets  the maximum tilt angle 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltMachine::MaxTiltAngle NXOpen::CAM::ToolPathTiltMachine::MaxTiltAngle@endlink  instead. <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltMachine::MaxTiltAngle instead.") void SetMaxTiltAngle
            (
                double maxTiltangle /** the value of maximal tilt angle */
            );
            /**Returns  the tool axis change 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltMachine::MaxToolAxisChange NXOpen::CAM::ToolPathTiltMachine::MaxToolAxisChange@endlink  instead. <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltMachine::MaxToolAxisChange instead.") double ToolAxisChange
            (
            );
            /**Sets  the tool axis change 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltMachine::MaxToolAxisChange NXOpen::CAM::ToolPathTiltMachine::MaxToolAxisChange@endlink  instead. <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltMachine::MaxToolAxisChange instead.") void SetToolAxisChange
            (
                double toolaxisChange /** the value of maximum tool axis change */
            );
            /**Returns  the minimum safeclearance 
             <br>  @deprecated Deprecated in NX8.0.0.  Use @link NXOpen::CAM::ToolPathTiltBuilder::MinHolderClearance NXOpen::CAM::ToolPathTiltBuilder::MinHolderClearance@endlink  instead. <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use NXOpen::CAM::ToolPathTiltBuilder::MinHolderClearance instead.") NXOpen::CAM::InheritableToolDepBuilder * MinSafeClearance
            (
            );
            /**Returns  the minimum holder clearance 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltClearance::MinHolderClearance NXOpen::CAM::ToolPathTiltClearance::MinHolderClearance@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltClearance::MinHolderClearance instead.") NXOpen::CAM::InheritableToolDepBuilder * MinHolderClearance
            (
            );
            /**Returns  the minimum shank clearance 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltClearance::MinShankClearance NXOpen::CAM::ToolPathTiltClearance::MinShankClearance@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltClearance::MinShankClearance instead.") NXOpen::CAM::InheritableToolDepBuilder * MinShankClearance
            (
            );
            /**Returns  the minimum neck clearance 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltClearance::MinNeckClearance NXOpen::CAM::ToolPathTiltClearance::MinNeckClearance@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltClearance::MinNeckClearance instead.") NXOpen::CAM::InheritableToolDepBuilder * MinNeckClearance
            (
            );
            /**Returns  the preferred tilt angle 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltAvoidance::PreferredTiltAngle NXOpen::CAM::ToolPathTiltAvoidance::PreferredTiltAngle@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltAvoidance::PreferredTiltAngle instead.") double PreferredTiltAngle
            (
            );
            /**Sets  the preferred tilt angle 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltAvoidance::PreferredTiltAngle NXOpen::CAM::ToolPathTiltAvoidance::PreferredTiltAngle@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltAvoidance::PreferredTiltAngle instead.") void SetPreferredTiltAngle
            (
                double preferredAngle /** the value of preferred tilt angle */
            );
            /**Returns  the maintain tilt 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltAvoidance::MaintainTilt NXOpen::CAM::ToolPathTiltAvoidance::MaintainTilt@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltAvoidance::MaintainTilt instead.") bool MaintainTilt
            (
            );
            /**Sets  the maintain tilt 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltAvoidance::MaintainTilt NXOpen::CAM::ToolPathTiltAvoidance::MaintainTilt@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltAvoidance::MaintainTilt instead.") void SetMaintainTilt
            (
                bool maintainTilt /** the value of maintain tilt */
            );
            /**Returns  the max maintain tilt distance 
             <br>  @deprecated Deprecated in NX9.0.0.  Use @link NXOpen::CAM::ToolPathTiltAvoidance::MaxMaintainTiltDistance NXOpen::CAM::ToolPathTiltAvoidance::MaxMaintainTiltDistance@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use NXOpen::CAM::ToolPathTiltAvoidance::MaxMaintainTiltDistance instead.") NXOpen::CAM::InheritableToolDepBuilder * MaxMaintainTiltDistance
            (
            );
            /**Returns  the clearance builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolPathTiltClearance * TiltClearance
            (
            );
            /**Returns  the machine builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolPathTiltMachine * TiltMachine
            (
            );
            /**Returns  the avoidance builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolPathTiltAvoidance * TiltAvoidance
            (
            );
            /**Returns  the tilting builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ToolPathTiltTilting * TiltTilting
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
