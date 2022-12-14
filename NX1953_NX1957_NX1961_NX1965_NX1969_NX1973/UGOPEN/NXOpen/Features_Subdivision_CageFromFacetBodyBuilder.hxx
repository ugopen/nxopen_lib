#ifndef NXOpen_FEATURES_SUBDIVISION_CAGEFROMFACETBODYBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_CAGEFROMFACETBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_CageFromFacetBodyBuilder.ja
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
#include <NXOpen/FacetCollector.hxx>
#include <NXOpen/Builder.hxx>
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
        namespace Subdivision
        {
            class CageFromFacetBodyBuilder;
        }
    }
    class Builder;
    class Expression;
    class FacetCollector;
    namespace Features
    {
        namespace Subdivision
        {
            class _CageFromFacetBodyBuilderBuilder;
            class CageFromFacetBodyBuilderImpl;
            /** Represents a @link NXOpen::Features::Subdivision::CageFromFacetBodyBuilder NXOpen::Features::Subdivision::CageFromFacetBodyBuilder@endlink  builder.   <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCageFromFacetBodyBuilder  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreateCageFromFacetBodyBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            AverageSize.Value </term> <description> 
             
            5 (millimeters part), 0.2 (inches part) </description> </item> 

            </list> 

             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  CageFromFacetBodyBuilder : public NXOpen::Builder
            {
                private: CageFromFacetBodyBuilderImpl * m_cagefromfacetbodybuilder_impl;
                private: friend class  _CageFromFacetBodyBuilderBuilder;
                protected: CageFromFacetBodyBuilder();
                public: ~CageFromFacetBodyBuilder();
                /**Returns  the facets to be subdivisioned 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::FacetCollector * FacetRegion
                (
                );
                /**Returns  the average size 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * AverageSize
                (
                );
                /**Returns  the deviation toggle
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowDeviationPlot
                (
                );
                /**Sets  the deviation toggle
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetShowDeviationPlot
                (
                    bool isShowDeviationPlot /** isshowdeviationplot */ 
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
