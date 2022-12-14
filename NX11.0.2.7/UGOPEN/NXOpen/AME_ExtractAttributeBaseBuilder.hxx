#ifndef NXOpen_AME_EXTRACTATTRIBUTEBASEBUILDER_HXX_INCLUDED
#define NXOpen_AME_EXTRACTATTRIBUTEBASEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ExtractAttributeBaseBuilder.ja
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
#include <NXOpen/AME_ExtractAttributeBaseBuilder.hxx>
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
        class ExtractAttributeBaseBuilder;
    }
    class Builder;
    class NXObject;
    namespace AME
    {
        class _ExtractAttributeBaseBuilderBuilder;
        class ExtractAttributeBaseBuilderImpl;
        /** Create a extract attribute   <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ExtractAttributeBaseBuilder : public NXOpen::Builder
        {
            private: ExtractAttributeBaseBuilderImpl * m_extractattributebasebuilder_impl;
            private: friend class  _ExtractAttributeBaseBuilderBuilder;
            protected: ExtractAttributeBaseBuilder();
            public: ~ExtractAttributeBaseBuilder();
            /**Returns  the object context
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString Context
            (
            );
            /**Sets  the object context
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetContext
            (
                const NXString & context /** context */ 
            );
            /**Sets  the object context
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetContext
            (
                const char * context /** context */ 
            );
            /**Returns  the extracted attribute name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString Name
            (
            );
            /**Sets  the extracted attribute name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the extracted attribute name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the object to extract the attribute from 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::NXObject * SourceObject
            (
            );
            /**Sets  the object to extract the attribute from 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSourceObject
            (
                NXOpen::NXObject * selection /** selection */ 
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
