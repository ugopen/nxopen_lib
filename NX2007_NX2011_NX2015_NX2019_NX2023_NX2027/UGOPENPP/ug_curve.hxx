/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric NX Curve C++ class definitions.

================================================================================

*/

#ifndef UG_CURVE_INCLUDED
#define UG_CURVE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_evaluatable.hxx>
#include <ug_smart.hxx>

#include <uf_curve.h>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgFace;
class UgEvaluatableObject;
class UgPoint;

class Point3;

// This class defines the interface for the manipulation of NX curve objects.
class OPENPPEXPORT UgCurveObject : public UgEvaluatableObject,
                                        public UgDisplayableSmartObject
{

    public:

        // This enum defines the curve trim extension methods should a curve
        // trim result in a lengthening of the curve.
        enum TrimExtension 
        {
            Natural  = UF_CURVE_NATURAL_SHAPE,      // Extend the curve normally by
                                                    // using its natural shape.
            Linear   = UF_CURVE_LINEAR_SHAPE,       // Extend the curve linearly by
                                                    // extending it in the line defined
                                                    // by the curve's end point and end
                                                    // tangent.
            Circular = UF_CURVE_CIRCULAR_SHAPE      // Extend the curve circularly by
                                                    // extending it in the arc defined
                                                    // by the curve's end point, end
                                                    // tangent, and end radius of 
                                                    // curvature.
        };

        // Trim the invoking object using a UgPoint object as the bounding object.
        // The point on the curve to trim to is the point on the curve that is the
        // closest to the UgPoint object.
        void trim 
        ( 
            const UgPoint             *bound_object,    // <I>
                                                        // The UgPoint object that serves
                                                        // as the bounding object for the
                                                        // trim.
            const Point3              &trim_point,      // <I> 
                                                        // A point in Absolute Coordinate
                                                        // System coordinates used to 
                                                        // specify which portion of the
                                                        // curve to trim away.
            const Point3              &help_point,      // <I> 
                                                        // A point in Absolute Coordinate
                                                        // System coordinates used to 
                                                        // help find the intersection 
                                                        // of the curve and the bounding
                                                        // object.
            TrimExtension              extension = Natural
                                                        // <I>
                                                        // The method of curve extension
                                                        // to use should the trim result
                                                        // in a lengthening of the curve.
        );

        // Trim the invoking object using a UgCurveObject object or a UgEdge object as
        // the bounding object.  The point on the curve to trim to is the intersection
        // point of the curve and the bounding object.
        void trim 
        ( 
            const UgEvaluatableObject *bound_object,    // <I>
                                                        // The UgEvaluatableObject object
                                                        // that serves as the bounding
                                                        // object for the trim.
            const Point3              &trim_point,      // <I> 
                                                        // A point in Absolute Coordinate
                                                        // System coordinates used to 
                                                        // specify which portion of the
                                                        // curve to trim away.
            const Point3              &help_point,      // <I> 
                                                        // A point in Absolute Coordinate
                                                        // System coordinates used to 
                                                        // help find the intersection 
                                                        // of the curve and the bounding
                                                        // object.
            TrimExtension              extension = Natural
                                                        // <I>
                                                        // The method of curve extension
                                                        // to use should the trim result
                                                        // in a lengthening of the curve.
        );
 
        // Trim the invoking object using a UgFace object as the bounding object.
        // The point on the curve to trim to is the intersection point of the curve and
        // the UgFace object.
        void trim 
        ( 
            const UgFace              *bound_object,    // <I>
                                                        // The UgFace object that serves
                                                        // as the bounding object for the
                                                        // trim.
            const Point3              &trim_point,      // <I> 
                                                        // A point in Absolute Coordinate
                                                        // System coordinates used to 
                                                        // specify which portion of the
                                                        // curve to trim away.
            const Point3              &help_point,      // <I> 
                                                        // A point in Absolute Coordinate
                                                        // System coordinates used to 
                                                        // help find the intersection 
                                                        // of the curve and the bounding
                                                        // object.
            TrimExtension              extension = Natural
                                                        // <I>
                                                        // The method of curve extension
                                                        // to use should the trim result
                                                        // in a lengthening of the curve.
        );

    protected:

        // Construct a UgCurveObject object
        UgCurveObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database curve that the
                                            // UgCurveObject object corresponds to.
        );

        // Destroy a UgCurveObject object
        virtual ~UgCurveObject ( );

};

#undef EXPORTLIBRARY

#endif  // UG_CURVE_INCLUDED
