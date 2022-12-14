#ifndef NXOpen_ANNOTATIONS_DIMENSIONSETBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DIMENSIONSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DimensionSetBuilder.ja
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
#include <NXOpen/Annotations_DimensionSetBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class DimensionSetBuilder;
    }
    namespace Annotations
    {
        class SelectAnnotation;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Annotations
    {
        class _DimensionSetBuilderBuilder;
        class DimensionSetBuilderImpl;
        /**
            Represents a @link NXOpen::Annotations::DimensionSetBuilder NXOpen::Annotations::DimensionSetBuilder@endlink 
             <br> This is a sub-builder class and cannot be directly instantiated  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DimensionSetBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** dimension set method */
            public: enum DimensionSetMethod
            {
                DimensionSetMethodNone/** Not part of a set */,
                DimensionSetMethodChain/** Part of a chain */,
                DimensionSetMethodBaseline/** Part of a baseline */
            };

            private: DimensionSetBuilderImpl * m_dimensionsetbuilder_impl;
            private: friend class  _DimensionSetBuilderBuilder;
            protected: DimensionSetBuilder();
            public: ~DimensionSetBuilder();
            /**Returns  the dimension set method 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DimensionSetBuilder::DimensionSetMethod Method
            (
            );
            /**Sets  the dimension set method 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetMethod
            (
                NXOpen::Annotations::DimensionSetBuilder::DimensionSetMethod method /** method */ 
            );
            /**Returns  the dimension or dimension set object 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SelectAnnotation * DimensionOrSet
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
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
