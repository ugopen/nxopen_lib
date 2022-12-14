#ifndef NXOpen_AME_PLCADDRESSRULESETUPBUILDER_HXX_INCLUDED
#define NXOpen_AME_PLCADDRESSRULESETUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_PlcAddressRuleSetupBuilder.ja
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
        class PlcAddressRuleSetupBuilder;
    }
    class Builder;
    namespace AME
    {
        class _PlcAddressRuleSetupBuilderBuilder;
        class PlcAddressRuleSetupBuilderImpl;
        /**   <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreatePlcAddressRuleSetupBuilder  NXOpen::AME::AMEManager::CreatePlcAddressRuleSetupBuilder @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  PlcAddressRuleSetupBuilder : public NXOpen::Builder
        {
            private: PlcAddressRuleSetupBuilderImpl * m_plcaddressrulesetupbuilder_impl;
            private: friend class  _PlcAddressRuleSetupBuilderBuilder;
            protected: PlcAddressRuleSetupBuilder();
            public: ~PlcAddressRuleSetupBuilder();
            /** Set the symbol properties
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetPlcAddressRuleSetMap
            (
                const NXString & propertyName /** propertyname */ ,
                const NXString & propertyValue /** propertyvalue */ 
            );
            /** Set the symbol properties
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetPlcAddressRuleSetMap
            (
                const char * propertyName /** propertyname */ ,
                const char * propertyValue /** propertyvalue */ 
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
