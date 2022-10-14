#ifndef NXOpen_CAM_DRILLTHREADMILLTOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAM_DRILLTHREADMILLTOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_DrillThreadMillToolBuilder.ja
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
#include <NXOpen/CAM_DrillToolBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class DrillThreadMillToolBuilder;
    }
    namespace CAM
    {
        class DrillToolBuilder;
    }
    namespace CAM
    {
        class _DrillThreadMillToolBuilderBuilder;
        class DrillThreadMillToolBuilderImpl;
        /** Represents a drill thread mill Tool Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateDrillThreadMillToolBuilder CAM::NCGroupCollection::CreateDrillThreadMillToolBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  DrillThreadMillToolBuilder : public CAM::DrillToolBuilder
        {
            /** form type */
            public: enum ToolFormTypeTypes
            {
                ToolFormTypeTypesUnified/** Unified */,
                ToolFormTypeTypesMetric/** Metric */,
                ToolFormTypeTypesTrapezoidal/** Trapezoidal */,
                ToolFormTypeTypesAcme/** Acme */,
                ToolFormTypeTypesStubacme/** Stub Acme */,
                ToolFormTypeTypesLowenherz/** Lowenherz */,
                ToolFormTypeTypesButtress/** Buttress */,
                ToolFormTypeTypesSparkplug/** Spark Plug */,
                ToolFormTypeTypesNpt/** NPT */,
                ToolFormTypeTypesHosecoupling/** Hose Coupling */,
                ToolFormTypeTypesFirehose/** Fire Hose */,
                ToolFormTypeTypesUnj/** UNJ */,
                ToolFormTypeTypesNps/** NPS */,
                ToolFormTypeTypesBsp/** BSP */,
                ToolFormTypeTypesBstp/** BSTP */,
                ToolFormTypeTypesHelicoil/** Helicoil */,
                ToolFormTypeTypesNs/** NS */,
                ToolFormTypeTypesUserDefined/** User Defined */
            };

            private: DrillThreadMillToolBuilderImpl * m_drillthreadmilltoolbuilder_impl;
            private: friend class  _DrillThreadMillToolBuilderBuilder;
            protected: DrillThreadMillToolBuilder();
            public: ~DrillThreadMillToolBuilder();
            /**Returns  the form type  <br> License requirements : None */
            public: NXOpen::CAM::DrillThreadMillToolBuilder::ToolFormTypeTypes TlFormType
            (
            );
            /**Sets  the form type  <br> License requirements : None */
            public: void SetTlFormType
            (
                NXOpen::CAM::DrillThreadMillToolBuilder::ToolFormTypeTypes tlFormType /** tlformtype */ 
            );
            /**Returns  the Form Name  <br> License requirements : None */
            public: NXString FormName
            (
            );
            /**Sets  the Form Name  <br> License requirements : None */
            public: void SetFormName
            (
                const NXString & formName /**  the form name */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif