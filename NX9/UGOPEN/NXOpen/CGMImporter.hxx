#ifndef NXOpen_CGMIMPORTER_HXX_INCLUDED
#define NXOpen_CGMIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CGMImporter.ja
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
#include <NXOpen/Importer.hxx>
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
    class CGMImporter;
    class Importer;
    class _CGMImporterBuilder;
    class CGMImporterImpl;
    /** Used to import a CGM file into the work part.
     <br> To obtain an instance of this class use @link ImportManager::CreateCgmImporter ImportManager::CreateCgmImporter@endlink .  <br> 
     <br>  Created in NX7.5.0.  <br>  
    */
    class NXOPENCPPEXPORT  CGMImporter : public Importer
    {
        private: CGMImporterImpl * m_cgmimporter_impl;
        private: friend class  _CGMImporterBuilder;
        protected: CGMImporter();
        public: ~CGMImporter();
        /**Returns  the crosshatching flag, true if crosshatching should be done
            
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: bool Crosshatching
        (
        );
        /**Sets  the crosshatching flag, true if crosshatching should be done
            
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void SetCrosshatching
        (
            bool crosshatching /** crosshatching */ 
        );
        /**Returns  
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: bool UseExportSessionWidths
        (
        );
        /**Sets  
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void SetUseExportSessionWidths
        (
            bool useCgmExportSessionWidths /** use cgm export session widths */ 
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