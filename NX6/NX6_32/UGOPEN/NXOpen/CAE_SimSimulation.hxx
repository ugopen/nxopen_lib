#ifndef NXOpen_CAE_SIMSIMULATION_HXX_INCLUDED
#define NXOpen_CAE_SIMSIMULATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimSimulation.ja
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
        class SimSimulation;
    }
    namespace CAE
    {
        class AutoBCBuilder;
    }
    namespace CAE
    {
        class AutoPairsBuilder;
    }
    namespace CAE
    {
        class CorrelManager;
    }
    namespace CAE
    {
        class FEModelOccurrence;
    }
    namespace CAE
    {
        class LaminateMetaSol;
    }
    namespace CAE
    {
        class LaminateMetaSolBuilder;
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class Manager;
        }
    }
    namespace CAE
    {
        class SimBC;
    }
    namespace CAE
    {
        class SimBCBuilder;
    }
    namespace CAE
    {
        class SimConstraintCollection;
    }
    namespace CAE
    {
        class SimLoadCollection;
    }
    namespace CAE
    {
        class SimMotionLoadsBuilder;
    }
    namespace CAE
    {
        class SimMotionLoadsListItemBuilder;
    }
    namespace CAE
    {
        class SimRecipeCollection;
    }
    namespace CAE
    {
        class SimSimulationObjectCollection;
    }
    namespace CAE
    {
        class SimSolution;
    }
    namespace CAE
    {
        class SimSolutionStep;
    }
    class NXObject;
    namespace CAE
    {
        class _SimSimulationBuilder;
        /**  @brief  This is the root object in a .sim file. Only one instance of this class will exist in each fem part file 

           <br> To obtain an instance of this class, use @link CAE::SimPart::Simulation CAE::SimPart::Simulation@endlink  <br> */
        class NXOPENCPPEXPORT SimSimulation : public NXObject
        {
            private: friend class  _SimSimulationBuilder;
            protected: SimSimulation();
            /**Returns  the active solution
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimSolution * ActiveSolution
            (
            );
            /**Sets  the active solution
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetActiveSolution
            (
                NXOpen::CAE::SimSolution * activeSolution /** the active solution  @link CAE::SimSolution CAE::SimSolution@endlink */
            );
            /** Creates a solution
                      @return  the created @link CAE::SimSolution CAE::SimSolution@endlink   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimSolution * CreateSolution
            (
                const NXString & solverType /** name of the solver   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & analysisType /** name of the analysis type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & solutionType /** name of the solution type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & name /** name of the solution to be created   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Delete the solution
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteSolution
            (
                NXOpen::CAE::SimSolution * solution /** the @link CAE::SimSolution CAE::SimSolution@endlink  to be deleted */
            );
            /** Clone the solution
                      @return  the  newly created @link CAE::SimSolution CAE::SimSolution@endlink    <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimSolution * CloneSolution
            (
                NXOpen::CAE::SimSolution * oldSolution /** the @link CAE::SimSolution CAE::SimSolution@endlink  to be cloned */,
                const NXString & suggestedName /** name to use instead of default name (may be NULL)   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a step and add to the solution
                      @return  step @link CAE::SimSolutionStep CAE::SimSolutionStep@endlink  to be added  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimSolutionStep * CreateSolutionStep
            (
                NXOpen::CAE::SimSolution * solution /** the solution to which the step will be added,
                                                                                                 if a null is passed the current active solution
                                                                                                 will be used */,
                int stepType /** index of the step type */,
                const NXString & name /** name of the step   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a BC builder for the load descriptor passed
                      @return  bc builder  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimBCBuilder * CreateBcBuilderForLoadDescriptor
            (
                const NXString & bcDescName /** name of the load descriptor   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & bcName /** name of the load to be created   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a BC builder for the constraint descriptor passed
                      @return  bc builder  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimBCBuilder * CreateBcBuilderForConstraintDescriptor
            (
                const NXString & bcDescName /** name of the constraint descriptor   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & bcName /** name of the constraint to be created   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a BC builder for the simulation object descriptor passed
                      @return  bc builder  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimBCBuilder * CreateBcBuilderForSimulationObjectDescriptor
            (
                const NXString & bcDescName /** name of the simulation object descriptor   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & bcName /** name of the simulation object to be created   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a BC builder for the BC passed
                      @return  bc builder  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimBCBuilder * CreateBcBuilderForBc
            (
                NXOpen::CAE::SimBC * bc /** bc object */
            );
            /** Adds the boundary condition to the step in the solution passed.
                        If solution is NULL then the boundary condition is added to the active solution
                        If step is NULL then the boundary condition is added to the active step
                      <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AddBc
            (
                NXOpen::CAE::SimBC * bc /** bc object */,
                NXOpen::CAE::SimSolution * solution /** solution */,
                NXOpen::CAE::SimSolutionStep * solutionStep /** solution step */
            );
            /** Creates a @link CAE::AutoPairsBuilder CAE::AutoPairsBuilder@endlink   @return  The AutoPairsBuilder object  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AutoPairsBuilder * CreateAutoPairsBuilder
            (
                const NXString & pcBCDescName /** The neutral name of the AutoPairsDescriptor.    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a @link CAE::AutoBCBuilder CAE::AutoBCBuilder@endlink   @return  The AutoBCBuilder object 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AutoBCBuilder * CreateAutoBcBuilder
            (
                const NXString & pcBCDescName /** The neutral name of the LBCDescriptor.    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a @link CAE::AutoBCBuilder CAE::AutoBCBuilder@endlink   @return  The AutoBCBuilder object  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AutoBCBuilder * CreateAutoBcBuilder
            (
                const NXString & pcBCDescName /** The neutral name of the LBCDescriptor.    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & pcRecipeName /** The name of the AutoBCRecipe    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the femodeloccurrence @link  CAE::FEModelOccurrence   CAE::FEModelOccurrence @endlink  assoicated with the simulation object
                     <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::FEModelOccurrence * Femodel
            (
            );
            /** Creates a @link CAE::SimMotionLoadsBuilder CAE::SimMotionLoadsBuilder@endlink   @return  The SimMotionLoadsBuilder object  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimMotionLoadsBuilder * CreateMotionLoadsBuilder
            (
            );
            /** Creates a @link CAE::SimMotionLoadsListItemBuilder CAE::SimMotionLoadsListItemBuilder@endlink   @return  The SimMotionLoadsListItemBuilder object  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimMotionLoadsListItemBuilder * CreateMotionLoadsListItemBuilder
            (
            );
            /** Creates a @link CAE::LaminateMetaSolBuilder CAE::LaminateMetaSolBuilder@endlink   @return   <br> License requirements : nx_lam_composites ("Laminate Composites") */
            public: NXOpen::CAE::LaminateMetaSolBuilder * CreateLaminateMetaSolBuilder
            (
                NXOpen::CAE::LaminateMetaSol * tMetaSol /** tmetasol */ 
            );


            private: NXOpen::CAE::SimLoadCollection *loads;
            /** Returns the load collection belonging to this sim part */
            public: NXOpen::CAE::SimLoadCollection *Loads()
            {
                return loads;
            }
            private: NXOpen::CAE::SimConstraintCollection *constraints;
            /** Returns the constraint collection belonging to this sim part */
            public: NXOpen::CAE::SimConstraintCollection *Constraints()
            {
                return constraints;
            }
            private: NXOpen::CAE::SimSimulationObjectCollection *simulationObjects;
            /** Returns the simulation object collection belonging to this sim part */
            public: NXOpen::CAE::SimSimulationObjectCollection *SimulationObjects()
            {
                return simulationObjects;
            }
            private: NXOpen::CAE::ResponseSimulation::Manager *responseSimulationManager;
            /** Returns the response simulation manager belonging to this sim part */
            public: NXOpen::CAE::ResponseSimulation::Manager *ResponseSimulationManager()
            {
                return responseSimulationManager;
            }
            private: NXOpen::CAE::CorrelManager *correlManager;
            /** Returns the correl manager belonging to this sim part */
            public: NXOpen::CAE::CorrelManager *CorrelManager()
            {
                return correlManager;
            }
            private: NXOpen::CAE::SimRecipeCollection *simulationRecipes;
            /** Returns the simulation recipe collection belonging to this sim part */
            public: NXOpen::CAE::SimRecipeCollection *SimulationRecipes()
            {
                return simulationRecipes;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
