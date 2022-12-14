#ifndef NXOpen_FEATURES_SHIPENDCUT_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPENDCUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipEndCut.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ShipEndCut;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _ShipEndCutBuilder;
        class ShipEndCutImpl;
        /** Represents a ship end cut feature */
        class NXOPENCPPEXPORT  ShipEndCut : public Features::BodyFeature
        {
            private: ShipEndCutImpl * m_shipendcut_impl;
            private: friend class  _ShipEndCutBuilder;
            protected: ShipEndCut();
            public: ~ShipEndCut();
        };
    }
}
#undef EXPORTLIBRARY
#endif
