#ifndef NXOpen_CAE_MODELANDLOADPREPROCESSPRESSURETOFORCEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MODELANDLOADPREPROCESSPRESSURETOFORCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelAndLoadPreProcessPressureToForceBuilder.ja
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
#include <NXOpen/CAE_ModelAndLoadPreProcessOperationBuilder.hxx>
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
        class ModelAndLoadPreProcessPressureToForceBuilder;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcessOperationBuilder;
    }
    namespace CAE
    {
        class _ModelAndLoadPreProcessPressureToForceBuilderBuilder;
        class ModelAndLoadPreProcessPressureToForceBuilderImpl;
        /**
            Builds a @link NXOpen::CAE::ModelAndLoadPreProcessPressureToForce NXOpen::CAE::ModelAndLoadPreProcessPressureToForce@endlink  object which 
            represets an operation.
             <br> There is no kf creator for this.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ModelAndLoadPreProcessPressureToForceBuilder : public NXOpen::CAE::ModelAndLoadPreProcessOperationBuilder
        {
            private: ModelAndLoadPreProcessPressureToForceBuilderImpl * m_modelandloadpreprocesspressuretoforcebuilder_impl;
            private: friend class  _ModelAndLoadPreProcessPressureToForceBuilderBuilder;
            protected: ModelAndLoadPreProcessPressureToForceBuilder();
            public: ~ModelAndLoadPreProcessPressureToForceBuilder();
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