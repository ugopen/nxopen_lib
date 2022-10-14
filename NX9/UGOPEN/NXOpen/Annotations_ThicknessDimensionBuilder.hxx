#ifndef NXOpen_ANNOTATIONS_THICKNESSDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_THICKNESSDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ThicknessDimensionBuilder.ja
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
#include <NXOpen/Annotations_BaseThicknessDimensionBuilder.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class ThicknessDimensionBuilder;
    }
    namespace Annotations
    {
        class BaseThicknessDimensionBuilder;
    }
    namespace Annotations
    {
        class _ThicknessDimensionBuilderBuilder;
        class ThicknessDimensionBuilderImpl;
        /** Represents a @link Annotations::ConcentricCircleDimension Annotations::ConcentricCircleDimension@endlink  builder  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateThicknessDimensionBuilder  Annotations::DimensionCollection::CreateThicknessDimensionBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  ThicknessDimensionBuilder : public Annotations::BaseThicknessDimensionBuilder
        {
            private: ThicknessDimensionBuilderImpl * m_thicknessdimensionbuilder_impl;
            private: friend class  _ThicknessDimensionBuilderBuilder;
            protected: ThicknessDimensionBuilder();
            public: ~ThicknessDimensionBuilder();
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif