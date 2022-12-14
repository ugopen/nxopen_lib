#ifndef NXOpen_CAE_MODELANDLOADPREPROCESSTIMETOWATERFALLBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MODELANDLOADPREPROCESSTIMETOWATERFALLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelAndLoadPreProcessTimeToWaterfallBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/CAE_ModelAndLoadPreProcessOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class ModelAndLoadPreProcessTimeToWaterfallBuilder;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcessOperationBuilder;
    }
    class Expression;
    namespace CAE
    {
        class _ModelAndLoadPreProcessTimeToWaterfallBuilderBuilder;
        class ModelAndLoadPreProcessTimeToWaterfallBuilderImpl;
        /**
            Builds a @link NXOpen::CAE::ModelAndLoadPreProcessTimeToWaterfall NXOpen::CAE::ModelAndLoadPreProcessTimeToWaterfall@endlink  object which 
            represets an operation.
             <br> There is no kf creator for this.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ModelAndLoadPreProcessTimeToWaterfallBuilder : public NXOpen::CAE::ModelAndLoadPreProcessOperationBuilder
        {
            /** the frame size type enumeration */
            public: enum FrameSizeTypeEnum
            {
                FrameSizeTypeEnumTime/** time */ ,
                FrameSizeTypeEnumSamples/** samples */ 
            };

            /** the supported identifiers for the RPM selection function */
            public: enum FunctionVariableEnum
            {
                FunctionVariableEnumElementName/** element name */ ,
                FunctionVariableEnumVariableName/** variable name */ ,
                FunctionVariableEnumFirstMarkerPosition/** first marker position */ ,
                FunctionVariableEnumSecondMarkerPosition/** second marker position */ ,
                FunctionVariableEnumNode/** node */ ,
                FunctionVariableEnumSubcase/** subcase */ 
            };

            private: ModelAndLoadPreProcessTimeToWaterfallBuilderImpl * m_modelandloadpreprocesstimetowaterfallbuilder_impl;
            private: friend class  _ModelAndLoadPreProcessTimeToWaterfallBuilderBuilder;
            protected: ModelAndLoadPreProcessTimeToWaterfallBuilder();
            public: ~ModelAndLoadPreProcessTimeToWaterfallBuilder();
            /**Returns  the start value of the RPM definition 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RpmStart
            (
            );
            /**Returns  the end value of the RPM definition 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RpmEnd
            (
            );
            /**Returns  the step value of the RPM definition 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RpmStep
            (
            );
            /**Returns  the frame type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ModelAndLoadPreProcessTimeToWaterfallBuilder::FrameSizeTypeEnum FrameSizeType
            (
            );
            /**Sets  the frame type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFrameSizeType
            (
                NXOpen::CAE::ModelAndLoadPreProcessTimeToWaterfallBuilder::FrameSizeTypeEnum frameSizeType /** framesizetype */ 
            );
            /**Returns  the frame size in time 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * FrameSizeTime
            (
            );
            /**Returns  the frame size in samples 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: int FrameSizeSamples
            (
            );
            /**Sets  the frame size in samples 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFrameSizeSamples
            (
                int frameSizeSamples /** framesizesamples */ 
            );
            /** Sets the selected RPM function. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetRpmFunction
            (
                const std::vector<NXOpen::CAE::ModelAndLoadPreProcessTimeToWaterfallBuilder::FunctionVariableEnum> & functionSelectionTypes /** functionselectiontypes */ ,
                const std::vector<NXString> & functionSelectionValues /** functionselectionvalues */ 
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
