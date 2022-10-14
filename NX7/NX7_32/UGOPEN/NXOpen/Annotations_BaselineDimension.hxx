#ifndef NXOpen_ANNOTATIONS_BASELINEDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_BASELINEDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_BaselineDimension.ja
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
#include <NXOpen/Annotations_DimensionSet.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class BaselineDimension;
    }
    namespace Annotations
    {
        class DimensionSet;
    }
    namespace Annotations
    {
        class _BaselineDimensionBuilder;
        /** Represents a baseline dimension. It is a set of horizontal or vertical
                dimensions.  <br> To create a new instance of this class, use @link Annotations::DimensionSetCollection::CreateHorizontalBaselineDimension Annotations::DimensionSetCollection::CreateHorizontalBaselineDimension@endlink  <br> */
        class NXOPENCPPEXPORT BaselineDimension : public Annotations::DimensionSet
        {
            private: friend class  _BaselineDimensionBuilder;
            protected: BaselineDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif