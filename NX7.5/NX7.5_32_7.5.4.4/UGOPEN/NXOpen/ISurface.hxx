#ifndef NXOpen_ISURFACE_HXX_INCLUDED
#define NXOpen_ISURFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ISurface.ja
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
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ISurface;
    class INXObject;
    /** Represents something containing a two dimensional surface */
    class NXOPENCPPEXPORT  ISurface : public virtual INXObject
    {
        public: virtual ~ISurface() {}
    };
}
#undef EXPORTLIBRARY
#endif
