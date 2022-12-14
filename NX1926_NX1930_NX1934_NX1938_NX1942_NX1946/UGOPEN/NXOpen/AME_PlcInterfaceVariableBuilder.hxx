#ifndef NXOpen_AME_PLCINTERFACEVARIABLEBUILDER_HXX_INCLUDED
#define NXOpen_AME_PLCINTERFACEVARIABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_PlcInterfaceVariableBuilder.ja
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
#include <NXOpen/AME_DataTypeBuilder.hxx>
#include <NXOpen/AME_BulkEngineeringObjectBuilder.hxx>
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
        class PlcInterfaceVariableBuilder;
    }
    namespace AME
    {
        class BulkEngineeringObjectBuilder;
    }
    namespace AME
    {
        class DataTypeBuilder;
    }
    namespace AME
    {
        class _PlcInterfaceVariableBuilderBuilder;
        class PlcInterfaceVariableBuilderImpl;
        /** PlcInterfaceVariableBuilder class will be used for (bulk) variable object creation and editing  <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreatePlcInterfaceVariableBuilder  NXOpen::AME::AMEManager::CreatePlcInterfaceVariableBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AspectPlacement </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        ShowInAutomation </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        ShowInFunction </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        ShowInLocation </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        ShowInProduct </term> <description> 
         
        false </description> </item> 

        </list> 

         <br>  Created in NX12.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  PlcInterfaceVariableBuilder : public NXOpen::AME::BulkEngineeringObjectBuilder
        {
            private: PlcInterfaceVariableBuilderImpl * m_plcinterfacevariablebuilder_impl;
            private: friend class  _PlcInterfaceVariableBuilderBuilder;
            protected: PlcInterfaceVariableBuilder();
            public: ~PlcInterfaceVariableBuilder();
            /**Returns  the object data type builder
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::DataTypeBuilder * DataTypeComp
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
