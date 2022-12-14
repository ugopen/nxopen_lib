#ifndef NXOpen_SCHEMATIC_SHEET_HXX_INCLUDED
#define NXOpen_SCHEMATIC_SHEET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Schematic_Sheet.ja
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
#include <NXOpen/libnxopencpp_schematic_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Schematic
    {
        class Sheet;
    }
    class NXObject;
    namespace Schematic
    {
        class _SheetBuilder;
        class SheetImpl;

        /// \cond NX_NO_DOC 
        /** 
                Represents Schematic Sheet class
             <br> Use the static method to obtain an instance.  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_SCHEMATICEXPORT  Sheet : public NXOpen::NXObject
        {
            private: SheetImpl * m_sheet_impl;
            private: friend class  _SheetBuilder;
            protected: Sheet();
            public: ~Sheet();
        };

        /// \endcond 
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
