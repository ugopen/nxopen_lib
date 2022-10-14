#ifndef NXOpen_ANNOTATIONS_ASSOCIATEDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ASSOCIATEDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_AssociateDimensionBuilder.ja
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
#include <NXOpen/Annotations_AssociateDimensionBuilder.hxx>
#include <NXOpen/Annotations_AssociativityBuilder.hxx>
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
        class AssociateDimensionBuilder;
    }
    namespace Annotations
    {
        class AssociativityBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _AssociateDimensionBuilderBuilder;
        class AssociateDimensionBuilderImpl;
        /**
            Represents a @link Annotations::AssociateDimensionBuilder Annotations::AssociateDimensionBuilder@endlink 
             <br> To create a new instance of this class, use @link Annotations::AnnotationManager::CreateAssociateDimensionBuilder  Annotations::AnnotationManager::CreateAssociateDimensionBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  AssociateDimensionBuilder : public Builder
        {
            private: AssociateDimensionBuilderImpl * m_associatedimensionbuilder_impl;
            private: friend class  _AssociateDimensionBuilderBuilder;
            protected: AssociateDimensionBuilder();
            public: ~AssociateDimensionBuilder();
            /**Returns  the first associativity 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::AssociativityBuilder * Associativity1
            (
            );
            /**Returns  the second associativity 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::AssociativityBuilder * Associativity2
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