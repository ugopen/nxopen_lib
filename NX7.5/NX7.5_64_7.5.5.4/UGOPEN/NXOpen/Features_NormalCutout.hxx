#ifndef NXOpen_FEATURES_NORMALCUTOUT_HXX_INCLUDED
#define NXOpen_FEATURES_NORMALCUTOUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_NormalCutout.ja
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
        class NormalCutout;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _NormalCutoutBuilder;
        class NormalCutoutImpl;
        /** Represents a Normal Cutout feature */
        class NXOPENCPPEXPORT  NormalCutout : public Features::Feature
        {
            private: NormalCutoutImpl * m_normalcutout_impl;
            private: friend class  _NormalCutoutBuilder;
            protected: NormalCutout();
            public: ~NormalCutout();
        };
    }
}
#undef EXPORTLIBRARY
#endif