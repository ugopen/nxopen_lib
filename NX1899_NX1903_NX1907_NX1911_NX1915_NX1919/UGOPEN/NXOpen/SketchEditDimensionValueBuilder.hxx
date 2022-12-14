#ifndef NXOpen_SKETCHEDITDIMENSIONVALUEBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHEDITDIMENSIONVALUEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchEditDimensionValueBuilder.ja
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
#include <NXOpen/SketchOperationBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
    class SketchEditDimensionValueBuilder;
    class Expression;
    class SelectNXObjectList;
    class SketchOperationBuilder;
    class _SketchEditDimensionValueBuilderBuilder;
    class SketchEditDimensionValueBuilderImpl;
    /** Represents a @link NXOpen::SketchEditDimensionValueBuilder NXOpen::SketchEditDimensionValueBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateEditDimensionValueBuilder  NXOpen::SketchCollection::CreateEditDimensionValueBuilder @endlink  <br> 
     <br>  Created in NX1899.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchEditDimensionValueBuilder : public NXOpen::SketchOperationBuilder
    {
        private: SketchEditDimensionValueBuilderImpl * m_sketcheditdimensionvaluebuilder_impl;
        private: friend class  _SketchEditDimensionValueBuilderBuilder;
        protected: SketchEditDimensionValueBuilder();
        public: ~SketchEditDimensionValueBuilder();
        /**Returns  the expression for driving dimension 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Expression * Expression
        (
        );
        /**Returns  the dimension value 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: double DimValue
        (
        );
        /**Sets  the dimension value 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
        public: void SetDimValue
        (
            double dimValue /** dimvalue */ 
        );
        /**Returns  the extra geometries to be moved along with the dimension geometry when dimension is directional 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObjectList * ExtraGeometries
        (
        );
        /** Load extra geometry. 
                    This function needs to be called if the extra geometry collection or dimension direction changes after the builder is committed 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
        public: void LoadExtraGeometry
        (
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
