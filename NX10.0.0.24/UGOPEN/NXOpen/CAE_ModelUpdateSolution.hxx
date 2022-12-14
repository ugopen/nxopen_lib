#ifndef NXOpen_CAE_MODELUPDATESOLUTION_HXX_INCLUDED
#define NXOpen_CAE_MODELUPDATESOLUTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelUpdateSolution.ja
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
#include <NXOpen/CAE_ModelUpdateCorrelMethodBuilder.hxx>
#include <NXOpen/CAE_ModelUpdateOptimOptionsBuilder.hxx>
#include <NXOpen/CAE_ModelUpdateOptionsBuilder.hxx>
#include <NXOpen/CAE_ModelUpdateOverallWeightsBuilder.hxx>
#include <NXOpen/CAE_CorrelSolution.hxx>
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
        class ModelUpdateSolution;
    }
    namespace CAE
    {
        class CorrelSolution;
    }
    namespace CAE
    {
        class ModelUpdateCorrelMethodBuilder;
    }
    namespace CAE
    {
        class ModelUpdateDesignVariable;
    }
    namespace CAE
    {
        class ModelUpdateDesignVariablesCollection;
    }
    namespace CAE
    {
        class ModelUpdateOptimOptionsBuilder;
    }
    namespace CAE
    {
        class ModelUpdateOptionsBuilder;
    }
    namespace CAE
    {
        class ModelUpdateOverallWeightsBuilder;
    }
    namespace CAE
    {
        class _ModelUpdateSolutionBuilder;
        class ModelUpdateSolutionImpl;
        /** Represents a @link NXOpen::CAE::ModelUpdateSolution NXOpen::CAE::ModelUpdateSolution@endlink , which is a meta-solution used to update finite element models to match real life test data  <br> To create or edit an instance of this class, use @link NXOpen::CAE::ModelUpdateSolutionBuilder  NXOpen::CAE::ModelUpdateSolutionBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ModelUpdateSolution : public NXOpen::CAE::CorrelSolution
        {
            /** Represents the type when export to targets and errors to csv file */
            public: enum TargetType
            {
                TargetTypeAll/** Export all the targets to the csv file */,
                TargetTypeFrequencies/** Export all the frequency targets to the csv file*/,
                TargetTypeModeShapes/** Export all the mode shape targets to the csv file */
            };

            private: ModelUpdateSolutionImpl * m_modelupdatesolution_impl;
            private: friend class  _ModelUpdateSolutionBuilder;
            protected: ModelUpdateSolution();
            public: ~ModelUpdateSolution();
            /** Creates the builder object of model update options  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NXOpen::CAE::ModelUpdateOptionsBuilder * CreateOptionsBuilder
            (
            );
            /** Creates the builder object of model update optimize options  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NXOpen::CAE::ModelUpdateOptimOptionsBuilder * CreateOptimOptionsBuilder
            (
            );
            /** Gets the number of design variables  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: int GetDesignVarNumber
            (
            );
            /** Sets a specific design variable as active or not 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetDesignVarActive
            (
                int designVarIndex /** index of design variable */,
                bool active /** activate or deactivate flag */
            );
            /** Sets value for a specific design variable 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetDesignVarValue
            (
                int designVarIndex /** index of design variable */,
                double value /** new value of design variable */
            );
            /** Sets lower bound for a specific design variable 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetDesignVarLowerBound
            (
                int designVarIndex /** index of design variable */,
                double lowerBound /** new lower bound value of design variable */
            );
            /** Sets upper bound for a specific design variable 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetDesignVarUpperBound
            (
                int designVarIndex /** index of design variable */,
                double upperBound /** new upper bound value of design variable */
            );
            /** Sets weight for a specific design variable 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetDesignVarWeight
            (
                int designVarIndex /** index of design variable */,
                double weight /** new weight value of design variable */
            );
            /** Calculates errors 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void CalculateErrors
            (
            );
            /** Resets the design variables 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void ResetDesignVariables
            (
            );
            /** Sets the value of the design variables. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetDesignVariablesInitialValue
            (
                double initialValue /** initial value */ 
            );
            /** Resets the targets 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void ResetTargets
            (
            );
            /** Sets active status for a specific frequency target 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetFreqTargetActive
            (
                int freqTargetIndex /** index of frequency target */,
                bool active /** new active status of frequency target */
            );
            /** Sets active status for a specific mode shape target 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetModeShapeTargetActive
            (
                int modeShapeTargetIndex /** index of mode shape target */,
                bool active /** new active status of mode shape target */
            );
            /** Sets weight for a specific frequency target 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetFreqTargetWeight
            (
                int freqTargetIndex /** index of frequency target */,
                double weight /** new weight value of frequency target */
            );
            /** Sets weight for a specific mode shape target 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void SetModeShapeTargetWeight
            (
                int modeShapeTargetIndex /** index of mode shape target */,
                double modeShapeWeight /** new weight value of mode shape target */
            );
            /** Creates the builder object of model update overall weights  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NXOpen::CAE::ModelUpdateOverallWeightsBuilder * CreateOverallWeightsBuilder
            (
            );
            /** Creates the builder object of model update correlation method  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NXOpen::CAE::ModelUpdateCorrelMethodBuilder * CreateCorrelMethodBuilder
            (
            );
            /** Update the design variable modeling objects 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void UpdateDesignVariables
            (
            );
            /** Update the finite element model 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void UpdateFiniteElementModel
            (
            );
            /** Export the model update design variables to the csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void ExportDesignVariablesCsvFile
            (
                const NXString & fileName /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export the model update design variables to the csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            void ExportDesignVariablesCsvFile
            (
                const char * fileName /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export the model update sensitivities to the csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void ExportSensitivitiesCsvFile
            (
                const NXString & fileName /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export the model update sensitivities to the csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            void ExportSensitivitiesCsvFile
            (
                const char * fileName /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export the model update errors to the csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void ExportErrorsCsvFile
            (
                NXOpen::CAE::ModelUpdateSolution::TargetType targetType /** Target type of export to csv file */,
                const NXString & fileName /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export the model update errors to the csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            void ExportErrorsCsvFile
            (
                NXOpen::CAE::ModelUpdateSolution::TargetType targetType /** Target type of export to csv file */,
                const char * fileName /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export the model update targets to the csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: void ExportTargetsCsvFile
            (
                NXOpen::CAE::ModelUpdateSolution::TargetType tagetType /** Target type of export to csv file */,
                const NXString & fileName /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export the model update targets to the csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            void ExportTargetsCsvFile
            (
                NXOpen::CAE::ModelUpdateSolution::TargetType tagetType /** Target type of export to csv file */,
                const char * fileName /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Make a clone of a model update solution.  @return  Cloned solution 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NXOpen::CAE::ModelUpdateSolution * CloneModelupdate
            (
            );
            /** Returns the design variables in the model update solution @return  
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::CAE::ModelUpdateDesignVariable *> GetDesignVariables
            (
            );


            /** The design variables collection for this meta solution. 
             <br>  Created in NX8.0.1.  <br>  
            */
            public: NXOpen::CAE::ModelUpdateDesignVariablesCollection *DesignVariables();
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
