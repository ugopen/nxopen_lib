#ifndef NXOpen_ANNOTATIONS_CENTERLINE2DSETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_CENTERLINE2DSETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_Centerline2dSettingsBuilder.ja
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
#include <NXOpen/Annotations_Centerline2dSettingsBuilder.hxx>
#include <NXOpen/Annotations_CenterlineSettingsBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class Centerline2dSettingsBuilder;
    }
    namespace Annotations
    {
        class CenterlineSettingsBuilder;
    }
    namespace Annotations
    {
        class _Centerline2dSettingsBuilderBuilder;
        class Centerline2dSettingsBuilderImpl;
        /** Represents a Builder for Centerline2dSettings.*/
        class NXOPENCPPEXPORT  Centerline2dSettingsBuilder : public Annotations::CenterlineSettingsBuilder
        {
            private: Centerline2dSettingsBuilderImpl * m_centerline2dsettingsbuilder_impl;
            private: friend class  _Centerline2dSettingsBuilderBuilder;
            protected: Centerline2dSettingsBuilder();
            public: ~Centerline2dSettingsBuilder();
            /**Returns  the short dash size parameter for 2D Centerline  <br> License requirements : None */
            public: double Size
            (
            );
            /**Sets  the short dash size parameter for 2D Centerline  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSize
            (
                double size /** size */ 
            );
            /**Returns  the extension parameter for 2D Centerline <br> License requirements : None */
            public: double Extension
            (
            );
            /**Sets  the extension parameter for 2D Centerline <br> License requirements : drafting ("DRAFTING") */
            public: void SetExtension
            (
                double extension /** extension */ 
            );
            /**Returns  the individual extension distance On/Off parameter for 2D Centerline <br> License requirements : None */
            public: bool IndividualDistance
            (
            );
            /**Sets  the individual extension distance On/Off parameter for 2D Centerline <br> License requirements : drafting ("DRAFTING") */
            public: void SetIndividualDistance
            (
                bool individualDistance /** individualdistance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
