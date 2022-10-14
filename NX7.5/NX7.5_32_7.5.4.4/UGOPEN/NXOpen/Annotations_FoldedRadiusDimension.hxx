#ifndef NXOpen_ANNOTATIONS_FOLDEDRADIUSDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_FOLDEDRADIUSDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_FoldedRadiusDimension.ja
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
#include <NXOpen/Annotations_BaseFoldedRadiusDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class FoldedRadiusDimension;
    }
    namespace Annotations
    {
        class BaseFoldedRadiusDimension;
    }
    namespace Annotations
    {
        class _FoldedRadiusDimensionBuilder;
        class FoldedRadiusDimensionImpl;
        /** Represents a folded radius dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateFoldedRadiusDimension Annotations::DimensionCollection::CreateFoldedRadiusDimension@endlink  <br> */
        class NXOPENCPPEXPORT  FoldedRadiusDimension : public Annotations::BaseFoldedRadiusDimension
        {
            private: FoldedRadiusDimensionImpl * m_foldedradiusdimension_impl;
            private: friend class  _FoldedRadiusDimensionBuilder;
            protected: FoldedRadiusDimension();
            public: ~FoldedRadiusDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif