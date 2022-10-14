#ifndef NXOpen_AME_EPLANIMPORTPROJECTTEMPLATEBUILDER_HXX_INCLUDED
#define NXOpen_AME_EPLANIMPORTPROJECTTEMPLATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_EplanImportProjectTemplateBuilder.ja
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
#include <NXOpen/AME_EplanImportProjectTemplateBuilder.hxx>
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
        class EplanImportProjectTemplateBuilder;
    }
    class Builder;
    namespace AME
    {
        class _EplanImportProjectTemplateBuilderBuilder;
        class EplanImportProjectTemplateBuilderImpl;
        /** EplanImportProjectTemplateBuilder  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateEplanImportProjectTemplateBuilder  NXOpen::AME::AMEManager::CreateEplanImportProjectTemplateBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  EplanImportProjectTemplateBuilder : public NXOpen::Builder
        {
            private: EplanImportProjectTemplateBuilderImpl * m_eplanimportprojecttemplatebuilder_impl;
            private: friend class  _EplanImportProjectTemplateBuilderBuilder;
            protected: EplanImportProjectTemplateBuilder();
            public: ~EplanImportProjectTemplateBuilder();
            /**Returns  the project template file 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString ProjectTemplateFile
            (
            );
            /**Sets  the project template file 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetProjectTemplateFile
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the project template file 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetProjectTemplateFile
            (
                const char * filename /** filename */ 
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