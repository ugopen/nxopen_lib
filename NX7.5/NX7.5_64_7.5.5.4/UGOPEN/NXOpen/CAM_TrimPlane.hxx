#ifndef NXOpen_CAM_TRIMPLANE_HXX_INCLUDED
#define NXOpen_CAM_TRIMPLANE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_TrimPlane.ja
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
#include <NXOpen/CAM_TrimPlane.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class TrimPlane;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    class Point;
    namespace CAM
    {
        class _TrimPlaneBuilder;
        class TrimPlaneImpl;
        /** Represents Trim Plane */
        class NXOPENCPPEXPORT  TrimPlane : public TaggedObject
        {
            /** The limit options */
            public: enum LimitOptions
            {
                LimitOptionsNone/** Plane is inactive. */,
                LimitOptionsPoint/** Plane is defined by a point. */,
                LimitOptionsDistance/** Plane is defined by a distance value. */
            };

            /** The content options */
            public: enum Content
            {
                ContentRadial/** radial */,
                ContentAxial/** axial. */
            };

            private: TrimPlaneImpl * m_trimplane_impl;
            private: friend class  _TrimPlaneBuilder;
            protected: TrimPlane();
            public: ~TrimPlane();
            /**Returns  the limit option  <br> License requirements : None */
            public: NXOpen::CAM::TrimPlane::LimitOptions LimitOption
            (
            );
            /**Sets  the limit option  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLimitOption
            (
                NXOpen::CAM::TrimPlane::LimitOptions trimPlaneMode /** the limit option */
            );
            /**Returns  the trim plane point  <br> License requirements : None */
            public: NXOpen::Point * Point
            (
            );
            /**Sets  the trim plane point  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPoint
            (
                NXOpen::Point * point /** the trim plane point */
            );
            /**Returns  the radius  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * Radius
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
