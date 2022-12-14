#ifndef NXOpen_FEATURES_SECTIONINERTIAANALYSIS_HXX_INCLUDED
#define NXOpen_FEATURES_SECTIONINERTIAANALYSIS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SectionInertiaAnalysis.ja
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
        class SectionInertiaAnalysis;
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        class _SectionInertiaAnalysisBuilder;
        class SectionInertiaAnalysisImpl;
        /** Represents a section inertia analysis feature */
        class NXOPENCPPEXPORT  SectionInertiaAnalysis : public Features::BodyFeature
        {
            private: SectionInertiaAnalysisImpl * m_sectioninertiaanalysis_impl;
            private: friend class  _SectionInertiaAnalysisBuilder;
            protected: SectionInertiaAnalysis();
            public: ~SectionInertiaAnalysis();
        };
    }
}
#undef EXPORTLIBRARY
#endif
