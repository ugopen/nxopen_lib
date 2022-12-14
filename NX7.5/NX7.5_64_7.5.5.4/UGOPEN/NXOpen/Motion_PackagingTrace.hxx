#ifndef NXOpen_MOTION_PACKAGINGTRACE_HXX_INCLUDED
#define NXOpen_MOTION_PACKAGINGTRACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_PackagingTrace.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Motion_Packaging.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class PackagingTrace;
    }
    namespace Motion
    {
        class Packaging;
    }
    namespace Motion
    {
        class _PackagingTraceBuilder;
        class PackagingTraceImpl;
        /** This class represents a Packaging Trace object.  A Trace object
            is used to define a request to trace moving objects of a
            mechanism during motion animation. */
        class NXOPENCPPEXPORT  PackagingTrace : public Motion::Packaging
        {
            private: PackagingTraceImpl * m_packagingtrace_impl;
            private: friend class  _PackagingTraceBuilder;
            protected: PackagingTrace();
            public: ~PackagingTrace();
        };
    }
}
#undef EXPORTLIBRARY
#endif
