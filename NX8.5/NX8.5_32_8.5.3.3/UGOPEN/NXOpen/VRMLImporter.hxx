#ifndef NXOpen_VRMLIMPORTER_HXX_INCLUDED
#define NXOpen_VRMLIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     VRMLImporter.ja
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
    class VRMLImporter;
    class Importer;
    class _VRMLImporterBuilder;
    class VRMLImporterImpl;
    /** Used to import a VRML file into the work part.
     <br> To obtain an instance of this class use @link ImportManager::CreateVrmlImporter ImportManager::CreateVrmlImporter@endlink .  <br> 
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  VRMLImporter : public Importer
    {
        /** Specifies the angular tolerance. 
         <br>  Created in NX5.0.0.  <br>  
        */
        public: enum AngularToleranceType
        {
            AngularToleranceTypeCoarse/** Import with coarse angular tolerance. */,
            AngularToleranceTypeMedium/** Import with medium angular tolerance. */,
            AngularToleranceTypeFine/** Import with fine angular tolerance. */
        };

        /** Specifies the VRML file units. 
         <br>  Created in NX5.0.0.  <br>  
        */
        public: enum FileUnitsType
        {
            FileUnitsTypeMeters/** VRML file is in units of meters. */,
            FileUnitsTypeMillimeters/** VRML file is in units of millimeters. */,
            FileUnitsTypeInches/** VRML file is in units of inches. */
        };

        private: VRMLImporterImpl * m_vrmlimporter_impl;
        private: friend class  _VRMLImporterBuilder;
        protected: VRMLImporter();
        public: ~VRMLImporter();
        /**Returns  the Hide Smooth Edges flag.  True if the Hide Smooth Edges flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool HideSmoothEdges
        (
        );
        /**Sets  the Hide Smooth Edges flag.  True if the Hide Smooth Edges flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetHideSmoothEdges
        (
            bool hideSmoothEdges /** hide smooth edges */ 
        );
        /**Returns  the angular tolerance.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::VRMLImporter::AngularToleranceType AngularTolerance
        (
        );
        /**Sets  the angular tolerance.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAngularTolerance
        (
            NXOpen::VRMLImporter::AngularToleranceType angularTolerance /** angular tolerance */ 
        );
        /**Returns  the Generate One Model flag.  True if the Generate One Model flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool GenerateOneModel
        (
        );
        /**Sets  the Generate One Model flag.  True if the Generate One Model flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetGenerateOneModel
        (
            bool generateOneModel /** generate one model */ 
        );
        /**Returns  the All Levels of Detail flag.  True if the All Levels of Detail flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool AllLevelsOfDetail
        (
        );
        /**Sets  the All Levels of Detail flag.  True if the All Levels of Detail flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAllLevelsOfDetail
        (
            bool allLevelsOfDetail /** all levels of detail */ 
        );
        /**Returns  the file units.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::VRMLImporter::FileUnitsType FileUnits
        (
        );
        /**Sets  the file units.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetFileUnits
        (
            NXOpen::VRMLImporter::FileUnitsType fileUnits /** file units */ 
        );
        /**Returns  the More Summary Details flag.  True if the More Summary Details flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool MoreSummaryDetails
        (
        );
        /**Sets  the More Summary Details flag.  True if the More Summary Details flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMoreSummaryDetails
        (
            bool moreSummaryDetails /** more summary details */ 
        );
        /**Returns  the Suppress Warning Messages flag.  True if the Suppress Warning Messages flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: bool SuppressWarningMessages
        (
        );
        /**Sets  the Suppress Warning Messages flag.  True if the Suppress Warning Messages flag is on.
            
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSuppressWarningMessages
        (
            bool suppressWarningMessages /** suppress warning messages */ 
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
