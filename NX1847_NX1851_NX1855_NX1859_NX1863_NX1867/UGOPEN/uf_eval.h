/*******************************************************************************
              Copyright (c) 1998-2005  UGS Corp.
                     All Rights Reserved                       



File description:

Open C API interface to functions that evaluate curves.  These functions are
the preferred way of evaluating curves and edges.

The routines in this header file allow you to obtain the data for curves
(lines, arcs, conics, and splines) by querying the curve structure for a
specific curve through the evaluator. The evaluator is a pointer to the
UF_EVAL_s data structure.  These routines allow you to:
  . Query the data of curves, conics, and splines.
  . Copy the evaluator of a curve or edge.
  . Evaluate a point, derivatives, and unit vector of an evaluator of a curve
    or edge.

The UF_EVAL module accepts denormalized parameters, that is the parameters
may not be between 0 and 1.  The parameterization will be set up
when the curve is created.  You can get the parameterization by calling
 UF_EVAL_ask_limits.

To use these routines, you must first call UF_EVAL_initialize which
returns the pointer to the evaluator. Once you obtain the evaluator
you can use any of the evaluator routines. After you have obtained the
requested information, free the evaluator with UF_EVAL_free.


*******************************************************************************/

#ifndef UF_EVAL_H_INCLUDED
#define UF_EVAL_H_INCLUDED

#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct UF_EVAL_S *UF_EVAL_p_t;

struct UF_EVAL_line_s
{
    double      length;       /* Line length */
    double      start[3];     /* Start point (ABS coordinates) */
    double      end[3];       /* End point (ABS coordinates) */
    double      unit[3];      /* Unit direction vector (ABS coordinates) */
};

typedef struct UF_EVAL_line_s UF_EVAL_line_t, *UF_EVAL_line_p_t;

struct UF_EVAL_arc_s
{
    logical     is_periodic;  /* Is the curve periodic or not? */
    double      limits[2];    /* Curve limits (in radians): [0] = min; [1] = max */
    double      radius;       /* Radius */
    double      center[3];    /* Center (ABS coordinates) */
    double      x_axis[3];    /* Unit direction vector of the x axis (ABS) */
    double      y_axis[3];    /* Unit direction vector of the y axis (ABS) */
};

typedef struct UF_EVAL_arc_s UF_EVAL_arc_t, *UF_EVAL_arc_p_t;

struct UF_EVAL_ellipse_s
{
    logical     is_periodic;  /* Is the curve periodic or not? */
    double      limits[2];    /* Curve limits: [0] = min; [1] = max */
    double      minor;        /* Minor radius */
    double      major;        /* Major radius */
    double      center[3];    /* Center (ABS coordinates) */
    double      x_axis[3];    /* Unit direction vector of the x axis (ABS) */
    double      y_axis[3];    /* Unit direction vector of the y axis (ABS) */
};

typedef struct UF_EVAL_ellipse_s UF_EVAL_ellipse_t, *UF_EVAL_ellipse_p_t;

struct UF_EVAL_parabola_s
{
    double      limits[2];    /* Curve limits: [0] = min [1] = max */
    double      k1;           /* Conic coefficient */
    double      center[3];    /* Center (ABS coordinates) */
    double      x_axis[3];    /* Unit direction vector of the x axis (ABS) */
    double      y_axis[3];    /* Unit direction vector of the y axis (ABS) */
};

typedef struct UF_EVAL_parabola_s UF_EVAL_parabola_t, *UF_EVAL_parabola_p_t;

struct UF_EVAL_hyperbola_s
{
    double      limits[2];    /* Curve limits: [0] = min [1] = max */
    double      k1;           /* First coefficient for evaluating hyperbola */
    double      k2;           /* Second coefficient for evaluating hyperbola
                           Note that the limits and k1,k2 are values used for
                           efficient evaluation of the hyperbola and are
                           not the same as the start/end parameters and k1,k2
                           of UF_CURVE_ask_conic_data.  
                        */
    double      center[3];    /* Center (ABS coordinates) */
    double      x_axis[3];    /* Unit direction vector of the x axis (ABS) */
    double      y_axis[3];    /* Unit direction vector of the y axis (ABS) */
};

typedef struct UF_EVAL_hyperbola_s UF_EVAL_hyperbola_t, *UF_EVAL_hyperbola_p_t;

