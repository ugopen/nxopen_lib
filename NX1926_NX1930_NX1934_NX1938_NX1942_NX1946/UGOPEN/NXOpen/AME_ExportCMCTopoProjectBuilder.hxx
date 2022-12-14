#ifndef NXOpen_AME_EXPORTCMCTOPOPROJECTBUILDER_HXX_INCLUDED
#define NXOpen_AME_EXPORTCMCTOPOPROJECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ExportCMCTopoProjectBuilder.ja
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
        class ExportCMCTopoProjectBuilder;
    }
    namespace AME
    {
        class SelectAMEBaseNode;
    }
    class Builder;
    namespace AME
    {
        class _ExportCMCTopoProjectBuilderBuilder;
        class ExportCMCTopoProjectBuilderImpl;
        /** Export CMC topology into file <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateExportCmctopoProjectBuilder  NXOpen::AME::AMEManager::CreateExportCmctopoProjectBuilder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ExportCMCTopoProjectBuilder : public NXOpen::Builder
        {
            private: ExportCMCTopoProjectBuilderImpl * m_exportcmctopoprojectbuilder_impl;
            private: friend class  _ExportCMCTopoProjectBuilderBuilder;
            protected: ExportCMCTopoProjectBuilder();
            public: ~ExportCMCTopoProjectBuilder();
            /**Returns  the Station node selection 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAMEBaseNode * SelectStationNode
            (
            );
            /**Returns  the output folder path to save CMC topology file
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString FolderPath
            (
            );
            /**Sets  the output folder path to save CMC topology file
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFolderPath
            (
                const NXString & folderPath /** folderpath */ 
            );
            /**Sets  the output folder path to save CMC topology file
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetFolderPath
            (
                const char * folderPath /** folderpath */ 
            );
            /** Generate CMC Topo Project 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void GenerateCMCProject
            (
            );
            /**Returns  the output file name 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString FileName
            (
            );
            /**Sets  the output file name 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFileName
            (
                const NXString & fileName /** filename */ 
            );
            /**Sets  the output file name 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetFileName
            (
                const char * fileName /** filename */ 
            );
            /**Returns  the toggle overwrite existing file 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool ToggleOverwriteExistingFile
            (
            );
            /**Sets  the toggle overwrite existing file 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetToggleOverwriteExistingFile
            (
                bool toggleOverwriteExistingFile /** toggleoverwriteexistingfile */ 
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
