#ifndef NXOpen_MOTION_COUPLERCABLE_HXX_INCLUDED
#define NXOpen_MOTION_COUPLERCABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_CouplerCable.ja
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
#include <NXOpen/Motion_Coupler.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class CouplerCable;
    }
    namespace Motion
    {
        class Coupler;
    }
    namespace Motion
    {
        class _CouplerCableBuilder;
        /** Represents a motion cable object */
        class NXOPENCPPEXPORT CouplerCable : public Motion::Coupler
        {
            private: friend class  _CouplerCableBuilder;
            protected: CouplerCable();
        };
    }
}
#undef EXPORTLIBRARY
#endif
