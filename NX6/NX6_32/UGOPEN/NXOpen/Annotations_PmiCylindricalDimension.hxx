#ifndef NXOpen_ANNOTATIONS_PMICYLINDRICALDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMICYLINDRICALDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiCylindricalDimension.ja
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
        class PmiCylindricalDimension;
    }
    namespace Annotations
    {
        class BaseCylindricalDimension;
    }
    namespace Annotations
    {
        class _PmiCylindricalDimensionBuilder;
        /** Represents a PMI cylindrical dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreatePmiCylindricalDimension Annotations::DimensionCollection::CreatePmiCylindricalDimension@endlink  <br> */
        class NXOPENCPPEXPORT PmiCylindricalDimension : public Annotations::BaseCylindricalDimension
        {
            private: friend class  _PmiCylindricalDimensionBuilder;
            protected: PmiCylindricalDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif
