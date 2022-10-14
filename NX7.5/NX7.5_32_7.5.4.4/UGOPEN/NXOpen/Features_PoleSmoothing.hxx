#ifndef NXOpen_FEATURES_POLESMOOTHING_HXX_INCLUDED
#define NXOpen_FEATURES_POLESMOOTHING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PoleSmoothing.ja
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
        class PoleSmoothing;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _PoleSmoothingBuilder;
        class PoleSmoothingImpl;
        /** Represents a pole smoothing feature */
        class NXOPENCPPEXPORT  PoleSmoothing : public Features::BodyFeature
        {
            private: PoleSmoothingImpl * m_polesmoothing_impl;
            private: friend class  _PoleSmoothingBuilder;
            protected: PoleSmoothing();
            public: ~PoleSmoothing();
        };
    }
}
#undef EXPORTLIBRARY
#endif