#ifndef NXOpen_MECHATRONICS_COLLISIONSENSOR_HXX_INCLUDED
#define NXOpen_MECHATRONICS_COLLISIONSENSOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_CollisionSensor.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Mechatronics
    {
        class CollisionSensor;
    }
    class DisplayableObject;
    namespace Mechatronics
    {
        class _CollisionSensorBuilder;
        class CollisionSensorImpl;
        /** Represents the Collision Sensor. A Collision Sensor is able to detect the presence
            of objects that intersect with its volume. */
        class NXOPENCPPEXPORT  CollisionSensor : public DisplayableObject
        {
            private: CollisionSensorImpl * m_collisionsensor_impl;
            private: friend class  _CollisionSensorBuilder;
            protected: CollisionSensor();
            public: ~CollisionSensor();
        };
    }
}
#undef EXPORTLIBRARY
#endif
