#ifndef NXOpen_FEATURES_EDGERIP_HXX_INCLUDED
#define NXOpen_FEATURES_EDGERIP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_EdgeRip.ja
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
        class EdgeRip;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _EdgeRipBuilder;
        /** Represents an EdgeRip feature */
        class NXOPENCPPEXPORT EdgeRip : public Features::Feature
        {
            private: friend class  _EdgeRipBuilder;
            protected: EdgeRip();
        };
    }
}
#undef EXPORTLIBRARY
#endif