#ifndef NXOpen_MOTION_GENERALCOUPLER_HXX_INCLUDED
#define NXOpen_MOTION_GENERALCOUPLER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_GeneralCoupler.ja
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
        class GeneralCoupler;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _GeneralCouplerBuilder;
        class GeneralCouplerImpl;
        /** Represents motion 2-3 joint coupler  <br> To create or edit an instance of this class, use @link NXOpen::Motion::GeneralCouplerBuilder  NXOpen::Motion::GeneralCouplerBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  GeneralCoupler : public NXOpen::Motion::MotionObject
        {
            private: GeneralCouplerImpl * m_generalcoupler_impl;
            private: friend class  _GeneralCouplerBuilder;
            protected: GeneralCoupler();
            public: ~GeneralCoupler();
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
