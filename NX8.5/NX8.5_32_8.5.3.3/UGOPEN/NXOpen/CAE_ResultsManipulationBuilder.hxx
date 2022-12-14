#ifndef NXOpen_CAE_RESULTSMANIPULATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESULTSMANIPULATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResultsManipulationBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/CAE_ResultsManipulationBuilder.hxx>
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
        class ResultsManipulationBuilder;
    }
    class Builder;
    namespace CAE
    {
        class Result;
    }
    namespace CAE
    {
        class SimSolution;
    }
    class Unit;
    namespace CAE
    {
        class _ResultsManipulationBuilderBuilder;
        class ResultsManipulationBuilderImpl;
        /** Represents an abstract @link CAE::ResultsManipulationBuilder CAE::ResultsManipulationBuilder@endlink   <br> This is an abstract class and cannot be instantiated  <br> 
         <br>  Created in NX7.5.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ResultsManipulationBuilder : public Builder
        {
            /** Action options */
            public: enum Action
            {
                ActionExport/** export */ ,
                ActionExportResultsOnly/** no longer used */,
                ActionExportResultsAndModel/** no longer used */,
                ActionCreateImportedResult/** no longer used */,
                ActionCreateCompanionResult/** create companion result */ ,
                ActionCreateCompanionResultWithModel/** no longer used */,
                ActionCreateImportedSolution/** create imported solution */ 
            };

            /** Result Append Method options */
            public: enum ResultAppendMethod
            {
                ResultAppendMethodCreateNewLoadCases/** create new load cases */ ,
                ResultAppendMethodMergeWithPrimaryResultsData/** merge with primary results data */ 
            };

            /** Units system options */
            public: enum UnitsSystem
            {
                UnitsSystemNone/** none */ ,
                UnitsSystemFromResult/** from result */ ,
                UnitsSystemUserDefined/** user defined */ 
            };

            private: ResultsManipulationBuilderImpl * m_resultsmanipulationbuilder_impl;
            private: friend class  _ResultsManipulationBuilderBuilder;
            protected: ResultsManipulationBuilder();
            public: ~ResultsManipulationBuilder();
            /** The action 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetAction
            (
                NXOpen::CAE::ResultsManipulationBuilder::Action action /** set action */
            );
            /** The output name 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetOutputName
            (
                const NXString & outputName /** set output name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The output name 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetOutputName
            (
                const char * outputName /** set output name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The load case name 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetLoadcaseName
            (
                const NXString & loadcaseName /** set load case name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The load case name 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetLoadcaseName
            (
                const char * loadcaseName /** set load case name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The output file 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetOutputFile
            (
                const NXString & outputFile /** set output file   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The output file 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetOutputFile
            (
                const char * outputFile /** set output file   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The imported solution name if action is @link CAE::ResultsManipulationBuilder::ActionCreateImportedSolution CAE::ResultsManipulationBuilder::ActionCreateImportedSolution@endlink  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetImportedSolutionName
            (
                const NXString & importedSolutionName /** set imported solution name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The imported solution name if action is @link CAE::ResultsManipulationBuilder::ActionCreateImportedSolution CAE::ResultsManipulationBuilder::ActionCreateImportedSolution@endlink  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetImportedSolutionName
            (
                const char * importedSolutionName /** set imported solution name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The companion solution if action is @link CAE::ResultsManipulationBuilder::ActionCreateCompanionResult CAE::ResultsManipulationBuilder::ActionCreateCompanionResult@endlink  
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCompanionSolution
            (
                NXOpen::CAE::SimSolution * solution /** set companion solution */
            );
            /** The companion result name if action is @link CAE::ResultsManipulationBuilder::ActionCreateCompanionResult CAE::ResultsManipulationBuilder::ActionCreateCompanionResult@endlink  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCompanionResultName
            (
                const NXString & companionResultName /** set companion result name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The companion result name if action is @link CAE::ResultsManipulationBuilder::ActionCreateCompanionResult CAE::ResultsManipulationBuilder::ActionCreateCompanionResult@endlink  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetCompanionResultName
            (
                const char * companionResultName /** set companion result name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The append method if action is @link CAE::ResultsManipulationBuilder::ActionCreateCompanionResult CAE::ResultsManipulationBuilder::ActionCreateCompanionResult@endlink  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetAppendMethod
            (
                NXOpen::CAE::ResultsManipulationBuilder::ResultAppendMethod appendMethod /** set append method */
            );
            /** The units system 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetUnitsSystem
            (
                NXOpen::CAE::ResultsManipulationBuilder::UnitsSystem unitsSystem /** set units system */
            );
            /** The user-defined units system 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetUserDefinedUnitsSystem
            (
                const NXOpen::CAE::Result::ResultBasicUnit & unitsSystem /** set user-defined units system */
            );
            /** The result to copy the units system from 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetUnitsSystemResult
            (
                NXOpen::CAE::Result * result /** set the result for the units system */
            );
            /** The output quantity 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetOutputQuantity
            (
                NXOpen::CAE::Result::Quantity quantity /** not all values may be valid */
            );
            /** Include nodes and elements 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetIncludeModel
            (
                bool includeModel /** nodes and elements will be included */
            );
            /** Import the result immediately 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetImportResult
            (
                bool importResult /** nodes and elements will be included */
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
