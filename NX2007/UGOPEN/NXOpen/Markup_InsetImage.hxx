#ifndef NXOpen_MARKUP_INSETIMAGE_HXX_INCLUDED
#define NXOpen_MARKUP_INSETIMAGE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Markup_InsetImage.ja
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
        class InsetImage;
    }
    namespace Markup
    {
        class Element;
    }
    namespace Markup
    {
        class _InsetImageBuilder;
        class InsetImageImpl;
        /**
                Represents a @link NXOpen::Markup::InsetImage NXOpen::Markup::InsetImage@endlink 
             <br> To create or edit an instance of this class, use @link NXOpen::Markup::ElementBuilder  NXOpen::Markup::ElementBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_MARKUPEXPORT  InsetImage : public NXOpen::Markup::Element
        {
            private: InsetImageImpl * m_insetimage_impl;
            private: friend class  _InsetImageBuilder;
            protected: InsetImage();
            public: ~InsetImage();
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