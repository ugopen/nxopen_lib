#ifndef NXOpen_FEATURES_SEW_HXX_INCLUDED
#define NXOpen_FEATURES_SEW_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Sew.ja
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
#include <NXOpen/Features_CombineBodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class Sew;
    }
    namespace Features
    {
        class CombineBodyFeature;
    }
    namespace Features
    {
        class _SewBuilder;
        /** Represents a sew feature */
        class NXOPENCPPEXPORT Sew : public Features::CombineBodyFeature
        {
            private: friend class  _SewBuilder;
            protected: Sew();
        };
    }
}
#undef EXPORTLIBRARY
#endif
