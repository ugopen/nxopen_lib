#ifndef NXOpen_CAM_WEDMCUTTINGBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WEDMCUTTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WedmCuttingBuilder.ja
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
        class WedmCuttingBuilder;
    }
    namespace CAM
    {
        class ParamBuilder;
    }
    namespace CAM
    {
        class _WedmCuttingBuilderBuilder;
        /** Represents a WedmCutting Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateWedmCuttingBuilder CAM::NCGroupCollection::CreateWedmCuttingBuilder@endlink  <br> */
        class NXOPENCPPEXPORT WedmCuttingBuilder : public CAM::ParamBuilder
        {
            private: friend class  _WedmCuttingBuilderBuilder;
            protected: WedmCuttingBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
