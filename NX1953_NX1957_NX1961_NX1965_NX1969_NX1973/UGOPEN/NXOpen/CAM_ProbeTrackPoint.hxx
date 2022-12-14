#ifndef NXOpen_CAM_PROBETRACKPOINT_HXX_INCLUDED
#define NXOpen_CAM_PROBETRACKPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ProbeTrackPoint.ja
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
#include <NXOpen/CAM_SolidTrackPoint.hxx>
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
        class ProbeTrackPoint;
    }
    namespace CAM
    {
        class SolidTrackPoint;
    }
    namespace CAM
    {
        class _ProbeTrackPointBuilder;
        class ProbeTrackPointImpl;
        /** Represents an Track Point  <br> To obtain an instance of this class us @link NXOpen::CAM::TrackPointCollection NXOpen::CAM::TrackPointCollection@endlink   <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ProbeTrackPoint : public NXOpen::CAM::SolidTrackPoint
        {
            private: ProbeTrackPointImpl * m_probetrackpoint_impl;
            private: friend class  _ProbeTrackPointBuilder;
            protected: ProbeTrackPoint();
            public: ~ProbeTrackPoint();
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
