#ifndef NXOpen_CAE_DURSPECIALISTTEMPERATURESOURCE_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTTEMPERATURESOURCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistTemperatureSource.ja
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
        class DurSpecialistTemperatureSource;
    }
    class NXObject;
    namespace CAE
    {
        class _DurSpecialistTemperatureSourceBuilder;
        class DurSpecialistTemperatureSourceImpl;
        /** Represents a @link NXOpen::CAE::DurSpecialistTemperatureSource NXOpen::CAE::DurSpecialistTemperatureSource@endlink   <br> To create or edit an instance of this class, use @link NXOpen::CAE::DurSpecialistTemperatureSourceBuilder  NXOpen::CAE::DurSpecialistTemperatureSourceBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistTemperatureSource : public NXOpen::NXObject
        {
            private: DurSpecialistTemperatureSourceImpl * m_durspecialisttemperaturesource_impl;
            private: friend class  _DurSpecialistTemperatureSourceBuilder;
            protected: DurSpecialistTemperatureSource();
            public: ~DurSpecialistTemperatureSource();
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
