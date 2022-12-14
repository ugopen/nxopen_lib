#ifndef NXOpen_CREOIMPORTER_HXX_INCLUDED
#define NXOpen_CREOIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CreoImporter.ja
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
#include <NXOpen/BaseImporter.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class CreoImporter;
    class BaseImporter;
    class _CreoImporterBuilder;
    class CreoImporterImpl;
    /**
        Represents a @link NXOpen::CreoImporter NXOpen::CreoImporter@endlink  to be used when importing the Creo Data
        This class is created using @link NXOpen::DexManager NXOpen::DexManager@endlink .
        NULL object will be returned from Commit()  <br> To create a new instance of this class, use @link NXOpen::DexManager::CreateCreoImporter  NXOpen::DexManager::CreateCreoImporter @endlink  <br> 
    Default values.
    <list type="table"> 
     
    <listheader><term> 
    Property</term>  <description> 
    Value</description> </listheader>
    <item><term> 
     
    HealBodies </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    ImportTo </term> <description> 
     
    WorkPart </description> </item> 

    <item><term> 
     
    ImportToTeamcenter </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    IncludeNonManifoldObj </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    Optimize </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    SimplifyGeometry </term> <description> 
     
    0 </description> </item> 

    </list> 

     <br>  Created in NX1953.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  CreoImporter : public NXOpen::BaseImporter
    {
        /** Import To Option */
        public: enum ImportToOption
        {
            ImportToOptionWorkPart/** import creo file to work part */,
            ImportToOptionNewPart/** import creo file to new part */
        };

        private: CreoImporterImpl * m_creoimporter_impl;
        private: friend class  _CreoImporterBuilder;
        protected: CreoImporter();
        public: ~CreoImporter();
        /** Save the settings - this will save the settings to a file specified 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void SaveSettings
        (
            const NXString & filename /** filename */ 
        );
        /** Save the settings - this will save the settings to a file specified 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        void SaveSettings
        (
            const char * filename /** filename */ 
        );
        /**Returns  the settings file - definition file for default options
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: NXString SettingsFile
        (
        );
        /**Sets  the settings file - definition file for default options
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSettingsFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  the settings file - definition file for default options
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        void SetSettingsFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the heal bodies - if set to true then imported data will be healed 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: bool HealBodies
        (
        );
        /**Sets  the heal bodies - if set to true then imported data will be healed 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void SetHealBodies
        (
            bool healBodies /** healbodies */ 
        );
        /**Returns  the simplify geometry - if value set to true then imported data will be simplified 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: bool SimplifyGeometry
        (
        );
        /**Sets  the simplify geometry - if value set to true then imported data will be simplified 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSimplifyGeometry
        (
            bool simplifyGeometry /** simplifygeometry */ 
        );
        /**Returns  the Optimize - if value set to true then redundant geometries will be removed 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: bool Optimize
        (
        );
        /**Sets  the Optimize - if value set to true then redundant geometries will be removed 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOptimize
        (
            bool optimize /** optimize */ 
        );
        /**Returns  the include non manifold obj - if set to true then non-manifold objects from Creo will also 
                    be imported 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: bool IncludeNonManifoldObj
        (
        );
        /**Sets  the include non manifold obj - if set to true then non-manifold objects from Creo will also 
                    be imported 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void SetIncludeNonManifoldObj
        (
            bool includeNonManifoldObj /** includenonmanifoldobj */ 
        );
        /**Returns  the import to. This option will determine the destination for imported Creo file. It can
                    either be new part or work part. 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::CreoImporter::ImportToOption ImportTo
        (
        );
        /**Sets  the import to. This option will determine the destination for imported Creo file. It can
                    either be new part or work part. 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void SetImportTo
        (
            NXOpen::CreoImporter::ImportToOption importTo /** importto */ 
        );
        /**Returns  the import to Teamcenter  - if set to true then imported data can be added to Teamcenter
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: bool ImportToTeamcenter
        (
        );
        /**Sets  the import to Teamcenter  - if set to true then imported data can be added to Teamcenter
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void SetImportToTeamcenter
        (
            bool importToTeamcenter /** importtoteamcenter */ 
        );
    };
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
