#ifndef NXOpen_BLOCKSTYLER_DOUBLETABLE_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_DOUBLETABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_DoubleTable.ja
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
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace BlockStyler
    {
        class DoubleTable;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    namespace BlockStyler
    {
        class _DoubleTableBuilder;
        class DoubleTableImpl;
        /** Represents a Double Table block
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENUICPPEXPORT  DoubleTable : public NXOpen::BlockStyler::UIBlock
        {
            private: DoubleTableImpl * m_doubletable_impl;
            private: friend class  _DoubleTableBuilder;
            protected: DoubleTable();
            public: ~DoubleTable();
            /**Returns  the CellWidth
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int CellWidth
            (
            );
            /**Sets  the CellWidth
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetCellWidth
            (
                int cellWidth /** cell width */ 
            );
            /**Returns  the ColumnTitles
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link NXOpen::BlockStyler::DoubleTable::JA_BLOCK_STYLER_DOUBLE_TABLE_get_column_titles NXOpen::BlockStyler::DoubleTable::JA_BLOCK_STYLER_DOUBLE_TABLE_get_column_titles@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use NXOpen::BlockStyler::DoubleTable::JA_BLOCK_STYLER_DOUBLE_TABLE_get_column_titles instead.") NXString ColumnTitles
            (
            );
            /**Sets  the ColumnTitles
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link NXOpen::BlockStyler::DoubleTable::JA_BLOCK_STYLER_DOUBLE_TABLE_set_column_titles NXOpen::BlockStyler::DoubleTable::JA_BLOCK_STYLER_DOUBLE_TABLE_set_column_titles@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1847.0.0.  Use NXOpen::BlockStyler::DoubleTable::JA_BLOCK_STYLER_DOUBLE_TABLE_set_column_titles instead.") void SetColumnTitles
            (
                const NXString & title /** title */ 
            );
            /**Sets  the ColumnTitles
             <br>  @deprecated Deprecated in NX1847.0.0.  Use @link NXOpen::BlockStyler::DoubleTable::JA_BLOCK_STYLER_DOUBLE_TABLE_set_column_titles NXOpen::BlockStyler::DoubleTable::JA_BLOCK_STYLER_DOUBLE_TABLE_set_column_titles@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            void SetColumnTitles
            (
                const char * title /** title */ 
            );
            /** Gets the MaximumValues @return Value to get from the property. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetMaximumValues
            (
                int* nRows /** Number of Rows in the 2D matrix */,
                int* nColumns /** Number of Columns in the 2D matrix */
            );
            /** Sets the MaximumValues
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMaximumValues
            (
                int nRows /** Number of Rows in the 2D matrix */,
                int nColumns /** Number of Columns in the 2D matrix */,
                const std::vector<double> & matrixValue /**Value to set to the property */
            );
            /** Gets the MinimumValues @return Value to get from the property 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetMinimumValues
            (
                int* nRows /** Number of Rows in the 2D matrix */,
                int* nColumns /** Number of Columns in the 2D matrix */
            );
            /** Sets the MinimumValues
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetMinimumValues
            (
                int nRows /** Number of Rows in the 2D matrix */,
                int nColumns /** Number of Columns in the 2D matrix */,
                const std::vector<double> & matrixValue /**Value to set for given property. */
            );
            /** Gets the Values in table @return Value to get from the property. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetValues
            (
                int* nRows /** Number of Rows in the 2D matrix */,
                int* nColumns /** Number of Columns in the 2D matrix */
            );
            /** Sets the Values in table
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetValues
            (
                int nRows /** Number of Rows in the 2D matrix */,
                int nColumns /** Number of Columns in the 2D matrix */,
                const std::vector<double> & matrixValue /**Value to set for the property. */
            );
            /** Gets the titles of rows in table @return Value to get from the property. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetRowTitles
            (
            );
            /** Sets the titles of rows in table
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetRowTitles
            (
                std::vector<NXString> & rowTitle /**Value to set for the property. */
            );
            /**Returns  the Spin
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool Spin
            (
            );
            /**Sets  the Spin
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSpin
            (
                bool spin /** spin */ 
            );
            /**Returns  the WrapSpin. Use this property only when Spin is true
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool WrapSpin
            (
            );
            /**Sets  the WrapSpin. Use this property only when Spin is true
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetWrapSpin
            (
                bool wrapSpin /** wrap spin */ 
            );
            /**Returns  the Increment. Use this property only when Spin is true
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: double Increment
            (
            );
            /**Sets  the Increment. Use this property only when Spin is true
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetIncrement
            (
                double increment /** increment */ 
            );
            /**Returns  the RetainValue. If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool RetainValue
            (
            );
            /**Sets  the RetainValue. If true, indicates that the values in the block would be stored in dialog memory upon OK, Apply or Close. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRetainValue
            (
                bool retain /** retain */ 
            );
            /** Gets the Column Tiltles @return Column Title values to get from the property. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetColumnTitles
            (
            );
            /** Sets the Column Titles
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetColumnTitles
            (
                std::vector<NXString> & columnTitles /**Column Title values to set for the property. */
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
