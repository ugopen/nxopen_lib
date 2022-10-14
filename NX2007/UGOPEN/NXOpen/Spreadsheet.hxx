#ifndef NXOpen_SPREADSHEET_HXX_INCLUDED
#define NXOpen_SPREADSHEET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Spreadsheet.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/SpreadsheetCellData.hxx>
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
    class Spreadsheet;
    class SpreadsheetCellData;
    class SpreadsheetImpl;
    /** Represents a class for internal spreadsheet. 
    To call functions from this class, use @link Spreadsheet Spreadsheet@endlink  object returned by @link NXOpen::SpreadsheetManager::Open  NXOpen::SpreadsheetManager::Open @endlink . 
     <br>  Usable only on Windows <br> 
     <br>  Created in NX11.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  Spreadsheet : public NXOpen::TransientObject
    {
        private: SpreadsheetImpl * m_spreadsheet_impl;
        /// \cond NX_NO_DOC 
        public: explicit Spreadsheet(void *ptr);
        /// \endcond 
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector.  
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~Spreadsheet();
        /** Retrieves a numeric value from a cell. @return  Retrieves a numerical value from a cell
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SpreadsheetCellData * GetNumber
        (
            int row /** Row index of the cell */,
            int col /** Column index of the cell */,
            int sheet /** Sheet index (current worksheet, if zero is specified) */
        );
        /** Retrieves a formula from a cell. @return  Retrieves a formula from a cell. 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SpreadsheetCellData * GetFormula
        (
            int row /** Row index of the cell */,
            int col /** Column index of the cell */,
            int sheet /** Sheet index (current worksheet, if zero is specified) */
        );
        /** Returns the total number of sheets in the spreadsheet  @return  Number of sheets in the spreadsheet 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: int GetNumberOfSheets
        (
        );
        /** Returns the current work sheet number of the spreadsheet.  @return  Current work sheet number of the spreadsheet. 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: int GetSheetNumber
        (
        );
        /** Returns sheet number of the sheet with given name.  @return  Work sheet number of the given spreadsheet name.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: int GetSheetNumberOfName
        (
            const NXString & sheetname /** Sheet name */
        );
        /** Returns sheet number of the sheet with given name.  @return  Work sheet number of the given spreadsheet name.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        int GetSheetNumberOfName
        (
            const char * sheetname /** Sheet name */
        );
        /** Returns the String in the cell  @return  Retrieves a string value from a cell 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SpreadsheetCellData * GetString
        (
            int row /** Row index of the cell */,
            int col /** Column index of the cell */,
            int sheet /** Sheet index of the cell (current worksheet, if zero is specified). */
        );
        /** Returns a number, string or formula depending on the contents of the cell.  @return  The value in a spreadsheet cell as either a string or a number 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SpreadsheetCellData * GetValue
        (
            int row /** Row index of the cell */,
            int col /** Column index of the cell */,
            int sheet /** Sheet index of the cell (current worksheet, if zero is specified). */
        );
        /** Stores a formula into a cell.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetFormula
        (
            int row /** Row index of the cell */,
            int col /** Column index of the cell */,
            NXOpen::SpreadsheetCellData * cellvalue /** cellvalue */ ,
            int sheet /** Sheet index of the cell (current worksheet, if zero is specified). */
        );
        /**  Stores a numeric value in the specified cell of the worksheet.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetNumber
        (
            int row /** Row index of the cell */,
            int col /** Column index of the cell */,
            NXOpen::SpreadsheetCellData * cellvalue /** Numeric value to be set in the cell. */,
            int sheet /** Sheet index (current worksheet, if zero is specified).*/
        );
        /** Sets the worksheet with specified index as current worksheet  
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSheetNumber
        (
            int sheet /** The number to which the current work sheet is to be set. */
        );
        /** Sets the string in the cell. 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetString
        (
            int row /** Row index of the cell.*/,
            int col /** Column index of the cell. */,
            NXOpen::SpreadsheetCellData * cellvalue /** String to be stored in this cell. */,
            int sheet /** Sheet index (current worksheet, if zero is specified).*/
        );
        /** Clears the contents of the current worksheet. 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void Clear
        (
        );
        /** Deletes (clears) one or more rows/columns of data from a worksheet.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void Delete
        (
            int start1 /** From where the deletion should start */,
            int end1 /** Upto where the rows should be deleted */,
            int sheet /** The sheet in which deletion should take place.(Current sheet, if no sheet is specified) */,
            int operation /** 1 for row deletion and 2 for column deletion. */
        );
        /** Deletes specified number of sheets beginning with the specified sheet
            (from the current worksheet, if no sheet is specified).
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void DeleteSheets
        (
            int sheet /** Sheet Number, starting from which sheets are to be deleted. */,
            int count /** Number of sheets to be deleted */
        );
        /** Clears the contents of the specified range 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void EraseRange
        (
            int row0 /** Starting row for range */,
            int col0 /** Starting column for range */,
            int row1 /** Ending row for range */,
            int col1 /** Ending column for range */,
            int sheet0 /** Sheet number for start of the range */,
            int sheet1 /** Sheet number for end of the range */
        );
        /** Returns the evaluated value of a cell. @return  The value in a spreadsheet cell as either a string or a number 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SpreadsheetCellData * EvaluateCell
        (
            int row /** Row index of the cell */,
            int col /** Column index of the cell */,
            int sheet /** Sheet index (current worksheet, if zero is specified).*/
        );
        /** Inserts specified number of sheets before the specified sheet (or the 
            current work sheet if no sheet is specified).
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void InsertSheets
        (
            int sheet /** Sheet number, before which the sheets are to be inserted. */,
            int count /** Number of sheets to be inserted.*/
        );
        /** Terminates excel sheet for opened part.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void Terminate
        (
        );
        /** Saves the spreadsheet in the part file.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void Save
        (
        );
        /** Recalculates the spreadsheet.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void Recalculate
        (
        );
        /** Returns list of existing sheet names in the spreadsheet. 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void GetSheetNames
        (
            std::vector<NXString> & sheetnames /** List of sheet names from specified spreadsheet */
        );
        /** Resolves the named reference and returns the range of cells that are named
             This method returns a list, of the following format:
               Start Row,
               Start Column,
               End Row,
               End Column,
               Start Sheet Number,
               End Sheet Number
            of the named reference.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void GetNamedRange
        (
            const NXString & rangename /** Range name */,
            std::vector<int> & namedrange /** The range of cells for given range name */
        );
        /** Resolves the named reference and returns the range of cells that are named
             This method returns a list, of the following format:
               Start Row,
               Start Column,
               End Row,
               End Column,
               Start Sheet Number,
               End Sheet Number
            of the named reference.
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        void GetNamedRange
        (
            const char * rangename /** Range name */,
            std::vector<int> & namedrange /** The range of cells for given range name */
        );
        /** Defines a name for the Range of cells. 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        public: void SetNamedRange
        (
            const NXString & rangename /** Name to be given to the range */,
            int row0 /** Starting row of the table, which is being named */,
            int col0 /** Starting column of the table, which is being named */,
            int row1 /** Row of the table, upto which the name will apply */,
            int col1 /** Column of the table, upto which the name will apply */,
            int sheet /** Sheet index of the table (current worksheet, if zero is specified).*/
        );
        /** Defines a name for the Range of cells. 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX11.0.0.  <br>  
         <br> License requirements : None */
        void SetNamedRange
        (
            const char * rangename /** Name to be given to the range */,
            int row0 /** Starting row of the table, which is being named */,
            int col0 /** Starting column of the table, which is being named */,
            int row1 /** Row of the table, upto which the name will apply */,
            int col1 /** Column of the table, upto which the name will apply */,
            int sheet /** Sheet index of the table (current worksheet, if zero is specified).*/
        );
    }; //lint !e1712 default constructor not defined for class  

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