#ifndef NXOpen_SPLINE_HXX_INCLUDED
#define NXOpen_SPLINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Spline.ja
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
#include <NXOpen/Curve.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Spline;
    class Curve;
    class _SplineBuilder;
    /** Represents a spline curve.  <br> To create an instance of this object cannot be created at this time. <br> */
    class NXOPENCPPEXPORT Spline : public Curve
    {
        private: friend class  _SplineBuilder;
        protected: Spline();
    };
}
#undef EXPORTLIBRARY
#endif
