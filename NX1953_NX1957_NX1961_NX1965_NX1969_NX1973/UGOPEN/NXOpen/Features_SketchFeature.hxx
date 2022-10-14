#ifndef NXOpen_FEATURES_SKETCHFEATURE_HXX_INCLUDED
#define NXOpen_FEATURES_SKETCHFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SketchFeature.ja
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
        class SketchFeature;
    }
    namespace Features
    {
        class Feature;
    }
    class Sketch;
    namespace Features
    {
        class _SketchFeatureBuilder;
        class SketchFeatureImpl;
        /** Represents a sketch feature  <br> This is an abstract class, and cannot be instantiated  <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  SketchFeature : public NXOpen::Features::Feature
        {
            private: SketchFeatureImpl * m_sketchfeature_impl;
            private: friend class  _SketchFeatureBuilder;
            protected: SketchFeature();
            public: ~SketchFeature();
            /**Returns  the sketch that is owned by this feature 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Sketch * Sketch
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