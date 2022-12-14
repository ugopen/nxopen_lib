#ifndef NXOpen_CAE_RESPONSESIMULATION_CSDEXCITATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_CSDEXCITATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_CSDExcitationBuilder.ja
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
#include <NXOpen/CAE_ResponseSimulation_CSDExcitation.hxx>
#include <NXOpen/CAE_ResponseSimulation_Excitation.hxx>
#include <NXOpen/CAE_ResponseSimulation_ExcitationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class CSDExcitationBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class Excitation;
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
            class _CSDExcitationBuilderBuilder;
            class CSDExcitationBuilderImpl;
            /** Represents the manager to @link CAE::ResponseSimulation::CSDExcitation CAE::ResponseSimulation::CSDExcitation@endlink .
                 The object of type @link CAE::ResponseSimulation::CSDExcitation CAE::ResponseSimulation::CSDExcitation@endlink 
                  can only be created or edited through this class.
                  <br> To create a new instance of this class, use @link CAE::ResponseSimulation::ExcitationCollection::CreateCsdExcitationBuilder CAE::ResponseSimulation::ExcitationCollection::CreateCsdExcitationBuilder@endlink  <br> */
            class NXOPENCPPEXPORT  CSDExcitationBuilder : public CAE::ResponseSimulation::ExcitationBuilder
            {
                private: CSDExcitationBuilderImpl * m_csdexcitationbuilder_impl;
                private: friend class  _CSDExcitationBuilderBuilder;
                protected: CSDExcitationBuilder();
                public: ~CSDExcitationBuilder();
                /** Returns the from function  @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::Excitation * GetFromFunction
                (
                    NXOpen::CAE::ResponseSimulation::Excitation::Component* componentType /** componenttype */ 
                );
                /** Sets the from function  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetFromFunction
                (
                    NXOpen::CAE::ResponseSimulation::Excitation * fromExcitation /** fromexcitation */ ,
                    NXOpen::CAE::ResponseSimulation::Excitation::Component componentType /** componenttype */ 
                );
                /** Returns the to function  @return   <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::Excitation * GetToFunction
                (
                    NXOpen::CAE::ResponseSimulation::Excitation::Component* componentType /** componenttype */ 
                );
                /** Sets the to function  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetToFunction
                (
                    NXOpen::CAE::ResponseSimulation::Excitation * toExcitation /** toexcitation */ ,
                    NXOpen::CAE::ResponseSimulation::Excitation::Component componentType /** componenttype */ 
                );
                /**Returns  the correlation type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::CSDExcitation::CorrelationType CorrelationType
                (
                );
                /**Sets  the correlation type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetCorrelationType
                (
                    NXOpen::CAE::ResponseSimulation::CSDExcitation::CorrelationType type /** type */ 
                );
                /**Returns  the correlation type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: double CorrelationValue
                (
                );
                /**Sets  the correlation type  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void SetCorrelationValue
                (
                    double correlationValue /** correlationvalue */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
