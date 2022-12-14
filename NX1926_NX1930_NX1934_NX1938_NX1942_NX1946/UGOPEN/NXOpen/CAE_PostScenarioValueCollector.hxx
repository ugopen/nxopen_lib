#ifndef NXOpen_CAE_POSTSCENARIOVALUECOLLECTOR_HXX_INCLUDED
#define NXOpen_CAE_POSTSCENARIOVALUECOLLECTOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostScenarioValueCollector.ja
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
        class PostScenarioValueCollector;
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
        class PostScenarioValueCollectorImpl;

        /// \cond NX_NO_DOC 
        /** An object used to collect multiple values from a Post Scenario callback that requires it.  <br> No support for KF.  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostScenarioValueCollector : public NXOpen::TransientObject
        {
            private: PostScenarioValueCollectorImpl * m_postscenariovaluecollector_impl;
            /// \cond NX_NO_DOC 
            public: explicit PostScenarioValueCollector(void *ptr);
            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Add a string. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void AddString
            (
                const NXString & theValue /** thevalue */ 
            );
            /** Add a string. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            void AddString
            (
                const char * theValue /** thevalue */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Add a @link CAE::PostScenarioVariant CAE::PostScenarioVariant@endlink . 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void AddValue
            (
                NXOpen::CAE::PostScenarioVariant * theValue /** thevalue */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Read values. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::CAE::PostScenarioVariant *> GetValues
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Dispose of this instance. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PostScenarioValueCollector();

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
