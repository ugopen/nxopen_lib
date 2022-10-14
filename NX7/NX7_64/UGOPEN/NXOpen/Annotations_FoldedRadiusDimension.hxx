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
        /** Represents a folded radius dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateFoldedRadiusDimension Annotations::DimensionCollection::CreateFoldedRadiusDimension@endlink  <br> */
        class NXOPENCPPEXPORT FoldedRadiusDimension : public Annotations::BaseFoldedRadiusDimension
        {
            private: friend class  _FoldedRadiusDimensionBuilder;
            protected: FoldedRadiusDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif