#ifndef NXOpen_MOTION_POINTONCURVE_HXX_INCLUDED
#define NXOpen_MOTION_POINTONCURVE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_PointOnCurve.ja
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
#include <NXOpen/Motion_MotionObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class PointOnCurve;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _PointOnCurveBuilder;
        class PointOnCurveImpl;
        /** Represents a point on curve */
        class NXOPENCPPEXPORT  PointOnCurve : public Motion::MotionObject
        {
            private: PointOnCurveImpl * m_pointoncurve_impl;
            private: friend class  _PointOnCurveBuilder;
            protected: PointOnCurve();
            public: ~PointOnCurve();
        };
    }
}
#undef EXPORTLIBRARY
#endif