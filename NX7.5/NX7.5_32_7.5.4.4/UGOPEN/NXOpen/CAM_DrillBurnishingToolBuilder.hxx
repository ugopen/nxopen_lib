#ifndef NXOpen_CAM_DRILLBURNISHINGTOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DRILLBURNISHINGTOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DrillBurnishingToolBuilder.ja
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
#include <NXOpen/CAM_DrillToolBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class DrillBurnishingToolBuilder;
    }
    namespace CAM
    {
        class DrillToolBuilder;
    }
    namespace CAM
    {
        class _DrillBurnishingToolBuilderBuilder;
        class DrillBurnishingToolBuilderImpl;
        /** Represents a drill burnishing Tool Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateDrillBurnishingToolBuilder CAM::NCGroupCollection::CreateDrillBurnishingToolBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  DrillBurnishingToolBuilder : public CAM::DrillToolBuilder
        {
            private: DrillBurnishingToolBuilderImpl * m_drillburnishingtoolbuilder_impl;
            private: friend class  _DrillBurnishingToolBuilderBuilder;
            protected: DrillBurnishingToolBuilder();
            public: ~DrillBurnishingToolBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
