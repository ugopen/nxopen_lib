#ifndef NXOpen_FEATURES_UNTRIMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_UNTRIMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_UntrimBuilder.ja
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
        class UntrimBuilder;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _UntrimBuilderBuilder;
        class UntrimBuilderImpl;
        /**
            Represents a @link NXOpen::Features::Untrim NXOpen::Features::Untrim@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateUntrimBuilder  NXOpen::Features::FeatureCollection::CreateUntrimBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  UntrimBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: UntrimBuilderImpl * m_untrimbuilder_impl;
            private: friend class  _UntrimBuilderBuilder;
            protected: UntrimBuilder();
            public: ~UntrimBuilder();
            /**Returns  the faces to untrim 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * FacesToUntrim
            (
            );
            /**Returns  the hide original option.
                    Controls whether parent body should be hidden or not. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool HideOriginal
            (
            );
            /**Sets  the hide original option.
                    Controls whether parent body should be hidden or not. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetHideOriginal
            (
                bool hideOriginal /** Set true to hide parent object otherwise false to display parent as it is */
            );
            /**Returns  the option indicates to create associative untrim feature or unparameterized feature
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the option indicates to create associative untrim feature or unparameterized feature
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /** Removes parameters of feature.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RemoveParameter
            (
                NXOpen::Features::Feature * untrimFeature /** untrimfeature */ 
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
