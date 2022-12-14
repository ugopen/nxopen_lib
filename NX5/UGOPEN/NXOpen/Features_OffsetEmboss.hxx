#ifndef NXOpen_FEATURES_OFFSETEMBOSS_HXX_INCLUDED
#define NXOpen_FEATURES_OFFSETEMBOSS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_OffsetEmboss.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class OffsetEmboss;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _OffsetEmbossBuilder;
        /** Represents an offset emboss feature */
        class NXOPENCPPEXPORT OffsetEmboss : public Features::BodyFeature
        {
            private: friend class  _OffsetEmbossBuilder;
            protected: OffsetEmboss();
        };
    }
}
#undef EXPORTLIBRARY
#endif
