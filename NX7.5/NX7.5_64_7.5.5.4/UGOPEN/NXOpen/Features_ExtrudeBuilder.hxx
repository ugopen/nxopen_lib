#ifndef NXOpen_FEATURES_EXTRUDEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_EXTRUDEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ExtrudeBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ExtrudeBuilder;
    }
    class Direction;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class BooleanOperation;
    }
    namespace GeometricUtilities
    {
        class FeatureOffset;
    }
    namespace GeometricUtilities
    {
        class FeatureOptions;
    }
    namespace GeometricUtilities
    {
        class Limits;
    }
    namespace GeometricUtilities
    {
        class MultiDraft;
    }
    class Section;
    /** This enum represents the type of limit */
    enum ExtrudeLimitDataLimitType
    {
        ExtrudeLimitDataLimitTypeDistance/** distance */ ,
        ExtrudeLimitDataLimitTypeUntilNext/** until next */ ,
        ExtrudeLimitDataLimitTypeUntilSelected/** until selected */ ,
        ExtrudeLimitDataLimitTypeUntilSelectedExtendFace/** until selected extend face */ ,
        ExtrudeLimitDataLimitTypeThroughAll/** through all */ 
    };

    /** This enum represents the type of offset */
    enum ExtrudeOffsetDataOffsetType
    {
        ExtrudeOffsetDataOffsetTypeNone/** No offset */,
        ExtrudeOffsetDataOffsetTypeNormalOffset/** Offset with two different distances */,
        ExtrudeOffsetDataOffsetTypeSymmetricOffset/** Offset with same distance in both directions */,
        ExtrudeOffsetDataOffsetTypeSingleOffset/** Offset with single distance in one direction */
    };

    /** This enum represents the type of taper */
    enum ExtrudeTaperDataTaperType
    {
        ExtrudeTaperDataTaperTypeNone/** No taper */,
        ExtrudeTaperDataTaperTypeSimpleFromStart/** Simple taper from start edges */,
        ExtrudeTaperDataTaperTypeSimpleFromProfile/** Simple taper from profile */,
        ExtrudeTaperDataTaperTypeSymmetric/** Symmetric taper */,
        ExtrudeTaperDataTaperTypeMatchedEnds/** Matched end taper */,
        ExtrudeTaperDataTaperTypeAsymmetric/** ASymmetric taper */
    };

    namespace Features
    {
        class _ExtrudeBuilderBuilder;
        class ExtrudeBuilderImpl;
        /** Represents a extrude feature builder. It creates or edits extrude feature.
             <br> 
            This class provides methods to get the various extrude sub components.
             <br> 
             <br> 
            Following are default values and options.
             <br> 

             <br> 
            <b> Section </b> User must set it
             <br> 
             <br> 
            <b> Direction </b>  Sections default direction
             <br> 
             <br> 
            <b> Limit Type </b>
             <br> 
             <br> 
            <b> Start Limit Distance </b> 0.0/0.0   [in/mm]
             <br> 
             <br> 
            <b> End Limit Distance </b>  1.0/25.0  [in/mm]
             <br> 
             <br> 
            <b> Draft Type </b> @link  GeometricUtilities::SimpleDraft::SimpleDraftTypeNoDraft   GeometricUtilities::SimpleDraft::SimpleDraftTypeNoDraft @endlink 
             <br> 
             <br> 
            <b> Offset Type </b>  JA_EXTRUDE_OFFSET_DATA_offset_type_none 
             <br> 
             <br> 
            <b> Boolean Sign </b>  @link  Features::Feature::BooleanTypeCreate   Features::Feature::BooleanTypeCreate @endlink 
             <br> 
             <br> 
            <b> Boolean Target </b>  NULL
             <br> 
             <br> 
            <b> Allow Self-intersecting Section </b> false
             <br> 

          <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateExtrudeBuilder Features::FeatureCollection::CreateExtrudeBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ExtrudeBuilder : public Features::FeatureBuilder
        {
            private: ExtrudeBuilderImpl * m_extrudebuilder_impl;
            private: friend class  _ExtrudeBuilderBuilder;
            protected: ExtrudeBuilder();
            public: ~ExtrudeBuilder();
            /**Returns  the section
                 <br> License requirements : None */
            public: NXOpen::Section * Section
            (
            );
            /**Sets  the section
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSection
            (
                NXOpen::Section * section /** Section to be extruded This parameter may not be NULL.*/
            );
            /**Returns  the extrude direction
                 <br> License requirements : None */
            public: NXOpen::Direction * Direction
            (
            );
            /**Sets  the extrude direction
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDirection
            (
                NXOpen::Direction * direction /** Extrude direction This parameter may not be NULL.*/
            );
            /**Returns  the distance tolerance
                 <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distance tolerance */ 
            );
            /**Returns  the chaining tolerance
                 <br> License requirements : None */
            public: double ChainingTolerance
            (
            );
            /**Sets  the chaining tolerance
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetChainingTolerance
            (
                double chainingTolerance /** chaining tolerance */ 
            );
            /**Returns  the planar tolerance
                 <br> License requirements : None */
            public: double PlanarTolerance
            (
            );
            /**Sets  the planar tolerance
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPlanarTolerance
            (
                double planarTolerance /** planar tolerance */ 
            );
            /**Returns  the angle tolerance
                 <br> License requirements : None */
            public: double AngularTolerance
            (
            );
            /**Sets  the angle tolerance
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAngularTolerance
            (
                double angleTolerance /** angle tolerance */ 
            );
            /**Returns  the extrude boolean operation
                 <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BooleanOperation * BooleanOperation
            (
            );
            /**Returns  the extrude draft operation
                 <br> License requirements : None */
            public: NXOpen::GeometricUtilities::MultiDraft * Draft
            (
            );
            /**Returns  the extrude Offset operation
                 <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FeatureOffset * Offset
            (
            );
            /**Returns  the extrude limits
                 <br> License requirements : None */
            public: NXOpen::GeometricUtilities::Limits * Limits
            (
            );
            /**Returns  the feature options
                 <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FeatureOptions * FeatureOptions
            (
            );
            /** SET all the tolerances at once
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetToleranceValues
            (
                double distanceTolerance /** distance tolerance */ ,
                double chainingTolerance /** chaining tolerance */ ,
                double planarTolerance /** planar tolerance */ ,
                double angularTolerance /** angular tolerance */ 
            );
            /** SET option for supporting self-intersecting section
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void AllowSelfIntersectingSection
            (
                bool allowSelfIntersectingSection /** If true, allow self-intersecting section. */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
