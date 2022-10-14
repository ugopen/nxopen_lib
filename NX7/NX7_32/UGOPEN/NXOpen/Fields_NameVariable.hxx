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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** This class stores the common name and measure for field variables. */
        class NXOPENCPPEXPORT NameVariable : public NXObject
        {
            private: friend class  _NameVariableBuilder;
            protected: NameVariable();
            /**Returns  the name of the variable  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Returns  the measure of the variable  <br> License requirements : None */
            public: NXString Measure
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif