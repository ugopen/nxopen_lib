#ifndef NXOpen_MECHATRONICS_SIGNALMAPPINGBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_SIGNALMAPPINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_SignalMappingBuilder.ja
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
#include <NXOpen/Mechatronics_SignalMappingBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class SignalMappingBuilder;
    }
    class Builder;
    namespace Mechatronics
    {
        class SignalConnectionBuilderList;
    }
    namespace Mechatronics
    {
        class _SignalMappingBuilderBuilder;
        class SignalMappingBuilderImpl;
        /** Represents a @link Mechatronics::SignalMappingBuilder Mechatronics::SignalMappingBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Mechatronics::PhysicsManager::CreateSignalMappingBuilder  NXOpen::Mechatronics::PhysicsManager::CreateSignalMappingBuilder @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  SignalMappingBuilder : public NXOpen::Builder
        {
            private: SignalMappingBuilderImpl * m_signalmappingbuilder_impl;
            private: friend class  _SignalMappingBuilderBuilder;
            protected: SignalMappingBuilder();
            public: ~SignalMappingBuilder();
            /**Returns  the signal connection builder list 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::SignalConnectionBuilderList * SignalConnectionList
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