#ifndef NXOpen_ANNOTATIONS_MAJORANGULARDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_MAJORANGULARDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_MajorAngularDimensionBuilder.ja
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
#include <NXOpen/Annotations_AngularDimensionBuilder.hxx>
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
        class MajorAngularDimensionBuilder;
    }
    namespace Annotations
    {
        class AngularDimensionBuilder;
    }
    namespace Annotations
    {
        class _MajorAngularDimensionBuilderBuilder;
        class MajorAngularDimensionBuilderImpl;
        /** Represents a @link Annotations::AngularDimension Annotations::AngularDimension@endlink  builder  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateMajorAngularDimensionBuilder  Annotations::DimensionCollection::CreateMajorAngularDimensionBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  MajorAngularDimensionBuilder : public Annotations::AngularDimensionBuilder
        {
            private: MajorAngularDimensionBuilderImpl * m_majorangulardimensionbuilder_impl;
            private: friend class  _MajorAngularDimensionBuilderBuilder;
            protected: MajorAngularDimensionBuilder();
            public: ~MajorAngularDimensionBuilder();
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
