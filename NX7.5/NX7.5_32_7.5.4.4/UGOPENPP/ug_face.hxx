/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Face C++ class definitions.

================================================================================

*/

#ifndef UG_FACE_INCLUDED
#define UG_FACE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_displayable.hxx>
#include <ug_evaluatable.hxx>

#include <ug_vector.hxx>

#include <vector3.hxx>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class UgBodyFeatureObject;
class UgCurve;
class UgBody;
class UgEdge;
class UgAssemblyNode;

class FaceFaceIntersectionPoint;
class Derivatives;
class Loop;

// This class defines the interface for the manipulation of NX face objects.
class OPENPPEXPORT UgFace : public UgDisplayableObject
{

    UG_DECLARE_INTERNAL_CLASS ( UgFace )

    public:

        // Return the U parameter limits of the invoking object.
        const Interval askLimitsInU ( ) const;

        // Return the V parameter limits of the invoking object.
        const Interval askLimitsInV ( ) const;

        // Return a point on the invoking object.
        // The point is in Absolute Coordinate System coordinates.
        const Point3 evaluatePoint
        (
            double u_parameter,             // <I>
                                            // The U parameter at which to evaluate
            double v_parameter              // <I>
                                            // The V parameter at which to evaluate
        ) const;

        // Return a unit normal vector on the invoking object.
        // The vector is in Absolute Coordinate System coordinates.
        const Vector3 evaluateNormal
        (
            double u_parameter,             // <I>
                                            // The U parameter at which to evaluate
            double v_parameter              // <I>
                                            // The V parameter at which to evaluate
        ) const;

        // Return the partial derivative vectors on the invoking object.
        // The vectors are in Absolute Coordinate System coordinates.
        const Derivatives evaluateDerivatives
        (
            double u_parameter,             // <I>
                                            // The U parameter at which to evaluate
            double v_parameter              // <I>
                                            // The V parameter at which to evaluate
        ) const;

        // Return the point on the invoking object that is the closest to
        // a given reference point.
        void evaluateClosestPoint
        (
            const Point3 &reference_point,      // <I>
                                                // The reference point in Absolute
                                                // Coordinate System coordinates
            double       *parameter_u,          // <O>
                                                // The U parameter of the closest point
            double       *parameter_v,          // <O>
                                                // The V parameter of the closest point
            Point3       *closest_point         // <O>
                                                // The closest point on the face in
                                                // Absolute Coordinate System coordinates
        ) const;

        // Return the body of the invoking object.
        UgBody *askBody ( ) const;

        // Return all the features of the invoking object.
        const std::vector < UgBodyFeatureObject * > askFeatures ( ) const;

        // Return all of the split faces of the invoking object.  All of the faces,
        // including the invoking face, that were split from the invoking face are
        // returned by this method.  A face splits as a result of any number of
        // feature operations.  For example, if a slot is created on a block, the
        // face that is broken to create the slot is split.
        const std::vector < UgFace * > askSplitFaces ( ) const;

        // Return all of the loops of the invoking object.
        const std::vector < Loop > askLoops ( ) const;

        // Return all of the edges of the invoking object.
        const std::vector < UgEdge * > askEdges ( ) const;

        // Compute and return all of the intersection points between the invoking
        // object and the given UgEvaluatableObject object.
        const std::vector < CurveFaceIntersectionPoint > computeIntersectionPoints
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

        // Compute and return all of the intersection points between the invoking
        // object and the given UgFace object.
        const std::vector < FaceFaceIntersectionPoint > computeIntersectionPoints
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

        // Compute and return all of the intersection curves between the invoking
        // object and the given UgFace object.
        const std::vector < UgCurveObject * > computeIntersectionCurves
        (
            const UgFace              *face,    // <I>
                                                // The UgFace object to intersect
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

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is
        // not an occurrence
        UgFace *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        UgFace *askOccurrence
        (
             const UgAssemblyNode *node  // <I>
                                         // The owning object of the returned occurrence
                                         // object.
        ) const;

        // Return a std::vector object that contains all of the occurrences of the
        // invoking prototype object in all of the UgAssemblyNode objects in the
        // session.  Return a zero-length std::vector if the invoking object is not a
        // prototype object, or if the invoking object has no occurrences.
        const std::vector < UgFace * > askAllOccurrences ( ) const;

    protected:

        // Construct a UgFace object
        UgFace
        (
            tag_t tag = NULL_TAG            // The tag of the NX database face that the
                                            // UgFace object corresponds to.
        );

        // Destroy a UgFace object
        virtual ~UgFace ( );

};

// A helper class for UgFace.  This class defines the data that represents
// the partial derivative vectors calculated from evaluating a UgFace object.
class OPENPPEXPORT Derivatives
{

    public:

        // Construct a Derivatives object that has all derivatives initialized
        // to the zero vector.
        Derivatives ( );

        // Construct a Derivatives object that has all derivatives initialized
        // to the given derivative vectors.
        Derivatives
        (
            const Vector3 &du,    // <I>
                                  // The first partial derivative vector
                                  // with respect to the U parameter.
            const Vector3 &dv,    // <I>
                                  // The first partial derivative vector
                                  // with respect to the V parameter.
            const Vector3 &d2u,   // <I>
                                  // The second partial derivative vector
                                  // with respect to the U parameter.
            const Vector3 &dudv,  // <I>
                                  // The second partial derivative vector
                                  // with respect to the U and V parameter.
            const Vector3 &d2v,   // <I>
                                  // The second partial derivative vector
                                  // with respect to the V parameter.
            const Vector3 &d3u,   // <I>
                                  // The third partial derivative vector
                                  // with respect to the U parameter.
            const Vector3 &d2udv, // <I>
                                  // The first partial derivative vector
                                  // with respect to the U parameter of
                                  // the second partial derivative
                                  // with respect to the U and V parameter.
            const Vector3 &dud2v, // <I>
                                  // The first partial derivative vector
                                  // with respect to the V parameter of
                                  // the second partial derivative
                                  // with respect to the U and V parameter.
            const Vector3 &d3v    // <I>
                                  // The third partial derivative vector
                                  // with respect to the V parameter.
        );

        // Destroy a Derivatives object.
        ~Derivatives ( );

        // The first partial derivative vector with respect to the U parameter.
        Vector3 m_du;

        // The first partial derivative vector with respect to the V parameter.
        Vector3 m_dv;

        // The second partial derivative vector with respect to the U parameter.
        Vector3 m_d2u;

        // The second partial derivative vector with respect to the U and V
        // parameter.
        Vector3 m_dudv;

        // The second partial derivative vector with respect to the V parameter.
        Vector3 m_d2v;

        // The third partial derivative vector with respect to the U parameter.
        Vector3 m_d3u;

        // The first partial derivative vector with respect to the U parameter
        // of the second partial derivative with respect to the U and V parameter.
        Vector3 m_d2udv;

        // The first partial derivative vector with respect to the V parameter
        // of the second partial derivative with respect to the U and V parameter.
        Vector3 m_dud2v;

        // The third partial derivative vector with respect to the V parameter.
        Vector3 m_d3v;

};

// A helper class for UgFace.  A loop is a closed connected set of edges that
// represents one boundary of a face.  The loop can be either a peripheral
// loop, a hole loop, or some other kind of loop.  This class defines the
// interface for the creation and manipulation of loop objects.
class OPENPPEXPORT Loop
{

    public:

        // Determine if the invoking object is a peripheral loop.
        bool isPeripheralLoop ( ) const;

        // Determine if the invoking object is a hole loop.
        bool isHoleLoop ( ) const;

        // Determine if the invoking object is some other kind of loop.
        bool isOtherLoop ( ) const;

