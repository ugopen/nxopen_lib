#ifndef NXOpen_CAE_AXISYMMETRICPARAMETERS_HXX_INCLUDED
#define NXOpen_CAE_AXISYMMETRICPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AxiSymmetricParameters.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class AxiSymmetricParameters;
    }
    namespace CAE
    {
        class _AxiSymmetricParametersBuilder;
        class AxiSymmetricParametersImpl;
        /** Implementation of axi-symmetry utility  <br> To obtain an instance of this class use.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AxiSymmetricParameters : public NXOpen::TaggedObject
        {
            /** Axi Symmetric result type */
            public: enum GetResult
            {
                GetResultOnOriginalModel/** on original model */ ,
                GetResultRevolvedModel/** revolved model */ 
            };

            /** Axis of rotation */
            public: enum AxisOfRotation
            {
                AxisOfRotationXAxis/** xaxis */ ,
                AxisOfRotationYAxis/** yaxis */ ,
                AxisOfRotationZAxis/** zaxis */ 
            };

            /** Result Values */
            public: enum Options
            {
                OptionsAtRevolveAngle/** at revolve angle */ ,
                OptionsEnvelopeAcrossCircumference/** envelope across circumference */ 
            };

            /** Envelope Values */
            public: enum EnvVal
            {
                EnvValMaximum/** maximum */ ,
                EnvValMinimum/** minimum */ ,
                EnvValAbsoluteMaximum/** absolute maximum */ ,
                EnvValAbsoluteMinimum/** absolute minimum */ ,
                EnvValAverage/** average */ ,
                EnvValSum/** sum */ 
            };

            private: AxiSymmetricParametersImpl * m_axisymmetricparameters_impl;
            private: friend class  _AxiSymmetricParametersBuilder;
            protected: AxiSymmetricParameters();
            public: ~AxiSymmetricParameters();
            /**Returns  the result option enum 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::AxiSymmetricParameters::GetResult ResultOption
            (
            );
            /**Sets  the result option enum 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetResultOption
            (
                NXOpen::CAE::AxiSymmetricParameters::GetResult enumAxes /** enumaxes */ 
            );
            /**Returns  the axes of rotation enum 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::AxiSymmetricParameters::AxisOfRotation RotationAxis
            (
            );
            /**Sets  the axes of rotation enum 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetRotationAxis
            (
                NXOpen::CAE::AxiSymmetricParameters::AxisOfRotation enumAxes /** enumaxes */ 
            );
            /**Returns  the options enum 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::AxiSymmetricParameters::Options AxiOptions
            (
            );
            /**Sets  the options enum 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetAxiOptions
            (
                NXOpen::CAE::AxiSymmetricParameters::Options enumOptions /** enumoptions */ 
            );
            /**Returns  the envelope value enum 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::AxiSymmetricParameters::EnvVal EnvelopeVal
            (
            );
            /**Sets  the envelope value enum 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetEnvelopeVal
            (
                NXOpen::CAE::AxiSymmetricParameters::EnvVal enumEnv /** enumenv */ 
            );
            /**Returns  the revolve angle 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: double RevolveAngle
            (
            );
            /**Sets  the revolve angle 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetRevolveAngle
            (
                double revAngle /** revangle */ 
            );
            /**Returns  the start revolve angle 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: double StartRevolveAngle
            (
            );
            /**Sets  the start revolve angle 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetStartRevolveAngle
            (
                double startAngle /** startangle */ 
            );
            /**Returns  the end revolve angle 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: double EndRevolveAngle
            (
            );
            /**Sets  the end revolve angle 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetEndRevolveAngle
            (
                double endAngle /** endangle */ 
            );
            /**Returns  the number of sections 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: int NumberOfSections
            (
            );
            /**Sets  the number of sections 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetNumberOfSections
            (
                int numberOfSections /** numberofsections */ 
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