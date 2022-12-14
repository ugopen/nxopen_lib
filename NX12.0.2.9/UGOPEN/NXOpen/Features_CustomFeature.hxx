#ifndef NXOpen_FEATURES_CUSTOMFEATURE_HXX_INCLUDED
#define NXOpen_FEATURES_CUSTOMFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CustomFeature.ja
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
#include <NXOpen/Features_ConstructionFeatureData.hxx>
#include <NXOpen/Features_CustomFeatureData.hxx>
#include <NXOpen/Features_OutputFeatureData.hxx>
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
        class CustomFeature;
    }
    class Body;
    namespace Features
    {
        class ConstructionFeatureData;
    }
    namespace Features
    {
        class CustomFeatureData;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class OutputFeatureData;
    }
    namespace Features
    {
        class _CustomFeatureBuilder;
        class CustomFeatureImpl;
        /** Represents a custom feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::CustomFeatureBuilder  NXOpen::Features::CustomFeatureBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  CustomFeature : public NXOpen::Features::Feature
        {
            private: CustomFeatureImpl * m_customfeature_impl;
            private: friend class  _CustomFeatureBuilder;
            protected: CustomFeature();
            public: ~CustomFeature();
            /**Returns  the custom feature data 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::CustomFeatureData * FeatureData
            (
            );
            /** Returns the bodies created by the feature  @return  
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::Body *> GetBodies
            (
            );
            /** Get construction features of custom feature @return  Output array of @link Features::ConstructionFeatureData Features::ConstructionFeatureData@endlink 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::Features::ConstructionFeatureData *> GetConstructionFeatures
            (
            );
            /** Get output features of custom feature @return  Output array of @link Features::OutputFeatureData Features::OutputFeatureData@endlink 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::Features::OutputFeatureData *> GetOutputFeatures
            (
            );
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
