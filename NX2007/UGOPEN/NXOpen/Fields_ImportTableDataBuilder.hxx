#ifndef NXOpen_FIELDS_IMPORTTABLEDATABUILDER_HXX_INCLUDED
#define NXOpen_FIELDS_IMPORTTABLEDATABUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_ImportTableDataBuilder.ja
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
#include <NXOpen/Fields_FieldTable.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_fields_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Fields
    {
        class ImportTableDataBuilder;
    }
    class Builder;
    namespace Fields
    {
        class _ImportTableDataBuilderBuilder;
        class ImportTableDataBuilderImpl;
        /** Represents a @link NXOpen::Fields::ImportTableDataBuilder NXOpen::Fields::ImportTableDataBuilder@endlink  builder 
            which can be used to import data for @link NXOpen::Fields::FieldTable NXOpen::Fields::FieldTable@endlink   <br> To create a new instance of this class, use @link NXOpen::Fields::FieldManager::CreateImportTableDataBuilderFromTable  NXOpen::Fields::FieldManager::CreateImportTableDataBuilderFromTable @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_FIELDSEXPORT  ImportTableDataBuilder : public NXOpen::Builder
        {
            private: ImportTableDataBuilderImpl * m_importtabledatabuilder_impl;
            private: friend class  _ImportTableDataBuilderBuilder;
            protected: ImportTableDataBuilder();
            public: ~ImportTableDataBuilder();
            /**Returns  the import data file 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ImportFile
            (
            );
            /**Sets  the import data file 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetImportFile
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the import data file 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            void SetImportFile
            (
                const char * filename /** filename */ 
            );
            /**Returns  the is structured data value 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsStructDataFormat
            (
            );
            /**Sets  the is structured data value 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStructDataFormat
            (
                bool structuredDataFormat /** structured data format */ 
            );
            /**Returns  the create spatial map value 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateSpatialMap
            (
            );
            /**Sets  the create spatial map value 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCreateSpatialMap
            (
                bool createSpatialMap /** createspatialmap */ 
            );
            /**Returns  the duplicate value option 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Fields::FieldTable::DuplicateValueOption DuplicateValues
            (
            );
            /**Sets  the duplicate value option 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDuplicateValues
            (
                NXOpen::Fields::FieldTable::DuplicateValueOption duplicateValueOption /** duplicate value option */ 
            );
            /**Returns  the number of structured data rows 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: int NumStructDataRows
            (
            );
            /**Sets  the number of structured data rows 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNumStructDataRows
            (
                int numRows /** numrows */ 
            );
            /**Returns  the number of structured data columns 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: int NumStructDataColumns
            (
            );
            /**Sets  the number of structured data columns 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNumStructDataColumns
            (
                int numColumns /** numcolumns */ 
            );
            /**Sets  the number of structured data planes 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNumStructDataPlanes
            (
                int numPlanes /** num planes */ 
            );
            /**Returns  the number of structured data planes 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: int NumStructDataPlanes
            (
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void RescanImportFile
            (
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetClearTableOnImport
            (
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