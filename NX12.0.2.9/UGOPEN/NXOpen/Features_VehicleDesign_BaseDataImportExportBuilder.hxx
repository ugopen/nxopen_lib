#ifndef NXOpen_FEATURES_VEHICLEDESIGN_BASEDATAIMPORTEXPORTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_BASEDATAIMPORTEXPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_BaseDataImportExportBuilder.ja
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
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace VehicleDesign
        {
            class BaseDataImportExportBuilder;
        }
    }
    class Builder;
    namespace PDM
    {
        class ObjectCreateBuilder;
    }
    namespace Features
    {
        namespace VehicleDesign
        {
            class _BaseDataImportExportBuilderBuilder;
            class BaseDataImportExportBuilderImpl;
            /** Represents a @link NXOpen::Features::VehicleDesign::BaseDataImportExportBuilder NXOpen::Features::VehicleDesign::BaseDataImportExportBuilder@endlink  
                        builder used to import and export expressions from and to a spreadsheet. <br> To create a new instance of this class, use @link NXOpen::Features::VehicleDesignCollection::CreateBaseDataImportExportBuilder  NXOpen::Features::VehicleDesignCollection::CreateBaseDataImportExportBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            ExportOption </td> <td> 
             
            NewItem </td> </tr> 

            <tr><td> 
             
            OperateOption </td> <td> 
             
            Import </td> </tr> 

            <tr><td> 
             
            OverrideExistingExpressions </td> <td> 
             
            0 </td> </tr> 

            </table>  

             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  BaseDataImportExportBuilder : public NXOpen::Builder
            {
                /** This enum represents the import or export operate options*/
                public: enum OperateOptions
                {
                    OperateOptionsImport/** import */ ,
                    OperateOptionsExport/** export */ 
                };

                /** This enum represents the option to indicate if the expressions are to be exported to a new item or an existing item in Teamcenter.*/
                public: enum ExportOptions
                {
                    ExportOptionsNewItem/** new item */ ,
                    ExportOptionsExistingItem/** existing item */ 
                };

                private: BaseDataImportExportBuilderImpl * m_basedataimportexportbuilder_impl;
                private: friend class  _BaseDataImportExportBuilderBuilder;
                protected: BaseDataImportExportBuilder();
                public: ~BaseDataImportExportBuilder();
                /**Returns  the option which indicates if the spreadsheet is to be imported or exported. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::BaseDataImportExportBuilder::OperateOptions OperateOption
                (
                );
                /**Sets  the option which indicates if the spreadsheet is to be imported or exported. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void SetOperateOption
                (
                    NXOpen::Features::VehicleDesign::BaseDataImportExportBuilder::OperateOptions operateOptions /** operateoptions */ 
                );
                /**Returns  the option which indicates if the expressions are to be exported a new create item or an existing item in Teamcenter. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::BaseDataImportExportBuilder::ExportOptions ExportOption
                (
                );
                /**Sets  the option which indicates if the expressions are to be exported a new create item or an existing item in Teamcenter. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void SetExportOption
                (
                    NXOpen::Features::VehicleDesign::BaseDataImportExportBuilder::ExportOptions exportOption /** exportoption */ 
                );
                /**Returns  the value which indicates whether to override existing expressions in the work part when importing. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool OverrideExistingExpressions
                (
                );
                /**Sets  the value which indicates whether to override existing expressions in the work part when importing. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void SetOverrideExistingExpressions
                (
                    bool overrideExistingExpressions /** overrideexistingexpressions */ 
                );
                /**Returns  the name of the Teamcenter dataset from which the spreadsheet is to be imported from or exported to. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString DatasetName
                (
                );
                /**Sets  the name of the Teamcenter dataset from which the spreadsheet is to be imported from or exported to. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void SetDatasetName
                (
                    const NXString & datasetName /** datasetname */ 
                );
                /**Sets  the name of the Teamcenter dataset from which the spreadsheet is to be imported from or exported to. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                void SetDatasetName
                (
                    const char * datasetName /** datasetname */ 
                );
                /**Returns  the spreadsheet name which indicates the spreadsheet to be imported or exported. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString SpreadSheetFileName
                (
                );
                /**Sets  the spreadsheet name which indicates the spreadsheet to be imported or exported. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void SetSpreadSheetFileName
                (
                    const NXString & spreadSheetFileName /** spreadsheetfilename */ 
                );
                /**Sets  the spreadsheet name which indicates the spreadsheet to be imported or exported. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                void SetSpreadSheetFileName
                (
                    const char * spreadSheetFileName /** spreadsheetfilename */ 
                );
                /**Returns  the item ID number which indicates the item that the spreadsheet is to be imported from or exported to. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString SpreadsheetItemID
                (
                );
                /**Sets  the item ID number which indicates the item that the spreadsheet is to be imported from or exported to. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void SetSpreadsheetItemID
                (
                    const NXString & spreadsheetItemID /** spreadsheetitemid */ 
                );
                /**Sets  the item ID number which indicates the item that the spreadsheet is to be imported from or exported to. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                void SetSpreadsheetItemID
                (
                    const char * spreadsheetItemID /** spreadsheetitemid */ 
                );
                /**Returns  the item revision of the spreadsheet that is to be imported from or exported to. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString SpreadsheetItemRevision
                (
                );
                /**Sets  the item revision of the spreadsheet that is to be imported from or exported to. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void SetSpreadsheetItemRevision
                (
                    const NXString & spreadsheetItemRevision /** spreadsheetitemrevision */ 
                );
                /**Sets  the item revision of the spreadsheet that is to be imported from or exported to. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                void SetSpreadsheetItemRevision
                (
                    const char * spreadsheetItemRevision /** spreadsheetitemrevision */ 
                );
                /**Returns  the item name of the spreadsheet in Teamcenter. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString SpreadsheetItemName
                (
                );
                /**Sets  the item name of the spreadsheet in Teamcenter. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void SetSpreadsheetItemName
                (
                    const NXString & spreadsheetItemName /** spreadsheetitemname */ 
                );
                /**Sets  the item name of the spreadsheet in Teamcenter. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                void SetSpreadsheetItemName
                (
                    const char * spreadsheetItemName /** spreadsheetitemname */ 
                );
                /** Used to assign Item number and revision in Teamcenter .
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void AssignItemNumber
                (
                    NXString* itemId /** itemid */ ,
                    NXString* itemName /** itemname */ ,
                    NXString* itemRevision /** itemrevision */ ,
                    bool* idSensitivity /** idsensitivity */ ,
                    bool* revSensitivity /** revsensitivity */ 
                );
                /** Used to assign Item revision in Teamcenter. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void AssignItemRevision
                (
                    const NXString & itemId /** itemid */ ,
                    NXString* itemRevision /** itemrevision */ ,
                    bool* revSensitivity /** revsensitivity */ 
                );
                /** Used to assign Item revision in Teamcenter. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                void AssignItemRevision
                (
                    const char * itemId /** itemid */ ,
                    NXString* itemRevision /** itemrevision */ ,
                    bool* revSensitivity /** revsensitivity */ 
                );
                /** Sets @link NXOpen::PDM::ObjectCreateBuilder NXOpen::PDM::ObjectCreateBuilder@endlink  
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : gateway ("UG GATEWAY") */
                public: void SetObjectCreateBuilder
                (
                    NXOpen::PDM::ObjectCreateBuilder * objectCreateBuilder /** objectcreatebuilder */ 
                );
            };
        }
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
