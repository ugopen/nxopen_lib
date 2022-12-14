#ifndef NXOpen_CAE_LAMINATEPOSTREPORT_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEPOSTREPORT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminatePostReport.ja
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
        class LaminatePostReport;
    }
    namespace CAE
    {
        class LaminateGraphicalReportCollection;
    }
    namespace CAE
    {
        class LaminateQuickReportCollection;
    }
    namespace CAE
    {
        class LaminateSpreadsheetReportCollection;
    }
    class NXObject;
    namespace CAE
    {
        class _LaminatePostReportBuilder;
        class LaminatePostReportImpl;
        /** Represents an advanced post reporting setup for laminate results. Can be used
                to generate spreadsheet and graphical reports.  <br> There is no kf creator.  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LaminatePostReport : public NXOpen::NXObject
        {
            private: LaminatePostReportImpl * m_laminatepostreport_impl;
            private: friend class  _LaminatePostReportBuilder;
            protected: LaminatePostReport();
            public: ~LaminatePostReport();
            /**Returns  the name of the laminate post report setup 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name of the laminate post report setup 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name of the laminate post report setup 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_lam_composites ("Laminate Composites") */
            void SetName
            (
                const char * name /** name */ 
            );


            /** The laminate spreadsheet report collection 
             <br>  Created in NX8.0.0.  <br>  
            */
            public: NXOpen::CAE::LaminateSpreadsheetReportCollection *LaminateSpreadsheetReports();
            /** The laminate graphical report collection 
             <br>  Created in NX8.0.0.  <br>  
            */
            public: NXOpen::CAE::LaminateGraphicalReportCollection *LaminateGraphicalReports();
            /** The laminate quick report collection 
             <br>  Created in NX8.0.0.  <br>  
            */
            public: NXOpen::CAE::LaminateQuickReportCollection *LaminateQuickReports();
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
