#ifndef NXOpen_FEATURES_MASTERCUT_HXX_INCLUDED
#define NXOpen_FEATURES_MASTERCUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MasterCut.ja
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
        class MasterCut;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _MasterCutBuilder;
        /** Represents a section view feature */
        class NXOPENCPPEXPORT MasterCut : public Features::Feature
        {
            private: friend class  _MasterCutBuilder;
            protected: MasterCut();
        };
    }
}
#undef EXPORTLIBRARY
#endif