#ifndef NXOpen_AME_ENGINEERINGOBJECTBASEBUILDER_HXX_INCLUDED
#define NXOpen_AME_ENGINEERINGOBJECTBASEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_EngineeringObjectBaseBuilder.ja
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
#include <NXOpen/AME_MultipleObjectsBuilder.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class EngineeringObjectBaseBuilder;
    }
    namespace AME
    {
        class MultipleObjectsBuilder;
    }
    namespace AME
    {
        class _EngineeringObjectBaseBuilderBuilder;
        class EngineeringObjectBaseBuilderImpl;
        /** JA class for the insert Eng object dialog <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  EngineeringObjectBaseBuilder : public NXOpen::AME::MultipleObjectsBuilder
        {
            private: EngineeringObjectBaseBuilderImpl * m_engineeringobjectbasebuilder_impl;
            private: friend class  _EngineeringObjectBaseBuilderBuilder;
            protected: EngineeringObjectBaseBuilder();
            public: ~EngineeringObjectBaseBuilder();
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