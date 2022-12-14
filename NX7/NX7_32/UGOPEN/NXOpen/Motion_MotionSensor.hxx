#ifndef NXOpen_MOTION_MOTIONSENSOR_HXX_INCLUDED
#define NXOpen_MOTION_MOTIONSENSOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_MotionSensor.ja
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
        class MotionSensor;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _MotionSensorBuilder;
        /** Represents a motion sensor */
        class NXOPENCPPEXPORT MotionSensor : public Motion::MotionObject
        {
            private: friend class  _MotionSensorBuilder;
            protected: MotionSensor();
        };
    }
}
#undef EXPORTLIBRARY
#endif
