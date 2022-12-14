#ifndef NXOpen_MECHATRONICS_SCOUTEXPORTBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_SCOUTEXPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_SCOUTExportBuilder.ja
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
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class SCOUTExportBuilder;
    }
    class Builder;
    namespace Mechatronics
    {
        class CamProfileBuilder;
    }
    namespace Mechatronics
    {
        class _SCOUTExportBuilderBuilder;
        class SCOUTExportBuilderImpl;
        /** Represents a @link NXOpen::Mechatronics::SCOUTExportBuilder NXOpen::Mechatronics::SCOUTExportBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Mechatronics::PhysicsManager::CreateSCOUTExportBuilder  NXOpen::Mechatronics::PhysicsManager::CreateSCOUTExportBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  SCOUTExportBuilder : public NXOpen::Builder
        {
            /** Represents the export file type. */
            public: enum ExportFileType
            {
                ExportFileTypeCsv/** CSV File */,
                ExportFileTypeXml/** XML File */,
                ExportFileTypeVdi/** VDI File */
            };

            private: SCOUTExportBuilderImpl * m_scoutexportbuilder_impl;
            private: friend class  _SCOUTExportBuilderBuilder;
            protected: SCOUTExportBuilder();
            public: ~SCOUTExportBuilder();
            /**Returns  the export file name 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ExportFile
            (
            );
            /**Sets  the export file name 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetExportFile
            (
                const NXString & exportFile /** exportfile */ 
            );
            /**Sets  the export file name 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void SetExportFile
            (
                const char * exportFile /** exportfile */ 
            );
            /**Returns  the export file format. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::SCOUTExportBuilder::ExportFileType ExportFileFormat
            (
            );
            /**Sets  the export file format. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetExportFileFormat
            (
                NXOpen::Mechatronics::SCOUTExportBuilder::ExportFileType exportFileFormat /** exportfileformat */ 
            );
            /**Write elements to SCOUT 44.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void ExportToScout
            (
                NXOpen::Builder * camProfile /**Cam Profile Builder*/
            );
            /**Write elements to SCOUT with more traverses type.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void ExportToScoutWithFormula
            (
                NXOpen::Mechatronics::CamProfileBuilder * camProfile /**Cam Profile Builder*/
            );
            /**Write elements to Generic XY point.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void ExportToPointXyValue
            (
                NXOpen::Mechatronics::CamProfileBuilder * camProfile /**Cam Profile Builder*/
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
