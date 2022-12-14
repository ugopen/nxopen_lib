#ifndef NXOpen_SHEETMETALELLIPSEPRINTER_HXX_INCLUDED
#define NXOpen_SHEETMETALELLIPSEPRINTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SheetMetalEllipsePrinter.ja
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
#include <NXOpen/CurveValidator.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class SheetMetalEllipsePrinter;
    class CurveValidator;
    class _SheetMetalEllipsePrinterBuilder;
    class SheetMetalEllipsePrinterImpl;

    /// \cond NX_NO_DOC 
    /** Ellipse printer for a SheetMetal part.  <br> Creator not available in KF because this is NXSheetMetal Autotest Printer class and should not be made available to customers.  <br> 
     <br>  Created in NX12.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  SheetMetalEllipsePrinter : public NXOpen::CurveValidator
    {
        private: SheetMetalEllipsePrinterImpl * m_sheetmetalellipseprinter_impl;
        private: friend class  _SheetMetalEllipsePrinterBuilder;
        protected: SheetMetalEllipsePrinter();
        public: ~SheetMetalEllipsePrinter();
    };

    /// \endcond 
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
