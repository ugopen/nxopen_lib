#ifndef NXOpen_CAE_DURABILITYRANDOMEVENT_HXX_INCLUDED
#define NXOpen_CAE_DURABILITYRANDOMEVENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurabilityRandomEvent.ja
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
        class DurabilityRandomEvent;
    }
    namespace CAE
    {
        class DurabilityEvent;
    }
    namespace CAE
    {
        class _DurabilityRandomEventBuilder;
        class DurabilityRandomEventImpl;
        /** Represents a @link NXOpen::CAE::DurabilityRandomEvent NXOpen::CAE::DurabilityRandomEvent@endlink . 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurabilityRandomEvent : public NXOpen::CAE::DurabilityEvent
        {
            private: DurabilityRandomEventImpl * m_durabilityrandomevent_impl;
            private: friend class  _DurabilityRandomEventBuilder;
            protected: DurabilityRandomEvent();
            public: ~DurabilityRandomEvent();
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
