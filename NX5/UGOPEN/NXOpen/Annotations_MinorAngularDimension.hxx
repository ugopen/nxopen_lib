#ifndef NXOpen_ANNOTATIONS_MINORANGULARDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_MINORANGULARDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_MinorAngularDimension.ja
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
#include <NXOpen/Annotations_AngularDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class MinorAngularDimension;
    }
    namespace Annotations
    {
        class AngularDimension;
    }
    namespace Annotations
    {
        class _MinorAngularDimensionBuilder;
        /** Represents a minor angular dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateMinorAngularDimension Annotations::DimensionCollection::CreateMinorAngularDimension@endlink  <br> */
        class NXOPENCPPEXPORT MinorAngularDimension : public Annotations::AngularDimension
        {
            private: friend class  _MinorAngularDimensionBuilder;
            protected: MinorAngularDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif
