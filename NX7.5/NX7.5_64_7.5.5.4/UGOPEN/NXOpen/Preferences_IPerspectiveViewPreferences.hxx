#ifndef NXOpen_PREFERENCES_IPERSPECTIVEVIEWPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_IPERSPECTIVEVIEWPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_IPerspectiveViewPreferences.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class IPerspectiveViewPreferences;
    }
    namespace Preferences
    {
        /** Represents set of PerspectiveViewPreferences applicable to drafting views. */
        class NXOPENCPPEXPORT  IPerspectiveViewPreferences
        {
            virtual void EnsureVtableExists() {}
            public: virtual ~IPerspectiveViewPreferences() {}
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif