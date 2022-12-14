#ifndef NXOpen_CAE_RESULTMANAGER_HXX_INCLUDED
#define NXOpen_CAE_RESULTMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResultManager.ja
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
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ResultManager;
    }
    class Session;
    namespace CAE
    {
        class ImportedResult;
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class Solution;
        }
    }
    namespace CAE
    {
        class Result;
    }
    namespace CAE
    {
        class ResultAccess;
    }
    namespace CAE
    {
        class ResultParameters;
    }
    namespace CAE
    {
        class SimSolution;
    }
    namespace CAE
    {
        class SolutionResult;
    }
    class Unit;
    namespace CAE
    {
        /** Manages results  <br> To obtain an instance of this class, refer to @link Session Session@endlink  <br> */
        class NXOPENCPPEXPORT ResultManager
        {
            private: NXOpen::Session* m_owner;
            public: explicit ResultManager(NXOpen::Session *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Creates a imported result object given a solver results file and the unit systems that these results are defined in.
                        It is user's responsibility to destroy the result object once done
                        using @link CAE::ResultManager::DeleteResult CAE::ResultManager::DeleteResult@endlink , in order to free up system resources
                     @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ImportedResult * CreateImportedResult
            (
                const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXOpen::CAE::Result::ResultBasicUnit & unitsystem /** unitsystem */ 
            );
            /** Creates a solution result object given a @link CAE::SimSolution CAE::SimSolution@endlink  
                        It is user's responsibility to destroy the result object once done
                        using @link CAE::ResultManager::DeleteResult CAE::ResultManager::DeleteResult@endlink , in order to free up system resources
                     @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SolutionResult * CreateSolutionResult
            (
                NXOpen::CAE::SimSolution * solution /** solution */ 
            );
            /** Creates a solution result object given a @link CAE::ResponseSimulation::Solution  CAE::ResponseSimulation::Solution @endlink  
                        It is user's responsibility to destroy the result object once done
                        using @link CAE::ResultManager::DeleteResult CAE::ResultManager::DeleteResult@endlink , in order to free up system resources
                     @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SolutionResult * CreateResponseSolutionResult
            (
                NXOpen::CAE::ResponseSimulation::Solution * responseSolution /** responsesolution */ 
            );
            /** Creates a result parameter object.
                        It is user's responsibility to destroy the result parameters object once done 
                        using @link CAE::ResultManager::DeleteResultParameters CAE::ResultManager::DeleteResultParameters@endlink , in order to free up system resources
                     @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ResultParameters * CreateResultParameters
            (
            );
            /** Creates a result access object
                        It is user's responsibility to destroy the result access object once done
                        using @link CAE::ResultManager::DeleteResultAccess CAE::ResultManager::DeleteResultAccess@endlink , in order to free up system resources        
                     @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ResultAccess * CreateResultAccess
            (
                NXOpen::CAE::Result * result /** analysis results for which you want to access information */,
                NXOpen::CAE::ResultParameters * parameters /** defines the specific results state you wish to access */
            );
            /** delete a @link CAE::Result  CAE::Result @endlink  object. If a @link CAE::ResultAccess  CAE::ResultAccess @endlink  object referencing it, that will also be deleted <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteResult
            (
                NXOpen::CAE::Result * result /** result */ 
            );
            /** delete a @link CAE::ResultAccess CAE::ResultAccess@endlink  object.  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteResultAccess
            (
                NXOpen::CAE::ResultAccess * result /** result */ 
            );
            /** delete a @link CAE::ResultParameters CAE::ResultParameters@endlink  object.  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteResultParameters
            (
                NXOpen::CAE::ResultParameters * result /** result */ 
            );
            /** Convert older version of ODB file to currently supported version  <br> License requirements : None */
            public: void ConvertOdbFile
            (
                const NXString & inputFileName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & outputFileName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
