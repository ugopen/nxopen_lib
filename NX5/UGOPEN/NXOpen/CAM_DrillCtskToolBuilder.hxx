#ifndef NXOpen_CAM_DRILLCTSKTOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DRILLCTSKTOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DrillCtskToolBuilder.ja
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
        class DrillCtskToolBuilder;
    }
    namespace CAM
    {
        class DrillToolBuilder;
    }
    namespace CAM
    {
        class _DrillCtskToolBuilderBuilder;
        /** Represents a Drill Ctsk Tool Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateDrillCtskToolBuilder CAM::NCGroupCollection::CreateDrillCtskToolBuilder@endlink  <br> */
        class NXOPENCPPEXPORT DrillCtskToolBuilder : public CAM::DrillToolBuilder
        {
            private: friend class  _DrillCtskToolBuilderBuilder;
            protected: DrillCtskToolBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
