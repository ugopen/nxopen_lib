#ifndef NXOpen_AME_APPLICATIONBUILDER_HXX_INCLUDED
#define NXOpen_AME_APPLICATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ApplicationBuilder.ja
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
#include <NXOpen/AME_GlobalSelectionBuilder.hxx>
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
        class ApplicationBuilder;
    }
    namespace AME
    {
        class GlobalSelectionBuilder;
    }
    namespace AME
    {
        class Project;
    }
    class NXObject;
    class Part;
    namespace AME
    {
        class _ApplicationBuilderBuilder;
        class ApplicationBuilderImpl;
        /** Create the AD application builder see AMEApplicationBuilder <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateApplicationBuilder  NXOpen::AME::AMEManager::CreateApplicationBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ApplicationBuilder : public NXOpen::NXObject
        {
            private: ApplicationBuilderImpl * m_applicationbuilder_impl;
            private: friend class  _ApplicationBuilderBuilder;
            protected: ApplicationBuilder();
            public: ~ApplicationBuilder();
            /**  Enter the Automation Designer application. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void Enter
            (
            );
            /**  Exit the Automation Designer application and delete builder.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void Exit
            (
            );
            /** Set collaborative design
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void EstablishProject
            (
                const NXString & uid /** uid */ 
            );
            /** Set collaborative design
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void EstablishProject
            (
                const char * uid /** uid */ 
            );
            /** Get the project object
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::Project * GetProject
            (
            );
            /** Get the global selection builder
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::GlobalSelectionBuilder * GetGlobalSelectionBuilder
            (
            );
            /**  Save the current Automation Designer project.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SaveProject
            (
            );
            /**  Create a CD for workset part.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::Project * CreateCollaborativeDesign
            (
                NXOpen::Part * workSet /** workset */ 
            );
            /**  Create a CD for workset part with predefined ID
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::Project * CreateCollaborativeDesign
            (
                NXOpen::Part * workSet /** workset */ ,
                const NXString & cdID /** cdid */ 
            );
            /**  Create a CD for workset part with predefined ID
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            NXOpen::AME::Project * CreateCollaborativeDesign
            (
                NXOpen::Part * workSet /** workset */ ,
                const char * cdID /** cdid */ 
            );
            /**  Create a new project for workset part.
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::Project * EstablishNewProject
            (
                NXOpen::Part * workSet /** workset */ 
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
