#ifndef NXOpen_CAM_INSPECTIONSCANCURVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONSCANCURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionScanCurveBuilder.ja
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
#include <NXOpen/CAM_InspectionMoveBuilder.hxx>
#include <NXOpen/CAM_InspectionMethodBuilder.hxx>
#include <NXOpen/CAM_InspectionScanCurveBuilder.hxx>
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
        class InspectionScanCurveBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class InheritableIntBuilder;
    }
    namespace CAM
    {
        class InspectionMoveBuilder;
    }
    class NXObject;
    namespace CAM
    {
        class _InspectionScanCurveBuilderBuilder;
        class InspectionScanCurveBuilderImpl;
        /** Represents the builder for the CMM Inspection sub-operation Scan Curve.  <br> To create a new instance of this class, use @link CAM::InspectionMoveCollection::CreateInspectionScanCurveBuilder  CAM::InspectionMoveCollection::CreateInspectionScanCurveBuilder @endlink  <br> 
         <br>  Created in NX7.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  InspectionScanCurveBuilder : public CAM::InspectionMoveBuilder
        {
            private: InspectionScanCurveBuilderImpl * m_inspectionscancurvebuilder_impl;
            private: friend class  _InspectionScanCurveBuilderBuilder;
            protected: InspectionScanCurveBuilder();
            public: ~InspectionScanCurveBuilder();
            /**Returns  the curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * Curve
            (
            );
            /**Sets  the curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCurve
            (
                NXOpen::NXObject * curve /** curve */ 
            );
            /**Returns  the Number of Scan Points on the curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: int Nbpoints
            (
            );
            /**Sets  the Number of Scan Points on the curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNbpoints
            (
                int nbpoints /** nbpoints */ 
            );
            /**Returns  the Reverse Direction flag on the curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool Reversedirection
            (
            );
            /**Sets  the Reverse Direction flag on the curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReversedirection
            (
                bool reversedir /** reversedir */ 
            );
            /**Returns  the Start Distance of the Scan Curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double StartDistance
            (
            );
            /**Sets  the Start Distance of the Scan Curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStartDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the End Distance of the Scan Curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double EndDistance
            (
            );
            /**Sets  the End Distance of the Scan Curve 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: void SetEndDistance
            (
                double distance /** distance */ 
            );
            /**Returns  the Minimum Spacing of points along the Scan Curve 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * MinSpacing
            (
            );
            /**Returns  the Maximum Spacing of points along the Scan Curve 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * MaxSpacing
            (
            );
            /**Returns  the Curvature Increase Factor for points along the Scan Curve 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * CurvatureFactor
            (
            );
            /**Returns  the curve specification mode 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionMethodBuilder::ScanCurveModeTypes CurveMode
            (
            );
            /**Sets  the curve specification mode 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetCurveMode
            (
                NXOpen::CAM::InspectionMethodBuilder::ScanCurveModeTypes mode /** mode */ 
            );
            /**Returns  the Start Distance of the Scan Curve 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * StartDistanceBuilder
            (
            );
            /**Returns  the End Distance of the Scan Curve 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * EndDistanceBuilder
            (
            );
            /**Returns  the Start Percentage of the Scan Curve 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * StartPercentage
            (
            );
            /**Returns  the End Percentage of the Scan Curve 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * EndPercentage
            (
            );
            /**Returns  the start/end mode 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InspectionMethodBuilder::UVModeTypes StartEndMode
            (
            );
            /**Sets  the start/end mode 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStartEndMode
            (
                NXOpen::CAM::InspectionMethodBuilder::UVModeTypes startEndMode /** startendmode */ 
            );
            /**Returns  the builder for the Number of Scan Points on the curve 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * NbPointsBuilder
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