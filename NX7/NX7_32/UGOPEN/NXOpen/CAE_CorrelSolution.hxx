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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class CorrelSolution;
    }
    namespace CAE
    {
        class CorrelAlignmentBuilder;
    }
    namespace CAE
    {
        class CorrelModePairingBuilder;
    }
    class NXObject;
    namespace CAE
    {
        class _CorrelSolutionBuilder;
        /** Represents a @link CAE::CorrelSolution CAE::CorrelSolution@endlink , which is a meta-solution used to compare results from two structural dynamics solutions */
        class NXOPENCPPEXPORT CorrelSolution : public NXObject
        {
            private: friend class  _CorrelSolutionBuilder;
            protected: CorrelSolution();
            /** Creates the builder object for mode pairing editing  @return    <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::CorrelModePairingBuilder * CreateModePairingBuilder
            (
            );
            /** Creates the builder object for mode alignment editing  @return    <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::CorrelAlignmentBuilder * CreateAlignmentBuilder
            (
            );
            /** Returns the correlation solution name  @return  the @link CAE::CorrelSolution CAE::CorrelSolution@endlink   name  <br> License requirements : None */
            public: NXString GetSolutionName
            (
            );
            /** Sets the correlation solution name  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetSolutionName
            (
                const NXString & solutionName /** new solution name */,
                bool renameResultFile /** if there are result files associated with the solution, rename the files or not*/
            );
            /** Deletes a correlation solution  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void Destroy
            (
                bool deleteResultFile /** delete the result files associated with the solution or not */
            );
            /** Computes the Model Assurance Criterion (MAC) correlation metric for active modes  @return  the MAC values computed  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: std::vector<double> ComputeMacs
            (
                std::vector<double> & referenceModeFrequencies /** ref mode frequencies */,
                std::vector<int> & referenceModeNumbers /** ref mode numbers */,
                std::vector<double> & workModeFrequencies /** work mode frequencies */,
                std::vector<int> & workModeNumbers /** work mode numbers */
            );
            /** Computes the CoMAC correlation metric for active modes 
             @deprecated Deprecated in NX6.0.2 <br> 
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ComputeComacs
            (
            );
            /** Computes the CoMAC correlation metric for active modes  @return   <br> License requirements : nx_correl_base ("FE Correlation") */
            public: std::vector<double> CalculateComacs
            (
                std::vector<int> & referenceModesNumbers /** reference modes numbers */ ,
                std::vector<int> & workModesNumbers /** work modes numbers */ ,
                std::vector<double> & referenceModeFrequencies /** reference mode frequencies */ ,
                std::vector<double> & workModeFrequencies /** work mode frequencies */ ,
                std::vector<int> & refDofFromSensors /** ref dof from sensors */ ,
                std::vector<int> & refDofIndex /** ref dof index */ ,
                std::vector<int> & refDofComponent /** ref dof component */ 
            );
            /** Sets a specific reference mode as active or not  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveRefMode
            (
                int refModeNumber /** reference mode to activate or deactivate */,
                bool active /** activate or deactivate flag */
            );
            /** Sets a specific work mode as active or not  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveWorkMode
            (
                int workModeNumber /** work mode to activate or deactivate */,
                bool active /** activate or deactivate flag */
            );
            /** Sets a specific mode pair as active or not  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveModePair
            (
                int referenceModeNumber /** reference mode of the pair */,
                int workModeNumber /** work mode of the pair */,
                bool active /** activate or deactivate flag */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
