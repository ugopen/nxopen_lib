#ifndef NXOpen_MECHATRONICS_POSITIONSENSOR_HXX_INCLUDED
#define NXOpen_MECHATRONICS_POSITIONSENSOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_PositionSensor.ja
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
        class PositionSensor;
    }
    class DisplayableObject;
    namespace Mechatronics
    {
        class _PositionSensorBuilder;
        class PositionSensorImpl;
        /**  @brief  Represents the Position Sensor. A Position Sensor is able to detect the position of joint or controller.  

           <br> To create or edit an instance of this class, use @link NXOpen::Mechatronics::PositionSensorBuilder  NXOpen::Mechatronics::PositionSensorBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  PositionSensor : public NXOpen::DisplayableObject
        {
            private: PositionSensorImpl * m_positionsensor_impl;
            private: friend class  _PositionSensorBuilder;
            protected: PositionSensor();
            public: ~PositionSensor();
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