#ifndef NXOpen_ANNOTATIONS_GENERALHORIZONTALDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_GENERALHORIZONTALDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_GeneralHorizontalDimension.ja
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
#include <NXOpen/Annotations_BaseHorizontalDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class GeneralHorizontalDimension;
    }
    namespace Annotations
    {
        class BaseHorizontalDimension;
    }
    namespace Annotations
    {
        class _GeneralHorizontalDimensionBuilder;
        class GeneralHorizontalDimensionImpl;
        /** Represents a horizontal dimension  <br> To obtain an instance of this class use @link Annotations::DimensionCollection Annotations::DimensionCollection@endlink  <br> */
        class NXOPENCPPEXPORT  GeneralHorizontalDimension : public Annotations::BaseHorizontalDimension
        {
            private: GeneralHorizontalDimensionImpl * m_generalhorizontaldimension_impl;
            private: friend class  _GeneralHorizontalDimensionBuilder;
            protected: GeneralHorizontalDimension();
            public: ~GeneralHorizontalDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif