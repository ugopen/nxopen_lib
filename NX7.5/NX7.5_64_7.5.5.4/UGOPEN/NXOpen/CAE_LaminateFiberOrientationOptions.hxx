#ifndef NXOpen_CAE_LAMINATEFIBERORIENTATIONOPTIONS_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEFIBERORIENTATIONOPTIONS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateFiberOrientationOptions.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class LaminateFiberOrientationOptions;
    }
    class NXObject;
    namespace CAE
    {
        class _LaminateFiberOrientationOptionsBuilder;
        class LaminateFiberOrientationOptionsImpl;
        /** Laminate Fiber Orientation Options */
        class NXOPENCPPEXPORT  LaminateFiberOrientationOptions : public NXObject
        {
            private: LaminateFiberOrientationOptionsImpl * m_laminatefiberorientationoptions_impl;
            private: friend class  _LaminateFiberOrientationOptionsBuilder;
            protected: LaminateFiberOrientationOptions();
            public: ~LaminateFiberOrientationOptions();
        };
    }
}
#undef EXPORTLIBRARY
#endif
