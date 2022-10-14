#ifndef NXOpen_FEATURES_TRACELINES_HXX_INCLUDED
#define NXOpen_FEATURES_TRACELINES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TraceLines.ja
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
#include <NXOpen/Features_CurveFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class TraceLines;
    }
    namespace Features
    {
        class CurveFeature;
    }
    namespace Features
    {
        class _TraceLinesBuilder;
        class TraceLinesImpl;
        /** Represents a trace lines feature */
        class NXOPENCPPEXPORT  TraceLines : public Features::CurveFeature
        {
            private: TraceLinesImpl * m_tracelines_impl;
            private: friend class  _TraceLinesBuilder;
            protected: TraceLines();
            public: ~TraceLines();
        };
    }
}
#undef EXPORTLIBRARY
#endif