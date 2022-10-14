#ifndef NXOpen_MOTION_DRIVERMULTIOPERATIONS_HXX_INCLUDED
#define NXOpen_MOTION_DRIVERMULTIOPERATIONS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_DriverMultiOperations.ja
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
#include <NXOpen/Motion_DriverOperation.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class DriverMultiOperations;
    }
    namespace Motion
    {
        class DriverOperation;
    }
    namespace Motion
    {
        class _DriverMultiOperationsBuilder;
        class DriverMultiOperationsImpl;
        /** Represents a @link NXOpen::Motion::DriverMultiOperations NXOpen::Motion::DriverMultiOperations@endlink  
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  DriverMultiOperations : public NXOpen::TaggedObject
        {
            private: DriverMultiOperationsImpl * m_drivermultioperations_impl;
            private: friend class  _DriverMultiOperationsBuilder;
            protected: DriverMultiOperations();
            public: ~DriverMultiOperations();
            /**Returns  the motion motion euler angle1, it is for revolute joint and cylindrical joint 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::DriverOperation * MotionEulerAngle1
            (
            );
            /**Returns  the motion translation z, it is for slider joint and cylindrical joint 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::DriverOperation * MotionTranslationZ
            (
            );
            /**Returns  the motion point on curve, it is for point on curve constraint 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::DriverOperation * MotionPointOnCurve
            (
            );
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