#ifndef NXOpen_LINECOLORFONTWIDTHBUILDER_HXX_INCLUDED
#define NXOpen_LINECOLORFONTWIDTHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineColorFontWidthBuilder.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/LineFontBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
    class LineColorFontWidthBuilder;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class LineFontBuilder;
    class NXColor;
    class _LineColorFontWidthBuilderBuilder;
    class LineColorFontWidthBuilderImpl;
    /** 
    Represent a @link NXOpen::LineColorFontWidthBuilder NXOpen::LineColorFontWidthBuilder@endlink  
     <br> This is a sub-builder class and cannot be directly instantiated  <br> 
     <br>  Created in NX9.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  LineColorFontWidthBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
    {
        private: LineColorFontWidthBuilderImpl * m_linecolorfontwidthbuilder_impl;
        private: friend class  _LineColorFontWidthBuilderBuilder;
        protected: LineColorFontWidthBuilder();
        public: ~LineColorFontWidthBuilder();
        /**Returns  the line color 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::NXColor * LineColor
        (
        );
        /**Sets  the line color 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void SetLineColor
        (
            NXOpen::NXColor * lineColor /** linecolor */ 
        );
        /**Returns  the line font 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::LineFontBuilder * LineFont
        (
        );
        /**Returns  the line width 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::DisplayableObject::ObjectWidth LineWidth
        (
        );
        /**Sets  the line width 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void SetLineWidth
        (
            NXOpen::DisplayableObject::ObjectWidth width /** width */ 
        );
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