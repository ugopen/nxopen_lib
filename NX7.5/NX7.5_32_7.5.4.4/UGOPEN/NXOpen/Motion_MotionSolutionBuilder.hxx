#ifndef NXOpen_MOTION_MOTIONSOLUTIONBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_MOTIONSOLUTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_MotionSolutionBuilder.ja
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
#include <NXOpen/Motion_AdamsSolverProperty.hxx>
#include <NXOpen/Motion_MotionSolutionBuilder.hxx>
#include <NXOpen/Motion_RecurdynSolverProperty.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class MotionSolutionBuilder;
    }
    class Builder;
    class Direction;
    namespace Motion
    {
        class AdamsSolverProperty;
    }
    namespace Motion
    {
        class RecurdynSolverProperty;
    }
    namespace Motion
    {
        class _MotionSolutionBuilderBuilder;
        class MotionSolutionBuilderImpl;
        /**
            Represents a @link Motion::MotionSolutionBuilder Motion::MotionSolutionBuilder@endlink 
             <br> To create a new instance of this class, use @link Motion::MotionSolutionCollection::CreateSolutionBuilder Motion::MotionSolutionCollection::CreateSolutionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  MotionSolutionBuilder : public Builder
        {
            /** Solution type */
            public: enum SolutionTypes
            {
                SolutionTypesNormal/** Normal run */,
                SolutionTypesArticulation/** Articulation run */,
                SolutionTypesSpreadsheet/** Spreadsheet run */,
                SolutionTypesFlexbody/** Flexible Body Dynamics run */
            };

            /** Analysis type */
            public: enum AnalysisTypes
            {
                AnalysisTypesDynamic/** Dynamic\Kinematic analysis */,
                AnalysisTypesStatic/** Static analysis */,
                AnalysisTypesControl/** control */ 
            };

            private: MotionSolutionBuilderImpl * m_motionsolutionbuilder_impl;
            private: friend class  _MotionSolutionBuilderBuilder;
            protected: MotionSolutionBuilder();
            public: ~MotionSolutionBuilder();
            /**Returns  the solution type  <br> License requirements : None */
            public: NXOpen::Motion::MotionSolutionBuilder::SolutionTypes SolutionType
            (
            );
            /**Sets  the solution type  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSolutionType
            (
                NXOpen::Motion::MotionSolutionBuilder::SolutionTypes solutionType /** solutiontype */ 
            );
            /**Returns  the analysis type  <br> License requirements : None */
            public: NXOpen::Motion::MotionSolutionBuilder::AnalysisTypes AnalysisType
            (
            );
            /**Sets  the analysis type  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetAnalysisType
            (
                NXOpen::Motion::MotionSolutionBuilder::AnalysisTypes analysisType /** analysistype */ 
            );
            /**Returns  the time  <br> License requirements : None */
            public: double Time
            (
            );
            /**Sets  the time  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetTime
            (
                double time /** time */ 
            );
            /**Returns  the step  <br> License requirements : None */
            public: int Step
            (
            );
            /**Sets  the step  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStep
            (
                int step /** step */ 
            );
            /**Returns  Include Static Analysis  <br> License requirements : None */
            public: bool StaticAnalysis
            (
            );
            /**Sets  Include Static Analysis  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStaticAnalysis
            (
                bool staticAnalysis /** staticanalysis */ 
            );
            /**Returns  the gravity vector  <br> License requirements : None */
            public: NXOpen::Direction * GravityVector
            (
            );
            /**Sets  the gravity vector  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetGravityVector
            (
                NXOpen::Direction * gravityVector /** gravityvector */ 
            );
            /**Returns  the gravity value  <br> License requirements : None */
            public: double GravityValue
            (
            );
            /**Sets  the gravity value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetGravityValue
            (
                double gravityValue /** gravityvalue */ 
            );
            /**Returns  the description  <br> License requirements : None */
            public: NXString Description
            (
            );
            /**Sets  the description  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /**Returns  the name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Returns  the Adams Solver property  <br> License requirements : None */
            public: NXOpen::Motion::AdamsSolverProperty * AdamsSolverProperty
            (
            );
            /**Sets  the Adams Solver property  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetAdamsSolverProperty
            (
                NXOpen::Motion::AdamsSolverProperty * adamsSolverProperty /** adamssolverproperty */ 
            );
            /**Returns  the Recurdyn Solver property  <br> License requirements : None */
            public: NXOpen::Motion::RecurdynSolverProperty * RecurdynSolverProperty
            (
            );
            /**Sets  the Recurdyn Solver property  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetRecurdynSolverProperty
            (
                NXOpen::Motion::RecurdynSolverProperty * recurdynSolverProperty /** recurdynsolverproperty */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
