#ifndef NXOpen_MOTION_COUPLER_HXX_INCLUDED
#define NXOpen_MOTION_COUPLER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_Coupler.ja
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
#include <NXOpen/Motion_MotionObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class Coupler;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _CouplerBuilder;
        /** Represents a motion coupler object  <br> This is an abstract class, and cannot be created. <br> */
        class NXOPENCPPEXPORT Coupler : public Motion::MotionObject
        {
            private: friend class  _CouplerBuilder;
            protected: Coupler();
        };
    }
}
#undef EXPORTLIBRARY
#endif