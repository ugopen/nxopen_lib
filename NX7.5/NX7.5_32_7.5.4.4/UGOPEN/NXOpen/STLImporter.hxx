#ifndef NXOpen_STLIMPORTER_HXX_INCLUDED
#define NXOpen_STLIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     STLImporter.ja
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
namespace NXOpen
{
    class STLImporter;
    class Importer;
    class _STLImporterBuilder;
    class STLImporterImpl;
    /** Used to import an STL file into the work part.
     <br>  <br> */
    class NXOPENCPPEXPORT  STLImporter : public Importer
    {
        /** Specifies the angular tolerance. */
        public: enum AngularToleranceType
        {
            AngularToleranceTypeCoarse/** Import with coarse angular tolerance. */,
            AngularToleranceTypeMedium/** Import with medium angular tolerance. */,
            AngularToleranceTypeFine/** Import with fine angular tolerance. */
        };

        /** Specifies the STL file units. */
        public: enum FileUnitsType
        {
            FileUnitsTypeMeters/** STL file is in units of meters. */,
            FileUnitsTypeMillimeters/** STL file is in units of millimeters. */,
            FileUnitsTypeInches/** STL file is in units of inches. */
        };

        /** Specifies the STL file format. */
        public: enum FileFormatType
        {
            FileFormatTypeAscii/** STL file is in ASCII format. */,
            FileFormatTypeBinary/** STL file is in binary format. */
        };

        private: STLImporterImpl * m_stlimporter_impl;
        private: friend class  _STLImporterBuilder;
        protected: STLImporter();
        public: ~STLImporter();
        /**Returns  the Hide Smooth Edges flag.  True if the Hide Smooth Edges flag is on.
             <br> License requirements : None */
        public: bool HideSmoothEdges
        (
        );
        /**Sets  the Hide Smooth Edges flag.  True if the Hide Smooth Edges flag is on.
             <br> License requirements : None */
        public: void SetHideSmoothEdges
        (
            bool hideSmoothEdges /** hide smooth edges */ 
        );
        /**Returns  the angular tolerance.
             <br> License requirements : None */
        public: NXOpen::STLImporter::AngularToleranceType AngularTolerance
        (
        );
        /**Sets  the angular tolerance.
             <br> License requirements : None */
        public: void SetAngularTolerance
        (
            NXOpen::STLImporter::AngularToleranceType angularTolerance /** angular tolerance */ 
        );
        /**Returns  the file units.
             <br> License requirements : None */
        public: NXOpen::STLImporter::FileUnitsType FileUnits
        (
        );
        /**Sets  the file units.
             <br> License requirements : None */
        public: void SetFileUnits
        (
            NXOpen::STLImporter::FileUnitsType fileUnits /** file units */ 
        );
        /**Returns  the Display Information flag.  True if the Display Information flag is on.
             <br> License requirements : None */
        public: bool DisplayInformation
        (
        );
        /**Sets  the Display Information flag.  True if the Display Information flag is on.
             <br> License requirements : None */
        public: void SetDisplayInformation
        (
            bool displayInformation /** display information */ 
        );
        /**Returns  the file format.
             <br> License requirements : None */
        public: NXOpen::STLImporter::FileFormatType FileFormat
        (
        );
        /**Sets  the file format.
             <br> License requirements : None */
        public: void SetFileFormat
        (
            NXOpen::STLImporter::FileFormatType fileFormat /** file format */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif