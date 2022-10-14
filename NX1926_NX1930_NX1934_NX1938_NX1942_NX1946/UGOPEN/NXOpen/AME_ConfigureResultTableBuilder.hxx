#ifndef NXOpen_AME_CONFIGURERESULTTABLEBUILDER_HXX_INCLUDED
#define NXOpen_AME_CONFIGURERESULTTABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ConfigureResultTableBuilder.ja
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
        class ConfigureResultTableBuilder;
    }
    class Builder;
    namespace AME
    {
        class _ConfigureResultTableBuilderBuilder;
        class ConfigureResultTableBuilderImpl;
        /** Represents configure result table class builder  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateConfigureResultTableBuilder  NXOpen::AME::AMEManager::CreateConfigureResultTableBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ConfigureResultTableBuilder : public NXOpen::Builder
        {
            private: ConfigureResultTableBuilderImpl * m_configureresulttablebuilder_impl;
            private: friend class  _ConfigureResultTableBuilderBuilder;
            protected: ConfigureResultTableBuilder();
            public: ~ConfigureResultTableBuilder();
            /** The action to add properties 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void Add
            (
                const NXString & objectTypeName /** objecttypename */ ,
                const NXString & groupName /** groupname */ ,
                const NXString & propertyName /** propertyname */ 
            );
            /** The action to add properties 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void Add
            (
                const char * objectTypeName /** objecttypename */ ,
                const char * groupName /** groupname */ ,
                const char * propertyName /** propertyname */ 
            );
            /** The action to move added column up 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void MoveUp
            (
                const NXString & objectTypeName /** objecttypename */ ,
                const NXString & groupName /** groupname */ ,
                const NXString & propertyName /** propertyname */ 
            );
            /** The action to move added column up 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void MoveUp
            (
                const char * objectTypeName /** objecttypename */ ,
                const char * groupName /** groupname */ ,
                const char * propertyName /** propertyname */ 
            );
            /** The action to move earlier added column 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void Remove
            (
                const NXString & objectTypeName /** objecttypename */ ,
                const NXString & groupName /** groupname */ ,
                const NXString & propertyName /** propertyname */ 
            );
            /** The action to move earlier added column 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void Remove
            (
                const char * objectTypeName /** objecttypename */ ,
                const char * groupName /** groupname */ ,
                const char * propertyName /** propertyname */ 
            );
            /** The action to move added column down 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void MoveDown
            (
                const NXString & objectTypeName /** objecttypename */ ,
                const NXString & groupName /** groupname */ ,
                const NXString & propertyName /** propertyname */ 
            );
            /** The action to move added column down 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void MoveDown
            (
                const char * objectTypeName /** objecttypename */ ,
                const char * groupName /** groupname */ ,
                const char * propertyName /** propertyname */ 
            );
            /** The visibility status of each column or group 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetVisibility
            (
                const NXString & objectTypeName /** objecttypename */ ,
                const NXString & groupName /** groupname */ ,
                const NXString & propertyName /** propertyname */ ,
                bool visibility /** visibility */ 
            );
            /** The visibility status of each column or group 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetVisibility
            (
                const char * objectTypeName /** objecttypename */ ,
                const char * groupName /** groupname */ ,
                const char * propertyName /** propertyname */ ,
                bool visibility /** visibility */ 
            );
            /** The action to add sorting criteria 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void AddSortingCriteria
            (
                const NXString & objectType /** objecttype */ ,
                const NXString & categoryType /** categorytype */ ,
                const NXString & propertyName /** propertyname */ ,
                const NXString & sortType /** sorttype */ 
            );
            /** The action to add sorting criteria 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void AddSortingCriteria
            (
                const char * objectType /** objecttype */ ,
                const char * categoryType /** categorytype */ ,
                const char * propertyName /** propertyname */ ,
                const char * sortType /** sorttype */ 
            );
            /** The action to clear sorting criteria
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ClearSortingCriteria
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