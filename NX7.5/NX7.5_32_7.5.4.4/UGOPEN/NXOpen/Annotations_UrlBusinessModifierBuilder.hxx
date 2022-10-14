#ifndef NXOpen_ANNOTATIONS_URLBUSINESSMODIFIERBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_URLBUSINESSMODIFIERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_UrlBusinessModifierBuilder.ja
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
#include <NXOpen/Annotations_UrlBusinessModifierBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class UrlBusinessModifierBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _UrlBusinessModifierBuilderBuilder;
        class UrlBusinessModifierBuilderImpl;
        /** Represents a @link Annotations::UrlBusinessModifier Annotations::UrlBusinessModifier@endlink  builder  <br> To create a new instance of this class, use @link Annotations::BusinessModifierCollection::CreateUrlBusinessModifierBuilder Annotations::BusinessModifierCollection::CreateUrlBusinessModifierBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  UrlBusinessModifierBuilder : public Builder
        {
            private: UrlBusinessModifierBuilderImpl * m_urlbusinessmodifierbuilder_impl;
            private: friend class  _UrlBusinessModifierBuilderBuilder;
            protected: UrlBusinessModifierBuilder();
            public: ~UrlBusinessModifierBuilder();
            /**Returns  the str title  <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the str title  <br> License requirements : geometric_tol ("GDT") */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Returns  the url  <br> License requirements : None */
            public: NXString Url
            (
            );
            /**Sets  the url  <br> License requirements : geometric_tol ("GDT") */
            public: void SetUrl
            (
                const NXString & url /** url */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif