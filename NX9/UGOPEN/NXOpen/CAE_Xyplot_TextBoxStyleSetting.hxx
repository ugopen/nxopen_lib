#ifndef NXOpen_CAE_XYPLOT_TEXTBOXSTYLESETTING_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_TEXTBOXSTYLESETTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_TextBoxStyleSetting.ja
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
#include <NXOpen/CAE_Xyplot_TextBoxStyleSetting.hxx>
#include <NXOpen/TaggedObject.hxx>
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
            class TextBoxStyleSetting;
        }
    }
    class NXColor;
    namespace CAE
    {
        namespace Xyplot
        {
            class _TextBoxStyleSettingBuilder;
            class TextBoxStyleSettingImpl;
            /** Represents the text box display style. Call @link CAE::Xyplot::TextStyleSetting::CommitChange CAE::Xyplot::TextStyleSetting::CommitChange@endlink 
                        to apply style changes to corresponding plot after it's modified. <br> Not support KF.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TextBoxStyleSetting : public TaggedObject
            {
                private: TextBoxStyleSettingImpl * m_textboxstylesetting_impl;
                private: friend class  _TextBoxStyleSettingBuilder;
                protected: TextBoxStyleSetting();
                public: ~TextBoxStyleSetting();
                /**Returns  a value indicating whether to display the text box 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Visibility
                (
                );
                /**Sets  a value indicating whether to display the text box 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetVisibility
                (
                    bool visibility /** visibility */ 
                );
                /**Returns  the text box outline color
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::NXColor * Color
                (
                );
                /**Sets  the text box outline color
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetColor
                (
                    NXOpen::NXColor * color /** color */ 
                );
                /**Returns  a value indicating whether to fill the text box 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsFilled
                (
                );
                /**Sets  a value indicating whether to fill the text box 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetFilled
                (
                    bool isFilled /** isfilled */ 
                );
                /**Returns  the text box filling color
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::NXColor * FillingColor
                (
                );
                /**Sets  the text box filling color
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetFillingColor
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
