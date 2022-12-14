#ifndef NXOpen_FEATURES_SOLIDPUNCH_HXX_INCLUDED
#define NXOpen_FEATURES_SOLIDPUNCH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SolidPunch.ja
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
    namespace Features
    {
        class SolidPunch;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _SolidPunchBuilder;
        class SolidPunchImpl;
        /** Represents a Solid Punch feature */
        class NXOPENCPPEXPORT  SolidPunch : public Features::Feature
        {
            private: SolidPunchImpl * m_solidpunch_impl;
            private: friend class  _SolidPunchBuilder;
            protected: SolidPunch();
            public: ~SolidPunch();
        };
    }
}
#undef EXPORTLIBRARY
#endif
