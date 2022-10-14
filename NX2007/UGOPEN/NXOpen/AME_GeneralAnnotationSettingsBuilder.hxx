#ifndef NXOpen_AME_GENERALANNOTATIONSETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_AME_GENERALANNOTATIONSETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_GeneralAnnotationSettingsBuilder.ja
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
#include <NXOpen/TextColorFontWidthBuilder.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class GeneralAnnotationSettingsBuilder;
    }
    class Builder;
    class TextColorFontWidthBuilder;
    namespace AME
    {
        class _GeneralAnnotationSettingsBuilderBuilder;
        class GeneralAnnotationSettingsBuilderImpl;
        /** builder for the general annotation settings dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateGeneralAnnotationSettingsBuilder  NXOpen::AME::AMEManager::CreateGeneralAnnotationSettingsBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  GeneralAnnotationSettingsBuilder : public NXOpen::Builder
        {
            /** horizontal text postion type */
            public: enum HorizontalTextPosition
            {
                HorizontalTextPositionAbove/** above */ ,
                HorizontalTextPositionBelow/** below */ 
            };

            /** verical text postion type */
            public: enum VerticalTextPosition
            {
                VerticalTextPositionLeft/** left */ ,
                VerticalTextPositionRight/** right */ 
            };

            /** the separator between Source and Target */
            public: enum SourceAndTargetSeparator
            {
                SourceAndTargetSeparatorLessthanGreaterthan/** lessthan greaterthan */ ,
                SourceAndTargetSeparatorSemiColon/** semi colon */ 
            };

            /** the separator for annotation set */
            public: enum AnnotationSeparator
            {
                AnnotationSeparatorSemiColon/** semi colon */ ,
                AnnotationSeparatorComma/** comma */ ,
                AnnotationSeparatorMultiline/** multiline */ 
            };

            private: GeneralAnnotationSettingsBuilderImpl * m_generalannotationsettingsbuilder_impl;
            private: friend class  _GeneralAnnotationSettingsBuilderBuilder;
            protected: GeneralAnnotationSettingsBuilder();
            public: ~GeneralAnnotationSettingsBuilder();
            /**Returns  the text color font width 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::TextColorFontWidthBuilder * TextCFW
            (
            );
            /**Returns  the vertical text position 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::GeneralAnnotationSettingsBuilder::VerticalTextPosition TextPositionVertical
            (
            );
            /**Sets  the vertical text position 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetTextPositionVertical
            (
                NXOpen::AME::GeneralAnnotationSettingsBuilder::VerticalTextPosition type /** type */ 
            );
            /**Returns  the horizontal text position 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::GeneralAnnotationSettingsBuilder::HorizontalTextPosition TextPositionHorizontal
            (
            );
            /**Sets  the horizontal text position 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetTextPositionHorizontal
            (
                NXOpen::AME::GeneralAnnotationSettingsBuilder::HorizontalTextPosition type /** type */ 
            );
            /**Returns  the text offset 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: double Offset
            (
            );
            /**Sets  the text offset 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetOffset
            (
                double textOffset /** textoffset */ 
            );
            /**Returns  the text height 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: double TextHeight
            (
            );
            /**Sets  the text height 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetTextHeight
            (
                double textHeight /** textheight */ 
            );
            /**Returns  the separator for annotation set 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::GeneralAnnotationSettingsBuilder::AnnotationSeparator AnnotationSetSeparator
            (
            );
            /**Sets  the separator for annotation set 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetAnnotationSetSeparator
            (
                NXOpen::AME::GeneralAnnotationSettingsBuilder::AnnotationSeparator type /** type */ 
            );
            /**Returns  the separator between source and target 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::GeneralAnnotationSettingsBuilder::SourceAndTargetSeparator SourceTargetSeparator
            (
            );
            /**Sets  the separator between source and target 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetSourceTargetSeparator
            (
                NXOpen::AME::GeneralAnnotationSettingsBuilder::SourceAndTargetSeparator type /** type */ 
            );
            /** Set the default values 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ResetToDefault
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