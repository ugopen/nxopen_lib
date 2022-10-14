#ifndef NXOpen_FEATURES_SCALE_HXX_INCLUDED
#define NXOpen_FEATURES_SCALE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Scale.ja
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
        class Scale;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _ScaleBuilder;
        class ScaleImpl;
        /** Represents a scale feature */
        class NXOPENCPPEXPORT  Scale : public Features::BodyFeature
        {
            private: ScaleImpl * m_scale_impl;
            private: friend class  _ScaleBuilder;
            protected: Scale();
            public: ~Scale();
        };
    }
}
#undef EXPORTLIBRARY
#endif