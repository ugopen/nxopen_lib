#ifndef NXOpen_CAM_MILLVOLUMEGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MILLVOLUMEGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MillVolumeGeomBuilder.ja
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
#include <NXOpen/CAM_MillGeomBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MillVolumeGeomBuilder;
    }
    namespace CAM
    {
        class MillGeomBuilder;
    }
    namespace CAM
    {
        class _MillVolumeGeomBuilderBuilder;
        /** Represents a MillVolumeGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateMillVolumeGeomBuilder CAM::NCGroupCollection::CreateMillVolumeGeomBuilder@endlink  <br> */
        class NXOPENCPPEXPORT MillVolumeGeomBuilder : public CAM::MillGeomBuilder
        {
            private: friend class  _MillVolumeGeomBuilderBuilder;
            protected: MillVolumeGeomBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif