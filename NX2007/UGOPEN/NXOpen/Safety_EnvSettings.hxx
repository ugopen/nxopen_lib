#ifndef NXOpen_SAFETY_ENVSETTINGS_HXX_INCLUDED
#define NXOpen_SAFETY_ENVSETTINGS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Safety_EnvSettings.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libsafetyopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Safety
    {
        class EnvSettings;
    }
    class NXObject;
    namespace Safety
    {
        class _EnvSettingsBuilder;
        class EnvSettingsImpl;
        /**  Represents the Safety Environment Settings.     <br> No Creator  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class SAFETYOPENCPPEXPORT  EnvSettings : public NXOpen::NXObject
        {
            private: EnvSettingsImpl * m_envsettings_impl;
            private: friend class  _EnvSettingsBuilder;
            protected: EnvSettings();
            public: ~EnvSettings();
        };
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