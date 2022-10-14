#ifndef NXOpen_CAE_XYPLOT_AXISITEMSTYLE_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_AXISITEMSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_AxisItemStyle.ja
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
#include <NXOpen/CAE_Xyplot_TextStyleSetting.hxx>
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
            class AxisItemStyle;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class TextStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _AxisItemStyleBuilder;
            class AxisItemStyleImpl;
            /** Represents the axis item display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
                        to apply style changes to corresponding plot after it's modified.
                     <br> Not support KF.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  AxisItemStyle : public NXOpen::CAE::Xyplot::TextStyleSetting
            {
                private: AxisItemStyleImpl * m_axisitemstyle_impl;
                private: friend class  _AxisItemStyleBuilder;
                protected: AxisItemStyle();
                public: ~AxisItemStyle();
                /**Returns  the maximum character count. The minimum value is 1. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int MaximumCharacterCount
                (
                );
                /**Sets  the maximum character count. The minimum value is 1. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetMaximumCharacterCount
                (
                    int maximumCharacterCount /** maximum character count */
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