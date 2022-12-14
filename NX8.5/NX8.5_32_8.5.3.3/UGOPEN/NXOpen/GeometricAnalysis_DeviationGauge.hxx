#ifndef NXOpen_GEOMETRICANALYSIS_DEVIATIONGAUGE_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_DEVIATIONGAUGE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_DeviationGauge.ja
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
#include <NXOpen/GeometricAnalysis_AnalysisObject.hxx>
#include <NXOpen/libnxopencpp_geometricanalysis_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class DeviationGauge;
    }
    namespace GeometricAnalysis
    {
        class AnalysisObject;
    }
    namespace GeometricAnalysis
    {
        class _DeviationGaugeBuilder;
        class DeviationGaugeImpl;
        /** Deviation Gauge analysis object class  <br> To create or edit an instance of this class, use @link GeometricAnalysis::DeviationGaugeBuilder  GeometricAnalysis::DeviationGaugeBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICANALYSISEXPORT  DeviationGauge : public GeometricAnalysis::AnalysisObject
        {
            private: DeviationGaugeImpl * m_deviationgauge_impl;
            private: friend class  _DeviationGaugeBuilder;
            protected: DeviationGauge();
            public: ~DeviationGauge();
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
