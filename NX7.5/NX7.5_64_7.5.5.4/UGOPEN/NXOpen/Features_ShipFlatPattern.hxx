#ifndef NXOpen_FEATURES_SHIPFLATPATTERN_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPFLATPATTERN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipFlatPattern.ja
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
        class ShipFlatPattern;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _ShipFlatPatternBuilder;
        class ShipFlatPatternImpl;
        /** Represents a ship flat pattern feature */
        class NXOPENCPPEXPORT  ShipFlatPattern : public Features::BodyFeature
        {
            private: ShipFlatPatternImpl * m_shipflatpattern_impl;
            private: friend class  _ShipFlatPatternBuilder;
            protected: ShipFlatPattern();
            public: ~ShipFlatPattern();
        };
    }
}
#undef EXPORTLIBRARY
#endif
