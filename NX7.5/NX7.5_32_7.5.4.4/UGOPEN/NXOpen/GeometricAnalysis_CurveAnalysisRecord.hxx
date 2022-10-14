#ifndef NXOpen_GEOMETRICANALYSIS_CURVEANALYSISRECORD_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_CURVEANALYSISRECORD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_CurveAnalysisRecord.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class CurveAnalysisRecord;
    }
    namespace GeometricAnalysis
    {
        class CurveAnalysisRecordImpl;
        /** Represents the information regarding how to display a curve's poles, knots, combs, peaks and inflections */
        class NXOPENCPPEXPORT  CurveAnalysisRecord : public TransientObject
        {
            /** Direction option types */
            public: enum DirectionOptionType
            {
                DirectionOptionTypeNone/** no direction   */,
                DirectionOptionTypePlaneOfCurve/** best fit plane */,
                DirectionOptionTypeSpecifyVector/** specify vector */,
                DirectionOptionTypeWorkView/** work view      */
            };

            private: CurveAnalysisRecordImpl * m_curveanalysisrecord_impl;
            public: explicit CurveAnalysisRecord(void *ptr);
            /** Free resources associated with the instance.  <br> License requirements : None */
            public: virtual ~CurveAnalysisRecord();
            /**Sets  the flag to show pole  <br> License requirements : None */
            public: void SetShowPole
            (
                bool on /** true to show pole */
            );
            /**Returns  the flag to show pole  <br> License requirements : None */
            public: bool ShowPole
            (
            );
            /**Sets  the flag to show comb  <br> License requirements : None */
            public: void SetShowComb
            (
                bool on /** true to show comb */
            );
            /**Returns  the flag to show comb  <br> License requirements : None */
            public: bool ShowComb
            (
            );
            /**Sets  the flag to show inflection  <br> License requirements : None */
            public: void SetShowInflection
            (
                bool on /** true to show inflection */
            );
            /**Returns  the flag to show inflection  <br> License requirements : None */
            public: bool ShowInflection
            (
            );
            /**Sets  the flag to show peak  <br> License requirements : None */
            public: void SetShowPeak
            (
                bool on /** true to show peak */
            );
            /**Returns  the flag to show peak  <br> License requirements : None */
            public: bool ShowPeak
            (
            );
            /**Sets  the flag to show knot  <br> License requirements : None */
            public: void SetShowKnot
            (
                bool on /** true to show knot */
            );
            /**Returns  the flag to show knot  <br> License requirements : None */
            public: bool ShowKnot
            (
            );
            /**Sets  the start parameter, range from 0 to 100  <br> License requirements : None */
            public: void SetStart
            (
                double start /** start parameter */
            );
            /**Returns  the start parameter, range from 0 to 100  <br> License requirements : None */
            public: double Start
            (
            );
            /**Sets  the end parameter  <br> License requirements : None */
            public: void SetEnd
            (
                double end /** end parameter */
            );
            /**Returns  the end parameter  <br> License requirements : None */
            public: double End
            (
            );
            /**Sets  the comb density  <br> License requirements : None */
            public: void SetCombDensity
            (
                int density /** comb density */
            );
            /**Returns  the comb density  <br> License requirements : None */
            public: int CombDensity
            (
            );
            /**Sets  the comb interneedle density  <br> License requirements : None */
            public: void SetCombInterneedleDensity
            (
                int interneedleDensity /** comb interneedle density */
            );
            /**Returns  the comb interneedle density  <br> License requirements : None */
            public: int CombInterneedleDensity
            (
            );
            /**Sets  the flag to limit the maximum length of the comb  <br> License requirements : None */
            public: void SetUseMaxLength
            (
                bool on /** true to use the max length to limit comb */
            );
            /**Returns  the flag to limit the maximum length of the comb  <br> License requirements : None */
            public: bool UseMaxLength
            (
            );
            /**Sets  the comb maximum length  <br> License requirements : None */
            public: void SetCombMaxLength
            (
                double maxLength /** max length */
            );
            /**Returns  the comb maximum length  <br> License requirements : None */
            public: double CombMaxLength
            (
            );
            /**Sets  the direction option  <br> License requirements : None */
            public: void SetDirectionOption
            (
                NXOpen::GeometricAnalysis::CurveAnalysisRecord::DirectionOptionType directionOption /** direction option */
            );
            /**Returns  the direction option  <br> License requirements : None */
            public: NXOpen::GeometricAnalysis::CurveAnalysisRecord::DirectionOptionType DirectionOption
            (
            );
            /**Sets  the diection  <br> License requirements : None */
            public: void SetDirection
            (
                const NXOpen::Vector3d & direction /** direction */
            );
            /**Returns  the diection  <br> License requirements : None */
            public: NXOpen::Vector3d Direction
            (
            );
            /**Sets  the comb scale factor  <br> License requirements : None */
            public: void SetCombScaleFactor
            (
                double factor /** comb scale factor */
            );
            /**Returns  the comb scale factor  <br> License requirements : None */
            public: double CombScaleFactor
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif