#ifndef NXOpen_CAM_MILLGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MILLGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MillGeomBuilder.ja
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
#include <NXOpen/CAM_FeatureGeomBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MillGeomBuilder;
    }
    namespace CAM
    {
        class FeatureGeomBuilder;
    }
    namespace CAM
    {
        class _MillGeomBuilderBuilder;
        /** Represents a MillGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateMillGeomBuilder CAM::NCGroupCollection::CreateMillGeomBuilder@endlink  <br> */
        class NXOPENCPPEXPORT MillGeomBuilder : public CAM::FeatureGeomBuilder
        {
            private: friend class  _MillGeomBuilderBuilder;
            protected: MillGeomBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif