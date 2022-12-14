#ifndef NXOpen_CAE_XYPLOT_GRAPHOPTIONSSTYLE2D_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_GRAPHOPTIONSSTYLE2D_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_GraphOptionsStyle2D.ja
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
#include <NXOpen/CAE_XyplotDataTypes.hxx>
#include <NXOpen/CAE_Xyplot_CurveDisplaySettings.hxx>
#include <NXOpen/CAE_Xyplot_BaseDisplayStyleSetting.hxx>
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
            class GraphOptionsStyle2D;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseDisplayStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class CurveDisplaySettings;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _GraphOptionsStyle2DBuilder;
            class GraphOptionsStyle2DImpl;
            /** Manages the specific settings for 2D graph.  <br> Not support KF.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  GraphOptionsStyle2D : public NXOpen::CAE::Xyplot::BaseDisplayStyleSetting
            {
                private: GraphOptionsStyle2DImpl * m_graphoptionsstyle2d_impl;
                private: friend class  _GraphOptionsStyle2DBuilder;
                protected: GraphOptionsStyle2D();
                public: ~GraphOptionsStyle2D();
                /**Returns  a value specifies whether to show frequency band summation 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowFrequencyBandSummation
                (
                );
                /**Sets  a value specifies whether to show frequency band summation 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetShowFrequencyBandSummation
                (
                    bool showFreqBandSummation /** showfreqbandsummation */ 
                );
                /**Returns  a value specifies the frequency band summation band type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::FrequencyBandSummationBandType FrequencyBandSummationBandType
                (
                );
                /**Sets  a value specifies the frequency band summation band type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetFrequencyBandSummationBandType
                (
                    NXOpen::CAE::Xyplot::FrequencyBandSummationBandType freqBandSummationBandType /** freqbandsummationbandtype */ 
                );
                /**Returns  a value specifies whether to show total response line for 2D polar plot 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowTotalResponseLineForPolar
                (
                );
                /**Sets  a value specifies whether to show total response line for 2D polar plot 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetShowTotalResponseLineForPolar
                (
                    bool showTotalResponseLineForPolar /** showtotalresponselineforpolar */ 
                );
                /**Returns  a value specifies whether to show total response line for 2D vector plot 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowTotalResponseLineForVector
                (
                );
                /**Sets  a value specifies whether to show total response line for 2D vector plot 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetShowTotalResponseLineForVector
                (
                    bool showTotalResponseLineForVector /** showtotalresponselineforvector */ 
                );
                /**Returns  the total response line setting 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::CurveDisplaySettings * TotalResponseLineSetting
                (
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
