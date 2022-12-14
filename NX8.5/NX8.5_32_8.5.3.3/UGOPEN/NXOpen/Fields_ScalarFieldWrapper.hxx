#ifndef NXOpen_FIELDS_SCALARFIELDWRAPPER_HXX_INCLUDED
#define NXOpen_FIELDS_SCALARFIELDWRAPPER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_ScalarFieldWrapper.ja
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
#include <NXOpen/NXObject.hxx>
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
        class ScalarFieldWrapper;
    }
    class Expression;
    namespace Fields
    {
        class Field;
    }
    class NXObject;
    namespace Fields
    {
        class _ScalarFieldWrapperBuilder;
        class ScalarFieldWrapperImpl;
        /** This class defines a scalar value that is internally 
                backed up by a (optionally scaled) field or an expression. 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FIELDSEXPORT  ScalarFieldWrapper : public NXObject
        {
            private: ScalarFieldWrapperImpl * m_scalarfieldwrapper_impl;
            private: friend class  _ScalarFieldWrapperBuilder;
            protected: ScalarFieldWrapper();
            public: ~ScalarFieldWrapper();
            /** Sets the implementation of the wrapper to the specified expression 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetExpression
            (
                NXOpen::Expression * expression /** an existing expression that will be this wrapper's value */
            );
            /** Returns the implementation if the wrapper is backed up by an expression;
                        NULL otherwise  @return  an existing expression or NULL 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * GetExpression
            (
            );
            /** Sets the implementation of the wrapper to the specified field 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetField
            (
                NXOpen::Fields::Field * field /** an existing field that will be this wrapper's value */,
                double scaleFactor /** the field will be multiplied by this scale factor when being evaluated */
            );
            /** Returns the implementation if the wrapper is backed up by a field;
                        NULL otherwise  @return  an existing field or NULL 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Fields::Field * GetField
            (
            );
            /** Returns the scale factor to be applied to the field, this is only applicable if the wrapper is backed up by a field  @return  the field will be multiplied by this scale factor when being evaluated 
             <br>  Created in NX8.0.3.  <br>  
             <br> License requirements : None */
            public: double GetFieldScaleFactor
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
