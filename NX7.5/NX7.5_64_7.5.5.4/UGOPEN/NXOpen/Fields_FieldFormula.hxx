#ifndef NXOpen_FIELDS_FIELDFORMULA_HXX_INCLUDED
#define NXOpen_FIELDS_FIELDFORMULA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_FieldFormula.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Fields
    {
        class FieldFormula;
    }
    namespace Fields
    {
        class Field;
    }
    namespace Fields
    {
        class FieldExpression;
    }
    namespace Fields
    {
        class FieldVariable;
    }
    namespace Fields
    {
        class _FieldFormulaBuilder;
        class FieldFormulaImpl;
        /**  @brief  Represents the Field Formula class. 

         
             <br> A field (see @link Fields::Field Fields::Field@endlink ) which has <b><tt>n</tt></b> number of dependent
            variables, where each dependent variable (see @link Fields::FieldVariable Fields::FieldVariable@endlink ) is implemented using the NX Expression sub-system.
            In practical terms, a field formula is implemented using n number of field expressions
            @link Fields::FieldExpression Fields::FieldExpression@endlink . <br>  */
        class NXOPENCPPEXPORT  FieldFormula : public Fields::Field
        {
            private: FieldFormulaImpl * m_fieldformula_impl;
            private: friend class  _FieldFormulaBuilder;
            protected: FieldFormula();
            public: ~FieldFormula();
            /** Edit the formula field.  Specifies the new expression @link Fields::FieldExpression Fields::FieldExpression@endlink 
                        array and the array of @link Fields::FieldVariable Fields::FieldVariable@endlink s used.
                     <br> License requirements : None */
            public: void EditFieldFormula
            (
                const std::vector<NXOpen::Fields::FieldVariable *> & indepVarArray /** independent variables to be associated with the field */,
                const std::vector<NXOpen::Fields::FieldExpression *> & depExpArray /** dependent field expressions to be associated with the field */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
