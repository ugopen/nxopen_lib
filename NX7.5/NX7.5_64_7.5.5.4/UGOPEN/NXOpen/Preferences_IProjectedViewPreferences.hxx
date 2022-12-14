#ifndef NXOpen_PREFERENCES_IPROJECTEDVIEWPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_IPROJECTEDVIEWPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_IProjectedViewPreferences.ja
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
        class IProjectedViewPreferences;
    }
    namespace Preferences
    {
        /** Represents set of ProjectedViewPreferences applicable to drafting views. */
        class NXOPENCPPEXPORT  IProjectedViewPreferences
        {
            virtual void EnsureVtableExists() {}
            public: virtual ~IProjectedViewPreferences() {}
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
