#ifndef NXOpen_TDP_TEMPLATEEDITCELLBUILDER_HXX_INCLUDED
#define NXOpen_TDP_TEMPLATEEDITCELLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     TDP_TemplateEditCellBuilder.ja
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
#include <NXOpen/Annotations_TextWithEditControlsBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/TextColorFontWidthBuilder.hxx>
#include <NXOpen/libtdpopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace TDP
    {
        class TemplateEditCellBuilder;
    }
    namespace Annotations
    {
        class TextWithEditControlsBuilder;
    }
    class Builder;
    class TextColorFontWidthBuilder;
    namespace TDP
    {
        class _TemplateEditCellBuilderBuilder;
        class TemplateEditCellBuilderImpl;
        /** Represents a Edit Cell builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateEditcellBuilder  NXOpen::TDP::Manager::CreateTemplateEditcellBuilder @endlink  <br> 
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

         <br>  Created in NX1847.0.0.  <br>  
        */
        class TDPOPENCPPEXPORT  TemplateEditCellBuilder : public NXOpen::Builder
        {
            /** Represents the option @link NXOpen::TDP::TemplateEditCellBuilder::TextJustificationType NXOpen::TDP::TemplateEditCellBuilder::TextJustificationType@endlink 
                       for a @link NXOpen::TDP::TemplateEditCellBuilder NXOpen::TDP::TemplateEditCellBuilder@endlink .
                    
             <br>  Created in NX1847.0.0.  <br>  
            */
            public: enum TextJustificationType
            {
                TextJustificationTypeLeft/** left */ ,
                TextJustificationTypeCenter/** center */ ,
                TextJustificationTypeRight/** right */ 
            };

            private: TemplateEditCellBuilderImpl * m_templateeditcellbuilder_impl;
            private: friend class  _TemplateEditCellBuilderBuilder;
            protected: TemplateEditCellBuilder();
            public: ~TemplateEditCellBuilder();
            /**Returns  the text 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::TextWithEditControlsBuilder * Text
            (
            );
            /**Returns  the text color font width 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TextColorFontWidthBuilder * TextColorFontWidth
            (
            );
            /**Returns  the height of the cell 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: double TextHeight
            (
            );
            /**Sets  the height of the cell 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTextHeight
            (
                double height /** height */ 
            );
            /**Returns  the text alignment of the cell 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TDP::TemplateEditCellBuilder::TextJustificationType TextJustification
            (
            );
            /**Sets  the text alignment of the cell 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTextJustification
            (
                NXOpen::TDP::TemplateEditCellBuilder::TextJustificationType alignment /** alignment */ 
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
