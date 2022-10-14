#ifndef NXOpen_CAE_XYPLOT_CURVEDISPLAYSETTINGS_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_CURVEDISPLAYSETTINGS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_CurveDisplaySettings.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/CAE_Xyplot_BaseDisplayStyleSetting.hxx>
#include <NXOpen/CAE_Xyplot_ICurveDisplaySettings.hxx>
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
            class CurveDisplaySettings;
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
            class ICurveDisplaySettings;
        }
    }
    class NXColor;
    namespace CAE
    {
        namespace Xyplot
        {
            class _CurveDisplaySettingsBuilder;
            class CurveDisplaySettingsImpl;
            /** Represents the curve display style. Call Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
                        to apply style changes to corresponding plot after it's modified. <br> Not support KF.  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  CurveDisplaySettings : public NXOpen::CAE::Xyplot::BaseDisplayStyleSetting, public virtual NXOpen::CAE::Xyplot::ICurveDisplaySettings
            {
                private: CurveDisplaySettingsImpl * m_curvedisplaysettings_impl;
                private: friend class  _CurveDisplaySettingsBuilder;
                protected: CurveDisplaySettings();
                public: ~CurveDisplaySettings();
                /**Returns  the line color 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::NXColor * Color
                (
                );
                /**Sets  the line color 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void SetColor
                (
                    NXOpen::NXColor * color /** color */ 
                );
                /**Returns  the line font 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::DisplayableObject::ObjectFont Font
                (
                );
                /**Sets  the line font 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void SetFont
                (
                    NXOpen::DisplayableObject::ObjectFont gridFont /** gridfont */ 
                );
                /**Returns  the line width 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::DisplayableObject::ObjectWidth Width
                (
                );
                /**Sets  the line width 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual void SetWidth
                (
                    NXOpen::DisplayableObject::ObjectWidth gridWidth /** gridwidth */ 
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