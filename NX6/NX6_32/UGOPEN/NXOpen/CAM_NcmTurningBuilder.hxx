#ifndef NXOpen_CAM_NCMTURNINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NCMTURNINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmTurningBuilder.ja
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
        class NcmTurningBuilder;
    }
    namespace CAM
    {
        class NcmSubopBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceApproachBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceClearanceBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceDepartureBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceFromBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceGohomeBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceReturnBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceStartBuilder;
    }
    namespace CAM
    {
        class TurnAvoidanceStartOfEngageBuilder;
    }
    namespace CAM
    {
        class _NcmTurningBuilderBuilder;
        /** Represents a CAM.NcmTurningBuilder */
        class NXOPENCPPEXPORT NcmTurningBuilder : public CAM::NcmSubopBuilder
        {
            private: friend class  _NcmTurningBuilderBuilder;
            protected: NcmTurningBuilder();
            /**Returns  the avoidance from builder <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceFromBuilder * AvoidanceFromBuilder
            (
            );
            /**Returns  the avoidance start builder <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceStartBuilder * AvoidanceStartBuilder
            (
            );
            /**Returns  the start of engage builder  <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceStartOfEngageBuilder * AvoidanceStartOfEngageBuilder
            (
            );
            /**Returns  the departure path builder  <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceDepartureBuilder * AvoidanceDepartureBuilder
            (
            );
            /**Returns  the return path builder  <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceReturnBuilder * AvoidanceReturnBuilder
            (
            );
            /**Returns  the gohome point builder  <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceGohomeBuilder * AvoidanceGohomeBuilder
            (
            );
            /**Returns  the prefer direct motion to start of engage  <br> License requirements : None */
            public: bool AvoidanceToStartOfEngage
            (
            );
            /**Sets  the prefer direct motion to start of engage  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAvoidanceToStartOfEngage
            (
                bool avoidanceToStartOfEngage /** the prefer direct motion to start of engage */
            );
            /**Returns  the prefer direct motion between regions  <br> License requirements : None */
            public: bool AvoidanceBetweenRegions
            (
            );
            /**Sets  the prefer direct motion between regions  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAvoidanceBetweenRegions
            (
                bool avoidanceBetweenRegions /** the prefer direct motion between regions */
            );
            /**Returns  the prefer direct motion after last retract  <br> License requirements : None */
            public: bool AvoidanceAfterLastRetract
            (
            );
            /**Sets  the prefer direct motion after last retract  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAvoidanceAfterLastRetract
            (
                bool avoidanceAfterLastRetract /** the prefer direct motion after last retract */
            );
            /**Returns  the approach path builder  <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceApproachBuilder * AvoidanceApproachBuilder
            (
            );
            /**Returns  the clearance builder  <br> License requirements : None */
            public: NXOpen::CAM::TurnAvoidanceClearanceBuilder * AvoidanceClearanceBuilder
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
