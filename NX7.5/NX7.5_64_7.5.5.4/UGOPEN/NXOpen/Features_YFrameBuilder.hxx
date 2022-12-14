#ifndef NXOpen_FEATURES_YFRAMEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_YFRAMEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_YFrameBuilder.ja
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
#include <NXOpen/Features_TransFrameBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class YFrameBuilder;
    }
    namespace Features
    {
        class TransFrameBuilder;
    }
    namespace Features
    {
        class _YFrameBuilderBuilder;
        class YFrameBuilderImpl;
        /**
            Represents a @link Features::YFrameBuilder Features::YFrameBuilder@endlink  
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateYFrameBuilder Features::FeatureCollection::CreateYFrameBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  YFrameBuilder : public Features::TransFrameBuilder
        {
            private: YFrameBuilderImpl * m_yframebuilder_impl;
            private: friend class  _YFrameBuilderBuilder;
            protected: YFrameBuilder();
            public: ~YFrameBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
