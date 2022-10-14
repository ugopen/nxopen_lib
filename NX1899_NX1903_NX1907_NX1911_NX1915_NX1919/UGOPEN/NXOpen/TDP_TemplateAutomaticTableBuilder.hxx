#ifndef NXOpen_TDP_TEMPLATEAUTOMATICTABLEBUILDER_HXX_INCLUDED
#define NXOpen_TDP_TEMPLATEAUTOMATICTABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TDP_TemplateAutomaticTableBuilder.ja
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
#include <NXOpen/LineColorFontWidthBuilder.hxx>
#include <NXOpen/TDP_TemplateBaseRectangleBuilder.hxx>
#include <NXOpen/libtdpopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace TDP
    {
        class TemplateAutomaticTableBuilder;
    }
    class LineColorFontWidthBuilder;
    namespace TDP
    {
        class TemplateBaseRectangleBuilder;
    }
    namespace TDP
    {
        class _TemplateAutomaticTableBuilderBuilder;
        class TemplateAutomaticTableBuilderImpl;
        /** Represents a Template Automatic Table Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateAutomaticTableBuilder  NXOpen::TDP::Manager::CreateTemplateAutomaticTableBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class TDPOPENCPPEXPORT  TemplateAutomaticTableBuilder : public NXOpen::TDP::TemplateBaseRectangleBuilder
        {
            /** represents the automatic table contents */
            public: enum ContentType
            {
                ContentTypeBom/** Bill Of Materials Table */,
                ContentTypePmi/** PMI Table */,
                ContentTypeView/** View Table */
            };

            /** represents BOM column types for automatic table editor */
            public: enum JaTdpTemplateAutomaticTableBomColumnType
            {
                JaTdpTemplateAutomaticTableBomColumnTypeIndex/** index */ ,
                JaTdpTemplateAutomaticTableBomColumnTypePartName/** part name */ ,
                JaTdpTemplateAutomaticTableBomColumnTypeQuantity/** quantity */ ,
                JaTdpTemplateAutomaticTableBomColumnTypeAttribute/** attribute */ 
            };

            /** represents PMI column types for automatic table editor */
            public: enum JaTdpTemplateAutomaticTablePmiColumnType
            {
                JaTdpTemplateAutomaticTablePmiColumnTypeIndex/** index */ ,
                JaTdpTemplateAutomaticTablePmiColumnTypePmiName/** pmi name */ ,
                JaTdpTemplateAutomaticTablePmiColumnTypeValue/** value */ ,
                JaTdpTemplateAutomaticTablePmiColumnTypeAttribute/** attribute */ 
            };

            private: TemplateAutomaticTableBuilderImpl * m_templateautomatictablebuilder_impl;
            private: friend class  _TemplateAutomaticTableBuilderBuilder;
            protected: TemplateAutomaticTableBuilder();
            public: ~TemplateAutomaticTableBuilder();
            /**Returns  the content 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplateAutomaticTableBuilder::ContentType Contents
            (
            );
            /**Sets  the content 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetContents
            (
                NXOpen::TDP::TemplateAutomaticTableBuilder::ContentType content /** content */ 
            );
            /**Returns  the show border toggle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowBorder
            (
            );
            /**Sets  the show border toggle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowBorder
            (
                bool showBorder /** showborder */ 
            );
            /**Returns  the color and width 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * ColorWidth
            (
            );
            /** To swap the columns in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool SwapColumns
            (
                int index1 /** location of the first item */,
                int index2 /** location of the second item */,
                int length /** number of rows selected for swapping */
            );
            /** To add the row in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool AddColumn
            (
            );
            /** To delete the row in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool DeleteColumn
            (
                int index /** index of the column to be deleted */
            );
            /** To modify the Bom column type in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdateBomColumn
            (
                int rowIndex /** index of the column to be updated */,
                NXOpen::TDP::TemplateAutomaticTableBuilder::JaTdpTemplateAutomaticTableBomColumnType colType /** column type to be updated */
            );
            /** To modify the Pmi column type in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdatePmiColumn
            (
                int rowIndex /** index of the column to be updated */,
                NXOpen::TDP::TemplateAutomaticTableBuilder::JaTdpTemplateAutomaticTablePmiColumnType colType /** column type to be updated */
            );
            /** To modify the header column in table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdateHeader
            (
                int rowIndex /** index of the column to be updated */,
                const NXString & value /** Value to be updated */
            );
            /** To modify the header column in table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            bool UpdateHeader
            (
                int rowIndex /** index of the column to be updated */,
                const char * value /** Value to be updated */
            );
            /** To modify the Attribute name in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpdateAttribute
            (
                int rowIndex /** index of the column to be updated */,
                const NXString & value /** Value to be updated */
            );
            /** To modify the Attribute name in the table
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            bool UpdateAttribute
            (
                int rowIndex /** index of the column to be updated */,
                const char * value /** Value to be updated */
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