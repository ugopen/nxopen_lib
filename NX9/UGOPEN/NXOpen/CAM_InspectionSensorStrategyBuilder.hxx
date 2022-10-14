#ifndef NXOpen_CAM_INSPECTIONSENSORSTRATEGYBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONSENSORSTRATEGYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionSensorStrategyBuilder.ja
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
#include <NXOpen/CAM_InheritableBuilder.hxx>
#include <NXOpen/CAM_InspectionMoveBuilder.hxx>
#include <NXOpen/CAM_InspectionSensorStrategyBuilder.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class InspectionSensorStrategyBuilder;
    }
    namespace CAM
    {
        class InheritableBuilder;
    }
    namespace CAM
    {
        class _InspectionSensorStrategyBuilderBuilder;
        class InspectionSensorStrategyBuilderImpl;
        /** Represents a builder for an inheritable sensor strategy enum value 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionSensorStrategyBuilder : public CAM::InheritableBuilder
        {
            private: InspectionSensorStrategyBuilderImpl * m_inspectionsensorstrategybuilder_impl;
            private: friend class  _InspectionSensorStrategyBuilderBuilder;
            protected: InspectionSensorStrategyBuilder();
            public: ~InspectionSensorStrategyBuilder();
            /**Returns  the current sensor strategy 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionMoveBuilder::SensorStrategyTypes Value
            (
            );
            /**Sets  the current sensor strategy 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetValue
            (
                NXOpen::CAM::InspectionMoveBuilder::SensorStrategyTypes itemValue /** the new sensor strategy */
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