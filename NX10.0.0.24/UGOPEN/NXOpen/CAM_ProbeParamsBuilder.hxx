#ifndef NXOpen_CAM_PROBEPARAMSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_PROBEPARAMSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ProbeParamsBuilder.ja
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
#include <NXOpen/CAM_ProbeControlParametersBuilder.hxx>
#include <NXOpen/CAM_ProbeParamsBuilder.hxx>
#include <NXOpen/CAM_ProbeProtectedParametersBuilder.hxx>
#include <NXOpen/CAM_ProbeStockParametersBuilder.hxx>
#include <NXOpen/CAM_ProbeToleranceParametersBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ProbeParamsBuilder;
    }
    namespace CAM
    {
        class ProbeControlParametersBuilder;
    }
    namespace CAM
    {
        class ProbeProtectedParametersBuilder;
    }
    namespace CAM
    {
        class ProbeStockParametersBuilder;
    }
    namespace CAM
    {
        class ProbeToleranceParametersBuilder;
    }
    namespace CAM
    {
        class _ProbeParamsBuilderBuilder;
        class ProbeParamsBuilderImpl;
        /** Represents the Probe Params Builder  <br> This builder cannot be instantiated separately.  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ProbeParamsBuilder : public NXOpen::TaggedObject
        {
            private: ProbeParamsBuilderImpl * m_probeparamsbuilder_impl;
            private: friend class  _ProbeParamsBuilderBuilder;
            protected: ProbeParamsBuilder();
            public: ~ProbeParamsBuilder();
            /**Returns  the probe protected parameters builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeProtectedParametersBuilder * ProbeProtectedParameters
            (
            );
            /**Returns  the probe control  parameters builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeControlParametersBuilder * ProbeControlParameters
            (
            );
            /**Returns  the probe stock  parameters builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeStockParametersBuilder * ProbeStockParameters
            (
            );
            /**Returns  the probe tolerance parameters builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeToleranceParametersBuilder * ProbeToleranceParameters
            (
            );
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
