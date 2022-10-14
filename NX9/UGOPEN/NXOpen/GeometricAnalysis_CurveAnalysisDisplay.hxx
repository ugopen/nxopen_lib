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
        /** Represents a tool to control whether to show a curve's poles,knots,combs,peaks and inflections  <br> To obtain an instance of this class, refer to @link GeometricAnalysis::AnalysisObjectCollection  GeometricAnalysis::AnalysisObjectCollection @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICANALYSISEXPORT  CurveAnalysisDisplay
        {
            /** Show flag types 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link GeometricAnalysis::CurveAnalysisDisplay::SetShowPole GeometricAnalysis::CurveAnalysisDisplay::SetShowPole@endlink , @link GeometricAnalysis::CurveAnalysisDisplay::SetShowKnot GeometricAnalysis::CurveAnalysisDisplay::SetShowKnot@endlink , @link GeometricAnalysis::CurveAnalysisDisplay::SetShowEndPoints GeometricAnalysis::CurveAnalysisDisplay::SetShowEndPoints@endlink  methods. <br>  
            */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use GeometricAnalysis::CurveAnalysisDisplay::SetShowPole, GeometricAnalysis::CurveAnalysisDisplay::SetShowKnot, GeometricAnalysis::CurveAnalysisDisplay::SetShowEndPoints methods.") enum ShowFlagType
            {
                ShowFlagTypePole/** show pole   */,
                ShowFlagTypeComb/** show comb */,
                ShowFlagTypeInflection/** show inflection */,
                ShowFlagTypePeak/** show peak      */,
                ShowFlagTypeKnot/** show knot      */,
                ShowFlagTypeEndpoint/** show endpoint  */
            };

            private: CurveAnalysisDisplayImpl * m_curveanalysisdisplay_impl;
            private: NXOpen::GeometricAnalysis::AnalysisObjectCollection* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CurveAnalysisDisplay(NXOpen::GeometricAnalysis::AnalysisObjectCollection *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CurveAnalysisDisplay();
            /** Sets analysis record 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link GeometricAnalysis::CurveCurvatureAnalysis GeometricAnalysis::CurveCurvatureAnalysis@endlink . <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use GeometricAnalysis::CurveCurvatureAnalysis.") void SetAnalysisRecord
            (
                NXOpen::Curve * curve /** curve */,
                NXOpen::GeometricAnalysis::CurveAnalysisRecord * record /** curve analysis record */
            );
            /** Gets analysis record  @return  curve analysis record 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link GeometricAnalysis::CurveCurvatureAnalysis GeometricAnalysis::CurveCurvatureAnalysis@endlink . <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use GeometricAnalysis::CurveCurvatureAnalysis.") NXOpen::GeometricAnalysis::CurveAnalysisRecord * GetAnalysisRecord
            (
                NXOpen::Curve * curve /** curve */
            );
            /** Creats a curve analysis record  @return  
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link GeometricAnalysis::CurveCurvatureAnalysis GeometricAnalysis::CurveCurvatureAnalysis@endlink . <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use GeometricAnalysis::CurveCurvatureAnalysis.") NXOpen::GeometricAnalysis::CurveAnalysisRecord * NewRecord
            (
            );
            /** Sets show flags 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link GeometricAnalysis::CurveCurvatureAnalysis GeometricAnalysis::CurveCurvatureAnalysis@endlink . <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use GeometricAnalysis::CurveCurvatureAnalysis.") void SetShowFlag
            (
                NXOpen::Curve * curve /** curve */,
                NXOpen::GeometricAnalysis::CurveAnalysisDisplay::ShowFlagType choice /** pole/comb/inflection/peak/knot */,
                bool on /** true/false to show flags */
            );
            /** Sets a flag representing poles display state of a b-spline curve 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetShowPole
            (
                NXOpen::Curve * curve /** curve */,
                bool show /** show */ 
            );
            /** Gets a flag representing poles display state of a b-spline curve @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool GetShowPole
            (
                NXOpen::Curve * curve /** curve */
            );
            /** Sets a flag representing knots display state of a b-spline curve
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetShowKnot
            (
                NXOpen::Curve * curve /** curve */,
                bool show /** show */ 
            );
            /** Gets a flag representing knots display state of a b-spline curve @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool GetShowKnot
            (
                NXOpen::Curve * curve /** curve */
            );
            /** Sets a flag representing end points display state of a curve
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetShowEndPoints
            (
                NXOpen::Curve * curve /** curve */,
                bool show /** show */ 
            );
            /** Gets a flag representing end points display state of a curve @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool GetShowEndPoints
            (
                NXOpen::Curve * curve /** curve */
            );
        }; //lint !e1712 default constructor not defined for class  

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