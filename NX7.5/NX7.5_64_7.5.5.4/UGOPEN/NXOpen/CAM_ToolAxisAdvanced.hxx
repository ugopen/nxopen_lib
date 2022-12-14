#ifndef NXOpen_CAM_TOOLAXISADVANCED_HXX_INCLUDED
#define NXOpen_CAM_TOOLAXISADVANCED_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ToolAxisAdvanced.ja
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
#include <NXOpen/CAM_ToolAxisAdvanced.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ToolAxisAdvanced;
    }
    namespace CAM
    {
        class InterpolateVector;
    }
    namespace CAM
    {
        class _ToolAxisAdvancedBuilder;
        class ToolAxisAdvancedImpl;
        /** Represents a Tool Axis Advanced Builder */
        class NXOPENCPPEXPORT  ToolAxisAdvanced : public TaggedObject
        {
            /** Available types for Tool Axis Advanced type*/
            public: enum Type
            {
                TypeAutomatic/** Automatic */,
                TypeInterpolateVector/** Interpolate Vector*/,
                TypeBladeSwarf/** Blade Swarf */,
                TypeFollowBladeUv/** Follow Blade UV */
            };

            /** Rotate About type*/
            public: enum RotateAboutType
            {
                RotateAboutTypePartAxis/** Part Axis */,
                RotateAboutTypeBlade/** Blade */
            };

            private: ToolAxisAdvancedImpl * m_toolaxisadvanced_impl;
            private: friend class  _ToolAxisAdvancedBuilder;
            protected: ToolAxisAdvanced();
            public: ~ToolAxisAdvanced();
            /**Returns  the tool axis types  <br> License requirements : None */
            public: NXOpen::CAM::ToolAxisAdvanced::Type ToolAxisType
            (
            );
            /**Sets  the tool axis types  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolAxisType
            (
                NXOpen::CAM::ToolAxisAdvanced::Type toolAxis /** the tool axis type */
            );
            /**Returns  the tilt angle  <br> License requirements : None */
            public: double TiltAngle
            (
            );
            /**Sets  the tilt angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTiltAngle
            (
                double tiltAngle /** the tilt angle value */
            );
            /**Returns  the leading angle  <br> License requirements : None */
            public: double LeadingAngle
            (
            );
            /**Sets  the leading angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetLeadingAngle
            (
                double leadingAngle /** the leading angle value */
            );
            /**Returns  the splitter angle  <br> License requirements : None */
            public: double SplitterAngle
            (
            );
            /**Sets  the splitter angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSplitterAngle
            (
                double splitterAngle /** the leading angle value */
            );
            /**Returns  the trailing angle  <br> License requirements : None */
            public: double TrailingAngle
            (
            );
            /**Sets  the trailing angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTrailingAngle
            (
                double trailingAngle /** the leading angle value */
            );
            /**Returns  the Interpolate Vector builder   <br> License requirements : None */
            public: NXOpen::CAM::InterpolateVector * InterpolateVector
            (
            );
            /**Returns  the rotate about  <br> License requirements : None */
            public: NXOpen::CAM::ToolAxisAdvanced::RotateAboutType RotateAbout
            (
            );
            /**Sets  the rotate about  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRotateAbout
            (
                NXOpen::CAM::ToolAxisAdvanced::RotateAboutType rotateAbout /** the rotate about value */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
