#ifndef NXOpen_CAM_DRILLCOUNTERBORETOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DRILLCOUNTERBORETOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DrillCounterboreToolBuilder.ja
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
        class DrillCounterboreToolBuilder;
    }
    namespace CAM
    {
        class DrillToolBuilder;
    }
    namespace CAM
    {
        class _DrillCounterboreToolBuilderBuilder;
        /** Represents a drill counterbore Tool Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateDrillCounterboreToolBuilder CAM::NCGroupCollection::CreateDrillCounterboreToolBuilder@endlink  <br> */
        class NXOPENCPPEXPORT DrillCounterboreToolBuilder : public CAM::DrillToolBuilder
        {
            private: friend class  _DrillCounterboreToolBuilderBuilder;
            protected: DrillCounterboreToolBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
