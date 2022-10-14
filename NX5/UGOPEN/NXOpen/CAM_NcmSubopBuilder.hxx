#ifndef NXOpen_CAM_NCMSUBOPBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NCMSUBOPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmSubopBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class NcmSubopBuilder;
    }
    class Builder;
    namespace CAM
    {
        class _NcmSubopBuilderBuilder;
        /**
            Represents a @link CAM::NcmSubopBuilder CAM::NcmSubopBuilder@endlink 
             <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT NcmSubopBuilder : public Builder
        {
            private: friend class  _NcmSubopBuilderBuilder;
            protected: NcmSubopBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif