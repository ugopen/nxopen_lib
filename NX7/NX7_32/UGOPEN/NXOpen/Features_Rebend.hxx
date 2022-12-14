#ifndef NXOpen_FEATURES_REBEND_HXX_INCLUDED
#define NXOpen_FEATURES_REBEND_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Rebend.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class Rebend;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _RebendBuilder;
        /** Represents a Rebend feature */
        class NXOPENCPPEXPORT Rebend : public Features::Feature
        {
            private: friend class  _RebendBuilder;
            protected: Rebend();
        };
    }
}
#undef EXPORTLIBRARY
#endif
