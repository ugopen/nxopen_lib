#ifndef NXOpen_FEATURES_VIRTUALBLENDEDGEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VIRTUALBLENDEDGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VirtualBlendEdgeBuilder.ja
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
#include <NXOpen/Features_VirtualBlendEdgeBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class VirtualBlendEdgeBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectNXObject;
    namespace Features
    {
        class _VirtualBlendEdgeBuilderBuilder;
        class VirtualBlendEdgeBuilderImpl;
        /** Represents a @link Features::VirtualBlendEdgeBuilder Features::VirtualBlendEdgeBuilder@endlink   <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateVirtualBlendEdgeBuilder Features::FeatureCollection::CreateVirtualBlendEdgeBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  VirtualBlendEdgeBuilder : public Features::FeatureBuilder
        {
            private: VirtualBlendEdgeBuilderImpl * m_virtualblendedgebuilder_impl;
            private: friend class  _VirtualBlendEdgeBuilderBuilder;
            protected: VirtualBlendEdgeBuilder();
            public: ~VirtualBlendEdgeBuilder();
            /**Returns  the select blend face  <br> License requirements : None */
            public: NXOpen::SelectNXObject * Selection
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
