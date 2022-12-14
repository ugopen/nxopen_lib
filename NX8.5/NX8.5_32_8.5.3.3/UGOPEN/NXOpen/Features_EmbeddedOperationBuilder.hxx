#ifndef NXOpen_FEATURES_EMBEDDEDOPERATIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_EMBEDDEDOPERATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_EmbeddedOperationBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class EmbeddedOperationBuilder;
    }
    class Builder;
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _EmbeddedOperationBuilderBuilder;
        class EmbeddedOperationBuilderImpl;
        /** Represents an EmbeddedOperationBuilder  <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  EmbeddedOperationBuilder : public Builder
        {
            private: EmbeddedOperationBuilderImpl * m_embeddedoperationbuilder_impl;
            private: friend class  _EmbeddedOperationBuilderBuilder;
            protected: EmbeddedOperationBuilder();
            public: ~EmbeddedOperationBuilder();
            /** Commits the operation and creates the feature  @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::Feature * CommitOperation
            (
            );
            /** Returns the feature currently being edited by this builder. If
                    a new feature is being created, and the builder has not yet
                    been commited, returns NULL.
                  @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::Feature * GetOperation
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
