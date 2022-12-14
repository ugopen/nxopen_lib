#ifndef NXOpen_ANNOTATIONS_PARALLELDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PARALLELDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ParallelDimension.ja
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
#include <NXOpen/Annotations_ILinearTolerance.hxx>
#include <NXOpen/Annotations_LinearTolerance.hxx>
#include <NXOpen/Annotations_Dimension.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class ParallelDimension;
    }
    namespace Annotations
    {
        class Dimension;
    }
    namespace Annotations
    {
        class ILinearTolerance;
    }
    namespace Annotations
    {
        class LinearTolerance;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _ParallelDimensionBuilder;
        /** Represents a parallel dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreateParallelDimension Annotations::DimensionCollection::CreateParallelDimension@endlink  <br> */
        class NXOPENCPPEXPORT ParallelDimension : public Annotations::Dimension, public virtual Annotations::ILinearTolerance
        {
            private: friend class  _ParallelDimensionBuilder;
            protected: ParallelDimension();
            /** Returns the tolerance  @return   <br> License requirements : None */
            public: virtual NXOpen::Annotations::LinearTolerance * GetTolerance
            (
            );
            /** Sets the tolerance  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetTolerance
            (
                NXOpen::Annotations::LinearTolerance * tolerance /** tolerance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
