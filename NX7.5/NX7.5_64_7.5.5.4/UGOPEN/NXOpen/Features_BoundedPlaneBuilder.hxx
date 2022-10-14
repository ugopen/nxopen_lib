#ifndef NXOpen_FEATURES_BOUNDEDPLANEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_BOUNDEDPLANEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_BoundedPlaneBuilder.ja
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
#include <NXOpen/Features_BoundedPlaneBuilder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class BoundedPlaneBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class Section;
    namespace Features
    {
        class _BoundedPlaneBuilderBuilder;
        class BoundedPlaneBuilderImpl;
        /**
            Represents a @link Features::BoundedPlane Features::BoundedPlane@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateBoundedPlaneBuilder Features::FeatureCollection::CreateBoundedPlaneBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  BoundedPlaneBuilder : public Features::FeatureBuilder
        {
            private: BoundedPlaneBuilderImpl * m_boundedplanebuilder_impl;
            private: friend class  _BoundedPlaneBuilderBuilder;
            protected: BoundedPlaneBuilder();
            public: ~BoundedPlaneBuilder();
            /**Returns  the bounding curves  <br> License requirements : None */
            public: NXOpen::Section * BoundingCurves
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif