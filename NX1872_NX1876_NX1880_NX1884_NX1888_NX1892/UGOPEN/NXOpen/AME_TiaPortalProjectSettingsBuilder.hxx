#ifndef NXOpen_AME_TIAPORTALPROJECTSETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_AME_TIAPORTALPROJECTSETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_TiaPortalProjectSettingsBuilder.ja
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
        class TiaPortalProjectSettingsBuilder;
    }
    class Builder;
    namespace AME
    {
        class _TiaPortalProjectSettingsBuilderBuilder;
        class TiaPortalProjectSettingsBuilderImpl;
        /** TiaPortalProjectSettingsBuilder  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateTiaPortalProjectSettingsBuilder  NXOpen::AME::AMEManager::CreateTiaPortalProjectSettingsBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  TiaPortalProjectSettingsBuilder : public NXOpen::Builder
        {
            /** represents the TIA Portal Version type */
            public: enum TiaPortalVersionType
            {
                TiaPortalVersionTypeV14Sp1/** v14sp1 */ ,
                TiaPortalVersionTypeV15/** v15 */ ,
                TiaPortalVersionTypeV151/** v151 */ 
            };

            private: TiaPortalProjectSettingsBuilderImpl * m_tiaportalprojectsettingsbuilder_impl;
            private: friend class  _TiaPortalProjectSettingsBuilderBuilder;
            protected: TiaPortalProjectSettingsBuilder();
            public: ~TiaPortalProjectSettingsBuilder();
            /**Returns  the current tia portal version 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::TiaPortalProjectSettingsBuilder::TiaPortalVersionType TiaPortalVersion
            (
            );
            /**Sets  the current tia portal version 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetTiaPortalVersion
            (
                NXOpen::AME::TiaPortalProjectSettingsBuilder::TiaPortalVersionType version /** version */ 
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