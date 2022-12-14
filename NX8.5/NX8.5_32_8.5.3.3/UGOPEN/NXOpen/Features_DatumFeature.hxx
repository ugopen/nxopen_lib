#ifndef NXOpen_FEATURES_DATUMFEATURE_HXX_INCLUDED
#define NXOpen_FEATURES_DATUMFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DatumFeature.ja
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
        class DatumFeature;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _DatumFeatureBuilder;
        class DatumFeatureImpl;
        /** Represents a Datum feature that is positioned by a set of constraints. This
                is an abstract class, and has two concrete subclasses, @link Features::DatumAxisFeature Features::DatumAxisFeature@endlink 
                and @link Features::DatumPlaneFeature Features::DatumPlaneFeature@endlink 
              <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  DatumFeature : public Features::Feature
        {
            private: DatumFeatureImpl * m_datumfeature_impl;
            private: friend class  _DatumFeatureBuilder;
            protected: DatumFeature();
            public: ~DatumFeature();
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
