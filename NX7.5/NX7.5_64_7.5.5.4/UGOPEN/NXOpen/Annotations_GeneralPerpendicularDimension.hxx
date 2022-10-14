#ifndef NXOpen_ANNOTATIONS_GENERALPERPENDICULARDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_GENERALPERPENDICULARDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_GeneralPerpendicularDimension.ja
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
#include <NXOpen/Annotations_BasePerpendicularDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class GeneralPerpendicularDimension;
    }
    namespace Annotations
    {
        class BasePerpendicularDimension;
    }
    namespace Annotations
    {
        class _GeneralPerpendicularDimensionBuilder;
        class GeneralPerpendicularDimensionImpl;
        /** Represents a horizontal dimension  <br> To obtain an instance of this class use @link Annotations::DimensionCollection Annotations::DimensionCollection@endlink  <br> */
        class NXOPENCPPEXPORT  GeneralPerpendicularDimension : public Annotations::BasePerpendicularDimension
        {
            private: GeneralPerpendicularDimensionImpl * m_generalperpendiculardimension_impl;
            private: friend class  _GeneralPerpendicularDimensionBuilder;
            protected: GeneralPerpendicularDimension();
            public: ~GeneralPerpendicularDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif