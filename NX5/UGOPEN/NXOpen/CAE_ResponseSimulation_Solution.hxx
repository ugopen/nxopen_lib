#ifndef NXOpen_CAE_RESPONSESIMULATION_SOLUTION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_SOLUTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_Solution.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class Solution;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class FrfEvaluationSetting;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ModalProperties;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class RSEvent;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class TransmissibilityEvaluationSetting;
        }
    }
    class NXObject;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _SolutionBuilder;
            /** Represents a meta solution providing response analysis functionalities in the .sim file  */
            class NXOPENCPPEXPORT Solution : public NXObject
            {
                private: friend class  _SolutionBuilder;
                protected: Solution();
                /** Returns the response simulation solution name  @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXString GetSolutionName
                (
                );
                /** Sets the response simulation solution name  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetSolutionName
                (
                    const NXString & solutionName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    bool renameResultFile /** if there are result files associated with the solution, rename the files or not*/
                );
                /** Deletes a response simulation solution, including all events and excitations
                            under it  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void Destroy
                (
                    bool deleteResultFile /** delete the result files associated with the solution or not */
                );
                /** Returns the modal properties of Response Analysis Meta solution @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::ModalProperties * GetModalProperties
                (
                );
                /** Returns all the events of the solution @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: std::vector<NXOpen::CAE::ResponseSimulation::RSEvent *> GetEvents
                (
                );
                /** Imports an event to the solution  @return    <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::RSEvent * ImportEvent
                (
                    const NXString & event_definition_file /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                    const NXString & suggested_name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Clones an event to the solution  @return    <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::RSEvent * CloneEvent
                (
                    NXOpen::CAE::ResponseSimulation::RSEvent * source_event /** source event */ ,
                    const NXString & suggested_name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /**Returns  the active event  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::RSEvent * ActiveEvent
                (
                );
                /**Sets  the active event  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetActiveEvent
                (
                    NXOpen::CAE::ResponseSimulation::RSEvent * active_event /** active event */ 
                );
                /** Returns the result file name of solution  @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXString GetResultFileName
                (
                );
                /** Performs evaluation for FRF. The evaluation results will be stored in an AFU file, 
                        which name could be returned by @link CAE::ResponseSimulation::Solution::GetResultFileName CAE::ResponseSimulation::Solution::GetResultFileName@endlink   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void EvaluateFrf
                (
                    NXOpen::CAE::ResponseSimulation::FrfEvaluationSetting * evaluation_setting /** evaluation setting */ 
                );
                /** Performs evaluation for transimissibility. The evaluation results will be stored in an AFU file,
                        which name could be returned by @link CAE::ResponseSimulation::Solution::GetResultFileName CAE::ResponseSimulation::Solution::GetResultFileName@endlink   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void EvaluateTransmissibility
                (
                    NXOpen::CAE::ResponseSimulation::TransmissibilityEvaluationSetting * evaluation_setting /** evaluation setting */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif