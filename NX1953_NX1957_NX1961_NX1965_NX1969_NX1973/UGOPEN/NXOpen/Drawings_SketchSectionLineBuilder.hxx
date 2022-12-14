#ifndef NXOpen_DRAWINGS_SKETCHSECTIONLINEBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_SKETCHSECTIONLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_SketchSectionLineBuilder.ja
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
#include <NXOpen/Drawings_ParentViewBuilder.hxx>
#include <NXOpen/Drawings_SectionLineSettingsBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class SketchSectionLineBuilder;
    }
    class Builder;
    namespace Drawings
    {
        class ParentViewBuilder;
    }
    namespace Drawings
    {
        class SectionLineSettingsBuilder;
    }
    namespace Drawings
    {
        class SelectDraftingView;
    }
    class Section;
    class Sketch;
    namespace Drawings
    {
        class _SketchSectionLineBuilderBuilder;
        class SketchSectionLineBuilderImpl;
        /** Represents a @link Drawings::SectionLine Drawings::SectionLine@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Drawings::SectionLineCollection::CreateSketchSectionLineBuilder  NXOpen::Drawings::SectionLineCollection::CreateSketchSectionLineBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AssociateToSketch </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        FoldedToggle </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        SectionLineType </term> <description> 
         
        SimpleStepped </description> </item> 

        <item><term> 
         
        SectionType </term> <description> 
         
        StandAlone </description> </item> 

        </list> 

         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  SketchSectionLineBuilder : public NXOpen::Builder
        {
            /** Section  type */
            public: enum Type
            {
                TypeStandAlone/** stand alone */ ,
                TypeDerived/** derived */ 
            };

            /** Section line type */
            public: enum SectionLineTypes
            {
                SectionLineTypesSimpleStepped/** simple stepped */ ,
                SectionLineTypesHalf/** half */ ,
                SectionLineTypesPoinToPoint/** poin to point */ 
            };

            private: SketchSectionLineBuilderImpl * m_sketchsectionlinebuilder_impl;
            private: friend class  _SketchSectionLineBuilderBuilder;
            protected: SketchSectionLineBuilder();
            public: ~SketchSectionLineBuilder();
            /**Returns  the parent view 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::ParentViewBuilder * ParentView
            (
            );
            /** Set the sketch 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetSketch
            (
                NXOpen::Sketch * sketch /** the sketch which created or selected*/
            );
            /**Returns  the sketch section 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * SketchSection
            (
            );
            /**Returns  the section line type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SketchSectionLineBuilder::SectionLineTypes SectionLineType
            (
            );
            /**Sets  the section line type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetSectionLineType
            (
                NXOpen::Drawings::SketchSectionLineBuilder::SectionLineTypes sectionLineType /** sectionlinetype */ 
            );
            /**Returns  the reverse direction 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reversedirection */ 
            );
            /**Returns  the folded toggle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool FoldedToggle
            (
            );
            /**Sets  the folded toggle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetFoldedToggle
            (
                bool foldedToggle /** foldedtoggle */ 
            );
            /**Returns  the settings 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SectionLineSettingsBuilder * Settings
            (
            );
            /**Returns  the associate to sketch 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool AssociateToSketch
            (
            );
            /**Sets  the associate to sketch 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAssociateToSketch
            (
                bool associateToSketch /** associatetosketch */ 
            );
            /**Returns  the section type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SketchSectionLineBuilder::Type SectionType
            (
            );
            /**Sets  the section type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetSectionType
            (
                NXOpen::Drawings::SketchSectionLineBuilder::Type sectionType /** sectiontype */ 
            );
            /**Returns  the source view 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Drawings::SelectDraftingView * SourceView
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
