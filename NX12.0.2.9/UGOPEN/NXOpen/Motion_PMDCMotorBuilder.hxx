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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Motion_MotorBuilder.hxx>
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
        class PMDCMotorBuilder;
    }
    class Expression;
    namespace Motion
    {
        class MotorBuilder;
    }
    namespace Motion
    {
        class _PMDCMotorBuilderBuilder;
        class PMDCMotorBuilderImpl;
        /** Represents a @link NXOpen::Motion::PMDCMotorBuilder NXOpen::Motion::PMDCMotorBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::Motion::PMDCMotorCollection::CreatePmdcMotorBuilder  NXOpen::Motion::PMDCMotorCollection::CreatePmdcMotorBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  PMDCMotorBuilder : public NXOpen::Motion::MotorBuilder
        {
            /** Motor type  */
            public: enum Type
            {
                TypeWithRotor/** Included rotor - load torque */,
                TypeWithoutRotor/** Excluded rotor - rotor speed */
            };

            private: PMDCMotorBuilderImpl * m_pmdcmotorbuilder_impl;
            private: friend class  _PMDCMotorBuilderBuilder;
            protected: PMDCMotorBuilder();
            public: ~PMDCMotorBuilder();
            /**Returns  the motor type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Motion::PMDCMotorBuilder::Type MotorType
            (
            );
            /**Sets  the motor type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetMotorType
            (
                NXOpen::Motion::PMDCMotorBuilder::Type motorType /** motor type */ 
            );
            /**Returns  the rotor interia 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double RotorInteria
            (
            );
            /**Sets  the rotor interia 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetRotorInteria
            (
                double rotorInteria /** rotor interia */ 
            );
            /**Returns  the damping coefficient 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double DampingCoefficient
            (
            );
            /**Sets  the damping coefficient 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetDampingCoefficient
            (
                double dampingCoefficient /** damping coefficient */ 
            );
            /**Returns  the initial speed 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double InitialSpeed
            (
            );
            /**Sets  the initial speed 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetInitialSpeed
            (
                double initialSpeed /** initial speed */ 
            );
            /**Returns  the name 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXString Name
            (
            );
            /**Sets  the name 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetName
            (
                const NXString & motorName /** motor name */ 
            );
            /**Sets  the name 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            void SetName
            (
                const char * motorName /** motor name */ 
            );
            /**Returns   the Nominal Voltage Expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Expression * NominalVoltageExpression
            (
            );
            /**Returns   the Voltage Constant Expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Expression * VoltageConstantExpression
            (
            );
            /**Returns   the Inductant Expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Expression * InductanceExpression
            (
            );
            /**Returns   the Resistance Expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Expression * ResistanceExpression
            (
            );
            /**Returns   the Initial Current Expression
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Expression * InitialCurrentExpression
            (
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
