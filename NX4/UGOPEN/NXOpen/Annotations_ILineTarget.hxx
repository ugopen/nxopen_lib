#ifndef NXOpen_ANNOTATIONS_ILINETARGET_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ILINETARGET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ILineTarget.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class ILineTarget;
    }
    class INXObject;
    namespace Annotations
    {
        /** Represents interface class for line datum target */
        class NXOPENCPPEXPORT ILineTarget : public virtual INXObject
        {
            /**Returns  the target start point coordinates  <br> License requirements : None */
            public: virtual NXOpen::Point3d StartPointCoordinates
            (
            ) = 0;
            /**Returns  the target end point coordinates  <br> License requirements : None */
            public: virtual NXOpen::Point3d EndPointCoordinates
            (
            ) = 0;
        };
    }
}
#undef EXPORTLIBRARY
#endif