#ifndef NXOpen_SIM_SIMDEBUGBUILDER_HXX_INCLUDED
#define NXOpen_SIM_SIMDEBUGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_SimDebugBuilder.ja
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
#include <NXOpen/SIM_SimDebugBuilder.hxx>
#include <NXOpen/libnxopencpp_sim_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace SIM
    {
        class SimDebugBuilder;
    }
    class Builder;
    namespace SIM
    {
        class _SimDebugBuilderBuilder;
        class SimDebugBuilderImpl;
        /**
            Represents a @link NXOpen::SIM::SimDebugBuilder NXOpen::SIM::SimDebugBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::SIM::KinematicConfigurator::CreateSimDebugBuilder  NXOpen::SIM::KinematicConfigurator::CreateSimDebugBuilder @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_SIMEXPORT  SimDebugBuilder : public NXOpen::Builder
        {
            /** Represents the driver type */
            public: enum DriverType
            {
                DriverTypeCse/** CSE driver */,
                DriverTypeMtd/** MTD driver */
            };

            /** Represents the ui type */
            public: enum UiType
            {
                UiTypeDisplayMomEvent/** Display Mom Event */,
                UiTypeShowPartAndTipJunctions/** Show Part And Tip Junction */,
                UiTypeGenerateSpinningTools/** Generate Spinning Tools */,
                UiTypeUseHybridGougeChecker/** Use Hybrid Gouge Checker */,
                UiTypeUseMtbOldDialogs/** Use MTB Old Dialogs */,
                UiTypeUseFastTicker/** Use Fast Ticker */,
                UiTypePrintOutTraceSerialNumbers/** Print Out Trace Serial Numbers */,
                UiTypePerformanceDisplayDetail/** Performance Display Detail */,
                UiTypePerformanceDisplayTime/** Performance Display Time */,
                UiTypePerformanceIndentTime/** Performance Indent Time */,
                UiTypePerformanceDisplayData/** Performance Display Data */,
                UiTypeDctkWriteCollisionPairs/** Write Collision Pairs */
            };

            /** Represents the trace type */
            public: enum TraceType
            {
                TraceTypeButtonDown/** Trace Button Down */,
                TraceTypeVcr/** Trace Vcr */,
                TraceTypeIpw/** Trace Ipw */,
                TraceTypePerformance/** Trace Performance */,
                TraceTypeCollision/** Trace Collision */,
                TraceTypeGouge/** Trace Gouge */,
                TraceTypeHighlighting/** Trace Highlighting */,
                TraceTypeDetails/** Trace Details */,
                TraceTypePositionalIsv/** Trace Positional Isv */,
                TraceTypeSpinningNonSpinning/** Trace Spinning Nonspinning */,
                TraceTypeKinematicModel/** Trace Kinematic Model */,
                TraceTypeEvent/** Trace Event */,
                TraceTypeLineServer/** Trace Line Server */,
                TraceTypeSync/** Trace Sync */,
                TraceTypeDctkSettings/** Trace Dctk Settings*/,
                TraceTypeDctkMovements/** Trace Dctk Movements*/,
                TraceTypeDctkDisplay/** Trace Dctk Display*/,
                TraceTypeDctkCollision/** Trace Dctk Collision*/,
                TraceTypeToolPathPicking/** Trace ToolPath Picking*/
            };

            /** Represents the dump type */
            public: enum DumpType
            {
                DumpTypeNone/** Dump Nothing */,
                DumpTypeKinematicModel/** Dump Kinematic Model */,
                DumpTypeHighlighting/** Dump Highlighting */,
                DumpTypeIpw/** Dump IPW */,
                DumpTypeCollision/** Dump Collision */,
                DumpTypeOutputBuffer/** Dump Output Buffer */,
                DumpTypeTime/** Dump Time */,
                DumpTypeDetails/** Dump Details */,
                DumpTypeSynchronizeUi/** Dump Synchronize UI */,
                DumpTypeSynchronizeManagerXtp/** Dump SynchronizeManagerXtp */,
                DumpTypeEngineParams/** Dump Engine Params */,
                DumpTypeMomVariables/** Dump Mom Variables */,
                DumpTypeDebugUi/** Dump Debug UI */,
                DumpTypeSimulationSettings/** Dump Simulation Settings */,
                DumpTypeSimManager/** Dump SimManager */,
                DumpTypePathEvents/** Dump Path Events */,
                DumpTypeMachiningTimeAnalysis/** Dump Machining Time Analysis */
            };

            /** The output type */
            public: enum OutputType
            {
                OutputTypeSyslog/** Output to syslog */,
                OutputTypeListingWindow/** Output to listing window */,
                OutputTypeAutotest/** Output to autotest */,
                OutputTypeToFile/** Output to file */
            };

            /** Represents the kinematic model type */
            public: enum KinematicModelType
            {
                KinematicModelTypeMain/** Main Kinematic Model*/,
                KinematicModelTypeSimulation/** Simulation Kinematic Model*/,
                KinematicModelTypeDriver/** Driver Kinematic Model*/
            };

            /** Represents the printout tags or pointers type */
            public: enum PrintoutTagsOrPointersType
            {
                PrintoutTagsOrPointersTypeBoolean/** Boolean*/,
                PrintoutTagsOrPointersTypeValue/** Value*/,
                PrintoutTagsOrPointersTypeName/** Name*/
            };

            private: SimDebugBuilderImpl * m_simdebugbuilder_impl;
            private: friend class  _SimDebugBuilderBuilder;
            protected: SimDebugBuilder();
            public: ~SimDebugBuilder();
            /**Returns  the driver 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SIM::SimDebugBuilder::DriverType Driver
            (
            );
            /**Sets  the driver 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetDriver
            (
                NXOpen::SIM::SimDebugBuilder::DriverType type /** The driver type*/
            );
            /** Gets the debug setting  @return  The state
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetUiSetting
            (
                NXOpen::SIM::SimDebugBuilder::UiType type /** The ui type*/
            );
            /** Sets the debug setting 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetUiSetting
            (
                NXOpen::SIM::SimDebugBuilder::UiType type /** The ui type*/,
                bool state /** The state*/
            );
            /** Gets the trace  @return  The state
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetTrace
            (
                NXOpen::SIM::SimDebugBuilder::TraceType type /** The trace type*/
            );
            /**Sets the trace 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetTrace
            (
                NXOpen::SIM::SimDebugBuilder::TraceType type /** The trace type*/,
                bool state /** The state*/
            );
            /**Returns  the dump 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SIM::SimDebugBuilder::DumpType Dump
            (
            );
            /**Sets  the dump 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetDump
            (
                NXOpen::SIM::SimDebugBuilder::DumpType type /** The dump type*/
            );
            /**Returns  the dump output 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SIM::SimDebugBuilder::OutputType DumpOutput
            (
            );
            /**Sets  the dump output 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetDumpOutput
            (
                NXOpen::SIM::SimDebugBuilder::OutputType type /** The dump output type*/
            );
            /**Returns  the output filename 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: NXString DumpToFileName
            (
            );
            /**Sets  the output filename 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetDumpToFileName
            (
                const NXString & name /** the output new name */
            );
            /**Sets  the output filename 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            void SetDumpToFileName
            (
                const char * name /** the output new name */
            );
            /**Returns  the kinematic model 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SIM::SimDebugBuilder::KinematicModelType KinematicModel
            (
            );
            /**Sets  the kinematic model 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetKinematicModel
            (
                NXOpen::SIM::SimDebugBuilder::KinematicModelType type /** The kinematic model type*/
            );
            /** Show the kinematic model state 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void ShowKinematicModelState
            (
            );
            /**Returns  the printout tags type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SIM::SimDebugBuilder::PrintoutTagsOrPointersType PrintoutTags
            (
            );
            /**Sets  the printout tags type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : ug_isv_full ("Full functionality for Integrated Simulation and Verification") */
            public: void SetPrintoutTags
            (
                NXOpen::SIM::SimDebugBuilder::PrintoutTagsOrPointersType type /** The printout tags type*/
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