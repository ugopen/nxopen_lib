#ifndef NXOpen_CAE_XYPLOT_PREFERENCE_HXX_INCLUDED
#define NXOpen_CAE_XYPLOT_PREFERENCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Xyplot_Preference.ja
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
#include <NXOpen/CAE_Xyplot_Preference.hxx>
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
            class Preference;
        }
    }
    namespace CAE
    {
        namespace Xyplot
        {
            class _PreferenceBuilder;
            class PreferenceImpl;
            /** Manages the preference data  <br> Not support KF.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  Preference : public TaggedObject
            {
                /** Defines the target graphic window type */
                public: enum TargetGraphicWindowOption
                {
                    TargetGraphicWindowOptionMain/** Only shows plot graph on main graphic window */,
                    TargetGraphicWindowOptionSeparate/** Only shows plot graph on a separate graphic window */,
                    TargetGraphicWindowOptionBoth/** Shows plot graph on either main graphic window or a separate graphic window */
                };

                /** Defines whether to always show plot graph on a new separate graphic window */
                public: enum NewWindowChoice
                {
                    NewWindowChoicePrompt/** Prompts user to show plot graph on either an existing or a new separate graphic window */,
                    NewWindowChoiceAlways/** Always show plot graph on a new separate graphic window */
                };

                private: PreferenceImpl * m_preference_impl;
                private: friend class  _PreferenceBuilder;
                protected: Preference();
                public: ~Preference();
                /**Returns  the target window setting value 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::Preference::TargetGraphicWindowOption TargetWindowSetting
                (
                );
                /**Sets  the target window setting value 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetTargetWindowSetting
                (
                    NXOpen::CAE::Xyplot::Preference::TargetGraphicWindowOption targetWindowSetting /** targetwindowsetting */ 
                );
                /**Returns  the new window setting value. Avaliable when @link CAE::Xyplot::Preference::TargetWindowSetting CAE::Xyplot::Preference::TargetWindowSetting @endlink and @link CAE::Xyplot::Preference::SetTargetWindowSetting CAE::Xyplot::Preference::SetTargetWindowSetting @endlink 
                                is @link CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Xyplot::Preference::NewWindowChoice NewWindowSetting
                (
                );
                /**Sets  the new window setting value. Avaliable when @link CAE::Xyplot::Preference::TargetWindowSetting CAE::Xyplot::Preference::TargetWindowSetting @endlink and @link CAE::Xyplot::Preference::SetTargetWindowSetting CAE::Xyplot::Preference::SetTargetWindowSetting @endlink 
                                is @link CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate CAE::Xyplot::Preference::TargetGraphicWindowOptionSeparate@endlink . 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void SetNewWindowSetting
                (
                    NXOpen::CAE::Xyplot::Preference::NewWindowChoice newWindowSetting /** New window setting */
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
