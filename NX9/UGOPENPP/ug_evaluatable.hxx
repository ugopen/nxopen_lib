/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Evaluatable NX object C++ class definitions

================================================================================

*/

#ifndef UG_EVALUATABLE_INCLUDED
#define UG_EVALUATABLE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_displayable.hxx>
#include <ug_session.hxx>
#include <ug_part.hxx>

#include <ug_vector.hxx>

#include <interval.hxx>

#include <point3.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgCurveObject;
class UgFace;

class Evaluator;
class CurveCurveIntersectionPoint;
class CurveCurveCoincidentCurve;
class CurveFaceIntersectionPoint;

class Curve;

// This class defines the interface for the manipulation of NX curve objects
// and NX edge objects.
class OPENPPEXPORT UgEvaluatableObject : public UgDisplayableObject
{

    public:

        // Return the Curve object that represents the invoking object.
        virtual const Curve *askCurve ( ) const = 0;

        // Return the Evaluator object that represents the invoking object.
        const Evaluator askEvaluator ( )  const;      

        // Compute and return the entire arc length of the invoking object.
        double computeArcLength ( ) const;

        // Compute and return a portion of the arc length of the invoking object.
        double computeArcLength
        (
            const Interval     &interval        // <I>
                                                // The start and end parameters of the invoking
                                                // object that define the arc length to return.
                                                // The values are raw parameters of the invoking
                                                // object.
        ) const;

        // Compute and return all of the intersection points between the invoking
        // object and the given UgEvaluatableObject object.
        const std::vector < CurveCurveIntersectionPoint > computeIntersectionPoints 
        ( 
            const UgEvaluatableObject *curve,   // <I>
                                                // The UgEvaluatableObject object to intersect
                                                // with the invoking object.
            double                     tolerance = UgSession::getDistanceTolerance ( )
                                                // <I>
                                                // A distance tolerance value in the units of
                                                // the current work part that is used in the
                                                // intersection algorithm.  Any time the
                                                // invoking object passes within this distance
                                                // of the other object, it is considered an
                                                // intersection.
        ) const;

        // Compute and return all of the coincident curves between the invoking
        // object and the given UgEvaluatableObject object.
        const std::vector < CurveCurveCoincidentCurve > computeCoincidentCurves
        ( 
            const UgEvaluatableObject *curve,   // <I>
                                                // The UgEvaluatableObject object to intersect
                                                // with the invoking object.
            double                     tolerance = UgSession::getDistanceTolerance ( ), //
                                                // <I>
                                                // A distance tolerance value in the units of
                                                // the current work part that is used in the
                                                // intersection algorithm.  Any time the
                                                // invoking object passes within this distance
                                                // of the other object, it is considered an
                                                // intersection.
            const UgObject            *part_or_object = UgSession::getWorkPart ( )
                                                // <I>
                                                // This argument defines the owning part of
                                                // the new curves.  If the argument is a
                                                // UgPart object, the argument is the owning
                                                // part of the new curves.  If the argument
                                                // is not a UgPart object, the part that owns
                                                // the argument is the owning part of the new
                                                // curves.
        ) const;

        // Compute and return all of the intersection points between the invoking
        // object and the given UgFace object.
        const std::vector < CurveFaceIntersectionPoint > computeIntersectionPoints
        ( 
            const UgFace              *face,    // <I> 
                                                // The UgFace object to intersect
                                                // with the invoking object.
            double                     tolerance = UgSession::getDistanceTolerance ( )
                                                // <I>
                                                // A distance tolerance value in the units of
                                                // the current work part that is used in the
                                                // intersection algorithm.  Any time the
                                                // invoking object passes within this distance
                                                // of the other object, it is considered an
                                                // intersection.
        ) const;
    
    protected:

        // Construct a UgEvaluatableObject object
        UgEvaluatableObject
        (
            tag_t tag = NULL_TAG            // The tag of the NX database curve or edge that the
                                            // UgEvaluatableObject object corresponds to.
        );

        // Destroy a UgEvaluatableObject object
        virtual ~UgEvaluatableObject ( );

};

// A helper class for UgEvaluatableObject.  This class defines the data that represents
// an intesection point of two UgEvaluatableObject objects.
class OPENPPEXPORT CurveCurveIntersectionPoint
{

    public:

        // Return the intersection point in Absolute Coordinate System coordinates.
        const Point3 askPoint ( ) const;

        // Return the parameter of the intersection point with respect to the object 
        // that invoked the method computeIntersectionPoints ( ).
        double askParameterOnInvoking ( ) const;

        // Return the parameter of the intersection point with respect to the object 
        // that was passed as an argument to the method computeIntersectionPoints ( ).
        double askParameterOnCurve ( ) const;

        // Construct a CurveCurveIntersectionPoint object.  This default constructor is 
        // required to allow for a std::vector of these objects.
        CurveCurveIntersectionPoint ( );

    protected:

        // Construct a CurveCurveIntersectionPoint object by specifying the point and
        // the parameters.
        CurveCurveIntersectionPoint
        (
            Point3 point,                       // The intersection point in Absolute
                                                // Coordinate System coordinates.
            double param_invoke,                // The parameter of the intersection point
                                                // with respect to the invoking object.
            double param_curve                  // The parameter of the intersection point
                                                // with respect to the argument object.
        );

    private:

        // The intersection point in Absolute Coordinate System coordinates.
        Point3 m_point;

        // The parameter of the intersection point with respect to the invoking object.
        double m_parameter_invoke;

        // The parameter of the intersection point with respect to the argument object.
        double m_parameter_curve;

    // The UgEvaluatableObject class is a friend to allow it to invoke the protected
    // constructor of this class.
    friend class UgEvaluatableObject;

};

// A helper class for UgEvaluatableObject.  This class defines the data that represents
// a coincident curve intesection of two UgEvaluatableObject objects.
class OPENPPEXPORT CurveCurveCoincidentCurve
{

    public:

        // Return the coincident curve intersection.
        UgCurveObject *askCurve ( ) const;

        // Return the Interval object that represents the start and end parameters
        // of the coincident curve with respect to the object that invoked the 
        // method computeCoincidentCurves ( ).
        const Interval askIntervalOnInvoking ( ) const;

        // Return the Interval object that represents the start and end parameters
        // of the coincident curve with respect to the object that was passed as
        // an argument to the method computeCoincidentCurves ( ). 
        const Interval askIntervalOnCurve ( ) const;
      
        // Construct a CurveCurveCoincidentCurve object.  This default constructor is 
        // required to allow for a std::vector of these objects.
        CurveCurveCoincidentCurve ( );

    protected:

        // Construct a CurveCurveCoincidentCurve object by specifying the curve and
        // the Interval objects.
        CurveCurveCoincidentCurve
        (
            UgCurveObject   *curve,             // The coincident curve object.
            const Interval  &interval_invoke,   // The parameter interval of the coincident
                                                // curve with respect to the invoking object.
            const Interval  &interval_curve     // The parameter interval of the coincident
                                                // curve with respect to the argument object.
        );

    private:

        // The coincident curve object
        const UgCurveObject    *m_curve;

        // The parameter interval of the coincident curve with respect to the invoking object.
        Interval                m_interval_invoke;
        
        // The parameter interval of the coincident curve with respect to the argument object.
        Interval                m_interval_curve;

    // The UgEvaluatableObject class is a friend to allow it to invoke the protected
    // constructor of this class.
    friend class UgEvaluatableObject;

};

// A helper class for UgEvaluatableObject and UgFace.  This class defines the data that
// represents an intesection point of a UgEvaluatableObject object and a UgFace object.
class OPENPPEXPORT CurveFaceIntersectionPoint
{

    public:

        // Return the intersection point in Absolute Coordinate System coordinates.
        const Point3 askPoint ( ) const;

        // Return the parameter of the intersection point with respect to the UgEvaluatableObject
        // object. 
        double askParameterOnCurve ( ) const;

        // Return the U parameter of the intersection point with respect to the UgFace object. 
        double askUParameterOnFace ( ) const;

        // Return the V parameter of the intersection point with respect to the UgFace object. 
        double askVParameterOnFace ( ) const;

        // Construct a CurveFaceIntersectionPoint object.  This default constructor is 
        // required to allow for a std::vector of these objects.
        CurveFaceIntersectionPoint ( );

    protected:

        // Construct a CurveFaceIntersectionPoint object by specifying the point and
        // the parameters.
        CurveFaceIntersectionPoint
        (
            Point3 point,                       // The intersection point in Absolute
                                                // Coordinate System coordinates.
            double param_curve,                 // The parameter of the intersection point
                                                // with respect to the UgEvaluatableObject
                                                // object.
            double u_param_face,                // The U parameter of the intersection point
                                                // with respect to the UgFace object.
            double v_param_face                 // The V parameter of the intersection point
                                                // with respect to the UgFace object.
        );

    private:

        // The intersection point in Absolute Coordinate System coordinates.
        Point3 m_point;

        // The parameter of the intersection point with respect to the UgEvaluatableObject
        // object.
        double m_parameter_curve;

        // The U parameter of the intersection point with respect to the UgFace object.
        double m_u_parameter_face;

        // The V parameter of the intersection point with respect to the UgFace object.
        double m_v_parameter_face;

    // The UgEvaluatableObject class is a friend to allow it to invoke the protected
    // constructor of this class.
    friend class UgEvaluatableObject;

};

#undef EXPORTLIBRARY

#endif  // UG_EVALAUTABLE_INCLUDED
