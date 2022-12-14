#ifndef NXOpen_MOTION_POINTONSURFACE_HXX_INCLUDED
#define NXOpen_MOTION_POINTONSURFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_PointOnSurface.ja
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
        class PointOnSurface;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _PointOnSurfaceBuilder;
        /** Represents a point on surface motion object*/
        class NXOPENCPPEXPORT PointOnSurface : public Motion::MotionObject
        {
            private: friend class  _PointOnSurfaceBuilder;
            protected: PointOnSurface();
        };
    }
}
#undef EXPORTLIBRARY
#endif
