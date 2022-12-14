#ifndef NXOpen_FEATURES_THROUGHCURVES_HXX_INCLUDED
#define NXOpen_FEATURES_THROUGHCURVES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ThroughCurves.ja
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
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class ThroughCurves;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _ThroughCurvesBuilder;
        class ThroughCurvesImpl;
        /** Represents a Through Curves feature.  <br> To create or edit an instance of this class, use @link NXOpen::Features::ThroughCurvesBuilder  NXOpen::Features::ThroughCurvesBuilder @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  ThroughCurves : public NXOpen::Features::BodyFeature
        {
            private: ThroughCurvesImpl * m_throughcurves_impl;
            private: friend class  _ThroughCurvesBuilder;
            protected: ThroughCurves();
            public: ~ThroughCurves();
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
