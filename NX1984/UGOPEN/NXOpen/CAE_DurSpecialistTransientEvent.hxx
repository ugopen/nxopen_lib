#ifndef NXOpen_CAE_DURSPECIALISTTRANSIENTEVENT_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTTRANSIENTEVENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistTransientEvent.ja
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
        class DurSpecialistTransientEvent;
    }
    namespace CAE
    {
        class DurSpecialistEvent;
    }
    namespace CAE
    {
        class _DurSpecialistTransientEventBuilder;
        class DurSpecialistTransientEventImpl;
        /** Represents a @link NXOpen::CAE::DurSpecialistTransientEvent NXOpen::CAE::DurSpecialistTransientEvent@endlink   <br> To create or edit an instance of this class, use @link NXOpen::CAE::DurSpecialistTransientEventBuilder  NXOpen::CAE::DurSpecialistTransientEventBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistTransientEvent : public NXOpen::CAE::DurSpecialistEvent
        {
            private: DurSpecialistTransientEventImpl * m_durspecialisttransientevent_impl;
            private: friend class  _DurSpecialistTransientEventBuilder;
            protected: DurSpecialistTransientEvent();
            public: ~DurSpecialistTransientEvent();
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