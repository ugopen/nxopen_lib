#ifndef NXOpen_MECHATRONICS_DISTANCESENSOR_HXX_INCLUDED
#define NXOpen_MECHATRONICS_DISTANCESENSOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_DistanceSensor.ja
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
        class DistanceSensor;
    }
    class DisplayableObject;
    namespace Mechatronics
    {
        class _DistanceSensorBuilder;
        class DistanceSensorImpl;
        /**  @brief  Represents the Distance Sensor. A Distance Sensor is able to detect the shortest distance between the sensor and collision body
            of objects that intersect with its volume.  

           <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::DistanceSensorBuilder  NXOpen::Mechatronics::DistanceSensorBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  DistanceSensor : public NXOpen::DisplayableObject
        {
            private: DistanceSensorImpl * m_distancesensor_impl;
            private: friend class  _DistanceSensorBuilder;
            protected: DistanceSensor();
            public: ~DistanceSensor();
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
