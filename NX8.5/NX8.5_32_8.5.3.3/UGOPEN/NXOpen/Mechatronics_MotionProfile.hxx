#ifndef NXOpen_MECHATRONICS_MOTIONPROFILE_HXX_INCLUDED
#define NXOpen_MECHATRONICS_MOTIONPROFILE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_MotionProfile.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class MotionProfile;
    }
    class NXObject;
    namespace Mechatronics
    {
        class _MotionProfileBuilder;
        class MotionProfileImpl;
        /** Represents the MotionProfile class. A Motion Profile is used to define
            motion profile for a cam constraint.  <br> To create or edit an instance of this class, use @link Mechatronics::MotionProfileBuilder  Mechatronics::MotionProfileBuilder @endlink  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  MotionProfile : public NXObject
        {
            private: MotionProfileImpl * m_motionprofile_impl;
            private: friend class  _MotionProfileBuilder;
            protected: MotionProfile();
            public: ~MotionProfile();
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