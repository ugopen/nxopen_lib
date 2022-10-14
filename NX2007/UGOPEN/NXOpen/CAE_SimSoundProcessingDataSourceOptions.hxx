#ifndef NXOpen_CAE_SIMSOUNDPROCESSINGDATASOURCEOPTIONS_HXX_INCLUDED
#define NXOpen_CAE_SIMSOUNDPROCESSINGDATASOURCEOPTIONS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimSoundProcessingDataSourceOptions.ja
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
#include <NXOpen/CAE_DataReaderDatabaseOptions.hxx>
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
        class SimSoundProcessingDataSourceOptions;
    }
    namespace CAE
    {
        class DataReaderDatabaseOptions;
    }
    class NXObject;
    namespace CAE
    {
        class _SimSoundProcessingDataSourceOptionsBuilder;
        class SimSoundProcessingDataSourceOptionsImpl;
        /**  @brief    

         
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimSoundProcessingDataSourceOptions : public NXOpen::NXObject
        {
            private: SimSoundProcessingDataSourceOptionsImpl * m_simsoundprocessingdatasourceoptions_impl;
            private: friend class  _SimSoundProcessingDataSourceOptionsBuilder;
            protected: SimSoundProcessingDataSourceOptions();
            public: ~SimSoundProcessingDataSourceOptions();
            /**Returns  the file name path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FileName
            (
            );
            /**Sets  the file name path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFileName
            (
                const NXString & fileName /** filename */ 
            );
            /**Sets  the file name path 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetFileName
            (
                const char * fileName /** filename */ 
            );
            /**Returns  the data base options 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DataReaderDatabaseOptions * DatabaseOptions
            (
            );
            /**Returns  the node label 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: int NodeLabel
            (
            );
            /**Sets  the node label 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetNodeLabel
            (
                int nodeLabel /** nodelabel */ 
            );
            /** Plot the content of the selected file. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Plot
            (
                int deviceIndex /** deviceindex */ ,
                int viewportIndex /** viewportindex */ 
            );
            /**Returns  the data set name 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DataSetName
            (
            );
            /**Sets  the data set name 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetDataSetName
            (
                const NXString & dataSetName /** datasetname */ 
            );
            /**Sets  the data set name 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetDataSetName
            (
                const char * dataSetName /** datasetname */ 
            );
            /**Returns  the subcase name 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SubcaseName
            (
            );
            /**Sets  the subcase name 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSubcaseName
            (
                const NXString & subcaseName /** subcasename */ 
            );
            /**Sets  the subcase name 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetSubcaseName
            (
                const char * subcaseName /** subcasename */ 
            );
            /**Returns  the flag used to filter binaural irs only 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: bool BinauralOnly
            (
            );
            /**Sets  the flag used to filter binaural irs only 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetBinauralOnly
            (
                bool binauralOnly /** binauralonly */ 
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