#ifndef NXOpen_FEATURES_RESIZEBLENDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_RESIZEBLENDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ResizeBlendBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_ResizeBlendBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ResizeBlendBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _ResizeBlendBuilderBuilder;
        /**
            Represents a builder for a resize blend feature, don't use it until nx502.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateResizeBlendBuilder Features::FeatureCollection::CreateResizeBlendBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ResizeBlendBuilder : public Features::FeatureBuilder
        {
            private: friend class  _ResizeBlendBuilderBuilder;
            protected: ResizeBlendBuilder();
            /**Returns  the blend faces collector, don't use it until nx502  <br> License requirements : None */
            public: NXOpen::ScCollector * BlendFace
            (
            );
            /**Returns  the blend radius, don't use it until nx502  <br> License requirements : None */
            public: NXOpen::Expression * Radius
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif