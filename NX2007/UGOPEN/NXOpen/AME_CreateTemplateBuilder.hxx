#ifndef NXOpen_AME_CREATETEMPLATEBUILDER_HXX_INCLUDED
#define NXOpen_AME_CREATETEMPLATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_CreateTemplateBuilder.ja
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
#include <NXOpen/AME_ObjectNameBuilder.hxx>
#include <NXOpen/AME_Project.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class CreateTemplateBuilder;
    }
    namespace AME
    {
        class ObjectNameBuilder;
    }
    namespace AME
    {
        class Project;
    }
    class Builder;
    class SelectNXObjectList;
    namespace AME
    {
        class _CreateTemplateBuilderBuilder;
        class CreateTemplateBuilderImpl;
        /**Create Template dialog JA class  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateTemplateBuilder  NXOpen::AME::AMEManager::CreateTemplateBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  CreateTemplateBuilder : public NXOpen::Builder
        {
            private: CreateTemplateBuilderImpl * m_createtemplatebuilder_impl;
            private: friend class  _CreateTemplateBuilderBuilder;
            protected: CreateTemplateBuilder();
            public: ~CreateTemplateBuilder();
            /**Returns  the selected objects from project
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::SelectNXObjectList * SelectedObjects
            (
            );
            /**Returns  the template name and description ui block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ObjectNameBuilder * TemplateNameAndDescription
            (
            );
            /**Sets  the template toggle for create fragment
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCreateFragmentToggle
            (
                bool createFragmentToggle /** createfragmenttoggle */ 
            );
            /**Returns  the template toggle for create fragment
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool CreateFragmentToggle
            (
            );
            /**Creates the template project
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::Project * CreateTemplateProject
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