#ifndef NXOpen_SKETCHLINEARDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHLINEARDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchLinearDimensionBuilder.ja
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
#include <NXOpen/Annotations_DrivingValueBuilder.hxx>
#include <NXOpen/Annotations_BaseLinearDimensionBuilder.hxx>
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
    class SketchLinearDimensionBuilder;
    namespace Annotations
    {
        class BaseLinearDimensionBuilder;
    }
    namespace Annotations
    {
        class DrivingValueBuilder;
    }
    class _SketchLinearDimensionBuilderBuilder;
    class SketchLinearDimensionBuilderImpl;
    /** Represents a @link NXOpen::SketchLinearDimensionBuilder NXOpen::SketchLinearDimensionBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateLinearDimensionBuilder  NXOpen::SketchCollection::CreateLinearDimensionBuilder @endlink  <br> 
     <br>  Created in NX9.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchLinearDimensionBuilder : public NXOpen::Annotations::BaseLinearDimensionBuilder
    {
        private: SketchLinearDimensionBuilderImpl * m_sketchlineardimensionbuilder_impl;
        private: friend class  _SketchLinearDimensionBuilderBuilder;
        protected: SketchLinearDimensionBuilder();
        public: ~SketchLinearDimensionBuilder();
        /**Returns  the driving value builder, which manages driving dimension values 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Annotations::DrivingValueBuilder * Driving
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
