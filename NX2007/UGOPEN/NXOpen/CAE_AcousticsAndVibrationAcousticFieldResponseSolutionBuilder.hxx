#ifndef NXOpen_CAE_ACOUSTICSANDVIBRATIONACOUSTICFIELDRESPONSESOLUTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ACOUSTICSANDVIBRATIONACOUSTICFIELDRESPONSESOLUTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AcousticsAndVibrationAcousticFieldResponseSolutionBuilder.ja
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
#include <NXOpen/CAE_AcousticsAndVibrationAcousticFieldResponseOutputRequestComponentAccessor.hxx>
#include <NXOpen/CAE_AcousticsAndVibrationAcousticRadiatingSurfaceGroupComponentAccessor.hxx>
#include <NXOpen/CAE_AcousticsAndVibrationSolverParametersComponentAccessor.hxx>
#include <NXOpen/CAE_ModelAndLoadPreProcessFrequencyOptions.hxx>
#include <NXOpen/Builder.hxx>
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
        class AcousticsAndVibrationAcousticFieldResponseSolutionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class AcousticsAndVibrationAcousticFieldResponseOutputRequestComponentAccessor;
    }
    namespace CAE
    {
        class AcousticsAndVibrationAcousticRadiatingSurfaceGroupComponentAccessor;
    }
    namespace CAE
    {
        class AcousticsAndVibrationSolverParametersComponentAccessor;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcessFrequencyOptions;
    }
    namespace CAE
    {
        class _AcousticsAndVibrationAcousticFieldResponseSolutionBuilderBuilder;
        class AcousticsAndVibrationAcousticFieldResponseSolutionBuilderImpl;
        /**
            Builds a @link NXOpen::CAE::AcousticsAndVibrationAcousticFieldResponseSolution NXOpen::CAE::AcousticsAndVibrationAcousticFieldResponseSolution@endlink  object which 
            represets a data processing meta solution.
             <br> To create a new instance of this class, use @link NXOpen::CAE::AcousticsAndVibrationAcousticFieldResponseSolutionCollection::CreateBuilder  NXOpen::CAE::AcousticsAndVibrationAcousticFieldResponseSolutionCollection::CreateBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AcousticsAndVibrationAcousticFieldResponseSolutionBuilder : public NXOpen::Builder
        {
            private: AcousticsAndVibrationAcousticFieldResponseSolutionBuilderImpl * m_acousticsandvibrationacousticfieldresponsesolutionbuilder_impl;
            private: friend class  _AcousticsAndVibrationAcousticFieldResponseSolutionBuilderBuilder;
            protected: AcousticsAndVibrationAcousticFieldResponseSolutionBuilder();
            public: ~AcousticsAndVibrationAcousticFieldResponseSolutionBuilder();
            /**Returns  the meta solution name. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SolutionName
            (
            );
            /**Sets  the meta solution name. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSolutionName
            (
                const NXString & title /** title */ 
            );
            /**Sets  the meta solution name. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetSolutionName
            (
                const char * title /** title */ 
            );
            /**Returns  the solver parameters 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AcousticsAndVibrationSolverParametersComponentAccessor * SolverParameters
            (
            );
            /**Returns  the output request 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AcousticsAndVibrationAcousticFieldResponseOutputRequestComponentAccessor * OutputRequest
            (
            );
            /**Returns  the loads 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AcousticsAndVibrationAcousticRadiatingSurfaceGroupComponentAccessor * LoadsGroup
            (
            );
            /**Returns  the frequency options 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ModelAndLoadPreProcessFrequencyOptions * FrequencyOptions
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