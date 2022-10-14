#ifndef NXOpen_FEATURES_FEATURESAMPLEOFFSETCURVEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_FEATURESAMPLEOFFSETCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_FeatureSampleOffsetCurveBuilder.ja
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
#include <NXOpen/Features_ServiceOrientedFeatureCurveBuilder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

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
        class FeatureSampleOffsetCurveBuilder;
    }
    class Expression;
    namespace Features
    {
        class ServiceOrientedFeatureCurveBuilder;
    }
    class Section;
    namespace Features
    {
        class _FeatureSampleOffsetCurveBuilderBuilder;
        class FeatureSampleOffsetCurveBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link Features::FeatureSampleOffsetCurve Features::FeatureSampleOffsetCurve@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureSampleCollection::CreateFeatureSampleOffsetCurveBuilder  NXOpen::Features::FeatureSampleCollection::CreateFeatureSampleOffsetCurveBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        OffsetDistance.Value </term> <description> 
         
        5 (millimeters part), 5 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENDEBUGSESSIONCPPEXPORT  FeatureSampleOffsetCurveBuilder : public NXOpen::Features::ServiceOrientedFeatureCurveBuilder
        {
            private: FeatureSampleOffsetCurveBuilderImpl * m_featuresampleoffsetcurvebuilder_impl;
            private: friend class  _FeatureSampleOffsetCurveBuilderBuilder;
            protected: FeatureSampleOffsetCurveBuilder();
            public: ~FeatureSampleOffsetCurveBuilder();
            /**Returns  the section 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * Section
            (
            );
            /**Returns  the offset distance 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetDistance
            (
            );
        };

        /// \endcond 
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