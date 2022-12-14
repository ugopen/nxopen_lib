#ifndef NXOpen_CAE_SIMSOLVEMANAGER_HXX_INCLUDED
#define NXOpen_CAE_SIMSOLVEMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimSolveManager.ja
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
#include <NXOpen/CAE_SimSolution.hxx>
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
        class SimSolveManager;
    }
    class Session;
    namespace CAE
    {
        class SimSolution;
    }
    namespace CAE
    {
        class SimSolveManagerImpl;
        /**  @brief  Represents a @link NXOpen::CAE::SimSolveManager NXOpen::CAE::SimSolveManager@endlink  
            manager which is used to manage the solve process of solutions.  

           <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimSolveManager
        {
            private: SimSolveManagerImpl * m_simsolvemanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit SimSolveManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static SimSolveManager* theSimSolveManager;
            /** Returns the SimSolveManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static SimSolveManager* GetSimSolveManager(NXOpen::Session *owner);
            public: ~SimSolveManager();
            /** Return the chain of prerequisites for the given solution. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void GetChainOfPrerequisites
            (
                NXOpen::CAE::SimSolution * pSol /** the solution for which we want the chain of prerequisites */,
                std::vector<NXOpen::CAE::SimSolution *> & pSolutions /** the prerequisites of the input solution */,
                std::vector<bool> & hasResult /** returns if the nth prerequisite has a result */
            );
            /** Solve the chain of solutions given in input. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SolveChainOfSolutions
            (
                const std::vector<NXOpen::CAE::SimSolution *> & pSolutions /** The solutions to be solved */,
                NXOpen::CAE::SimSolution::SolveOption solveOption /** solve option */,
                NXOpen::CAE::SimSolution::SetupCheckOption setupCheckOption /** setup check option */,
                NXOpen::CAE::SimSolution::SolveMode runModeOption /** run mode option */,
                int* numSolutionsSolved /** the number of solutions solved*/,
                int* numSolutionsFailed /** the number of solutions which failed*/,
                int* numSolutionsSkipped /** the number of solutions which have been skipped*/
            );
            /** Solve all solutions in the sim document. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SolveAllSolutions
            (
                NXOpen::CAE::SimSolution::SolveOption solveOption /** solve option */,
                NXOpen::CAE::SimSolution::SetupCheckOption setupCheckOption /** setup check option */,
                NXOpen::CAE::SimSolution::SolveMode runModeOption /** run mode option */,
                bool skipSolutionWithResults /** skip the solution if it has a result */,
                int* numSolutionsSolved /** the number of solutions solved*/,
                int* numSolutionsFailed /** the number of solutions which failed */,
                int* numSolutionsSkipped /** the number of solutions which have been skipped*/
            );
            /** Solve all meta solutions in the sim document. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SolveAllMetaSolutions
            (
                NXOpen::CAE::SimSolution::SolveOption solveOption /** solve option */,
                NXOpen::CAE::SimSolution::SetupCheckOption setupCheckOption /** setup check option */,
                NXOpen::CAE::SimSolution::SolveMode runModeOption /** run mode option */,
                bool skipSolutionWithResults /** skip the solution if it has a result */,
                int* numSolutionsSolved /** the number of solutions solved */,
                int* numSolutionsFailed /** the number of solutions which failed */,
                int* numSolutionsSkipped /** the number of solutions which have been skipped */
            );
        }; //lint !e1712 default constructor not defined for class  

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
