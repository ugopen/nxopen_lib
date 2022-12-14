#ifndef NXOpen_CAM_CENTERLINEDRILLTURNINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_CENTERLINEDRILLTURNINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CenterlineDrillTurningBuilder.ja
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
#include <NXOpen/CAM_TurningOperationBuilder.hxx>
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
        class CenterlineDrillTurningBuilder;
    }
    namespace CAM
    {
        class CenterlineDrillVariableIncrementBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class NcmTurningBuilder;
    }
    namespace CAM
    {
        class TurningOperationBuilder;
    }
    class NXObject;
    class Point;
    namespace CAM
    {
        class _CenterlineDrillTurningBuilderBuilder;
        class CenterlineDrillTurningBuilderImpl;
        /** Represents a CenterlineDrillTurningBuilder  <br> To create a new instance of this class, use @link NXOpen::CAM::OperationCollection::CreateCenterlineDrillTurningBuilder  NXOpen::CAM::OperationCollection::CreateCenterlineDrillTurningBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  CenterlineDrillTurningBuilder : public NXOpen::CAM::TurningOperationBuilder
        {
            /** the dwell modes
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum DwellTypes
            {
                DwellTypesNone/** Dwell: None */,
                DwellTypesTime/** Dwell: Time */,
                DwellTypesRevolutions/** Dwell: Revolutions */
            };

            /** the spindle stop types
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum SpindleStopTypes
            {
                SpindleStopTypesNone/** Spindle stop: None */,
                SpindleStopTypesBeforeRetract/** Spindle stop: Before retract */
            };

            /** the start position
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum StartPositionTypes
            {
                StartPositionTypesAutomatic/** Start Position: Automatic */,
                StartPositionTypesSpecify/** Start Position: Specify */
            };

            /** the depth option types 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum DepthTypes
            {
                DepthTypesDistance/** Depth options: Distance */,
                DepthTypesEndPoint/** Depth options: End Point */,
                DepthTypesCrossHoleDimensions/** Depth options: Cross Hole Dimensions */,
                DepthTypesCrossHole/** Depth options: Cross Hole */,
                DepthTypesShoulderDepth/** obsolete       Shoulder Depth */,
                DepthTypesCountersinkDiameter/** Depth options: Countersink Diameter */
            };

            /** the depth reference option types 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: enum DepthReferenceTypes
            {
                DepthReferenceTypesToolTip/** Depth Reference options: Tool Tip */,
                DepthReferenceTypesToolShoulder/** Depth Reference options: Tool Shoulder */,
                DepthReferenceTypesCycleTrackingPoint/** Depth Reference options: Cycle Tracking Point */
            };

            /** the drilling location 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum DrillingLocationTypes
            {
                DrillingLocationTypesOnCenterline/** Drilling Location: On centerline */,
                DrillingLocationTypesOffCenterline/** Drilling Location: Off centerline */
            };

            /** the removal increment types 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum RemovalIncrementTypes
            {
                RemovalIncrementTypesConstant/** Removal Increment Type: Constant */,
                RemovalIncrementTypesVariable/** Removal Increment Type: Variable */
            };

            /** the retract types for simulated cycles 
             <br>  Created in NX7.5.0.  <br>  
            */
            public: enum FinalRetractTypes
            {
                FinalRetractTypesToStartPosition/** Final Retract Type: To start position */,
                FinalRetractTypesManual/** Final Retract Type: Manual */
            };

            /** the centerline cycle types
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum CycleTypes
            {
                CycleTypesDrill/** Cycle: Drill */,
                CycleTypesDrillDeep/** Cycle: Drill, Deep */,
                CycleTypesDrillBreakChip/** Cycle: Drill, Break Chip */,
                CycleTypesTap/** Cycle: Tap */,
                CycleTypesTapFloat/** Cycle: Tap, Float */,
                CycleTypesBore/** Cycle: Bore */
            };

            /** the output option 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum OutputOptionTypes
            {
                OutputOptionTypesMachineCycle/** Output Option: Machine Cycle */,
                OutputOptionTypesSimulated/** Output Option: Simulated */
            };

            private: CenterlineDrillTurningBuilderImpl * m_centerlinedrillturningbuilder_impl;
            private: friend class  _CenterlineDrillTurningBuilderBuilder;
            protected: CenterlineDrillTurningBuilder();
            public: ~CenterlineDrillTurningBuilder();
            /**Returns  the entrance diameter 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * EntranceDiameter
            (
            );
            /**Returns  the dwell type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::DwellTypes DwellType
            (
            );
            /**Sets  the dwell type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDwellType
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::DwellTypes dwellMode /** the dwell type */
            );
            /**Returns  the dwell value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * DwellValue
            (
            );
            /**Returns  the spindle stop 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::SpindleStopTypes SpindleStop
            (
            );
            /**Sets  the spindle stop 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSpindleStop
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::SpindleStopTypes spindleStop /** the spindle stop */
            );
            /**Returns  the start position 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::StartPositionTypes StartPosition
            (
            );
            /**Sets  the start position 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStartPosition
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::StartPositionTypes startPositionMode /** the start position mode */
            );
            /**Returns  the start position point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * StartPositionPoint
            (
            );
            /**Sets  the start position point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStartPositionPoint
            (
                NXOpen::Point * startPositionSpecifyPoint /** the start position point */
            );
            /**Returns  the depth option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::DepthTypes DepthOption
            (
            );
            /**Sets  the depth option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDepthOption
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::DepthTypes depthOption /** the depth option */
            );
            /**Returns  the depth distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * DepthDistance
            (
            );
            /**Returns  the depth reference 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::DepthReferenceTypes DepthReference
            (
            );
            /**Sets  the depth reference 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDepthReference
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::DepthReferenceTypes depthReference /** the depth reference */
            );
            /**Returns  the depth offset value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * DepthOffset
            (
            );
            /**Returns  the depth end point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * DepthEndPoint
            (
            );
            /**Sets  the depth end point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDepthEndPoint
            (
                NXOpen::Point * endPoint /** the depth end point */
            );
            /**Returns  the cross hole diameter 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * CrossHoleDiameter
            (
            );
            /**Returns  the cross hole distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * CrossHoleDistance
            (
            );
            /**Returns  the cross hole angle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * CrossHoleAngle
            (
            );
            /**Returns  the cross hole circle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * CrossHoleCircle
            (
            );
            /**Sets  the cross hole circle 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCrossHoleCircle
            (
                NXOpen::NXObject * crossHoleCircle /** the cross hole circle */
            );
            /**Returns  the break through toggle IMPORTANT: Parameter is obsolete from NX9 on and must not be used longer. 
             <br>  @deprecated Deprecated in NX9.0.0.  Use 'depth reference' instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use 'depth reference' instead.") bool BreakThrough
            (
            );
            /**Sets  the break through toggle IMPORTANT: Parameter is obsolete from NX9 on and must not be used longer. 
             <br>  @deprecated Deprecated in NX9.0.0.  Use 'depth reference' instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use 'depth reference' instead.") void SetBreakThrough
            (
                bool breakThroughFlag /** the break through flag value */
            );
            /**Returns  the break through distance IMPORTANT: Parameter is obsolete from NX9 on and must not be used longer. 
             <br>  @deprecated Deprecated in NX9.0.0.  Use 'depth offset' instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Use 'depth offset' instead.") NXOpen::CAM::InheritableDoubleBuilder * BreakThroughDistance
            (
            );
            /**Returns  the drilling location 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::DrillingLocationTypes DrillingLocation
            (
            );
            /**Sets  the drilling location 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDrillingLocation
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::DrillingLocationTypes drillingLocationMode /** the drilling location */
            );
            /**Returns  the off center distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * OffCenterDistance
            (
            );
            /**Returns  the reverse direction value
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction value
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetReverseDirection
            (
                bool isReverseDirection /** the reverse direction value */
            );
            /**Returns  the chip removal increment type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::RemovalIncrementTypes ChipRemovalIncrementType
            (
            );
            /**Sets  the chip removal increment type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetChipRemovalIncrementType
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::RemovalIncrementTypes incrementType /** the removal increment type */
            );
            /**Returns  the constant increment 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * ConstantIncrement
            (
            );
            /**Returns  the safe or departure distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * SafeOrDepartureDistance
            (
            );
            /**Returns  the retract type for simulated cycles 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::FinalRetractTypes FinalRetractType
            (
            );
            /**Sets  the retract type for simulated cycles 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetFinalRetractType
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::FinalRetractTypes finalRetractType /** the retract type for simulated cycles */
            );
            /**Returns  the retract distance for simulated cycles
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * FinalRetractDistance
            (
            );
            /**Returns  the reposition distance 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * RepositionDistance
            (
            );
            /**Returns  the variable increment list
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillVariableIncrementBuilder * VariableIncrementList
            (
            );
            /**Returns  the drill step 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * DrillStep
            (
            );
            /**Returns  the drill step modifier1 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * DrillStepModifier1
            (
            );
            /**Returns  the drill step modifier2 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * DrillStepModifier2
            (
            );
            /**Returns  the centerline cycle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::CycleTypes CenterlineCycle
            (
            );
            /**Sets  the centerline cycle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCenterlineCycle
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::CycleTypes cycleMode /** the cycle */
            );
            /**Returns  the output option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CenterlineDrillTurningBuilder::OutputOptionTypes OutputOption
            (
            );
            /**Sets  the output option 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOutputOption
            (
                NXOpen::CAM::CenterlineDrillTurningBuilder::OutputOptionTypes outputOptionMode /** the output option mode */
            );
            /**Returns  the clearance distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * ClearanceDistance
            (
            );
            /**Returns  the engage distance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * EngageDistance
            (
            );
            /**Returns  the non-cutting builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmTurningBuilder * NonCuttingBuilder
            (
            );
            /** Returns the cycle tracking point  @return  
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXString GetCycleTrackingPoint
            (
            );
            /** Sets the cycle tracking point 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCycleTrackingPoint
            (
                const NXString & name /** name */ 
            );
            /** Sets the cycle tracking point 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetCycleTrackingPoint
            (
                const char * name /** name */ 
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
