#ifndef NXOpen_AME_IMPORTHWXMLBUILDER_HXX_INCLUDED
#define NXOpen_AME_IMPORTHWXMLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ImportHWXmlBuilder.ja
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
#include <NXOpen/AME_AMEBaseNode.hxx>
#include <NXOpen/AME_SelectionBaseDefinitionBuilder.hxx>
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
        class ImportHWXmlBuilder;
    }
    namespace AME
    {
        class AMEBaseNode;
    }
    namespace AME
    {
        class SelectAMEBaseNode;
    }
    namespace AME
    {
        class SelectionBaseDefinitionBuilder;
    }
    class Builder;
    namespace AME
    {
        class _ImportHWXmlBuilderBuilder;
        class ImportHWXmlBuilderImpl;
        /** the Import HW Xml builder  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateImportHwxmlBuilder  NXOpen::AME::AMEManager::CreateImportHwxmlBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ImportHWXmlBuilder : public NXOpen::Builder
        {
            private: ImportHWXmlBuilderImpl * m_importhwxmlbuilder_impl;
            private: friend class  _ImportHWXmlBuilderBuilder;
            protected: ImportHWXmlBuilder();
            public: ~ImportHWXmlBuilder();
            /**Returns  the selected engineering object 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAMEBaseNode * SelectionTarget
            (
            );
            /**Returns  the currently selected TIA project item name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString CurrentlySelectedTiaProjectName
            (
            );
            /**Sets  the currently selected TIA project item name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCurrentlySelectedTiaProjectName
            (
                const NXString & projectName /** projectname */ 
            );
            /**Sets  the currently selected TIA project item name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetCurrentlySelectedTiaProjectName
            (
                const char * projectName /** projectname */ 
            );
            /**Returns  the currently selected TIA project item path 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString CurrentlySelectedTiaProjectPath
            (
            );
            /**Sets  the currently selected TIA project item path 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCurrentlySelectedTiaProjectPath
            (
                const NXString & projectPath /** projectpath */ 
            );
            /**Sets  the currently selected TIA project item path 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetCurrentlySelectedTiaProjectPath
            (
                const char * projectPath /** projectpath */ 
            );
            /**Returns  the currently selected TIA station item name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString CurrentlySelectedStationItemName
            (
            );
            /**Sets  the currently selected TIA station item name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCurrentlySelectedStationItemName
            (
                const NXString & stationName /** stationname */ 
            );
            /**Sets  the currently selected TIA station item name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetCurrentlySelectedStationItemName
            (
                const char * stationName /** stationname */ 
            );
            /**Returns  the currently selected TIA software block item name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString CurrentlySelectedSWBlockItemName
            (
            );
            /**Sets  the currently selected TIA software block item name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCurrentlySelectedSWBlockItemName
            (
                const NXString & swBlockName /** swblockname */ 
            );
            /**Sets  the currently selected TIA software block item name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetCurrentlySelectedSWBlockItemName
            (
                const char * swBlockName /** swblockname */ 
            );
            /** Set project xml 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetProjectXml
            (
                const std::vector<NXString> & projectXmlParts /** projectxmlparts */ 
            );
            /** Import station 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::AMEBaseNode * ImportStation
            (
                const NXString & stationId /** stationid */ 
            );
            /** Import station 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            NXOpen::AME::AMEBaseNode * ImportStation
            (
                const char * stationId /** stationid */ 
            );
            /** Import Tia project with option get station list 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void GetStationList
            (
            );
            /** Import Tia project with option get station preview 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void GetStationPreview
            (
                const NXString & stationName /** stationname */ 
            );
            /** Import Tia project with option get station preview 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void GetStationPreview
            (
                const char * stationName /** stationname */ 
            );
            /** Import plc station 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: std::vector<NXOpen::AME::AMEBaseNode *> ImportPlcStations
            (
                const std::vector<NXString> & stationNames /** stationnames */ 
            );
            /** Import sw blocks 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ImportSwBlocks
            (
                const std::vector<NXString> & swBlockIds /** swblockids */ ,
                bool isOnline /** isonline */ 
            );
            /**Returns  the engineering object definition or product definition
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectionBaseDefinitionBuilder * SelectLibraryObject
            (
            );
            /** Get library preview 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void GetLibraryPreview
            (
            );
            /** Import master copy from hardware library 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ImportHwLibraryMasterCopies
            (
                const std::vector<NXString> & masterCopyIds /** mastercopyids */ 
            );
            /** Import sw blocks and UDTs from TIA library 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ImportSwLibraryTypes
            (
                const std::vector<NXString> & swTypeIds /** swtypeids */ 
            );
            /**Returns  the currently selected TIA library item name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString CurrentlySelectedTiaLibraryName
            (
            );
            /**Sets  the currently selected TIA library item name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCurrentlySelectedTiaLibraryName
            (
                const NXString & libraryName /** libraryname */ 
            );
            /**Sets  the currently selected TIA library item name 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetCurrentlySelectedTiaLibraryName
            (
                const char * libraryName /** libraryname */ 
            );
            /**Returns  the currently selected TIA library item path 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString CurrentlySelectedTiaLibraryPath
            (
            );
            /**Sets  the currently selected TIA library item path 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCurrentlySelectedTiaLibraryPath
            (
                const NXString & libraryPath /** librarypath */ 
            );
            /**Sets  the currently selected TIA library item path 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetCurrentlySelectedTiaLibraryPath
            (
                const char * libraryPath /** librarypath */ 
            );
            /** The Tia Portal Version 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetTiaPortalVersion
            (
                const NXString & tiaPortalVersion /** tiaportalversion */ 
            );
            /** The Tia Portal Version 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetTiaPortalVersion
            (
                const char * tiaPortalVersion /** tiaportalversion */ 
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