struct UF_EVAL_spline_s
{
    logical     is_periodic;  /* Is the curve periodic or not? */
    logical     is_rational;  /* Is the spline rational or not? */
    int         order;        /* Order of the spline */
    int         num_knots;    /* Number of knot values (double) */
    int         num_control;  /* Number of control vertices (PNT4_t) */
};

typedef struct UF_EVAL_spline_s UF_EVAL_spline_t, *UF_EVAL_spline_p_t;

/*******************************************************************************
Initialize an evaluator structure.

Returns a pointer to the evaluator of a curve or edge. The evaluator
can be used to find points, derivatives and vectors of a curve or edge
at a given parameter value.  No longer use
UF_CURVE_ask_curve_struct ( ),
UF_CURVE_ask_curve_struct_data ( ) and
UF_CURVE_free_curve_struct ( ).

Note that this API will approximate procedurally created edges (such as 
edges created by intersecting two surfaces) with a spline to the current 
Modeling distance tolerance. 

Environment: Internal  and  External

See Also:  UF_EVAL_initialize_2
 UF_EVAL_free

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_initialize
(
    tag_t        tag,      /* <I>
                           Object identifier of a curve or edge
                           */
    UF_EVAL_p_t *evaluator /* <OF,free:UF_EVAL_free>
                           Evaluator structure for this curve.  It must be
                           freed by calling UF_EVAL_free.
                           */
);

/*******************************************************************************
Initialize an evaluator structure.

Returns a pointer to the evaluator of a curve or edge. The evaluator
can be used to find points, derivatives and vectors of a curve or edge
at a given parameter value.  No longer use
UF_CURVE_ask_curve_struct ( ),
UF_CURVE_ask_curve_struct_data ( ) and
UF_CURVE_free_curve_struct ( ).

This API will not approximate procedurally created edges.

Environment: Internal  and  External

See Also:  UF_EVAL_initialize
 UF_EVAL_free

History: Originally released in NX7.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_initialize_2
(
    tag_t        tag,      /* <I>
                           Object identifier of a curve or edge
                           */
    UF_EVAL_p_t *evaluator /* <OF,free:UF_EVAL_free>
                           Evaluator structure for this curve.  It must be
                           freed by calling UF_EVAL_free.
                           */
);

/*******************************************************************************
Copies the evaluator of an curve or edge.
Return copy of evaluator structure.

Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_free

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_copy
(
    UF_EVAL_p_t  evaluator,     /* <I>
                                Evaluator structure to copy
                                */
    UF_EVAL_p_t *evaluator_copy /* <OF,free:UF_EVAL_free>
                                Copy of the evaluator structure.  This must
                                be freed by calling UF_EVAL_free.
                                */
);

/*******************************************************************************
Returns the curve limits of the evaluator of a curve or edge.

Environment: Internal  and  External

See Also:  UF_EVAL_initialize

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_ask_limits
(
    UF_EVAL_p_t evaluator, /* <I>
                           evaluator structure
                           */
    double      limits[2]  /* <O>
                           limits
                           */
);

/*******************************************************************************
Query if the input curve is periodic.
Determines if the evaluator is from a periodic curve or edge.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_is_periodic
(
    UF_EVAL_p_t  evaluator,  /* <I>
                             evaluator structure for the curve.
                             */
    logical     *is_periodic /* <O>
                             TRUE if the curve is periodic, else FALSE
                             */
);

/*******************************************************************************
Evaluates a point or the derivatives of an evaluator of a curve or edge

Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_ask_limits

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_evaluate
(
    UF_EVAL_p_t  evaluator,     /* <I>
                                Evaluator structure for the curve.
                                */
    int          n_derivatives, /* <I>
                                number of derivative vectors
                                */
    double       parm,          /* <I>
                                Parameter to evaluate the curve at.  This
                                parameter is not normalized.  The parameter
                                limits for a given curve can be found by calling
                                UF_EVAL_ask_limits.
                                */
    double       point[3],      /* <O>
                                point on curve
                                */
    double      derivatives[]    /* <O,len:3*n_derivatives>
                                Derivative vectors on the curve.  The caller
                                is responsible for providing space to return
                                3*n_derivatives real numbers.
                                */
);

/*******************************************************************************
Evaluates a point or the unit vectors of an evaluator of a curve or edge.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_ask_limits

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_evaluate_unit_vectors
(
    UF_EVAL_p_t evaluator,  /* <I>
                            The evaluator structure for the curve.
                            */
    double      parm,       /* <I>
                            The parameter to evaluate at.  Note that the
                            parameter is not normalized.  You can get the
                            parameters for the given evaluator structure
                            by calling UF_EVAL_ask_limits.
                            */
    double      point[3],   /* <O>
                            The point on the curve
                            */
    double      tangent[3], /* <O>
                            The tangent to the curve at that point.
                            */
    double      normal[3],  /* <O>
                            The normal to the curve at that point.
                            */
    double      binormal[3] /* <O>
                            The binormal to the curve at that point.
                            */
);

/*******************************************************************************
Returns the closest parameter point on the curve or edge given a
specified reference point.  Note that parameters returned are not
normalized.

Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_ask_limits
 UF_MODL_ask_point_along_curve_2 -- Handles curves with sharp corners better

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_evaluate_closest_point
(
    UF_EVAL_p_t   evaluator,          /* <I>
                                      The evaluator structure of the curve.
                                      */
    const double  reference_point[3], /* <I>
                                      The reference point
                                      */
    double       *parm,               /* <O>
                                      The parameter of the closest point on
                                      the curve to the reference point.  This
                                      parameter is not normalized.
                                      */
    double        closest_point[3]    /* <O>
                                      The closest point on the curve to the
                                      reference point.
                                      */
);

/*******************************************************************************
Determines if two evaluators are equal. This implies that the curve(s)
and/or edge(s) are equal.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_is_equal
(
    UF_EVAL_p_t  evaluator1, /* <I>
                             evaluator structure for the first curve
                             */
    UF_EVAL_p_t  evaluator2, /* <I>
                             evaluator structure for the second curve
                             */
    logical     *is_equal    /* <O>
                             TRUE if the curves are equal, else FALSE
                             */
);

/******************************************************************************
Determines if the evaluator is from a linear curve or edge.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_ask_line

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_is_line
(
    UF_EVAL_p_t  evaluator, /* <I>
                            The evaluator structure of the curve.
                            */
    logical     *is_line    /* <O>
                            TRUE if this is a line, else FALSE
                            */
);

/******************************************************************************
Determines if the given evaluator is from a circular curve or edge.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_ask_arc

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_is_arc
(
    UF_EVAL_p_t  evaluator, /* <I>
                            evaluator structure of the curve
                            */
    logical     *is_arc     /* <O>
                            TRUE if this is an arc, else FALSE
                            */
);

/*******************************************************************************
Determines if the evaluator is from an elliptical curve or edge
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_ask_ellipse

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_is_ellipse
(
    UF_EVAL_p_t  evaluator, /* <I>
                            evaluator structure of the curve.
                            */
    logical     *is_ellipse /* <O>
                            TRUE if this is an ellipse, else FALSE
                            */
);

/*******************************************************************************
Determines if the evaluator is from a parabolic curve. There are no
parabolic edges in NX.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_ask_parabola

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_is_parabola
(
    UF_EVAL_p_t  evaluator,  /* <I>
                             evaluator structure of the curve
                             */
    logical     *is_parabola /* <O>
                             TRUE if the curve is a parabola, else FALSE
                             */
);

/*******************************************************************************
Determines if the evaluator is from a hyperbolic curve.  There are no
hyperbolic edges in NX.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_ask_hyperbola

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_is_hyperbola
(
    UF_EVAL_p_t  evaluator,   /* <I>
                              evaluator structure of the curve.
                              */
    logical     *is_hyperbola /* <O>
                              TRUE if the curve is a hyperbola, else FALSE
                              */
);

/*******************************************************************************
Determines if the evaluator is from a spline curve or edge.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_ask_spline
  UF_EVAL_ask_spline_control_pts
  UF_EVAL_ask_spline_knots

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_is_spline
(
    UF_EVAL_p_t  evaluator, /* <I>
                            evaluator structure of the curve
                            */
    logical     *is_spline  /* <O>
                            TRUE if the curve is a spline, else FALSE
                            */
);

