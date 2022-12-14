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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/GeometricAnalysis_AnalysisObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Deviation Gauge analysis object class */
        class NXOPENCPPEXPORT DeviationGauge : public GeometricAnalysis::AnalysisObject
        {
            private: friend class  _DeviationGaugeBuilder;
            protected: DeviationGauge();
        };
    }
}
#undef EXPORTLIBRARY
#endif
