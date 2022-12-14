#ifndef NXOpen_ANNOTATIONS_GENERALCYLINDRICALDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_GENERALCYLINDRICALDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_GeneralCylindricalDimension.ja
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
#include <NXOpen/Annotations_BaseCylindricalDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class GeneralCylindricalDimension;
    }
    namespace Annotations
    {
        class BaseCylindricalDimension;
    }
    namespace Annotations
    {
        class _GeneralCylindricalDimensionBuilder;
        /** Represents a horizontal dimension  <br> To obtain an instance of this class use @link Annotations::DimensionCollection Annotations::DimensionCollection@endlink  <br> */
        class NXOPENCPPEXPORT GeneralCylindricalDimension : public Annotations::BaseCylindricalDimension
        {
            private: friend class  _GeneralCylindricalDimensionBuilder;
            protected: GeneralCylindricalDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif
