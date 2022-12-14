#ifndef NXOpen_DISPLAY_SELECTFONTFILEBUILDER_HXX_INCLUDED
#define NXOpen_DISPLAY_SELECTFONTFILEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Display_SelectFontFileBuilder.ja
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
#include <NXOpen/Display_SelectFontFileBuilder.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    namespace Display
    {
        class SelectFontFileBuilder;
    }
    class Builder;
    namespace Display
    {
        class _SelectFontFileBuilderBuilder;
        class SelectFontFileBuilderImpl;
        /**  This class is being used in conjunction with the "Select Font File
             dialog, which is (at least so far) only for internal debugging use.
             So no documentation of this class should be published to customers.
             RDB_FIX What needs to be done to stop this class from being published.

        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        DeletePreviousText </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        Fill </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FontCycling </td> <td> 
         
        Off </td> </tr> 

        <tr><td> 
         
        Geometry </td> <td> 
         
        Absolute </td> </tr> 

        <tr><td> 
         
        GlyphHeight </td> <td> 
         
        0.125 </td> </tr> 

        <tr><td> 
         
        GlyphSpacingAdjustment </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        GlyphWidth </td> <td> 
         
        0.125 </td> </tr> 

        <tr><td> 
         
        HiddenStyle </td> <td> 
         
        Invisible </td> </tr> 

        <tr><td> 
         
        Justification </td> <td> 
         
        Normal </td> </tr> 

        <tr><td> 
         
        Layout </td> <td> 
         
        LeftToRight </td> </tr> 

        <tr><td> 
         
        LineSpacingAdjustment </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        ReferenceLocation </td> <td> 
         
        BaselineStart </td> </tr> 

        <tr><td> 
         
        Rotation2d </td> <td> 
         
        Degrees0 </td> </tr> 

        <tr><td> 
         
        Rotation3d </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Scale3 </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        SuppressKerning </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Vector2X </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        Vector2Y </td> <td> 
         
        0.0 </td> </tr> 

        </table>  
        */
        class NXOPENDEBUGSESSIONCPPEXPORT  SelectFontFileBuilder : public Builder
        {
            /** Identifies the text layout, which defines the direction in which 
                        glyphs advance or flow along a single line, and the direction in 
                        which lines advance or flow along a page. */
            public: enum LayoutType
            {
                LayoutTypeLeftToRight/**
                            A horizontal layout in which the direction of glyph flow on each 
                            line is from left-to-right, and the direction of line flow is 
                            from top-to-bottom. */,
                LayoutTypeRightToLeft/**
                            A horizontal layout in which the direction of glyph flow on each
                            line is from right-to-left, and the direction of line flow is 
                            from top-to-bottom (e.g. Hebrew). */,
                LayoutTypeTopToBottom/**
                            A vertical layout in which the direction of glyph flow on each 
                            line is from top-to-bottom, and the direction of line flow is 
                            from right-to-left (e.g. Chinese, Japanese, Korean). */
            };

            /** Specifies whether available fonts are automatically cycled. */
            public: enum FontCyclingType
            {
                FontCyclingTypeOff/** off */ ,
                FontCyclingTypeOn/** on */ ,
                FontCyclingTypeContinuous/** continuous */ 
            };

            /** Specifies the coordinate spaces of text geometry. */
            public: enum GeometryType
            {
                GeometryTypeAbsolute/** absolute */ ,
                GeometryTypeScreen/** screen */ ,
                GeometryTypeAbsRotScreenSize/** abs rot screen size */ 
            };

            /** Identifies the location on the text box used to position text. */
            public: enum RefLocation
            {
                RefLocationBaselineStart/** baseline start */ ,
                RefLocationBaselineCenter/** baseline center */ ,
                RefLocationBaselineEnd/** baseline end */ ,
                RefLocationTopLeft/** top left */ ,
                RefLocationTopCenter/** top center */ ,
                RefLocationTopRight/** top right */ ,
                RefLocationCenterLeft/** center left */ ,
                RefLocationCenterCenter/** center center */ ,
                RefLocationCenterRight/** center right */ ,
                RefLocationBottomLeft/** bottom left */ ,
                RefLocationBottomCenter/** bottom center */ ,
                RefLocationBottomRight/** bottom right */ 
            };

            /** Specifies how glyphs are justified in the text box. */
            public: enum JustificationType
            {
                JustificationTypeNormal/** normal */ ,
                JustificationTypeCenter/** center */ ,
                JustificationTypeOpposite/** opposite */ 
            };

            /** Specifies how Screen text is rotated in the plane of the screen. */
            public: enum Rotation2dType
            {
                Rotation2dTypeDegrees0/** degrees0 */ ,
                Rotation2dTypeDegrees90/** degrees90 */ ,
                Rotation2dTypeDegrees180/** degrees180 */ ,
                Rotation2dTypeDegrees270/** degrees270 */ 
            };

            /** Specifies the behavior of hidden text. */
            public: enum HiddenStyleType
            {
                HiddenStyleTypeInvisible/** invisible */ ,
                HiddenStyleTypeShowThrough/** show through */ ,
                HiddenStyleTypeOverlay/** overlay */ 
            };

            private: SelectFontFileBuilderImpl * m_selectfontfilebuilder_impl;
            private: friend class  _SelectFontFileBuilderBuilder;
            protected: SelectFontFileBuilder();
            public: ~SelectFontFileBuilder();
            /**Returns  the font name: family name of the font  <br> License requirements : None */
            public: NXString FontName
            (
            );
            /**Sets  the font name: family name of the font  <br> License requirements : None */
            public: void SetFontName
            (
                const NXString & fontName /** fontname */ 
            );
            /**Returns  the style name: style of the font  <br> License requirements : None */
            public: NXString StyleName
            (
            );
            /**Sets  the style name: style of the font  <br> License requirements : None */
            public: void SetStyleName
            (
                const NXString & styleName /** stylename */ 
            );
            /**Returns  the text layout, which defines the direction in which glyphs 
                        advance or flow along a single line, and the direction in which 
                        lines advance or flow along a page.  <br> License requirements : None */
            public: NXOpen::Display::SelectFontFileBuilder::LayoutType Layout
            (
            );
            /**Sets  the text layout, which defines the direction in which glyphs 
                        advance or flow along a single line, and the direction in which 
                        lines advance or flow along a page.  <br> License requirements : None */
            public: void SetLayout
            (
                NXOpen::Display::SelectFontFileBuilder::LayoutType layout /** layout */ 
            );
            /**Returns  whether available fonts are automatically cycled.  <br> License requirements : None */
            public: NXOpen::Display::SelectFontFileBuilder::FontCyclingType FontCycling
            (
            );
            /**Sets  whether available fonts are automatically cycled.  <br> License requirements : None */
            public: void SetFontCycling
            (
                NXOpen::Display::SelectFontFileBuilder::FontCyclingType fontCycling /** fontcycling */ 
            );
            /**Returns   the first line of text.  <br> License requirements : None */
            public: NXString Line1
            (
            );
            /**Sets   the first line of text.  <br> License requirements : None */
            public: void SetLine1
            (
                const NXString & line1 /** line1 */ 
            );
            /**Returns   the second line of text.  <br> License requirements : None */
            public: NXString Line2
            (
            );
            /**Sets   the second line of text.  <br> License requirements : None */
            public: void SetLine2
            (
                const NXString & line2 /** line2 */ 
            );
            /**Returns   the third line of text.  <br> License requirements : None */
            public: NXString Line3
            (
            );
            /**Sets   the third line of text.  <br> License requirements : None */
            public: void SetLine3
            (
                const NXString & line3 /** line3 */ 
            );
            /**Returns  the coordinate spaces of text geometry.  <br> License requirements : None */
            public: NXOpen::Display::SelectFontFileBuilder::GeometryType Geometry
            (
            );
            /**Sets  the coordinate spaces of text geometry.  <br> License requirements : None */
            public: void SetGeometry
            (
                NXOpen::Display::SelectFontFileBuilder::GeometryType geometry /** geometry */ 
            );
            /**Returns  the location on the text box used to position text.  <br> License requirements : None */
            public: NXOpen::Display::SelectFontFileBuilder::RefLocation ReferenceLocation
            (
            );
            /**Sets  the location on the text box used to position text.  <br> License requirements : None */
            public: void SetReferenceLocation
            (
                NXOpen::Display::SelectFontFileBuilder::RefLocation referenceLocation /** referencelocation */ 
            );
            /**Returns  the justification of glyphs in the text box.  <br> License requirements : None */
            public: NXOpen::Display::SelectFontFileBuilder::JustificationType Justification
            (
            );
            /**Sets  the justification of glyphs in the text box.  <br> License requirements : None */
            public: void SetJustification
            (
                NXOpen::Display::SelectFontFileBuilder::JustificationType justification /** justification */ 
            );
            /**Returns  the 3D rotation status; whether 3D text is rotated to the
                        current plane of the work view.  <br> License requirements : None */
            public: bool Rotation3d
            (
            );
            /**Sets  the 3D rotation status; whether 3D text is rotated to the
                        current plane of the work view.  <br> License requirements : None */
            public: void SetRotation3d
            (
                bool rotation3d /** rotation3d */ 
            );
            /**Returns  the 2D rotation status; how Screen text is rotated in the 
                        plane of the screen.  <br> License requirements : None */
            public: NXOpen::Display::SelectFontFileBuilder::Rotation2dType Rotation2d
            (
            );
            /**Sets  the 2D rotation status; how Screen text is rotated in the 
                        plane of the screen.  <br> License requirements : None */
            public: void SetRotation2d
            (
                NXOpen::Display::SelectFontFileBuilder::Rotation2dType rotation2d /** rotation2d */ 
            );
            /**Returns  the glyph width.  <br> License requirements : None */
            public: double GlyphWidth
            (
            );
            /**Sets  the glyph width.  <br> License requirements : None */
            public: void SetGlyphWidth
            (
                double glyphWidth /** glyphwidth */ 
            );
            /**Returns  the glyph height.  <br> License requirements : None */
            public: double GlyphHeight
            (
            );
            /**Sets  the glyph height.  <br> License requirements : None */
            public: void SetGlyphHeight
            (
                double glyphHeight /** glyphheight */ 
            );
            /**Returns  the extra spacing added between glyphs (positive or negative).  <br> License requirements : None */
            public: double GlyphSpacingAdjustment
            (
            );
            /**Sets  the extra spacing added between glyphs (positive or negative).  <br> License requirements : None */
            public: void SetGlyphSpacingAdjustment
            (
                double glyphSpacingAdjustment /** glyphspacingadjustment */ 
            );
            /**Returns  the extra spacing added between lines (positive or negative).  <br> License requirements : None */
            public: double LineSpacingAdjustment
            (
            );
            /**Sets  the extra spacing added between lines (positive or negative).  <br> License requirements : None */
            public: void SetLineSpacingAdjustment
            (
                double lineSpacingAdjustment /** linespacingadjustment */ 
            );
            /**Returns  the kerning status; whether kerning is suppressed.  <br> License requirements : None */
            public: bool SuppressKerning
            (
            );
            /**Sets  the kerning status; whether kerning is suppressed.  <br> License requirements : None */
            public: void SetSuppressKerning
            (
                bool suppressKerning /** suppresskerning */ 
            );
            /**Returns  the 3D offset scale for ScreenPoints.  <br> License requirements : None */
            public: double Scale3
            (
            );
            /**Sets  the 3D offset scale for ScreenPoints.  <br> License requirements : None */
            public: void SetScale3
            (
                double scale3 /** scale3 */ 
            );
            /**Returns  the 2D X offset for ScreenPoints.  <br> License requirements : None */
            public: double Vector2X
            (
            );
            /**Sets  the 2D X offset for ScreenPoints.  <br> License requirements : None */
            public: void SetVector2X
            (
                double vector2X /** vector2x */ 
            );
            /**Returns  the 2D Y offset for ScreenPoints.  <br> License requirements : None */
            public: double Vector2Y
            (
            );
            /**Sets  the 2D Y offset for ScreenPoints.  <br> License requirements : None */
            public: void SetVector2Y
            (
                double vector2Y /** vector2y */ 
            );
            /**Returns  the fill status; whether the text box background is filled.  <br> License requirements : None */
            public: bool Fill
            (
            );
            /**Sets  the fill status; whether the text box background is filled.  <br> License requirements : None */
            public: void SetFill
            (
                bool fill /** fill */ 
            );
            /**Returns  the behavior of hidden text.  <br> License requirements : None */
            public: NXOpen::Display::SelectFontFileBuilder::HiddenStyleType HiddenStyle
            (
            );
            /**Sets  the behavior of hidden text.  <br> License requirements : None */
            public: void SetHiddenStyle
            (
                NXOpen::Display::SelectFontFileBuilder::HiddenStyleType hiddenStyle /** hiddenstyle */ 
            );
            /**Returns  the delete behavior; whether previously created text is 
                        automatically deleted before displaying new text.  <br> License requirements : None */
            public: bool DeletePreviousText
            (
            );
            /**Sets  the delete behavior; whether previously created text is 
                        automatically deleted before displaying new text.  <br> License requirements : None */
            public: void SetDeletePreviousText
            (
                bool deletePreviousText /** deleteprevioustext */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
