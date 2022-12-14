#ifndef NXOpen_CAM_INSPECTIONSENSORMASSEDITBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONSENSORMASSEDITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionSensorMassEditBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAM_InspectionSensorMassEditBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionSensorMassEditBuilder;
    }
    class Builder;
    namespace CAM
    {
        class _InspectionSensorMassEditBuilderBuilder;
        class InspectionSensorMassEditBuilderImpl;
        /** Edit Multiple Subops Dialog builder  <br> To create a new instance of this class, use @link CAM::InspectionMoveCollection::CreateInspectionSensorMassEditBuilder CAM::InspectionMoveCollection::CreateInspectionSensorMassEditBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  InspectionSensorMassEditBuilder : public Builder
        {
            /** the sensor selection mode */
            public: enum SensorSelectModeType
            {
                SensorSelectModeTypeAutomatic/** Choose sensor automatically */,
                SensorSelectModeTypeSpecifySensor/** Manually specify sensor */,
                SensorSelectModeTypeSpecifyProbeAngles/** Manually specify probe angles */,
                SensorSelectModeTypeSpecifyProbeTip/** Manually specify probe tip */,
                SensorSelectModeTypeSpecifyAnglesandTip/** Manually specify probe angles and probe tip */
            };

            /** the sensor strategy */
            public: enum SensorStrategyType
            {
                SensorStrategyTypeCreateasneeded/** Create as needed */,
                SensorStrategyTypeUseexistingonly/** Use existing only */
            };

            private: InspectionSensorMassEditBuilderImpl * m_inspectionsensormasseditbuilder_impl;
            private: friend class  _InspectionSensorMassEditBuilderBuilder;
            protected: InspectionSensorMassEditBuilder();
            public: ~InspectionSensorMassEditBuilder();
            /**Returns  the sensor strategy  <br> License requirements : None */
            public: NXOpen::CAM::InspectionSensorMassEditBuilder::SensorStrategyType SensorStrategy
            (
            );
            /**Sets  the sensor strategy  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetSensorStrategy
            (
                NXOpen::CAM::InspectionSensorMassEditBuilder::SensorStrategyType sensorStrategy /** sensorstrategy */ 
            );
            /**Returns  the sensor name  <br> License requirements : None */
            public: NXString SensorName
            (
            );
            /**Sets  the sensor name  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetSensorName
            (
                const NXString & sensorName /** sensorname */ 
            );
            /**Returns  the tip  <br> License requirements : None */
            public: int TipNumber
            (
            );
            /**Sets  the tip  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTipNumber
            (
                int tipNumber /** tipnumber */ 
            );
            /**Returns  the angle a  <br> License requirements : None */
            public: double AngleA
            (
            );
            /**Sets  the angle a  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngleA
            (
                double angleA /** anglea */ 
            );
            /**Returns  the angle b  <br> License requirements : None */
            public: double AngleB
            (
            );
            /**Sets  the angle b  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetAngleB
            (
                double angleB /** angleb */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
