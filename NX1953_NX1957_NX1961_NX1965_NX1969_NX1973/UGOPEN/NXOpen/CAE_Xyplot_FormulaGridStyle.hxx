#ifndef NXOpen_CAE_XYPLOT_FORMULAGRIDSTYLE_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_FORMULAGRIDSTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_FormulaGridStyle.ja
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
#include <NXOpen/CAE_Xyplot_CurveDisplaySettings.hxx>
#include <NXOpen/CAE_Xyplot_FormulaExpressionStyle.hxx>
#include <NXOpen/CAE_Xyplot_TextStyleSetting.hxx>
#include <NXOpen/CAE_Xyplot_BaseDisplayStyleSetting.hxx>
#include <NXOpen/CAE_Xyplot_IVisibleDisplayStyle.hxx>
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
            class FormulaGridStyle;
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
            class FormulaExpressionStyle;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class IVisibleDisplayStyle;
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
            class _FormulaGridStyleBuilder;
            class FormulaGridStyleImpl;
            /** Manages the formula grid style.  <br> Not support KF.  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  FormulaGridStyle : public NXOpen::CAE::Xyplot::BaseDisplayStyleSetting, public virtual NXOpen::CAE::Xyplot::IVisibleDisplayStyle
            {
                private: FormulaGridStyleImpl * m_formulagridstyle_impl;
                private: friend class  _FormulaGridStyleBuilder;
                protected: FormulaGridStyle();
                public: ~FormulaGridStyle();
                /** Gets the formula expression style.  @return  expression style 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::FormulaExpressionStyle * GetExpressionStyle
                (
                );
                /** Gets the grid line style.  @return  grid line style 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::CurveDisplaySettings * GetGridLineStyle
                (
                );
                /** Gets the grid value text style.  @return  grid value text style 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::TextStyleSetting * GetGridValueTextStyle
                (
                );
                /**Returns  the visibility 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual bool Visibility
                (
                );
                /**Sets  the visibility 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void SetVisibility
                (
                    bool visibility /** visibility */ 
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
