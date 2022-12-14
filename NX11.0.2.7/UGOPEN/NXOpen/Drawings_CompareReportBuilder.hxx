#ifndef NXOpen_DRAWINGS_COMPAREREPORTBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_COMPAREREPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_CompareReportBuilder.ja
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
#include <NXOpen/Drawings_CompareReportBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class CompareReportBuilder;
    }
    class Builder;
    namespace Drawings
    {
        class _CompareReportBuilderBuilder;
        class CompareReportBuilderImpl;
        /** Represents a @link NXOpen::Drawings::CompareReportBuilder NXOpen::Drawings::CompareReportBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::DrawingCompareManager::CreateCompareReportBuilder  NXOpen::DrawingCompareManager::CreateCompareReportBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  CompareReportBuilder : public NXOpen::Builder
        {
            private: CompareReportBuilderImpl * m_comparereportbuilder_impl;
            private: friend class  _CompareReportBuilderBuilder;
            protected: CompareReportBuilder();
            public: ~CompareReportBuilder();
            /** Returns the summary  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetSummary
            (
            );
            /**Returns  the report summary status line
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SummaryStatusLine
            (
            );
            /** Returns the detail summary of report @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetDetailSummary
            (
            );
            /** Returns the changes summary of report @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetChangesSummary
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
