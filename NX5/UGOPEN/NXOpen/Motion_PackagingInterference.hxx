#ifndef NXOpen_MOTION_PACKAGINGINTERFERENCE_HXX_INCLUDED
#define NXOpen_MOTION_PACKAGINGINTERFERENCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_PackagingInterference.ja
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
#include <NXOpen/Motion_Packaging.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class PackagingInterference;
    }
    namespace Motion
    {
        class Packaging;
    }
    namespace Motion
    {
        class _PackagingInterferenceBuilder;
        /** This class represents a Packaging Interference object.
            An Interference object is used to define a request to check for
            interference between sets of moving bodies in a mechanism. */
        class NXOPENCPPEXPORT PackagingInterference : public Motion::Packaging
        {
            private: friend class  _PackagingInterferenceBuilder;
            protected: PackagingInterference();
        };
    }
}
#undef EXPORTLIBRARY
#endif
