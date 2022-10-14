#ifndef NXOpen_CAE_XYPLOT_BASEPLATESTYLESETTING_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_BASEPLATESTYLESETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_BasePlateStyleSetting.ja
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
#include <NXOpen/CAE_Xyplot_BaseSymbolStyleSetting.hxx>
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
            class BasePlateStyleSetting;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class BaseSymbolStyleSetting;
        }
    }
    class NXColor;
    namespace CAE
    {
        namespace Xyplot
        {
            class _BasePlateStyleSettingBuilder;
            class BasePlateStyleSettingImpl;
            /** Represents the base plate display style. Call @link CAE::Xyplot::BaseDisplayStyleSetting::CommitChange CAE::Xyplot::BaseDisplayStyleSetting::CommitChange@endlink 
                        to apply style changes to corresponding plot after it's modified.
                     <br> Not support KF.  <br> 
             <br>  @deprecated Deprecated in NX12.0.0.  There is no replacement for this class. <br>  

             <br>  Created in NX9.0.0.  <br>  
            */
            class NX_DEPRECATED("Deprecated in NX12.0.0.  There is no replacement for this class.") NXOPENCPP_CAEEXPORT  BasePlateStyleSetting : public NXOpen::CAE::Xyplot::BaseSymbolStyleSetting
            {
                private: BasePlateStyleSettingImpl * m_baseplatestylesetting_impl;
                private: friend class  _BasePlateStyleSettingBuilder;
                protected: BasePlateStyleSetting();
                public: ~BasePlateStyleSetting();
                /**Returns  a value indicating whether to display the outline 
                 <br>  @deprecated Deprecated in NX12.0.0.  There is no replacement for this class. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX12.0.0.  There is no replacement for this class.") bool ShowOutline
                (
                );
                /**Sets  a value indicating whether to display the outline 
                 <br>  @deprecated Deprecated in NX12.0.0.  There is no replacement for this class. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX12.0.0.  There is no replacement for this class.") void SetShowOutline
                (
                    bool showOutline /** showoutline */ 
                );
                /**Returns  the outline color 
                 <br>  @deprecated Deprecated in NX12.0.0.  There is no replacement for this class. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX12.0.0.  There is no replacement for this class.") NXOpen::NXColor * OutlineColor
                (
                );
                /**Sets  the outline color 
                 <br>  @deprecated Deprecated in NX12.0.0.  There is no replacement for this class. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX12.0.0.  There is no replacement for this class.") void SetOutlineColor
                (
                    NXOpen::NXColor * outlineColor /** outlinecolor */ 
                );
                /**Returns  the filling color 
                 <br>  @deprecated Deprecated in NX12.0.0.  There is no replacement for this class. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX12.0.0.  There is no replacement for this class.") NXOpen::NXColor * FillingColor
                (
                );
                /**Sets  the filling color 
                 <br>  @deprecated Deprecated in NX12.0.0.  There is no replacement for this class. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX12.0.0.  There is no replacement for this class.") void SetFillingColor
                (
                    NXOpen::NXColor * fillingColor /** fillingcolor */ 
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