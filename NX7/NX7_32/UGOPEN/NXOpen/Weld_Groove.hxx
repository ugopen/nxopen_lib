#ifndef NXOpen_WELD_GROOVE_HXX_INCLUDED
#define NXOpen_WELD_GROOVE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_Groove.ja
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
    namespace Weld
    {
        class Groove;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Weld
    {
        class _GrooveBuilder;
        /** Represents a WeldGroove feature. */
        class NXOPENCPPEXPORT Groove : public Features::Feature
        {
            private: friend class  _GrooveBuilder;
            protected: Groove();
        };
    }
}
#undef EXPORTLIBRARY
#endif
