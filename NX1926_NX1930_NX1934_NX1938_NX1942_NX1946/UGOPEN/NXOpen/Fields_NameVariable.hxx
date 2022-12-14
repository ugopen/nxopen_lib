#ifndef NXOpen_FIELDS_NAMEVARIABLE_HXX_INCLUDED
#define NXOpen_FIELDS_NAMEVARIABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Fields_NameVariable.ja
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
        class NameVariable;
    }
    class NXObject;
    namespace Fields
    {
        class _NameVariableBuilder;
        class NameVariableImpl;
        /** This class stores the common name and measure for field variables. 
         <br>  Created in NX6.0.2.  <br>  
        */
        class NXOPENCPP_FIELDSEXPORT  NameVariable : public NXOpen::NXObject
        {
            private: NameVariableImpl * m_namevariable_impl;
            private: friend class  _NameVariableBuilder;
            protected: NameVariable();
            public: ~NameVariable();
            /**Returns  the measure of the variable 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: NXString Measure
            (
            );
            /**Returns  the name of the variable 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: NXString Name
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
