#ifndef NXOpen_ANNOTATIONS_CYLINDRICALDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_CYLINDRICALDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CylindricalDimension.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Annotations_ILinearTolerance.hxx>
#include <NXOpen/Annotations_LinearTolerance.hxx>
#include <NXOpen/Annotations_Dimension.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class CylindricalDimension;
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
    class BasePart;
    class INXObject;
    class NXObject;
    namespace Annotations
    {
        class _CylindricalDimensionBuilder;
        /** Represents a cylindrical dimension */
        class NXOPENCPPEXPORT CylindricalDimension : public Annotations::Dimension, public virtual Annotations::ILinearTolerance
        {
            private: friend class  _CylindricalDimensionBuilder;
            protected: CylindricalDimension();
            /** Returns the tolerance  @return   <br> License requirements : None */
            public: virtual NXOpen::Annotations::LinearTolerance * GetTolerance
            (
            );
            /** Sets the tolerance  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetTolerance
            (
                NXOpen::Annotations::LinearTolerance * tolerance /** */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
