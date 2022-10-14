#ifndef NXOpen_CAM_OUTPUTUNCUTREGIONS_HXX_INCLUDED
#define NXOpen_CAM_OUTPUTUNCUTREGIONS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_OutputUncutRegions.ja
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
#include <NXOpen/CAM_OutputUncutRegions.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class OutputUncutRegions;
    }
    namespace CAM
    {
        class _OutputUncutRegionsBuilder;
        class OutputUncutRegionsImpl;
        /**
            Represents a @link CAM::OutputUncutRegions CAM::OutputUncutRegions@endlink 
            */
        class NXOPENCPPEXPORT  OutputUncutRegions : public TaggedObject
        {
            private: OutputUncutRegionsImpl * m_outputuncutregions_impl;
            private: friend class  _OutputUncutRegionsBuilder;
            protected: OutputUncutRegions();
            public: ~OutputUncutRegions();
            /**Returns  the overlap distance  <br> License requirements : None */
            public: double OverlapDistance
            (
            );
            /**Sets  the overlap distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOverlapDistance
            (
                double overlapDist /** The Uncut Overlap Distance value */
            );
            /**Returns  the auto save boundary toggle <br> License requirements : None */
            public: bool AutoSaveBoundary
            (
            );
            /**Sets  the auto save boundary toggle <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAutoSaveBoundary
            (
                bool outputBnd /** The Uncut output boundary value */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif