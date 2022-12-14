#ifndef NXOpen_FIELDS_FIELDLINKSTABLE_HXX_INCLUDED
#define NXOpen_FIELDS_FIELDLINKSTABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_FieldLinksTable.ja
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
#include <NXOpen/Fields_Field.hxx>
#include <NXOpen/Fields_FieldEvaluator.hxx>
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
        class FieldLinksTable;
    }
    namespace Fields
    {
        class Field;
    }
    namespace Fields
    {
        class FieldVariable;
    }
    namespace Fields
    {
        class _FieldLinksTableBuilder;
        class FieldLinksTableImpl;
        /**  @brief  Represents the Field LinksTable class. 

          
             <br> A field (see @link Fields::Field Fields::Field@endlink ) defined in terms of tabular data involving 
            one look-up independent column, an equal number of look-up fields and one or more 
            dependent variables (see @link Fields::FieldVariable Fields::FieldVariable@endlink ).  This is similar to a table
            (see @link Fields::FieldTable Fields::FieldTable@endlink ), except instead of the interpolation dependent 
            values being defined as numerical contants, they are defined by another field. <br>   <br> To obtain a instance of this class use @link Fields::FieldManager Fields::FieldManager@endlink  .  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_FIELDSEXPORT  FieldLinksTable : public Fields::Field
        {
            private: FieldLinksTableImpl * m_fieldlinkstable_impl;
            private: friend class  _FieldLinksTableBuilder;
            protected: FieldLinksTable();
            public: ~FieldLinksTable();
            /** Edit the LinksTable field.  Specifies the new array of @link Fields::FieldVariable Fields::FieldVariable@endlink s 
                    for independent and dependent variables, as well as the new double values and linked fields.
                    The datapoints and linked fields arrays are row based and number of each must equal the 
                    num_rows. The data_points array represents the values for the first independent value.  For example, if 
                    the LinksTable has a domain of txyz, the values in this array are all values of t.
                    The linked fields array must consist of the fields with independent variables representing the 
                    remaining variables in the independent domain of the LinksTable.  For example, if the LinksTable has 
                    a domain of txyz, the independent domain of the fields in this array are all xyz.  NULL values are  allowed for 
                    linked fields and indicate a discontinuity at the associated value of the first independent  variable.
                    The dependent quantities are determined from the linked fields.  The linked fields must have the same 
                    dependent variables as the Linkstable.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void EditFieldLinksTable
            (
                const std::vector<NXOpen::Fields::FieldVariable *> & indepVarArray /** independent variables to be associated with the field */,
                const std::vector<NXOpen::Fields::FieldVariable *> & depVarArray /** dependent variables of this and all linked fields */,
                const std::vector<double> & datapoints /** row based array of double values representing the first independent variable; the number of points should equal the number of rows. */,
                const std::vector<NXOpen::Fields::Field *> & linkFieldsArray /** row based array of link field values representing the table; the number of fields should equal the number of rows.*/
            );
            /**Returns  a flag specifying if the table has discontinuites 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool Discontinuities
            (
            );
            /**Returns  the outside table values interpolation method for linear interpolation 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Fields::FieldEvaluator::ValuesOutsideTableInterpolationEnum ValuesOutsideTableInterpolation
            (
            );
            /**Sets  the outside table values interpolation method for linear interpolation 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetValuesOutsideTableInterpolation
            (
                NXOpen::Fields::FieldEvaluator::ValuesOutsideTableInterpolationEnum interpolationMethod /** the outside table values interpolation method */
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
