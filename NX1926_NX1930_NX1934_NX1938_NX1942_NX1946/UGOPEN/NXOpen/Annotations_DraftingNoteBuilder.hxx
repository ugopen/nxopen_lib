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
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Annotations_ForeshorteningSymbolBuilder.hxx>
#include <NXOpen/Annotations_LeaderBuilder.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Annotations_StyleBuilder.hxx>
#include <NXOpen/Annotations_TextWithEditControlsBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class DraftingNoteBuilder;
    }
    namespace Annotations
    {
        class ForeshorteningSymbolBuilder;
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
        class SimpleDraftingAid;
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
    class SelectDisplayableObject;
    namespace Annotations
    {
        class _DraftingNoteBuilderBuilder;
        class DraftingNoteBuilderImpl;
        /** Represents a @link NXOpen::Annotations::Note NXOpen::Annotations::Note@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::AnnotationManager::CreateDraftingNoteBuilder  NXOpen::Annotations::AnnotationManager::CreateDraftingNoteBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Text.TextBlock.CustomSymbolScale </term> <description> 
         
        1.0 </description> </item> 

        <item><term> 
         
        Text.TextBlock.SymbolAspectRatio </term> <description> 
         
        1.0 </description> </item> 

        <item><term> 
         
        Text.TextBlock.SymbolHeight </term> <description> 
         
        25.4 (millimeters part), 1.0 (inches part) </description> </item> 

        <item><term> 
         
        Text.TextBlock.SymbolLength </term> <description> 
         
        25.4 (millimeters part), 1.0 (inches part) </description> </item> 

        <item><term> 
         
        Text.TextBlock.SymbolPreferences </term> <description> 
         
        UseCurrent </description> </item> 

        <item><term> 
         
        Text.TextBlock.SymbolScale </term> <description> 
         
        1.0 </description> </item> 

        <item><term> 
         
        Text.TextBlock.SymbolSizeMethod </term> <description> 
         
        ScaleAndAspectRatio </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DraftingNoteBuilder : public NXOpen::Builder
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

            private: DraftingNoteBuilderImpl * m_draftingnotebuilder_impl;
            private: friend class  _DraftingNoteBuilderBuilder;
            protected: DraftingNoteBuilder();
            public: ~DraftingNoteBuilder();
            /**Returns  the origin 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::OriginBuilder * Origin
            (
            );
            /**Returns  the @link NXOpen::Annotations::LeaderBuilder NXOpen::Annotations::LeaderBuilder@endlink  for the annotation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LeaderBuilder * Leader
            (
            );
            /**Returns  the text 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TextWithEditControlsBuilder * Text
            (
            );
            /**Returns  the style builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * Style
            (
            );
            /**Returns  the vertical text for text 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool VerticalText
            (
            );
            /**Sets  the vertical text for text 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVerticalText
            (
                bool verticalText /** verticaltext */ 
            );
            /**Returns  the text alignment 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::Annotations::DraftingNoteBuilder::TextAlign TextAlignment
            (
            );
            /**Sets  the text alignment 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTextAlignment
            (
                NXOpen::Annotations::DraftingNoteBuilder::TextAlign textAlignment /** textalignment */ 
            );
            /**Returns  the note from which the properties are inherited 
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * Inherit
            (
            );
            /** Inheriting properties from the note  
             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : None */
            public: void InheritProperties
            (
                NXOpen::Annotations::SimpleDraftingAid * annotation /** annotation */ ,
                int recordNumber /** recordnumber */ 
            );
            /**Returns  the foreshortening symbol builder 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ForeshorteningSymbolBuilder * ForeshorteningSymbol
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
