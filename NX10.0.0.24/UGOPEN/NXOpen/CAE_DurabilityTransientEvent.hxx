#ifndef NXOpen_CAE_DURABILITYTRANSIENTEVENT_HXX_INCLUDED
#define NXOpen_CAE_DURABILITYTRANSIENTEVENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurabilityTransientEvent.ja
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
#include <NXOpen/CAE_DurabilityEvent.hxx>
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
        class DurabilityTransientEvent;
    }
    namespace CAE
    {
        class DurabilityEvent;
    }
    namespace CAE
    {
        class _DurabilityTransientEventBuilder;
        class DurabilityTransientEventImpl;
        /** Represents a @link NXOpen::CAE::DurabilityTransientEvent NXOpen::CAE::DurabilityTransientEvent@endlink . 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurabilityTransientEvent : public NXOpen::CAE::DurabilityEvent
        {
            private: DurabilityTransientEventImpl * m_durabilitytransientevent_impl;
            private: friend class  _DurabilityTransientEventBuilder;
            protected: DurabilityTransientEvent();
            public: ~DurabilityTransientEvent();
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
