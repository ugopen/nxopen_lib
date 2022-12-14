#ifndef NXOpen_AME_DEFINEASPECTBUILDER_HXX_INCLUDED
#define NXOpen_AME_DEFINEASPECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_DefineAspectBuilder.ja
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
#include <NXOpen/AME_DefineAspectBuilder.hxx>
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
        class DefineAspectBuilder;
    }
    class Builder;
    namespace AME
    {
        class _DefineAspectBuilderBuilder;
        class DefineAspectBuilderImpl;
        /** Define Aspects for Engineering Object Definition  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::DefineAspectBuilder  NXOpen::AME::AMEManager::DefineAspectBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  DefineAspectBuilder : public NXOpen::Builder
        {
            private: DefineAspectBuilderImpl * m_defineaspectbuilder_impl;
            private: friend class  _DefineAspectBuilderBuilder;
            protected: DefineAspectBuilder();
            public: ~DefineAspectBuilder();
            /**Sets  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFunction
            (
                bool val /** val */ 
            );
            /**Returns  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool Function
            (
            );
            /**Sets  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetLocation
            (
                bool val /** val */ 
            );
            /**Returns  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool Location
            (
            );
            /**Sets  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetProduct
            (
                bool val /** val */ 
            );
            /**Returns  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool Product
            (
            );
            /**Sets  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFunctionDesignation
            (
                bool val /** val */ 
            );
            /**Returns  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool FunctionDesignation
            (
            );
            /**Sets  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetLocationDesignation
            (
                bool val /** val */ 
            );
            /**Returns  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool LocationDesignation
            (
            );
            /**Sets  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetProductDesignation
            (
                bool val /** val */ 
            );
            /**Returns  the value for Function Aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool ProductDesignation
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
