#ifndef NXOpen_CAE_SOLUTIONMANAGER_HXX_INCLUDED
#define NXOpen_CAE_SOLUTIONMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SolutionManager.ja
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
#include <NXOpen/CAE_LbcAssociationMgr.hxx>
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
        class SolutionManager;
    }
    namespace CAE
    {
        class LbcAssociationMgr;
    }
    namespace CAE
    {
        class SimBC;
    }
    namespace CAE
    {
        class SimLbcFolder;
    }
    namespace CAE
    {
        class SimLoadSet;
    }
    namespace CAE
    {
        class SimSolution;
    }
    namespace CAE
    {
        class _SolutionManagerBuilder;
        class SolutionManagerImpl;
        /**
            Represents @link NXOpen::CAE::SolutionManager NXOpen::CAE::SolutionManager@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::SimSimulation::CreateSolutionManager  NXOpen::CAE::SimSimulation::CreateSolutionManager @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SolutionManager : public NXOpen::CAE::LbcAssociationMgr
        {
            private: SolutionManagerImpl * m_solutionmanager_impl;
            private: friend class  _SolutionManagerBuilder;
            protected: SolutionManager();
            public: ~SolutionManager();
            /** Add bc to a solution
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void AddBc
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                NXOpen::CAE::SimBC * tBc /** bc object */
            );
            /** Remove bc from a solution
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void RemoveBc
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                NXOpen::CAE::SimBC * tBc /** bc object */
            );
            /** Add bc folder to a solution
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void AddFolder
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                NXOpen::CAE::SimLbcFolder * tBc /** bc folder object */
            );
            /** Remove bc folder from a solution
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void RemoveFolder
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                NXOpen::CAE::SimLbcFolder * tBc /** bc folder object */
            );
            /** Set scale factor on bc in a solution
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void ScaleBc
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                NXOpen::CAE::SimBC * tBc /** bc object */,
                double scale /** scale factor */
            );
            /** Set scale factor on bc folder in a solution
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void ScaleFolder
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                NXOpen::CAE::SimLbcFolder * tBc /** bc folder object */,
                double scale /** scale factor */
            );
            /** Add loadset to a solution
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void AddLoadset
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                NXOpen::CAE::SimLoadSet * tBc /** loadset object */
            );
            /** Remove loadset from a solution
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void RemoveLoadset
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                NXOpen::CAE::SimLoadSet * tBc /** loadset object */
            );
            /** Set scale factor on loadset in a solution
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void ScaleLoadset
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                NXOpen::CAE::SimLoadSet * tBc /** loadset object */,
                double scale /** scale factor */
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
