#ifndef NXOpen_SKETCHDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchDimensionBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SketchDimensionBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SketchDimensionBuilder;
    class Builder;
    class SelectNXObject;
    class _SketchDimensionBuilderBuilder;
    class SketchDimensionBuilderImpl;
    /**
    Edit the geometry references of an existing sketch dimension.  For active dimensions, the driving 
    expression can be kept or reset to the measured value of the new geometry.
     <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateDimensionBuilder  NXOpen::SketchCollection::CreateDimensionBuilder @endlink  <br> 
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchDimensionBuilder : public NXOpen::Builder
    {
        /** This enum determines the expression behavior when a dimension is attached to new geometry */
        public: enum ExpOption
        {
            ExpOptionKeepExpression/** keep expression, adjust geometry */,
            ExpOptionMeasureGeometry/** remove expression, measure geometry */
        };

        private: SketchDimensionBuilderImpl * m_sketchdimensionbuilder_impl;
        private: friend class  _SketchDimensionBuilderBuilder;
        protected: SketchDimensionBuilder();
        public: ~SketchDimensionBuilder();
        /**Returns  the first geometry 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObject * FirstGeometry
        (
        );
        /**Returns  the second geometry.  This will be NULL for Radius or Diameter dimensions. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObject * SecondGeometry
        (
        );
        /**Returns  the expression option 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SketchDimensionBuilder::ExpOption ExpressionOption
        (
        );
        /**Sets  the expression option 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: void SetExpressionOption
        (
            NXOpen::SketchDimensionBuilder::ExpOption option /** option */ 
        );
        /**Returns  the snap radius.  This is used to determine if the geometry is selected at a
                control point. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: double SnapRadius
        (
        );
        /**Sets  the snap radius.  This is used to determine if the geometry is selected at a
                control point. 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: void SetSnapRadius
        (
            double radius /** radius */ 
        );
    };
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