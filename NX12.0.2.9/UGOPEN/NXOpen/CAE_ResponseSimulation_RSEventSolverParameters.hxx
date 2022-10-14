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
            /** Represents a response analysis event 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  RSEventSolverParameters : public NXOpen::TaggedObject
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
                /**Returns  the DDAM A coefficient 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: double DdamCoefficientA
                (
                );
                /**Sets  the DDAM A coefficient 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDdamCoefficientA
                (
                    double coefficientA /** coefficienta */ 
                );
                /**Returns  the DDAM V coefficient 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: double DdamCoefficientV
                (
                );
                /**Sets  the DDAM V coefficient 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDdamCoefficientV
                (
                    double coefficientV /** coefficientv */ 
                );
                /** Returns DDAM coefficient value of the specified type  @return  
                 <br>  Created in NX7.5.2.  <br>  
                 <br> License requirements : None */
                public: double GetDdamCoefficient
                (
                    NXOpen::CAE::ResponseSimulation::RSEventSolverParameters::DdamCoefficientType coefficientType /** coefficienttype */ 
                );
                /** Sets the DDAM coefficient value of the specified type 
                 <br>  Created in NX7.5.2.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetDdamCoefficient
                (
                    NXOpen::CAE::ResponseSimulation::RSEventSolverParameters::DdamCoefficientType coefficientType /** coefficienttype */ ,
                    double coefficient /** coefficient */ 
                );
            };
        }
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