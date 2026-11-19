/*
================================================================================

          Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved

================================================================================
  File description:

    Header file for Geometric Splines C++ class definitions.

================================================================================

*/

#ifndef UG_SPLINE_INCLUDED
#define UG_SPLINE_INCLUDED

// ****************************************************************************
// Include files for base classes and other needed types
// ****************************************************************************

#include <ug_session.hxx>
#include <ug_curve.hxx>
#include <ug_part.hxx>

#include <ug_vector.hxx>

#include <spline.hxx>

#include <vector3.hxx>
#include <point3.hxx>

#include <uf_curve.h>
#include <libopenpp_exports.hxx>

// ****************************************************************************
// Forward declarations for classes
// ****************************************************************************

class ThruPoint;
class Spline;
class UgAssemblyNode;

// This class defines the interface for the creation and manipulation of
// NX spline objects.  The following documentation is predicated on a basic
// knowledge of spline curves.  Certain terms, like periodic, curvature,
// and order may be unclear unless that base knowledge is available.  The
// Open API documentation should provide that knowledge.
class OPENPPEXPORT UgSpline : public UgCurveObject, public Spline {

    UG_DECLARE_INTERNAL_CLASS ( UgSpline )

    public:

        // The object to be passed to a UgSpline create method that requires
        // parameters when the parameters of the spline are to be
        // automatically calculated.
        static const std::vector < double >  NoParameters;

        // Create a UgSpline object that passes through the given 3D points.
        static UgSpline *create 
        ( 
            bool                          is_periodic,   //
                                                    // <I>
                                                    // The periodicity of the spline.
                                                    // If true, the spline will be
                                                    // created periodic.  For periodic
                                                    // splines, the first point should
                                                    // not be repeated as the last
                                                    // point.
            int                           order,    // <I>
                                                    // The order of the spline, which
                                                    // is equal to its degree plus one.
            const std::vector < Point3 > &points,   // <I>
                                                    // The points, in Absolute Coordinate
                                                    // System coordinates, which the spline 
                                                    // will pass through.  Slopes and
                                                    // curvature will be automatically
                                                    // calculated.
            const std::vector < double > &parameters = NoParameters, //         
                                                    // <I>
                                                    // The parameters of the spline at the
                                                    // input points.  The parameterization
                                                    // needs to be monotonic increasing,
                                                    // but it does not need to be normalized.
                                                    // For non-periodic splines, there are an
                                                    // equal number of points and parameters.
                                                    // For a periodic spline, there is one more
                                                    // parameter than point.
            const UgObject               *part_or_object = UgSession::getWorkPart ( )
                                                    // <I>
                                                    // This argument defines the owning part of
                                                    // the new object.  If the argument is a
                                                    // UgPart object, the argument is the owning
                                                    // part of the new object.  If the argument
                                                    // is not a UgPart object, the part that owns
                                                    // the argument is the owning part of the new
                                                    // object.
        );

        // Create a UgSpline object that passes through the given fully
        // specified ThruPoint objects.
        static UgSpline *create 
        ( 
            bool                             is_periodic, //
                                                    // <I>
                                                    // The periodicity of the spline.
                                                    // If true, the spline will be
                                                    // created periodic.  For periodic
                                                    // splines, the first point should
                                                    // not be repeated as the last
                                                    // point.
            int                              order, // <I>
                                                    // The order of the spline, which
                                                    // is equal to its degree plus one.
            const std::vector < ThruPoint > &thru_points, //
                                                    // <I>
                                                    // The points, slope vectors, and curvature
                                                    // vectors, in Absolute Coordinate System
                                                    // coordinates, that control the shape
                                                    // of the spline.
            const std::vector < double >    &parameters = NoParameters, //
                                                    // <I>
                                                    // The parameters of the spline at the
                                                    // input points.  The parameterization
                                                    // needs to be monotonic increasing, but
                                                    // it does not need to be normalized.
                                                    // For non-periodic splines, there are an
                                                    // equal number of points and parameters.
                                                    // For a periodic spline, there is one more
                                                    // parameter than point.
            const UgObject                  *part_or_object = UgSession::getWorkPart ( )
                                                    // <I>
                                                    // This argument defines the owning part of
                                                    // the new object.  If the argument is a
                                                    // UgPart object, the argument is the owning
                                                    // part of the new object.  If the argument
                                                    // is not a UgPart object, the part that owns
                                                    // the argument is the owning part of the new
                                                    // object.
        );

        // Create a UgSpline object via knot sequence / control points.
        static UgSpline *create 
        ( 
            int                           order,    // <I>
                                                    // The order of the spline, which
                                                    // is equal to its degree plus one.
            const std::vector < double > &knot_sequence, //
                                                    // <I>
                                                    // The knot sequence of the spline.
                                                    // The number of values in the knot
                                                    // sequence is equal to the number
                                                    // of control points plus the order
                                                    // of the spline.
            const std::vector < Point4 > &control_points, //
                                                    // <I>
                                                    // The homogeneous control vertices of the
                                                    // spline.  The positions of the points
                                                    // are in Absolute Coordinate System
                                                    // coordinates.
            const UgObject               *part_or_object = UgSession::getWorkPart ( )
                                                    // <I>
                                                    // This argument defines the owning part of
                                                    // the new object.  If the argument is a
                                                    // UgPart object, the argument is the owning
                                                    // part of the new object.  If the argument
                                                    // is not a UgPart object, the part that owns
                                                    // the argument is the owning part of the new
                                                    // object.
        );

        // Return the spline data of the invoking object, returning only the
        // points through which the spline passes.
        void getThruPoints 
        ( 
            bool                     *is_periodic,  // <O>
                                                    // The periodicity of the spline.
                                                    // If true, the spline is periodic.
            int                      *order,        // <O>
                                                    // The order of the spline, which
                                                    // is equal to its degree plus one.
            std::vector < Point3 >   *points,       // <O>
                                                    // The points, in Absolute Coordinate
                                                    // System coordinates, which the spline 
                                                    // passes through.
            std::vector < double >   *parameters    // <O>
                                                    // The parameters of the spline
                                                    // at the points.
        ) const;

        // Return the spline data of the invoking object, returning the
        // points through which the spline passes, as well as the associated slope and
        // curvature vectors at those points.
        void getThruPoints 
        ( 
            bool                      *is_periodic, // <O>
                                                    // The periodicity of the spline.
                                                    // If true, the spline is periodic.
            int                       *order,       // <O>
                                                    // The order of the spline, which
                                                    // is equal to its degree plus one.
            std::vector < ThruPoint > *thru_points, // <O>
                                                    // The points, slope vectors, and curvature
                                                    // vectors, in Absolute Coordinate System
                                                    // coordinates, that control the shape
                                                    // of the spline.
            std::vector < double >    *parameters   // <O>
                                                    // The parameters of the spline
                                                    // at the points of the thru_points.
        ) const;

        // Edit the spline data of the invoking object, specifying only the
        // points through which the spline passes.
        void setThruPoints
        ( 
            bool                          is_periodic,  //
                                                    // <I>
                                                    // The new periodicity of the spline.
                                                    // If true, the spline will be made
                                                    // periodic.  For periodic splines,
                                                    // the first point should not be
                                                    // repeated as the last point.
            int                           order,    // <I>
                                                    // The new order of the spline, which
                                                    // is equal to its degree plus one.
            const std::vector < Point3 > &points,   // <I>
                                                    // The new points, in Absolute Coordinate
                                                    // System coordinates, which the spline 
                                                    // will pass through.  Slopes and curvature
                                                    // will be automatically calculated.
            const std::vector < double > &parameters = NoParameters
                                                    // <I>
                                                    // The new parameters of the spline at the
                                                    // input points.  The parameterization
                                                    // needs to be monotonic increasing, but
                                                    // it does not need to be normalized.
                                                    // For non-periodic splines, there are an
                                                    // equal number of points and parameters.
                                                    // For a periodic spline, there is one more
                                                    // parameter than point.
        );
        
        // Edit the spline data of the invoking object, specifying the
        // points through which the spline passes, as well as the associated slope and
        // curvature vectors at those points.
        void setThruPoints 
        ( 
            bool                             is_periodic, //
                                                    // <I>
                                                    // The new periodicity of the spline.
                                                    // If true, the spline will be made
                                                    // periodic.  For periodic splines,
                                                    // the first point should not be
                                                    // repeated as the last point.
            int                              order, // <I>
                                                    // The new order of the spline, which
                                                    // is equal to its degree plus one.
            const std::vector < ThruPoint > &thru_points, //
                                                    // <I>
                                                    // The new points, slope vectors, and curvature
                                                    // vectors, in Absolute Coordinate System
                                                    // coordinates, that control the shape
                                                    // of the spline.
            const std::vector < double >    &parameters = NoParameters
                                                    // <I>
                                                    // The new parameters of the spline at the
                                                    // input points.  The parameterization
                                                    // needs to be monotonic increasing, but
                                                    // it does not need to be normalized.
                                                    // For non-periodic splines, there are an
                                                    // equal number of points and parameters.
                                                    // For a periodic spline, there is one more
                                                    // parameter than point.
        );

        // Return the prototype object of the invoking object if the invoking object
        // is an occurrence.  Return the invoking object if the invoking object is 
        // not an occurrence
        UgSpline *askPrototype ( ) const;

        // Return the occurrence object that corresponds to the invoking prototype
        // object and is owned by the given UgAssemblyNode object. Return 0 if the
        // invoking object is not a prototype object, or if the occurrence object can
        // not be found.
        UgSpline *askOccurrence 
        (
             const UgAssemblyNode *node  // <I> 
                                         // The owning object of the returned occurrence
                                         // object.
        ) const;

        // Return a std::vector object that contains all of the occurrences of the
        // invoking prototype object in all of the UgAssemblyNode objects in the
        // session.  Return a zero-length std::vector if the invoking object is not a
        // prototype object, or if the invoking object has no occurrences.
        const std::vector < UgSpline * > askAllOccurrences ( ) const;

    protected:

        // Initialize a UgSpline object by actually creating an NX database spline
        // through the given 3D points.
        void initialize 
        ( 
            bool                          is_periodic,  //
                                                    // <I>
                                                    // The periodicity of the spline.
                                                    // If true, the spline will be
                                                    // created periodic.  For periodic
                                                    // splines, the first point should
                                                    // not be repeated as the last
                                                    // point.
            int                           order,    // <I>
                                                    // The order of the spline, which
                                                    // is equal to its degree plus one.
            const std::vector < Point3 > &points,   // <I>
                                                    // The points, in Absolute Coordinate
                                                    // System coordinates, which the spline 
                                                    // will pass through.  Slopes and curvature
                                                    // will be automatically calculated.
            const std::vector < double > &parameters = NoParameters, //
                                                    // <I>
                                                    // The parameters of the spline at the
                                                    // input points.  The parameterization
                                                    // needs to be monotonic increasing, but
                                                    // it does not need to be normalized.
                                                    // For non-periodic splines, there are an
                                                    // equal number of points and parameters.
                                                    // For a periodic spline, there is one more
                                                    // parameter than point.
            const UgObject           *part_or_object = UgSession::getWorkPart ( )
                                                    // <I>
                                                    // This argument defines the owning part of
                                                    // the new object.  If the argument is a
                                                    // UgPart object, the argument is the owning
                                                    // part of the new object.  If the argument
                                                    // is not a UgPart object, the part that owns
                                                    // the argument is the owning part of the new
                                                    // object.
        );

        // Initialize a UgSpline object by actually creating an NX database spline
        // object through the given fully specified ThruPoint objects.
        void initialize 
        (            
            bool                             is_periodic, //
                                                    // <I>
                                                    // The periodicity of the spline.
                                                    // If true, the spline will be
                                                    // created periodic.  For periodic
                                                    // splines, the first point should
                                                    // not be repeated as the last
                                                    // point.
            int                              order, // <I>
                                                    // The order of the spline, which
                                                    // is equal to its degree plus one.
            const std::vector < ThruPoint > &thru_points, //
                                                    // <I>
                                                    // The points, slope vectors, and curvature
                                                    // vectors, in Absolute Coordinate System
                                                    // coordinates, that control the shape
                                                    // of the spline.
            const std::vector < double >    &parameters = NoParameters, //
                                                    // <I>
                                                    // The parameters of the spline at the
                                                    // input points.  The parameterization
                                                    // needs to be monotonic increasing, but
                                                    // it does not need to be normalized.
                                                    // For non-periodic splines, there are an
                                                    // equal number of points and parameters.
                                                    // For a periodic spline, there is one more
                                                    // parameter than point.
            const UgObject              *part_or_object = UgSession::getWorkPart ( )
                                                    // <I>
                                                    // This argument defines the owning part of
                                                    // the new object.  If the argument is a
                                                    // UgPart object, the argument is the owning
                                                    // part of the new object.  If the argument
                                                    // is not a UgPart object, the part that owns
                                                    // the argument is the owning part of the new
                                                    // object.
        );

        // Initialize a UgSpline object by actually creating an NX database spline
        // object via knot sequence / control points.
        void initialize
        ( 
            int                           order,    // <I>
                                                    // The order of the spline, which
                                                    // is equal to its degree plus one.
            const std::vector < double > &knot_sequence, //
                                                    // <I>
                                                    // The knot sequence of the spline.
                                                    // The number of values in the knot
                                                    // sequence is equal to the number
                                                    // of control points plus the order
                                                    // of the spline.
            const std::vector < Point4 > &control_points, //
                                                    // <I>
                                                    // The homogeneous control vertices of the
                                                    // spline.  The positions of the points
                                                    // are in Absolute Coordinate System
                                                    // coordinates.
            const UgObject           *part_or_object = UgSession::getWorkPart ( )
                                                    // <I>
                                                    // This argument defines the owning part of
                                                    // the new object.  If the argument is a
                                                    // UgPart object, the argument is the owning
                                                    // part of the new object.  If the argument
                                                    // is not a UgPart object, the part that owns
                                                    // the argument is the owning part of the new
                                                    // object.
        );

        // Construct a UgSpline object
        UgSpline
        (
            tag_t tag = NULL_TAG                    // The tag of the NX database spline that the
                                                    // UgSpline object corresponds to.
        );

        // Destroy a UgSpline object
        virtual ~UgSpline ( );

    private:

        // Return the Curve object that represents the invoking object.
        // This method is provided to satisfy the pure virtual method
        // defined in the class UgEvaluatableObject.  It isn't needed by
        // direct users of this class because all of the methods that class
        // Curve provides are directly accessible via the indirect inheritance of
        // this class from the Curve class.  Hence, the scope of this method
        // is private in this class.  This method does enable polymorphic access
        // to objects of this class in the event that a UgEvaluatableObject
        // array containing edges as well as curves is encountered.
        const Curve *askCurve ( ) const;

        // Return the UgEvaluatableObject object that represents the invoking
        // object.  This method is provided to satisfy the pure virtual method
        // defined in the class Curve.  It isn't needed by direct users of this
        // this class because all the methods that class UgEvaluatableObject
        // provides are directly accessible via the inheritance of this class
        // from the UgEvaluatableObject class.  Hence, the scope of this method
        // is private in this class.  This method does enable polymorphic access
        // to objects of this class in the event that a Curve array containing
        // edges as well as curves is encountered.
        const UgEvaluatableObject *askEvaluatableObject ( ) const;

        // Convert the data that defines a UgSpline object into Open API data
        // so that an NX database spline may be easily created using the Open API.
        static void convertToUfData 
        (
            bool                             is_periodic, //
                                                    // <I>
                                                    // The periodicity of the spline.
                                                    // If true, the spline will be
                                                    // created periodic.  For periodic
                                                    // splines, the first point should
                                                    // not be repeated as the last
                                                    // point.
            const std::vector < ThruPoint > &thru_points, //
                                                    // <I>
                                                    // The points, slope vectors, and curvature
                                                    // vectors, in Absolute Coordinate System
                                                    // coordinates, that control the shape
                                                    // of the spline.
            const std::vector < double >    &parameters, //
                                                    // <I>
                                                    // The parameters of the spline at the
                                                    // input points.  The parameterization
                                                    // needs to be monotonic increasing, but
                                                    // it does not need to be normalized.
                                                    // For non-periodic splines, there are an
                                                    // equal number of points and parameters.
                                                    // For a periodic spline, there is one more
                                                    // parameter than point.
            UF_CURVE_pt_slope_crvatr_t
                                      **uf_data,    // <O>
                                                    // An array of Open struct's that
                                                    // correspond to the std::vector of
                                                    // input ThruPoint objects.
            double                    **uf_parameters
                                                    // <O>
                                                    // An array of double parameter values
                                                    // that correspond to the std::vector of
                                                    // input parameter values.
        );

};

//  A helper class for UgSpline.  This class defines the data that fully
//  specifies the shape of a spline that passes through the given 3D point
//  that an instance of this class contains.
class OPENPPEXPORT ThruPoint {
    
    public:

