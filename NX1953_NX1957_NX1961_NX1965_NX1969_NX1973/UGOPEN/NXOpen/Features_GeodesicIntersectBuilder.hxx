#ifndef NXOpen_FEATURES_GEODESICINTERSECTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_GEODESICINTERSECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_GeodesicIntersectBuilder.ja
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
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class GeodesicIntersectBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    class Section;
    class SelectDisplayableObject;
    namespace Features
    {
        class _GeodesicIntersectBuilderBuilder;
        class GeodesicIntersectBuilderImpl;
        /** Represents a @link NXOpen::Features::GeodesicIntersect NXOpen::Features::GeodesicIntersect@endlink  builder for Intersect command.  <br> To create a new instance of this class, use @link NXOpen::Features::GeodesicSketchCollection::CreateGeodesicIntersectBuilder  NXOpen::Features::GeodesicSketchCollection::CreateGeodesicIntersectBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        IntersectType </term> <description> 
         
        Datum </description> </item> 

        </list> 

         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  GeodesicIntersectBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Represents the type of objects that intersect with the support faces. */
            public: enum Type
            {
                TypeDatum/** Datum. */,
                TypeFace/** Face. */,
                TypeCurve/** Curve. */
            };

            private: GeodesicIntersectBuilderImpl * m_geodesicintersectbuilder_impl;
            private: friend class  _GeodesicIntersectBuilderBuilder;
            protected: GeodesicIntersectBuilder();
            public: ~GeodesicIntersectBuilder();
            /**Returns  the intersect type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GeodesicIntersectBuilder::Type IntersectType
            (
            );
            /**Sets  the intersect type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetIntersectType
            (
                NXOpen::Features::GeodesicIntersectBuilder::Type intersectType /** intersect type */ 
            );
            /**Returns  the datum plane or datum axis to intersect sketch face 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * IntersectDatum
            (
            );
            /**Returns  the faces to intersect sketch face 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * IntersectFaces
            (
            );
            /**Returns  the curves to intersect sketch face 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * IntersectCurves
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