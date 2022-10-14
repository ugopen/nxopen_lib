#ifndef NXOpen_CAE_XYPLOT_LINESTYLE3DSETTING_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_LINESTYLE3DSETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_LineStyle3DSetting.ja
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
#include <NXOpen/CAE_Xyplot_LineStyle3DSetting.hxx>
#include <NXOpen/CAE_Xyplot_BaseLineStyleSetting.hxx>
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
            class LineStyle3DSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseLineStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _LineStyle3DSettingBuilder;
            class LineStyle3DSettingImpl;
            /** Represents the 3d line display style.  <br> Not support KF.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  LineStyle3DSetting : public NXOpen::CAE::Xyplot::BaseLineStyleSetting
            {
                private: LineStyle3DSettingImpl * m_linestyle3dsetting_impl;
                private: friend class  _LineStyle3DSettingBuilder;
                protected: LineStyle3DSetting();
                public: ~LineStyle3DSetting();
                /**Returns  the line direction 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::Direction Direction
                (
                );
                /**Sets  the line direction 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetDirection
                (
                    NXOpen::CAE::Xyplot::Direction direction /** direction */ 
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