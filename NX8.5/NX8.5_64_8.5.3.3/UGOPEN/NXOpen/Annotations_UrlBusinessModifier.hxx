#ifndef NXOpen_ANNOTATIONS_URLBUSINESSMODIFIER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_URLBUSINESSMODIFIER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_UrlBusinessModifier.ja
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
#include <NXOpen/Annotations_BusinessModifier.hxx>
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
        class UrlBusinessModifier;
    }
    namespace Annotations
    {
        class BusinessModifier;
    }
    namespace Annotations
    {
        class _UrlBusinessModifierBuilder;
        class UrlBusinessModifierImpl;
        /** Represents business modifier that applies an URL to a PMI. Please see ug_url_busmod.dfa for attribute details.  <br> To create or edit an instance of this class, use @link Annotations::UrlBusinessModifierBuilder  Annotations::UrlBusinessModifierBuilder @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  UrlBusinessModifier : public Annotations::BusinessModifier
        {
            private: UrlBusinessModifierImpl * m_urlbusinessmodifier_impl;
            private: friend class  _UrlBusinessModifierBuilder;
            protected: UrlBusinessModifier();
            public: ~UrlBusinessModifier();
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