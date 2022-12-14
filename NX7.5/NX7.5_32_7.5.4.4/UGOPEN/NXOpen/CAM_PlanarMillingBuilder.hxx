#ifndef NXOpen_CAM_PLANARMILLINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_PLANARMILLINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_PlanarMillingBuilder.ja
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
#include <NXOpen/CAM_PlanarOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class PlanarMillingBuilder;
    }
    namespace CAM
    {
        class CutLevelPlanar;
    }
    namespace CAM
    {
        class MultiplePassesBuilder;
    }
    namespace CAM
    {
        class PlanarOperationBuilder;
    }
    namespace CAM
    {
        class _PlanarMillingBuilderBuilder;
        class PlanarMillingBuilderImpl;
        /** Represents a PlanarMilling Builder  <br> To create a new instance of this class, use @link CAM::OperationCollection::CreatePlanarMillingBuilder CAM::OperationCollection::CreatePlanarMillingBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  PlanarMillingBuilder : public CAM::PlanarOperationBuilder
        {
            private: PlanarMillingBuilderImpl * m_planarmillingbuilder_impl;
            private: friend class  _PlanarMillingBuilderBuilder;
            protected: PlanarMillingBuilder();
            public: ~PlanarMillingBuilder();
            /**Returns  the Save 2D In-Process Workpiece  <br> License requirements : None */
            public: bool Save2dIpw
            (
            );
            /**Sets  the Save 2D In-Process Workpiece  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSave2dIpw
            (
                bool saveMethod /** The In-Process Workpiece Save Method value */
            );
            /**Returns  the drive point  <br> License requirements : None */
            public: int DrivePoint
            (
            );
            /**Sets  the drive point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDrivePoint
            (
                int drivePoint /** The drive point value */
            );
            /**Returns  the Z-Depth Offset  <br> License requirements : None */
            public: double ZdepthOffset
            (
            );
            /**Sets  the Z-Depth Offset  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetZdepthOffset
            (
                double offset /** offset */ 
            );
            /**Returns  the Multiple Passes builder  <br> License requirements : None */
            public: NXOpen::CAM::MultiplePassesBuilder * MultiplePasses
            (
            );
            /**Returns  the Planar Mill Cut Level builder  <br> License requirements : None */
            public: NXOpen::CAM::CutLevelPlanar * CutLevel
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
