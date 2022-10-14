#ifndef NXOpen_MARKUP_RECTANGLE_HXX_INCLUDED
#define NXOpen_MARKUP_RECTANGLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Markup_Rectangle.ja
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
#include <NXOpen/Markup_Rectangle.hxx>
#include <NXOpen/Markup_MarkupObject.hxx>
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
        class Rectangle;
    }
    namespace Markup
    {
        class MarkupObject;
    }
    namespace Markup
    {
        class _RectangleBuilder;
        class RectangleImpl;

        /// \cond NX_NO_DOC 
        /**
                Represents a @link NXOpen::Markup::Rectangle NXOpen::Markup::Rectangle@endlink 
             <br> To create a new instance of this class, use @link NXOpen::Markup::MarkupFileObjectCollection::CreateRectangle  NXOpen::Markup::MarkupFileObjectCollection::CreateRectangle @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_MARKUPEXPORT  Rectangle : public NXOpen::Markup::MarkupObject
        {
            private: RectangleImpl * m_rectangle_impl;
            private: friend class  _RectangleBuilder;
            protected: Rectangle();
            public: ~Rectangle();
            /** Gets center length and width 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void GetCenterLengthAndWidth
            (
                NXOpen::Point2d* center /** center */ ,
                double* length /** length */ ,
                double* width /** width */ 
            );
            /** Sets center length and width 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCenterLengthAndWidth
            (
                const NXOpen::Point2d & center /** center */ ,
                double length /** length */ ,
                double width /** width */ 
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