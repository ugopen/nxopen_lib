#ifndef NXOpen_CAM_CYCLE_HXX_INCLUDED
#define NXOpen_CAM_CYCLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_Cycle.ja
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
#include <NXOpen/CAM_StepoverBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
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
        class Cycle;
    }
    namespace CAM
    {
        class CycleCoolant;
    }
    namespace CAM
    {
        class CycleDwell;
    }
    namespace CAM
    {
        class CycleNodragClearance;
    }
    namespace CAM
    {
        class CycleSpindle;
    }
    namespace CAM
    {
        class CycleStepRetract;
    }
    namespace CAM
    {
        class CycleTipRelease;
    }
    namespace CAM
    {
        class StepoverBuilder;
    }
    namespace CAM
    {
        class _CycleBuilder;
        class CycleImpl;
        /** Represets a User Defined Event 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  Cycle : public NXOpen::TaggedObject
        {
            /** Available types for dwell */
            public: enum DwellType
            {
                DwellTypeOn/** dwell on */,
                DwellTypeOff/** dwell off */,
                DwellTypeSeconds/** dwell seconds */,
                DwellTypeRevolutions/** dwell revolutions */
            };

            /** Available types for motion output */
            public: enum MotionOutputTypes
            {
                MotionOutputTypesMachineCycle/** Machine Cycle */,
                MotionOutputTypesSingleMoves/** single moves */,
                MotionOutputTypesInterruptedMoves/** interrupted moves */
            };

            /** Available types for fixed cut */
            public: enum CutMode
            {
                CutModeOff/** fixed cut distance off */,
                CutModeValue/** fixed cut distance by value */,
                CutModePercentage/** fixed cut distance by percentage of tool diameter */
            };

            private: CycleImpl * m_cycle_impl;
            private: friend class  _CycleBuilder;
            protected: Cycle();
            public: ~Cycle();
            /**Returns  the cycle type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString CycleType
            (
            );
            /**Sets  the cycle type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCycleType
            (
                const NXString & cycleName /** the cycle type*/
            );
            /**Sets  the cycle type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetCycleType
            (
                const char * cycleName /** the cycle type*/
            );
            /**Returns  the dwell type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Cycle::DwellType Dwell
            (
            );
            /**Sets  the dwell type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDwell
            (
                NXOpen::CAM::Cycle::DwellType dwell /** the dwell type */
            );
            /**Returns  the dwell value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double DwellValue
            (
            );
            /**Sets  the dwell value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDwellValue
            (
                double doubleValue /** the dwell value */
            );
            /**Returns  the option type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool Option
            (
            );
            /**Sets  the option type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOption
            (
                bool optionType /** the option type */
            );
            /**Returns  the cam status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool CamStatus
            (
            );
            /**Sets  the cam status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCamStatus
            (
                bool camStatus /** the cam status type */
            );
            /**Returns  the cam value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int CamValue
            (
            );
            /**Sets  the cam value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCamValue
            (
                int doubleValue /** the cam  */
            );
            /**Returns  the csink diameter 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double CsinkDiameter
            (
            );
            /**Sets  the csink diameter 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCsinkDiameter
            (
                double doubleValue /** the csink diameter */
            );
            /**Returns  the entrance diameter 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double EntranceDiameter
            (
            );
            /**Sets  the entrance diameter 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEntranceDiameter
            (
                double doubleValue /** the entrance diameter */
            );
            /**Returns  the text 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Text
            (
            );
            /**Sets  the text 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetText
            (
                const NXString & cText /** the text*/
            );
            /**Sets  the text 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetText
            (
                const char * cText /** the text*/
            );
            /**Returns  the motion output 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Cycle::MotionOutputTypes MotionOutput
            (
            );
            /**Sets  the motion output 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMotionOutput
            (
                NXOpen::CAM::Cycle::MotionOutputTypes newValue /** the motion output */
            );
            /**Returns  the axial stepover 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::StepoverBuilder * AxialStepover
            (
            );
            /**Returns  the step clearance status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool StepClearanceStatus
            (
            );
            /**Sets  the step clearance status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepClearanceStatus
            (
                bool camStatus /** the step clearance status type */
            );
            /**Returns  the step clearance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double StepClearance
            (
            );
            /**Sets  the step clearance 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepClearance
            (
                double doubleValue /** the step clearance */
            );
            /**Returns  the dwell start type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Cycle::DwellType DwellStart
            (
            );
            /**Sets  the dwell start type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDwellStart
            (
                NXOpen::CAM::Cycle::DwellType dwell /** the dwell start type */
            );
            /**Returns  the dwell start value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double DwellStartValue
            (
            );
            /**Sets  the dwell start value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDwellStartValue
            (
                double doubleValue /** the dwell start */
            );
            /**Returns  the dwell final type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Cycle::DwellType DwellFinal
            (
            );
            /**Sets  the dwell final type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDwellFinal
            (
                NXOpen::CAM::Cycle::DwellType dwell /** the dwell final type */
            );
            /**Returns  the dwell final value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double DwellFinalValue
            (
            );
            /**Sets  the dwell final value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDwellFinalValue
            (
                double doubleValue /** the dwell final */
            );
            /**Returns  the first cut mode type 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Cycle::CutMode FirstCutMode
            (
            );
            /**Sets  the first cut mode type 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFirstCutMode
            (
                NXOpen::CAM::Cycle::CutMode firstCutMode /** the first cut mode */
            );
            /**Returns  the the first cut value 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: double FirstCutValue
            (
            );
            /**Sets  the the first cut value 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFirstCutValue
            (
                double doubleValue /** the first cut */
            );
            /**Returns  the last cut mode type 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Cycle::CutMode LastCutMode
            (
            );
            /**Sets  the last cut mode type 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLastCutMode
            (
                NXOpen::CAM::Cycle::CutMode lastCutMode /** the last cut mode */
            );
            /**Returns  the the last cut value 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: double LastCutValue
            (
            );
            /**Sets  the the last cut value 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLastCutValue
            (
                double doubleValue /** the last cut */
            );
            /**Returns  the shift status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShiftStatus
            (
            );
            /**Sets  the shift status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetShiftStatus
            (
                bool camStatus /** the shift status type */
            );
            /**Returns  the shift 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double Shift
            (
            );
            /**Sets  the shift 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetShift
            (
                double doubleValue /** the shift */
            );
            /**Returns  the times status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool TimesStatus
            (
            );
            /**Sets  the times status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTimesStatus
            (
                bool camStatus /** the times status type */
            );
            /**Returns  the times 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int Times
            (
            );
            /**Sets  the times 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTimes
            (
                int times /** the times */
            );
            /**Returns  the orientation status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool OrientationStatus
            (
            );
            /**Sets  the orientation status 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOrientationStatus
            (
                bool oStatus /** the orientation status */
            );
            /**Returns  the orientation 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double Orientation
            (
            );
            /**Sets  the orientation 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOrientation
            (
                double orientation /** the orientation */
            );
            /** Check if parameter is active @return  if the parameter is active
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetParameterActive
            (
                const NXString & cycleParamName /** the name of the parameter*/
            );
            /** Check if parameter is active @return  if the parameter is active
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            bool GetParameterActive
            (
                const char * cycleParamName /** the name of the parameter*/
            );
            /** To Set if parameter is active
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetParameterActive
            (
                const NXString & cycleParamName /** the name of the parameter*/,
                bool parameterActive /** if the parameter is active*/
            );
            /** To Set if parameter is active
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetParameterActive
            (
                const char * cycleParamName /** the name of the parameter*/,
                bool parameterActive /** if the parameter is active*/
            );
            /** Get the integer value of the parameter @return  integer value of parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int GetIntegerValue
            (
                const NXString & cycleParamName /** the name of the parameter*/
            );
            /** Get the integer value of the parameter @return  integer value of parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            int GetIntegerValue
            (
                const char * cycleParamName /** the name of the parameter*/
            );
            /** Set the integer value of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetIntegerValue
            (
                const NXString & cycleParamName /** the name of the parameter*/,
                int integerValue /** integer value of the parameter*/
            );
            /** Set the integer value of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetIntegerValue
            (
                const char * cycleParamName /** the name of the parameter*/,
                int integerValue /** integer value of the parameter*/
            );
            /** Get the double value of the parameter @return  double value of parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double GetDoubleValue
            (
                const NXString & cycleParamName /** the name of the parameter*/
            );
            /** Get the double value of the parameter @return  double value of parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            double GetDoubleValue
            (
                const char * cycleParamName /** the name of the parameter*/
            );
            /** Set the double value of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDoubleValue
            (
                const NXString & cycleParamName /** the name of the parameter*/,
                double doubleValue /** double value of the parameter*/
            );
            /** Set the double value of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetDoubleValue
            (
                const char * cycleParamName /** the name of the parameter*/,
                double doubleValue /** double value of the parameter*/
            );
            /** Get the boolean value of the parameter @return  boolean value of parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetBooleanValue
            (
                const NXString & cycleParamName /** the name of the parameter*/
            );
            /** Get the boolean value of the parameter @return  boolean value of parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            bool GetBooleanValue
            (
                const char * cycleParamName /** the name of the parameter*/
            );
            /** Set the boolean value of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetBooleanValue
            (
                const NXString & cycleParamName /** the name of the parameter*/,
                bool booleanValue /** boolean value of the parameter*/
            );
            /** Set the boolean value of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetBooleanValue
            (
                const char * cycleParamName /** the name of the parameter*/,
                bool booleanValue /** boolean value of the parameter*/
            );
            /** Get the point of the parameter @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::Point3d GetPointValue
            (
                const NXString & cycleParamName /** the name of the parameter*/
            );
            /** Get the point of the parameter @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            NXOpen::Point3d GetPointValue
            (
                const char * cycleParamName /** the name of the parameter*/
            );
            /** Set the point of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPointValue
            (
                const NXString & cycleParamName /** the name of the parameter*/,
                const NXOpen::Point3d & point /** point */ 
            );
            /** Set the point of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetPointValue
            (
                const char * cycleParamName /** the name of the parameter*/,
                const NXOpen::Point3d & point /** point */ 
            );
            /** Get the vector of the parameter @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::Vector3d GetVectorValue
            (
                const NXString & cycleParamName /** the name of the parameter*/
            );
            /** Get the vector of the parameter @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            NXOpen::Vector3d GetVectorValue
            (
                const char * cycleParamName /** the name of the parameter*/
            );
            /** Set the vector of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetVectorValue
            (
                const NXString & cycleParamName /** the name of the parameter*/,
                const NXOpen::Vector3d & vector /** vector */ 
            );
            /** Set the vector of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetVectorValue
            (
                const char * cycleParamName /** the name of the parameter*/,
                const NXOpen::Vector3d & vector /** vector */ 
            );
            /** Get the string value of the parameter @return  string value of parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetStringValue
            (
                const NXString & cycleParamName /** the name of the parameter*/
            );
            /** Get the string value of the parameter @return  string value of parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            NXString GetStringValue
            (
                const char * cycleParamName /** the name of the parameter*/
            );
            /** Set the string value of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStringValue
            (
                const NXString & cycleParamName /** the name of the parameter*/,
                const NXString & stringValue /** string value of the parameter*/
            );
            /** Set the string value of the parameter
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetStringValue
            (
                const char * cycleParamName /** the name of the parameter*/,
                const char * stringValue /** string value of the parameter*/
            );
            /**Returns  the tracking point 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXString CycleTrackingPoint
            (
            );
            /**Sets  the tracking point 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCycleTrackingPoint
            (
                const NXString & cText /** the text*/
            );
            /**Sets  the tracking point 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetCycleTrackingPoint
            (
                const char * cText /** the text*/
            );
            /**Returns  the dwell at depth 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleDwell * DwellAtDepth
            (
            );
            /**Returns  the dwell at start point of phase 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleDwell * DwellAtStartPoint
            (
            );
            /**Returns  the dwell before cut 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleDwell * DwellBeforeCut
            (
            );
            /**Returns  the dwell at final depth 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleDwell * DwellAtFinalDepth
            (
            );
            /**Returns  the dwell before engage 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleDwell * DwellBeforeEngage
            (
            );
            /**Returns  the dwell before retract
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleDwell * DwellBeforeRetract
            (
            );
            /**Returns  the spindle before engage
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleSpindle * SpindleBeforeEngage
            (
            );
            /**Returns  the spindle before retract
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleSpindle * SpindleBeforeRetract
            (
            );
            /**Returns  the step retract
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleStepRetract * StepRetract
            (
            );
            /**Returns  the nodrag clearance
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleNodragClearance * NodragClearance
            (
            );
            /**Returns  the coolant 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleCoolant * CoolantBeforeEngage
            (
            );
            /**Returns  the coolant 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleCoolant * CoolantBeforeCut
            (
            );
            /**Returns  the coolant 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleCoolant * CoolantBeforeRetract
            (
            );
            /**Returns  the (minimal) tip release 
             <br>  Created in NX10.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CycleTipRelease * TipRelease
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