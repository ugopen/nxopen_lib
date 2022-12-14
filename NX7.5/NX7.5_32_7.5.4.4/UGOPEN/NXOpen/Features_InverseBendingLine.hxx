#ifndef NXOpen_FEATURES_INVERSEBENDINGLINE_HXX_INCLUDED
#define NXOpen_FEATURES_INVERSEBENDINGLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_InverseBendingLine.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class InverseBendingLine;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _InverseBendingLineBuilder;
        class InverseBendingLineImpl;
        /** Represents a inverse bending line feature */
        class NXOPENCPPEXPORT  InverseBendingLine : public Features::BodyFeature
        {
            private: InverseBendingLineImpl * m_inversebendingline_impl;
            private: friend class  _InverseBendingLineBuilder;
            protected: InverseBendingLine();
            public: ~InverseBendingLine();
        };
    }
}
#undef EXPORTLIBRARY
#endif
