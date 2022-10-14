#ifndef NXOpen_MOTION_ANALYTICALCONTACTPROPERTY_HXX_INCLUDED
#define NXOpen_MOTION_ANALYTICALCONTACTPROPERTY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_AnalyticalContactProperty.ja
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
        class AnalyticalContactProperty;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _AnalyticalContactPropertyBuilder;
        class AnalyticalContactPropertyImpl;
        /** Represents an Analytical Contact Property. Used to model contact between 
                spheres, revolved surfaces, extruded surfaces, and rails.  <br> To create or edit an instance of this class, use @link NXOpen::Motion::AnalyticalContactPropertyBuilder  NXOpen::Motion::AnalyticalContactPropertyBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  AnalyticalContactProperty : public NXOpen::Motion::MotionObject
        {
            private: AnalyticalContactPropertyImpl * m_analyticalcontactproperty_impl;
            private: friend class  _AnalyticalContactPropertyBuilder;
            protected: AnalyticalContactProperty();
            public: ~AnalyticalContactProperty();
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