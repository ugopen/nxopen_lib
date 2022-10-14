#ifndef NXOpen_GEOMETRICUTILITIES_QUADRILATERALFRAMEBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_QUADRILATERALFRAMEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_QuadrilateralFrameBuilder.ja
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
#include <NXOpen/GeometricUtilities_QuadrilateralFrameBuilder.hxx>
#include <NXOpen/GeometricUtilities_ShapeFrameBuilder.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class QuadrilateralFrameBuilder;
    }
    namespace GeometricUtilities
    {
        class ShapeFrameBuilder;
    }
    namespace GeometricUtilities
    {
        class _QuadrilateralFrameBuilderBuilder;
        class QuadrilateralFrameBuilderImpl;
        /** Represents a @link NXOpen::GeometricUtilities::QuadrilateralFrameBuilder NXOpen::GeometricUtilities::QuadrilateralFrameBuilder@endlink  
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  QuadrilateralFrameBuilder : public NXOpen::GeometricUtilities::ShapeFrameBuilder
        {
            /** Represents the quadrialteral frame subtypes */
            public: enum Subtypes
            {
                SubtypesArbitrary/** Arbitrary quadrilateral */,
                SubtypesParallelogram/** Parallelogram */,
                SubtypesRectangle/** Rectangle */,
                SubtypesSquare/** Square */
            };

            private: QuadrilateralFrameBuilderImpl * m_quadrilateralframebuilder_impl;
            private: friend class  _QuadrilateralFrameBuilderBuilder;
            protected: QuadrilateralFrameBuilder();
            public: ~QuadrilateralFrameBuilder();
            /**Returns  the subtype 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::QuadrilateralFrameBuilder::Subtypes Subtype
            (
            );
            /**Sets  the subtype 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSubtype
            (
                NXOpen::GeometricUtilities::QuadrilateralFrameBuilder::Subtypes subtype /** subtype */ 
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