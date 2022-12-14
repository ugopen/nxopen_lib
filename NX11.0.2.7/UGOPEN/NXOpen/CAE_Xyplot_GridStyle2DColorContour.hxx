#ifndef NXOpen_CAE_XYPLOT_GRIDSTYLE2DCOLORCONTOUR_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_GRIDSTYLE2DCOLORCONTOUR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_GridStyle2DColorContour.ja
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
#include <NXOpen/CAE_Xyplot_GridStyle2DColorContour.hxx>
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
            class GridStyle2DColorContour;
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
            class _GridStyle2DColorContourBuilder;
            class GridStyle2DColorContourImpl;
            /** Manages the grid styles for colorbar and colormap plot.  <br> Not support KF.  <br> 
             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  GridStyle2DColorContour : public NXOpen::CAE::Xyplot::BaseGridLayoutStyleSetting
            {
                private: GridStyle2DColorContourImpl * m_gridstyle2dcolorcontour_impl;
                private: friend class  _GridStyle2DColorContourBuilder;
                protected: GridStyle2DColorContour();
                public: ~GridStyle2DColorContour();
                /**Returns  the show order grid value 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ShowOrderGrid
                (
                );
                /**Sets  the show order grid value 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetShowOrderGrid
                (
                    bool isShowOrderGrid /** Show order grid value */
                );
                /**Returns  the automatic show order grid value 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsAutoOrderGrid
                (
                );
                /**Sets  the automatic show order grid value 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetAutoOrderGrid
                (
                    bool isAutoOrderGrid /** Automatic show order grid value */
                );
                /**Returns  the count of order grid 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: int OrderGridCount
                (
                );
                /**Sets  the count of order grid 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetOrderGridCount
                (
                    int orderGridCount /** Count of order grid */
                );
                /**Returns  the interval of order line 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: double OrderInterval
                (
                );
                /**Sets  the interval of order line 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetOrderInterval
                (
                    double orderInterval /** interval of order grid */
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
