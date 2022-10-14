#ifndef NXOpen_AME_PARAMETERRULEBUILDER_HXX_INCLUDED
#define NXOpen_AME_PARAMETERRULEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ParameterRuleBuilder.ja
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
#include <NXOpen/AME_ObjectConnectionBuilder.hxx>
#include <NXOpen/AME_ObjectConnectionDetailBuilder.hxx>
#include <NXOpen/AME_ParameterRuleBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class ParameterRuleBuilder;
    }
    namespace AME
    {
        class ObjectConnectionBuilder;
    }
    namespace AME
    {
        class ObjectConnectionDetailBuilder;
    }
    class Builder;
    namespace AME
    {
        class _ParameterRuleBuilderBuilder;
        class ParameterRuleBuilderImpl;
        /** JA class for the parameter rule dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateParameterRuleBuilder  NXOpen::AME::AMEManager::CreateParameterRuleBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ParameterRuleBuilder : public NXOpen::Builder
        {
            private: ParameterRuleBuilderImpl * m_parameterrulebuilder_impl;
            private: friend class  _ParameterRuleBuilderBuilder;
            protected: ParameterRuleBuilder();
            public: ~ParameterRuleBuilder();
            /**Returns  the object connection ui block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ObjectConnectionBuilder * ObjectConnection
            (
            );
            /**Returns  the object connection detail ui block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ObjectConnectionDetailBuilder * ObjectConnectionDetail
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