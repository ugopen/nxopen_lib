#ifndef NXOpen_MOTION_PMDCMOTORBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_PMDCMOTORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_PMDCMotorBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Motion_PMDCMotorBuilder.hxx>
#include <NXOpen/Motion_MotorBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class PMDCMotorBuilder;
    }
    namespace Motion
    {
        class MotorBuilder;
    }
    namespace Motion
    {
        class _PMDCMotorBuilderBuilder;
        /** Represents a @link Motion::PMDCMotorBuilder Motion::PMDCMotorBuilder@endlink   <br> To create a new instance of this class, use @link Motion::PMDCMotorCollection::CreatePmdcMotorBuilder Motion::PMDCMotorCollection::CreatePmdcMotorBuilder@endlink  <br> */
        class NXOPENCPPEXPORT PMDCMotorBuilder : public Motion::MotorBuilder
        {
            /** Motor type  */
            public: enum Type
            {
                TypeWithRotor/** Included rotor - load torque */,
                TypeWithoutRotor/** Excluded rotor - rotor speed */
            };

            private: friend class  _PMDCMotorBuilderBuilder;
            protected: PMDCMotorBuilder();
            /**Returns  the motor type  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Motion::PMDCMotorBuilder::Type MotorType
            (
            );
            /**Sets  the motor type  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetMotorType
            (
                NXOpen::Motion::PMDCMotorBuilder::Type motorType /** motor type */ 
            );
            /**Returns  the rotor interia  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double RotorInteria
            (
            );
            /**Sets  the rotor interia  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetRotorInteria
            (
                double rotorInteria /** rotor interia */ 
            );
            /**Returns  the damping coefficient  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double DampingCoefficient
            (
            );
            /**Sets  the damping coefficient  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetDampingCoefficient
            (
                double dampingCoefficient /** damping coefficient */ 
            );
            /**Returns  the initial speed  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double InitialSpeed
            (
            );
            /**Sets  the initial speed  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetInitialSpeed
            (
                double initialSpeed /** initial speed */ 
            );
            /**Returns  the nominal voltage  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double NominalVoltage
            (
            );
            /**Sets  the nominal voltage  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetNominalVoltage
            (
                double nominalVoltage /** nominal voltage */ 
            );
            /**Returns  the voltage constant  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double VoltageConstant
            (
            );
            /**Sets  the voltage constant  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetVoltageConstant
            (
                double voltageConstant /** voltage constant */ 
            );
            /**Returns  the inductance  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double Inductance
            (
            );
            /**Sets  the inductance  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetInductance
            (
                double inductance /** inductance */ 
            );
            /**Returns  the resistance  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double Resistance
            (
            );
            /**Sets  the resistance  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetResistance
            (
                double resistance /** resistance */ 
            );
            /**Returns  the initial current  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double InitialCurrent
            (
            );
            /**Sets  the initial current  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetInitialCurrent
            (
                double initialCurrent /** initial current */ 
            );
            /**Returns  the name  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXString Name
            (
            );
            /**Sets  the name  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetName
            (
                const NXString & motorName /** motor name */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif