#ifndef NXOpen_CAE_SIMSOUNDPROCESSINGIMPULSERESPONSE_HXX_INCLUDED
#define NXOpen_CAE_SIMSOUNDPROCESSINGIMPULSERESPONSE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimSoundProcessingImpulseResponse.ja
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
        class SimSoundProcessingImpulseResponse;
    }
    class NXObject;
    namespace CAE
    {
        class _SimSoundProcessingImpulseResponseBuilder;
        class SimSoundProcessingImpulseResponseImpl;
        /**  @brief  Represents a Sound Processing Impulse Response object  

         
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimSoundProcessingImpulseResponse : public NXOpen::NXObject
        {
            private: SimSoundProcessingImpulseResponseImpl * m_simsoundprocessingimpulseresponse_impl;
            private: friend class  _SimSoundProcessingImpulseResponseBuilder;
            protected: SimSoundProcessingImpulseResponse();
            public: ~SimSoundProcessingImpulseResponse();
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