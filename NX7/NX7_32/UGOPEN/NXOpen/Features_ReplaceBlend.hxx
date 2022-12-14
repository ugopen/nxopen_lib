#ifndef NXOpen_FEATURES_REPLACEBLEND_HXX_INCLUDED
#define NXOpen_FEATURES_REPLACEBLEND_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ReplaceBlend.ja
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
        class ReplaceBlend;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _ReplaceBlendBuilder;
        /** Represents a replace blend feature */
        class NXOPENCPPEXPORT ReplaceBlend : public Features::BodyFeature
        {
            private: friend class  _ReplaceBlendBuilder;
            protected: ReplaceBlend();
        };
    }
}
#undef EXPORTLIBRARY
#endif
