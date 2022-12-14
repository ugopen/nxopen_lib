#ifndef NXOpen_ANNOTATIONS_PMIUSERDEFINEDBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIUSERDEFINEDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiUserDefinedBuilder.ja
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
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/Annotations_PmiUserDefinedBuilder.hxx>
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
        class PmiUserDefinedBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class _PmiUserDefinedBuilderBuilder;
        class PmiUserDefinedBuilderImpl;
        /** Represents a @link Annotations::PmiUserDefined Annotations::PmiUserDefined@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreatePmiUserDefinedBuilder  Annotations::PmiAttributeCollection::CreatePmiUserDefinedBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiUserDefinedBuilder : public Annotations::PmiAttributeBuilder
        {
            private: PmiUserDefinedBuilderImpl * m_pmiuserdefinedbuilder_impl;
            private: friend class  _PmiUserDefinedBuilderBuilder;
            protected: PmiUserDefinedBuilder();
            public: ~PmiUserDefinedBuilder();
            /**Returns  the title 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the title 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Sets  the title 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            void SetTitle
            (
                const char * title /** title */ 
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
