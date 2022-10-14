#ifndef NXOpen_ANNOTATIONS_GEODESICDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_GEODESICDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_GeodesicDimensionBuilder.ja
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
#include <NXOpen/Annotations_DimensionMeasurementBuilder.hxx>
#include <NXOpen/Annotations_DrivingValueBuilder.hxx>
#include <NXOpen/Annotations_GeodesicDimensionBuilder.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Annotations_StyleBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class GeodesicDimensionBuilder;
    }
    namespace Annotations
    {
        class DimensionMeasurementBuilder;
    }
    namespace Annotations
    {
        class DrivingValueBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    class Builder;
    class SelectEdge;
    class SelectPoint;
    namespace Annotations
    {
        class _GeodesicDimensionBuilderBuilder;
        class GeodesicDimensionBuilderImpl;
        /** Represents a @link Annotations::Dimension Annotations::Dimension@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::DimensionCollection::CreateGeodesicDimensionBuilder  NXOpen::Annotations::DimensionCollection::CreateGeodesicDimensionBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  GeodesicDimensionBuilder : public NXOpen::Builder
        {
            private: GeodesicDimensionBuilderImpl * m_geodesicdimensionbuilder_impl;
            private: friend class  _GeodesicDimensionBuilderBuilder;
            protected: GeodesicDimensionBuilder();
            public: ~GeodesicDimensionBuilder();
            /**Returns  the curves or edges to dimension from 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectEdge * OriginCurve
            (
            );
            /**Returns  the measurement point 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPoint * MeasurementPoint
            (
            );
            /**Returns  the origin 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::OriginBuilder * Origin
            (
            );
            /**Returns  the style 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * Style
            (
            );
            /**Returns  the measurement 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DimensionMeasurementBuilder * Measurement
            (
            );
            /**Returns  the driving value builder, which manages driving dimension values 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DrivingValueBuilder * Driving
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