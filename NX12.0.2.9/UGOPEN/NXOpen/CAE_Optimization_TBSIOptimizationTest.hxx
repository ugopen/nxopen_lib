#ifndef NXOpen_CAE_OPTIMIZATION_TBSIOPTIMIZATIONTEST_HXX_INCLUDED
#define NXOpen_CAE_OPTIMIZATION_TBSIOPTIMIZATIONTEST_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Optimization_TBSIOptimizationTest.ja
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
        namespace Optimization
        {
            class TBSIOptimizationTest;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            /** Represents an interface to perform optimization test 
             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TBSIOptimizationTest
            {
                virtual void EnsureVtableExists() {}
                public: virtual ~TBSIOptimizationTest() {}
                /** Solves optimization test 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: virtual void SolveTest
                (
                ) = 0;
                /** Returns the file name of test result  @return  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: virtual NXString GetTestResultFile
                (
                ) = 0;
            }; //lint !e1712 default constructor not defined for class  

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