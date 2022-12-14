#ifndef NXOpen_CAE_XYPLOT_BARSTYLE2DSETTING_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_BARSTYLE2DSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_BarStyle2DSetting.ja
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
#include <NXOpen/CAE_Xyplot_BaseBarStyleSetting.hxx>
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
            class BarStyle2DSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseBarStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _BarStyle2DSettingBuilder;
            class BarStyle2DSettingImpl;
            /** Represents the 2d bar display style.  <br> Not support KF.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  BarStyle2DSetting : public NXOpen::CAE::Xyplot::BaseBarStyleSetting
            {
                private: BarStyle2DSettingImpl * m_barstyle2dsetting_impl;
                private: friend class  _BarStyle2DSettingBuilder;
                protected: BarStyle2DSetting();
                public: ~BarStyle2DSetting();
                /**Returns  a value indicating whether to set bar width as constant 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowConstantWidth
                (
                );
                /**Sets  a value indicating whether to set bar width as constant 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetShowConstantWidth
                (
                    bool showConstBarWidth /** showconstbarwidth */ 
                );
                /**Returns  the constant bar width. The range is from 0.05 to 100. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: double ConstantWidth
                (
                );
                /**Sets  the constant bar width. The range is from 0.05 to 100. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetConstantWidth
                (
                    double constBarWidth /** constbarwidth */ 
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
