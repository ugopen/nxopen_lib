#ifndef NXOpen_CAE_CORRELMACCONTRIBUTIONSDLGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CORRELMACCONTRIBUTIONSDLGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelMacContributionsDlgBuilder.ja
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
#include <NXOpen/CAE_ISensorSet.hxx>
#include <NXOpen/CAE_CorrelBaseBuilder.hxx>
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
        class CorrelMacContributionsDlgBuilder;
    }
    namespace CAE
    {
        class CorrelBaseBuilder;
    }
    namespace CAE
    {
        class ISensorSet;
    }
    namespace CAE
    {
        class _CorrelMacContributionsDlgBuilderBuilder;
        class CorrelMacContributionsDlgBuilderImpl;
        /** This builder is used to control the mac contributions dialog behavior of a @link NXOpen::CAE::CorrelSolution NXOpen::CAE::CorrelSolution@endlink   <br> To create a new instance of this class, use @link NXOpen::CAE::CorrelSolution::CreateMacContributionsDlgBuilder  NXOpen::CAE::CorrelSolution::CreateMacContributionsDlgBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CorrelMacContributionsDlgBuilder : public NXOpen::CAE::CorrelBaseBuilder
        {
            private: CorrelMacContributionsDlgBuilderImpl * m_correlmaccontributionsdlgbuilder_impl;
            private: friend class  _CorrelMacContributionsDlgBuilderBuilder;
            protected: CorrelMacContributionsDlgBuilder();
            public: ~CorrelMacContributionsDlgBuilder();
            /**Returns  the ref mode index value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: int RefModeIndex
            (
            );
            /**Sets  the ref mode index value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetRefModeIndex
            (
                int index /** index */ 
            );
            /**Returns  the work mode index value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: int WorkModeIndex
            (
            );
            /**Sets  the work mode index value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetWorkModeIndex
            (
                int index /** index */ 
            );
            /**Returns  the target MAC value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: double TargetMacValue
            (
            );
            /**Sets  the target MAC value 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetTargetMacValue
            (
                double targetMac /** targetmac */ 
            );
            /**Returns  the propagate results toggle 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: bool DeactivateToggle
            (
            );
            /**Sets  the propagate results toggle 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetDeactivateToggle
            (
                bool propResults /** propresults */ 
            );
            /**Returns  the temp sensor set 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: NXOpen::CAE::ISensorSet * TempSensorSet
            (
            );
            /**Sets  the temp sensor set 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetTempSensorSet
            (
                NXOpen::CAE::ISensorSet * pSensorSet /** psensorset */ 
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