#ifndef NXOpen_CAM_WEDMNOCOREGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WEDMNOCOREGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WedmNocoreGeomBuilder.ja
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
        class WedmNocoreGeomBuilder;
    }
    namespace CAM
    {
        class ParamBuilder;
    }
    namespace CAM
    {
        class _WedmNocoreGeomBuilderBuilder;
        /** Represents a WedmNocoreGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateWedmNocoreGeomBuilder CAM::NCGroupCollection::CreateWedmNocoreGeomBuilder@endlink  <br> */
        class NXOPENCPPEXPORT WedmNocoreGeomBuilder : public CAM::ParamBuilder
        {
            private: friend class  _WedmNocoreGeomBuilderBuilder;
            protected: WedmNocoreGeomBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
