#ifndef NXOpen_ANNOTATIONS_FEATUREIDBUSINESSMODIFIERBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_FEATUREIDBUSINESSMODIFIERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_FeatureIdBusinessModifierBuilder.ja
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
#include <NXOpen/Annotations_FeatureIdBusinessModifierBuilder.hxx>
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
        class FeatureIdBusinessModifierBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _FeatureIdBusinessModifierBuilderBuilder;
        class FeatureIdBusinessModifierBuilderImpl;
        /** Represents a @link NXOpen::Annotations::FeatureIdBusinessModifier NXOpen::Annotations::FeatureIdBusinessModifier@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::BusinessModifierCollection::CreateFeatureIdBusinessModifierBuilder  NXOpen::Annotations::BusinessModifierCollection::CreateFeatureIdBusinessModifierBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  FeatureIdBusinessModifierBuilder : public NXOpen::Builder
        {
            private: FeatureIdBusinessModifierBuilderImpl * m_featureidbusinessmodifierbuilder_impl;
            private: friend class  _FeatureIdBusinessModifierBuilderBuilder;
            protected: FeatureIdBusinessModifierBuilder();
            public: ~FeatureIdBusinessModifierBuilder();
            /**Returns  the str title 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the str title 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Sets  the str title 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            void SetTitle
            (
                const char * title /** title */ 
            );
            /**Returns  the feature ID 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FeatureId
            (
            );
            /**Sets  the feature ID 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetFeatureId
            (
                const NXString & featureId /** featureid */ 
            );
            /**Sets  the feature ID 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            void SetFeatureId
            (
                const char * featureId /** featureid */ 
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
