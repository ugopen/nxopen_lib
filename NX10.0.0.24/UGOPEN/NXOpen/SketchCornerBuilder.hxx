#ifndef NXOpen_SKETCHCORNERBUILDER_HXX_INCLUDED
#define NXOpen_SKETCHCORNERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchCornerBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/SketchCornerBuilder.hxx>
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
    class SketchCornerBuilder;
    class Builder;
    class SelectCurveList;
    class _SketchCornerBuilderBuilder;
    class SketchCornerBuilderImpl;
    /**
        Create a corner between two sketch curves.  The curves will be trimmed or extended to the
        intersection point of the input curves.  The reference point for each curve should be near the
        intersection point to designate which part of the curve to keep.  It should be as close as 
        possible to the curve.
         <br> To create a new instance of this class, use @link NXOpen::SketchCollection::CreateCornerBuilder  NXOpen::SketchCollection::CreateCornerBuilder @endlink  <br> 
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SketchCornerBuilder : public NXOpen::Builder
    {
        private: SketchCornerBuilderImpl * m_sketchcornerbuilder_impl;
        private: friend class  _SketchCornerBuilderBuilder;
        protected: SketchCornerBuilder();
        public: ~SketchCornerBuilder();
        /**Returns  the curves to make a corner 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectCurveList * Curves
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
