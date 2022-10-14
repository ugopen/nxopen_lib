#ifndef NXOpen_MOTION_TIREPROPERTYMOTORCYCLE_HXX_INCLUDED
#define NXOpen_MOTION_TIREPROPERTYMOTORCYCLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_TirePropertyMotorcycle.ja
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
#include <NXOpen/Motion_TirePropertyMotorcycle.hxx>
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
        class TirePropertyMotorcycle;
    }
    namespace Motion
    {
        class TireProperty;
    }
    namespace Motion
    {
        class _TirePropertyMotorcycleBuilder;
        class TirePropertyMotorcycleImpl;
        /**  <br> Motorcycle Tire Property element. <br> 
                This is an object that contains parameters needed for the Motorcycle Tire model  <br> To create or edit an instance of this class, use @link NXOpen::Motion::TirePropertyMotorcycleBuilder  NXOpen::Motion::TirePropertyMotorcycleBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  TirePropertyMotorcycle : public NXOpen::Motion::TireProperty
        {
            private: TirePropertyMotorcycleImpl * m_tirepropertymotorcycle_impl;
            private: friend class  _TirePropertyMotorcycleBuilder;
            protected: TirePropertyMotorcycle();
            public: ~TirePropertyMotorcycle();
            /** Copy parameters from another @link Motion::TirePropertyMotorcycle Motion::TirePropertyMotorcycle@endlink  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void CopyParameters
            (
                NXOpen::Motion::TirePropertyMotorcycle * source /** source */ 
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