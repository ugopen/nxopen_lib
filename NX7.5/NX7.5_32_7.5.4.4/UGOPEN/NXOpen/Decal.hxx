#ifndef NXOpen_DECAL_HXX_INCLUDED
#define NXOpen_DECAL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Decal.ja
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
    class Decal;
    class NXObject;
    class _DecalBuilder;
    class DecalImpl;
    /** Represents a Material Texture decal pair  <br> Decals are not supported in KF. <br> */
    class NXOPENCPPEXPORT  Decal : public NXObject
    {
        private: DecalImpl * m_decal_impl;
        private: friend class  _DecalBuilder;
        protected: Decal();
        public: ~Decal();
    };
}
#undef EXPORTLIBRARY
#endif
