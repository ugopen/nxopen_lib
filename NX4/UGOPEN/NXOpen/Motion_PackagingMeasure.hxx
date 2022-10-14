#ifndef NXOpen_MOTION_PACKAGINGMEASURE_HXX_INCLUDED
#define NXOpen_MOTION_PACKAGINGMEASURE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_PackagingMeasure.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Motion_Packaging.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class PackagingMeasure;
    }
    namespace Motion
    {
        class Packaging;
    }
    namespace Motion
    {
        class _PackagingMeasureBuilder;
        /** This class represents a Packaging Measure object.  A Measure object
            is used to define a request to measure minimum distances or angles
            between sets of moving objects in a mechanism. */
        class NXOPENCPPEXPORT PackagingMeasure : public Motion::Packaging
        {
            private: friend class  _PackagingMeasureBuilder;
            protected: PackagingMeasure();
        };
    }
}
#undef EXPORTLIBRARY
#endif