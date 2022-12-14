#ifndef NXOpen_CAE_XYPLOT_AXISLABELSTYLE_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_AXISLABELSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_AxisLabelStyle.ja
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
#include <NXOpen/CAE_Xyplot_CustomTextStyleSetting.hxx>
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
            class AxisLabelStyle;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class CustomTextStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _AxisLabelStyleBuilder;
            class AxisLabelStyleImpl;
            /** Represents the axis label display style. Call @link CAE::Xyplot::IDisplayStyle::CommitChange CAE::Xyplot::IDisplayStyle::CommitChange@endlink 
                        to apply style changes to corresponding plot after it's modified.
                     <br> Not support KF.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  AxisLabelStyle : public NXOpen::CAE::Xyplot::CustomTextStyleSetting
            {
                private: AxisLabelStyleImpl * m_axislabelstyle_impl;
                private: friend class  _AxisLabelStyleBuilder;
                protected: AxisLabelStyle();
                public: ~AxisLabelStyle();
                /**Returns  the option specifies whether to display axis label in a single line 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool UseSingleLine
                (
                );
                /**Sets  the option specifies whether to display axis label in a single line 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetUseSingleLine
                (
                    bool isSingleLine /** sinle line */
                );
                /**Returns  the option specifies whether to include unit information in axis label 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IncludeUnit
                (
                );
                /**Sets  the option specifies whether to include unit information in axis label 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetIncludeUnit
                (
                    bool hasIncludeUnit /** include unit */
                );
                /**Returns  the option specifies whether to include measure type in axis label 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IncludeMeasureType
                (
                );
                /**Sets  the option specifies whether to include measure type in axis label 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetIncludeMeasureType
                (
                    bool hasIncludeMeasureType /** include measure type */
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
