#ifndef NXOpen_DIAGRAMMING_LINERENDERINGPROPERTIESBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_LINERENDERINGPROPERTIESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_LineRenderingPropertiesBuilder.ja
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
#include <NXOpen/Diagramming_LineRenderingPropertiesBuilder.hxx>
#include <NXOpen/Diagramming_BaseSubObjectBuilder.hxx>
#include <NXOpen/libnxopencpp_diagramming_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Diagramming
    {
        class LineRenderingPropertiesBuilder;
    }
    namespace Diagramming
    {
        class BaseSubObjectBuilder;
    }
    class NXColor;
    namespace Diagramming
    {
        class _LineRenderingPropertiesBuilderBuilder;
        class LineRenderingPropertiesBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a LineRenderingPropertiesBuilder.
             <br> This is a sub-builder class and cannot be directly instantiated  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  LineRenderingPropertiesBuilder : public NXOpen::Diagramming::BaseSubObjectBuilder
        {
            private: LineRenderingPropertiesBuilderImpl * m_linerenderingpropertiesbuilder_impl;
            private: friend class  _LineRenderingPropertiesBuilderBuilder;
            protected: LineRenderingPropertiesBuilder();
            public: ~LineRenderingPropertiesBuilder();
            /**Returns  the stroke color. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * StrokeColor
            (
            );
            /**Sets  the stroke color. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStrokeColor
            (
                NXOpen::NXColor * colorId /** colorid */ 
            );
            /**Returns  the stroke opacity. The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double StrokeOpacity
            (
            );
            /**Sets  the stroke opacity. The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStrokeOpacity
            (
                double opacity /** opacity */ 
            );
            /**Returns  the stroke width. It should be equal or greater than 1. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int StrokeWidth
            (
            );
            /**Sets  the stroke width. It should be equal or greater than 1. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStrokeWidth
            (
                int width /** width */ 
            );
            /** Get the lengths of dashes and gaps which compose the pattern of a dash line. The two output arrays have the same length. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void GetDashArray
            (
                std::vector<int> & dashArray /** dasharray */ ,
                std::vector<int> & gapArray /** gaparray */ 
            );
            /** Set the lengths of dashs and gaps which compose the pattern of a dash line. The two input arrays should have the same length
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDashArray
            (
                const std::vector<int> & dashArray /** dasharray */ ,
                const std::vector<int> & gapArray /** gaparray */ 
            );
            /**Returns  the fill color. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * FillColor
            (
            );
            /**Sets  the fill color. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFillColor
            (
                NXOpen::NXColor * colorId /** colorid */ 
            );
            /**Returns  the fill opacity. The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double FillOpacity
            (
            );
            /**Sets  the fill opacity. The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFillOpacity
            (
                double opacity /** opacity */ 
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
