#ifndef NXOpen_ANNOTATIONS_PMIMINORANGULARDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIMINORANGULARDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiMinorAngularDimension.ja
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
        class PmiMinorAngularDimension;
    }
    namespace Annotations
    {
        class BaseMinorAngularDimension;
    }
    namespace Annotations
    {
        class _PmiMinorAngularDimensionBuilder;
        class PmiMinorAngularDimensionImpl;
        /** Represents a PMI minor angular dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreatePmiMinorAngularDimension  Annotations::DimensionCollection::CreatePmiMinorAngularDimension @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiMinorAngularDimension : public Annotations::BaseMinorAngularDimension
        {
            private: PmiMinorAngularDimensionImpl * m_pmiminorangulardimension_impl;
            private: friend class  _PmiMinorAngularDimensionBuilder;
            protected: PmiMinorAngularDimension();
            public: ~PmiMinorAngularDimension();
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