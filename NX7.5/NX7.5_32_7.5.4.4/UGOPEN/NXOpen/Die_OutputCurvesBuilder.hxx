#ifndef NXOpen_DIE_OUTPUTCURVESBUILDER_HXX_INCLUDED
#define NXOpen_DIE_OUTPUTCURVESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_OutputCurvesBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class OutputCurvesBuilder;
    }
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class ICurve;
    namespace Die
    {
        class _OutputCurvesBuilderBuilder;
        class OutputCurvesBuilderImpl;
        /** Represents an output curves feature builder.  <br> This is an abstract class, and cannot be created. <br> */
        class NXOPENCPPEXPORT  OutputCurvesBuilder : public Features::FeatureBuilder
        {
            /** Settings for the curve smoothing type. */
            public: enum SmoothTypes
            {
                SmoothTypesNone/** No smoothing */,
                SmoothTypesCubic/** Cubic */,
                SmoothTypesQuintic/** Quintic */
            };

            /** Settings for the trim curve type. */
            public: enum TrimCurveTypes
            {
                TrimCurveTypesTrim/** Regular trim curve. */,
                TrimCurveTypesExtended/** extended trim curve. */,
                TrimCurveTypesNone/** No trim curve. */
            };

            /** Settings for the trim curve output type. */
            public: enum TrimOutputCurveTypes
            {
                TrimOutputCurveTypesGeometric/** Geometric. */,
                TrimOutputCurveTypesCorrected/** Corrected. */,
                TrimOutputCurveTypesBoth/** Both geometric and corrected. */
            };

            /** Settings for the trim curve creation type. */
            public: enum TrimCurveCreateTypes
            {
                TrimCurveCreateTypesSection/** Section. */,
                TrimCurveCreateTypesSurface/** Surface. */
            };

            private: OutputCurvesBuilderImpl * m_outputcurvesbuilder_impl;
            private: friend class  _OutputCurvesBuilderBuilder;
            protected: OutputCurvesBuilder();
            public: ~OutputCurvesBuilder();
            /**Returns  the trim curve type.  Needs to be set before reference point  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::OutputCurvesBuilder::TrimCurveTypes TrimCurveType
            (
            );
            /**Sets  the trim curve type.  Needs to be set before reference point  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetTrimCurveType
            (
                NXOpen::Die::OutputCurvesBuilder::TrimCurveTypes trimCurveType /** trim curve type */ 
            );
            /**Returns  the reference feature - must be either a die section or form task feature  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Features::Feature * ReferenceFeature
            (
            );
            /**Sets  the reference feature - must be either a die section or form task feature  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetReferenceFeature
            (
                NXOpen::Features::Feature * referenceFeature /** reference feature */ 
            );
            /**Returns  the reference point.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Point3d ReferencePoint
            (
            );
            /**Sets  the reference point.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetReferencePoint
            (
                const NXOpen::Point3d & referencePoint /** reference point */ 
            );
            /**Returns  the first limit point.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Point3d FirstLimitPoint
            (
            );
            /**Sets  the first limit point.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetFirstLimitPoint
            (
                const NXOpen::Point3d & firstLimitPoint /** first limit point */ 
            );
            /**Returns  the last limit point.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Point3d LastLimitPoint
            (
            );
            /**Sets  the last limit point.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetLastLimitPoint
            (
                const NXOpen::Point3d & lastLimitPoint /** last limit point */ 
            );
            /**Returns  the offset distance  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: double OffsetDistance
            (
            );
            /**Sets  the offset distance  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetOffsetDistance
            (
                double offsetDistance /** each non-trim offset curve will be output by this distance */
            );
            /** Creates the output curve without a feature.  @return  output curves  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: std::vector<NXOpen::ICurve *> CreateNonAssociative
            (
            );
            /**Returns  the trim curve output type  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::OutputCurvesBuilder::TrimOutputCurveTypes TrimOutputCurveType
            (
            );
            /**Sets  the trim curve output type  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetTrimOutputCurveType
            (
                NXOpen::Die::OutputCurvesBuilder::TrimOutputCurveTypes trimCurveOutputType /** trim curve output type */ 
            );
            /**Returns  the trim curve creation type  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::OutputCurvesBuilder::TrimCurveCreateTypes TrimCurveCreateType
            (
            );
            /**Sets  the trim curve creation type  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetTrimCurveCreateType
            (
                NXOpen::Die::OutputCurvesBuilder::TrimCurveCreateTypes trimCurveType /** trim curve type */ 
            );
            /**Returns  the smooth type  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Die::OutputCurvesBuilder::SmoothTypes SmoothType
            (
            );
            /**Sets  the smooth type  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetSmoothType
            (
                NXOpen::Die::OutputCurvesBuilder::SmoothTypes smoothType /** smooth type */ 
            );
            /**Returns  the tolerance used for cubic or quintic smoothing.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: double SmoothTolerance
            (
            );
            /**Sets  the tolerance used for cubic or quintic smoothing.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetSmoothTolerance
            (
                double smoothTolerance /** smooth tolerance */ 
            );
            /**Returns  the angle tolerance.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angle tolerance */ 
            );
            /**Returns  the distance tolerance.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distance tolerance */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif