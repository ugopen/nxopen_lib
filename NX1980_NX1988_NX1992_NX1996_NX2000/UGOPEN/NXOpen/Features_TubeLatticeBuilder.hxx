#ifndef NXOpen_FEATURES_TUBELATTICEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TUBELATTICEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TubeLatticeBuilder.ja
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
#include <NXOpen/Expression.hxx>
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
        class TubeLatticeBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _TubeLatticeBuilderBuilder;
        class TubeLatticeBuilderImpl;
        /**Represents a Features.TubeLattice builder <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateTubeLatticeBuilder  NXOpen::Facet::FacetModelingCollection::CreateTubeLatticeBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        FalloffDistance.Value </term> <description> 
         
        5 (millimeters part), 0.2 (inches part) </description> </item> 

        <item><term> 
         
        NodeSize.Value </term> <description> 
         
        2 (millimeters part), 0.08 (inches part) </description> </item> 

        <item><term> 
         
        Resolution </term> <description> 
         
        Standard </description> </item> 

        <item><term> 
         
        RodSize.Value </term> <description> 
         
        1 (millimeters part), 0.04 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  TubeLatticeBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** End capping type */
            public: enum EndCapsType
            {
                EndCapsTypeNone/** none */ ,
                EndCapsTypeFlat/** flat */ ,
                EndCapsTypeRound/** round */ 
            };

            /** Resolution type */
            public: enum ResolutionType
            {
                ResolutionTypeCoarse/** coarse */ ,
                ResolutionTypeStandard/** standard */ ,
                ResolutionTypeFine/** fine */ ,
                ResolutionTypeExtraFine/** extra fine */ ,
                ResolutionTypeSuperFine/** super fine */ ,
                ResolutionTypeUltraFine/** ultra fine */ 
            };

            private: TubeLatticeBuilderImpl * m_tubelatticebuilder_impl;
            private: friend class  _TubeLatticeBuilderBuilder;
            protected: TubeLatticeBuilder();
            public: ~TubeLatticeBuilder();
            /**Returns  the graph structure 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * GraphStructure
            (
            );
            /**Returns  the node size 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * NodeSize
            (
            );
            /**Returns  the rod size 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RodSize
            (
            );
            /**Returns  the falloff distance 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * FalloffDistance
            (
            );
            /**Returns  the end capping type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::TubeLatticeBuilder::EndCapsType EndCaps
            (
            );
            /**Sets  the end capping type 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: void SetEndCaps
            (
                NXOpen::Features::TubeLatticeBuilder::EndCapsType endCaps /** endcaps */ 
            );
            /**Returns  the resolution 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::TubeLatticeBuilder::ResolutionType Resolution
            (
            );
            /**Sets  the resolution 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_polygon_modeling (" NX Polygon Modeling") */
            public: void SetResolution
            (
                NXOpen::Features::TubeLatticeBuilder::ResolutionType resolution /** resolution */ 
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