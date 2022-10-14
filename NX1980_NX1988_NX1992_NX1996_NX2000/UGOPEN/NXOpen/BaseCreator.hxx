#ifndef NXOpen_BASECREATOR_HXX_INCLUDED
#define NXOpen_BASECREATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BaseCreator.ja
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
#include <NXOpen/DexBuilder.hxx>
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
    class BaseCreator;
    class DexBuilder;
    class _BaseCreatorBuilder;
    class BaseCreatorImpl;
    /**
    This is an abstract class that provides the basic functionality common to all dex export builders.
    See the Export Builder subclasses for details of application-specific builders.
     <br> Creator not available in KF  <br> 
     <br>  Created in NX1872.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  BaseCreator : public NXOpen::DexBuilder
    {
        /** Export to destinationoptions */
        public: enum ExportDestinationOption
        {
            ExportDestinationOptionNativeFileSystem/**  export to native filesystem */,
            ExportDestinationOptionTeamcenter/**  export to teamcenter */
        };

        private: BaseCreatorImpl * m_basecreator_impl;
        private: friend class  _BaseCreatorBuilder;
        protected: BaseCreator();
        public: ~BaseCreator();
        /**Returns  the output file - filepath for output file
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: NXString OutputFile
        (
        );
        /**Sets  the output file - filepath for output file
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  the output file - filepath for output file
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        void SetOutputFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the dataset name - Name of dataset being created
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: NXString DatasetName
        (
        );
        /**Sets  the dataset name - Name of dataset being created
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetDatasetName
        (
            const NXString & datasetName /** datasetname */ 
        );
        /**Sets  the dataset name - Name of dataset being created
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        void SetDatasetName
        (
            const char * datasetName /** datasetname */ 
        );
        /**Returns  the output file extension - Extension of output file being created
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: NXString OutputFileExtension
        (
        );
        /**Sets  the output file extension - Extension of output file being created
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputFileExtension
        (
            const NXString & outputFileExtension /** outputfileextension */ 
        );
        /**Sets  the output file extension - Extension of output file being created
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        void SetOutputFileExtension
        (
            const char * outputFileExtension /** outputfileextension */ 
        );
        /**Returns  the export to - determines whether exporting to Teamcenter or Native file system
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::BaseCreator::ExportDestinationOption ExportDestination
        (
        );
        /**Sets  the export to - determines whether exporting to Teamcenter or Native file system
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetExportDestination
        (
            NXOpen::BaseCreator::ExportDestinationOption exportFrom /** exportfrom */ 
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