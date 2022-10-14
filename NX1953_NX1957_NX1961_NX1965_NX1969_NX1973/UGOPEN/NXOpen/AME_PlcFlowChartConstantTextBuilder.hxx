#ifndef NXOpen_AME_PLCFLOWCHARTCONSTANTTEXTBUILDER_HXX_INCLUDED
#define NXOpen_AME_PLCFLOWCHARTCONSTANTTEXTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_PlcFlowChartConstantTextBuilder.ja
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
        class PlcFlowChartConstantTextBuilder;
    }
    class Builder;
    namespace AME
    {
        class _PlcFlowChartConstantTextBuilderBuilder;
        class PlcFlowChartConstantTextBuilderImpl;
        /** JA class for the constant text rule <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreatePlcStateChartItemValueBuilder  NXOpen::AME::AMEManager::CreatePlcStateChartItemValueBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  PlcFlowChartConstantTextBuilder : public NXOpen::Builder
        {
            private: PlcFlowChartConstantTextBuilderImpl * m_plcflowchartconstanttextbuilder_impl;
            private: friend class  _PlcFlowChartConstantTextBuilderBuilder;
            protected: PlcFlowChartConstantTextBuilder();
            public: ~PlcFlowChartConstantTextBuilder();
            /**Returns  the constanttext name 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString ConstantText
            (
            );
            /**Sets  the constanttext name 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetConstantText
            (
                const NXString & resultText /** resulttext */ 
            );
            /**Sets  the constanttext name 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetConstantText
            (
                const char * resultText /** resulttext */ 
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