#ifndef NXOpen_ANNOTATIONS_PRODUCTGRIDSTYLEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PRODUCTGRIDSTYLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ProductGridStyleBuilder.ja
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
#include <NXOpen/Annotations.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class ProductGridStyleBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXColor;
    namespace Annotations
    {
        class _ProductGridStyleBuilderBuilder;
        class ProductGridStyleBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a @link NXOpen::Annotations::ProductGridStyleBuilder NXOpen::Annotations::ProductGridStyleBuilder@endlink .
            This class queries and sets preferences for product grid type annotations when creating or editing.
            
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  ProductGridStyleBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** The location of a grid label relative to its grid value */
            public: enum GridLabelLocation
            {
                GridLabelLocationBefore/** before */ ,
                GridLabelLocationAfter/** after */ ,
                GridLabelLocationAbove/** above */ ,
                GridLabelLocationBelow/** below */ 
            };

            /** The display of grid labels for the horizontal axis of a product grid */
            public: enum HorizontalLabelDisplay
            {
                HorizontalLabelDisplayBefore/** before */ ,
                HorizontalLabelDisplayAfter/** after */ ,
                HorizontalLabelDisplayBeforeAfter/** before after */ ,
                HorizontalLabelDisplayNone/** none */ 
            };

            /** The display of grid labels for the vertical axis of a product grid */
            public: enum VerticalLabelDisplay
            {
                VerticalLabelDisplayBelow/** below */ ,
                VerticalLabelDisplayAbove/** above */ ,
                VerticalLabelDisplayAboveBelow/** above below */ ,
                VerticalLabelDisplayNone/** none */ 
            };

            private: ProductGridStyleBuilderImpl * m_productgridstylebuilder_impl;
            private: friend class  _ProductGridStyleBuilderBuilder;
            protected: ProductGridStyleBuilder();
            public: ~ProductGridStyleBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the label used to identify the product grid reference CSYS X axis 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ReferenceXAxisLabel
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the label used to identify the product grid reference CSYS X axis 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetReferenceXAxisLabel
            (
                const NXString & referenceXAxisLabel /** referencexaxislabel */ 
            );
            /**Sets  the label used to identify the product grid reference CSYS X axis 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            void SetReferenceXAxisLabel
            (
                const char * referenceXAxisLabel /** referencexaxislabel */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the label used to identify the product grid reference CSYS Y axis 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ReferenceYAxisLabel
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the label used to identify the product grid reference CSYS Y axis 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetReferenceYAxisLabel
            (
                const NXString & referenceYAxisLabel /** referenceyaxislabel */ 
            );
            /**Sets  the label used to identify the product grid reference CSYS Y axis 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            void SetReferenceYAxisLabel
            (
                const char * referenceYAxisLabel /** referenceyaxislabel */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the label used to identify the product grid reference CSYS Z axis 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ReferenceZAxisLabel
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the label used to identify the product grid reference CSYS Z axis 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetReferenceZAxisLabel
            (
                const NXString & referenceZAxisLabel /** referencezaxislabel */ 
            );
            /**Sets  the label used to identify the product grid reference CSYS Z axis 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            void SetReferenceZAxisLabel
            (
                const char * referenceZAxisLabel /** referencezaxislabel */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the grid spacing 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: double GridSpacing
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the grid spacing 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetGridSpacing
            (
                double gridSpacing /** gridspacing */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the grid overhang 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: double GridOverhang
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the grid overhang 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetGridOverhang
            (
                double gridOverhang /** gridoverhang */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  whether horizontal grid lines are displayed 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowHorizontalGridLines
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  whether horizontal grid lines are displayed 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetShowHorizontalGridLines
            (
                bool showHorizontalGridLines /** showhorizontalgridlines */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  whether vertical grid lines are displayed 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowVerticalGridLines
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  whether vertical grid lines are displayed 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetShowVerticalGridLines
            (
                bool showVerticalGridLines /** showverticalgridlines */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the line color 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * LineColor
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the line color 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLineColor
            (
                NXOpen::NXColor * lineColor /** linecolor */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the line font 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectFont LineFont
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the line font 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLineFont
            (
                NXOpen::DisplayableObject::ObjectFont lineFont /** linefont */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the line width 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth LineWidth
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the line width 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLineWidth
            (
                NXOpen::Annotations::LineWidth lineWidth /** linewidth */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the location of horizontal labels relative to the product grid 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ProductGridStyleBuilder::HorizontalLabelDisplay LocationRelativeGridHorizontal
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the location of horizontal labels relative to the product grid 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLocationRelativeGridHorizontal
            (
                NXOpen::Annotations::ProductGridStyleBuilder::HorizontalLabelDisplay locationRelativeGridHorizontal /** locationrelativegridhorizontal */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the location of vertical labels relative to the product grid 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ProductGridStyleBuilder::VerticalLabelDisplay LocationRelativeGridVertical
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the location of vertical labels relative to the product grid 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLocationRelativeGridVertical
            (
                NXOpen::Annotations::ProductGridStyleBuilder::VerticalLabelDisplay locationRelativeGridVertical /** locationrelativegridvertical */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the location of the grid label relative to the grid value 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ProductGridStyleBuilder::GridLabelLocation LocationRelativeGridValue
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the location of the grid label relative to the grid value 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLocationRelativeGridValue
            (
                NXOpen::Annotations::ProductGridStyleBuilder::GridLabelLocation locationRelativeGridValue /** locationrelativegridvalue */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the label gap 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: double LabelGap
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the label gap 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLabelGap
            (
                double labelGap /** labelgap */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the label divisor 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: double LabelDivisor
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the label divisor 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLabelDivisor
            (
                double labelDivisor /** labeldivisor */ 
            );

            /// \endcond 
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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
