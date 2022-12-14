#ifndef NXOpen_CAE_SIMMOTIONLOADSBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SIMMOTIONLOADSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimMotionLoadsBuilder.ja
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
#include <NXOpen/CAE_SimMotionLoadsListItemBuilder.hxx>
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
        class SimMotionLoadsBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SimMotionLoadsListItemBuilder;
    }
    class Part;
    namespace CAE
    {
        class _SimMotionLoadsBuilderBuilder;
        class SimMotionLoadsBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::SimMotionLoadsBuilder NXOpen::CAE::SimMotionLoadsBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::SimSimulation::CreateMotionLoadsBuilder  NXOpen::CAE::SimSimulation::CreateMotionLoadsBuilder @endlink  <br> 
         <br>  Created in NX5.0.1.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimMotionLoadsBuilder : public NXOpen::Builder
        {
            private: SimMotionLoadsBuilderImpl * m_simmotionloadsbuilder_impl;
            private: friend class  _SimMotionLoadsBuilderBuilder;
            protected: SimMotionLoadsBuilder();
            public: ~SimMotionLoadsBuilder();
            /** Create a motion loads list item  builder from link and solution name 
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SimMotionLoadsListItemBuilder * CreateNewListItem
            (
                const NXString & linkName /** name of the link */,
                const NXString & solutionName /** name of the solution */
            );
            /** Create a motion loads list item  builder from link and solution name 
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            NXOpen::CAE::SimMotionLoadsListItemBuilder * CreateNewListItem
            (
                const char * linkName /** name of the link */,
                const char * solutionName /** name of the solution */
            );
            /** The number of load tranfer list items   @return  number of load tranfer list items 
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: int GetLoadTransferListItemCount
            (
            );
            /** Retrieve a load tranfer list item by its index    @return  
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SimMotionLoadsListItemBuilder * GetLoadTransferListItemByIndex
            (
                int index /** index of list item in the array of all list items */
            );
            /**Returns  the motion simulation part file 
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Part * MotionSimFile
            (
            );
            /**Sets  the motion simulation part file 
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: void SetMotionSimFile
            (
                NXOpen::Part * tSimMotionPart /** tsimmotionpart */ 
            );
            /**Returns  the selected load transfer item  
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SimMotionLoadsListItemBuilder * SelectedLoadTransferListItem
            (
            );
            /**Sets  the selected load transfer item  
             <br>  Created in NX5.0.1.  <br>  
             <br> License requirements : None */
            public: void SetSelectedLoadTransferListItem
            (
                NXOpen::CAE::SimMotionLoadsListItemBuilder * loadTranferItem /** loadtranferitem */ 
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
