#ifndef NXOpen_MOTION_DISCRETEDRIVETRAINLAYOUT_HXX_INCLUDED
#define NXOpen_MOTION_DISCRETEDRIVETRAINLAYOUT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_DiscreteDrivetrainLayout.ja
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
        class DiscreteDrivetrainLayout;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _DiscreteDrivetrainLayoutBuilder;
        class DiscreteDrivetrainLayoutImpl;
        /** Represents a discrete drivetrain layout motion object.  <br> This is created by Discrete Drivetrain  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  DiscreteDrivetrainLayout : public NXOpen::Motion::MotionObject
        {
            private: DiscreteDrivetrainLayoutImpl * m_discretedrivetrainlayout_impl;
            private: friend class  _DiscreteDrivetrainLayoutBuilder;
            protected: DiscreteDrivetrainLayout();
            public: ~DiscreteDrivetrainLayout();
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