#ifndef NXOpen_AME_BASEDEFINITIONATTRIBUTEHOLDER_HXX_INCLUDED
#define NXOpen_AME_BASEDEFINITIONATTRIBUTEHOLDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_BaseDefinitionAttributeHolder.ja
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
#include <NXOpen/NXObject.hxx>
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
        class BaseDefinitionAttributeHolder;
    }
    class NXObject;
    namespace AME
    {
        class _BaseDefinitionAttributeHolderBuilder;
        class BaseDefinitionAttributeHolderImpl;
        /** BaseDefinition Atributes Holder Object  <br> This does not need a creator.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  BaseDefinitionAttributeHolder : public NXOpen::NXObject
        {
            private: BaseDefinitionAttributeHolderImpl * m_basedefinitionattributeholder_impl;
            private: friend class  _BaseDefinitionAttributeHolderBuilder;
            protected: BaseDefinitionAttributeHolder();
            public: ~BaseDefinitionAttributeHolder();
            /** Set BaseDefinition 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetBasedefinition
            (
                NXOpen::NXObject * baseDef /** basedef */ 
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
