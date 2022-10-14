#ifndef NXOpen_CAE_DATAPROCESSING_HXX_INCLUDED
#define NXOpen_CAE_DATAPROCESSING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DataProcessing.ja
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
#include <NXOpen/CAE_IPostScenarioDataSource.hxx>
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
        class DataProcessing;
    }
    namespace CAE
    {
        class DataProcessingBlockCollection;
    }
    namespace CAE
    {
        class IPostScenarioDataSource;
    }
    class NXObject;
    namespace CAE
    {
        class _DataProcessingBuilder;
        class DataProcessingImpl;
        /** Represents a @link NXOpen::CAE::DataProcessing NXOpen::CAE::DataProcessing@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::CAE::DataProcessingBuilder  NXOpen::CAE::DataProcessingBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DataProcessing : public NXOpen::NXObject, public virtual NXOpen::CAE::IPostScenarioDataSource
        {
            private: DataProcessingImpl * m_dataprocessing_impl;
            private: friend class  _DataProcessingBuilder;
            protected: DataProcessing();
            public: ~DataProcessing();
            /** Processes the DPM 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Process
            (
            );


            /** The event collection for this meta solution. 
             <br>  Created in NX12.0.0.  <br>  
            */
            public: NXOpen::CAE::DataProcessingBlockCollection *Blocks();
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