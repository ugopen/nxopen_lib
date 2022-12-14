#ifndef NXOpen_ANNOTATIONS_BASEPRODUCTGRIDBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_BASEPRODUCTGRIDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_BaseProductGridBuilder.ja
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
#include <NXOpen/Annotations_StyleBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class BaseProductGridBuilder;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    class Builder;
    class CoordinateSystem;
    namespace Annotations
    {
        class _BaseProductGridBuilderBuilder;
        class BaseProductGridBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link NXOpen::Annotations::BaseProductGridBuilder NXOpen::Annotations::BaseProductGridBuilder@endlink .
            This class allows to creation of a product grid annotation
             <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  BaseProductGridBuilder : public NXOpen::Builder
        {
            private: BaseProductGridBuilderImpl * m_baseproductgridbuilder_impl;
            private: friend class  _BaseProductGridBuilderBuilder;
            protected: BaseProductGridBuilder();
            public: ~BaseProductGridBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the coordinate system 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * CoordinateSystem
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the coordinate system 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetCoordinateSystem
            (
                NXOpen::CoordinateSystem * coordinateSystem /** coordinatesystem */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the grid spacing 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double GridSpacing
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the grid spacing 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetGridSpacing
            (
                double gridSpacing /** gridspacing */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the horizontal line display 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowHorizontalLines
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the horizontal line display 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetShowHorizontalLines
            (
                bool showHorizontalLines /** showhorizontallines */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the horizontal minimum value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double HorizontalMinimumValue
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the horizontal minimum value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHorizontalMinimumValue
            (
                double horizontalMinimumValue /** horizontalminimumvalue */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the horizontal maximum value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double HorizontalMaximumValue
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the horizontal maximum value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHorizontalMaximumValue
            (
                double horizontalMaximumValue /** horizontalmaximumvalue */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the vertical line display 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowVerticalLines
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the vertical line display 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetShowVerticalLines
            (
                bool showVerticalLines /** showverticallines */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the vertical minimum value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double VerticalMinimumValue
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the vertical minimum value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetVerticalMinimumValue
            (
                double verticalMinimumValue /** verticalminimumvalue */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the vertical maximum value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double VerticalMaximumValue
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the vertical maximum value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetVerticalMaximumValue
            (
                double verticalMaximumValue /** verticalmaximumvalue */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the style 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * Style
            (
            );

            /// \endcond 
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
