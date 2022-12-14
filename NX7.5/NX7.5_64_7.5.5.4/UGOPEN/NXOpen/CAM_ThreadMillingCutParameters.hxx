#ifndef NXOpen_CAM_THREADMILLINGCUTPARAMETERS_HXX_INCLUDED
#define NXOpen_CAM_THREADMILLINGCUTPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ThreadMillingCutParameters.ja
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
#include <NXOpen/CAM_ThreadMillingCutParameters.hxx>
#include <NXOpen/CAM_CutParameters.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ThreadMillingCutParameters;
    }
    namespace CAM
    {
        class CutParameters;
    }
    namespace CAM
    {
        class VerticalPosition;
    }
    namespace CAM
    {
        class _ThreadMillingCutParametersBuilder;
        class ThreadMillingCutParametersImpl;
        /** Represents a ThreadMillingCutParameters Builder */
        class NXOPENCPPEXPORT  ThreadMillingCutParameters : public CAM::CutParameters
        {
            /** cut direction options */
            public: enum CutDirectionTypes
            {
                CutDirectionTypesClimb/** Climb cut */,
                CutDirectionTypesConventional/** Conventional cut */
            };

            private: ThreadMillingCutParametersImpl * m_threadmillingcutparameters_impl;
            private: friend class  _ThreadMillingCutParametersBuilder;
            protected: ThreadMillingCutParameters();
            public: ~ThreadMillingCutParameters();
            /**Returns  the cut direction  <br> License requirements : None */
            public: NXOpen::CAM::ThreadMillingCutParameters::CutDirectionTypes CutDirection
            (
            );
            /**Sets  the cut direction  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutDirection
            (
                NXOpen::CAM::ThreadMillingCutParameters::CutDirectionTypes cutDir /** the cut directon type */
            );
            /**Returns  the top offset  <br> License requirements : None */
            public: NXOpen::CAM::VerticalPosition * TopOffset
            (
            );
            /**Returns  the bottom offset  <br> License requirements : None */
            public: NXOpen::CAM::VerticalPosition * BottomOffset
            (
            );
            /**Returns  the continuous cut  <br> License requirements : None */
            public: bool ContinuousCut
            (
            );
            /**Sets  the continuous cut  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetContinuousCut
            (
                bool continuousCut /** the continuous cut */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
