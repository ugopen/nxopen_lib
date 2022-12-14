#ifndef NXOpen_CAM_DISPLAYSILHOUETTE_HXX_INCLUDED
#define NXOpen_CAM_DISPLAYSILHOUETTE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DisplaySilhouette.ja
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
#include <NXOpen/CAM_DisplaySilhouette.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class DisplaySilhouette;
    }
    namespace CAM
    {
        class _DisplaySilhouetteBuilder;
        class DisplaySilhouetteImpl;
        /** Represents a display silhouette Builder  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT  DisplaySilhouette : public TaggedObject
        {
            private: DisplaySilhouetteImpl * m_displaysilhouette_impl;
            private: friend class  _DisplaySilhouetteBuilder;
            protected: DisplaySilhouette();
            public: ~DisplaySilhouette();
            /**Returns  the percent of tool.The range is 1-100.  <br> License requirements : None */
            public: double PercentOfTool
            (
            );
            /**Sets  the percent of tool.The range is 1-100.  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPercentOfTool
            (
                double percentTool /** the percent of tool.The range is 1-100. */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
