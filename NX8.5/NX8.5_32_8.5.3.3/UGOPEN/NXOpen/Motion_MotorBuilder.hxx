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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Motion_MotionBuilder.hxx>
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
        class MotorBuilder;
    }
    namespace Motion
    {
        class MotionBuilder;
    }
    namespace Motion
    {
        class _MotorBuilderBuilder;
        class MotorBuilderImpl;
        /**  This builder class is used to create or edit @link  Motion::Motor   Motion::Motor @endlink   <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  MotorBuilder : public Motion::MotionBuilder
        {
            private: MotorBuilderImpl * m_motorbuilder_impl;
            private: friend class  _MotorBuilderBuilder;
            protected: MotorBuilder();
            public: ~MotorBuilder();
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
