#ifndef NXOpen_CAE_DURABILITYSOLVERBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURABILITYSOLVERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurabilitySolverBuilder.ja
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
#include <NXOpen/CAE_DurabilitySolverBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class DurabilitySolverBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _DurabilitySolverBuilderBuilder;
        class DurabilitySolverBuilderImpl;
        /** Represents the builder for solving the durability solution process. 
                When solving a solution process, the software checks to see which of the active
                events it needs to solve. It solves them first followed by solving the durability
                solution process. The result file for the durability solution process will contain
                worst case results for safety factors and cumulative damage from the active events.
                Only the solution process file will be overwritten every time this builder is committed.
             <br> To create a new instance of this class, use @link CAE::DurabilityManager::CreateSolverBuilder CAE::DurabilityManager::CreateSolverBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ActiveEventSolveOptions </td> <td> 
         
        Unsolved </td> </tr> 

        <tr><td> 
         
        CreateDiagnosticGroups </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ModelCheck </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SubmitOptions </td> <td> 
         
        Solve </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  DurabilitySolverBuilder : public Builder
        {
            /** the submit options enum.*/
            public: enum SubmitOptionsEnum
            {
                SubmitOptionsEnumSolve/** Solve */
            };

            /** the active event solve options enum.*/
            public: enum ActiveEventSolveOptionsEnum
            {
                ActiveEventSolveOptionsEnumUnsolved/** Unsolved */,
                ActiveEventSolveOptionsEnumAll/** All */
            };

            private: DurabilitySolverBuilderImpl * m_durabilitysolverbuilder_impl;
            private: friend class  _DurabilitySolverBuilderBuilder;
            protected: DurabilitySolverBuilder();
            public: ~DurabilitySolverBuilder();
            /**Returns  the submit options.  <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilitySolverBuilder::SubmitOptionsEnum SubmitOptions
            (
            );
            /**Sets  the submit options.  <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetSubmitOptions
            (
                NXOpen::CAE::DurabilitySolverBuilder::SubmitOptionsEnum submitOptions /** submitoptions */ 
            );
            /**Returns  the active event solve options.  <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilitySolverBuilder::ActiveEventSolveOptionsEnum ActiveEventSolveOptions
            (
            );
            /**Sets  the active event solve options.  <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetActiveEventSolveOptions
            (
                NXOpen::CAE::DurabilitySolverBuilder::ActiveEventSolveOptionsEnum activeEventSolveOptions /** activeeventsolveoptions */ 
            );
            /**Returns  the model check.  <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: bool ModelCheck
            (
            );
            /**Sets  the model check.  <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetModelCheck
            (
                bool modelCheck /** modelcheck */ 
            );
            /**Returns  the create diagnostic groups.  <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: bool CreateDiagnosticGroups
            (
            );
            /**Sets  the create diagnostic groups.  <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetCreateDiagnosticGroups
            (
                bool createDiagnosticGroups /** creatediagnosticgroups */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif