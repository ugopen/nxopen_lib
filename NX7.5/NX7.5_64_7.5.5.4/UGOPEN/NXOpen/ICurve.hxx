#ifndef NXOpen_ICURVE_HXX_INCLUDED
#define NXOpen_ICURVE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ICurve.ja
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
#include <NXOpen/IBaseCurve.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ICurve;
    class IBaseCurve;
    /** Represents something containing a two dimensional modeling curve */
    class NXOPENCPPEXPORT  ICurve : public virtual IBaseCurve
    {
        public: virtual ~ICurve() {}
    };
}
#undef EXPORTLIBRARY
#endif