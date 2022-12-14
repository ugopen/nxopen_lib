#ifndef NXOpen_FEATURES_KNUCKLEDPROFILES_HXX_INCLUDED
#define NXOpen_FEATURES_KNUCKLEDPROFILES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_KnuckledProfiles.ja
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
        class KnuckledProfiles;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _KnuckledProfilesBuilder;
        class KnuckledProfilesImpl;
        /** Represents a knuckled profiles manufacturing preparation feature */
        class NXOPENCPPEXPORT  KnuckledProfiles : public Features::BodyFeature
        {
            private: KnuckledProfilesImpl * m_knuckledprofiles_impl;
            private: friend class  _KnuckledProfilesBuilder;
            protected: KnuckledProfiles();
            public: ~KnuckledProfiles();
        };
    }
}
#undef EXPORTLIBRARY
#endif