        // This enum specifies how to control the slope of the spline at the through
        // point.
        enum SlopeType
        {
            SlopeTypeNone      = UF_CURVE_SLOPE_NONE,       //
                                        // No spline slope is assigned at the given point.
            SlopeTypeAuto      = UF_CURVE_SLOPE_AUTO,       //
                                        // The spline slope at the given
                                        // point is internally calculated using
                                        // all the through points specified.
            SlopeTypeDirection = UF_CURVE_SLOPE_DIR,        //
                                        // The direction of the spline slope at the given
                                        // point is defined by the m_slope_vector data
                                        // member of this object.
            SlopeTypeVector    = UF_CURVE_SLOPE_VEC         //
                                        // The direction and magnitude of the spline slope
                                        // at the given point is defined by the m_slope_vector
                                        // data member of this object.
        };

        // This enum specifies how to control the curvature of the spline at the through
        // point.
        enum CurvatureType
        {
            CurvatureTypeNone   = UF_CURVE_CRVATR_NONE,     //
                                        // No spline curvature is assigned at the given point.
            CurvatureTypeAuto   = UF_CURVE_CRVATR_AUTO_DIR, //
                                        // The magnitude of the spline curvature at the given
                                        // point is defined by the m_curvature_vector data
                                        // member of this object.  The direction of the spline
                                        // curvature is internally determined.  The corresponding
                                        // slope type must be SlopeTypeAuto
            CurvatureTypeVector = UF_CURVE_CRVATR_VEC       //
                                        // The direction and magnitude of the spline curvature
                                        // at the given point is defined by the m_curvature_vector
                                        // data member of this object.
        };

        // Construct a ThruPoint containing the given point.  The slope type
        // is set to SlopeTypeNone, and the curvature is set to CurvatureTypeNone. 
        ThruPoint
        (
            const Point3 &point = Point3 ( )    // The point of this object
                                                // that the spline will pass
                                                // through.
        );

        // Construct a fully specified ThruPoint.  If curvatureType is
        // defined as CurvatureTypeAuto, then slopeType must be defined as
        // SlopeTypeAuto.  If curvatureType is defined as CurvatureTypeVector, 
        // then slopeType must be defined as either SlopeTypeDirection
        // or SlopeTypeVector.
        ThruPoint 
        ( 
            const Point3  &point,               // The point of this object
                                                // that the spline will pass
                                                // through.
            SlopeType      slopeType,           // Type of spline slope control
                                                // at the given point.
            const Vector3 &slope,               // The vector defining the spline
                                                // slope at the given point.
            CurvatureType  curvatureType,       // Type of spline curvature control
                                                // at the given point.
            const Vector3 &curvature            // The vector defining the spline
                                                // curvature at the given point. 
        );

        // Point through which the spline will pass.
        Point3        m_thru_point;

        // The method of slope control being defined at the given point.
        // Assigning a spline slope at a given point is not allowed on
        // a spline with an order of less than 3.
        SlopeType     m_slope_type;

        // Vector defining the spline slope at the given point.  If both 
        // m_slope_vector and m_curvature_vector are defined, the two vectors
        // must be orthogonal.
        Vector3       m_slope_vector;

        // The method of curvature control being defined at the given point.
        // Assigning a spline curvature at a given point is not allowed on
        // a spline with an order of less than 4.
        CurvatureType m_curvature_type;

        // Vector defining the spline curvature at the given point.  If both 
        // m_slope_vector and m_curvature_vector are defined, the two vectors
        // must be orthogonal.
        Vector3       m_curvature_vector;

    private:

        // Construct a fully specified ThruPoint from an Open API 
        // UF_CURVE_pt_slope_crvatr_t struct.  The ThruPoint class
        // is based on the Open API struct, so the construction is straight
        // forward.
        ThruPoint 
        (
            const UF_CURVE_pt_slope_crvatr_t &uf_data
                                                    // The Open API struct to
                                                    // construct the ThruPoint
                                                    // from.
        );

        // Convert the invoking ThruPoint object into an Open API
        // UF_CURVE_pt_slope_crvatr_t struct and return that struct.  The
        // ThruPoint class is based on the Open API struct, so the conversion
        // is straight forward.
        UF_CURVE_pt_slope_crvatr_t asUgOpenStruct ( ) const;

    // The UgSpline class is a friend to make use of the private methods of
    // this class.  The private methods only make sense for creation and
    // manipulation of UgSpline objects.
    friend class UgSpline;

};

#undef EXPORTLIBRARY

#endif  // UG_SPLINE_INCLUDED
