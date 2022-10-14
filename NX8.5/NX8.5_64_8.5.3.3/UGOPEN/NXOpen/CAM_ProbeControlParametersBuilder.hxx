#ifndef NXOpen_CAM_PROBECONTROLPARAMETERSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_PROBECONTROLPARAMETERSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ProbeControlParametersBuilder.ja
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
#include <NXOpen/CAM_ProbeControlParametersBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ProbeControlParametersBuilder;
    }
    namespace CAM
    {
        class _ProbeControlParametersBuilderBuilder;
        class ProbeControlParametersBuilderImpl;
        /**
            Represents a @link CAM::ProbeControlParametersBuilder CAM::ProbeControlParametersBuilder@endlink 
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ProbeControlParametersBuilder : public TaggedObject
        {
            /** the print type flag */
            public: enum PrintType
            {
                PrintTypeNone/** None */,
                PrintTypeFeature/** Increment feature */,
                PrintTypeComponent/** Increment component */
            };

            /** the output adjustment method types */
            public: enum AdjustmentTypes
            {
                AdjustmentTypesNone/** None */,
                AdjustmentTypesXy/** XY Calibration */,
                AdjustmentTypesXyz/** XY Calibration and Z */,
                AdjustmentTypesContact/** Contact Point */
            };

            private: ProbeControlParametersBuilderImpl * m_probecontrolparametersbuilder_impl;
            private: friend class  _ProbeControlParametersBuilderBuilder;
            protected: ProbeControlParametersBuilder();
            public: ~ProbeControlParametersBuilder();
            /**Returns  the print option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeControlParametersBuilder::PrintType Print
            (
            );
            /**Sets  the print option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPrint
            (
                NXOpen::CAM::ProbeControlParametersBuilder::PrintType newValue /** newvalue */ 
            );
            /**Returns  the option to output the work offset to update 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool OutputWorkOffset
            (
            );
            /**Sets  the option to output the work offset to update 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOutputWorkOffset
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the option to output the tool offset to update 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool OutputToolOffset
            (
            );
            /**Sets  the option to output the tool offset to update 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOutputToolOffset
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the option to output the percent feedback 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool OutputPercentFeedback
            (
            );
            /**Sets  the option to output the percent feedback 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOutputPercentFeedback
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the option to output the probe overtravel distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool OutputOvertravel
            (
            );
            /**Sets  the option to output the probe overtravel distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOutputOvertravel
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the option to output the experience value location 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool OutputExperience
            (
            );
            /**Sets  the option to output the experience value location 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOutputExperience
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the work offset to update 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int WorkOffset
            (
            );
            /**Sets  the work offset to update 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetWorkOffset
            (
                int workOffset /** work offset */ 
            );
            /**Returns  the tool offset to update 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int ToolOffset
            (
            );
            /**Sets  the tool offset to update 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetToolOffset
            (
                int toolOffset /** tool offset */ 
            );
            /**Returns  the percent feedback
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double PercentFeedback
            (
            );
            /**Sets  the percent feedback
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPercentFeedback
            (
                double percentFeedback /** percent feedback */ 
            );
            /**Returns  the probe overtravel distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double Overtravel
            (
            );
            /**Sets  the probe overtravel distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOvertravel
            (
                double overtravel /** overtravel */ 
            );
            /**Returns  the experience value location 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int Experience
            (
            );
            /**Sets  the experience value location 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetExperience
            (
                int experience /** experience */ 
            );
            /**Returns  the output adjustment option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ProbeControlParametersBuilder::AdjustmentTypes Adjustment
            (
            );
            /**Sets  the output adjustment option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAdjustment
            (
                NXOpen::CAM::ProbeControlParametersBuilder::AdjustmentTypes newValue /** newvalue */ 
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