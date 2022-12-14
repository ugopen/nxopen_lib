#ifndef NXOpen_ANNOTATIONS_PMIDIAMETERDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIDIAMETERDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiDiameterDimension.ja
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
#include <NXOpen/Annotations_BaseDiameterDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiDiameterDimension;
    }
    namespace Annotations
    {
        class BaseDiameterDimension;
    }
    namespace Annotations
    {
        class _PmiDiameterDimensionBuilder;
        /** Represents a PMI diameter dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreatePmiDiameterDimension Annotations::DimensionCollection::CreatePmiDiameterDimension@endlink  <br> */
        class NXOPENCPPEXPORT PmiDiameterDimension : public Annotations::BaseDiameterDimension
        {
            private: friend class  _PmiDiameterDimensionBuilder;
            protected: PmiDiameterDimension();
        };
    }
}
#undef EXPORTLIBRARY
#endif
