#ifndef NXOpen_FEATURES_JOG_HXX_INCLUDED
#define NXOpen_FEATURES_JOG_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Jog.ja
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
        class Jog;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _JogBuilder;
        /** Represents a Jog feature */
        class NXOPENCPPEXPORT Jog : public Features::Feature
        {
            private: friend class  _JogBuilder;
            protected: Jog();
        };
    }
}
#undef EXPORTLIBRARY
#endif
