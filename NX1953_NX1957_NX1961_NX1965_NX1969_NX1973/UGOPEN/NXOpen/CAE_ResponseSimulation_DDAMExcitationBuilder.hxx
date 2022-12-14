#ifndef NXOpen_CAE_RESPONSESIMULATION_DDAMEXCITATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_DDAMEXCITATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_DDAMExcitationBuilder.ja
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
#include <NXOpen/CAE_ResponseSimulation_DDAMExcitation.hxx>
#include <NXOpen/CAE_ResponseSimulation_Excitation.hxx>
#include <NXOpen/CAE_ResponseSimulation_ExcitationBuilder.hxx>
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
        namespace ResponseSimulation
        {
            class DDAMExcitationBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ExcitationBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _DDAMExcitationBuilderBuilder;
            class DDAMExcitationBuilderImpl;
            /** Represents the manager to @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink .
                 The object of type @link NXOpen::CAE::ResponseSimulation::DDAMExcitation NXOpen::CAE::ResponseSimulation::DDAMExcitation@endlink  can only
                be created or edited through this class.  <br> To create a new instance of this class, use @link NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateDdamExcitationBuilder  NXOpen::CAE::ResponseSimulation::ExcitationCollection::CreateDdamExcitationBuilder @endlink  <br> 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  DDAMExcitationBuilder : public NXOpen::CAE::ResponseSimulation::ExcitationBuilder
            {
                private: DDAMExcitationBuilderImpl * m_ddamexcitationbuilder_impl;
                private: friend class  _DDAMExcitationBuilderBuilder;
                protected: DDAMExcitationBuilder();
                public: ~DDAMExcitationBuilder();
                /**Returns  the loading type
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DDAMExcitation::LoadingType LoadingType
                (
                );
                /**Sets  the loading type
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetLoadingType
                (
                    NXOpen::CAE::ResponseSimulation::DDAMExcitation::LoadingType loadingType /** loading type */ 
                );
                /**Returns  the response type
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::DDAMExcitation::ResponseType ResponseType
                (
                );
                /**Sets  the response type
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetResponseType
                (
                    NXOpen::CAE::ResponseSimulation::DDAMExcitation::ResponseType responseType /** response type */ 
                );
                /** Sets the status for a direction component
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetComponentStatus
                (
                    NXOpen::CAE::ResponseSimulation::Excitation::Component component /** component */ ,
                    bool enable /** enable */ 
                );
                /** Returns the status of a dierction component  @return  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: bool GetComponentStatus
                (
                    NXOpen::CAE::ResponseSimulation::Excitation::Component component /** component */ 
                );
            };
        }
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
