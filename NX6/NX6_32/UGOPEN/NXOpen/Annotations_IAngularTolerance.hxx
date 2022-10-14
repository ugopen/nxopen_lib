#ifndef NXOpen_ANNOTATIONS_IANGULARTOLERANCE_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_IANGULARTOLERANCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_IAngularTolerance.ja
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
#include <NXOpen/Annotations_AngularTolerance.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class IAngularTolerance;
    }
    namespace Annotations
    {
        class AngularTolerance;
    }
    class INXObject;
    namespace Annotations
    {
        /** Represents an object that has angular tolerance */
        class NXOPENCPPEXPORT IAngularTolerance : public virtual INXObject
        {
            /** Returns the tolerance  @return   <br> License requirements : None */
            public: virtual NXOpen::Annotations::AngularTolerance * GetTolerance
            (
            ) = 0;
            /** Sets the tolerance  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetTolerance
            (
                NXOpen::Annotations::AngularTolerance * tolerances /** tolerances */ 
            ) = 0;
        };
    }
}
#undef EXPORTLIBRARY
#endif