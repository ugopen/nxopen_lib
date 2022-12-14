#ifndef NXOpen_CAE_PRETESTSENSORCONFIGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_PRETESTSENSORCONFIGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PreTestSensorConfigBuilder.ja
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
#include <NXOpen/CAE_PreTestSensorConfigBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class PreTestSensorConfigBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _PreTestSensorConfigBuilderBuilder;
        class PreTestSensorConfigBuilderImpl;
        /** Represents a @link NXOpen::CAE::PreTestSensorConfig NXOpen::CAE::PreTestSensorConfig@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::PreTestSolutionCollection::CreateSensorConfigBuilder  NXOpen::CAE::PreTestSolutionCollection::CreateSensorConfigBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AlgorithmChoice </td> <td> 
         
        MinMac </td> </tr> 

        <tr><td> 
         
        NumTriaxialSensors </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        NumUniaxialSensors </td> <td> 
         
        10 </td> </tr> 

        </table>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PreTestSensorConfigBuilder : public NXOpen::Builder
        {
            /** Selected algorithm for the sensor selection */
            public: enum AlgorithmChoiceType
            {
                AlgorithmChoiceTypeMinMac/** min mac */ 
            };

            private: PreTestSensorConfigBuilderImpl * m_pretestsensorconfigbuilder_impl;
            private: friend class  _PreTestSensorConfigBuilderBuilder;
            protected: PreTestSensorConfigBuilder();
            public: ~PreTestSensorConfigBuilder();
            /**Returns  the sensor selection algorithm 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PreTestSensorConfigBuilder::AlgorithmChoiceType AlgorithmChoice
            (
            );
            /**Sets  the sensor selection algorithm 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetAlgorithmChoice
            (
                NXOpen::CAE::PreTestSensorConfigBuilder::AlgorithmChoiceType algorithmChoice /** algorithmchoice */ 
            );
            /**Returns  the number of uniaxial sensors to select 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int NumUniaxialSensors
            (
            );
            /**Sets  the number of uniaxial sensors to select 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetNumUniaxialSensors
            (
                int numUniaxialSensors /** numuniaxialsensors */ 
            );
            /**Returns  the number of triaxial sensors to select 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int NumTriaxialSensors
            (
            );
            /**Sets  the number of triaxial sensors to select 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetNumTriaxialSensors
            (
                int numTriaxialSensors /** numtriaxialsensors */ 
            );
            /**Returns  the name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            void SetName
            (
                const char * name /** name */ 
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
