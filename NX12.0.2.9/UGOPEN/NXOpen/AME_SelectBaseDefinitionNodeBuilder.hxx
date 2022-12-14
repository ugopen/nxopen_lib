#ifndef NXOpen_AME_SELECTBASEDEFINITIONNODEBUILDER_HXX_INCLUDED
#define NXOpen_AME_SELECTBASEDEFINITIONNODEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_SelectBaseDefinitionNodeBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class SelectBaseDefinitionNodeBuilder;
    }
    namespace AME
    {
        class SelectAMEBaseNode;
    }
    class Builder;
    class NXObject;
    namespace AME
    {
        class _SelectBaseDefinitionNodeBuilderBuilder;
        class SelectBaseDefinitionNodeBuilderImpl;
        /** Builder for selecting base definition node from navigators <br> This object does not need a creator  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  SelectBaseDefinitionNodeBuilder : public NXOpen::Builder
        {
            private: SelectBaseDefinitionNodeBuilderImpl * m_selectbasedefinitionnodebuilder_impl;
            private: friend class  _SelectBaseDefinitionNodeBuilderBuilder;
            protected: SelectBaseDefinitionNodeBuilder();
            public: ~SelectBaseDefinitionNodeBuilder();
            /**Returns  the selected Object 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAMEBaseNode * SelectObject
            (
            );
            /**Sets the selected base definition node object
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSelectedNode
            (
                NXOpen::NXObject * baseNode /** basenode */ 
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
