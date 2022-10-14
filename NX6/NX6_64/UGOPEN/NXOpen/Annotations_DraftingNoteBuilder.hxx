#ifndef NXOpen_ANNOTATIONS_DRAFTINGNOTEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRAFTINGNOTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DraftingNoteBuilder.ja
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
#include <NXOpen/Annotations_DraftingNoteBuilder.hxx>
#include <NXOpen/Annotations_LeaderBuilder.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Annotations_StyleBuilder.hxx>
#include <NXOpen/Annotations_TextWithEditControlsBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class DraftingNoteBuilder;
    }
    namespace Annotations
    {
        class LeaderBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    namespace Annotations
    {
        class TextWithEditControlsBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _DraftingNoteBuilderBuilder;
        /** Represents a @link Note Note@endlink  builder  <br> To create a new instance of this class, use @link Annotations::AnnotationManager::CreateDraftingNoteBuilder Annotations::AnnotationManager::CreateDraftingNoteBuilder@endlink  <br> 
        Default values:
        Text.TextBlock.SymbolAspectRatio: 1.0
        Text.TextBlock.SymbolHeight: 25.4 (millimeters part), 1.0 (inches part)
        Text.TextBlock.SymbolLength: 25.4 (millimeters part), 1.0 (inches part)
        Text.TextBlock.SymbolScale: 1.0
        Text.TextBlock.SymbolSizeMethod: ScaleAndAspectRatio
        */
        class NXOPENCPPEXPORT DraftingNoteBuilder : public Builder
        {
            /** text over leader types for text */
            public: enum TextAlign
            {
                TextAlignTop/** Align top */,
                TextAlignMiddle/** Align middle */,
                TextAlignBottom/** Align bottom */,
                TextAlignBelowbottomExtToMax/** Align below bottom extension to maximum */,
                TextAlignBelowbottomExtToMaxUnderline/** Align below bottom extension to maximum and underline */,
                TextAlignBelowbottom/** Align below bottom */,
                TextAlignBelowbottomUnderline/** Align below bottom and underline */,
                TextAlignBelowTopExtToMax/** Align below top extension to maximum */,
                TextAlignBelowTopExtToMaxUnderline/** Align below top extension to maximum and underline */,
                TextAlignBelowTop/** Align below top */,
                TextAlignBelowTopUnderline/** Align below top and underline */
            };

            /** thickness types for text */
            public: enum ThicknessTypes
            {
                ThicknessTypesMedium/** Medium thickness type */,
                ThicknessTypesThick/** Thick thickness type */
            };

            private: friend class  _DraftingNoteBuilderBuilder;
            protected: DraftingNoteBuilder();
            /**Returns  the origin  <br> License requirements : None */
            public: NXOpen::Annotations::OriginBuilder * Origin
            (
            );
            /**Returns  the @link Annotations::LeaderBuilder Annotations::LeaderBuilder@endlink  for the annotation  <br> License requirements : None */
            public: NXOpen::Annotations::LeaderBuilder * Leader
            (
            );
            /**Returns  the text  <br> License requirements : None */
            public: NXOpen::Annotations::TextWithEditControlsBuilder * Text
            (
            );
            /**Returns  the style builder  <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * Style
            (
            );
            /**Returns  the vertical text for text  <br> License requirements : None */
            public: bool VerticalText
            (
            );
            /**Sets  the vertical text for text  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetVerticalText
            (
                bool verticalText /** verticaltext */ 
            );
            /**Returns  the text alignment  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Annotations::DraftingNoteBuilder::TextAlign TextAlignment
            (
            );
            /**Sets  the text alignment  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetTextAlignment
            (
                NXOpen::Annotations::DraftingNoteBuilder::TextAlign textAlignment /** textalignment */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif