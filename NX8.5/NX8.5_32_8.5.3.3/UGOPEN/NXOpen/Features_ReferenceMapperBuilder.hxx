#ifndef NXOpen_FEATURES_REFERENCEMAPPERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_REFERENCEMAPPERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ReferenceMapperBuilder.ja
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
#include <NXOpen/Features_FeatureReferencesBuilder.hxx>
#include <NXOpen/Features_ReferenceMapperBuilder.hxx>
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
        class ReferenceMapperBuilder;
    }
    class Builder;
    namespace Features
    {
        class FeatureReferencesBuilder;
    }
    namespace Features
    {
        class _ReferenceMapperBuilderBuilder;
        class ReferenceMapperBuilderImpl;
        /**
            Represents a @link Features::ReferenceMapperBuilder Features::ReferenceMapperBuilder@endlink 
            It is used in the context of Boolean Target/Tool Mapping. Mapping needs to be done when the
            user edits a Boolean feature and adds/removes tools and/or target.The ReferenceMapper populates 
            @link Features::FeatureReferencesBuilder Features::FeatureReferencesBuilder@endlink  with the references of the removed
            tools and/or target and gives the user an opportunity to map it with the references of the
            newly added tools and/or target.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateReferenceMapperBuilder  Features::FeatureCollection::CreateReferenceMapperBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  ReferenceMapperBuilder : public Builder
        {
            private: ReferenceMapperBuilderImpl * m_referencemapperbuilder_impl;
            private: friend class  _ReferenceMapperBuilderBuilder;
            protected: ReferenceMapperBuilder();
            public: ~ReferenceMapperBuilder();
            /**Returns  the Feature References Builder 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::FeatureReferencesBuilder * FeatureReferences
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