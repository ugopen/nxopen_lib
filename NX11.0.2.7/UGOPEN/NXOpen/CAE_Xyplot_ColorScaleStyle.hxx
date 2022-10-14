#ifndef NXOpen_CAE_XYPLOT_COLORSCALESTYLE_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_COLORSCALESTYLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_ColorScaleStyle.ja
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
#include <NXOpen/CAE_Xyplot_ColorScaleStyle.hxx>
#include <NXOpen/CAE_Xyplot_IDisplayStyle.hxx>
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
            class ColorScaleStyle;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class IDisplayStyle;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _ColorScaleStyleBuilder;
            class ColorScaleStyleImpl;
            /** Represents the color scale display style. Call @link CAE::Xyplot::IDisplayStyle::CommitChange CAE::Xyplot::IDisplayStyle::CommitChange@endlink 
                        to apply style changes to corresponding plot after it's modified.
                     <br> Not support KF.  <br> 
             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ColorScaleStyle : public NXOpen::TaggedObject, public virtual NXOpen::CAE::Xyplot::IDisplayStyle
            {
                private: ColorScaleStyleImpl * m_colorscalestyle_impl;
                private: friend class  _ColorScaleStyleBuilder;
                protected: ColorScaleStyle();
                public: ~ColorScaleStyle();
                /**Returns   the level setting 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: int Level
                (
                );
                /**Sets   the level setting 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetLevel
                (
                    int level /** Level setting*/
                );
                /** Commits any edits that have been applied to the display style.
                                Triggers the corresponding plot to update graph. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: virtual void CommitChange
                (
                );
                /**Returns  the owner style 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXOpen::CAE::Xyplot::IDisplayStyle * Owner
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