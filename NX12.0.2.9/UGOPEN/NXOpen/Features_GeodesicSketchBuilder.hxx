#ifndef NXOpen_FEATURES_GEODESICSKETCHBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_GEODESICSKETCHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_GeodesicSketchBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
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
        class GeodesicSketchBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _GeodesicSketchBuilderBuilder;
        class GeodesicSketchBuilderImpl;
        /** Represents a @link Features::GeodesicSketch Features::GeodesicSketch@endlink  builder for GeodesicSketch feature.  <br> To create a new instance of this class, use @link NXOpen::Features::GeodesicSketchCollection::CreateGeodesicSketchBuilder  NXOpen::Features::GeodesicSketchCollection::CreateGeodesicSketchBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  GeodesicSketchBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: GeodesicSketchBuilderImpl * m_geodesicsketchbuilder_impl;
            private: friend class  _GeodesicSketchBuilderBuilder;
            protected: GeodesicSketchBuilder();
            public: ~GeodesicSketchBuilder();
            /**Returns  the collector of support faces. It can be a single face, or multiple faces 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * SupportFaces
            (
            );
            /**Sets  the collector of support faces. It can be a single face, or multiple faces 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSupportFaces
            (
                NXOpen::ScCollector * supportFaces /** support faces */ 
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