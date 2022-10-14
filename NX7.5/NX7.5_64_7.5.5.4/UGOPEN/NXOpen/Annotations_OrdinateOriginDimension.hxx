#ifndef NXOpen_ANNOTATIONS_ORDINATEORIGINDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ORDINATEORIGINDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_OrdinateOriginDimension.ja
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
#include <NXOpen/Annotations_Dimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class OrdinateOriginDimension;
    }
    namespace Annotations
    {
        class Dimension;
    }
    namespace Annotations
    {
        class _OrdinateOriginDimensionBuilder;
        class OrdinateOriginDimensionImpl;
        /** Represents an ordinate origin dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateOrdinateOriginDimension Annotations::DimensionCollection::CreateOrdinateOriginDimension@endlink  <br> */
        class NXOPENCPPEXPORT  OrdinateOriginDimension : public Annotations::Dimension
        {
            private: OrdinateOriginDimensionImpl * m_ordinateorigindimension_impl;
            private: friend class  _OrdinateOriginDimensionBuilder;
            protected: OrdinateOriginDimension();
            public: ~OrdinateOriginDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif