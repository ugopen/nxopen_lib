#ifndef NXOpen_DRAWINGS_TRACKDRAWINGCHANGESREPORTFILTERBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_TRACKDRAWINGCHANGESREPORTFILTERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_TrackDrawingChangesReportFilterBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class TrackDrawingChangesReportFilterBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _TrackDrawingChangesReportFilterBuilderBuilder;
        class TrackDrawingChangesReportFilterBuilderImpl;
        /**
            Represents a @link Drawings::TrackDrawingChangesReportFilterBuilder Drawings::TrackDrawingChangesReportFilterBuilder@endlink 
            
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  TrackDrawingChangesReportFilterBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Represents Report Filter options */
            public: enum Filter
            {
                FilterSheets/** Sheet Report Filter                         */,
                FilterViews/** Views Report Filter                         */,
                FilterDimensionsAll/** Dimension All Report Filter                 */,
                FilterDimensionsRetainedStatus/** Dimension Retained Status Report Filter     */,
                FilterDimensionsSize/** Dimension Size Report Filter                */,
                FilterDimensionsOrigin/** Dimension Origin Report Filter              */,
                FilterAnnotationNotes/** Annotation Notes Report Filter*/,
                FilterAnnotationNotesRetainedStatus/** Annotation Notes Retained Status Report Filter*/,
                FilterAnnotationNotesText/** Annotation Notes Text Report Filter*/,
                FilterAnnotationNotesOrigin/** Annotation Notes Origin Report Filter*/,
                FilterAnnotationNotesLeaderTerminator/** Annotation Notes Leader Terminator Report Filter*/,
                FilterAnnotationFCF/** Annotation Feature Control Frame Report Filter*/,
                FilterAnnotationFCFRetainedStatus/** Annotation Feature Control Frame Retained Status Report Filter*/,
                FilterAnnotationFCFText/** Annotation Feature Control Frame Text Report Filter*/,
                FilterAnnotationFCFOrigin/** Annotation Feature Control Frame Origin Report Filter*/,
                FilterAnnotationFCFLeaderTerminator/** Annotation Feature Control Frame Leader Terminator Report Filter*/,
                FilterAnnotationDFS/** Annotation Datum Feature Symbol Report Filter*/,
                FilterAnnotationDFSRetainedStatus/** Annotation Datum Feature Symbol Retained Status Report Filter*/,
                FilterAnnotationDFSText/** Annotation Datum Feature Symbol Text Report Filter*/,
                FilterAnnotationDFSOrigin/** Annotation Datum Feature Symbol Origin Report Filter*/,
                FilterAnnotationDFSLeaderTerminator/** Annotation Datum Feature Symbol Leader Terminator Report Filter*/,
                FilterAnnotationDTS/** Annotation Datum Target Symbol Report Filter*/,
                FilterAnnotationDTSRetainedStatus/** Annotation Datum Target Symbol Retained Status Report Filter*/,
                FilterAnnotationDTSText/** Annotation Datum Target Symbol Text Report Filter*/,
                FilterAnnotationDTSOrigin/** Annotation Datum Target Symbol Origin Report Filter*/,
                FilterAnnotationDTSLeaderTerminator/** Annotation Datum Target Symbol LeaderTerminator Report Filter*/,
                FilterAnnotationBalloons/** Annotation Balloons Report Filter*/,
                FilterAnnotationBalloonsRetainedStatus/** Annotation Balloons Retained Status Report Filter*/,
                FilterAnnotationBalloonsText/** Annotation Balloons Text Report Filter*/,
                FilterAnnotationBalloonsOrigin/** Annotation Balloons Origin Report Filter*/,
                FilterAnnotationBalloonsLeaderTerminator/** Annotation Balloons LeaderTerminator Report Filter*/,
                FilterAnnotationSFS/** Annotation Surface Finish Symbol Report Filter*/,
                FilterAnnotationSFSRetainedStatus/** Annotation Surface Finish Symbol Retained Status Report Filter*/,
                FilterAnnotationSFSText/** Annotation Surface Finish Symbol Text Report Filter*/,
                FilterAnnotationSFSOrigin/** Annotation Surface Finish Symbol Origin Report Filter*/,
                FilterAnnotationSFSLeaderTerminator/** Annotation Surface Finish Symbol LeaderTerminator Report Filter*/,
                FilterAnnotationWeldSymbol/** Annotation Weld Symbol Report Filter*/,
                FilterAnnotationWeldSymbolRetainedStatus/** Annotation Weld Symbol Retained Status Report Filter*/,
                FilterAnnotationWeldSymbolText/** Annotation Weld Symbol Text Report Filter*/,
                FilterAnnotationWeldSymbolOrigin/** Annotation Weld Symbol Origin Report Filter*/,
                FilterAnnotationWeldSymbolLeaderTerminator/** Annotation Weld Symbol LeaderTerminator Report Filter*/,
                FilterAnnotationTPS/** Annotation Target Point Symbol Report Filter*/,
                FilterAnnotationInterSymbol/** Annotation Intersection Symbol Report Filter*/,
                FilterAnnotationCrosshatch/** Annotation Crosshatch Report Filter*/,
                FilterAnnotationCenterlines/** Annotation Centerlines Report Filter*/,
                FilterSymbols/** Symbols Report Filter*/,
                FilterSymbolsRetainedStatus/** Symbols Retained Status Report Filter*/,
                FilterSymbolsText/** Symbols Text Report Filter*/,
                FilterSymbolsOrigin/** Symbols Origin Report Filter*/,
                FilterSymbolsLeaderTerminator/** Symbols Leader Terminator Report Filter*/,
                FilterTables/** Tables Report Filter*/,
                FilterPartsLists/** Parts Lists Report Filter*/,
                FilterHoleTable/** Hole Table Report Filter*/,
                FilterSketchCurvesLines/** Sketch Curves lines filter*/,
                FilterSketchCurvesArcs/** Sketch Curves arcs filter*/,
                FilterSketchCurvesCircles/** Sketch Curves circles filter*/,
                FilterSketchCurvesConics/** Sketch Curves conics filter*/,
                FilterSketchCurvesSplines/** Sketch Curves splines filter*/
            };

            private: TrackDrawingChangesReportFilterBuilderImpl * m_trackdrawingchangesreportfilterbuilder_impl;
            private: friend class  _TrackDrawingChangesReportFilterBuilderBuilder;
            protected: TrackDrawingChangesReportFilterBuilder();
            public: ~TrackDrawingChangesReportFilterBuilder();
            /** Returns report filter status  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetReportFilterStatus
            (
                NXOpen::Drawings::TrackDrawingChangesReportFilterBuilder::Filter reportFilterType /** reportfiltertype */ 
            );
            /** Sets report filter status 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetReportFilterStatus
            (
                NXOpen::Drawings::TrackDrawingChangesReportFilterBuilder::Filter reportFilterType /** reportfiltertype */ ,
                bool reportFilterStatus /** reportfilterstatus */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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