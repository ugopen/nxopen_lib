#ifndef NXOpen_CAE_CORRELSOLUTION_HXX_INCLUDED
#define NXOpen_CAE_CORRELSOLUTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelSolution.ja
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
#include <NXOpen/NXObject.hxx>
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
        class CorrelSolution;
    }
    namespace CAE
    {
        class CorrelModePairingBuilder;
    }
    namespace CAE
    {
        class SimSolution;
    }
    class NXObject;
    namespace CAE
    {
        /** shape Metric Code */
        enum CorrelShapemetrictype
        {
            CorrelShapemetrictypeMac/** Shape metric type is Modal Assurance Criteria*/,
            CorrelShapemetrictypeComac/** Shape metric type is Coordinate Modal Assurance Criteria*/,
            CorrelShapemetrictypeMsf/** Shape metric type is Modal Scale Factors*/,
            CorrelShapemetrictypeXortho/** Shape metric type is Cross Orthogonality*/,
            CorrelShapemetrictypeNco/** Shape metric type is Normalized Cross Orthogonality*/,
            CorrelShapemetrictypeSco/** Shape metric type is SEREP-Cross-Orthogonality*/
        };

    }
    namespace CAE
    {
        class _CorrelSolutionBuilder;
        class CorrelSolutionImpl;
        /** Represents a @link NXOpen::CAE::CorrelSolution NXOpen::CAE::CorrelSolution@endlink , which is a meta-solution used to compare results from two structural dynamics solutions  <br> To create or edit an instance of this class, use @link NXOpen::CAE::CorrelSolutionBuilder  NXOpen::CAE::CorrelSolutionBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CorrelSolution : public NXOpen::NXObject
        {
            private: CorrelSolutionImpl * m_correlsolution_impl;
            private: friend class  _CorrelSolutionBuilder;
            protected: CorrelSolution();
            public: ~CorrelSolution();
            /** Creates the builder object for mode pairing editing  @return   
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::CorrelModePairingBuilder * CreateModePairingBuilder
            (
            );
            /** Returns the correlation solution name  @return  the @link NXOpen::CAE::CorrelSolution NXOpen::CAE::CorrelSolution@endlink   name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetSolutionName
            (
            );
            /** Sets the correlation solution name
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetSolutionName
            (
                const NXString & solutionName /** new solution name */,
                bool renameResultFile /** if there are result files associated with the solution, rename the files or not*/
            );
            /** Sets the correlation solution name
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            void SetSolutionName
            (
                const char * solutionName /** new solution name */,
                bool renameResultFile /** if there are result files associated with the solution, rename the files or not*/
            );
            /** Deletes a correlation solution 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void Destroy
            (
                bool deleteResultFile /** delete the result files associated with the solution or not */
            );
            /** Computes the Model Assurance Criterion (MAC) correlation metric for active modes  @return  the MAC values computed 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: std::vector<double> ComputeMacs
            (
                std::vector<double> & referenceModeFrequencies /** ref mode frequencies */,
                std::vector<int> & referenceModeNumbers /** ref mode numbers */,
                std::vector<double> & workModeFrequencies /** work mode frequencies */,
                std::vector<int> & workModeNumbers /** work mode numbers */
            );
            /** Computes the CoMAC correlation metric for active modes  @return  comac values 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: std::vector<double> CalculateComacs
            (
                std::vector<int> & referenceModeNumbers /** reference mode numbers */,
                std::vector<int> & workModeNumbers /** work mode numbers */,
                std::vector<double> & referenceModeFrequencies /** reference mode frequencies */,
                std::vector<double> & workModeFrequencies /** work mode frequencies */,
                std::vector<int> & refNodesHaveSensors /** indicates if nodes have a sensor (0=yes, 1=no) */,
                std::vector<int> & refNodeIndex /** reference node index */,
                std::vector<int> & refDofIndex /** reference dof index */
            );
            /** Sets a specific reference mode as active or not 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveRefMode
            (
                int refModeNumber /** reference mode to activate or deactivate */,
                bool active /** activate or deactivate flag */
            );
            /** Sets a specific work mode as active or not 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveWorkMode
            (
                int workModeNumber /** work mode to activate or deactivate */,
                bool active /** activate or deactivate flag */
            );
            /** Sets a specific mode pair as active or not 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveModePair
            (
                int referenceModeNumber /** reference mode of the pair */,
                int workModeNumber /** work mode of the pair */,
                bool active /** activate or deactivate flag */
            );
            /** Sets a specific sensor as active or not 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveSensor
            (
                int sensorNumber /** sensor number */,
                bool active /** activate or deactivate flag */
            );
            /** Sets a specific sensor DOF as active or not 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveSensorDof
            (
                int sensorNumber /** sensor number */,
                int dofNumber /** dof number */,
                bool active /** activate or deactivate flag */
            );
            /** Sets a specific sensor DOF orientation 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveSensorDofOrientation
            (
                int sensorNumber /** sensor number */,
                int dofNumber /** dof number */,
                bool orientation /** true for positive orientation or false for negative orientation */
            );
            /** Export mode pair to CSV file 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ExportModePairCsvFile
            (
                const NXString & filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export mode pair to CSV file 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            void ExportModePairCsvFile
            (
                const char * filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export shape metrics to CSV file 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ExportShapeMetricsCsvFile
            (
                NXOpen::CAE::CorrelShapemetrictype metricCode /** shape metric code */,
                const NXString & filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export shape metrics to CSV file 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            void ExportShapeMetricsCsvFile
            (
                NXOpen::CAE::CorrelShapemetrictype metricCode /** shape metric code */,
                const char * filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Update correlation node matchings 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void UpdateNodeMatchings
            (
            );
            /** Compute mode pairs for correlation solution 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ComputeModePairsForSol
            (
            );
            /** Make a clone of a correl solution.  @return  Cloned solution 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::CorrelSolution * CloneCorrelation
            (
            );
            /** Update results for correlation solution 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void UpdateResultsForSolution
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                bool ignoreReload /** ignore reload */
            );
            /** Create Matching DOFSet 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void GenerateMatchingDofset
            (
            );
            /** Create COMAC results 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void GenerateComacResults
            (
            );
            /** Import node map CSV file 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ImportNodeMapCsvFile
            (
                const NXString & filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Import node map CSV file 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            void ImportNodeMapCsvFile
            (
                const char * filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export node map to CSV file 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ExportNodeMapCsvFile
            (
                const NXString & filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export node map to CSV file 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            void ExportNodeMapCsvFile
            (
                const char * filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
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
