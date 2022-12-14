#ifndef NXOpen_FEATURES_ZFRAMEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_ZFRAMEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ZFrameBuilder.ja
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
#include <NXOpen/Features_TransFrameBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ZFrameBuilder;
    }
    namespace Features
    {
        class TransFrameBuilder;
    }
    namespace Features
    {
        class _ZFrameBuilderBuilder;
        /**
            Represents a @link Features::ZFrameBuilder Features::ZFrameBuilder@endlink  
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateZFrameBuilder Features::FeatureCollection::CreateZFrameBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ZFrameBuilder : public Features::TransFrameBuilder
        {
            private: friend class  _ZFrameBuilderBuilder;
            protected: ZFrameBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif
