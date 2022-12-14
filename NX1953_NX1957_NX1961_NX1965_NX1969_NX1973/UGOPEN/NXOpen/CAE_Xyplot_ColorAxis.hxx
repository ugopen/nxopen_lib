#ifndef NXOpen_CAE_XYPLOT_COLORAXIS_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_COLORAXIS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_ColorAxis.ja
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
#include <NXOpen/CAE_Xyplot_AxisModel.hxx>
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
            class ColorAxis;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class AxisModel;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _ColorAxisBuilder;
            class ColorAxisImpl;
            /** Represents a color axis object on a XY graphing.  <br> Not support KF.  <br> 
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ColorAxis : public NXOpen::CAE::Xyplot::AxisModel
            {
                private: ColorAxisImpl * m_coloraxis_impl;
                private: friend class  _ColorAxisBuilder;
                protected: ColorAxis();
                public: ~ColorAxis();
                /** Gets the number of legend levels 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: int GetColorLegendLevelCount
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
