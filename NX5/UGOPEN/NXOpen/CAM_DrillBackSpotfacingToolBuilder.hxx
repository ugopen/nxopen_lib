#ifndef NXOpen_CAM_DRILLBACKSPOTFACINGTOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DRILLBACKSPOTFACINGTOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DrillBackSpotfacingToolBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAM_DrillToolBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class DrillBackSpotfacingToolBuilder;
    }
    namespace CAM
    {
        class DrillToolBuilder;
    }
    namespace CAM
    {
        class _DrillBackSpotfacingToolBuilderBuilder;
        /** Represents a drill back spotfacing Tool Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateDrillBackSpotfacingToolBuilder CAM::NCGroupCollection::CreateDrillBackSpotfacingToolBuilder@endlink  <br> */
        class NXOPENCPPEXPORT DrillBackSpotfacingToolBuilder : public CAM::DrillToolBuilder
        {
            private: friend class  _DrillBackSpotfacingToolBuilderBuilder;
            protected: DrillBackSpotfacingToolBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
