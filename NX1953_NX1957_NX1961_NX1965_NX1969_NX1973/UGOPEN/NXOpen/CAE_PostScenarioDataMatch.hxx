#ifndef NXOpen_CAE_POSTSCENARIODATAMATCH_HXX_INCLUDED
#define NXOpen_CAE_POSTSCENARIODATAMATCH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostScenarioDataMatch.ja
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
#include <NXOpen/CAE_PostScenarioResultGroupVariable.hxx>
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
        class PostScenarioDataMatch;
    }
    namespace CAE
    {
        class PostScenarioResultGroupVariable;
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
        class PostScenarioDataMatchImpl;
        /**  @brief   
                    Represents the match of @link NXOpen::CAE::PostScenarioDefinition NXOpen::CAE::PostScenarioDefinition@endlink  
                    and its parent @link NXOpen::CAE::DataSource NXOpen::CAE::DataSource@endlink  available for a @link NXOpen::CAE::PostScenarioBuilderSlot NXOpen::CAE::PostScenarioBuilderSlot@endlink .
                 

         
                 
                  
                      <br> 
                        One match corresponds to a combination of data source plus data definition.
                      <br> 
                      <br> 
                        A match is made out of: 
                        <ul>
                            <li> 
                                The name of the data source 
                            </li>
                            <li> 
                                The name of the data definition 
                            </li>
                            <li> 
                                The matching variables are : dependent variables, independent variables and selection variables
                            </li>
                        </ul>
                      <br> 
                 
             <br> No support for KF.  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostScenarioDataMatch : public NXOpen::TransientObject
        {
            private: PostScenarioDataMatchImpl * m_postscenariodatamatch_impl;
            /// \cond NX_NO_DOC 
            public: explicit PostScenarioDataMatch(void *ptr);
            /// \endcond 
            /** Dispose of this instance. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PostScenarioDataMatch();
            /**Returns  the data source name 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DataSourceName
            (
            );
            /**Returns  the data definition name 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DataDefinitionName
            (
            );
            /**  @brief  
                            Returns all the matching dependents comming from the data source. 
                         

             
                        
                         
                            The matching dependents are of type @link NXOpen::CAE::PostScenarioResultGroupVariable NXOpen::CAE::PostScenarioResultGroupVariable@endlink . 
                        
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAE::PostScenarioResultGroupVariable *> GetMatchedDependentVariables
            (
            );
            /**  @brief  
                            Returns all the matching independents comming from the data source. 
                         

             
                         
                         
                            The matching independents are of type @link NXOpen::CAE::PostScenarioResultGroupVariable NXOpen::CAE::PostScenarioResultGroupVariable@endlink . 
                        
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAE::PostScenarioResultGroupVariable *> GetMatchedIndependentVariables
            (
            );
            /**  @brief  
                            Returns the matching selection comming from the data source. 
                         

             
                        
                         
                            The matching selection is of a list of type @link NXOpen::CAE::PostScenarioResultGroupVariable NXOpen::CAE::PostScenarioResultGroupVariable@endlink . 
                        
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAE::PostScenarioResultGroupVariable *> GetMatchedSelectionVariables
            (
            );
            /**  @brief  
                            Returns the default selected value and all the values for a variable by the variable name. 
                         

             
                         
                        
                             <br> 
                                Use this method to get the values from a independent or a selection variable. The interest in dependent 
                                variables lies in the domain of the variable. You can inspect variable's domain via <ja_property>NXOpen.CAE.PostScenarioResultGroupVariable.Domain</ja_property>.
                             <br> 
                             <br> 
                                The values and the default value are of type @link NXOpen::CAE::PostScenarioVariant NXOpen::CAE::PostScenarioVariant@endlink .
                             <br> 
                             <br> 
                                The default value is optional so it can be NULL. 
                             <br> 
                        
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetVariableValues
            (
                const NXString & variableName /** variablename */ ,
                NXOpen::CAE::PostScenarioVariant ** defaultValue /** defaultvalue */ ,
                std::vector<NXOpen::CAE::PostScenarioVariant *> & values /** values */ 
            );
            /**  @brief  
                            Returns the default selected value and all the values for a variable by the variable name. 
                         

             
                         
                        
                             <br> 
                                Use this method to get the values from a independent or a selection variable. The interest in dependent 
                                variables lies in the domain of the variable. You can inspect variable's domain via <ja_property>NXOpen.CAE.PostScenarioResultGroupVariable.Domain</ja_property>.
                             <br> 
                             <br> 
                                The values and the default value are of type @link NXOpen::CAE::PostScenarioVariant NXOpen::CAE::PostScenarioVariant@endlink .
                             <br> 
                             <br> 
                                The default value is optional so it can be NULL. 
                             <br> 
                        
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void GetVariableValues
            (
                const char * variableName /** variablename */ ,
                NXOpen::CAE::PostScenarioVariant ** defaultValue /** defaultvalue */ ,
                std::vector<NXOpen::CAE::PostScenarioVariant *> & values /** values */ 
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
