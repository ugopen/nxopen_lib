#ifndef NXOpen_GEOMETRICANALYSIS_CURVEANALYSISDISPLAY_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_CURVEANALYSISDISPLAY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_CurveAnalysisDisplay.ja
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
#include <NXOpen/GeometricAnalysis_CurveAnalysisRecord.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class CurveAnalysisDisplay;
    }
    namespace GeometricAnalysis
    {
        class AnalysisObjectCollection;
    }
    class Curve;
    namespace GeometricAnalysis
    {
        class CurveAnalysisRecord;
    }
    namespace GeometricAnalysis
    {
        class CurveAnalysisDisplayImpl;
        /** Represents a tool to control whether to show a curve's poles,knots,combs,peaks and inflections  <br> To obtain an instance of this class, refer to @link GeometricAnalysis::AnalysisObjectCollection GeometricAnalysis::AnalysisObjectCollection@endlink  <br> */
        class NXOPENCPPEXPORT  CurveAnalysisDisplay
        {
            /** Show flag types */
            public: enum ShowFlagType
            {
                ShowFlagTypePole/** show pole   */,
                ShowFlagTypeComb/** show comb */,
                ShowFlagTypeInflection/** show inflection */,
                ShowFlagTypePeak/** show peak      */,
                ShowFlagTypeKnot/** show knot      */
            };

            private: CurveAnalysisDisplayImpl * m_curveanalysisdisplay_impl;
            private: NXOpen::GeometricAnalysis::AnalysisObjectCollection* m_owner;
            /** Constructor */
            public: explicit CurveAnalysisDisplay(NXOpen::GeometricAnalysis::AnalysisObjectCollection *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CurveAnalysisDisplay();
            /** Sets analysis record  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAnalysisRecord
            (
                NXOpen::Curve * curve /** curve */,
                NXOpen::GeometricAnalysis::CurveAnalysisRecord * record /** curve analysis record */
            );
            /** Gets analysis record  @return  curve analysis record  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricAnalysis::CurveAnalysisRecord * GetAnalysisRecord
            (
                NXOpen::Curve * curve /** curve */
            );
            /** Creats a curve analysis record  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::GeometricAnalysis::CurveAnalysisRecord * NewRecord
            (
            );
            /** Sets show flags  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetShowFlag
            (
                NXOpen::Curve * curve /** curve */,
                NXOpen::GeometricAnalysis::CurveAnalysisDisplay::ShowFlagType choice /** pole/comb/inflection/peak/knot */,
                bool on /** true/false to show flags */
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
