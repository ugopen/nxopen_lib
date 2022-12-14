#ifndef NXOpen_CAM_NCMPLANARBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NCMPLANARBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmPlanarBuilder.ja
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
#include <NXOpen/CAM_NcmSubopBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class NcmPlanarBuilder;
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
        class NcmSubopBuilder;
    }
    class Point;
    class SmartObject;
    namespace CAM
    {
        class _NcmPlanarBuilderBuilder;
        /**
            Represents a @link CAM::NcmPlanarBuilder CAM::NcmPlanarBuilder@endlink 
             <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateNcmPlanarBuilder CAM::NCGroupCollection::CreateNcmPlanarBuilder@endlink  <br> */
        class NXOPENCPPEXPORT NcmPlanarBuilder : public CAM::NcmSubopBuilder
        {
            /** Available types for closed area engage in planar milling */
            public: enum EngClosedAreaTypes
            {
                EngClosedAreaTypesHelical/** helical */,
                EngClosedAreaTypesRampOnShape/** ramp on shape */,
                EngClosedAreaTypesZigzagRamp/** zig-zag ramp (for future use) */,
                EngClosedAreaTypesPlunge/** plunge */,
                EngClosedAreaTypesNone/** none */
            };

            /** Available types for open area engage in planar milling */
            public: enum EngOpenAreaTypes
            {
                EngOpenAreaTypesSameAsClosed/** use same settings as for closed area */,
                EngOpenAreaTypesLinear/** linear */,
                EngOpenAreaTypesArc/** arc */,
                EngOpenAreaTypesHighSpeedArc/** high speed arc (for future use) */,
                EngOpenAreaTypesPoints/** points */,
                EngOpenAreaTypesAlongVector/** along vector */,
                EngOpenAreaTypesAngAngPlane/** angle angle plane */,
                EngOpenAreaTypesVectorPlane/** vector plane */
            };

            /** Available types for retract in planar milling */
            public: enum RetractTypes
            {
                RetractTypesSameAsEngage/** use same settings as for open area engage */,
                RetractTypesLinear/** linear */,
                RetractTypesArc/** arc */,
                RetractTypesHighSpeedArc/** high speed arc (for future use) */,
                RetractTypesPoints/** points */,
                RetractTypesLift/** lift */,
                RetractTypesAlongVector/** along vector */,
                RetractTypesAngAngPlane/** angle angle plane */,
                RetractTypesVectorPlane/** vector plane */,
                RetractTypesNone/** none (for future use) */
            };

            /** Available types for default region start in planar milling */
            public: enum DefaultRegionStartTypes
            {
                DefaultRegionStartTypesMidPoint/** start at mid point */,
                DefaultRegionStartTypesCorner/** start_at_corners */
            };

            /** Available strategies for transfer within levels in planar milling */
            public: enum TransferWithinLevelsWiths
            {
                TransferWithinLevelsWithsUseEngret/** Use engage and retract defs */,
                TransferWithinLevelsWithsFollowBoundary/** follow boundary (for future use) */,
                TransferWithinLevelsWithsLiftPlunge/** lift and plunge */
            };

            /** Available types for transfer within levels in planar milling */
            public: enum TransferWithinLevelsTypes
            {
                TransferWithinLevelsTypesLowestSafeZ/** lowest Safe Z */,
                TransferWithinLevelsTypesPrevPlane/** previous plane */,
                TransferWithinLevelsTypesClearance/** clearance */
            };

            /** Available types for transfer between levels in planar milling */
            public: enum TransferBetweenLevelsTypes
            {
                TransferBetweenLevelsTypesPrevPlane/** previous plane */,
                TransferBetweenLevelsTypesDirect/** direct */,
                TransferBetweenLevelsTypesClearance/** clearance */
            };

            /** Available types for transfer between regions in planar milling */
            public: enum TransferBetweenRegionsTypes
            {
                TransferBetweenRegionsTypesClearance/** clearance */,
                TransferBetweenRegionsTypesPrevPlane/** previous plane */,
                TransferBetweenRegionsTypesDirect/** direct */,
                TransferBetweenRegionsTypesLowestSafeZ/** lowest safe z */
            };

            /** Available types for cutter compensation in planar milling */
            public: enum CutcomTypes
            {
                CutcomTypesNone/** cutter compensation off */,
                CutcomTypesAllFinishPasses/** cutter compensation on all finish passes */,
                CutcomTypesFinalFinishPass/** cutter compensation on last finish pass */
            };

            private: friend class  _NcmPlanarBuilderBuilder;
            protected: NcmPlanarBuilder();
            /**Returns  the engage closed area type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmPlanarBuilder::EngClosedAreaTypes EngClosedAreaType
            (
            );
            /**Sets  the engage closed area type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngClosedAreaType
            (
                NXOpen::CAM::NcmPlanarBuilder::EngClosedAreaTypes engClosedAreaType /** engclosedareatype */ 
            );
            /**Returns  the engage closed area diameter builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngClosedAreaDiameterBuilder
            (
            );
            /**Returns  the engage closed area ramp angle  <br> License requirements : cam_base ("CAM BASE") */
            public: double EngClosedAreaRampAngle
            (
            );
            /**Sets  the engage closed area ramp angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngClosedAreaRampAngle
            (
                double engClosedAreaRampAngle /** engclosedarearampangle */ 
            );
            /**Returns  the engage closed area height builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngClosedAreaHeightBuilder
            (
            );
            /**Returns  the engage closed area use max width  <br> License requirements : cam_base ("CAM BASE") */
            public: bool EngClosedAreaUseMaxWidth
            (
            );
            /**Sets  the engage closed area use max width  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngClosedAreaUseMaxWidth
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the engage closed area max width builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngClosedAreaMaxWidthBuilder
            (
            );
            /**Returns  the engage closed area min clearance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngClosedAreaMinClearanceBuilder
            (
            );
            /**Returns  the engage closed area min ramp length builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngClosedAreaMinRampLengthBuilder
            (
            );
            /**Returns  the engage open area type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmPlanarBuilder::EngOpenAreaTypes EngOpenAreaType
            (
            );
            /**Sets  the engage open area type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaType
            (
                NXOpen::CAM::NcmPlanarBuilder::EngOpenAreaTypes engOpenAreaType /** engopenareatype */ 
            );
            /**Returns  the engage open area radius builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngOpenAreaRadiusBuilder
            (
            );
            /**Returns  the engage open area vector  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::SmartObject * EngOpenAreaVector
            (
            );
            /**Sets  the engage open area vector  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaVector
            (
                NXOpen::SmartObject * newValue /** newvalue */ 
            );
            /**Returns  the engage open area length builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngOpenAreaLengthBuilder
            (
            );
            /**Returns  the engage open area arc angle  <br> License requirements : cam_base ("CAM BASE") */
            public: double EngOpenAreaArcAngle
            (
            );
            /**Sets  the engage open area arc angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaArcAngle
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the engage open area swing angle  <br> License requirements : cam_base ("CAM BASE") */
            public: double EngOpenAreaSwingAngle
            (
            );
            /**Sets  the engage open area swing angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaSwingAngle
            (
                double engOpenAreaSwingAngle /** engopenareaswingangle */ 
            );
            /**Returns  the engage open area ramp angle  <br> License requirements : cam_base ("CAM BASE") */
            public: double EngOpenAreaRampAngle
            (
            );
            /**Sets  the engage open area ramp angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaRampAngle
            (
                double engOpenAreaRampAngle /** engopenarearampangle */ 
            );
            /** Returns engage open area points  <br> License requirements : cam_base ("CAM BASE") */
            public: void GetEngOpenAreaPoints
            (
                std::vector<NXOpen::Point *> & engOpenAreaPoints /** Array of points */
            );
            /** Sets engage open area points  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaPoints
            (
                const std::vector<NXOpen::Point *> & engOpenAreaPoints /** Array of points */
            );
            /**Returns  the engage open area use effective distance  <br> License requirements : cam_base ("CAM BASE") */
            public: bool EngOpenAreaUseEffectDist
            (
            );
            /**Sets  the engage open area use effective distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaUseEffectDist
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the engage open area effect dist builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngOpenAreaEffectDistBuilder
            (
            );
            /**Returns  the engage open area height builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngOpenAreaHeightBuilder
            (
            );
            /**Returns  the engage open area min clearance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * EngOpenAreaMinClearanceBuilder
            (
            );
            /**Returns  the engage open area trim  <br> License requirements : cam_base ("CAM BASE") */
            public: bool EngOpenAreaTrim
            (
            );
            /**Sets  the engage open area trim  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaTrim
            (
                bool engOpenAreaTrim /** engopenareatrim */ 
            );
            /**Returns  the engage open area start at arc center  <br> License requirements : cam_base ("CAM BASE") */
            public: bool EngOpenAreaStartAtArcCenter
            (
            );
            /**Sets  the engage open area start at arc center  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaStartAtArcCenter
            (
                bool engOpenAreaStartAtArcCenter /** engopenareastartatarccenter */ 
            );
            /**Returns  the engage open area plane  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::SmartObject * EngOpenAreaPlane
            (
            );
            /**Sets  the engage open area plane  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngOpenAreaPlane
            (
                NXOpen::SmartObject * newValue /** newvalue */ 
            );
            /**Returns  the flag to control limitation of engage and retract motions to cut regions  <br> License requirements : cam_base ("CAM BASE") */
            public: bool LimitEngRetToCutRegion
            (
            );
            /**Sets  the flag to control limitation of engage and retract motions to cut regions  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLimitEngRetToCutRegion
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the retract type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmPlanarBuilder::RetractTypes RetractType
            (
            );
            /**Sets  the retract type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractType
            (
                NXOpen::CAM::NcmPlanarBuilder::RetractTypes retractType /** retracttype */ 
            );
            /**Returns  the retract radius builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * RetractRadiusBuilder
            (
            );
            /**Returns  the retract vector  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::SmartObject * RetractVector
            (
            );
            /**Sets  the retract vector  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractVector
            (
                NXOpen::SmartObject * newValue /** newvalue */ 
            );
            /**Returns  the retract length builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * RetractLengthBuilder
            (
            );
            /**Returns  the retract arc angle  <br> License requirements : cam_base ("CAM BASE") */
            public: double RetractArcAngle
            (
            );
            /**Sets  the retract arc angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractArcAngle
            (
                double newValue /** newvalue */ 
            );
            /**Returns  the retract swing angle  <br> License requirements : cam_base ("CAM BASE") */
            public: double RetractSwingAngle
            (
            );
            /**Sets  the retract swing angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractSwingAngle
            (
                double retractSwingAngle /** retractswingangle */ 
            );
            /**Returns  the retract ramp angle  <br> License requirements : cam_base ("CAM BASE") */
            public: double RetractRampAngle
            (
            );
            /**Sets  the retract ramp angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractRampAngle
            (
                double retractRampAngle /** retractrampangle */ 
            );
            /** Returns retract points  <br> License requirements : cam_base ("CAM BASE") */
            public: void GetRetractPoints
            (
                std::vector<NXOpen::Point *> & retractPoints /** Array of points */
            );
            /** Sets retract points  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractPoints
            (
                const std::vector<NXOpen::Point *> & retractPoints /** Array of points */
            );
            /**Returns  the retract use effective distance  <br> License requirements : cam_base ("CAM BASE") */
            public: bool RetractUseEffectDist
            (
            );
            /**Sets  the retract use effective distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractUseEffectDist
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the retract effect dist builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * RetractEffectDistBuilder
            (
            );
            /**Returns  the retract height builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * RetractHeightBuilder
            (
            );
            /**Returns  the retract min clearance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * RetractMinClearanceBuilder
            (
            );
            /**Returns  the retract trim  <br> License requirements : cam_base ("CAM BASE") */
            public: bool RetractTrim
            (
            );
            /**Sets  the retract trim  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractTrim
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the retract plane  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::SmartObject * RetractPlane
            (
            );
            /**Sets  the retract plane  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetractPlane
            (
                NXOpen::SmartObject * newValue /** newvalue */ 
            );
            /**Returns  the start/drill points overlap distance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * OverlapDistanceBuilder
            (
            );
            /**Returns  the region start type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmPlanarBuilder::DefaultRegionStartTypes DefaultRegionStartType
            (
            );
            /**Sets  the region start type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDefaultRegionStartType
            (
                NXOpen::CAM::NcmPlanarBuilder::DefaultRegionStartTypes defaultRegionStartType /** defaultregionstarttype */ 
            );
            /** Returns region start points  <br> License requirements : cam_base ("CAM BASE") */
            public: void GetRegionStartPoints
            (
                std::vector<NXOpen::Point *> & regionStartPoints /** The points */
            );
            /** Sets region start points  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRegionStartPoints
            (
                const std::vector<NXOpen::Point *> & regionStartPoints /** The points */
            );
            /**Returns  the start points use effective distance  <br> License requirements : cam_base ("CAM BASE") */
            public: bool StartPointsUseEffectDist
            (
            );
            /**Sets  the start points use effective distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStartPointsUseEffectDist
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the region start points effective distance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * StartPointsEffectDistBuilder
            (
            );
            /** The pre-drill points  @return  Array of points  <br> License requirements : cam_base ("CAM BASE") */
            public: std::vector<NXOpen::Point *> GetPredrillPoints
            (
            );
            /** The pre-drill points  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPredrillPoints
            (
                const std::vector<NXOpen::Point *> & predrillPoints /** Array of points */
            );
            /**Returns  the pre-drill points use effective distance  <br> License requirements : cam_base ("CAM BASE") */
            public: bool PredrillPointsUseEffectDist
            (
            );
            /**Sets  the pre-drill points use effective distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPredrillPointsUseEffectDist
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the pre-drill points effective distance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * PredrillPointsEffectDistBuilder
            (
            );
            /**Returns  the transfer within levels strategy  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmPlanarBuilder::TransferWithinLevelsWiths TransferWithinLevelsWith
            (
            );
            /**Sets  the transfer within levels strategy  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTransferWithinLevelsWith
            (
                NXOpen::CAM::NcmPlanarBuilder::TransferWithinLevelsWiths newValue /** newvalue */ 
            );
            /**Returns  the transfer within levels max follow distance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferWithinLevelsMaxFollowDistanceBuilder
            (
            );
            /**Returns  the transfer within levels height builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferWithinLevelsHeightBuilder
            (
            );
            /**Returns  the transfer within levels type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmPlanarBuilder::TransferWithinLevelsTypes TransferWithinLevelsType
            (
            );
            /**Sets  the transfer within levels type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTransferWithinLevelsType
            (
                NXOpen::CAM::NcmPlanarBuilder::TransferWithinLevelsTypes transferType /** transfertype */ 
            );
            /**Returns  the transfer within levels safe distance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferWithinLevelsSafeDistanceBuilder
            (
            );
            /**Returns  the transfer between levels type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmPlanarBuilder::TransferBetweenLevelsTypes TransferBetweenLevelsType
            (
            );
            /**Sets  the transfer between levels type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTransferBetweenLevelsType
            (
                NXOpen::CAM::NcmPlanarBuilder::TransferBetweenLevelsTypes transferType /** transfertype */ 
            );
            /**Returns  the transfer between levels safe distance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferBetweenLevelsSafeDistanceBuilder
            (
            );
            /**Returns  the transfer between regions type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmPlanarBuilder::TransferBetweenRegionsTypes TransferBetweenRegionsType
            (
            );
            /**Sets  the transfer between regions type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTransferBetweenRegionsType
            (
                NXOpen::CAM::NcmPlanarBuilder::TransferBetweenRegionsTypes transferType /** transfertype */ 
            );
            /**Returns  the transfer between regions safe distance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferBetweenRegionsSafeDistanceBuilder
            (
            );
            /**Returns  the from point builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceFromBuilder
            (
            );
            /**Returns  the start point builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceStartBuilder
            (
            );
            /**Returns  the return point builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceReturnBuilder
            (
            );
            /**Returns  the gohome point builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmAvoidancePointBuilder * TransferAvoidanceGohomeBuilder
            (
            );
            /**Returns  the cutter compensation type  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmPlanarBuilder::CutcomTypes CutcomType
            (
            );
            /**Sets  the cutter compensation type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomType
            (
                NXOpen::CAM::NcmPlanarBuilder::CutcomTypes cutcomType /** cutcomtype */ 
            );
            /**Returns  the cutter compensation minimum move builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::InheritableToolDepBuilder * CutcomMinimumMoveBuilder
            (
            );
            /**Returns  the cutter compensation minimum angle  <br> License requirements : cam_base ("CAM BASE") */
            public: double CutcomMinimumAngle
            (
            );
            /**Sets  the cutter compensation minimum angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomMinimumAngle
            (
                double minimumAngle /** minimumangle */ 
            );
            /**Returns  the cutter compensation output plane status  <br> License requirements : cam_base ("CAM BASE") */
            public: bool CutcomOutputPlane
            (
            );
            /**Sets  the cutter compensation output plane status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomOutputPlane
            (
                bool outputPlane /** outputplane */ 
            );
            /**Returns  the cutter compensation output contact point status  <br> License requirements : cam_base ("CAM BASE") */
            public: bool CutcomOutputContactPoint
            (
            );
            /**Sets  the cutter compensation output contact point status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomOutputContactPoint
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the cutter compensation tracking point selection  <br> License requirements : cam_base ("CAM BASE") */
            public: int CutcomTrackingPointType
            (
            );
            /**Sets  the cutter compensation tracking point selection  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomTrackingPointType
            (
                int newValue /** newvalue */ 
            );
            /**Returns  the clearance builder (inheritable tool dep)  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NcmClearanceBuilder * ClearanceBuilder
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
