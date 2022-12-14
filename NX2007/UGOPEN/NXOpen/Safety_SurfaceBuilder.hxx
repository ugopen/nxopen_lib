#ifndef NXOpen_SAFETY_SURFACEBUILDER_HXX_INCLUDED
#define NXOpen_SAFETY_SURFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Safety_SurfaceBuilder.ja
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
#include <NXOpen/Safety_EntityBuilder.hxx>
#include <NXOpen/libsafetyopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Safety
    {
        class SurfaceBuilder;
    }
    namespace Safety
    {
        class EntityBuilder;
    }
    namespace Safety
    {
        class _SurfaceBuilderBuilder;
        class SurfaceBuilderImpl;
        /** Represents a builder of Surface object  <br> To create a new instance of this class, use @link NXOpen::Safety::SurfaceManager::CreateSurfaceBuilder  NXOpen::Safety::SurfaceManager::CreateSurfaceBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class SAFETYOPENCPPEXPORT  SurfaceBuilder : public NXOpen::Safety::EntityBuilder
        {
            private: SurfaceBuilderImpl * m_surfacebuilder_impl;
            private: friend class  _SurfaceBuilderBuilder;
            protected: SurfaceBuilder();
            public: ~SurfaceBuilder();
            /**Returns  the entity name.  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString EntityName
            (
            );
            /**Sets  the entity name.  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetEntityName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the entity name.  
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetEntityName
            (
                const char * name /** name */ 
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
