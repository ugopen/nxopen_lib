#ifndef NXOpen_MOTION_BUSHING_HXX_INCLUDED
#define NXOpen_MOTION_BUSHING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_Bushing.ja
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
        class Bushing;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _BushingBuilder;
        /** Represents a bushing */
        class NXOPENCPPEXPORT Bushing : public Motion::MotionObject
        {
            private: friend class  _BushingBuilder;
            protected: Bushing();
        };
    }
}
#undef EXPORTLIBRARY
#endif