#ifndef NXOpen_FEATURES_SERVICEORIENTEDFEATURECURVEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SERVICEORIENTEDFEATURECURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ServiceOrientedFeatureCurveBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
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
        class ServiceOrientedFeatureCurveBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class _ServiceOrientedFeatureCurveBuilderBuilder;
        class ServiceOrientedFeatureCurveBuilderImpl;
        /**
            Represents a @link NXOpen::Features::ServiceOrientedFeatureCurve NXOpen::Features::ServiceOrientedFeatureCurve@endlink  builder
             <br> Not support KF.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  ServiceOrientedFeatureCurveBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: ServiceOrientedFeatureCurveBuilderImpl * m_serviceorientedfeaturecurvebuilder_impl;
            private: friend class  _ServiceOrientedFeatureCurveBuilderBuilder;
            protected: ServiceOrientedFeatureCurveBuilder();
            public: ~ServiceOrientedFeatureCurveBuilder();
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
