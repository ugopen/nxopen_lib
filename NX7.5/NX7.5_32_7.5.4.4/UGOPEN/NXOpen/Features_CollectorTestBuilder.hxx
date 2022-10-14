#ifndef NXOpen_FEATURES_COLLECTORTESTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_COLLECTORTESTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CollectorTestBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_CollectorTestBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class CollectorTestBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _CollectorTestBuilderBuilder;
        class CollectorTestBuilderImpl;
        /**
            Represents a Features.CollectorTestBuilder builder
            */
        class NXOPENDEBUGSESSIONCPPEXPORT  CollectorTestBuilder : public Features::FeatureBuilder
        {
            private: CollectorTestBuilderImpl * m_collectortestbuilder_impl;
            private: friend class  _CollectorTestBuilderBuilder;
            protected: CollectorTestBuilder();
            public: ~CollectorTestBuilder();
            /**Returns  the collector  <br> License requirements : None */
            public: NXOpen::ScCollector * Collector
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif