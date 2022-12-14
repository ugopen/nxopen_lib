#ifndef NXOpen_MOTION_UDFDESCRIPTION_HXX_INCLUDED
#define NXOpen_MOTION_UDFDESCRIPTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_UdfDescription.ja
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
        class UdfDescription;
    }
    namespace Motion
    {
        class MotionObject;
    }
    namespace Motion
    {
        class _UdfDescriptionBuilder;
        class UdfDescriptionImpl;
        /** Represents a @link Motion::UdfDescription Motion::UdfDescription@endlink . This class
                exposes a read-only API for the udf description so that customers
                can check what description is available for a given UDF type.  <br> To create or edit an instance of this class, use @link NXOpen::Motion::UdfDescriptionBuilder  NXOpen::Motion::UdfDescriptionBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  UdfDescription : public NXOpen::Motion::MotionObject
        {
            private: UdfDescriptionImpl * m_udfdescription_impl;
            private: friend class  _UdfDescriptionBuilder;
            protected: UdfDescription();
            public: ~UdfDescription();
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
