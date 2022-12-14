#ifndef NXOpen_SAFETY_BODYBUILDER_HXX_INCLUDED
#define NXOpen_SAFETY_BODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Safety_BodyBuilder.ja
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
        class BodyBuilder;
    }
    namespace Safety
    {
        class EntityBuilder;
    }
    namespace Safety
    {
        class _BodyBuilderBuilder;
        class BodyBuilderImpl;
        /** Represents a builder of Safety Body object  <br> To create a new instance of this class, use @link NXOpen::Safety::BodyManager::CreateBodyBuilder  NXOpen::Safety::BodyManager::CreateBodyBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class SAFETYOPENCPPEXPORT  BodyBuilder : public NXOpen::Safety::EntityBuilder
        {
            private: BodyBuilderImpl * m_bodybuilder_impl;
            private: friend class  _BodyBuilderBuilder;
            protected: BodyBuilder();
            public: ~BodyBuilder();
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
