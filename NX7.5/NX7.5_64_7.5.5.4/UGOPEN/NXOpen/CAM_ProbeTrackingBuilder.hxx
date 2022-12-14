#ifndef NXOpen_CAM_PROBETRACKINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_PROBETRACKINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ProbeTrackingBuilder.ja
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
#include <NXOpen/CAM_SolidTrackingBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ProbeTrackingBuilder;
    }
    namespace CAM
    {
        class SolidTrackingBuilder;
    }
    class NXObject;
    namespace CAM
    {
        class _ProbeTrackingBuilderBuilder;
        class ProbeTrackingBuilderImpl;
        /** Represents a ProbeTracking Builder  <br> To create a new instance of this class, use @link CAM::Tool::CreateProbeTrackingBuilder CAM::Tool::CreateProbeTrackingBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ProbeTrackingBuilder : public CAM::SolidTrackingBuilder
        {
            private: ProbeTrackingBuilderImpl * m_probetrackingbuilder_impl;
            private: friend class  _ProbeTrackingBuilderBuilder;
            protected: ProbeTrackingBuilder();
            public: ~ProbeTrackingBuilder();
            /**Returns  the stem axis  <br> License requirements : None */
            public: NXOpen::NXObject * Axis
            (
            );
            /**Sets  the stem axis  <br> License requirements : None */
            public: void SetAxis
            (
                NXOpen::NXObject * axis /** the axis tag */
            );
            /**Returns  the stem top  <br> License requirements : None */
            public: NXOpen::NXObject * StemTop
            (
            );
            /**Sets  the stem top  <br> License requirements : None */
            public: void SetStemTop
            (
                NXOpen::NXObject * stemTop /** the stem_top tag */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
