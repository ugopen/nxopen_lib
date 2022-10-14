#ifndef NXOpen_FEATURES_UNSEW_HXX_INCLUDED
#define NXOpen_FEATURES_UNSEW_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Unsew.ja
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
        class Unsew;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _UnsewBuilder;
        /** Represents a Unsew feature */
        class NXOPENCPPEXPORT Unsew : public Features::BodyFeature
        {
            private: friend class  _UnsewBuilder;
            protected: Unsew();
        };
    }
}
#undef EXPORTLIBRARY
#endif