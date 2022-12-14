#ifndef NXOpen_CAE_OPTIMIZERAUTOTEST_HXX_INCLUDED
#define NXOpen_CAE_OPTIMIZERAUTOTEST_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_OptimizerAutotest.ja
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
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

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
        class OptimizerAutotest;
    }
    class DebugSession;
    namespace CAE
    {
        class OptimizerAutotestImpl;

        /// \cond NX_NO_DOC 
        /** Represents a class that is used for NX CAE Optimizer testing.  This class should not
            be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENDEBUGSESSIONCPPEXPORT  OptimizerAutotest
        {
            private: OptimizerAutotestImpl * m_optimizerautotest_impl;
            private: NXOpen::DebugSession* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit OptimizerAutotest(NXOpen::DebugSession *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~OptimizerAutotest();
            /** Set autotest to use HyperOpt or default NX Optimizer and load the optimizer library. Must be called first. 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Optimizer::LoadOptimizer CAE::Optimizer::LoadOptimizer@endlink  instead. <br>  

             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Optimizer::LoadOptimizer instead.") void SelectAndLoadOptimizer
            (
                bool bUseHyperopt /** busehyperopt */ 
            );
            /** Load NX Optimizer library. Must be called first. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void LoadOptimizer
            (
            );
            /** Initialize the internal memory that will be needed by the optimizer. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void InitializeMemory
            (
                int numDesignVariables /** numdesignvariables */ ,
                int numDesignConstraints /** numdesignconstraints */ ,
                int maxNumIterations /** maxnumiterations */ ,
                double maxConstraintViolation /** maxconstraintviolation */ ,
                double relativeConvergence /** relativeconvergence */ ,
                double absoluteConvergence /** absoluteconvergence */ ,
                double perturbationFraction /** perturbationfraction */ 
            );
            /** Initialize the optimizer with design data. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void InitializeRun
            (
                const std::vector<double> & desVarInitValues /** desvarinitvalues */ ,
                const std::vector<double> & desVarLowerValues /** desvarlowervalues */ ,
                const std::vector<double> & desVarUpperValues /** desvaruppervalues */ ,
                const std::vector<double> & constraintLimitValues /** constraintlimitvalues */ ,
                const std::vector<int> & constraintLimitTypes /** constraintlimittypes */ ,
                int objGoalType /** objgoaltype */ ,
                double objTargetValue /** objtargetvalue */ 
            );
            /** Execute the optimization for an iteration, should be called in a loop.  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int DoOptimization
            (
                const std::vector<double> & constraintRespValues /** constraintrespvalues */ ,
                double objectiveRespValue /** objectiverespvalue */ ,
                std::vector<double> & newDesVariableValues /** newdesvariablevalues */ 
            );
            /** Print optimization results test data to autotest XML file.  Must be called before terminate method. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void OptResultsPrintTestData
            (
                bool bAbsTolerance /** babstolerance */ ,
                double toleranceValue /** tolerancevalue */ 
            );
            /** Terminate optimization test and release all data memory. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void Terminate
            (
            );
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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
