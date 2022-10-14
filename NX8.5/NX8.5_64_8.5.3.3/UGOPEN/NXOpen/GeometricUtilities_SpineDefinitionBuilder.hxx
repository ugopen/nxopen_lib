#ifndef NXOpen_GEOMETRICUTILITIES_SPINEDEFINITIONBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_SPINEDEFINITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_SpineDefinitionBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_SpineDefinitionBuilder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class SpineDefinitionBuilder;
    }
    class Direction;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Section;
    namespace GeometricUtilities
    {
        class _SpineDefinitionBuilderBuilder;
        class SpineDefinitionBuilderImpl;
        /** Provides a spine definition for modeling operations 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  SpineDefinitionBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** Options to define a spine */
            public: enum MethodOptions
            {
                MethodOptionsNone/** No spine */,
                MethodOptionsCurve/** Spine by curve or a profile*/,
                MethodOptionsVector/** Spine by a vector */
            };

            private: SpineDefinitionBuilderImpl * m_spinedefinitionbuilder_impl;
            private: friend class  _SpineDefinitionBuilderBuilder;
            protected: SpineDefinitionBuilder();
            public: ~SpineDefinitionBuilder();
            /**Returns  the method 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::SpineDefinitionBuilder::MethodOptions Method
            (
            );
            /**Sets  the method 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMethod
            (
                NXOpen::GeometricUtilities::SpineDefinitionBuilder::MethodOptions method /** method */ 
            );
            /**Returns  the section 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * Section
            (
            );
            /**Returns  the vector 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * Vector
            (
            );
            /**Sets  the vector 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetVector
            (
                NXOpen::Direction * vector /** vector */ 
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