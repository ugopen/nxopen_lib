#ifndef NXOpen_ANNOTATIONS_RADIUSDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_RADIUSDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_RadiusDimension.ja
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
#include <NXOpen/Annotations_BaseRadiusDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class RadiusDimension;
    }
    namespace Annotations
    {
        class BaseRadiusDimension;
    }
    namespace Annotations
    {
        class _RadiusDimensionBuilder;
        class RadiusDimensionImpl;
        /** Represents a radius dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateRadiusDimension Annotations::DimensionCollection::CreateRadiusDimension@endlink  <br> */
        class NXOPENCPPEXPORT  RadiusDimension : public Annotations::BaseRadiusDimension
        {
            private: RadiusDimensionImpl * m_radiusdimension_impl;
            private: friend class  _RadiusDimensionBuilder;
            protected: RadiusDimension();
            public: ~RadiusDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif