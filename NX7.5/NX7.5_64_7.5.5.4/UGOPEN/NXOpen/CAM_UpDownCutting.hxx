#ifndef NXOpen_CAM_UPDOWNCUTTING_HXX_INCLUDED
#define NXOpen_CAM_UPDOWNCUTTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_UpDownCutting.ja
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
#include <NXOpen/CAM_UpDownCutting.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class UpDownCutting;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class _UpDownCuttingBuilder;
        class UpDownCuttingImpl;
        /**
            Represents a @link CAM::UpDownCutting CAM::UpDownCutting@endlink 
            */
        class NXOPENCPPEXPORT  UpDownCutting : public TaggedObject
        {
            private: UpDownCuttingImpl * m_updowncutting_impl;
            private: friend class  _UpDownCuttingBuilder;
            protected: UpDownCutting();
            public: ~UpDownCutting();
            /**Returns  the  ramp up angle  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * RampUpAngle
            (
            );
            /**Returns  the ramp down angle  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * RampDownAngle
            (
            );
            /**Returns  the apply at stepover toggle  <br> License requirements : None */
            public: bool ApplyAtStepover
            (
            );
            /**Sets  the apply at stepover toggle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetApplyAtStepover
            (
                bool propValue /** the Apply at Stepover value */
            );
            /**Returns  the optimize path toggle  <br> License requirements : None */
            public: bool OptimizePath
            (
            );
            /**Sets  the optimize path toggle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetOptimizePath
            (
                bool propValue /** the Optimize Path value */
            );
            /**Returns  the extend to boundary toggle  <br> License requirements : cam_base ("CAM BASE") */
            public: bool ExtendToBoundary
            (
            );
            /**Sets  the extend to boundary toggle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetExtendToBoundary
            (
                bool propValue /** the Extend to Boundary value */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
