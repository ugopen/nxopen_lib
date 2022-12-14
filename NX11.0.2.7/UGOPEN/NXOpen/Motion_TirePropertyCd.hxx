#ifndef NXOpen_MOTION_TIREPROPERTYCD_HXX_INCLUDED
#define NXOpen_MOTION_TIREPROPERTYCD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_TirePropertyCd.ja
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
#include <NXOpen/Motion_TirePropertyCd.hxx>
#include <NXOpen/Motion_TireProperty.hxx>
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
        class TirePropertyCd;
    }
    namespace Motion
    {
        class TireProperty;
    }
    namespace Motion
    {
        class _TirePropertyCdBuilder;
        class TirePropertyCdImpl;
        /** CDTIRE Tire Property 
            This is an object that contains parameters needed for the CDTIRE Tire model  <br> To create or edit an instance of this class, use @link NXOpen::Motion::TirePropertyCdBuilder  NXOpen::Motion::TirePropertyCdBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  TirePropertyCd : public NXOpen::Motion::TireProperty
        {
            private: TirePropertyCdImpl * m_tirepropertycd_impl;
            private: friend class  _TirePropertyCdBuilder;
            protected: TirePropertyCd();
            public: ~TirePropertyCd();
            /** Copy parameters from another @link Motion::TirePropertyCd Motion::TirePropertyCd@endlink  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void CopyParameters
            (
                NXOpen::Motion::TirePropertyCd * source /** source */ 
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
