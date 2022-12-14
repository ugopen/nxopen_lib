#ifndef NXOpen_FEATURES_SKETCHFEATURE_HXX_INCLUDED
#define NXOpen_FEATURES_SKETCHFEATURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SketchFeature.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class SketchFeature;
    }
    namespace Features
    {
        class Feature;
    }
    class Sketch;
    namespace Features
    {
        class _SketchFeatureBuilder;
        /** Represents a sketch feature  <br> This is an abstract class, and cannot be instantiated <br> */
        class NXOPENCPPEXPORT SketchFeature : public Features::Feature
        {
            private: friend class  _SketchFeatureBuilder;
            protected: SketchFeature();
            /**Returns  the sketch that is owned by this feature  <br> License requirements : None */
            public: NXOpen::Sketch * Sketch
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
