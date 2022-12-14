#ifndef NXOpen_FEATURES_ADMRESIZEFACE_HXX_INCLUDED
#define NXOpen_FEATURES_ADMRESIZEFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_AdmResizeFace.ja
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
        class AdmResizeFace;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _AdmResizeFaceBuilder;
        /** Represents an ADM resize face feature */
        class NXOPENCPPEXPORT AdmResizeFace : public Features::BodyFeature
        {
            private: friend class  _AdmResizeFaceBuilder;
            protected: AdmResizeFace();
        };
    }
}
#undef EXPORTLIBRARY
#endif
