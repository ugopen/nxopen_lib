#ifndef NXOpen_FEATURES_COATINGS_FEATUREPARMSBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_COATINGS_FEATUREPARMSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Coatings_FeatureParmsBuilder.ja
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
        namespace Coatings
        {
            class FeatureParmsBuilder;
        }
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace Coatings
        {
            class _FeatureParmsBuilderBuilder;
            class FeatureParmsBuilderImpl;
            /**
                This class is used to create or edit the information shared among all Coatings features.
                 <br> Cannot create directly.  <br> 
             <br>  Created in NX1899.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  FeatureParmsBuilder : public NXOpen::Features::FeatureBuilder
            {
                private: FeatureParmsBuilderImpl * m_featureparmsbuilder_impl;
                private: friend class  _FeatureParmsBuilderBuilder;
                protected: FeatureParmsBuilder();
                public: ~FeatureParmsBuilder();
                /**Returns  the tolerance used to determine when distances are considered zero. 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: double DistanceTolerance
                (
                );
                /**Sets  the tolerance used to determine when distances are considered zero. 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetDistanceTolerance
                (
                    double distanceTolerance /** distancetolerance */ 
                );
                /**Returns  the tolerance, in degrees, used to determine when angles are zero. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: double AngularTolerance
                (
                );
                /**Sets  the tolerance, in degrees, used to determine when angles are zero. 
                 <br>  Created in NX1899.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetAngularTolerance
                (
                    double angularTolerance /** angulartolerance */ 
                );
            };
        }
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
