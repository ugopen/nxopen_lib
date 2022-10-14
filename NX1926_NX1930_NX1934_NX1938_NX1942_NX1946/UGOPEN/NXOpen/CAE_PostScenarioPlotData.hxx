#ifndef NXOpen_CAE_POSTSCENARIOPLOTDATA_HXX_INCLUDED
#define NXOpen_CAE_POSTSCENARIOPLOTDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostScenarioPlotData.ja
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
#include <NXOpen/CAE_PostScenarioMetadata.hxx>
#include <NXOpen/CAE_PostScenarioPlotDataEntry.hxx>
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
        class PostScenarioPlotData;
    }
    namespace CAE
    {
        class PostScenarioMetadata;
    }
    namespace CAE
    {
        class PostScenarioPlotDataEntry;
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
        class PostScenarioPlotDataImpl;

        /// \cond NX_NO_DOC 
        /**  @brief  This class represents the plot data of a data set that flows through Scenario-based Data Visualization  

         

                
                 <br> 
                A plot has a name, data points for independents and dependents, and bound values for
                data set selection variables.  The DataPoints are consistent with the variables defined
                in the @link CAE::PostScenarioResultGroup CAE::PostScenarioResultGroup@endlink .
                 <br> 
                 <br> 
                To build a plot for output, use @link CAE::PostScenarioPlotBuilder CAE::PostScenarioPlotBuilder@endlink .
                 <br> 
                 <br> 
                A plot contains a number of @link CAE::PostScenarioPlotDataEntry CAE::PostScenarioPlotDataEntry@endlink  objects.
                These entries are columns are plane intersections in a hypercube,
                bound on dimensions called selection and high order independent variables.
                For an N dimensional sparse matrix, the dimensions
                N, N-1, ... 3, 2 are known here as high order independents
                while dimension 1 is known as the lowest order independent.
                The lowest order independent is modelled as an array
                of values representing the abscissa values of the  column
                it represents. The higher order independents - for an
                entry - are scalars which identify the position of the
                column in the multidimensional sparse matrix.
                 <br> 
                
                 <br> 
                For example, to model a 2D matrix, consider the
                high order independent RPM (R) , the low order     independent
                Frequency (F) and the dependent Displacement (D)
                The following are entries:  @code 
                    R=1, F=[1, 2, 3], D=[10, 11, 12]
                    R=2, F=[2, 3, 4], D=[11, 12, 13]
                    R-3, F=[2, 3, 4, 5], D=[11, 12, 13, 14] @endcode 
                
                These represent the following matrix @code 
                R\F 1  2  3  4  5
                1   10 11 12 -  -
                2   -  11 12 13 -
                3   -  11 12 13 14 @endcode 
                 <br> 
                
              <br> No support for KF.  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostScenarioPlotData : public NXOpen::TransientObject
        {
            private: PostScenarioPlotDataImpl * m_postscenarioplotdata_impl;
            /// \cond NX_NO_DOC 
            public: explicit PostScenarioPlotData(void *ptr);
            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Dispose of this instance. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PostScenarioPlotData();

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the name of the @link CAE::PostScenarioResultGroup CAE::PostScenarioResultGroup@endlink  this plot is contained in 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ResultGroupName
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the name of the @link CAE::PostScenarioConfigurationGroup CAE::PostScenarioConfigurationGroup@endlink  this plot is contained in 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ConfigurationGroupName
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the name of the this plot 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  @brief Get the value of a selection variable. 

             
                    
                        
                         <br> 
                        Selection variables can be retrieved from the owning @link CAE::PostScenarioResultGroup CAE::PostScenarioResultGroup@endlink .
                         <br> 
                         <br> 
                        Selection variables declared and required in the scenario descriptor have the name as declared therein.
                        Selection variables that are part of the data set but not requested by the scenario descriptor keep
                        their original name, and that name must be inspected through the Result Group, if the transformation
                        callback is interested.
                         <br> 
                        
                     
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PostScenarioVariant * GetSelectionVariableValue
            (
                const NXString & name /** name */ 
            );
            /**  @brief Get the value of a selection variable. 

             
                    
                        
                         <br> 
                        Selection variables can be retrieved from the owning @link CAE::PostScenarioResultGroup CAE::PostScenarioResultGroup@endlink .
                         <br> 
                         <br> 
                        Selection variables declared and required in the scenario descriptor have the name as declared therein.
                        Selection variables that are part of the data set but not requested by the scenario descriptor keep
                        their original name, and that name must be inspected through the Result Group, if the transformation
                        callback is interested.
                         <br> 
                        
                     
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAE::PostScenarioVariant * GetSelectionVariableValue
            (
                const char * name /** name */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  @brief Get the metadata attached to a selection variable. 

             
                    
                        
                         <br> 
                        Selection variables can be retrieved from the owning @link CAE::PostScenarioResultGroup CAE::PostScenarioResultGroup@endlink .
                         <br> 
                         <br> 
                        Selection variables declared and required in the scenario descriptor have the name as declared therein.
                        Selection variables that are part of the data set but not requested by the scenario descriptor keep
                        their original name, and that name must be inspected through the Result Group, if the transformation
                        callback is interested.
                         <br> 
                        
                     
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PostScenarioMetadata * GetSelectionVariableMetadata
            (
                const NXString & name /** name */ 
            );
            /**  @brief Get the metadata attached to a selection variable. 

             
                    
                        
                         <br> 
                        Selection variables can be retrieved from the owning @link CAE::PostScenarioResultGroup CAE::PostScenarioResultGroup@endlink .
                         <br> 
                         <br> 
                        Selection variables declared and required in the scenario descriptor have the name as declared therein.
                        Selection variables that are part of the data set but not requested by the scenario descriptor keep
                        their original name, and that name must be inspected through the Result Group, if the transformation
                        callback is interested.
                         <br> 
                        
                     
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAE::PostScenarioMetadata * GetSelectionVariableMetadata
            (
                const char * name /** name */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  @brief Get the plot entries that make up this dataset. 

             
                    
                        
                         <br> 
                        A Plot is made up of one or more Entries. Each Entry is a slice through the data set, which
                        should be viewed as a hyper-cube. The most common case is that of a collection of signals
                        or a collection of spatial results, in which case the dimension is 1, and there is only one
                        entry.
                         <br> 
                         <br> 
                        For more complex data sets, the dimensionality grows, so one Plot represents a cube, and one Entry
                        represents a one-dimensional slice. The dimension over which the slice is performed is the first
                        Independent Variable as defined in the Result Group, and this corresponds to the first independent
                        (rank 0) as requested in your Input Definition in the Descriptor. The other dimensions are bound
                        to one value, and are known as High Order Independents. The remaining dimension (rank 0) is unbound
                        and you can access all the values. For each value on that dimension, you can retrieve the dependent
                        values, which represent the data points of interest.
                         <br> 
                        
                     
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAE::PostScenarioPlotDataEntry *> GetEntries
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns   @brief Retrieve the plot-level metadata. 

             

                        
                        See @link CAE::PostScenarioMetadata CAE::PostScenarioMetadata@endlink .
                        
                      
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PostScenarioMetadata * Metadata
            (
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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