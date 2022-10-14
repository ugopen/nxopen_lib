#ifndef NXOpen_DRAWINGS_DRAWINGCOMPARESETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_DRAWINGCOMPARESETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_DrawingCompareSettingsBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Drawings_DrawingCompareSettingsBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class DrawingCompareSettingsBuilder;
    }
    class Builder;
    class NXColor;
    namespace Drawings
    {
        class _DrawingCompareSettingsBuilderBuilder;
        class DrawingCompareSettingsBuilderImpl;
        /** Represents a @link Drawings::DrawingCompareSettingsBuilder Drawings::DrawingCompareSettingsBuilder@endlink  builder  <br> To create a new instance of this class, use @link DrawingCompareManager::CreateDrawingCompareSettingsBuilder DrawingCompareManager::CreateDrawingCompareSettingsBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        BaselineForComparison </td> <td> 
         
        Snapshot </td> </tr> 

        <tr><td> 
         
        CenterlineCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CompareTolerance </td> <td> 
         
        0.001 </td> </tr> 

        <tr><td> 
         
        CrosshatchAreaFillsCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        DatumFeatureSymbolCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        DatumFeatureSymbolLeaderTerminatorCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DatumFeatureSymbolOriginCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DatumFeatureSymbolRetainedStatusCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DatumFeatureSymbolTextCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DatumTargetCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        DatumTargetLeaderTerminatorCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DatumTargetOriginCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DatumTargetRetainedStatusCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DatumTargetTextCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DimCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        DimOriginCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DimRetainedStatusCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DimSizeCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DisplayChangeSymbol </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FcfCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        FcfLeaderTerminatorCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FcfOriginCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FcfRetainedStatusCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FcfTextCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        NoteCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        NoteLeaderTerminatorCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        NoteOriginCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        NoteRetainedStatusCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        NoteTextCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        PartListCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        RestartNumbers </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SheetCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        SymbolCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        SymbolFont </td> <td> 
         
        Solid </td> </tr> 

        <tr><td> 
         
        SymbolLeaderTerminatorCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SymbolOriginCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SymbolRetainedStatusCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SymbolSize </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SymbolTextCompare </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SymbolType </td> <td> 
         
        Circle </td> </tr> 

        <tr><td> 
         
        SymbolWidth </td> <td> 
         
        Thin </td> </tr> 

        <tr><td> 
         
        TableCompare </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        ViewCompare </td> <td> 
         
        1 </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  DrawingCompareSettingsBuilder : public Builder
        {
            /** Represents a Compare Settings ComparisonBaseline*/
            public: enum ComparisonBaseline
            {
                ComparisonBaselineSnapshot/** snapshot */ ,
                ComparisonBaselineTrackedChanges/** tracked changes */ 
            };

            /** Represents a Compare Settings Change symbol Types*/
            public: enum ChangeSymbolType
            {
                ChangeSymbolTypeCircle/** circle */ ,
                ChangeSymbolTypeTriangleUp/** triangle up */ ,
                ChangeSymbolTypeTriangleDown/** triangle down */ ,
                ChangeSymbolTypeSquare/** square */ ,
                ChangeSymbolTypeHexagon/** hexagon */ 
            };

            /** Represents a Compare Settings Change symbol font types*/
            public: enum FontType
            {
                FontTypeSolid/** solid */ ,
                FontTypeDashed/** dashed */ ,
                FontTypePhantom/** phantom */ ,
                FontTypeCenterline/** centerline */ ,
                FontTypeDotted/** dotted */ ,
                FontTypeLongDash/** long dash */ ,
                FontTypeDottedDash/** dotted dash */ 
            };

            /** Represents a Compare Settings Change symbol width types*/
            public: enum WidthType
            {
                WidthTypeThin/** thin */ ,
                WidthTypeNormal/** normal */ ,
                WidthTypeThick/** thick */ 
            };

            private: DrawingCompareSettingsBuilderImpl * m_drawingcomparesettingsbuilder_impl;
            private: friend class  _DrawingCompareSettingsBuilderBuilder;
            protected: DrawingCompareSettingsBuilder();
            public: ~DrawingCompareSettingsBuilder();
            /**Returns  the compare tolerance  <br> License requirements : None */
            public: double CompareTolerance
            (
            );
            /**Sets  the compare tolerance  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCompareTolerance
            (
                double compareTolerance /** comparetolerance */ 
            );
            /**Returns  the baseline for comparison  <br> License requirements : None */
            public: NXOpen::Drawings::DrawingCompareSettingsBuilder::ComparisonBaseline BaselineForComparison
            (
            );
            /**Sets  the baseline for comparison  <br> License requirements : drafting ("DRAFTING") */
            public: void SetBaselineForComparison
            (
                NXOpen::Drawings::DrawingCompareSettingsBuilder::ComparisonBaseline baselineForComparison /** baselineforcomparison */ 
            );
            /**Returns  the restart numbers  <br> License requirements : None */
            public: bool RestartNumbers
            (
            );
            /**Sets  the restart numbers  <br> License requirements : drafting ("DRAFTING") */
            public: void SetRestartNumbers
            (
                bool restartNumbers /** restartnumbers */ 
            );
            /**Returns  the display change symbol  <br> License requirements : None */
            public: bool DisplayChangeSymbol
            (
            );
            /**Sets  the display change symbol  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDisplayChangeSymbol
            (
                bool displayChangeSymbol /** displaychangesymbol */ 
            );
            /**Returns  the symbol type  <br> License requirements : None */
            public: NXOpen::Drawings::DrawingCompareSettingsBuilder::ChangeSymbolType SymbolType
            (
            );
            /**Sets  the symbol type  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolType
            (
                NXOpen::Drawings::DrawingCompareSettingsBuilder::ChangeSymbolType symbolType /** symboltype */ 
            );
            /**Returns  the symbol size  <br> License requirements : None */
            public: double SymbolSize
            (
            );
            /**Sets  the symbol size  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolSize
            (
                double symbolSize /** symbolsize */ 
            );
            /**Returns  the color  <br> License requirements : None */
            public: NXOpen::NXColor * Color
            (
            );
            /**Sets  the color  <br> License requirements : drafting ("DRAFTING") */
            public: void SetColor
            (
                NXOpen::NXColor * color /** color */ 
            );
            /**Returns  the symbol font  <br> License requirements : None */
            public: NXOpen::Drawings::DrawingCompareSettingsBuilder::FontType SymbolFont
            (
            );
            /**Sets  the symbol font  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolFont
            (
                NXOpen::Drawings::DrawingCompareSettingsBuilder::FontType symbolFont /** symbolfont */ 
            );
            /**Returns  the symbol width  <br> License requirements : None */
            public: NXOpen::Drawings::DrawingCompareSettingsBuilder::WidthType SymbolWidth
            (
            );
            /**Sets  the symbol width  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolWidth
            (
                NXOpen::Drawings::DrawingCompareSettingsBuilder::WidthType symbolWidth /** symbolwidth */ 
            );
            /**Returns  the sheet compare  <br> License requirements : None */
            public: bool SheetCompare
            (
            );
            /**Sets  the sheet compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSheetCompare
            (
                bool sheetCompare /** sheetcompare */ 
            );
            /**Returns  the view compare  <br> License requirements : None */
            public: bool ViewCompare
            (
            );
            /**Sets  the view compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetViewCompare
            (
                bool viewCompare /** viewcompare */ 
            );
            /**Returns  the dim compare  <br> License requirements : None */
            public: bool DimCompare
            (
            );
            /**Sets  the dim compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDimCompare
            (
                bool dimCompare /** dimcompare */ 
            );
            /**Returns  the dim retained status compare  <br> License requirements : None */
            public: bool DimRetainedStatusCompare
            (
            );
            /**Sets  the dim retained status compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDimRetainedStatusCompare
            (
                bool dimRetainedStatusCompare /** dimretainedstatuscompare */ 
            );
            /**Returns  the dim size compare  <br> License requirements : None */
            public: bool DimSizeCompare
            (
            );
            /**Sets  the dim size compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDimSizeCompare
            (
                bool dimSizeCompare /** dimsizecompare */ 
            );
            /**Returns  the dim origin compare  <br> License requirements : None */
            public: bool DimOriginCompare
            (
            );
            /**Sets  the dim origin compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDimOriginCompare
            (
                bool dimOriginCompare /** dimorigincompare */ 
            );
            /**Returns  the note compare  <br> License requirements : None */
            public: bool NoteCompare
            (
            );
            /**Sets  the note compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetNoteCompare
            (
                bool noteCompare /** notecompare */ 
            );
            /**Returns  the note retained status compare  <br> License requirements : None */
            public: bool NoteRetainedStatusCompare
            (
            );
            /**Sets  the note retained status compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetNoteRetainedStatusCompare
            (
                bool noteRetainedStatusCompare /** noteretainedstatuscompare */ 
            );
            /**Returns  the note text compare  <br> License requirements : None */
            public: bool NoteTextCompare
            (
            );
            /**Sets  the note text compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetNoteTextCompare
            (
                bool noteTextCompare /** notetextcompare */ 
            );
            /**Returns  the note origin compare  <br> License requirements : None */
            public: bool NoteOriginCompare
            (
            );
            /**Sets  the note origin compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetNoteOriginCompare
            (
                bool noteOriginCompare /** noteorigincompare */ 
            );
            /**Returns  the note leader info compare  <br> License requirements : None */
            public: bool NoteLeaderTerminatorCompare
            (
            );
            /**Sets  the note leader info compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetNoteLeaderTerminatorCompare
            (
                bool noteLeaderTerminatorCompare /** noteleaderterminatorcompare */ 
            );
            /**Returns  the fcf compare  <br> License requirements : None */
            public: bool FcfCompare
            (
            );
            /**Sets  the fcf compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFcfCompare
            (
                bool fcfCompare /** fcfcompare */ 
            );
            /**Returns  the fcf retained status compare  <br> License requirements : None */
            public: bool FcfRetainedStatusCompare
            (
            );
            /**Sets  the fcf retained status compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFcfRetainedStatusCompare
            (
                bool fcfRetainedStatusCompare /** fcfretainedstatuscompare */ 
            );
            /**Returns  the fcf text compare  <br> License requirements : None */
            public: bool FcfTextCompare
            (
            );
            /**Sets  the fcf text compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFcfTextCompare
            (
                bool fcfTextCompare /** fcftextcompare */ 
            );
            /**Returns  the fcf origin compare  <br> License requirements : None */
            public: bool FcfOriginCompare
            (
            );
            /**Sets  the fcf origin compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFcfOriginCompare
            (
                bool fcfOriginCompare /** fcforigincompare */ 
            );
            /**Returns  the fcf leader info compare  <br> License requirements : None */
            public: bool FcfLeaderTerminatorCompare
            (
            );
            /**Sets  the fcf leader info compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetFcfLeaderTerminatorCompare
            (
                bool fcfLeaderTerminatorCompare /** fcfleaderterminatorcompare */ 
            );
            /**Returns  the datum feature symbol compare  <br> License requirements : None */
            public: bool DatumFeatureSymbolCompare
            (
            );
            /**Sets  the datum feature symbol compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumFeatureSymbolCompare
            (
                bool datumFeatureSymbolCompare /** datumfeaturesymbolcompare */ 
            );
            /**Returns  the datum feature symbol retained status compare  <br> License requirements : None */
            public: bool DatumFeatureSymbolRetainedStatusCompare
            (
            );
            /**Sets  the datum feature symbol retained status compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumFeatureSymbolRetainedStatusCompare
            (
                bool datumFeatureSymbolRetainedStatusCompare /** datumfeaturesymbolretainedstatuscompare */ 
            );
            /**Returns  the datum feature symbol text compare  <br> License requirements : None */
            public: bool DatumFeatureSymbolTextCompare
            (
            );
            /**Sets  the datum feature symbol text compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumFeatureSymbolTextCompare
            (
                bool datumFeatureSymbolTextCompare /** datumfeaturesymboltextcompare */ 
            );
            /**Returns  the datum feature symbol origin compare  <br> License requirements : None */
            public: bool DatumFeatureSymbolOriginCompare
            (
            );
            /**Sets  the datum feature symbol origin compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumFeatureSymbolOriginCompare
            (
                bool datumFeatureSymbolOriginCompare /** datumfeaturesymbolorigincompare */ 
            );
            /**Returns  the datum feature symbol leader info compare  <br> License requirements : None */
            public: bool DatumFeatureSymbolLeaderTerminatorCompare
            (
            );
            /**Sets  the datum feature symbol leader info compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumFeatureSymbolLeaderTerminatorCompare
            (
                bool datumFeatureSymbolLeaderTerminatorCompare /** datumfeaturesymbolleaderterminatorcompare */ 
            );
            /**Returns  the datum target compare  <br> License requirements : None */
            public: bool DatumTargetCompare
            (
            );
            /**Sets  the datum target compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumTargetCompare
            (
                bool datumTargetCompare /** datumtargetcompare */ 
            );
            /**Returns  the datum target retained status compare  <br> License requirements : None */
            public: bool DatumTargetRetainedStatusCompare
            (
            );
            /**Sets  the datum target retained status compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumTargetRetainedStatusCompare
            (
                bool datumTargetRetainedStatusCompare /** datumtargetretainedstatuscompare */ 
            );
            /**Returns  the datum target text compare  <br> License requirements : None */
            public: bool DatumTargetTextCompare
            (
            );
            /**Sets  the datum target text compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumTargetTextCompare
            (
                bool datumTargetTextCompare /** datumtargettextcompare */ 
            );
            /**Returns  the datum target origin compare  <br> License requirements : None */
            public: bool DatumTargetOriginCompare
            (
            );
            /**Sets  the datum target origin compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumTargetOriginCompare
            (
                bool datumTargetOriginCompare /** datumtargetorigincompare */ 
            );
            /**Returns  the datum target leader info compare  <br> License requirements : None */
            public: bool DatumTargetLeaderTerminatorCompare
            (
            );
            /**Sets  the datum target leader info compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetDatumTargetLeaderTerminatorCompare
            (
                bool datumTargetLeaderTerminatorCompare /** datumtargetleaderterminatorcompare */ 
            );
            /**Returns  the symbol compare  <br> License requirements : None */
            public: bool SymbolCompare
            (
            );
            /**Sets  the symbol compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolCompare
            (
                bool symbolCompare /** symbolcompare */ 
            );
            /**Returns  the symbol retained status compare  <br> License requirements : None */
            public: bool SymbolRetainedStatusCompare
            (
            );
            /**Sets  the symbol retained status compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolRetainedStatusCompare
            (
                bool symbolRetainedStatusCompare /** symbolretainedstatuscompare */ 
            );
            /**Returns  the symbol text compare  <br> License requirements : None */
            public: bool SymbolTextCompare
            (
            );
            /**Sets  the symbol text compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolTextCompare
            (
                bool symbolTextCompare /** symboltextcompare */ 
            );
            /**Returns  the symbol origin compare  <br> License requirements : None */
            public: bool SymbolOriginCompare
            (
            );
            /**Sets  the symbol origin compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolOriginCompare
            (
                bool symbolOriginCompare /** symbolorigincompare */ 
            );
            /**Returns  the symbol leader info compare  <br> License requirements : None */
            public: bool SymbolLeaderTerminatorCompare
            (
            );
            /**Sets  the symbol leader info compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetSymbolLeaderTerminatorCompare
            (
                bool symbolLeaderTerminatorCompare /** symbolleaderterminatorcompare */ 
            );
            /**Returns  the table compare  <br> License requirements : None */
            public: bool TableCompare
            (
            );
            /**Sets  the table compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetTableCompare
            (
                bool tableCompare /** tablecompare */ 
            );
            /**Returns  the part list compare  <br> License requirements : None */
            public: bool PartListCompare
            (
            );
            /**Sets  the part list compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetPartListCompare
            (
                bool partListCompare /** partlistcompare */ 
            );
            /**Returns  the centerline compare  <br> License requirements : None */
            public: bool CenterlineCompare
            (
            );
            /**Sets  the centerline compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCenterlineCompare
            (
                bool centerlineCompare /** centerlinecompare */ 
            );
            /**Returns  the crosshatch area fills compare  <br> License requirements : None */
            public: bool CrosshatchAreaFillsCompare
            (
            );
            /**Sets  the crosshatch area fills compare  <br> License requirements : drafting ("DRAFTING") */
            public: void SetCrosshatchAreaFillsCompare
            (
                bool crosshatchAreaFillsCompare /** crosshatchareafillscompare */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif