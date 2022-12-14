#ifndef NXOpen_ANNOTATIONS_PMIVERTICALDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIVERTICALDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiVerticalDimension.ja
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
#include <NXOpen/Annotations_BaseVerticalDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiVerticalDimension;
    }
    namespace Annotations
    {
        class BaseVerticalDimension;
    }
    namespace Annotations
    {
        class _PmiVerticalDimensionBuilder;
        /** Represents a PMI vertical dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreatePmiVerticalDimension Annotations::DimensionCollection::CreatePmiVerticalDimension@endlink  <br> */
        class NXOPENCPPEXPORT PmiVerticalDimension : public Annotations::BaseVerticalDimension
        {
            private: friend class  _PmiVerticalDimensionBuilder;
            protected: PmiVerticalDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif
