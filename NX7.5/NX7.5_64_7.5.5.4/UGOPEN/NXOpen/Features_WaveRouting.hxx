#ifndef NXOpen_FEATURES_WAVEROUTING_HXX_INCLUDED
#define NXOpen_FEATURES_WAVEROUTING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_WaveRouting.ja
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
        class WaveRouting;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class _WaveRoutingBuilder;
        class WaveRoutingImpl;
        /** Represents a waverouting feature */
        class NXOPENCPPEXPORT  WaveRouting : public Features::Feature
        {
            private: WaveRoutingImpl * m_waverouting_impl;
            private: friend class  _WaveRoutingBuilder;
            protected: WaveRouting();
            public: ~WaveRouting();
        };
    }
}
#undef EXPORTLIBRARY
#endif
