#ifndef NXOpen_ACISIMPORTER_HXX_INCLUDED
#define NXOpen_ACISIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AcisImporter.ja
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
    class AcisImporter;
    class Builder;
    class _AcisImporterBuilder;
    class AcisImporterImpl;
    /**
        Represents a @link AcisImporter AcisImporter@endlink  to be used when importing the Acis Data
        This class is created using @link DexManager DexManager@endlink .
        NULL object will be returned from Commit()  <br> To create a new instance of this class, use @link NXOpen::DexManager::CreateAcisImporter  NXOpen::DexManager::CreateAcisImporter @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    HealBodies </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    IncludeWires </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    Optimize </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    Sew </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    SimplifyGeometry </td> <td> 
     
    0 </td> </tr> 

    </table>  

     <br>  Created in NX11.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  AcisImporter : public NXOpen::Builder
    {
        private: AcisImporterImpl * m_acisimporter_impl;
        private: friend class  _AcisImporterBuilder;
        protected: AcisImporter();
        public: ~AcisImporter();
        /** Save the settings - this will save the settings to a file specified 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SaveSettings
        (
            const NXString & filename /** filename */ 
        );
        /** Save the settings - this will save the settings to a file specified 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        void SaveSettings
        (
            const char * filename /** filename */ 
        );
        /**Returns  the input file -  name of a file which is being imported 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXString InputFile
        (
        );
        /**Sets  the input file -  name of a file which is being imported 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetInputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  the input file -  name of a file which is being imported 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        void SetInputFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the settings file - definition file for default options
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXString SettingsFile
        (
        );
        /**Sets  the settings file - definition file for default options
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSettingsFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  the settings file - definition file for default options
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        void SetSettingsFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the heal bodies - if set to true then imported data will be healed 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool HealBodies
        (
        );
        /**Sets  the heal bodies - if set to true then imported data will be healed 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetHealBodies
        (
            bool healBodies /** healbodies */ 
        );
        /**Returns  the simplify geometry - if value set to true then imported data will be simplified 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool SimplifyGeometry
        (
        );
        /**Sets  the simplify geometry - if value set to true then imported data will be simplified 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSimplifyGeometry
        (
            bool simplifyGeometry /** simplifygeometry */ 
        );
        /**Returns  the Optimize - if value set to true then redundant geometries will be removed 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool Optimize
        (
        );
        /**Sets  the Optimize - if value set to true then redundant geometries will be removed 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOptimize
        (
            bool optimize /** optimize */ 
        );
        /**Returns  the IncludeWires - if value set to true then wireframes and points will be imported
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool IncludeWires
        (
        );
        /**Sets  the IncludeWires - if value set to true then wireframes and points will be imported
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetIncludeWires
        (
            bool includeWires /** includewires */ 
        );
        /**Returns  the Sew - if value set to true then automatic sewing will be done 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool Sew
        (
        );
        /**Sets  the Sew - if value set to true then automatic sewing will be done 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSew
        (
            bool sew /** sew */ 
        );
        /**Returns  the file open flag - set this to false if doing file import
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: bool FileOpenFlag
        (
        );
        /**Sets  the file open flag - set this to false if doing file import
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetFileOpenFlag
        (
            bool doingFileOpen /** doingfileopen */ 
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