#ifndef NXOpen_FEATURES_ALGORITHMICFEATUREBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_ALGORITHMICFEATUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_AlgorithmicFeatureBuilder.ja
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
        class AlgorithmicFeatureBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class NXObject;
    namespace Features
    {
        class _AlgorithmicFeatureBuilderBuilder;
        class AlgorithmicFeatureBuilderImpl;
        /** Represents AlgorithmicFeatureBuilder class <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateAlgorithmicFeatureBuilder  NXOpen::Features::FeatureCollection::CreateAlgorithmicFeatureBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  AlgorithmicFeatureBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: AlgorithmicFeatureBuilderImpl * m_algorithmicfeaturebuilder_impl;
            private: friend class  _AlgorithmicFeatureBuilderBuilder;
            protected: AlgorithmicFeatureBuilder();
            public: ~AlgorithmicFeatureBuilder();
            /**Returns  the rule instance 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * RuleInstance
            (
            );
            /**Sets  the rule instance 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_algorithmic (" NX Algorithmic Modeling") */
            public: void SetRuleInstance
            (
                NXOpen::NXObject * data /** data */ 
            );
            /**Returns  the associative flag
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsAssociative
            (
            );
            /**Sets  the associative flag
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_algorithmic (" NX Algorithmic Modeling") */
            public: void SetAssociative
            (
                bool isAssociative /** isassociative */ 
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
