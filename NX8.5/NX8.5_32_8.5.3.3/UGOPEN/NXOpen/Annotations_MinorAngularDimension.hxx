#ifndef NXOpen_ANNOTATIONS_MINORANGULARDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_MINORANGULARDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_MinorAngularDimension.ja
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
#include <NXOpen/Annotations_BaseMinorAngularDimension.hxx>
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
        class MinorAngularDimension;
    }
    namespace Annotations
    {
        class BaseMinorAngularDimension;
    }
    namespace Annotations
    {
        class _MinorAngularDimensionBuilder;
        class MinorAngularDimensionImpl;
        /** Represents a minor angular dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateMinorAngularDimension  Annotations::DimensionCollection::CreateMinorAngularDimension @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  MinorAngularDimension : public Annotations::BaseMinorAngularDimension
        {
            private: MinorAngularDimensionImpl * m_minorangulardimension_impl;
            private: friend class  _MinorAngularDimensionBuilder;
            protected: MinorAngularDimension();
            public: ~MinorAngularDimension();
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
