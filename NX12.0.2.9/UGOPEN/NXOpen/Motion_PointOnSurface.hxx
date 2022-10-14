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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Motion_IGraphSource.hxx>
#include <NXOpen/Motion_MotionObject.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class PointOnSurface;
    }
    namespace Motion
    {
        class IGraphSource;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _PointOnSurfaceBuilder;
        class PointOnSurfaceImpl;
        /** Represents a point on surface motion object <br> To create or edit an instance of this class, use @link NXOpen::Motion::PointOnSurfaceBuilder  NXOpen::Motion::PointOnSurfaceBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  PointOnSurface : public NXOpen::Motion::MotionObject, public virtual NXOpen::Motion::IGraphSource
        {
            private: PointOnSurfaceImpl * m_pointonsurface_impl;
            private: friend class  _PointOnSurfaceBuilder;
            protected: PointOnSurface();
            public: ~PointOnSurface();
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif