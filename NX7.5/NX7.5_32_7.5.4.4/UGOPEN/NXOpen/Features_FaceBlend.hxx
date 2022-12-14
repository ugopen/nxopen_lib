#ifndef NXOpen_FEATURES_FACEBLEND_HXX_INCLUDED
#define NXOpen_FEATURES_FACEBLEND_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_FaceBlend.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class FaceBlend;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _FaceBlendBuilder;
        class FaceBlendImpl;
        /** Represents a Face Blend feature. */
        class NXOPENCPPEXPORT  FaceBlend : public Features::Feature
        {
            private: FaceBlendImpl * m_faceblend_impl;
            private: friend class  _FaceBlendBuilder;
            protected: FaceBlend();
            public: ~FaceBlend();
        };
    }
}
#undef EXPORTLIBRARY
#endif
