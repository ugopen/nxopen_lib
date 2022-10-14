#ifndef NXOpen_CAE_XYPLOT_LEGENDTABLE_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_LEGENDTABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_LegendTable.ja
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
#include <NXOpen/CAE_Xyplot_LegendTableStyle.hxx>
#include <NXOpen/CAE_Xyplot_BaseModel.hxx>
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
        namespace Xyplot
        {
            class LegendTable;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseModel;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class LegendTableStyle;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _LegendTableBuilder;
            class LegendTableImpl;
            /** Manages the legend table.  <br> Not support KF.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  LegendTable : public NXOpen::CAE::Xyplot::BaseModel
            {
                private: LegendTableImpl * m_legendtable_impl;
                private: friend class  _LegendTableBuilder;
                protected: LegendTable();
                public: ~LegendTable();
                /**Returns  the legend table style 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::LegendTableStyle * LegendTableStyle
                (
                );
                /**Gets the free text of legend table item  @return   
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString GetFreeTextOfLegendItem
                (
                    int dataIndex /**the index of record index*/
                );
                /**Sets the free text of legend table item 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetFreeTextOfLegendItem
                (
                    int dataIndex /**the index of record index*/,
                    const NXString & freeText /** freetext */ 
                );
                /**Sets the free text of legend table item 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                void SetFreeTextOfLegendItem
                (
                    int dataIndex /**the index of record index*/,
                    const char * freeText /** freetext */ 
                );
                /**Resets the free text of legend table item 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void ResetFreeTextOfLegendItem
                (
                    int dataIndex /**the index of record index*/
                );
            };
        }
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