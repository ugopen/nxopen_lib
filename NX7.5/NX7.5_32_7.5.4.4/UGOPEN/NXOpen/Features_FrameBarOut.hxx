#ifndef NXOpen_FEATURES_FRAMEBAROUT_HXX_INCLUDED
#define NXOpen_FEATURES_FRAMEBAROUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_FrameBarOut.ja
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
        class FrameBarOut;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _FrameBarOutBuilder;
        class FrameBarOutImpl;
        /** Represents a FrameBarOut */
        class NXOPENCPPEXPORT  FrameBarOut : public Features::BodyFeature
        {
            private: FrameBarOutImpl * m_framebarout_impl;
            private: friend class  _FrameBarOutBuilder;
            protected: FrameBarOut();
            public: ~FrameBarOut();
        };
    }
}
#undef EXPORTLIBRARY
#endif
