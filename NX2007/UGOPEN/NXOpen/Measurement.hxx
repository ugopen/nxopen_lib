#ifndef NXOpen_MEASUREMENT_HXX_INCLUDED
#define NXOpen_MEASUREMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Measurement.ja
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
#include <NXOpen/GeometryTypes.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class Measurement;
    class Session;
    class Body;
    class Curve;
    class Direction;
    class DisplayableObject;
    class Edge;
    class Face;
    class ICurve;
    class IReferenceAxis;
    class NXObject;
    class Point;
    namespace Routing
    {
        class ISegment;
    }
    class ScCollector;
    class MeasurementImpl;
    /**
    Provides methods for calculating and displaying the measurement information.
     <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
     <br>  Created in NX3.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  Measurement
    {
        /** 
            Describes type of the 'Deviation Checking' report. 
            */
        public: enum DeviationReportType
        {
            DeviationReportTypeNoDeviation/** No Deviation*/,
            DeviationReportTypeAllDeviation/** All Deviation*/,
            DeviationReportTypeMaximumDistance/** Maximum Distance*/,
            DeviationReportTypeMinimumDistance/** Minimum Distance*/,
            DeviationReportTypeMaximumAngle/** Maximum Angle*/,
            DeviationReportTypeMinimumAngle/** Minimum Angle*/
        };

        /** Indicates alternate angle result */
        public: enum AlternateAngle
        {
            AlternateAngleInner/** Inner angle*/,
            AlternateAngleOuter/** Outer angle*/,
            AlternateAngleSupplimental/** Supplimental angle*/
        };

        /** Indicates alternate distance result */
        public: enum AlternateDistance
        {
            AlternateDistanceMinimum/** Minimum*/,
            AlternateDistanceMaximum/** Maximum*/,
            AlternateDistanceMaximumCenterToEdge/** Maximum Center to Edge*/,
            AlternateDistanceMaximumEdgeToCenter/** Maximum Edge to Centere*/,
            AlternateDistanceCenterToCenter/** Center to Center*/,
            AlternateDistanceThickness/** Thickness*/
        };

        /** Indicates alternate face property result */
        public: enum AlternateFace
        {
            AlternateFaceRadius/** radius */,
            AlternateFaceDiameter/** diameter */
        };

        /** Indicates quick measure types that maps to UM_MeasurementTypes */
        public: enum QuickMeasureType
        {
            QuickMeasureTypeDistance/** distance */ ,
            QuickMeasureTypeCurve/** curve */ ,
            QuickMeasureTypeFace/** face */ ,
            QuickMeasureTypeProjectedDistance/** projected distance */ ,
            QuickMeasureTypeAngleThreePoints/** angle three points */ ,
            QuickMeasureTypeCombinedFace/** combined face */ ,
            QuickMeasureTypeCombinedLength/** combined length */ ,
            QuickMeasureTypeCombinedBody/** combined body */ ,
            QuickMeasureTypeAngle/** angle */ ,
            QuickMeasureTypeBody/** body */ ,
            QuickMeasureTypePoint/** point */ ,
            QuickMeasureTypeArcLengthTwoPoints/** arc length two points */ ,
            QuickMeasureTypeEulerAngle/** euler angle */ ,
            QuickMeasureTypeBoundingBox/** bounding box */ ,
            QuickMeasureTypeSurfaceCenterLine/** surface center line */ ,
            QuickMeasureTypePolarAngle/** polar angle */ ,
            QuickMeasureTypePolarArea/** polar area */ ,
            QuickMeasureTypePolarRadius/** polar radius */ ,
            QuickMeasureTypeExtremePoint/** extreme point */ ,
            QuickMeasureTypeLast/** last */ 
        };

        /** Indicates value type for quick measure result */
        public: enum QuickMeasureValueType
        {
            QuickMeasureValueTypeLength/** length */,
            QuickMeasureValueTypeDistance/** distance */,
            QuickMeasureValueTypeArea/** area */,
            QuickMeasureValueTypeVolume/** volume */,
            QuickMeasureValueTypeMass/** mass */,
            QuickMeasureValueTypeInnerAngle/** inner angle */,
            QuickMeasureValueTypeOuterAngle/** outer angle */,
            QuickMeasureValueTypeRadius/** radius */,
            QuickMeasureValueTypeDiameter/** diameter */,
            QuickMeasureValueTypeUndefined/** undefined */
        };

        private: MeasurementImpl * m_measurement_impl;
        private: NXOpen::Session* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit Measurement(NXOpen::Session *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~Measurement();
        /** 
            Calculates and displays 'Total Arc Length' of all the selected objects.
             <br> Features.SewBuilder.Type of allowed input objects  are - @link NXOpen::Edge NXOpen::Edge@endlink ,@link NXOpen::Line NXOpen::Line@endlink ,@link NXOpen::Arc NXOpen::Arc@endlink ,@link NXOpen::Spline NXOpen::Spline@endlink ,and @link NXOpen::Curve NXOpen::Curve@endlink   <br> 
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayArcLength
        (
            const std::vector<NXOpen::DisplayableObject *> & selectedObjects /** Array of objects for which length to be calculated */
        );
        /** 
            Calculates and returns 'Total Arc Length' of all the selected objects.
             <br> Features.SewBuilder.Type of allowed input objects  are - @link NXOpen::Edge NXOpen::Edge@endlink ,@link NXOpen::Line NXOpen::Line@endlink ,@link NXOpen::Arc NXOpen::Arc@endlink ,@link NXOpen::Spline NXOpen::Spline@endlink ,and @link NXOpen::Curve NXOpen::Curve@endlink   <br> 
             @return  Total Arc Length 
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double GetArcLength
        (
            const std::vector<NXOpen::DisplayableObject *> & selectedObjects /** Array of objects for which length to be calculated */
        );
        /** 
            Calculates and displays 'Minimum Distance " between objects.
            Start points are NOT specified for any of the objects.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Curve, Edge, Face, Body, Plane, or Csys etc. <br> 
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayMinimumDistance
        (
            NXOpen::DisplayableObject * object1 /** First object */,
            NXOpen::DisplayableObject * object2 /** Second object*/,
            NXOpen::Point3d* closePoint1 /** Close point on first object */,
            NXOpen::Point3d* closePoint2 /** Close point on second object */
        );
        /** 
            Calculates and displays 'Minimum Distance' between objects.
            Start points are specified for both the objects. If any of object is Point,Pass NULL to the object
            and pass a point co-ordinates as a start point.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Point, Curve, Edge, Face, Body, Plane, or Csys etc. <br> 
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayMinimumDistance
        (
            NXOpen::NXObject * object1 /** First object */,
            const NXOpen::Point3d & startPointForObject1 /**Start point for first object */,
            NXOpen::NXObject * object2 /** Second object */,
            const NXOpen::Point3d & startPointForObject2 /**Start point for second object */,
            NXOpen::Point3d* closePoint1 /** Close point on first object */,
            NXOpen::Point3d* closePoint2 /** Close point on second object */
        );
        /** 
            Calculates and displays 'Minimum Distance' between objects.
            Start points are specified only for object1.If any of object is Point,Pass NULL to the object1
            and pass a point co-ordinates as a start_point_for_object_1.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Point, Curve, Edge, Face, Body, Plane, or Csys etc. <br> 
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayMinimumDistance
        (
            NXOpen::NXObject * object1 /** First object */,
            const NXOpen::Point3d & startPointForObject1 /**Start point for first object */,
            NXOpen::NXObject * object2 /** Second object */,
            NXOpen::Point3d* closePoint1 /** Close point on first object */,
            NXOpen::Point3d* closePoint2 /** Close point on second object */
        );
        /** 
            Calculates and displays 'Minimum Distance' between objects.
            Start points are specified only for object2.If any of object is Point,Pass NULL to the object2
            and pass a point co-ordinates as a start_point_for_object_2.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Point, Curve, Edge, Face, Body, Plane, or Csys etc. <br> 
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayMinimumDistance
        (
            NXOpen::NXObject * object1 /** First object */,
            NXOpen::NXObject * object2 /** Second object */,
            const NXOpen::Point3d & startPointForObject2 /**Start point for second object */,
            NXOpen::Point3d* closePoint1 /** Close point on first object */,
            NXOpen::Point3d* closePoint2 /** Close point on second object */
        );
        /** 
            Calculates and returns 'Minimum Distance " between objects.
            Start points are NOT specified for any of the objects.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Curve, Edge, Face, Body, Plane, or Csys etc. <br> 
             @return  minimum distance between two objects
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double GetMinimumDistance
        (
            NXOpen::NXObject * object1 /** First object */,
            NXOpen::NXObject * object2 /** Second object */,
            NXOpen::Point3d* closePoint1 /** Close point on first object */,
            NXOpen::Point3d* closePoint2 /** Close point on second object */,
            double* accuracy /**Accuracy of calculation */
        );
        /** 
            Calculates and returns 'Minimum Distance " between objects.
            Start points are specified for both the objects. 
            If any of object is Point,Pass NULL to the object and pass a point co-ordinates as a start point.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Point, Curve, Edge, Face, Body, Plane, or Csys etc. <br> 
             @return  minimum distance between two objects
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double GetMinimumDistance
        (
            NXOpen::NXObject * object1 /** First object */,
            const NXOpen::Point3d & startPointForObject1 /**Start point for first object */,
            NXOpen::NXObject * object2 /** Second object */,
            const NXOpen::Point3d & startPointForObject2 /**Start point for second object */,
            NXOpen::Point3d* closePoint1 /** Close point on first object */,
            NXOpen::Point3d* closePoint2 /** Close point on second object */,
            double* accuracy /**Accuracy of calculation */
        );
        /** 
            Calculates and returns 'Minimum Distance " between objects.
            Start points are specified only for first object.
            If any of object is Point,Pass NULL to the object1 and pass a point co-ordinates as a start_point_for_object_1.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Point, Curve, Edge, Face, Body, Plane, or Csys etc. <br> 
             @return  minimum distance between two objects
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double GetMinimumDistance
        (
            NXOpen::NXObject * object1 /** First object */,
            const NXOpen::Point3d & startPointForObject1 /**Start point for first object */,
            NXOpen::NXObject * object2 /** Second object */,
            NXOpen::Point3d* closePoint1 /** Close point on first object */,
            NXOpen::Point3d* closePoint2 /** Close point on second object */,
            double* accuracy /**Accuracy of calculation */
        );
        /** 
            Calculates and returns 'Minimum Distance " between objects.
            Start points are specified only for second object.
            If any of object is Point,Pass NULL to the object2 and pass a point co-ordinates as a start_point_for_object_2.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Point, Curve, Edge, Face, Body, Plane, or Csys etc. <br> 
             @return  Minimum distance between two objects
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double GetMinimumDistance
        (
            NXOpen::NXObject * object1 /** First object */,
            NXOpen::NXObject * object2 /** Second object */,
            const NXOpen::Point3d & startPointForObject2 /**Start point for second object */,
            NXOpen::Point3d* closePoint1 /** Close point on first object */,
            NXOpen::Point3d* closePoint2 /** Close point on second object */,
            double* accuracy /**Accuracy of calculation */
        );
        /** 
            Calculates and displays 'Angle' between objects.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Edge, Face, Body, Curve, Direction or Feature etc. <br> 
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayAngle
        (
            NXOpen::NXObject * object1 /**First object */,
            const NXOpen::Point3d & position1 /** Point position on first object*/,
            NXOpen::NXObject * object2 /**Second object*/,
            const NXOpen::Point3d & position2 /** Point position on second object*/
        );
        /** 
            Calculates and returns 'True Angle' between objects.
             <br> Features.SewBuilder.Type of allowed input objects  are -  Edge, Face, Body, Curve, Direction or Feature etc. <br> 
             @return  Angle between object1 and object2
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: double GetAngle
        (
            NXOpen::NXObject * object1 /**First object */,
            const NXOpen::Point3d & position1 /** Point position on first object*/,
            NXOpen::NXObject * object2 /**Second object*/,
            const NXOpen::Point3d & position2 /** Point position on second object*/
        );
        /** 
            Checks deviations between curves (curve to curve),and displays the report.
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayDeviationChecking
        (
            NXOpen::ICurve * curve1 /** Curve used for deviation checking */,
            NXOpen::ICurve * curve2 /** Curve used for deviation checking */,
            int numOfCheckPoints /** Number of equally spaced sample check points */,
            double distanceTolerance /** Distance Tolerance */,
            double angularTolerance /** Angle Tolerance */,
            NXOpen::Measurement::DeviationReportType reportType /** Type of the report */
        );
        /** 
            Checks deviations between a curve and a face (curve to face), and displays the report.
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayDeviationChecking
        (
            NXOpen::Curve * curve1 /** Curve used for deviation checking */,
            NXOpen::Face * face2 /** Face used for deviation checking */,
            int numOfCheckPoints /** Number of equally spaced sample check points*/,
            double distanceTolerance /** Distance Tolerance */,
            double angularTolerance /** Angle Tolerance */,
            NXOpen::Measurement::DeviationReportType reportType /** Type of the report */
        );
        /** 
            Checks deviations between a edge and a face (edge to face), and displays the report.
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayDeviationChecking
        (
            NXOpen::Face * face1 /** Face on which edge1 lies */,
            NXOpen::Edge * edge1 /** Edge used for deviation checking */,
            NXOpen::Face * face2 /** Face used for deviation checking */,
            int numOfCheckPoints /** Number of equally spaced sample check points */,
            double distanceTolerance /** Distance Tolerance */,
            double angularTolerance /** Angle Tolerance */,
            NXOpen::Measurement::DeviationReportType reportType /** Type of the report */
        );
        /** 
            Checks deviations between faces (face to face), and displays the report.
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayDeviationChecking
        (
            NXOpen::Face * face1 /** First face used for deviation checking */,
            NXOpen::Face * face2 /** Second face used for deviation checking */,
            int numOfCheckPointsU /** Number of equally spaced sample check points in u direction */,
            int numOfCheckPointsV /** Number of equally spaced sample check points in v direction */,
            double distanceTolerance /** Distance Tolerance */,
            double angularTolerance /** Angle Tolerance */,
            NXOpen::Measurement::DeviationReportType reportType /** Type of the report */
        );
        /** 
            Checks deviations between edges (edge to edge), and displays the report.
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX3.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayDeviationChecking
        (
            NXOpen::Face * face1 /** Face on which edge1 lies */,
            NXOpen::Edge * edge1 /** First edge used for deviation checking */,
            NXOpen::Face * face2 /** Face on which edge2 lies */,
            NXOpen::Edge * edge2 /** Second edge used for deviation checking */,
            int numOfCheckPoints /** Number of equally spaced sample check points */,
            double distanceTolerance /** Distance Tolerance */,
            double angularTolerance /** Angle Tolerance */,
            NXOpen::Measurement::DeviationReportType reportType /** Type of the report */
        );
        /** 
            Calculates and displays the arc length between two points on curves.  The points may be
            on a single curve or a set of connected curves.
             <br> Features.SewBuilder.Type of allowed input objects is @link NXOpen::Point NXOpen::Point@endlink  <br> 
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayArcLengthBetweenPoints
        (
            NXOpen::Point * point1 /** First point on curve */,
            NXOpen::Point * point2 /** Second point on curve */
        );
        /** 
            Calculates and returns the arc length between two points on curves.  The points may be
            on a single curve or a set of connected curves.  Also returns the curves that is the
            shortest path between the two points.
             <br> NXOpen.Features.SewBuilder.Type of allowed input objects is @link NXOpen::Point NXOpen::Point@endlink  <br> 
            
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void GetArcLengthBetweenPoints
        (
            NXOpen::Point * point1 /** First point on curve */,
            NXOpen::Point * point2 /** Second point on curve */,
            double* length /** Arc length between the two points*/,
            std::vector<NXOpen::Curve *> & curves /** The curves of the shortest path */
        );
        /** 
            Calculates and displays the Routing path length.  If the path is disconnected, not all of
            the @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink s can be arranged end to end, the length
            returned is the sum of the lengths of the segments.
             <br> NXOpen.Features.SewBuilder.Type of allowed input objects is @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink  <br> 
             <br> In Interactive mode, output will be displayed in the listing window <br> 
             <br> In Batch mode, output will be displayed to the standard output (stdout) <br> 
            
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void DisplayRoutingPathLength
        (
            const std::vector<NXOpen::Routing::ISegment *> & selectedObjects /** Array of @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink s for which length is calculated */,
            std::vector<NXOpen::Routing::ISegment *> & usedObjects /** Array of USED @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink s for which length is calculated */
        );
        /** 
            Calculates and returns the Routing path length.  If the path is disconnected, not all of
            the @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink s can be arranged end to end, the length
            returned is the sum of the lengths of the segments.
             <br> NXOpen.Features.SewBuilder.Type of allowed input objects is @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink  <br> 
             @return  Sum of the individual lengths 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: double GetRoutingPathLength
        (
            const std::vector<NXOpen::NXObject *> & selectedObjects /** Array of @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink s and @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink s for which length is calculated */,
            std::vector<NXOpen::NXObject *> & usedObjects /** The routing objects used in the path length computation */,
            std::vector<double> & individualLengths /** individuallengths */ 
        );
        /** 
            Calculates and returns 'Minimum Orthogonal Distance' between input point and face or edge.
             @return  Minimum orthogonal distance between input point and face or edge
         <br>  Created in NX10.0.3.  <br>  
         <br> License requirements : None */
        public: double GetMinimumOrthogonalDistance
        (
            NXOpen::DisplayableObject * object1 /**  input point */,
            NXOpen::DisplayableObject * object2 /**  face or edge */,
            NXOpen::Point3d* closestOrthogonalPoint /** Closest orthogonal point on face or edge */
        );
        /** Get qualifier for angle.
            
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void GetAngleQualifier
        (
            NXOpen::DisplayableObject * proto /** proto */ ,
            bool requireExact /** exact */,
            const std::vector<double> & seed /** seed */ ,
            bool flip /** flip opion */
        );
        /** Get angle between two entities and ankle points for angle dimension.
             <br> Features.SewBuilder.Types of allowed input objects include - Line, linear edge, Face,
            Datum Plane, Datum Axis. <br> 
             <br> The end point qualifier is used for lines and linear edges to determine
            the direction of the vector along the line. The returned value is in base part units. <br> 
             @return  angle between two objects 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: double GetAngle
        (
            NXOpen::Measurement::AlternateAngle alternateSolution /** selects inner or outer arc, supplimental angle, 0 - inner */,
            bool requireExact /** determines the type of geometry to use */,
            NXOpen::DisplayableObject * object1 /** First object */,
            NXOpen::DisplayableObject * object2 /** Second object */,
            NXOpen::Point3d* pt1 /** ankle point for angle dimension */,
            NXOpen::Point3d* pt2 /** ankle point for angle dimension */,
            NXOpen::Point3d* pt3 /** ankle point for angle dimension */,
            bool* isApproximate /** indicate if the result value is approximate */
        );
        /** Get distance between set of entities and also returns the ankle points for distance dimension.
             <br> NXOpen.Features.SewBuilder.Types of allowed input objects include - Point, Curve, Edge, Face, Body, 
            Datum Plane, Datum Axis and Facet Body. The returned value is in base part units. <br> 
             @return  distance between two set objects 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: double GetDistance
        (
            NXOpen::Measurement::AlternateDistance alternateSolution /** chooses the algorithm type such as min max */,
            bool requireExact /** determines the type of geometry to use */,
            const std::vector<NXOpen::DisplayableObject *> & objects1 /** First set of objects */,
            const std::vector<NXOpen::DisplayableObject *> & objects2 /** Second set of objects */,
            NXOpen::Point3d* pt1 /** ankle point for distance dimension */,
            NXOpen::Point3d* pt2 /** ankle point for distance dimension */,
            bool* isApproximate /** indicate if the result value is approximate */
        );
        /** 
            Calculates and returns face properties for a set of faces. The returned value in radiusDiameter is controlled by the inputs alternateSolution.
            The returned value is in base part units.
            
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: void GetFaceProperties
        (
            const std::vector<NXOpen::Face *> & faces /** Set of faces  */,
            double accuracy /** accuracy      */,
            NXOpen::Measurement::AlternateFace alternateSolution /** alternate solutions: radius or diameter */,
            bool requireExact /** determines the type of geometry to use */,
            double* area /** area of faces */,
            double* perimeter /** perimeter of faces */,
            double* radiusDiameter /** radius or diameter for circular faces */,
            NXOpen::Point3d* cog /** center of gravity */,
            double* minRadiusOfCurvature /** minimum radius of curvature */,
            double* areaErrorEstimate /** estimated error */,
            NXOpen::Point3d* anchorPoint /** ankle point for annotation leader */,
            bool* isApproximate /** indicate if the result value is approximate */
        );
        /** 
            Calculates and returns body properties for a set of bodys. Returned coordinates - centroid and part unit centroid are in work part coordinates.
            The returned value is in base part units.
            
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void GetBodyProperties
        (
            const std::vector<NXOpen::Body *> & bodys /** Set of bodys  */,
            double accuracy /** accuracy */,
            bool useWCS /** determines WCS to use */,
            std::vector<double> & massProps /** mass properties */,
            double* weight /** weight */,
            NXOpen::Point3d* centroid /** point of centroid */,
            std::vector<double> & centroidUnit /** unit of centroid */,
            double* density /** density */,
            std::vector<double> & axis /** axis */
        );
        /** 
            Calculates and returns projected distance for a set of object. Returned projected distance
            
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void GetProjectedDistanceProperties
        (
            const std::vector<NXOpen::NXObject *> & selList1 /** Set of list1  */,
            const std::vector<NXOpen::NXObject *> & selList2 /** Set of list2  */,
            NXOpen::NXObject * vectorTag /** tag of vector  */,
            NXOpen::NXObject * targetUnit /** target unit  */,
            bool requireExact /** requireExact */,
            int alternateSolution /** alternateSolution */,
            double* distance /** projected distance */,
            std::vector<NXOpen::Point3d> & points /** points */,
            bool* isApproximate /** isApproximate */
        );
        /** 
            Calculates and returns euler angles for a set of object. Returned theta1 ,theta2 and theta3
            
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void GetEulerAnglesProperties
        (
            NXOpen::NXObject * csys1Tag /** csys1 Tag  */,
            NXOpen::NXObject * csys2Tag /** csys2 Tag  */,
            int alternateSolution /** alternateSolution */,
            NXOpen::NXObject * targetUnit /** target unit  */,
            double* theta1 /** theta1 */,
            double* theta2 /** theta2 */,
            double* theta3 /** theta3 */
        );
        /** 
            Calculates and returns arc/curve  for a set of object. Returned arc length ,curve end and curve min radius
            
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void GetArcAndCurveProperties
        (
            const std::vector<NXOpen::NXObject *> & selList /** Set of list1  */,
            NXOpen::NXObject * targetUnit /** target unit  */,
            bool requireExact /** requireExact */,
            bool* isApproximate /** isApproximate */,
            double* arcLength /** arc Length */,
            double* radius /** radius */,
            double* diameter /** diameter */,
            double* minRadiusOfCurvature /** minimum radius of curvature  */,
            NXOpen::Point3d* startPoint /** start point */,
            NXOpen::Point3d* endPoint /** end point */,
            NXOpen::Point3d* arcCenter /** arc center */
        );
        /** 
            Calculates and returns extreme angle  for a set of object. Returned angle,pts adn axis
            
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void GetPolarAngleProperties
        (
            NXOpen::ScCollector * collector /** collector  */,
            NXOpen::Point * center /** center  */,
            NXOpen::IReferenceAxis * vector /** vector  */,
            bool minAngle /** min angle */,
            NXOpen::NXObject * targetUnit /** target unit  */,
            double* angle /** angle */,
            NXOpen::Point3d* p1 /** point1 */,
            NXOpen::Point3d* p2 /** point2 */,
            NXOpen::Point3d* p3 /** point3 */,
            NXOpen::Point3d* axis /** axis */
        );
        /** 
            Calculates and returns extreme area  for a set of object. Returned radius,pts adn axis
             @return  radius 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: double GetPolarAreaProperties
        (
            NXOpen::ScCollector * collector /** collector  */,
            NXOpen::NXObject * targetUnit /** target unit  */,
            NXOpen::Point3d* p1 /** point1 */,
            NXOpen::Point3d* p2 /** point2 */,
            NXOpen::Point3d* axis /** axis */
        );
        /** 
            Calculates and returns extreme radius for a set of object. Returned radius,pts adn axis
            
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void GetPolarRadiusProperties
        (
            NXOpen::ScCollector * collector /** collector  */,
            NXOpen::Point * center /** center  */,
            bool minDist /** min distance */,
            NXOpen::NXObject * targetUnit /** target unit  */,
            double* radius /** radius */,
            NXOpen::Point3d* p1 /** point1 */,
            NXOpen::Point3d* p2 /** point2 */,
            std::vector<double> & axis /** axis */
        );
        /** 
            Calculates and returns extreme points for a set of object. Returned extreme point details. The returned value is in base part units.
             @return  point 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Point3d GetExtremePointProperties
        (
            NXOpen::ScCollector * collector /** collector  */,
            const std::vector<NXOpen::Direction *> & vectors /** Set of vectors  */
        );
        /** 
            Calculates and returns points data. Returned point. The returned value is in base part units.
            
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void GetPointProperties
        (
            NXOpen::Point * point /** point  */,
            NXOpen::NXObject * csys /** csys  */,
            std::vector<NXOpen::Point3d> & coords /** point coordinate and display coordinate */
        );
        /** 
            Calculates and returns centerline. Returned points and length
             @return  length 
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: double GetCenterlineProperties
        (
            const std::vector<NXOpen::NXObject *> & selList /** Set of list  */,
            NXOpen::NXObject * targetUnit /** target unit  */,
            std::vector<NXOpen::NXObject *> & pvUGCurves /** pvUGCurves */,
            NXOpen::Point3d* startPoint /** start point */,
            NXOpen::Point3d* endPoint /** end point */
        );
        /** 
            Calculates and returns bounding box. Returned points and Volume. The returned value is in base part units.
            
         <br>  Created in NX2007.0.0.  <br>  
         <br> License requirements : None */
        public: void GetBoundingBoxProperties
        (
            const std::vector<NXOpen::NXObject *> & selList /** Set of list  */,
            int nAltSolution /** naltsolution */ ,
            const NXOpen::Point3d & ptAnchor /** anchor point */,
            bool allowCache /** allowcache */ ,
            std::vector<NXOpen::Point3d> & boxPoints /** point of box */,
            std::vector<NXOpen::Point3d> & dir /** dir */,
            std::vector<double> & edgeLength /** edge length */,
            NXOpen::Point3d* ptOrigin /** origin point */,
            NXOpen::Point3d* ptExtreme /** extreme point*/,
            double* pdVolume /** pdvolume */ 
        );
    }; //lint !e1712 default constructor not defined for class  

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