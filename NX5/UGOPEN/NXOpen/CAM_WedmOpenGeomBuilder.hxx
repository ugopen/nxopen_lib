#ifndef NXOpen_CAM_WEDMOPENGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WEDMOPENGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WedmOpenGeomBuilder.ja
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
#include <NXOpen/CAM_ParamBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class WedmOpenGeomBuilder;
    }
    namespace CAM
    {
        class ParamBuilder;
    }
    namespace CAM
    {
        class _WedmOpenGeomBuilderBuilder;
        /** Represents a WedmOpenGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateWedmOpenGeomBuilder CAM::NCGroupCollection::CreateWedmOpenGeomBuilder@endlink  <br> */
        class NXOPENCPPEXPORT WedmOpenGeomBuilder : public CAM::ParamBuilder
        {
            private: friend class  _WedmOpenGeomBuilderBuilder;
            protected: WedmOpenGeomBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif