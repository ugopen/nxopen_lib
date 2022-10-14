#ifndef NXOpen_ANNOTATIONS_VERTICALORDINATEDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_VERTICALORDINATEDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_VerticalOrdinateDimension.ja
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
#include <NXOpen/Annotations_OrdinateDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class VerticalOrdinateDimension;
    }
    namespace Annotations
    {
        class OrdinateDimension;
    }
    namespace Annotations
    {
        class _VerticalOrdinateDimensionBuilder;
        /** Represents a vertical ordinate dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateVerticalOrdinateDimension Annotations::DimensionCollection::CreateVerticalOrdinateDimension@endlink  <br> */
        class NXOPENCPPEXPORT VerticalOrdinateDimension : public Annotations::OrdinateDimension
        {
            private: friend class  _VerticalOrdinateDimensionBuilder;
            protected: VerticalOrdinateDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif