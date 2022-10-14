#ifndef NXOpen_FEATURES_POINTSETBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_POINTSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PointSetBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_PointSetBuilder.hxx>
#include <NXOpen/Features_PointSetFacePercentageBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class PointSetBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        class PointSetFacePercentageBuilder;
    }
    namespace Features
    {
        class PointSetFacePercentageBuilderList;
    }
    class NXObjectList;
    class Point;
    class PointList;
    class ScCollector;
    class Section;
    class SelectFace;
    class SelectNXObject;
    namespace Features
    {
        class _PointSetBuilderBuilder;
        /**
            Represents a @link Features::PointSetBuilder Features::PointSetBuilder@endlink . This builder is used to
            create and edit Point Set features. The Point Set feature allows you to create points 
            on curves, edges or faces.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreatePointSetBuilder Features::FeatureCollection::CreatePointSetBuilder@endlink  <br> 
        Default values:
        ArcLength.RightHandSide: 1 (millimeters part), 0.01 (inches part)
        Associative: 1
        ChordalTolerance.RightHandSide: 2.54 (millimeters part), 0.1 (inches part)
        CurvePointsBy: EqualArcLength
        EndPercentage.RightHandSide: 100
        FacePointsBy: Pattern
        NumberOfPoints: 2
        NumberOfPointsInUDirection: 10
        NumberOfPointsInVDirection: 10
        PatternLimitsBy: Percentages
        PatternLimitsEndingUValue.RightHandSide: 100
        PatternLimitsEndingVValue.RightHandSide: 100
        PatternLimitsStartingUValue.RightHandSide: 0
        PatternLimitsStartingVValue.RightHandSide: 0
        Ratio.RightHandSide: 1
        SplinePointsBy: DefiningPoints
        StartPercentage.RightHandSide: 0
        */
        class NXOPENCPPEXPORT PointSetBuilder : public Features::FeatureBuilder
        {
            /** The settings for the type of Point Set feature. */
            public: enum Types
            {
                TypesCurvePoints/** Create points along curve. */,
                TypesSplinePoints/** Create points along spline. */,
                TypesFacePoints/** Create points on face */
            };

            /** The settings for the curve points definition. */
            public: enum CurvePointsType
            {
                CurvePointsTypeEqualArcLength/** Points will be created at equal arc length along curve. */,
                CurvePointsTypeEqualParameters/** Points will be created at equal parameter spacing along curve. */,
                CurvePointsTypeGeometricProgression/** Points will be created with a geometric progression along curve. */,
                CurvePointsTypeChordalTolerance/** Points will be created based on the chordal deviation of curve. */,
                CurvePointsTypeIncrementalArcLength/** A point will be created at the arc length spacing input. */,
                CurvePointsTypeSpecifiedProjectionPoints/** Points will be created at minimum distance to curve. */,
                CurvePointsTypeCurvePercentage/** A point will be created at given curve percentage. */
            };

            /** The settings for the spline points definition. */
            public: enum SplinePointsType
            {
                SplinePointsTypeDefiningPoints/** Points will be created at spline defining points. */,
                SplinePointsTypeKnots/** Points will be created at spline knot points. */,
                SplinePointsTypePoles/** Points will be created at spline pole points. */
            };

            /** The settings for the face points definition. */
            public: enum FacePointsType
            {
                FacePointsTypePattern/** Points will be created based on a defined pattern. */,
                FacePointsTypeFacePercentage/** A point will be created at given face percentages. */,
                FacePointsTypeBSurfacePoles/** Points will be created at surface poles. */
            };

            /** The settings for the pattern limit definition. */
            public: enum PatternLimitsType
            {
                PatternLimitsTypeDiagonalPoints/** The pattern limit is defined by two points. */,
                PatternLimitsTypePercentages/** The pattern limit is defined by surface U and V values. */
            };

            private: friend class  _PointSetBuilderBuilder;
            protected: PointSetBuilder();
            /**Returns  the curve points definition setting. 
                        Only used when type is 
                        JA_POINT_SET_BUILDER_types_curve_points. 
                     <br> License requirements : None */
            public: NXOpen::Features::PointSetBuilder::CurvePointsType CurvePointsBy
            (
            );
            /**Sets  the curve points definition setting. 
                        Only used when type is 
                        JA_POINT_SET_BUILDER_types_curve_points. 
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCurvePointsBy
            (
                NXOpen::Features::PointSetBuilder::CurvePointsType curvePointsBy /** curvepointsby */ 
            );
            /**Returns  the spline points definition setting. 
                        Only used when type is 
                        JA_POINT_SET_BUILDER_types_spline_points. 
                     <br> License requirements : None */
            public: NXOpen::Features::PointSetBuilder::SplinePointsType SplinePointsBy
            (
            );
            /**Sets  the spline points definition setting. 
                        Only used when type is 
                        JA_POINT_SET_BUILDER_types_spline_points. 
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSplinePointsBy
            (
                NXOpen::Features::PointSetBuilder::SplinePointsType splinePointsBy /** splinepointsby */ 
            );
            /**Returns  the face points definition setting. 
                        Only used when type is 
                        JA_POINT_SET_BUILDER_types_face_points. 
                     <br> License requirements : None */
            public: NXOpen::Features::PointSetBuilder::FacePointsType FacePointsBy
            (
            );
            /**Sets  the face points definition setting. 
                        Only used when type is 
                        JA_POINT_SET_BUILDER_types_face_points. 
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFacePointsBy
            (
                NXOpen::Features::PointSetBuilder::FacePointsType facePointsBy /** facepointsby */ 
            );
            /**Returns  the collector that is used to hold a single curve or edge definition. 
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_arc_length, 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_parameters, 
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression,
                        JA_POINT_SET_BUILDER_curve_points_type_chordal_tolerance, or
                        JA_POINT_SET_BUILDER_curve_points_type_incremental_arc_length.
                     <br> License requirements : None */
            public: NXOpen::Section * SingleCurveOrEdgeCollector
            (
            );
            /**Returns  the collector that is used to hold multiple curves or edges. 
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_specified_projection_points, or
                        JA_POINT_SET_BUILDER_curve_points_type_incremental_arc_length.
                     <br> License requirements : None */
            public: NXOpen::Section * MultipleCurveOrEdgeCollector
            (
            );
            /**Returns  the collector that is used to hold a spline.
                        Only used when type is JA_POINT_SET_BUILDER_types_spline_points.
                     <br> License requirements : None */
            public: NXOpen::ScCollector * SplineCollector
            (
            );
            /**Returns  the select object that is used to hold the face.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is JA_POINT_SET_BUILDER_face_points_type_pattern.
                     <br> License requirements : None */
            public: NXOpen::SelectFace * SingleFaceObject
            (
            );
            /**Returns  the collector that is used to hold faces.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_face_percentage, or
                        JA_POINT_SET_BUILDER_face_points_type_b_surface_poles.
                     <br> License requirements : None */
            public: NXOpen::ScCollector * MultipleFaceCollector
            (
            );
            /**Returns  the number of points that will be created along curve.
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_arc_length, 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_parameters, or
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression.
                     <br> License requirements : None */
            public: int NumberOfPoints
            (
            );
            /**Sets  the number of points that will be created along curve.
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_arc_length, 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_parameters, or
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetNumberOfPoints
            (
                int numberOfPoints /** numberofpoints */ 
            );
            /**Returns  the percentage of the curve at which to start creating points.
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_arc_length, 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_parameters, or
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression.
                     <br> License requirements : None */
            public: NXOpen::Expression * StartPercentage
            (
            );
            /**Returns  an object (curve, edge, or point) that will be used to 
                        determine an intersection with the 
                        curves/edges selected for setting the StartPercentage
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_arc_length, 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_parameters, or
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression.

                        This interface should no longer be used. Use StartPercentageSection instead.
                     <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectObjectStartPercentage
            (
            );
            /**Returns  a section containing an object (curve, edge, or point) that will be used to 
                        determine an intersection with the 
                        curves/edges selected for setting the StartPercentage
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_arc_length, 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_parameters, or
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression.
                     <br> License requirements : None */
            public: NXOpen::Section * StartPercentageSection
            (
            );
            /**Returns  the percentage of the curve at which to stop creating points.
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_arc_length, 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_parameters, or
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression.
                     <br> License requirements : None */
            public: NXOpen::Expression * EndPercentage
            (
            );
            /**Returns  an object (curve, edge, or point) that will be used to 
                        determine an intersection with the 
                        curves/edges selected for setting the EndPercentage
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_arc_length, 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_parameters, or
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression.

                        This interface should no longer be used. Use EndPercentageSection instead.
                     <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectObjectEndPercentage
            (
            );
            /**Returns  a section containing an object (curve, edge, or point) that will be used to 
                        determine an intersection with the 
                        curves/edges selected for setting the EndPercentage
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_arc_length, 
                        JA_POINT_SET_BUILDER_curve_points_type_equal_parameters, or
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression.
                     <br> License requirements : None */
            public: NXOpen::Section * EndPercentageSection
            (
            );
            /**Returns  the ratio of geometric progression.
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_geometric_progression.
                     <br> License requirements : None */
            public: NXOpen::Expression * Ratio
            (
            );
            /**Returns  the chordal tolerance used in creating points.
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_chordal_tolerance.
                     <br> License requirements : None */
            public: NXOpen::Expression * ChordalTolerance
            (
            );
            /**Returns  the arc length of the curve at which a point is to be created.
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_incremental_arc_length.
                     <br> License requirements : None */
            public: NXOpen::Expression * ArcLength
            (
            );
            /**Returns  the projection point list.
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_specified_projection_points.
                     <br> License requirements : None */
            public: NXOpen::PointList * ProjectionPointList
            (
            );
            /**Returns  the curve percentage list.
                        Only used when type is JA_POINT_SET_BUILDER_types_curve_points,
                        and when CurvePointsBy is 
                        JA_POINT_SET_BUILDER_curve_points_type_curve_percentage.
                     <br> License requirements : None */
            public: NXOpen::NXObjectList * CurvePercentageList
            (
            );
            /**Returns  the number of points to be created in the u direction.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern.
                     <br> License requirements : None */
            public: int NumberOfPointsInUDirection
            (
            );
            /**Sets  the number of points to be created in the u direction.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetNumberOfPointsInUDirection
            (
                int numberOfPointsInUDirection /** numberofpointsinudirection */ 
            );
            /**Returns  the number of points to be created in the v direction.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern.
                     <br> License requirements : None */
            public: int NumberOfPointsInVDirection
            (
            );
            /**Sets  the number of points to be created in the v direction.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetNumberOfPointsInVDirection
            (
                int numberOfPointsInVDirection /** numberofpointsinvdirection */ 
            );
            /**Returns  the pattern limits definition setting.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern.
                     <br> License requirements : None */
            public: NXOpen::Features::PointSetBuilder::PatternLimitsType PatternLimitsBy
            (
            );
            /**Sets  the pattern limits definition setting.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPatternLimitsBy
            (
                NXOpen::Features::PointSetBuilder::PatternLimitsType patternLimitsBy /** patternlimitsby */ 
            );
            /**Returns  the starting diagonal point of the pattern.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern,
                        and when PatternLimitsBy is
                        JA_POINT_SET_BUILDER_pattern_limits_type_diagonal_points.
                     <br> License requirements : None */
            public: NXOpen::Point * PatternLimitsStartPoint
            (
            );
            /**Sets  the starting diagonal point of the pattern.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern,
                        and when PatternLimitsBy is
                        JA_POINT_SET_BUILDER_pattern_limits_type_diagonal_points.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPatternLimitsStartPoint
            (
                NXOpen::Point * patternLimitsStartPoint /** patternlimitsstartpoint */ 
            );
            /**Returns  the ending diagonal point of the pattern.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern,
                        and when PatternLimitsBy is
                        JA_POINT_SET_BUILDER_pattern_limits_type_diagonal_points.
                     <br> License requirements : None */
            public: NXOpen::Point * PatternLimitsEndPoint
            (
            );
            /**Sets  the ending diagonal point of the pattern.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern,
                        and when PatternLimitsBy is
                        JA_POINT_SET_BUILDER_pattern_limits_type_diagonal_points.
                     <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetPatternLimitsEndPoint
            (
                NXOpen::Point * patternLimitsEndPoint /** patternlimitsendpoint */ 
            );
            /**Returns  the starting u value of the pattern.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern,
                        and when PatternLimitsBy is
                        JA_POINT_SET_BUILDER_pattern_limits_type_percentages.
                     <br> License requirements : None */
            public: NXOpen::Expression * PatternLimitsStartingUValue
            (
            );
            /**Returns  the ending u value of the pattern.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern,
                        and when PatternLimitsBy is
                        JA_POINT_SET_BUILDER_pattern_limits_type_percentages.
                     <br> License requirements : None */
            public: NXOpen::Expression * PatternLimitsEndingUValue
            (
            );
            /**Returns  the starting v value of the pattern.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern,
                        and when PatternLimitsBy is
                        JA_POINT_SET_BUILDER_pattern_limits_type_percentages.
                     <br> License requirements : None */
            public: NXOpen::Expression * PatternLimitsStartingVValue
            (
            );
            /**Returns  the ending v value of the pattern.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_pattern,
                        and when PatternLimitsBy is
                        JA_POINT_SET_BUILDER_pattern_limits_type_percentages.
                     <br> License requirements : None */
            public: NXOpen::Expression * PatternLimitsEndingVValue
            (
            );
            /**Returns  the face percentage list.
                        Only used when type is JA_POINT_SET_BUILDER_types_face_points,
                        and when FacePointsBy is 
                        JA_POINT_SET_BUILDER_face_points_type_face_percentage.
                     <br> License requirements : None */
            public: NXOpen::Features::PointSetFacePercentageBuilderList * FacePercentageList
            (
            );
            /** Create an entry for the face percentage list.  @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::Features::PointSetFacePercentageBuilder * CreateFacePercentageListItem
            (
            );
            /**Returns  the associative setting. true indicates a feature will be created, 
                        false indicates just points will be created  <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associative setting. true indicates a feature will be created, 
                        false indicates just points will be created  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the distance tolerance. Used in combining curves when needed.  <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance. Used in combining curves when needed.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /**Returns  the angle tolerance. Used in determining curve tangency when needed.  <br> License requirements : None */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance. Used in determining curve tangency when needed.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angletolerance */ 
            );
            /**Returns  the type setting.  <br> License requirements : None */
            public: NXOpen::Features::PointSetBuilder::Types Type
            (
            );
            /**Sets  the type setting.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Features::PointSetBuilder::Types type /** type */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif