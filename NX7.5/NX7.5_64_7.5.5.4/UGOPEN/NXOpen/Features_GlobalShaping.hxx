#ifndef NXOpen_FEATURES_GLOBALSHAPING_HXX_INCLUDED
#define NXOpen_FEATURES_GLOBALSHAPING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_GlobalShaping.ja
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
        class GlobalShaping;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _GlobalShapingBuilder;
        class GlobalShapingImpl;
        /** Represents a global shaping feature */
        class NXOPENCPPEXPORT  GlobalShaping : public Features::BodyFeature
        {
            private: GlobalShapingImpl * m_globalshaping_impl;
            private: friend class  _GlobalShapingBuilder;
            protected: GlobalShaping();
            public: ~GlobalShaping();
        };
    }
}
#undef EXPORTLIBRARY
#endif
