#ifndef NXOpen_CAE_LAMINATEQUICKPOSTREPORT_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEQUICKPOSTREPORT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateQuickPostReport.ja
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
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class LaminateQuickPostReport;
    }
    class NXObject;
    namespace CAE
    {
        class _LaminateQuickPostReportBuilder;
        class LaminateQuickPostReportImpl;
        /**  @brief  Laminate quick post summary report  

           <br> To create or edit an instance of this class, use @link CAE::LaminateQuickPostReportBuilder  CAE::LaminateQuickPostReportBuilder @endlink  <br> 
         <br>  @deprecated Deprecated in NX8.0.0.  Use @link CAE::LaminateSpreadsheetReport CAE::LaminateSpreadsheetReport@endlink  and @link CAE::LaminateGraphicalReport CAE::LaminateGraphicalReport@endlink  and @link CAE::LaminateQuickReport CAE::LaminateQuickReport@endlink  instead. <br>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  NX_DEPRECATED("Deprecated in NX8.0.0.  Use CAE::LaminateSpreadsheetReport and CAE::LaminateGraphicalReport and CAE::LaminateQuickReport instead.")  LaminateQuickPostReport : public NXObject
        {
            private: LaminateQuickPostReportImpl * m_laminatequickpostreport_impl;
            private: friend class  _LaminateQuickPostReportBuilder;
            protected: LaminateQuickPostReport();
            public: ~LaminateQuickPostReport();
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
