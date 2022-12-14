#ifndef NXOpen_FEATURES_MIRRORFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_MIRRORFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MirrorFeatureBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class MirrorFeatureBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class SelectFeatureList;
    }
    class Plane;
    class SelectISurface;
    namespace Features
    {
        class _MirrorFeatureBuilderBuilder;
        class MirrorFeatureBuilderImpl;
        /**
            Represents a @link NXOpen::Features::MirrorFeature NXOpen::Features::MirrorFeature@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateMirrorFeatureBuilder  NXOpen::Features::FeatureCollection::CreateMirrorFeatureBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  MirrorFeatureBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** the Plane options. */
            public: enum PlaneOptions
            {
                PlaneOptionsExisting/** existing plane*/,
                PlaneOptionsNew/** new plane */
            };

            private: MirrorFeatureBuilderImpl * m_mirrorfeaturebuilder_impl;
            private: friend class  _MirrorFeatureBuilderBuilder;
            protected: MirrorFeatureBuilder();
            public: ~MirrorFeatureBuilder();
            /**Returns  the Mirror Plane
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectISurface * Plane
            (
            );
            /**Returns  the Features
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeatureList * FeatureSet
            (
            );
            /**Returns  the plane option
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::MirrorFeatureBuilder::PlaneOptions PlaneOption
            (
            );
            /**Sets  the plane option
                
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPlaneOption
            (
                NXOpen::Features::MirrorFeatureBuilder::PlaneOptions planeOptions /** plane options */ 
            );
            /**Returns  the plane constructor 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * PlaneConstructor
            (
            );
            /**Sets  the plane constructor 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPlaneConstructor
            (
                NXOpen::Plane * planeConstructor /** planeconstructor */ 
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
