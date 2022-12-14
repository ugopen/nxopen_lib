#ifndef NXOpen_CAE_DURSPECIALISTLOADPROVIDERBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTLOADPROVIDERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistLoadProviderBuilder.ja
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
#include <NXOpen/CAE_DurSpecialistEvent.hxx>
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
        class DurSpecialistLoadProviderBuilder;
    }
    class Builder;
    namespace CAE
    {
        class DurSpecialistEvent;
    }
    namespace CAE
    {
        class _DurSpecialistLoadProviderBuilderBuilder;
        class DurSpecialistLoadProviderBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link NXOpen::CAE::DurSpecialistLoadProvider NXOpen::CAE::DurSpecialistLoadProvider@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistLoadProviderCollection::CreateLoadProviderBuilder  NXOpen::CAE::DurSpecialistLoadProviderCollection::CreateLoadProviderBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistLoadProviderBuilder : public NXOpen::Builder
        {
            private: DurSpecialistLoadProviderBuilderImpl * m_durspecialistloadproviderbuilder_impl;
            private: friend class  _DurSpecialistLoadProviderBuilderBuilder;
            protected: DurSpecialistLoadProviderBuilder();
            public: ~DurSpecialistLoadProviderBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the event type. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistEvent::EventType LoadDefinition
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the event type. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetLoadDefinition
            (
                NXOpen::CAE::DurSpecialistEvent::EventType type /** type */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            void SetName
            (
                const char * name /** name */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the description. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Description
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the description. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetDescription
            (
                const NXString & description /** description */ 
            );
            /**Sets  the description. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            void SetDescription
            (
                const char * description /** description */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the event. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistEvent * Event
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the event. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: void SetEvent
            (
                NXOpen::CAE::DurSpecialistEvent * durabilityEvent /** durabilityevent */ 
            );

            /// \endcond 
        };

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
