#ifndef NXOpen_DISPLAY_REFLECTION_HXX_INCLUDED
#define NXOpen_DISPLAY_REFLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_Reflection.ja
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
#include <NXOpen/Display_Image.hxx>
#include <NXOpen/Display_Reflection.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_display_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Display
    {
        class Reflection;
    }
    class Builder;
    namespace Display
    {
        class Image;
    }
    namespace Display
    {
        class _ReflectionBuilder;
        class ReflectionImpl;
        /**
            Represents a @link Display::Reflection Display::Reflection@endlink 
            Reflection defines the source of reflection in shiny objects for Studio
            rendering style or High Quality Images.
             <br> This class is restricted to being called from a program running during an 
            Interactive NX session.  If run from a non-interactive session it will 
            return NULL. <br> 
             <br> To create a new instance of this class, use @link NXOpen::ViewCollection::CreateReflection  NXOpen::ViewCollection::CreateReflection @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_DISPLAYEXPORT  Reflection : public NXOpen::Builder
        {
            /** where the reflections for rendering will be obtained */
            public: enum Type
            {
                TypeBackground/** use the background for reflections */,
                TypeStage/** use the stage for reflections */,
                TypeIbl/** use the image-based lighting image for reflections */,
                TypeImage/** use the given image file for reflection */
            };

            private: ReflectionImpl * m_reflection_impl;
            private: friend class  _ReflectionBuilder;
            protected: Reflection();
            public: ~Reflection();
            /**Returns  the reflection type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::Reflection::Type ReflectionMap
            (
            );
            /**Sets  the reflection type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReflectionMap
            (
                NXOpen::Display::Reflection::Type reflectionMap /** reflectionmap */ 
            );
            /**Returns  the reflections's image builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Display::Image * Image
            (
            );
            /**Sets  the reflections's image builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImage
            (
                NXOpen::Display::Image * imageBuilder /** image builder */ 
            );
            /**Returns  the reflection's image filename 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ImageFilename
            (
            );
            /**Sets  the reflection's image filename 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImageFilename
            (
                const NXString & imageFileName /** image file name */ 
            );
            /**Sets  the reflection's image filename 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetImageFilename
            (
                const char * imageFileName /** image file name */ 
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
