#ifndef NXOpen_GENERALSCALARTABLE_HXX_INCLUDED
#define NXOpen_GENERALSCALARTABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeneralScalarTable.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class GeneralScalarTable;
    class Unit;
    /**  @brief  Represents a General M x N table of scalar (real) values.   

       <br> This is an abstract class <br> */
    class NXOPENCPPEXPORT GeneralScalarTable : public TransientObject
    {
        public: explicit GeneralScalarTable(void *ptr);
        /** Returns the table size  <br> License requirements : None */
        public: void SetTableSize
        (
            int nRows /** Number of Rows */,
            int nCols /** Number of Columns */,
            double dDefaultValue /** Default Value */
        );
        /**Returns  the number of rows  <br> License requirements : None */
        public: int NumRows
        (
        );
        /**Returns  the numuber of columns <br> License requirements : None */
        public: int NumCols
        (
        );
        /** Returns the cell value  @return   <br> License requirements : None */
        public: double GetCellValue
        (
            int iRow /** Row Index       */,
            int iCol /** Column Index    */
        );
        /** Sets cell value  <br> License requirements : None */
        public: void SetCellValue
        (
            int iRow /** Row Index                    */,
            int iCol /** Column Index                 */,
            double cellValue /** Value to store in the cell   */
        );
        /** Sets the entire Nth row of values. Input array must be as long as
                the number of columns @link GeneralScalarTable::NumCols GeneralScalarTable::NumCols@endlink       <br> License requirements : None */
        public: void SetNthRow
        (
            int iRow /** Row Index   */,
            const std::vector<double> & rowValues /** Row Values */
        );
        /** Returns the entire Nth row of values. Output array will be as long as 
                the number of columns @link GeneralScalarTable::NumCols GeneralScalarTable::NumCols@endlink       @return  Row Values   <br> License requirements : None */
        public: std::vector<double> GetNthRow
        (
            int iRow /** Row Index   */
        );
        /** Sets the entire Nth column of values. Input array must be as long as 
                the number of rows @link GeneralScalarTable::NumRows GeneralScalarTable::NumRows@endlink        <br> License requirements : None */
        public: void SetNthColumn
        (
            int iCol /** Column Index    */,
            const std::vector<double> & columnValues /** Column values   */
        );
        /** Returns the entire Nth column of values. Output array will be as long as 
                the number of rows @link GeneralScalarTable::NumRows GeneralScalarTable::NumRows@endlink         @return  Column Values    <br> License requirements : None */
        public: std::vector<double> GetNthColumn
        (
            int iCol /** Column Index    */
        );
        /** Sets the entire Nth column of values. Input array must be as long as
                the number of rows  @link GeneralScalarTable::NumRows GeneralScalarTable::NumRows@endlink       <br> License requirements : None */
        public: void SetNthColumnUnits
        (
            int iCol /** Column Index */,
            NXOpen::Unit * unitType /** Unit type for the column */
        );
        /** Returns the entire Nth column of values. Output array will be as long as
                the number of rows  @link GeneralScalarTable::NumRows GeneralScalarTable::NumRows@endlink       @return  Unit type for the column NULL if the Column has no units  <br> License requirements : None */
        public: NXOpen::Unit * GetNthColumnUnits
        (
            int iCol /** Column Index*/
        );
        /** Destroys the object  <br> License requirements : None */
        public: virtual ~GeneralScalarTable();
    };
}
#undef EXPORTLIBRARY
#endif
