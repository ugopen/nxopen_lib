#ifndef NXOpen_CAE_POSTSCENARIOAGGREGATEVALUEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_POSTSCENARIOAGGREGATEVALUEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostScenarioAggregateValueBuilder.ja
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
#include <NXOpen/CAE_PostScenarioVariant.hxx>
#include <NXOpen/TransientObject.hxx>
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
        class PostScenarioAggregateValueBuilder;
    }
    namespace CAE
    {
        class PostScenarioVariant;
    }
    namespace CAE
    {
    }
    namespace CAE
    {
        class PostScenarioAggregateValueBuilderImpl;
        /**  @brief  
                    Builder for aggregated values. 
                 

          

                Allows you to build the aggregated values with reverse mapping to the original deaggregated values.
                The framework uses the reverse mapping to query the data sources.

                
                    In order to get a valid output, the following conditions must be met:
                    <ul>
                        <li>
                            Deaggregate values for all slot variables provided by 
                            @link CAE::PostScenarioAggregationInput CAE::PostScenarioAggregationInput@endlink  must be fed to this class. 
                        </li>
                        <li>
                            All deaggregate values must be equal to one of the values provided by 
                            @link CAE::PostScenarioAggregationInput CAE::PostScenarioAggregationInput@endlink .
                        </li>
                    </ul>

                    Note: it is valid for your callback to return an empty reverse map in the output parameter. 
                    In this case, the Plot button will be disabled in the GUI. It is expected that you notify the 
                    user why the Plot button was disabled via the MessageCollector argument.
                
             <br> No support for KF.  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostScenarioAggregateValueBuilder : public NXOpen::TransientObject
        {
            private: PostScenarioAggregateValueBuilderImpl * m_postscenarioaggregatevaluebuilder_impl;
            /// \cond NX_NO_DOC 
            public: explicit PostScenarioAggregateValueBuilder(void *ptr);
            /// \endcond 
            /** Dispose of this instance. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PostScenarioAggregateValueBuilder();
            /** Sets the deaggregate values for one of the slot variables that is being aggregated. 
                    
                        
                            This will raise exceptions if invalid inputs are provided. 
                        
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDeaggregates
            (
                const NXString & slotVariable /** The slot variable. */,
                const std::vector<NXOpen::CAE::PostScenarioVariant *> & deaggregateValues /** The deaggregate values. */
            );
            /** Sets the deaggregate values for one of the slot variables that is being aggregated. 
                    
                        
                            This will raise exceptions if invalid inputs are provided. 
                        
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void SetDeaggregates
            (
                const char * slotVariable /** The slot variable. */,
                const std::vector<NXOpen::CAE::PostScenarioVariant *> & deaggregateValues /** The deaggregate values. */
            );
            /** Execute changes. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void Commit
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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
