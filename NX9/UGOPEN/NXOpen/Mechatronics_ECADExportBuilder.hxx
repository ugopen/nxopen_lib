#ifndef NXOpen_MECHATRONICS_ECADEXPORTBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_ECADEXPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_ECADExportBuilder.ja
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
#include <NXOpen/Mechatronics_ECADExportBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class ECADExportBuilder;
    }
    class Builder;
    namespace Mechatronics
    {
        class SelectLogicObjectList;
    }
    namespace Mechatronics
    {
        class _ECADExportBuilderBuilder;
        class ECADExportBuilderImpl;
        /** Represents a @link Mechatronics::ECADExportBuilder Mechatronics::ECADExportBuilder@endlink   <br> To create a new instance of this class, use @link Mechatronics::PhysicsManager::CreateECADExportBuilder  Mechatronics::PhysicsManager::CreateECADExportBuilder @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  ECADExportBuilder : public Builder
        {
            /** Represents the export file type. 
             <br>  @deprecated Deprecated in NX9.0.0.  This enum type has no replacement. It is no longer supported. <br>  
            */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  This enum type has no replacement. It is no longer supported.") enum ExportFileType
            {
                ExportFileTypeXml/** XML File */,
                ExportFileTypeCsv/** CSV File */,
                ExportFileTypeEplan/** EPLAN File */
            };

            private: ECADExportBuilderImpl * m_ecadexportbuilder_impl;
            private: friend class  _ECADExportBuilderBuilder;
            protected: ECADExportBuilder();
            public: ~ECADExportBuilder();
            /**Returns  the export file name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString ExportFile
            (
            );
            /**Sets  the export file name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetExportFile
            (
                const NXString & exportFile /** The export file name */
            );
            /**Sets  the export file name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void SetExportFile
            (
                const char * exportFile /** The export file name */
            );
            /**Returns  the selected logical objects. This can be a @link LogicObject LogicObject@endlink . 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Mechatronics::SelectLogicObjectList * SelectLogicals
            (
            );
            /** Gets the exported attributes name  @return  Exported attributes name 
             <br>  @deprecated Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported.") std::vector<NXString> GetExportAttributesName
            (
            );
            /** Sets the exported attributes name 
             <br>  @deprecated Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported.") void SetExportAttributesName
            (
                std::vector<NXString> & exportAttributesName /** Exported attributes name */
            );
            /**Returns  the export file format. 
             <br>  @deprecated Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported.") NXOpen::Mechatronics::ECADExportBuilder::ExportFileType ExportFileFormat
            (
            );
            /**Sets  the export file format. 
             <br>  @deprecated Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public:  NX_DEPRECATED("Deprecated in NX9.0.0.  This method has no replacement. It is no longer supported.") void SetExportFileFormat
            (
                NXOpen::Mechatronics::ECADExportBuilder::ExportFileType exportFileFormat /** exportfileformat */ 
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