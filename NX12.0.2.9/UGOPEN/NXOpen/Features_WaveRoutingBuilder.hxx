#ifndef NXOpen_FEATURES_WAVEROUTINGBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_WAVEROUTINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_WaveRoutingBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
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
        class WaveRoutingBuilder;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectObjectList;
    namespace Features
    {
        class _WaveRoutingBuilderBuilder;
        class WaveRoutingBuilderImpl;
        /**
            Represents a @link NXOpen::Features::WaveRoutingBuilder NXOpen::Features::WaveRoutingBuilder@endlink  
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateWaveRoutingBuilder  NXOpen::Features::FeatureCollection::CreateWaveRoutingBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Associative </td> <td> 
         
        True </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  WaveRoutingBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: WaveRoutingBuilderImpl * m_waveroutingbuilder_impl;
            private: friend class  _WaveRoutingBuilderBuilder;
            protected: WaveRoutingBuilder();
            public: ~WaveRoutingBuilder();
            /**Returns  the routing 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectObjectList * RoutingObjects
            (
            );
            /**Returns  the associative 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associative 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the makepositionindependent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool MakePositionIndependent
            (
            );
            /**Sets  the makepositionindependent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMakePositionIndependent
            (
                bool makePositionIndependent /** makepositionindependent */ 
            );
            /** Commits the feature and set create on the fly flag  @return  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::Feature * CommitCreateOnTheFly
            (
            );
            /** Prints wave browser type information about link 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : wave ("WAVE FUNCTIONALITY") */
            public: void GetWaveLinkInformation
            (
                NXString* info /** queried wave information */,
                bool* xformExists /** true if there is a transform */,
                NXOpen::Point3d* xformOrigin /** transformation origin */,
                NXOpen::Matrix3x3* xformOrientation /** transformation matrix */,
                double* xformScale /** transformation scale */
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
