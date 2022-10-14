#ifndef NXOpen_FEATURES_DRAWNCUTOUT_HXX_INCLUDED
#define NXOpen_FEATURES_DRAWNCUTOUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DrawnCutout.ja
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
        class DrawnCutout;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _DrawnCutoutBuilder;
        class DrawnCutoutImpl;
        /** Represents a DrawnCutout feature */
        class NXOPENCPPEXPORT  DrawnCutout : public Features::Feature
        {
            private: DrawnCutoutImpl * m_drawncutout_impl;
            private: friend class  _DrawnCutoutBuilder;
            protected: DrawnCutout();
            public: ~DrawnCutout();
        };
    }
}
#undef EXPORTLIBRARY
#endif