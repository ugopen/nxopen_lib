/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric Evaluator C++ class definitions.

================================================================================

*/

#ifndef EVALUATOR_INCLUDED
#define EVALUATOR_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_openpp.hxx>
#include <ug_vector.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgEvaluatableObject;
class Interval;
class Vector3;
class Point3;
class Point4;

extern "C"
{
// 
typedef struct UF_EVAL_S            UF_EVAL_t;

// 
typedef struct UF_EVAL_line_s       UF_EVAL_line_t;

// 
typedef struct UF_EVAL_arc_s        UF_EVAL_arc_t;

// 
typedef struct UF_EVAL_ellipse_s    UF_EVAL_ellipse_t;

// 
typedef struct UF_EVAL_parabola_s   UF_EVAL_parabola_t;

// 
typedef struct UF_EVAL_hyperbola_s  UF_EVAL_hyperbola_t;

// 
typedef struct UF_EVAL_spline_s     UF_EVAL_spline_t;
}

// This class defines the interface for evaluating points and vectors on a curve
// represented by a UG curve object or a UG edge object.  All parameter values
// used by the interface to this class represent a natural parameter value of the 
// curve in question.  Using a natural parameter value that is beyond the extents
// of the curve will not throw an exception, but the points and vectors return
// from such an evaluation will not lie on the curve.
class OPENPPEXPORT Evaluator
{ 

    public:

        // Construct an Evaluator object by copying an existing Evaluator object
        Evaluator
        (
            const Evaluator &evaluator          // The Evaluator object to copy
        );

        // Destroy an Evaluator object
        virtual ~Evaluator ( );
          
        // Return the start and end parameters of the invoking object.
        const Interval askLimits ( ) const;

        // Return a point on the curve of the invoking object.
        // The point is in Absolute Coordinate System coordinates.
        const Point3 evaluatePoint
        (
            double        parameter             // <I>
                                                // The natural curve parameter at which to evaluate.
        ) const;
 
        // Return a unit tangent vector on the curve of the invoking object.
        // The vector is in Absolute Coordinate System coordinates.
        const Vector3 evaluateTangent
        (
            double        parameter             // <I>
                                                // The natural curve parameter at which to evaluate.
        ) const;

        // Return a unit normal vector on the curve of the invoking object.
        // The vector is in Absolute Coordinate System coordinates.
        const Vector3 evaluateNormal
        (
            double        parameter             // <I>
                                                // The natural curve parameter at which to evaluate.
        ) const;

        // Return a unit binormal vector on the curve of the invoking object.
        // The vector is in Absolute Coordinate System coordinates.
        const Vector3 evaluateBinormal
        (
            double        parameter             // <I>
                                                // The natural curve parameter at which to evaluate.
        ) const;

        // Return derivative vectors on the curve of the invoking object.
        // The vectors are in Absolute Coordinate System coordinates.
        const std::vector < Vector3 > evaluateDerivatives
        (
            double        parameter,            // <I>
                                                // The natural curve parameter at which to evaluate.
            int           n_derivatives = 1     // <I>
                                                // The number of derivatives requested.
        ) const;

        // Return the point on the curve of the invoking object that is the closest to
        // a given reference point.
        void evaluateClosestPoint 
        ( 
            const Point3 &reference_point,      // <I>
                                                // The reference point in Absolute
                                                // Coordinate System coordinates
            double       *parameter,            // <O>
                                                // The natural curve parameter of the closest point
            Point3       *closest_point         // <O>
                                                // The closest point on the curve in
                                                // Absolute Coordinate System coordinates
        ) const;
 
    private:

        // Construct an Evaluator object from the given UgEvaluatableObject object.
        Evaluator
        (
            const UgEvaluatableObject *object   // The UgEvaluatableObject object that
                                                // supplies the data to construct the
                                                // Evaluator object.
        );

        // Determine the equality of two Evaluator objects.  The two objects are
        // considered equal if both evaluator objects represent the same curve type
        // and if the data of one evaluator is equal to the data of the other within
        // the system tolerance.
        bool operator==
        (
            const Evaluator    &evaluator       // The Evaluator object to test for equality
                                                // against the invoking object.
        ) const;

        // Determine if the invoking object is periodic.
        bool isPeriodic ( ) const;

        // Determine if the invoking object represents a linear curve.
        bool isLine    ( ) const;

        // Determine if the invoking object represents a circular curve.
        bool isArc     ( ) const;

        // Determine if the invoking object represents an elliptical curve.
        bool isEllipse ( ) const;

        // Determine if the invoking object represents a spline curve.
        bool isSpline  ( ) const;

        // Return all of the line data of the invoking object via a UG/Open struct,
        // throwing an exception if the invoking object represents the wrong curve type.
        const UF_EVAL_line_t      askLine      ( ) const;

        // Return all of the arc data of the invoking object via a UG/Open struct,
        // throwing an exception if the invoking object represents the wrong curve type.
        const UF_EVAL_arc_t       askArc       ( ) const;

        // Return all of the ellipse data of the invoking object via a UG/Open struct,
        // throwing an exception if the invoking object represents the wrong curve type.
        const UF_EVAL_ellipse_t   askEllipse   ( ) const;

        // Return all of the parabola data of the invoking object via a UG/Open struct,
        // throwing an exception if the invoking object represents the wrong curve type.
        const UF_EVAL_parabola_t  askParabola  ( ) const;

        // Return all of the hyperbola data of the invoking object via a UG/Open struct,
        // throwing an exception if the invoking object represents the wrong curve type.
        const UF_EVAL_hyperbola_t askHyperbola ( ) const;

        // Return all of the spline data of the invoking object via a UG/Open struct,
        // throwing an exception if the invoking object represents the wrong curve type.
        const UF_EVAL_spline_t    askSpline    ( ) const;

        // Return the knot sequence of the invoking object, throwing an exception if the
        // invoking object does not represent a spline.
        const std::vector < double > getSplineKnotSequence  ( ) const;

        // Return the homogeneous control vertices of the invoking object, throwing an
        // exception if the invoking object does not represent a spline.
        // The positions of the points are in Absolute Coordinate System coordinates.
        const std::vector < Point4 > getSplineControlPoints ( ) const;

        // The UG/Open struct that represents the evaluator data of this object.
        UF_EVAL_t    *m_evaluator;

    // The UgEvaluatableObject class is a friend to make use of the private constructor.
    // Only UgEvaluatableObject objects can construct valid Evaluator objects.
    friend class UgEvaluatableObject;
 
    // The UgEdge class is a friend to make use of the private methods of this class that
    // determine the curve type.
    friend class UgEdge;

    // The UgEdgeLineObject class is a friend to make use of the isLine ( ) method of this
    // class.
    friend class UgEdgeLineObject;

    // The UgEdgeArcObject class is a friend to make use of the isArc ( ) method of this
    // class.
    friend class UgEdgeArcObject;

    // The UgEdgeEllipseObject class is a friend to make use of the isEllipse ( ) method of this
    // class.
    friend class UgEdgeEllipseObject;

    // The UgEdgeSplineObject class is a friend to make use of the isSpline ( ) method of this
    // class.
    friend class UgEdgeSplineObject;

    // The Curve class is a friend to make use of the isPeriodic ( ) method of this
    // class.
    friend class Curve;

    // The Line class is a friend to access the UG/Open struct that represents this class.
    friend class Line;

    // The Arc class is a friend to access the UG/Open struct that represents this class.
    friend class Arc;

    // The Ellipse class is a friend to access the UG/Open struct that represents this class.
    friend class Ellipse;

    // The Parabola class is a friend to access the UG/Open struct that represents this class.
    friend class Parabola;

    // The Hyperbola class is a friend to access the UG/Open struct that represents this class.
    friend class Hyperbola;

    // The Spline class is a friend to access the UG/Open struct that represents this class,
    // as well as the knot sequence and control points.
    friend class Spline;

};

#undef EXPORTLIBRARY

#endif  // EVALUATOR_INCLUDED
