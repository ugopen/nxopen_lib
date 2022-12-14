#ifndef NXOpen_CAE_ACOUSTICSANDVIBRATIONLOADIDENTIFICATIONSOLUTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ACOUSTICSANDVIBRATIONLOADIDENTIFICATIONSOLUTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AcousticsAndVibrationLoadIdentificationSolutionBuilder.ja
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
#include <NXOpen/CAE_AcousticsAndVibrationFrfDataComponentAccessor.hxx>
#include <NXOpen/CAE_AcousticsAndVibrationMappingDataComponentAccessor.hxx>
#include <NXOpen/CAE_AcousticsAndVibrationSolutionOptionsComponentAccessor.hxx>
#include <NXOpen/CAE_AcousticsAndVibrationSolverParametersComponentAccessor.hxx>
#include <NXOpen/CAE_AcousticsAndVibrationVibrationDataComponentAccessor.hxx>
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
        class AcousticsAndVibrationLoadIdentificationSolutionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class AcousticsAndVibrationFrfDataComponentAccessor;
    }
    namespace CAE
    {
        class AcousticsAndVibrationMappingDataComponentAccessor;
    }
    namespace CAE
    {
        class AcousticsAndVibrationSolutionOptionsComponentAccessor;
    }
    namespace CAE
    {
        class AcousticsAndVibrationSolverParametersComponentAccessor;
    }
    namespace CAE
    {
        class AcousticsAndVibrationVibrationDataComponentAccessor;
    }
    namespace CAE
    {
        class _AcousticsAndVibrationLoadIdentificationSolutionBuilderBuilder;
        class AcousticsAndVibrationLoadIdentificationSolutionBuilderImpl;
        /**
            Builds a @link NXOpen::CAE::AcousticsAndVibrationLoadIdentificationSolution NXOpen::CAE::AcousticsAndVibrationLoadIdentificationSolution@endlink  object which 
            represets a data processing meta solution.
             <br> To create a new instance of this class, use @link NXOpen::CAE::AcousticsAndVibrationLoadIdentificationSolutionCollection::CreateBuilder  NXOpen::CAE::AcousticsAndVibrationLoadIdentificationSolutionCollection::CreateBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AcousticsAndVibrationLoadIdentificationSolutionBuilder : public NXOpen::Builder
        {
            private: AcousticsAndVibrationLoadIdentificationSolutionBuilderImpl * m_acousticsandvibrationloadidentificationsolutionbuilder_impl;
            private: friend class  _AcousticsAndVibrationLoadIdentificationSolutionBuilderBuilder;
            protected: AcousticsAndVibrationLoadIdentificationSolutionBuilder();
            public: ~AcousticsAndVibrationLoadIdentificationSolutionBuilder();
            /**Returns  the meta solution name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SolutionName
            (
            );
            /**Sets  the meta solution name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSolutionName
            (
                const NXString & title /** title */ 
            );
            /**Sets  the meta solution name. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetSolutionName
            (
                const char * title /** title */ 
            );
            /**Returns  the vibration data accessor. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AcousticsAndVibrationVibrationDataComponentAccessor * VibrationData
            (
            );
            /**Returns  the FRF data accessor. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AcousticsAndVibrationFrfDataComponentAccessor * FrfData
            (
            );
            /**Returns  the mapping data accessor. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AcousticsAndVibrationMappingDataComponentAccessor * MappingData
            (
            );
            /**Returns  the solver parameters accessor. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AcousticsAndVibrationSolverParametersComponentAccessor * SolverParameters
            (
            );
            /**Returns  the solver parameters accessor. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::AcousticsAndVibrationSolutionOptionsComponentAccessor * SolutionOptions
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
