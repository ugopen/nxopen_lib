#ifndef NXOpen_ANNOTATIONS_GENERALMINORANGULARDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_GENERALMINORANGULARDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_GeneralMinorAngularDimension.ja
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
#include <NXOpen/Annotations_BaseMinorAngularDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class GeneralMinorAngularDimension;
    }
    namespace Annotations
    {
        class BaseMinorAngularDimension;
    }
    namespace Annotations
    {
        class _GeneralMinorAngularDimensionBuilder;
        /** Represents a minor angular dimension  <br> To obtain an instance of this class use @link Annotations::DimensionCollection Annotations::DimensionCollection@endlink  <br> */
        class NXOPENCPPEXPORT GeneralMinorAngularDimension : public Annotations::BaseMinorAngularDimension
        {
            private: friend class  _GeneralMinorAngularDimensionBuilder;
            protected: GeneralMinorAngularDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif
