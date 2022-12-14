#ifndef NXOpen_CAM_SOLIDTRACKPOINT_HXX_INCLUDED
#define NXOpen_CAM_SOLIDTRACKPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_SolidTrackPoint.ja
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
#include <NXOpen/CAM_TrackPoint.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class SolidTrackPoint;
    }
    namespace CAM
    {
        class TrackPoint;
    }
    namespace CAM
    {
        class _SolidTrackPointBuilder;
        class SolidTrackPointImpl;
        /** Represents an Track Point  <br> To obtain an instance of this class us @link CAM::TrackPointCollection CAM::TrackPointCollection@endlink  <br> */
        class NXOPENCPPEXPORT  SolidTrackPoint : public CAM::TrackPoint
        {
            private: SolidTrackPointImpl * m_solidtrackpoint_impl;
            private: friend class  _SolidTrackPointBuilder;
            protected: SolidTrackPoint();
            public: ~SolidTrackPoint();
        };
    }
}
#undef EXPORTLIBRARY
#endif