/*******************************************************************************
Returns the line data of the evaluator of a linear curve or edge
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_is_line

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_ask_line
(
    UF_EVAL_p_t      evaluator, /* <I>
                                evaluator structure of the curve.  This must
                                be a line, or an error will be returned.
                                */
    UF_EVAL_line_p_t line       /* <O>
                                The data for this line.
                                */
);

/*******************************************************************************
Returns the arc data of the evaluator of a circular curve or edge.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_is_arc

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_ask_arc
(
    UF_EVAL_p_t     evaluator, /* <I>
                               evaluator structure for the curve.  This must
                               be an arc, or an error will be returned.
                               */
    UF_EVAL_arc_p_t arc        /* <O>
                               arc data
                               */
);

/*******************************************************************************
Returns the ellipse data of the evaluator of an elliptical curve or
edge.

Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_is_ellipse

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_ask_ellipse
(
    UF_EVAL_p_t         evaluator, /* <I>
                                   evaluator structure for the curve.  This must
                                   be an ellipse, or an error will be returned.
                                   */
    UF_EVAL_ellipse_p_t ellipse    /* <O>
                                   ellipse data
                                   */
);

/*******************************************************************************
Returns the parabola data from the evaluator of a parabolic curve.
There are no parabolic edges in NX.

Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_is_parabola


History: Originally released in V15.0
******************************************************************************/
extern UFUNEXPORT int UF_EVAL_ask_parabola
(
    UF_EVAL_p_t          evaluator, /* <I>
                                    evaluator structure for the curve.  This 
                                    must be a parabola, or an error will be 
                                    returned.
                                    */
    UF_EVAL_parabola_p_t parabola   /* <O>
                                    parabola data
                                    */
);

/*******************************************************************************
Returns the hyperbola data of the evaluator of a hyperbolic curve.
There are no hyperbolic edges in NX.

Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_is_hyperbola


History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_ask_hyperbola
(
    UF_EVAL_p_t           evaluator, /* <I>
                                     evaluator structure for the curve.  This 
                                     must be a hyperbola, or an error will be 
                                     returned.
                                     */
    UF_EVAL_hyperbola_p_t hyperbola  /* <O>
                                     hyperbola data
                                     */
);

/*******************************************************************************
Returns the spline data of the evaluator of a spline curve or edge
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_is_spline
  UF_EVAL_ask_spline_control_pts
  UF_EVAL_ask_spline_knots

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_ask_spline
(
    UF_EVAL_p_t        evaluator, /* <I>
                                  evaluator structure for the curve.  This must
                                  be a spline, or an error will be returned.
                                  */
    UF_EVAL_spline_p_t spline     /* <O>
                                  spline data
                                  */
);
/*******************************************************************************
Returns the spline knots of the evaluator of a spline curve or edge.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_is_spline
  UF_EVAL_ask_spline
  UF_EVAL_ask_spline_control_pts

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_ask_spline_knots
(
    UF_EVAL_p_t   evaluator, /* <I>
                             evaluator structure for the curve.  This must
                             be a spline, or an error will be returned.
                             */
    int          *n_knots,   /* <O>
                             count of knots in sequence
                             */
    double      **knots      /* <OF,len:n_knots>
                             knot sequence points, the parameter values for
                             each knot point in the spline.  This array must
                             be freed by calling UF_free.  These parameters
                             are not normalized.
                             */
);

/*******************************************************************************
Returns the spline control points of the evaluator of a spline curve or
edge.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_is_spline
  UF_EVAL_ask_spline
  UF_EVAL_ask_spline_knots

History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_ask_spline_control_pts
(
    UF_EVAL_p_t   evaluator, /* <I>
                             evaluator structure for the curve.  This must
                             be a spline, or an error will be returned.
                             */
    int          *n_points,  /* <O>
                             count of control points
                             */
    double      **points     /* <OF,len:n_points*4>
                             For each control point, four values are returned,
                             ( wx, wy, xz, w ).  This array must be freed by
                             calling UF_free.
                             */
);

/*******************************************************************************
Frees the evaluator of a curve or edge.
Environment: Internal  and  External

See Also:  UF_EVAL_initialize
  UF_EVAL_copy


History: Originally released in V15.0
*******************************************************************************/
extern UFUNEXPORT int UF_EVAL_free
(
    UF_EVAL_p_t evaluator /* <I>
                          evalauator structure to be freed
                          */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_EVAL_H_INCLUDED */
