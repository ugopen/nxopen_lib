#ifndef NXOpen_REPORT_TEXTITEM_HXX_INCLUDED
#define NXOpen_REPORT_TEXTITEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Report_TextItem.ja
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
#include <NXOpen/Report_BaseItem.hxx>
#include <NXOpen/libnxopencpp_report_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Report
    {
        class TextItem;
    }
    namespace Report
    {
        class BaseItem;
    }
    namespace Report
    {
        class _TextItemBuilder;
        class TextItemImpl;
        /** Represents a text item.  <br> Not support KF.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_REPORTEXPORT  TextItem : public NXOpen::Report::BaseItem
        {
            private: TextItemImpl * m_textitem_impl;
            private: friend class  _TextItemBuilder;
            protected: TextItem();
            public: ~TextItem();
            /** Get the text content. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void GetText
            (
                std::vector<NXString> & lineTexts /** linetexts */ 
            );
            /** Set the text content. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetText
            (
                std::vector<NXString> & lineTexts /** linetexts */ 
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
