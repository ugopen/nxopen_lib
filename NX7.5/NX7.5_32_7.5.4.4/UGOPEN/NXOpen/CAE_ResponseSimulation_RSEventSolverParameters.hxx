#ifndef NXOpen_CAE_RESPONSESIMULATION_RSEVENTSOLVERPARAMETERS_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_RSEVENTSOLVERPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_RSEventSolverParameters.ja
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
#include <NXOpen/CAE_ResponseSimulation_RSEventSolverParameters.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class RSEventSolverParameters;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _RSEventSolverParametersBuilder;
            class RSEventSolverParametersImpl;
            /** Represents a response analysis event */
            class NXOPENCPPEXPORT  RSEventSolverParameters : public TaggedObject
            {
                /** Represents DDAM coefficient type */
                public: enum DdamCoefficientType
                {
                    DdamCoefficientTypeAf/** af */ ,
                    DdamCoefficientTypeVf/** vf */ ,
                    DdamCoefficientTypeAa/** aa */ ,
                    DdamCoefficientTypeAb/** ab */ ,
                    DdamCoefficientTypeAc/** ac */ ,
                    DdamCoefficientTypeAd/** ad */ ,
                    DdamCoefficientTypeVa/** va */ ,
                    DdamCoefficientTypeVb/** vb */ ,
                    DdamCoefficientTypeVc/** vc */ 
                };

                private: RSEventSolverParametersImpl * m_rseventsolverparameters_impl;
                private: friend class  _RSEventSolverParametersBuilder;
                protected: RSEventSolverParameters();
                public: ~RSEventSolverParameters();
                /**Returns  the DDAM A coefficient  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: double DdamCoefficientA
                (
                );
                /**Sets  the DDAM A coefficient  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDdamCoefficientA
                (
                    double coefficientA /** coefficienta */ 
                );
                /**Returns  the DDAM V coefficient  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: double DdamCoefficientV
                (
                );
                /**Sets  the DDAM V coefficient  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDdamCoefficientV
                (
                    double coefficientV /** coefficientv */ 
                );
                /** Returns DDAM coefficient value of the specified type  @return   <br> License requirements : None */
                public: double GetDdamCoefficient
                (
                    NXOpen::CAE::ResponseSimulation::RSEventSolverParameters::DdamCoefficientType coefficientType /** coefficienttype */ 
                );
                /** Sets the DDAM coefficient value of the specified type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDdamCoefficient
                (
                    NXOpen::CAE::ResponseSimulation::RSEventSolverParameters::DdamCoefficientType coefficientType /** coefficienttype */ ,
                    double coefficient /** coefficient */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
