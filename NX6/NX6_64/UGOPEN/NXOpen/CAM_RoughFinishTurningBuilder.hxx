#ifndef NXOpen_CAM_ROUGHFINISHTURNINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_ROUGHFINISHTURNINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_RoughFinishTurningBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAM_TurningOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class RoughFinishTurningBuilder;
    }
    namespace CAM
    {
        class TrimPlane;
    }
    namespace CAM
    {
        class TrimPoint;
    }
    namespace CAM
    {
        class TurnCutParameters;
    }
    namespace CAM
    {
        class TurningOperationBuilder;
    }
    class NXObject;
    class Point;
    namespace CAM
    {
        class _RoughFinishTurningBuilderBuilder;
        /** Represents a RoughFinishTurning Builder  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT RoughFinishTurningBuilder : public CAM::TurningOperationBuilder
        {
            /** the Custom Member Data types */
            public: enum CustomMemberDataTypes
            {
                CustomMemberDataTypesWithinRegion/** Within Region */,
                CustomMemberDataTypesWithinDistance/** Within Distance */
            };

            /** the Cut regions types */
            public: enum CutRegionsTypes
            {
                CutRegionsTypesSingleRegion/** Cut regions type: Single Region */,
                CutRegionsTypesSingleDirection/** Cut regions type: Single Direction */,
                CutRegionsTypesReverseDirection/** Cut regions type: Reverse Direction */,
                CutRegionsTypesBiDirectional/** Cut regions type: Bi-directional */,
                CutRegionsTypesAlternate/** Cut regions type: Alternate */
            };

            /** the Tolerance Offset types */
            public: enum ToleranceOffsetTypes
            {
                ToleranceOffsetTypesAfterContainment/** Tolerance offset after containment. */,
                ToleranceOffsetTypesBeforeContainment/** Tolerance offset before containment. */
            };

            /** the Mininmum Area types */
            public: enum MinimumAreaTypes
            {
                MinimumAreaTypesNone/** None. */,
                MinimumAreaTypesSpecify/** Specify */
            };

            /** the Extend Mode types */
            public: enum ExtendModeTypes
            {
                ExtendModeTypesTagential/** Tagential */,
                ExtendModeTypesSpecify/** Specify */
            };

            /** the Region Selection types */
            public: enum RegionSelectionTypes
            {
                RegionSelectionTypesAutomatic/** Automatic cut region selection. */,
                RegionSelectionTypesManual/** Manual cut region selection. */
            };

            private: friend class  _RoughFinishTurningBuilderBuilder;
            protected: RoughFinishTurningBuilder();
            /**Returns  the Omit Reversals toggle <br> License requirements : None */
            public: bool OmitReversals
            (
            );
            /**Sets  the Omit Reversals toggle <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOmitReversals
            (
                bool omitReversals /** the omit reversals */
            );
            /**Returns  the Ignore Minimum Boring Diameter toggle <br> License requirements : None */
            public: bool IgnoreMinimumBoringDiameter
            (
            );
            /**Sets  the Ignore Minimum Boring Diameter toggle <br> License requirements : cam_base ("CAM BASE") */
            public: void SetIgnoreMinimumBoringDiameter
            (
                bool ignoreMinBoringDia /** the Ignore Minimum Boring Diameter */
            );
            /**Returns  the radial trim plane 1  <br> License requirements : None */
            public: NXOpen::CAM::TrimPlane * RadialTrimPlane1
            (
            );
            /**Returns  the radial trim plane 2  <br> License requirements : None */
            public: NXOpen::CAM::TrimPlane * RadialTrimPlane2
            (
            );
            /**Returns  the axial trim plane 1  <br> License requirements : None */
            public: NXOpen::CAM::TrimPlane * AxialTrimPlane1
            (
            );
            /**Returns  the axial trim plane 2  <br> License requirements : None */
            public: NXOpen::CAM::TrimPlane * AxialTrimPlane2
            (
            );
            /**Returns  the trim point 1  <br> License requirements : None */
            public: NXOpen::CAM::TrimPoint * TrimPoint1
            (
            );
            /**Returns  the trim point 2  <br> License requirements : None */
            public: NXOpen::CAM::TrimPoint * TrimPoint2
            (
            );
            /**Returns  the Custom Member Data type  <br> License requirements : None */
            public: NXOpen::CAM::RoughFinishTurningBuilder::CustomMemberDataTypes CustomMemberData
            (
            );
            /**Sets  the Custom Member Data type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCustomMemberData
            (
                NXOpen::CAM::RoughFinishTurningBuilder::CustomMemberDataTypes surfaceSensitivityMode /** the custom member data type*/
            );
            /**Returns  the Custom Member Data Distance  <br> License requirements : None */
            public: double CustomMemberDataDistance
            (
            );
            /**Sets  the Custom Member Data Distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCustomMemberDataDistance
            (
                double surfaceSensitivityTolerance /** the custom member data distance */
            );
            /**Returns  the Tolerance Offset type  <br> License requirements : None */
            public: NXOpen::CAM::RoughFinishTurningBuilder::ToleranceOffsetTypes ToleranceOffset
            (
            );
            /**Sets  the Tolerance Offset type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToleranceOffset
            (
                NXOpen::CAM::RoughFinishTurningBuilder::ToleranceOffsetTypes toleranceOffsetMode /** the tolerance offset type */
            );
            /**Returns  the Region Selection type  <br> License requirements : None */
            public: NXOpen::CAM::RoughFinishTurningBuilder::RegionSelectionTypes RegionSelection
            (
            );
            /**Sets  the Region Selection type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRegionSelection
            (
                NXOpen::CAM::RoughFinishTurningBuilder::RegionSelectionTypes cutRegionSelectionMode /** the region selection type */
            );
            /**Returns  the Region Selection Point  <br> License requirements : None */
            public: NXOpen::Point * RegionSelectionPoint
            (
            );
            /**Sets  the Region Selection Point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRegionSelectionPoint
            (
                NXOpen::Point * cutRegionSelectionPoint /** the region selection point */
            );
            /**Returns  the Cut regions type  <br> License requirements : None */
            public: NXOpen::CAM::RoughFinishTurningBuilder::CutRegionsTypes CutRegions
            (
            );
            /**Sets  the Cut regions type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutRegions
            (
                NXOpen::CAM::RoughFinishTurningBuilder::CutRegionsTypes multipleCutRegions /** the Cut regions type */
            );
            /**Returns  the Minimum Area type  <br> License requirements : None */
            public: NXOpen::CAM::RoughFinishTurningBuilder::MinimumAreaTypes MinimumArea
            (
            );
            /**Sets  the Minimum Area type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMinimumArea
            (
                NXOpen::CAM::RoughFinishTurningBuilder::MinimumAreaTypes minimumAreaActive /** the minimum area type */
            );
            /**Returns  the Minimum Area Size <br> License requirements : None */
            public: double MinimumAreaSize
            (
            );
            /**Sets  the Minimum Area Size <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMinimumAreaSize
            (
                double minArea /** the minimum area size */
            );
            /**Returns  the Start Offset  <br> License requirements : None */
            public: double StartOffset
            (
            );
            /**Sets  the Start Offset  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStartOffset
            (
                double startOffset /** the start offset */
            );
            /**Returns  the end offset  <br> License requirements : None */
            public: double EndOffset
            (
            );
            /**Sets  the end offset  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEndOffset
            (
                double endOffset /** the end offset */
            );
            /**Returns  the start angle  <br> License requirements : None */
            public: double StartAngle
            (
            );
            /**Sets  the start angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStartAngle
            (
                double startAngle /** the start angle */
            );
            /**Returns  the end angle  <br> License requirements : None */
            public: double EndAngle
            (
            );
            /**Sets  the end angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEndAngle
            (
                double endAngle /** the end angle */
            );
            /**Returns  the Extend Mode  <br> License requirements : None */
            public: NXOpen::CAM::RoughFinishTurningBuilder::ExtendModeTypes ExtendMode
            (
            );
            /**Sets  the Extend Mode  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetExtendMode
            (
                NXOpen::CAM::RoughFinishTurningBuilder::ExtendModeTypes tangentialStartEndExtension /** the extend mode type */
            );
            /**Returns  the Level Angle  <br> License requirements : None */
            public: double LevelAngle
            (
            );
            /**Sets  the Level Angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLevelAngle
            (
                double levelAngle /** the Level Angle */
            );
            /**Returns  the Step Angle  <br> License requirements : None */
            public: double StepAngle
            (
            );
            /**Sets  the Step Angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepAngle
            (
                double stepAngle /** the Step Angle */
            );
            /**Returns  the Level Angle Vector  <br> License requirements : None */
            public: NXOpen::NXObject * LevelAngleVector
            (
            );
            /**Sets  the Level Angle Vector  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLevelAngleVector
            (
                NXOpen::NXObject * angleVector /** the Level Angle Vector */
            );
            /** Set the Step Angle Vector  @return  the Step Angle Vector  <br> License requirements : None */
            public: NXOpen::NXObject * GetStepAngleVector
            (
            );
            /** Get the Step Angle Vector  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepAngleVector
            (
                NXOpen::NXObject * angleVector /** the Step Angle Vector */
            );
            /**Returns  the cut parameter object <br> License requirements : None */
            public: NXOpen::CAM::TurnCutParameters * CutParameters
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif