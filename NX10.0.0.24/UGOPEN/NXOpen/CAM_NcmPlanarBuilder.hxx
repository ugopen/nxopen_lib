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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAM_NcmTransfer.hxx>
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
        class NcmPlanarEngRetBuilder;
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
        class NcmTransfer;
    }
    class Point;
    namespace CAM
    {
        class _NcmPlanarBuilderBuilder;
        class NcmPlanarBuilderImpl;
        /**
            Represents a @link NXOpen::CAM::NcmPlanarBuilder NXOpen::CAM::NcmPlanarBuilder@endlink 
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  NcmPlanarBuilder : public NXOpen::CAM::NcmSubopBuilder
        {
            /** Available options for output of pre-drill points in planar milling */
            public: enum PredrillPointsOutputOptions
            {
                PredrillPointsOutputOptionsNone/** No Pre-Drill points */,
                PredrillPointsOutputOptionsAllRegions/** Pre-Drill Points for all regions */,
                PredrillPointsOutputOptionsBottomRegions/** Pre-Drill Points for bottom regions only*/
            };

            /** Available strategies for transfer within levels in planar milling */
            public: enum TransferWithinLevelsWiths
            {
                TransferWithinLevelsWithsUseEngret/** Use engage and retract defs */,
                TransferWithinLevelsWithsFollowBoundary/** follow boundary (for future use) */,
                TransferWithinLevelsWithsLiftPlunge/** lift and plunge */,
                TransferWithinLevelsWithsNone/** none */,
                TransferWithinLevelsWithsSmooth/** smooth */
            };

            /** Available types for transfer within levels in planar milling */
            public: enum TransferWithinLevelsTypes
            {
                TransferWithinLevelsTypesLowestSafeZ/** lowest Safe Z */,
                TransferWithinLevelsTypesPrevPlane/** previous plane */,
                TransferWithinLevelsTypesDirect/** direct */,
                TransferWithinLevelsTypesClearance/** tool axis to clearance */,
                TransferWithinLevelsTypesBlankPlane/** Blank Plane */,
                TransferWithinLevelsTypesShortestToClearance/** shortest to clearance */,
                TransferWithinLevelsTypesCutPlaneToClearance/** cut plane to clearance */,
                TransferWithinLevelsTypesSmooth/** smooth */
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
                TransferBetweenRegionsTypesClearance/** tool axis to clearance */,
                TransferBetweenRegionsTypesPrevPlane/** previous plane */,
                TransferBetweenRegionsTypesDirect/** direct */,
                TransferBetweenRegionsTypesLowestSafeZ/** lowest safe z */,
                TransferBetweenRegionsTypesBlankPlane/** Blank Plane */,
                TransferBetweenRegionsTypesShortestToClearance/** shortest to clearance */,
                TransferBetweenRegionsTypesCutPlaneToClearance/** cut plane to clearance */
            };

            /** Available strategies for initial engage in planar milling */
            public: enum InitialEng
            {
                InitialEngInherit/** Use engage defs */,
                InitialEngLift/** lift */,
                InitialEngNone/** none */
            };

            /** Available types for initial clearance in planar milling */
            public: enum InitialTypes
            {
                InitialTypesClearance/** tool axis to clearance */,
                InitialTypesDistance/** distance */,
                InitialTypesNone/** none */,
                InitialTypesBlankPlane/** blank plane */,
                InitialTypesShortestDistanceToClearance/** shortest distance to clearance */,
                InitialTypesCutPlaneToClearance/** cut plane to clearance */
            };

            /** Available strategies for final retract in planar milling */
            public: enum FinalRet
            {
                FinalRetInherit/** Use retract defs */,
                FinalRetPlunge/** plunge */,
                FinalRetNone/** none */
            };

            /** Available types for final clearance in planar milling */
            public: enum FinalTypes
            {
                FinalTypesClearance/** tool axis clearance */,
                FinalTypesDistance/** distance */,
                FinalTypesNone/** none */,
                FinalTypesShortestDistanceToClearance/** shortest distance to clearance */,
                FinalTypesCutPlaneToClearance/** cut plane to clearance */
            };

            /** Available types for cutter compensation in planar milling */
            public: enum CutcomTypes
            {
                CutcomTypesNone/** cutter compensation off */,
                CutcomTypesAllFinishPasses/** cutter compensation on all finish passes */,
                CutcomTypesFinalFinishPass/** cutter compensation on last finish pass */
            };

            private: NcmPlanarBuilderImpl * m_ncmplanarbuilder_impl;
            private: friend class  _NcmPlanarBuilderBuilder;
            protected: NcmPlanarBuilder();
            public: ~NcmPlanarBuilder();
            /**Returns  the default engage closed area builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarEngRetBuilder * EngageClosedAreaBuilder
            (
            );
            /**Returns  the default engage open area builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarEngRetBuilder * EngageOpenAreaBuilder
            (
            );
            /**Returns  the flag to control limitation of engage and retract motions to cut regions 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool LimitEngRetToCutRegion
            (
            );
            /**Sets  the flag to control limitation of engage and retract motions to cut regions 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLimitEngRetToCutRegion
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the initial engage closed area builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarEngRetBuilder * EngageInitialClosedBuilder
            (
            );
            /**Returns  the initial engage open area builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarEngRetBuilder * EngageInitialOpenBuilder
            (
            );
            /**Returns  the retract area builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarEngRetBuilder * RetractAreaBuilder
            (
            );
            /**Returns  the final retract builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarEngRetBuilder * RetractFinalBuilder
            (
            );
            /**Returns  the smoothing builder 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmSmoothingBuilder * SmoothingBuilder
            (
            );
            /**Returns  the start/drill points overlap distance builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * OverlapDistanceBuilder
            (
            );
            /**Returns  the pre-drill points output option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarBuilder::PredrillPointsOutputOptions PredrillPointsOutput
            (
            );
            /**Sets  the pre-drill points output option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPredrillPointsOutput
            (
                NXOpen::CAM::NcmPlanarBuilder::PredrillPointsOutputOptions newValue /** newvalue */ 
            );
            /** The pre-drill points  @return  Array of points 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Point *> GetPredrillPoints
            (
            );
            /** The pre-drill points 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPredrillPoints
            (
                const std::vector<NXOpen::Point *> & predrillPoints /** Array of points */
            );
            /**Returns  the pre-drill points use effective distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool PredrillPointsUseEffectDist
            (
            );
            /**Sets  the pre-drill points use effective distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPredrillPointsUseEffectDist
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the pre-drill points effective distance builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * PredrillPointsEffectDistBuilder
            (
            );
            /**Returns  the transfer within levels strategy 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarBuilder::TransferWithinLevelsWiths TransferWithinLevelsWith
            (
            );
            /**Sets  the transfer within levels strategy 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTransferWithinLevelsWith
            (
                NXOpen::CAM::NcmPlanarBuilder::TransferWithinLevelsWiths newValue /** newvalue */ 
            );
            /**Returns  the transfer within levels max follow distance builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferWithinLevelsMaxFollowDistanceBuilder
            (
            );
            /**Returns  the transfer within levels height builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferWithinLevelsHeightBuilder
            (
            );
            /**Returns  the transfer within levels type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarBuilder::TransferWithinLevelsTypes TransferWithinLevelsType
            (
            );
            /**Sets  the transfer within levels type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTransferWithinLevelsType
            (
                NXOpen::CAM::NcmPlanarBuilder::TransferWithinLevelsTypes transferType /** transfertype */ 
            );
            /**Returns  the transfer within levels safe distance builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferWithinLevelsSafeDistanceBuilder
            (
            );
            /**Returns  the transfer between levels type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarBuilder::TransferBetweenLevelsTypes TransferBetweenLevelsType
            (
            );
            /**Sets  the transfer between levels type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTransferBetweenLevelsType
            (
                NXOpen::CAM::NcmPlanarBuilder::TransferBetweenLevelsTypes transferType /** transfertype */ 
            );
            /**Returns  the transfer between levels safe distance builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * TransferBetweenLevelsSafeDistanceBuilder
            (
            );
            /**Returns  the transfer between regions type 
             <br>  @deprecated Deprecated in NX9.0.0.  Please use @link NXOpen::CAM::NcmTransfer::Type NXOpen::CAM::NcmTransfer::Type@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Please use NXOpen::CAM::NcmTransfer::Type instead.") NXOpen::CAM::NcmPlanarBuilder::TransferBetweenRegionsTypes TransferBetweenRegionsType
            (
            );
            /**Sets  the transfer between regions type 
             <br>  @deprecated Deprecated in NX9.0.0.  Please use @link NXOpen::CAM::NcmTransfer::Type NXOpen::CAM::NcmTransfer::Type@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Please use NXOpen::CAM::NcmTransfer::Type instead.") void SetTransferBetweenRegionsType
            (
                NXOpen::CAM::NcmPlanarBuilder::TransferBetweenRegionsTypes transferType /** transfertype */ 
            );
            /**Returns  the transfer between regions safe distance builder (inheritable tool dep) 
             <br>  @deprecated Deprecated in NX9.0.0.  Please use @link NXOpen::CAM::NcmTransfer::SafeDistanceBuilder NXOpen::CAM::NcmTransfer::SafeDistanceBuilder@endlink  instead. <br>  

             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  Please use NXOpen::CAM::NcmTransfer::SafeDistanceBuilder instead.") NXOpen::CAM::InheritableToolDepBuilder * TransferBetweenRegionsSafeDistanceBuilder
            (
            );
            /**Returns  the initial type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarBuilder::InitialTypes InitialType
            (
            );
            /**Sets  the initial type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetInitialType
            (
                NXOpen::CAM::NcmPlanarBuilder::InitialTypes initialType /** initialtype */ 
            );
            /**Returns  the initial safe distance builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * InitialSafeDistanceBuilder
            (
            );
            /**Returns  the final type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarBuilder::FinalTypes FinalType
            (
            );
            /**Sets  the final type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFinalType
            (
                NXOpen::CAM::NcmPlanarBuilder::FinalTypes finalType /** finaltype */ 
            );
            /**Returns  the final safe distance builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * FinalSafeDistanceBuilder
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
            /**Returns  the cutter compensation type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarBuilder::CutcomTypes CutcomType
            (
            );
            /**Sets  the cutter compensation type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomType
            (
                NXOpen::CAM::NcmPlanarBuilder::CutcomTypes cutcomType /** cutcomtype */ 
            );
            /**Returns  the cutter compensation minimum move builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * CutcomMinimumMoveBuilder
            (
            );
            /**Returns  the cutter compensation minimum angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double CutcomMinimumAngle
            (
            );
            /**Sets  the cutter compensation minimum angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomMinimumAngle
            (
                double minimumAngle /** minimumangle */ 
            );
            /**Returns  the cutter compensation output plane status 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool CutcomOutputPlane
            (
            );
            /**Sets  the cutter compensation output plane status 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomOutputPlane
            (
                bool outputPlane /** outputplane */ 
            );
            /**Returns  the suppress cutter compensation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool SuppressCutcom
            (
            );
            /**Sets  the suppress cutter compensation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSuppressCutcom
            (
                bool suppressCutcom /** suppresscutcom */ 
            );
            /**Returns  the cutter compensation output contact point status 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool CutcomOutputContactPoint
            (
            );
            /**Sets  the cutter compensation output contact point status 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomOutputContactPoint
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the cutter compensation tracking point selection 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int CutcomTrackingPointType
            (
            );
            /**Sets  the cutter compensation tracking point selection 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomTrackingPointType
            (
                int newValue /** newvalue */ 
            );
            /**Returns  the clearance builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmClearanceBuilder * ClearanceBuilder
            (
            );
            /**Returns  the Transfer Between Regions builder  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmTransfer * TransferBetweenRegionsBuilder
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