#ifndef NXOpen_MOTION_SCALARFORCE_HXX_INCLUDED
#define NXOpen_MOTION_SCALARFORCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_ScalarForce.ja
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
        class ScalarForce;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _ScalarForceBuilder;
        class ScalarForceImpl;
        /** Represents the Motion ScalarForce class. */
        class NXOPENCPPEXPORT  ScalarForce : public Motion::MotionObject
        {
            private: ScalarForceImpl * m_scalarforce_impl;
            private: friend class  _ScalarForceBuilder;
            protected: ScalarForce();
            public: ~ScalarForce();
        };
    }
}
#undef EXPORTLIBRARY
#endif
