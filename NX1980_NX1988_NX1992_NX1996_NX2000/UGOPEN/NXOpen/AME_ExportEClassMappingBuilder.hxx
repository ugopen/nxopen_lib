#ifndef NXOpen_AME_EXPORTECLASSMAPPINGBUILDER_HXX_INCLUDED
#define NXOpen_AME_EXPORTECLASSMAPPINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ExportEClassMappingBuilder.ja
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
        class ExportEClassMappingBuilder;
    }
    namespace AME
    {
        class SelectAMEBaseNode;
    }
    class Builder;
    namespace AME
    {
        class _ExportEClassMappingBuilderBuilder;
        class ExportEClassMappingBuilderImpl;
        /** Export eclass mapping into file <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateExportEclassMappingBuilder  NXOpen::AME::AMEManager::CreateExportEclassMappingBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ExportEClassMappingBuilder : public NXOpen::Builder
        {
            private: ExportEClassMappingBuilderImpl * m_exporteclassmappingbuilder_impl;
            private: friend class  _ExportEClassMappingBuilderBuilder;
            protected: ExportEClassMappingBuilder();
            public: ~ExportEClassMappingBuilder();
            /**Returns  the EClass node selection 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAMEBaseNode * SelectEClassNode
            (
            );
            /**Returns  the output folder path to save eclass mapping file
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString FolderPath
            (
            );
            /**Sets  the output folder path to save eclass mapping file
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFolderPath
            (
                const NXString & folderPath /** folderpath */ 
            );
            /**Sets  the output folder path to save eclass mapping file
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetFolderPath
            (
                const char * folderPath /** folderpath */ 
            );
            /** Validate directory path for export eClass mapping
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ValidateFolderPath
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