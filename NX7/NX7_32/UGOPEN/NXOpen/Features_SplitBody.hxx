#ifndef NXOpen_FEATURES_SPLITBODY_HXX_INCLUDED
#define NXOpen_FEATURES_SPLITBODY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SplitBody.ja
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
        class SplitBody;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _SplitBodyBuilder;
        /** Represents a split body feature */
        class NXOPENCPPEXPORT SplitBody : public Features::BodyFeature
        {
            private: friend class  _SplitBodyBuilder;
            protected: SplitBody();
        };
    }
}
#undef EXPORTLIBRARY
#endif