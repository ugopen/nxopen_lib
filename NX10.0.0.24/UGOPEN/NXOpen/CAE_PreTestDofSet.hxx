#ifndef NXOpen_CAE_PRETESTDOFSET_HXX_INCLUDED
#define NXOpen_CAE_PRETESTDOFSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PreTestDofSet.ja
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
        class PreTestDofSet;
    }
    namespace CAE
    {
        class CaeDOFSet;
    }
    namespace CAE
    {
        class FENode;
    }
    class NXObject;
    namespace CAE
    {
        class _PreTestDofSetBuilder;
        class PreTestDofSetImpl;
        /** Represents Dof Set within a pre-test setup  <br> To create or edit an instance of this class, use @link NXOpen::CAE::PreTestDofSetBuilder  NXOpen::CAE::PreTestDofSetBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PreTestDofSet : public NXOpen::NXObject
        {
            private: PreTestDofSetImpl * m_pretestdofset_impl;
            private: friend class  _PreTestDofSetBuilder;
            protected: PreTestDofSet();
            public: ~PreTestDofSet();
            /** Setting the @link NXOpen::CAE::CaeDOFSet NXOpen::CAE::CaeDOFSet@endlink  reference 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetDofSet
            (
                NXOpen::CAE::CaeDOFSet * dofsetref /** The reference DOFSet */
            );
            /** Setting the dofs manually 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetDofs
            (
                const std::vector<NXOpen::CAE::FENode *> & nodes /** Nodes defining the dof set */,
                const std::vector<bool> & dofs /** Flags to indicate which Dofs are activated. */
            );
            /** Export dof set shape metrics to CSV file 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void ExportShapeMetricsCsvFile
            (
                NXOpen::CAE::CorrelShapemetrictype metricCode /** shape metric code */,
                const NXString & filename /** CSV file name.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Export dof set shape metrics to CSV file 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            void ExportShapeMetricsCsvFile
            (
                NXOpen::CAE::CorrelShapemetrictype metricCode /** shape metric code */,
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
