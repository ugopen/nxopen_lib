#ifndef NXOpen_WELD_WELDBEAD_HXX_INCLUDED
#define NXOpen_WELD_WELDBEAD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_WeldBead.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Weld
    {
        class WeldBead;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Weld
    {
        class _WeldBeadBuilder;
        class WeldBeadImpl;
        /** Represents a Weld Bead feature */
        class NXOPENCPPEXPORT  WeldBead : public Features::Feature
        {
            private: WeldBeadImpl * m_weldbead_impl;
            private: friend class  _WeldBeadBuilder;
            protected: WeldBead();
            public: ~WeldBead();
        };
    }
}
#undef EXPORTLIBRARY
#endif
