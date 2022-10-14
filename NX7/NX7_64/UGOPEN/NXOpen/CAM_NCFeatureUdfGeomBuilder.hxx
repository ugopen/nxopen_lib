#ifndef NXOpen_CAM_NCFEATUREUDFGEOMBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NCFEATUREUDFGEOMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NCFeatureUdfGeomBuilder.ja
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
#include <NXOpen/CAM_NCFeatureGeomBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class NCFeatureUdfGeomBuilder;
    }
    namespace CAM
    {
        class NCFeatureGeomBuilder;
    }
    namespace CAM
    {
        class _NCFeatureUdfGeomBuilderBuilder;
        /** Represents a NCFeatureUdfGeom Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateNcfeatureUdfGeomBuilder CAM::NCGroupCollection::CreateNcfeatureUdfGeomBuilder@endlink  <br> */
        class NXOPENCPPEXPORT NCFeatureUdfGeomBuilder : public CAM::NCFeatureGeomBuilder
        {
            private: friend class  _NCFeatureUdfGeomBuilderBuilder;
            protected: NCFeatureUdfGeomBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif