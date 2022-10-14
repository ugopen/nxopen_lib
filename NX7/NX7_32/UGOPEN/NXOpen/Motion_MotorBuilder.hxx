#ifndef NXOpen_MOTION_MOTORBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_MOTORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_MotorBuilder.ja
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
#include <NXOpen/Motion_MotionBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class MotorBuilder;
    }
    namespace Motion
    {
        class MotionBuilder;
    }
    namespace Motion
    {
        class _MotorBuilderBuilder;
        /**  This builder class is used to create or edit @link  Motion::Motor   Motion::Motor @endlink   <br> This is an abstract class, and cannot be created. <br> */
        class NXOPENCPPEXPORT MotorBuilder : public Motion::MotionBuilder
        {
            private: friend class  _MotorBuilderBuilder;
            protected: MotorBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif