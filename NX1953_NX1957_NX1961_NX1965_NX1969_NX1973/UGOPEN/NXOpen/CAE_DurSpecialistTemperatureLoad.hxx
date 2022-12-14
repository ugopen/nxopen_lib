#ifndef NXOpen_CAE_DURSPECIALISTTEMPERATURELOAD_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTTEMPERATURELOAD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistTemperatureLoad.ja
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
        class DurSpecialistTemperatureLoad;
    }
    class NXObject;
    namespace CAE
    {
        class _DurSpecialistTemperatureLoadBuilder;
        class DurSpecialistTemperatureLoadImpl;
        /** Represents a @link NXOpen::CAE::DurSpecialistTemperatureLoad NXOpen::CAE::DurSpecialistTemperatureLoad@endlink   <br> To create or edit an instance of this class, use @link NXOpen::CAE::DurSpecialistTemperatureLoadBuilder  NXOpen::CAE::DurSpecialistTemperatureLoadBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistTemperatureLoad : public NXOpen::NXObject
        {
            private: DurSpecialistTemperatureLoadImpl * m_durspecialisttemperatureload_impl;
            private: friend class  _DurSpecialistTemperatureLoadBuilder;
            protected: DurSpecialistTemperatureLoad();
            public: ~DurSpecialistTemperatureLoad();
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
