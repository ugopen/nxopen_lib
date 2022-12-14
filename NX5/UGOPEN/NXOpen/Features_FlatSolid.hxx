#ifndef NXOpen_FEATURES_FLATSOLID_HXX_INCLUDED
#define NXOpen_FEATURES_FLATSOLID_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_FlatSolid.ja
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
        class FlatSolid;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _FlatSolidBuilder;
        /** Represents a Flat Solid feature */
        class NXOPENCPPEXPORT FlatSolid : public Features::Feature
        {
            private: friend class  _FlatSolidBuilder;
            protected: FlatSolid();
        };
    }
}
#undef EXPORTLIBRARY
#endif
