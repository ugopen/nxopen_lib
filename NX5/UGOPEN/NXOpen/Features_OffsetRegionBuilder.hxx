#ifndef NXOpen_FEATURES_OFFSETREGIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_OFFSETREGIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_OffsetRegionBuilder.ja
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
#include <NXOpen/Features_OffsetRegionBuilder.hxx>
#include <NXOpen/ModlDirect_SelectBlend.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class OffsetRegionBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace ModlDirect
    {
        class SelectBlend;
    }
    class ScCollector;
    namespace Features
    {
        class _OffsetRegionBuilderBuilder;
        /**
            Represents a builder for an offset region feature, don't use it until nx502.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateOffsetRegionBuilder Features::FeatureCollection::CreateOffsetRegionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT OffsetRegionBuilder : public Features::FeatureBuilder
        {
            private: friend class  _OffsetRegionBuilderBuilder;
            protected: OffsetRegionBuilder();
            /**Returns  the face to offset, don't use it until nx502  <br> License requirements : None */
            public: NXOpen::ScCollector * Face
            (
            );
            /**Returns  the distance to offset, don't use it until nx502  <br> License requirements : None */
            public: NXOpen::Expression * Distance
            (
            );
            /**Returns  the direction of offset, don't use it until nx502  <br> License requirements : None */
            public: bool Direction
            (
            );
            /**Sets  the direction of offset, don't use it until nx502  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDirection
            (
                bool direction /** direction */ 
            );
            /**Returns  the adjacent blend face to offset, don't use it until nx502  <br> License requirements : None */
            public: NXOpen::ModlDirect::SelectBlend * BlendFace
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
