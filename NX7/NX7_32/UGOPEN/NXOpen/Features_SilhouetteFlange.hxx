#ifndef NXOpen_FEATURES_SILHOUETTEFLANGE_HXX_INCLUDED
#define NXOpen_FEATURES_SILHOUETTEFLANGE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SilhouetteFlange.ja
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
        class SilhouetteFlange;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _SilhouetteFlangeBuilder;
        /** Represents a silhouette flange feature */
        class NXOPENCPPEXPORT SilhouetteFlange : public Features::BodyFeature
        {
            private: friend class  _SilhouetteFlangeBuilder;
            protected: SilhouetteFlange();
        };
    }
}
#undef EXPORTLIBRARY
#endif
