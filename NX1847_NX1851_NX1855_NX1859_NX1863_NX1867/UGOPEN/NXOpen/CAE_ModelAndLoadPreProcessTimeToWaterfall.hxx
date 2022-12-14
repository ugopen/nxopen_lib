#ifndef NXOpen_CAE_MODELANDLOADPREPROCESSTIMETOWATERFALL_HXX_INCLUDED
#define NXOpen_CAE_MODELANDLOADPREPROCESSTIMETOWATERFALL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelAndLoadPreProcessTimeToWaterfall.ja
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
#include <NXOpen/CAE_ModelAndLoadPreProcessOperation.hxx>
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
        class ModelAndLoadPreProcessTimeToWaterfall;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcessOperation;
    }
    namespace CAE
    {
        class _ModelAndLoadPreProcessTimeToWaterfallBuilder;
        class ModelAndLoadPreProcessTimeToWaterfallImpl;
        /** Represents a @link NXOpen::CAE::ModelAndLoadPreProcessTimeToWaterfall NXOpen::CAE::ModelAndLoadPreProcessTimeToWaterfall@endlink . 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ModelAndLoadPreProcessTimeToWaterfall : public NXOpen::CAE::ModelAndLoadPreProcessOperation
        {
            private: ModelAndLoadPreProcessTimeToWaterfallImpl * m_modelandloadpreprocesstimetowaterfall_impl;
            private: friend class  _ModelAndLoadPreProcessTimeToWaterfallBuilder;
            protected: ModelAndLoadPreProcessTimeToWaterfall();
            public: ~ModelAndLoadPreProcessTimeToWaterfall();
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
