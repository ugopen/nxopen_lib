#ifndef NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_STUDY_HXX_INCLUDED
#define NXOpen_FEATURES_TOPOLOGYOPTIMIZATION_STUDY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TopologyOptimization_Study.ja
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
#include <NXOpen/Features_TopologyOptimization_AnalysisConstraint.hxx>
#include <NXOpen/Features_TopologyOptimization_AnalysisConstraintBuilder.hxx>
#include <NXOpen/Features_TopologyOptimization_AnalysisLoad.hxx>
#include <NXOpen/Features_TopologyOptimization_AnalysisLoadBuilder.hxx>
#include <NXOpen/Features_TopologyOptimization_Connection.hxx>
#include <NXOpen/Features_TopologyOptimization_ConnectionBuilder.hxx>
#include <NXOpen/Features_TopologyOptimization_ConstructionBody.hxx>
#include <NXOpen/Features_TopologyOptimization_ConstructionBodyBuilder.hxx>
#include <NXOpen/Features_TopologyOptimization_ConstructionBodyCollector.hxx>
#include <NXOpen/Features_TopologyOptimization_DesignSpace.hxx>
#include <NXOpen/Features_TopologyOptimization_DesignSpaceBuilder.hxx>
#include <NXOpen/Features_TopologyOptimization_OptimizationConstraint.hxx>
#include <NXOpen/Features_TopologyOptimization_OptimizationConstraintBuilder.hxx>
#include <NXOpen/Features_TopologyOptimization_SceneryBody.hxx>
#include <NXOpen/Features_TopologyOptimization_SceneryBodyBuilder.hxx>
#include <NXOpen/Features_TopologyOptimization_ShapeConstraint.hxx>
#include <NXOpen/Features_TopologyOptimization_ShapeConstraintBuilder.hxx>
#include <NXOpen/Features_TopologyOptimization_StudyBuilder.hxx>
#include <NXOpen/Features_TopologyOptimization_Subcase.hxx>
#include <NXOpen/Features_TopologyOptimization_SubcaseManager.hxx>
#include <NXOpen/Features_TopologyOptimization_Container.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace TopologyOptimization
        {
            class Study;
        }
    }
    class Body;
    namespace Features
    {
        namespace TopologyOptimization
        {
            class AnalysisConstraint;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class AnalysisConstraintBuilder;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class AnalysisLoad;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class AnalysisLoadBuilder;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class Connection;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class ConnectionBuilder;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class ConstructionBody;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class ConstructionBodyBuilder;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class ConstructionBodyCollector;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class Container;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class DesignSpace;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class DesignSpaceBuilder;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class OptimizationConstraint;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class OptimizationConstraintBuilder;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class SceneryBody;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class SceneryBodyBuilder;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class ShapeConstraint;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class ShapeConstraintBuilder;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class Subcase;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class SubcaseManager;
        }
    }
    namespace Features
    {
        namespace TopologyOptimization
        {
            class _StudyBuilder;
            class StudyImpl;
            /** Represents a Topology Optimization Study  <br> To create or edit an instance of this class, use @link NXOpen::Features::TopologyOptimization::StudyBuilder  NXOpen::Features::TopologyOptimization::StudyBuilder @endlink  <br> 
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  Study : public NXOpen::Features::TopologyOptimization::Container
            {
                private: StudyImpl * m_study_impl;
                private: friend class  _StudyBuilder;
                protected: Study();
                public: ~Study();
                /**Returns  the analysis type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::StudyBuilder::AnalysisOption AnalysisType
                (
                );
                /**Sets  the analysis type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetAnalysisType
                (
                    NXOpen::Features::TopologyOptimization::StudyBuilder::AnalysisOption type /** type */ 
                );
                /**Returns  the optimization objective type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::TopologyOptimization::StudyBuilder::OptimizationObjectiveOption OptimizationObjective
                (
                );
                /**Sets  the optimization objective type 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void SetOptimizationObjective
                (
                    NXOpen::Features::TopologyOptimization::StudyBuilder::OptimizationObjectiveOption objective /** objective */ 
                );
                /** Optimizes (solves) this @link NXOpen::Features::TopologyOptimization::Study NXOpen::Features::TopologyOptimization::Study@endlink  if the optimization is fully setup and ready to optimize.
                                The optimization (solve) can be executed independent of the owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  state.
                                The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  could be suppressed or delayed for update.

                                This method will return aftering pre-processing and launching the optimization process to run independent of the NX session. In other words, the
                                method will not wait for the topology optimization process to complete.

                                Optimization results from the solve need to be loaded into the @link NXOpen::Features::TopologyOptimization::Study NXOpen::Features::TopologyOptimization::Study@endlink  object by calling
                                @link NXOpen::Features::TopologyOptimization::Study::RetrieveOptimizationResults NXOpen::Features::TopologyOptimization::Study::RetrieveOptimizationResults@endlink .
                            
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void RunOptimization
                (
                );
                /** Terminates the optimization process, if any, for this @link NXOpen::Features::TopologyOptimization::Study NXOpen::Features::TopologyOptimization::Study@endlink  after it was launched using
                                @link NXOpen::Features::TopologyOptimization::Study::RunOptimization NXOpen::Features::TopologyOptimization::Study::RunOptimization@endlink  and before the process completes or errors out. Calling this method
                                does not guarantee that the optimization process will indeed terminate; process state is subject to its progress, hardware and software resources,
                                the real time elapsed since it was launched, and other factors. Returns TRUE if the process was previously running and indeed stopped by this method.
                                Aborting the optimization will NOT produce partial results and the optimization cannot be resumed (restarted) after being terminated.
                            
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: bool AbortOptimizationProcess
                (
                );
                /** Loads results and the optimized bodies from the optimization into this @link NXOpen::Features::TopologyOptimization::Study NXOpen::Features::TopologyOptimization::Study@endlink  when the process has completed. 
                                This method follows @link NXOpen::Features::TopologyOptimization::Study::RunOptimization NXOpen::Features::TopologyOptimization::Study::RunOptimization@endlink  and will wait for topology optimization process to complete.
                                The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  should be active (i.e. not suppressed) before calling this method.
                            
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void RetrieveOptimizationResults
                (
                );
                /** Delete optimization results from a completed optimization process instead of loading them into this @link NXOpen::Features::TopologyOptimization::Study NXOpen::Features::TopologyOptimization::Study@endlink .
                                This method follows @link NXOpen::Features::TopologyOptimization::Study::RunOptimization NXOpen::Features::TopologyOptimization::Study::RunOptimization@endlink  and will wait for topology optimization process to complete.
                                Use @link NXOpen::Features::TopologyOptimization::Study::AbortOptimizationProcess NXOpen::Features::TopologyOptimization::Study::AbortOptimizationProcess@endlink  to terminate a running optimization process and delete in-process results.
                                The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  should be active (i.e. not suppressed) before calling this method.
                            
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void DiscardUnretrievedOptimizationResults
                (
                );
                /** Unlocks the @link NXOpen::Features::TopologyOptimization::Study NXOpen::Features::TopologyOptimization::Study@endlink  if it is read-only. This method can be used to make a @link NXOpen::Features::TopologyOptimization::Study NXOpen::Features::TopologyOptimization::Study@endlink 
                                editable if optimization results could not be loaded due to errors or due to missing data. Use @link NXOpen::Features::TopologyOptimization::Study::AbortOptimizationProcess NXOpen::Features::TopologyOptimization::Study::AbortOptimizationProcess@endlink  to
                                terminate a running optimization process or @link NXOpen::Features::TopologyOptimization::Study::DiscardUnretrievedOptimizationResults NXOpen::Features::TopologyOptimization::Study::DiscardUnretrievedOptimizationResults@endlink  to delete results instead of loading them.
                                The owning @link NXOpen::Features::TopologyOptimizationFeature NXOpen::Features::TopologyOptimizationFeature@endlink  should be active (i.e. not suppressed) before calling this method.
                            
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void Unlock
                (
                );
                /** Get optimized bodies for this @link NXOpen::Features::TopologyOptimization::Study NXOpen::Features::TopologyOptimization::Study@endlink   @return  the optimized bodies 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::Body *> GetOptimizedBodies
                (
                );
                /** Discards optimization results and the optimized bodies for this @link NXOpen::Features::TopologyOptimization::Study NXOpen::Features::TopologyOptimization::Study@endlink  if the topology optimization was previous executed. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: void DiscardOptimizationResults
                (
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::SceneryBody NXOpen::Features::TopologyOptimization::SceneryBody@endlink  
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::SceneryBodyBuilder * CreateSceneryBodyBuilder
                (
                    NXOpen::Features::TopologyOptimization::SceneryBody * topOptSceneryBody /** topoptscenerybody */ 
                );
                /** Gets all @link NXOpen::Features::TopologyOptimization::SceneryBody NXOpen::Features::TopologyOptimization::SceneryBody@endlink  objects from the given study. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: void GetAllSceneryBodies
                (
                    std::vector<NXOpen::Features::TopologyOptimization::SceneryBody *> & topOptSceneryBodies /** topoptscenerybodies */ 
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::Connection NXOpen::Features::TopologyOptimization::Connection@endlink  
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::ConnectionBuilder * CreateConnectionBuilder
                (
                    NXOpen::Features::TopologyOptimization::Connection * connection /** connection */ 
                );
                /** Gets all @link NXOpen::Features::TopologyOptimization::Connection NXOpen::Features::TopologyOptimization::Connection@endlink  objects from the given study. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: void GetAllConnections
                (
                    std::vector<NXOpen::Features::TopologyOptimization::Connection *> & topOptConnections /** topoptconnections */ 
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::AnalysisConstraintBuilder NXOpen::Features::TopologyOptimization::AnalysisConstraintBuilder@endlink  
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::AnalysisConstraintBuilder * CreateAnalysisConstraintBuilder
                (
                    NXOpen::Features::TopologyOptimization::AnalysisConstraint * constraint /** constraint */ 
                );
                /** Gets all @link NXOpen::Features::TopologyOptimization::AnalysisConstraint NXOpen::Features::TopologyOptimization::AnalysisConstraint@endlink  objects from the given study. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: void GetAllAnalysisConstraints
                (
                    std::vector<NXOpen::Features::TopologyOptimization::AnalysisConstraint *> & analysisConstraints /** analysisconstraints */ 
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::DesignSpaceBuilder NXOpen::Features::TopologyOptimization::DesignSpaceBuilder@endlink  
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::DesignSpaceBuilder * CreateDesignSpaceBuilder
                (
                    NXOpen::Features::TopologyOptimization::DesignSpace * designSpace /** designspace */ 
                );
                /** Gets all @link NXOpen::Features::TopologyOptimization::DesignSpace NXOpen::Features::TopologyOptimization::DesignSpace@endlink  objects from the given study. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: void GetAllDesignSpaces
                (
                    std::vector<NXOpen::Features::TopologyOptimization::DesignSpace *> & designSpaces /** designspaces */ 
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::AnalysisLoad NXOpen::Features::TopologyOptimization::AnalysisLoad@endlink  
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::AnalysisLoadBuilder * CreateAnalysisLoadBuilder
                (
                    NXOpen::Features::TopologyOptimization::AnalysisLoad * load /** load */ 
                );
                /** Gets all @link NXOpen::Features::TopologyOptimization::AnalysisLoad NXOpen::Features::TopologyOptimization::AnalysisLoad@endlink  objects from the given study. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: void GetAllAnalysisLoads
                (
                    std::vector<NXOpen::Features::TopologyOptimization::AnalysisLoad *> & analysisLoads /** analysisloads */ 
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::OptimizationConstraintBuilder NXOpen::Features::TopologyOptimization::OptimizationConstraintBuilder@endlink  
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::OptimizationConstraintBuilder * CreateOptimizationConstraintBuilder
                (
                    NXOpen::Features::TopologyOptimization::OptimizationConstraint * optConstraint /** optconstraint */ 
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::SubcaseManager NXOpen::Features::TopologyOptimization::SubcaseManager@endlink  
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::SubcaseManager * CreateSubcaseManager
                (
                );
                /** Gets all @link NXOpen::Features::TopologyOptimization::Subcase NXOpen::Features::TopologyOptimization::Subcase@endlink  objects from the given study. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: void GetAllSubcases
                (
                    std::vector<NXOpen::Features::TopologyOptimization::Subcase *> & subcases /** subcases */ 
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::ConstructionBodyBuilder NXOpen::Features::TopologyOptimization::ConstructionBodyBuilder@endlink  that can be used to create one or more @link NXOpen::Features::TopologyOptimization::ConstructionBody NXOpen::Features::TopologyOptimization::ConstructionBody@endlink  objects,
                            a single @link NXOpen::Features::TopologyOptimization::ConstructionBodyCollector NXOpen::Features::TopologyOptimization::ConstructionBodyCollector@endlink  object, or to edit a single @link NXOpen::Features::TopologyOptimization::ConstructionBody NXOpen::Features::TopologyOptimization::ConstructionBody@endlink  object. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::ConstructionBodyBuilder * CreateConstructionBodyBuilder
                (
                    NXOpen::Features::TopologyOptimization::ConstructionBody * topOptConstructionBody /** topoptconstructionbody */ 
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::ConstructionBodyBuilder NXOpen::Features::TopologyOptimization::ConstructionBodyBuilder@endlink  that can be used to edit a single @link NXOpen::Features::TopologyOptimization::ConstructionBodyCollector NXOpen::Features::TopologyOptimization::ConstructionBodyCollector@endlink  object. 
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::ConstructionBodyBuilder * CreateConstructionBodyCollectorBuilder
                (
                    NXOpen::Features::TopologyOptimization::ConstructionBodyCollector * constrBodyCollector /** constrbodycollector */ 
                );
                /** Creates a @link NXOpen::Features::TopologyOptimization::ShapeConstraint NXOpen::Features::TopologyOptimization::ShapeConstraint@endlink  
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::ShapeConstraintBuilder * CreateShapeConstraintBuilder
                (
                    NXOpen::Features::TopologyOptimization::ShapeConstraint * topOptShapeConstraint /** topoptshapeconstraint */ 
                );
                /** Clones (copies) a @link NXOpen::Features::TopologyOptimization::Subcase NXOpen::Features::TopologyOptimization::Subcase@endlink  object and returns the cloned (copied) object if successful. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::Subcase * CloneSubcase
                (
                    NXOpen::Features::TopologyOptimization::Subcase * existingSubcase /** existingsubcase */ 
                );
                /** Clones (copies) a @link NXOpen::Features::TopologyOptimization::AnalysisLoad NXOpen::Features::TopologyOptimization::AnalysisLoad@endlink  object and returns the cloned (copied) object if successful. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::AnalysisLoad * CloneAnalysisLoad
                (
                    NXOpen::Features::TopologyOptimization::AnalysisLoad * existingload /** existingload */ 
                );
                /** Clones (copies) a @link NXOpen::Features::TopologyOptimization::AnalysisConstraint NXOpen::Features::TopologyOptimization::AnalysisConstraint@endlink  object and returns the cloned (copied) object if successful. 
                 <br>  Created in NX1980.0.0.  <br>  
                 <br> License requirements : des_top_opt ("Topology Optimization for Designers") OR sc_des_topol_opt (" Topology Optimization for Designers") */
                public: NXOpen::Features::TopologyOptimization::AnalysisConstraint * CloneAnalysisConstraint
                (
                    NXOpen::Features::TopologyOptimization::AnalysisConstraint * existingConstraint /** existingconstraint */ 
                );
            };
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