        // Return all of the edges of the invoking object.
        const std::vector < UgEdge * > askEdges ( ) const;

        // Construct a Loop object.  This default constructor is
        // required to allow for a std::vector of these objects.
        Loop ( );

        // Destroy a Loop object.
        ~Loop ( );

    private:

        // This enum defines the available loop types.
        enum LoopType
        {
            Peripheral = 1,         // Defines a peripheral loop, which defines the
                                    // farthest extent of the face.  A face can have
                                    // only one peripheral loop.
            Hole       = 2,         // Defines a hole loop, which defines an area that
                                    // has been removed from the interior of a face.
                                    // A face may have any number of hole loops.
            Other      = 3          // Defines a loop where the distinction between
                                    // peripheral and hole does not make sense, e.g.
                                    // on a spherical or toroidal face.
        };

        // Construct a Loop object by specifying the type and the edges.
        Loop
        (
            LoopType                        loop_type, // The type of loop to construct
            const std::vector < UgEdge * > &edges      // The connected set of edges that make
                                                       // the loop.
        );

        // The type of the loop.
        LoopType                  m_loop_type;

        // The array of edges that represents a connect set that make the loop.
        std::vector < UgEdge * >  m_edges;

    // The UgFace class is a friend to allow it to invoke the private constructor
    // of this class.
    friend class UgFace;

};

// A helper class for UgFace.  This class defines the data that represents
// an intesection point of two UgFace objects.
class OPENPPEXPORT FaceFaceIntersectionPoint
{

    public:

        // Return the intersection point in Absolute Coordinate System coordinates.
        const Point3 askPoint ( ) const;

        // Return the U parameter of the intersection point with respect to the object
        // that invoked the method computeIntersectionPoints ( ).
        double askUParameterOnInvoking ( ) const;

        // Return the V parameter of the intersection point with respect to the object
        // that invoked the method computeIntersectionPoints ( ).
        double askVParameterOnInvoking ( ) const;

        // Return the U parameter of the intersection point with respect to the object
        // that was passed as an argument to the method computeIntersectionPoints ( ).
        double askUParameterOnFace ( ) const;

        // Return the V parameter of the intersection point with respect to the object
        // that was passed as an argument to the method computeIntersectionPoints ( ).
        double askVParameterOnFace ( ) const;

        // Construct a FaceFaceIntersectionPoint object.  This default constructor is
        // required to allow for a std::vector of these objects.
        FaceFaceIntersectionPoint ( );

        // Destroy a FaceFaceIntersectionPoint object.
        ~FaceFaceIntersectionPoint ( );

    private:

        // Construct a FaceFaceIntersectionPoint object by specifying the point and
        // the parameters.
        FaceFaceIntersectionPoint
        (
            Point3 point,                       // The intersection point in Absolute
                                                // Coordinate System coordinates.
            double u_param_invoke,              // The U parameter of the intersection point
                                                // with respect to the invoking object.
            double v_param_invoke,              // The V parameter of the intersection point
                                                // with respect to the invoking object.
            double u_param_face,                // The U parameter of the intersection point
                                                // with respect to the argument object.
            double v_param_face                 // The V parameter of the intersection point
                                                // with respect to the argument object.
        );

        // The intersection point in Absolute Coordinate System coordinates.
        Point3 m_point;

        // The U parameter of the intersection point with respect to the invoking object.
        double m_v_parameter_invoke;

        // The V parameter of the intersection point with respect to the invoking object.
        double m_u_parameter_invoke;

        // The U parameter of the intersection point with respect to the argument object.
        double m_u_parameter_face;

        // The V parameter of the intersection point with respect to the argument object.
        double m_v_parameter_face;

    // The UgFace class is a friend to allow it to invoke the private
    // constructor of this class.
    friend class UgFace;

};

#undef EXPORTLIBRARY

#endif  // UG_FACE_INCLUDED
