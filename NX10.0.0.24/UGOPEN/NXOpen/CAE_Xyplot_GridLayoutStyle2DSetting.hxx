#ifndef NXOpen_CAE_XYPLOT_GRIDLAYOUTSTYLE2DSETTING_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_GRIDLAYOUTSTYLE2DSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_GridLayoutStyle2DSetting.ja
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
#include <NXOpen/CAE_Xyplot_BaseGridLayoutStyleSetting.hxx>
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
            class GridLayoutStyle2DSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseGridLayoutStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _GridLayoutStyle2DSettingBuilder;
            class GridLayoutStyle2DSettingImpl;
            /** Represents the 2d grid layout display style.  <br> Not support KF.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  GridLayoutStyle2DSetting : public NXOpen::CAE::Xyplot::BaseGridLayoutStyleSetting
            {
                private: GridLayoutStyle2DSettingImpl * m_gridlayoutstyle2dsetting_impl;
                private: friend class  _GridLayoutStyle2DSettingBuilder;
                protected: GridLayoutStyle2DSetting();
                public: ~GridLayoutStyle2DSetting();
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
