#ifndef NXOpen_CAM_TURNAVOIDANCEPATHPOINTSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TURNAVOIDANCEPATHPOINTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TurnAvoidancePathPointsBuilder.ja
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
        class TurnAvoidancePathPointsBuilder;
    }
    class NXObject;
    class Point;
    namespace CAM
    {
        class _TurnAvoidancePathPointsBuilderBuilder;
        class TurnAvoidancePathPointsBuilderImpl;
        /** Represents a turn avoidance path points builder 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  TurnAvoidancePathPointsBuilder : public NXOpen::TaggedObject
        {
            /** the cs modes 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum CsTypes
            {
                CsTypesWcs/** WCS */,
                CsTypesMcs/** MCS */
            };

            /** the motion to point type options 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum MotionTypes
            {
                MotionTypesAutomatic/** Motion to Point: Automatic */,
                MotionTypesDirect/** Motion to Point: Direct */,
                MotionTypesRadialThenAxial/** Motion to Point: Radial then Axial */,
                MotionTypesAxialThenRadial/** Motion to Point: Axial then Radial */
            };

            /** the feed rate type options 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum FeedrateModesTypes
            {
                FeedrateModesTypesRapid/** Feed Rate: Automatic */,
                FeedrateModesTypesApproachOrDepature/** Feed Rate: Direct */,
                FeedrateModesTypesEngageOrReturn/** Feed Rate: Radial then Axial */,
                FeedrateModesTypesCut/** Feed Rate: Axial then Radial */,
                FeedrateModesTypesCustom/** Feed Rate: Axial then Radial */
            };

            /** the custom feed rate unit options 
             <br>  Created in NX6.0.0.  <br>  
            */
            public: enum CustomFeedrateUnitTypes
            {
                CustomFeedrateUnitTypesNone/** Feed Rate: Automatic */,
                CustomFeedrateUnitTypesIpmOrMmpm/** Feed Rate: Direct */,
                CustomFeedrateUnitTypesIprOrMmpr/** Feed Rate: Radial then Axial */
            };

            /** the point status options 
             <br>  Created in NX6.0.2.  <br>  
            */
            public: enum PointStatus
            {
                PointStatusInactive/** Point Status: Inactive */,
                PointStatusActive/** Point Status: Active */
            };

            private: TurnAvoidancePathPointsBuilderImpl * m_turnavoidancepathpointsbuilder_impl;
            private: friend class  _TurnAvoidancePathPointsBuilderBuilder;
            protected: TurnAvoidancePathPointsBuilder();
            public: ~TurnAvoidancePathPointsBuilder();
            /**Returns  the cs mode 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidancePathPointsBuilder::CsTypes CsMode
            (
            );
            /**Sets  the cs mode 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCsMode
            (
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CsTypes csMode /** the cs mode value */
            );
            /** Get the values of an existing avoidance path point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void GetPointListData
            (
                int index /** the index of avoidance path point*/,
                NXOpen::NXObject ** specifyPoint /** selected point */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::MotionTypes* motionType /** the motionTypeColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::FeedrateModesTypes* feedrateType /** the feedrate Type */,
                double* customFeedrateValue /** the feedrateColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CustomFeedrateUnitTypes* customFeedrateUnit /** the feedrateUnitColumn */
            );
            /** Get the values of an existing avoidance path point 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: void GetPointData
            (
                int index /** the index of avoidance path point*/,
                NXOpen::NXObject ** specifyPoint /** selected point */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::MotionTypes* motionType /** the motionTypeColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::FeedrateModesTypes* feedrateType /** the feedrate Type */,
                double* customFeedrateValue /** the feedrateColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CustomFeedrateUnitTypes* customFeedrateUnit /** the feedrateUnitColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::PointStatus* pointStatus /** the point status */,
                int* startEventFlag /** the start event status */,
                NXOpen::NXObject ** startEventPath /** the start event path */,
                int* endEventFlag /** the end event status */,
                NXOpen::NXObject ** endEventPath /** the end event path */
            );
            /** Gets the values of an existing avoidance path point 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: void GetPointData
            (
                int index /** the index of avoidance path point*/,
                NXOpen::Point ** specifyPoint /** selected point */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::MotionTypes* motionType /** the motionTypeColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::FeedrateModesTypes* feedrateType /** the feedrate Type */,
                double* customFeedrateValue /** the feedrateColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CustomFeedrateUnitTypes* customFeedrateUnit /** the feedrateUnitColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::PointStatus* pointStatus /** the point status */,
                int* startEventFlag /** the start event status */,
                NXOpen::NXObject ** startEventPath /** the start event path */,
                int* endEventFlag /** the end event status */,
                NXOpen::NXObject ** endEventPath /** the end event path */,
                double* toolHolderAngle /** the tool holder angle */
            );
            /**Returns  the number of avoidance path points 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: int PointListDataNumberOfTrackPoints
            (
            );
            /** Create a new avoidance path point, name maybe changed if not unique 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPointListData
            (
                int index /** the index which new avoidance path point will be added after */,
                NXOpen::NXObject * specifyPoint /** selected point */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::MotionTypes motionType /** the motionTypeColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::FeedrateModesTypes feedrateType /** the feedrate Type */,
                double customFeedrateValue /** the feedrateColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CustomFeedrateUnitTypes customFeedrateUnit /** the feedrateUnitColumn */
            );
            /** Create a new avoidance path point, name maybe changed if not unique. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPointData
            (
                int index /** the index which new avoidance path point will be added after */,
                NXOpen::NXObject * specifyPoint /** selected point */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::MotionTypes motionType /** the motionTypeColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::FeedrateModesTypes feedrateType /** the feedrate Type */,
                double customFeedrateValue /** the feedrateColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CustomFeedrateUnitTypes customFeedrateUnit /** the feedrateUnitColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::PointStatus pointStatus /** the point status */,
                int startEventFlag /** the start event status */,
                NXOpen::NXObject * startEventPath /** the start event path */,
                int endEventFlag /** the end event status */,
                NXOpen::NXObject * endEventPath /** the end event path */
            );
            /** Creates a new avoidance path point, name maybe changed if not unique. 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPointData
            (
                int index /** the index which new avoidance path point will be added after */,
                NXOpen::Point * specifyPoint /** selected point */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::MotionTypes motionType /** the motionTypeColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::FeedrateModesTypes feedrateType /** the feedrate Type */,
                double customFeedrateValue /** the feedrateColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CustomFeedrateUnitTypes customFeedrateUnit /** the feedrateUnitColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::PointStatus pointStatus /** the point status */,
                int startEventFlag /** the start event status */,
                NXOpen::NXObject * startEventPath /** the start event path */,
                int endEventFlag /** the end event status */,
                NXOpen::NXObject * endEventPath /** the end event path */,
                double toolHolderAngle /** the tool holder angle */
            );
            /** Modify an existing avoidance path point,name maybe changed if not unique 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void Modify
            (
                int index /** the index of modified avoidance path point */,
                NXOpen::NXObject * specifyPoint /** selected point */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::MotionTypes motionType /** the motionTypeColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::FeedrateModesTypes feedrateType /** the feedrate Type */,
                double customFeedrateValue /** the feedrateColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CustomFeedrateUnitTypes customFeedrateUnit /** the feedrateUnitColumn */
            );
            /** Modify an existing avoidance path point,name maybe changed if not unique 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void ModifyData
            (
                int index /** the index of modified avoidance path point */,
                NXOpen::NXObject * specifyPoint /** selected point */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::MotionTypes motionType /** the motionTypeColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::FeedrateModesTypes feedrateType /** the feedrate Type */,
                double customFeedrateValue /** the feedrateColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CustomFeedrateUnitTypes customFeedrateUnit /** the feedrateUnitColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::PointStatus pointStatus /** the point status */,
                int startEventFlag /** the start event status */,
                NXOpen::NXObject * startEventPath /** the start event path */,
                int endEventFlag /** the end event status */,
                NXOpen::NXObject * endEventPath /** the end event path */
            );
            /** Modifies an existing avoidance path point,name maybe changed if not unique 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void ModifyData
            (
                int index /** the index of modified avoidance path point */,
                NXOpen::Point * specifyPoint /** selected point */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::MotionTypes motionType /** the motionTypeColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::FeedrateModesTypes feedrateType /** the feedrate Type */,
                double customFeedrateValue /** the feedrateColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::CustomFeedrateUnitTypes customFeedrateUnit /** the feedrateUnitColumn */,
                NXOpen::CAM::TurnAvoidancePathPointsBuilder::PointStatus pointStatus /** the point status */,
                int startEventFlag /** the start event status */,
                NXOpen::NXObject * startEventPath /** the start event path */,
                int endEventFlag /** the end event status */,
                NXOpen::NXObject * endEventPath /** the end event path */,
                double toolHolderAngle /** the tool holder angle */
            );
            /** Delete an existing avoidance path point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void Delete
            (
                int index /** the index of deleted avoidance path point */
            );
            /** Move up a avoidance path point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void MoveUp
            (
                int index /** the index of item which should be moved up*/
            );
            /** Move down a avoidance path point 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void MoveDown
            (
                int index /** the index of item which should be moved down*/
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