#ifndef NXOpen_GEOMETRICANALYSIS_CURVEANALYSISPEAKSBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_CURVEANALYSISPEAKSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_CurveAnalysisPeaksBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/GeometricAnalysis_CurveAnalysisPeaksBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class CurveAnalysisPeaksBuilder;
    }
    class Builder;
    class Direction;
    class Point;
    class ScCollector;
    namespace GeometricAnalysis
    {
        class _CurveAnalysisPeaksBuilderBuilder;
        /**
            This class handles the options setting for the curve analysis information (Peaks) display.
             <br> To create a new instance of this class, use @link GeometricAnalysis::AnalysisObjectCollection::CreateCurveAnalysisPeaksBuilder GeometricAnalysis::AnalysisObjectCollection::CreateCurveAnalysisPeaksBuilder@endlink  <br> */
        class NXOPENCPPEXPORT CurveAnalysisPeaksBuilder : public Builder
        {
            /** Direction option types */
            public: enum DirectionOptionType
            {
                DirectionOptionTypeNone/** no direction    */,
                DirectionOptionTypePlaneOfCurve/** best fit plane  */,
                DirectionOptionTypeSpecifyVector/** specify vector  */,
                DirectionOptionTypeWorkView/** work view       */
            };

            private: friend class  _CurveAnalysisPeaksBuilderBuilder;
            protected: CurveAnalysisPeaksBuilder();
            /**Returns  the selected curves  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::ScCollector * SelectedCurves
            (
            );
            /**Returns  the direction option  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricAnalysis::CurveAnalysisPeaksBuilder::DirectionOptionType DirectionOption
            (
            );
            /**Sets  the direction option  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDirectionOption
            (
                NXOpen::GeometricAnalysis::CurveAnalysisPeaksBuilder::DirectionOptionType option /** option */ 
            );
            /**Returns  the vector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Direction * Vector
            (
            );
            /**Sets  the vector  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetVector
            (
                NXOpen::Direction * vect /** vect */ 
            );
            /** Create points at the peaks of the curve @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::Point *> CreatePoints
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif