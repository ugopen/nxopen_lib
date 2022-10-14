#ifndef NXOpen_CAM_NCMPLANARENGRETBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NCMPLANARENGRETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmPlanarEngRetBuilder.ja
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
        class NcmPlanarEngRetBuilder;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    class Point;
    class SmartObject;
    namespace CAM
    {
        class _NcmPlanarEngRetBuilderBuilder;
        class NcmPlanarEngRetBuilderImpl;
        /** Represents a builder for an inheritable double value in of a CAM.CAMObject 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  NcmPlanarEngRetBuilder : public TaggedObject
        {
            /** Available types for engage/retract in Planar Milling */
            public: enum EngRetTypes
            {
                EngRetTypesSameAsDefault/** Same as Default (Inherit) */,
                EngRetTypesSameAsClosed/** Same as Closed Engage (from open) */,
                EngRetTypesSameAsEngage/** Same as (Open) Engage (from retract) */,
                EngRetTypesHelical/** Helical Ramp */,
                EngRetTypesRampOnShape/** Ramp on shape */,
                EngRetTypesZigzagRamp/** ZigZag Ramp */,
                EngRetTypesLinear/** Linear */,
                EngRetTypesArc/** Arc */,
                EngRetTypesArcParallelToToolAxis/** Arc - Parallel to Tool Axis */,
                EngRetTypesArcNormalToToolAxis/** Arc - Normal to Tool Axis */,
                EngRetTypesArcNormalToPart/** Arc - Normal to Part */,
                EngRetTypesHighSpeedArc/** High Speed Arcs */,
                EngRetTypesPoints/** to-from points */,
                EngRetTypesPlungeLift/** Plunge Engage/Lift Retract */,
                EngRetTypesAlongVector/** Vector Dist */,
                EngRetTypesAngAngPlane/** Linear to plane */,
                EngRetTypesVectorPlane/** Vector to plane */,
                EngRetTypesNone/** None */,
                EngRetTypesLinearRelativeCut/** Linear relative to cut direction */
            };

            /** Available types for the Height From which engage helical/ramp/plunge
                        is measured in Planar Milling */
            public: enum MeasureHeightFrom
            {
                MeasureHeightFromCurrentLevel/** Measure from current level */,
                MeasureHeightFromPreviousLevel/** Measure from previous level */,
                MeasureHeightFromPlane/** Measure from user-defined plane */
            };

            private: NcmPlanarEngRetBuilderImpl * m_ncmplanarengretbuilder_impl;
            private: friend class  _NcmPlanarEngRetBuilderBuilder;
            protected: NcmPlanarEngRetBuilder();
            public: ~NcmPlanarEngRetBuilder();
            /**Returns  the type of engage/retract 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarEngRetBuilder::EngRetTypes EngRetType
            (
            );
            /**Sets  the type of engage/retract 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngRetType
            (
                NXOpen::CAM::NcmPlanarEngRetBuilder::EngRetTypes newValue /** the new value */
            );
            /**Returns  the height from which engage helical/ramp/plunge is measured 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmPlanarEngRetBuilder::MeasureHeightFrom HeightFrom
            (
            );
            /**Sets  the height from which engage helical/ramp/plunge is measured 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetHeightFrom
            (
                NXOpen::CAM::NcmPlanarEngRetBuilder::MeasureHeightFrom newValue /** the new value */
            );
            /**Returns  the engage/retract length builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * LengthBuilder
            (
            );
            /**Returns  the engage/retract height builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * HeightBuilder
            (
            );
            /**Returns  the engage/retract radius builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * RadiusBuilder
            (
            );
            /**Returns  the engage/retract diameter builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * DiameterBuilder
            (
            );
            /**Returns  the linear extension before arc engage/retract 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * ExtendBeforeArc
            (
            );
            /**Returns  the linear extension after arc engage/retract 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * ExtendAfterArc
            (
            );
            /**Returns  the engage/retract vector 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SmartObject * Vector
            (
            );
            /**Sets  the engage/retract vector 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetVector
            (
                NXOpen::SmartObject * vector /** the engage/retract vector */
            );
            /**Returns  the engage/retract arc angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double ArcAngle
            (
            );
            /**Sets  the engage/retract arc angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetArcAngle
            (
                double newValue /** the arc angle */
            );
            /**Returns  the engage/retract swing angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double SwingAngle
            (
            );
            /**Sets  the engage/retract swing angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSwingAngle
            (
                double newValue /** the swing angle */
            );
            /**Returns  the engage/retract ramp angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double RampAngle
            (
            );
            /**Sets  the engage/retract ramp angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRampAngle
            (
                double newValue /** the ramp angle */
            );
            /**Returns  the engage/retract min clearance builder 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * MinClearanceBuilder
            (
            );
            /**Returns  the engage/retract start at arc center 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool StartAtArcCenter
            (
            );
            /**Sets  the engage/retract start at arc center 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStartAtArcCenter
            (
                bool newValue /** the start at arc center */
            );
            /**Returns  the engage/retract plane,plane entity type covers Xform and Plane 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SmartObject * Plane
            (
            );
            /**Sets  the engage/retract plane,plane entity type covers Xform and Plane 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPlane
            (
                NXOpen::SmartObject * plane /** the engage/retract plane */
            );
            /** Gets engage/retract points 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void GetPoints
            (
                std::vector<NXOpen::Point *> & points /** Array of points */
            );
            /** Sets engage/retract points 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPoints
            (
                const std::vector<NXOpen::Point *> & points /** Array of points */
            );
            /**Returns  the engage/retract use effective distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseEffectDist
            (
            );
            /**Sets  the engage/retract use effective distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetUseEffectDist
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the engage/retract effect dist builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * EffectDistBuilder
            (
            );
            /**Returns  the engage/retract minimum ramp length builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * MinRampLengthBuilder
            (
            );
            /**Returns  the engage/retract use max width 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseMaxWidth
            (
            );
            /**Sets  the engage/retract use max width 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetUseMaxWidth
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the engage/retract max width builder (inheritable tool dep) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * MaxWidthBuilder
            (
            );
            /**Returns  the engage/retract trim 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool Trim
            (
            );
            /**Sets  the engage/retract trim 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTrim
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the flag whether to ignore blank outside trim boundaries 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool IgnoreBlankOnTrimSide
            (
            );
            /**Sets  the flag whether to ignore blank outside trim boundaries 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetIgnoreBlankOnTrimSide
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the helical ramp angle builder of Helical and Ramp on Shape type of Engages
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * HelicalRampAngleBuilder
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