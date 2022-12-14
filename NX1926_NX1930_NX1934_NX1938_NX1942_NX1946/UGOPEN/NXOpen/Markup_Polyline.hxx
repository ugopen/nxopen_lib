#ifndef NXOpen_MARKUP_POLYLINE_HXX_INCLUDED
#define NXOpen_MARKUP_POLYLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Markup_Polyline.ja
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
#include <NXOpen/Markup_Element.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_markup_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Markup
    {
        class Polyline;
    }
    namespace Markup
    {
        class Element;
    }
    namespace Markup
    {
        class _PolylineBuilder;
        class PolylineImpl;

        /// \cond NX_NO_DOC 
        /**
                Represents a @link NXOpen::Markup::Polyline NXOpen::Markup::Polyline@endlink 
             <br> To create a new instance of this class, use @link NXOpen::Markup::ElementCollection::CreatePolyline  NXOpen::Markup::ElementCollection::CreatePolyline @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_MARKUPEXPORT  Polyline : public NXOpen::Markup::Element
        {
            /** Represents the @link NXOpen::Markup::Polyline NXOpen::Markup::Polyline@endlink  line option.
                    */
            public: enum LineOption
            {
                LineOptionLine/** Line type */,
                LineOptionSpline/** Spline type  */
            };

            private: PolylineImpl * m_polyline_impl;
            private: friend class  _PolylineBuilder;
            protected: Polyline();
            public: ~Polyline();
            /**Returns  the line type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Markup::Polyline::LineOption LineType
            (
            );
            /**Sets  the line type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: void SetLineType
            (
                NXOpen::Markup::Polyline::LineOption lineType /** linetype */ 
            );
            /** Gets a list of points 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void GetPoints
            (
                std::vector<NXOpen::Point3d> & points /** points */ 
            );
            /** Sets a list of points 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : dmu_markup ("License to expose DMU functionality in NX desktop") */
            public: void SetPoints
            (
                const std::vector<NXOpen::Point3d> & points /** points */ 
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
