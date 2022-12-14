#ifndef NXOpen_CAM_CLEANUPSETTINGS_HXX_INCLUDED
#define NXOpen_CAM_CLEANUPSETTINGS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CleanupSettings.ja
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
#include <NXOpen/CAM_CleanupSettings.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class CleanupSettings;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class _CleanupSettingsBuilder;
        class CleanupSettingsImpl;
        /**    Represents a @link CAM::CleanupSettings CAM::CleanupSettings@endlink     */
        class NXOPENCPPEXPORT  CleanupSettings : public TaggedObject
        {
            private: CleanupSettingsImpl * m_cleanupsettings_impl;
            private: friend class  _CleanupSettingsBuilder;
            protected: CleanupSettings();
            public: ~CleanupSettings();
            /**Returns  the Valleys, Cleanup Geometry Settings <br> License requirements : None */
            public: bool Valleys
            (
            );
            /**Sets  the Valleys, Cleanup Geometry Settings <br> License requirements : cam_base ("CAM BASE") */
            public: void SetValleys
            (
                bool cleanupSettingDoubleContacts /** the Valleys value */
            );
            /**Returns  the Auto Save, Cleanup Geometry Settings <br> License requirements : None */
            public: bool AutoSave
            (
            );
            /**Sets  the Auto Save, Cleanup Geometry Settings <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAutoSave
            (
                bool cleanupAutoSave /** the AutoSave value */
            );
            /**Returns  the Extra Cross Drive, Cleanup Geometry Settings <br> License requirements : cam_base ("CAM BASE") */
            public: bool ExtraCrossDrive
            (
            );
            /**Sets  the Extra Cross Drive, Cleanup Geometry Settings <br> License requirements : cam_base ("CAM BASE") */
            public: void SetExtraCrossDrive
            (
                bool cleanupSettingExtraCrossDrive /** the Extra Cross Drive value */
            );
            /**Returns  the Steep Areas, Cleanup Geometry Settings <br> License requirements : cam_base ("CAM BASE") */
            public: bool SteepAreas
            (
            );
            /**Sets  the Steep Areas, Cleanup Geometry Settings <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSteepAreas
            (
                bool cleanupSettingSteepAreas /** the Steep Areas value */
            );
            /**Returns  the Directional, Cleanup Geometry Settings <br> License requirements : None */
            public: bool Directional
            (
            );
            /**Sets  the Directional, Cleanup Geometry Settings <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDirectional
            (
                bool cleanupSettingSteepDirectional /** the Directional value */
            );
            /**Returns  the  builder of Steep Angle, Cleanup Geometry Settings <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * SteepAngle
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
