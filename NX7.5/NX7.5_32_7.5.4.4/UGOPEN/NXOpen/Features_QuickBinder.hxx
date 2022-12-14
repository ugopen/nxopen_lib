#ifndef NXOpen_FEATURES_QUICKBINDER_HXX_INCLUDED
#define NXOpen_FEATURES_QUICKBINDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_QuickBinder.ja
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
        class QuickBinder;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _QuickBinderBuilder;
        class QuickBinderImpl;
        /** Represents a quick binder feature */
        class NXOPENCPPEXPORT  QuickBinder : public Features::BodyFeature
        {
            private: QuickBinderImpl * m_quickbinder_impl;
            private: friend class  _QuickBinderBuilder;
            protected: QuickBinder();
            public: ~QuickBinder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
