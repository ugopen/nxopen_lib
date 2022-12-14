#ifndef NXOpen_AME_FORMSHEETBUILDER_HXX_INCLUDED
#define NXOpen_AME_FORMSHEETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_FormSheetBuilder.ja
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
#include <NXOpen/AME_BasicPropertiesBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class FormSheetBuilder;
    }
    namespace AME
    {
        class BasicPropertiesBuilder;
    }
    class Builder;
    namespace AME
    {
        class _FormSheetBuilderBuilder;
        class FormSheetBuilderImpl;
        /** JA class for the Form Sheet dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateFormSheetBuilder  NXOpen::AME::AMEManager::CreateFormSheetBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        FormSheetSizeOption </term> <description> 
         
        Standard </description> </item> 

        <item><term> 
         
        FormSheetStandardMetricSize </term> <description> 
         
        A3landscape </description> </item> 

        <item><term> 
         
        Height </term> <description> 
         
        297 </description> </item> 

        <item><term> 
         
        Length </term> <description> 
         
        420 </description> </item> 

        <item><term> 
         
        StandardType </term> <description> 
         
        Iec </description> </item> 

        </list> 

         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  FormSheetBuilder : public NXOpen::Builder
        {
            /** Represents form sheet size option */
            public: enum SizeOption
            {
                SizeOptionStandard/** standard */ ,
                SizeOptionCustom/** custom */ 
            };

            /** Represents standard metric sizes for form sheet */
            public: enum StandardMetricSize
            {
                StandardMetricSizeA4landscape/** a4landscape */ ,
                StandardMetricSizeA3landscape/** a3landscape */ ,
                StandardMetricSizeA2landscape/** a2landscape */ ,
                StandardMetricSizeA1landscape/** a1landscape */ ,
                StandardMetricSizeA0landscape/** a0landscape */ ,
                StandardMetricSizeA4portrait/** a4portrait */ 
            };

            /** Represents standard metric sizes for ANSI form sheet */
            public: enum AnsiStandardMetricSize
            {
                AnsiStandardMetricSizeA/** a */ ,
                AnsiStandardMetricSizeB/** b */ ,
                AnsiStandardMetricSizeC/** c */ ,
                AnsiStandardMetricSizeD/** d */ ,
                AnsiStandardMetricSizeE/** e */ 
            };

            /** The types of managing the standard.*/
            public: enum StandardTypes
            {
                StandardTypesIec/** iec */ ,
                StandardTypesAnsi/** ansi */ 
            };

            private: FormSheetBuilderImpl * m_formsheetbuilder_impl;
            private: friend class  _FormSheetBuilderBuilder;
            protected: FormSheetBuilder();
            public: ~FormSheetBuilder();
            /**Returns  the size option type of type @link NXOpen::AME::FormSheetBuilder::SizeOption NXOpen::AME::FormSheetBuilder::SizeOption@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::FormSheetBuilder::SizeOption FormSheetSizeOption
            (
            );
            /**Sets  the size option type of type @link NXOpen::AME::FormSheetBuilder::SizeOption NXOpen::AME::FormSheetBuilder::SizeOption@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFormSheetSizeOption
            (
                NXOpen::AME::FormSheetBuilder::SizeOption sizeOption /** sizeoption */ 
            );
            /**Returns  the standard metric size of type @link NXOpen::AME::FormSheetBuilder::StandardMetricSize NXOpen::AME::FormSheetBuilder::StandardMetricSize@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::FormSheetBuilder::StandardMetricSize FormSheetStandardMetricSize
            (
            );
            /**Sets  the standard metric size of type @link NXOpen::AME::FormSheetBuilder::StandardMetricSize NXOpen::AME::FormSheetBuilder::StandardMetricSize@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFormSheetStandardMetricSize
            (
                NXOpen::AME::FormSheetBuilder::StandardMetricSize standardMetricSize /** standardmetricsize */ 
            );
            /**Returns  the standard metric size of type @link NXOpen::AME::FormSheetBuilder::AnsiFormSheetStandardMetricSize NXOpen::AME::FormSheetBuilder::AnsiFormSheetStandardMetricSize@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::FormSheetBuilder::AnsiStandardMetricSize AnsiFormSheetStandardMetricSize
            (
            );
            /**Sets  the standard metric size of type @link NXOpen::AME::FormSheetBuilder::AnsiFormSheetStandardMetricSize NXOpen::AME::FormSheetBuilder::AnsiFormSheetStandardMetricSize@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetAnsiFormSheetStandardMetricSize
            (
                NXOpen::AME::FormSheetBuilder::AnsiStandardMetricSize standardMetricSize /** standardmetricsize */ 
            );
            /**Returns  the height 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: double Height
            (
            );
            /**Sets  the height 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetHeight
            (
                double height /** height */ 
            );
            /**Returns  the length 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: double Length
            (
            );
            /**Sets  the length 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetLength
            (
                double length /** length */ 
            );
            /**Returns  the name and description 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::BasicPropertiesBuilder * BasicProperties
            (
            );
            /**Returns  the standard type 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::FormSheetBuilder::StandardTypes StandardType
            (
            );
            /**Sets  the standard type 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStandardType
            (
                NXOpen::AME::FormSheetBuilder::StandardTypes actionType /** actiontype */ 
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
