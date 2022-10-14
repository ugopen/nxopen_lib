#ifndef NXOpen_FEATURES_JOE_HXX_INCLUDED
#define NXOpen_FEATURES_JOE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Joe.ja
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
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class Joe;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _JoeBuilder;
        class JoeImpl;
        /** Represents a Joe feature */
        class NXOPENDEBUGSESSIONCPPEXPORT  Joe : public Features::BodyFeature
        {
            private: JoeImpl * m_joe_impl;
            private: friend class  _JoeBuilder;
            protected: Joe();
            public: ~Joe();
        };
    }
}
#undef EXPORTLIBRARY
#endif