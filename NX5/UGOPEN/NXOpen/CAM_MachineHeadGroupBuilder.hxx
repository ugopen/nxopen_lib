#ifndef NXOpen_CAM_MACHINEHEADGROUPBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MACHINEHEADGROUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MachineHeadGroupBuilder.ja
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
#include <NXOpen/CAM_ParamBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MachineHeadGroupBuilder;
    }
    namespace CAM
    {
        class ParamBuilder;
    }
    namespace CAM
    {
        class _MachineHeadGroupBuilderBuilder;
        /** Represents a MachineHeadGroup Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateMachineHeadGroupBuilder CAM::NCGroupCollection::CreateMachineHeadGroupBuilder@endlink  <br> */
        class NXOPENCPPEXPORT MachineHeadGroupBuilder : public CAM::ParamBuilder
        {
            private: friend class  _MachineHeadGroupBuilderBuilder;
            protected: MachineHeadGroupBuilder();
            /**Returns  the x distance  <br> License requirements : cam_base ("CAM BASE") */
            public: double XDistanceBuilder
            (
            );
            /**Sets  the x distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetXDistanceBuilder
            (
                double x_value /** the x distance value */
            );
            /**Returns  the y distance  <br> License requirements : cam_base ("CAM BASE") */
            public: double YDistanceBuilder
            (
            );
            /**Sets  the y distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetYDistanceBuilder
            (
                double y_value /** the y distance value */
            );
            /**Returns  the z distance  <br> License requirements : cam_base ("CAM BASE") */
            public: double ZDistanceBuilder
            (
            );
            /**Sets  the z distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetZDistanceBuilder
            (
                double z_value /** the z distance value */
            );
            /**Returns  the i direction  <br> License requirements : cam_base ("CAM BASE") */
            public: double IDirectionBuilder
            (
            );
            /**Sets  the i direction  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetIDirectionBuilder
            (
                double i_value /** the i direction value */
            );
            /**Returns  the j direction  <br> License requirements : cam_base ("CAM BASE") */
            public: double JDirectionBuilder
            (
            );
            /**Sets  the j direction  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetJDirectionBuilder
            (
                double j_value /** the j direction value */
            );
            /**Returns  the k direction  <br> License requirements : cam_base ("CAM BASE") */
            public: double KDirectionBuilder
            (
            );
            /**Sets  the k direction  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetKDirectionBuilder
            (
                double k_value /** the k direction value */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif