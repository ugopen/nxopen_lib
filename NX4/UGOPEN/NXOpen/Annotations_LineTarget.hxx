#ifndef NXOpen_ANNOTATIONS_LINETARGET_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_LINETARGET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_LineTarget.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Annotations_ILineTarget.hxx>
#include <NXOpen/Annotations_DatumTarget.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class LineTarget;
    }
    namespace Annotations
    {
        class DatumTarget;
    }
    namespace Annotations
    {
        class ILineTarget;
    }
    class BasePart;
    class INXObject;
    class NXObject;
    namespace Annotations
    {
        class _LineTargetBuilder;
        /** Represents a line datum target */
        class NXOPENCPPEXPORT LineTarget : public Annotations::DatumTarget, public virtual Annotations::ILineTarget
        {
            private: friend class  _LineTargetBuilder;
            protected: LineTarget();
            /**Returns  the target start point coordinates  <br> License requirements : None */
            public: virtual NXOpen::Point3d StartPointCoordinates
            (
            );
            /**Returns  the target end point coordinates  <br> License requirements : None */
            public: virtual NXOpen::Point3d EndPointCoordinates
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
