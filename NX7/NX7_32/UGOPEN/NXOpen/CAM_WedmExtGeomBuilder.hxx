#ifndef NXOpen_CAM_WEDMEXTGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WEDMEXTGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WedmExtGeomBuilder.ja
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
#include <NXOpen/CAM_WedmBasedGeomBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class WedmExtGeomBuilder;
    }
    namespace CAM
    {
        class WedmBasedGeomBuilder;
    }
    namespace CAM
    {
        class _WedmExtGeomBuilderBuilder;
        /** Represents a WedmExtGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateWedmExtGeomBuilder CAM::NCGroupCollection::CreateWedmExtGeomBuilder@endlink  <br> */
        class NXOPENCPPEXPORT WedmExtGeomBuilder : public CAM::WedmBasedGeomBuilder
        {
            private: friend class  _WedmExtGeomBuilderBuilder;
            protected: WedmExtGeomBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif