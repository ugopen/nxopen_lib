#ifndef NXOpen_ANNOTATIONS_GENERALVERTICALDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_GENERALVERTICALDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_GeneralVerticalDimension.ja
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
#include <NXOpen/Annotations_BaseVerticalDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class GeneralVerticalDimension;
    }
    namespace Annotations
    {
        class BaseVerticalDimension;
    }
    namespace Annotations
    {
        class _GeneralVerticalDimensionBuilder;
        class GeneralVerticalDimensionImpl;
        /** Represents a horizontal dimension  <br> To obtain an instance of this class use @link Annotations::DimensionCollection Annotations::DimensionCollection@endlink  <br> */
        class NXOPENCPPEXPORT  GeneralVerticalDimension : public Annotations::BaseVerticalDimension
        {
            private: GeneralVerticalDimensionImpl * m_generalverticaldimension_impl;
            private: friend class  _GeneralVerticalDimensionBuilder;
            protected: GeneralVerticalDimension();
            public: ~GeneralVerticalDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif
