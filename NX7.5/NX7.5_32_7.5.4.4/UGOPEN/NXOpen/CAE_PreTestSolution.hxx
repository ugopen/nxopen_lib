#ifndef NXOpen_CAE_PRETESTSOLUTION_HXX_INCLUDED
#define NXOpen_CAE_PRETESTSOLUTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PreTestSolution.ja
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
#include <NXOpen/CAE_CorrelSolution.hxx>
#include <NXOpen/CAE_PreTestExportUnvBuilder.hxx>
#include <NXOpen/CAE_PreTestSolution.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class PreTestSolution;
    }
    namespace CAE
    {
        class PreTestExportUnvBuilder;
    }
    namespace CAE
    {
        class PreTestSensorConfig;
    }
    namespace CAE
    {
        class PreTestSensorSelectionControl;
    }
    namespace CAE
    {
        class SimSolution;
    }
    class NXObject;
    namespace CAE
    {
        class _PreTestSolutionBuilder;
        class PreTestSolutionImpl;
        /** Represents a pre-test setup */
        class NXOPENCPPEXPORT  PreTestSolution : public NXObject
        {
            private: PreTestSolutionImpl * m_pretestsolution_impl;
            private: friend class  _PreTestSolutionBuilder;
            protected: PreTestSolution();
            public: ~PreTestSolution();
            /**Returns  the pre-test name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the pre-test name  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /** Sets a specific work mode as active or not  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetActiveWorkMode
            (
                int workModeNumber /** work mode to activate or deactivate */,
                bool active /** activate or deactivate flag */
            );
            /** Sets weight for a specific work mode  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetWorkModeWeight
            (
                int workModeNumber /** work mode number to set the weight */,
                double weight /** weight to set the work mode */
            );
            /** Export shape metrics to CSV file  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ExportShapeMetricsCsvFile
            (
                NXOpen::CAE::CorrelShapemetrictype metricCode /** shape metric code */,
                const NXString & filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Solve sensor configuration  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SolveSensorConfig
            (
                NXOpen::CAE::PreTestSensorConfig * tSensorConfig /** sensor config */
            );
            /** Update results for pre-test solution  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void UpdateResultsForSolution
            (
                NXOpen::CAE::SimSolution * tSolution /** solution */,
                bool ignoreReload /** ignore reload */
            );
            /** Creates a pre-test export Unv builder  @return  export UNV Builder  <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::PreTestExportUnvBuilder * CreateExportUnvBuilder
            (
            );


            /** The sensor selection configuration setup for this pre-test setup */
            public: NXOpen::CAE::PreTestSensorSelectionControl *SensorSelectionControl();
        };
    }
}
#undef EXPORTLIBRARY
#endif