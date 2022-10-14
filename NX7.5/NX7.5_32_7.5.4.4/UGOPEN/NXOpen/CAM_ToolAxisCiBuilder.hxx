#ifndef NXOpen_CAM_TOOLAXISCIBUILDER_HXX_INCLUDED
#define NXOpen_CAM_TOOLAXISCIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ToolAxisCiBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ToolAxisCiBuilder;
    }
    namespace CAM
    {
        class _ToolAxisCiBuilderBuilder;
        class ToolAxisCiBuilderImpl;
        /** Represents a tool axis ci Builder */
        class NXOPENCPPEXPORT  ToolAxisCiBuilder : public TaggedObject
        {
            private: ToolAxisCiBuilderImpl * m_toolaxiscibuilder_impl;
            private: friend class  _ToolAxisCiBuilderBuilder;
            protected: ToolAxisCiBuilder();
            public: ~ToolAxisCiBuilder();
            /**Returns  the tool axis types  <br> License requirements : None */
            public: int ToolAxis
            (
            );
            /**Sets  the tool axis types  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolAxis
            (
                int toolAxis /** the tool axis type */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif