#ifndef NXOpen_CAM_NCMSCENGRETBUILDER_HXX_INCLUDED
#define NXOpen_CAM_NCMSCENGRETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NcmScEngRetBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class NcmScEngRetBuilder;
    }
    namespace CAM
    {
        class InheritableToolDepBuilder;
    }
    class Plane;
    class Point;
    class SmartObject;
    namespace CAM
    {
        class _NcmScEngRetBuilderBuilder;
        class NcmScEngRetBuilderImpl;
        /** Represents a builder for an inheritable double value in of a CAM.CAMObject */
        class NXOPENCPPEXPORT  NcmScEngRetBuilder : public TaggedObject
        {
            /** Available types for engage/retract in surface contouring */
            public: enum EngRetTypes
            {
                EngRetTypesSameAsDefault/** Same as Default */,
                EngRetTypesSameAsEngage/** Same as Engage (only for retract) */,
                EngRetTypesLinear/** Linear */,
                EngRetTypesLinearAlongVector/** Linear - Along Vector */,
                EngRetTypesLinearNormalToPart/** Linear - Normal to Part */,
                EngRetTypesArcParallelToToolAxis/** Arc - Parallel to Tool Axis */,
                EngRetTypesArcNormalToToolAxis/** Arc - Normal to Tool Axis */,
                EngRetTypesArcTangentToApproach/** Arc - Tangent to Approach */,
                EngRetTypesArcNormalToPart/** Arc - Normal to Part */,
                EngRetTypesHelicalClw/** Helical Clockwise*/,
                EngRetTypesHelicalCclw/** Helical Counter Clockwise */,
                EngRetTypesPlungeLift/** Plunge Engage/Lift Retract */,
                EngRetTypesNone/** None */,
                EngRetTypesPoints/** to-from point */
            };

            /** Available types for the Height or Length from which the linear/helical/plunge
                        engage or linear/plunge retract is measured in Surface Contour Milling */
            public: enum MeasureFromTypes
            {
                MeasureFromTypesDistance/** Measure from distance */,
                MeasureFromTypesPlane/** Measure from user-defined plane */
            };

            private: NcmScEngRetBuilderImpl * m_ncmscengretbuilder_impl;
            private: friend class  _NcmScEngRetBuilderBuilder;
            protected: NcmScEngRetBuilder();
            public: ~NcmScEngRetBuilder();
            /**Returns  the type of engage/retract  <br> License requirements : None */
            public: NXOpen::CAM::NcmScEngRetBuilder::EngRetTypes EngRetType
            (
            );
            /**Sets  the type of engage/retract  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngRetType
            (
                NXOpen::CAM::NcmScEngRetBuilder::EngRetTypes newValue /** the new value */
            );
            /**Returns  the engage/retract length builder  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * LengthBuilder
            (
            );
            /**Returns  the engage/retract height builder  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * HeightBuilder
            (
            );
            /**Returns  the height or length from which engage linear/helical/plunge is measured  <br> License requirements : None */
            public: NXOpen::CAM::NcmScEngRetBuilder::MeasureFromTypes MeasureFrom
            (
            );
            /**Sets  the height or length from which engage linear/helical/plunge is measured  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMeasureFrom
            (
                NXOpen::CAM::NcmScEngRetBuilder::MeasureFromTypes newValue /** the new value */
            );
            /**Returns  the engage/retract plane  <br> License requirements : None */
            public: NXOpen::Plane * Plane
            (
            );
            /**Sets  the engage/retract plane  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPlane
            (
                NXOpen::Plane * plane /** the engage/retract plane */
            );
            /**Returns  the engage/retract radius builder  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * RadiusBuilder
            (
            );
            /**Returns  the engage/retract diameter builder  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * DiameterBuilder
            (
            );
            /**Returns  the engage/retract vector  <br> License requirements : None */
            public: NXOpen::SmartObject * Vector
            (
            );
            /**Sets  the engage/retract vector  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetVector
            (
                NXOpen::SmartObject * vector /** the engage/retract vector */
            );
            /**Returns  the engage/retract arc angle  <br> License requirements : None */
            public: double ArcAngle
            (
            );
            /**Sets  the engage/retract arc angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetArcAngle
            (
                double newValue /** the arc angle */
            );
            /**Returns  the engage/retract swing angle  <br> License requirements : None */
            public: double SwingAngle
            (
            );
            /**Sets  the engage/retract swing angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetSwingAngle
            (
                double newValue /** the swing angle */
            );
            /**Returns  the engage/retract ramp angle  <br> License requirements : None */
            public: double RampAngle
            (
            );
            /**Sets  the engage/retract ramp angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRampAngle
            (
                double newValue /** the ramp angle */
            );
            /**Returns  the engage/retract ramp angle for helical moves  <br> License requirements : None */
            public: double HelicalRampAngle
            (
            );
            /**Sets  the engage/retract ramp angle for helical moves  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetHelicalRampAngle
            (
                double newValue /** the ramp angle */
            );
            /**Returns  the engage/retract linear extension builder  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * LinearExtensionBuilder
            (
            );
            /** Gets engage/retract points  <br> License requirements : None */
            public: void GetPoints
            (
                std::vector<NXOpen::Point *> & points /** Array of points */
            );
            /** Sets engage/retract points  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPoints
            (
                const std::vector<NXOpen::Point *> & points /** Array of points */
            );
            /**Returns  the engage/retract use effective distance  <br> License requirements : None */
            public: bool UseEffectDist
            (
            );
            /**Sets  the engage/retract use effective distance  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetUseEffectDist
            (
                bool newValue /** newvalue */ 
            );
            /**Returns  the engage/retract effect dist builder (inheritable tool dep)  <br> License requirements : None */
            public: NXOpen::CAM::InheritableToolDepBuilder * EffectDistBuilder
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif