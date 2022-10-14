#ifndef NXOpen_ANNOTATIONS_RETAINEDANNOTATIONSBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_RETAINEDANNOTATIONSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_RetainedAnnotationsBuilder.ja
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
#include <NXOpen/LineColorFontWidthBuilder.hxx>
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
        class RetainedAnnotationsBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class LineColorFontWidthBuilder;
    namespace Annotations
    {
        class _RetainedAnnotationsBuilderBuilder;
        class RetainedAnnotationsBuilderImpl;
        /**
            Represents a @link NXOpen::Annotations::RetainedAnnotationsBuilder NXOpen::Annotations::RetainedAnnotationsBuilder@endlink 
            
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  RetainedAnnotationsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: RetainedAnnotationsBuilderImpl * m_retainedannotationsbuilder_impl;
            private: friend class  _RetainedAnnotationsBuilderBuilder;
            protected: RetainedAnnotationsBuilder();
            public: ~RetainedAnnotationsBuilder();
            /**Returns  the flag indicating to show the retained annotations. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowRetainedAnnotations
            (
            );
            /**Sets  the flag indicating to show the retained annotations. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetShowRetainedAnnotations
            (
                bool showRetainedAnnotations /** showretainedannotations */ 
            );
            /**Returns  the line color font width of retained drafting objects.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * LineColorFontWidth
            (
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