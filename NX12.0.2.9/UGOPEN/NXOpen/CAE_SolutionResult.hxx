#ifndef NXOpen_CAE_SOLUTIONRESULT_HXX_INCLUDED
#define NXOpen_CAE_SOLUTIONRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SolutionResult.ja
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
#include <NXOpen/CAE_Result.hxx>
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
        class SolutionResult;
    }
    namespace CAE
    {
        class Result;
    }
    namespace CAE
    {
        class SimPart;
    }
    namespace CAE
    {
        class SimResultReference;
    }
    namespace CAE
    {
        class SimSolution;
    }
    namespace CAE
    {
        class SimSolutionStep;
    }
    namespace CAE
    {
        class _SolutionResultBuilder;
        class SolutionResultImpl;
        /** Represents analysis results for a given @link NXOpen::CAE::SimSolution NXOpen::CAE::SimSolution@endlink . 
                Use @link NXOpen::CAE::ResultManager NXOpen::CAE::ResultManager@endlink  to create an 
                @link NXOpen::CAE::SolutionResult NXOpen::CAE::SolutionResult@endlink 
             <br> An instance of this class can not be obtained  <br> 
         <br>  Created in NX6.0.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SolutionResult : public NXOpen::CAE::Result
        {
            private: SolutionResultImpl * m_solutionresult_impl;
            private: friend class  _SolutionResultBuilder;
            protected: SolutionResult();
            public: ~SolutionResult();
            /**Returns  the solution 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimSolution * Solution
            (
            );
            /** Combine the load cases  
             <br>  @deprecated Deprecated in NX10.0.0.  Use overloaded function with Result Reference instead. <br>  

             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use overloaded function with Result Reference instead.") void CombineLoadcases
            (
                NXOpen::CAE::SimPart * part /** part */ ,
                NXOpen::CAE::SimSolution * solution /** solution */ ,
                const std::vector<NXOpen::CAE::SimSolutionStep *> & lcaseas /** lcaseas */ ,
                const std::vector<double> & factors /** factors */ ,
                const NXString & desc /** desc */ 
            );
            /** Combine the load cases  
             <br>  @deprecated Deprecated in NX10.0.0.  Use overloaded function with Result Reference instead. <br>  

             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void CombineLoadcases
            (
                NXOpen::CAE::SimPart * part /** part */ ,
                NXOpen::CAE::SimSolution * solution /** solution */ ,
                const std::vector<NXOpen::CAE::SimSolutionStep *> & lcaseas /** lcaseas */ ,
                const std::vector<double> & factors /** factors */ ,
                const char * desc /** desc */ 
            );
            /** Combine the load cases  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void CombineLoadcases
            (
                NXOpen::CAE::SimPart * part /** part */ ,
                NXOpen::CAE::SimResultReference * tResultRef /** tresultref */ ,
                const std::vector<NXOpen::CAE::SimSolutionStep *> & lcaseas /** lcaseas */ ,
                const std::vector<double> & factors /** factors */ ,
                const NXString & desc /** desc */ 
            );
            /** Combine the load cases  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void CombineLoadcases
            (
                NXOpen::CAE::SimPart * part /** part */ ,
                NXOpen::CAE::SimResultReference * tResultRef /** tresultref */ ,
                const std::vector<NXOpen::CAE::SimSolutionStep *> & lcaseas /** lcaseas */ ,
                const std::vector<double> & factors /** factors */ ,
                const char * desc /** desc */ 
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
