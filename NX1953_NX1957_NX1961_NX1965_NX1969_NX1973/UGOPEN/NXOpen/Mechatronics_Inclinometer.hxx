#ifndef NXOpen_MECHATRONICS_INCLINOMETER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_INCLINOMETER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_Inclinometer.ja
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
#include <NXOpen/DisplayableObject.hxx>
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
        class Inclinometer;
    }
    class DisplayableObject;
    namespace Mechatronics
    {
        class _InclinometerBuilder;
        class InclinometerImpl;
        /**  @brief  Represents the Inclinometer. An Inclinometer is able to detect the angle of the rigid body.  

           <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::InclinometerBuilder  NXOpen::Mechatronics::InclinometerBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  Inclinometer : public NXOpen::DisplayableObject
        {
            private: InclinometerImpl * m_inclinometer_impl;
            private: friend class  _InclinometerBuilder;
            protected: Inclinometer();
            public: ~Inclinometer();
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
