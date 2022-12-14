#ifndef NXOpen_ANNOTATIONS_PMIRADIUSDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIRADIUSDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiRadiusDimension.ja
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
#include <NXOpen/Annotations_BaseRadiusDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiRadiusDimension;
    }
    namespace Annotations
    {
        class BaseRadiusDimension;
    }
    namespace Annotations
    {
        class _PmiRadiusDimensionBuilder;
        /** Represents a PMI radius dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreatePmiRadiusDimension Annotations::DimensionCollection::CreatePmiRadiusDimension@endlink  <br> */
        class NXOPENCPPEXPORT PmiRadiusDimension : public Annotations::BaseRadiusDimension
        {
            private: friend class  _PmiRadiusDimensionBuilder;
            protected: PmiRadiusDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif
