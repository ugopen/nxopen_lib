/*******************************************************************************
             Copyright (c) 1998-2006 UGS Corp.
                       Unpublished - All Rights Reserved



File Description:

This file provides routines that enable you to manipulate points and curves.
Using the subroutines in this file, you can:
 . Get the data of an arc with respect to the coordinate system the arc is in.
 . Get the coordinates of a line with respect to the absolute coordinate system.
 . Get the structure pointer corresponding to the specified curve id.
 . Get the curve type and data for a specified curve structure.
 . Free the curve structure pointer.
 . Create an arc.
 . Create a fillet between the specified curves.
 . Create a line.
 . Create a new spline curve.

Documentation for UF_STRING_p_t and UF_STRING_t can be found in the NX Open
Reference Manual under uf_modl -> Types ->  string_list.


******************************************************************************/

#ifndef UF_CURVE_INCLUDED
#define UF_CURVE_INCLUDED

#include <uf_defs.h>
#include <libufun_exports.h>
#include <uf_cfi.h>
/*****************************************************************************

 *****************************************************************************/

#define ERROR_UF_CURVE_base    1480000
#include <uf_modl_types.h>

#define UF_CURVE_NOT_A_POINT_TAG    (ERROR_UF_CURVE_base)
#define UF_CURVE_NOT_A_LINE_TAG     (ERROR_UF_CURVE_base + 1)
#define UF_CURVE_NOT_AN_ARC_TAG     (ERROR_UF_CURVE_base + 2)
#define UF_CURVE_NOT_A_MATRIX_TAG   (ERROR_UF_CURVE_base + 3)
#define UF_CURVE_ANGLES_EXCEED_2PI  (ERROR_UF_CURVE_base + 4)
#define UF_CURVE_START_EXCEEDS_END  (ERROR_UF_CURVE_base + 5)
#define UF_CURVE_NOT_A_CONIC_TAG        (ERROR_UF_CURVE_base + 6)
#define UF_CURVE_NOT_A_CONIC        (ERROR_UF_CURVE_base + 7)
#define UF_CURVE_ANGLE_INVALID      (ERROR_UF_CURVE_base + 8)
#define UF_CURVE_ENDPOINTS_Z_DIFFERENT  (ERROR_UF_CURVE_base + 9)
#define UF_CURVE_INVALID_SUBTYPE    (ERROR_UF_CURVE_base + 10)
#define UF_CURVE_NOT_A_SPLINE_TAG       (ERROR_UF_CURVE_base + 11)
#define UF_CURVE_SPLINE_ILLEGAL_DATA    (ERROR_UF_CURVE_base + 12)
#define UF_CURVE_SPLINE_DEGENERATE      (ERROR_UF_CURVE_base + 13)
#define UF_CURVE_SPLINE_WEIGHT_NONPOS   (ERROR_UF_CURVE_base + 14)
#define UF_CURVE_SPLINE_CANT_CREATE     (ERROR_UF_CURVE_base + 15)
#define UF_CURVE_AMBIGUOUS_ENDS         (ERROR_UF_CURVE_base + 16)
#define UF_CURVE_TRIM_MULT_PTS          (ERROR_UF_CURVE_base + 17)
#define UF_CURVE_CONT_ORDER_ILLEGAL     (ERROR_UF_CURVE_base + 18)
#define UF_CURVE_CANT_EVAL_FIXED_LENGTH (ERROR_UF_CURVE_base + 19)

#ifdef __cplusplus
extern "C" {
#endif

#define UF_CURVE_2_CURVE                  0   /* UF_CURVE_create_fillet */
#define UF_CURVE_3_CURVE                  1   /* UF_CURVE_create_fillet */

#define UF_CURVE_TANGENT_OUTSIDE          0   /* UF_CURVE_create_fillet */
#define UF_CURVE_FILLET_IN_CIRCLE         1   /* UF_CURVE_create_fillet */
#define UF_CURVE_CIRCLE_IN_FILLET         2   /* UF_CURVE_create_fillet */


#define UF_CURVE_NATURAL_SHAPE         0   /* UF_CURVE_EDIT_TRIM_CURVE */
#define UF_CURVE_LINEAR_SHAPE          1   /* UF_CURVE_EDIT_TRIM_CURVE */
#define UF_CURVE_CIRCULAR_SHAPE        2   /* UF_CURVE_EDIT_TRIM_CURVE */

#define UF_CURVE_TANGENT               0   /* UF_CURVE_create_bridge_curve */
#define UF_CURVE_CURVATURE             1   /* UF_CURVE_create_bridge_curve */

#define UF_CURVE_SLOPE_NONE            -1  /* UF_CURVE_ASK_SPLINE_THRU_PTS */
#define UF_CURVE_SLOPE_AUTO            0   /* UF_CURVE_ASK_SPLINE_THRU_PTS */
#define UF_CURVE_SLOPE_DIR             1   /* UF_CURVE_ASK_SPLN_BY_DEF_DATA */
#define UF_CURVE_SLOPE_VEC             2   /* UF_CURVE_ASK_SPLN_BY_DEF_DATA */

#define UF_CURVE_CRVATR_NONE           -1  /* UF_CURVE_CREATE_SPLINE_THRU_PTS */
#define UF_CURVE_CRVATR_AUTO_DIR       1   /* UF_CURVE_CREATE_SPLINE_THRU_PTS */
#define UF_CURVE_CRVATR_VEC            2   /* UF_CURVE_CREATE_SPLINE_THRU_PTS */

enum UF_MODL_units_e
{
   UF_MODL_UNITS_PART = 0, /* same as parts units */
   UF_MODL_INCH,           /* inches */
   UF_MODL_MMETER,         /*  millimeters */
   UF_MODL_CMETER,         /* centimeters */
   UF_MODL_METER           /*  meters */
} ;

typedef enum UF_MODL_units_e UF_MODL_units_t;

/* Type of curve projection
UF_CURVE_create/ask/edit_combine_curves */
enum UF_CURVE_direction_e
{
        UF_CURVE_ALONG_PLANAR_CURVE_NORMALS,
        UF_CURVE_ALONG_FIXED_VECTOR
};

typedef enum UF_CURVE_direction_e UF_CURVE_direction_t;

struct UF_CURVE_struct_s
{
    void    *crv_data;        /* A pointer to a void structure. This structure
                                 should be appropriately typecast to get the
                                 correct curve structure. The different curve
                                 structures are:
                                 POINT_DATA, LINE_DATA, ARC_DATA, CONIC_DATA
                                 or BEZ_DATA */
    int     crv_type;         /* Curve object type. Valid types are:
                                 UF_point_type
                                 UF_line_type
                                 UF_circle_type
                                 UF_conic_type
                                 UF_spline_type
                              */
    double  crv_t0;           /* the start parameter of the curve */
    double  crv_tscale;       /* Difference between the start and end
                                 parameters of the curve for example:
                                 tend = crv_t0 + crv_tscale
                              */
    int     curve_periodic;   /* Periodic flag for the curve
                                 0 = nonperiodic
                                 1 = periodic
                              */
} ;

typedef struct UF_CURVE_struct_s UF_CURVE_struct_t,
*UF_CURVE_struct_p_t;

/*
    */

/* 
 */

/**********************************************************
structure containing edit information passed to
UF_CURVE_edit_move_mult_points.

explanation:  start segment (SS) and end segment (ES)
remain fixed while the inner segment (IS) is moved by
defining the new location of its end points (e1,e2)

 SS         e1      IS      e2             ES
.....+......+...............+............+.... curve S(u)
     |      S(disp_par1)    S(disp_par2) |
     |                                   |
     S(lim_par1)                         S(lim_par2)

methods to define direction/distance for moving ei:

displace_methodj  direction           distance
j=1               curve normal at ei  distancei
j=2               vectori             distancei
j=3               new location defined by dir_pti
**************************************************************
Structure containing edit information

*/
struct  UF_CURVE_BCMMCP_s
{
    double lim_par1,          /* limit of start segment (SS) */
           lim_par2,          /* limit of end segment (ES) */
           disp_par1,         /* left limit of inner segment */
           disp_par2,         /* right limit of inner segment */
           distance1,         /* distance to move e1 needed depending on
                                 selected displace_method */
           distance2,         /* distance to move e2 needed depending on
                                 selected displace_method */
           vector1[3],        /* direction to move e1 needed depending on
                                 selected displace_method */
           vector2[3],        /* direction to move e2 needed depending on
                                 selected displace_method */
           dir_pt1[3],        /* new location for e1 needed depending on
                                 selected displace_method */
           dir_pt2[3];        /* new location for e2 needed depending on
                                 selected displace_method */

    int    displace_method1,  /* displacement method for e1 */
           displace_method2 ; /* displacement method for e2 */

                              /* ^ needed depending on selected
                              displace_method */
} ;

/*

*/


typedef struct  UF_CURVE_BCMMCP_s UF_CURVE_BCMMCP_t,
*UF_CURVE_BCMMCP_p_t;

/**********************************************************
structure containing output intersection information
for UF_CURVE_intersect.

Parameter values are in natural parameter space.
**************************************************************/
struct  UF_CURVE_intersect_info_s
{
    int type_of_intersection; /* type of intersection found
                                 = 0 -> none
                                 = 1 -> 3D intersection
                                 = 2 -> 2D intersection */
    double curve_point[3];    /* intersection point coordinates
                                 on curve */
    double curve_parm;        /* parameter value of intersection
                                 point on curve */
    double entity_parms[2];   /* parameter value(s) of intersection
                                 point on entity, both values
                                 are valid when the entity is a
                                 body or face, neither value is
                                 valid for a plane or datum plane,
                                 otherwise only the first value is
                                 used */
} ;

typedef struct UF_CURVE_intersect_info_s  UF_CURVE_intersect_info_t,
*UF_CURVE_intersect_info_p_t;

struct UF_CURVE_line_s {
    double      start_point [ 3 ];  /* line start point */
    double      end_point [ 3 ];    /* line end point */
} ;

typedef struct UF_CURVE_line_s UF_CURVE_line_t,
*UF_CURVE_line_p_t;

/*******************************************************************

The matrix tag defines the orientation of the arc. The arc center is
with respect to the origin (0,0,0) of the absolute coordinate system
using the orientation of the arcs matrix. If you have arc center
coordinates with respect to the absolute coordinate system you must
map the coordinates to the arcs CSYS and enter these mapped
coordinates into the arc_center[3] member field of the
UF_CURVE_arc_s structure. To obtain the mapped coordinates use
the following transformation mapping:

[X][T] = mapped coordinates

where you take the matrix multiplication of X and T. X is the vector
coordinates [x y z] that you wish to map, T is the orientation matrix
represented by matrix_tag. The results, mapped coordinates, are the
values to enter into arc_center[3]
To obtain an orientation (rotation) matrix rotated about an axis at a
specified angle use UF_MTX3_rotate_about_axis. To obtain the
product of a vector and matrix use UF_MTX3_vec_multiply. To create
the matrix and obtain its tag use UF_CSYS_create_matrix.


See the Matrices and Coordinate System (uf_csys.h)
for routines that you can use for getting the matrix_tag.
***************************************************************************/
struct UF_CURVE_arc_s {
    tag_t       matrix_tag;             /* matrix for the CSYS the arc is in */
    double      start_angle;            /* expressed in radians */
    double      end_angle;              /* expressed in radians */
    double      arc_center [ 3 ];       /* center of the arc */
    double      radius;                 /* radius of the arc */
} ;

typedef struct UF_CURVE_arc_s UF_CURVE_arc_t,
*UF_CURVE_arc_p_t;

/**********************************************************************

**********************************************************************
The matrix defines the orientation of the plane in which the conic lies,
in the same manner as the matrix for an arc. The X axis of the matrix
determines the orientation of angle zero.

A point on the conic (in the XY plane) is given by

   For ellipse:

    X = k1 * cos (t)
        Y = k2 * sin (t)

   For parabola:

    X = t**2 / k1
        Y = t

   For hyperbola:

    X = k1 / cos (t)
        Y = k2 * sin (t) / cos (t)

where t is the parameter value.

NOTE that for an ellipse, the parameter values are NOT angles.
For a given parameter value, t, the angle (in radians) is the inverse
tangent (arctan) of Y/X.  For angles between 0 and pi/2 the following
equation can be used to determine ellipse parameter values:

t = arctan( (k1 / k2) * tan(angle) )

This is a general function to compute the parameter when the angles are between
0 and 2pi range.

static void ConvertAngleToParamterForEllipse( double k1, //<I>
                                              double k2, //<I>
                                              double angle, //<I>
                                              double *tParameter //<O>paramter of angle)
{
   double  xx = k2 * cos (angle*DEGRA);
   double  yy = k1 * sin (angle*DEGRA);
    if( fabs(yy) > 1.0e-10 )
    {
        if( fabs(xx) > 1.0e-10)
        {
            *tParameter = atan(yy/xx);
            if( xx > 0.0 && yy < 0.0)
                *tParameter +=TWOPI;
            if( xx < 0.0 && yy < 0.0)
                *tParameter += PI;
            if( xx < 0.0 && yy > 0.0)
                *tParameter += PI;
        }
        else
        {
            *tParameter = PI/2.0;
            if(yy < 0.0)
                *tParameter = 3.0*PI/2.0;
        }
    }
    else
    {
        *tParameter = 0.0;
        if(xx < 0)
            *tParameter = PI;
    }
}

*****************************************************************/
struct UF_CURVE_conic_s {
    tag_t matrix_tag;       /* tag of defining matrix for conic */
    int conic_type;     /* subtype: see uf_object_types.h */
    double rotation_angle;  /* angle of rotation of conic X from matrix X */
    double start_param;     /* start parameter value */
    double end_param;       /* end parameter value */
    double center [ 3 ];    /* center of conic */
    double k1;          /* first shape parameter */
    double k2;          /* second shape parameter */
} ;

typedef struct UF_CURVE_conic_s UF_CURVE_conic_t,
*UF_CURVE_conic_p_t;

/*****************************************************************
The matrix defines the orientation of the plane in which the conic lies,
in the same manner as the matrix for an arc. The X axis of the matrix
determines the orientation of angle zero. The type of the conic must
be determined from the coefficients. The points select the branch of
the hyperbola and determine the parameterization sense.
*****************************************************************/
struct UF_CURVE_genconic_s {
    tag_t matrix_tag;       /* tag of matrix defining orientation, or
                                   construction space*/
    double coefficients [ 6 ];  /* the coefficients of the conic in general
                                   form, a through f*/
    double start_pt [ 3 ];  /* starting point, in construction space */
    double end_pt [ 3 ];    /* ending point, in construction space */
} ;

typedef struct UF_CURVE_genconic_s UF_CURVE_genconic_t,
*UF_CURVE_genconic_p_t;

enum UF_CURVE_join_types
{
    UF_CURVE_NO_JOIN = 0,       /*  Don't join the curves */
    UF_CURVE_CUBIC_JOIN,        /*  Create a cubic polynomial join curve  */
    UF_CURVE_GENERAL_JOIN,      /*  Create a general spline join curve  */
    UF_CURVE_QUINTIC_JOIN       /*  Create a quintic polynomial join curve  */
};
typedef enum UF_CURVE_join_types UF_CURVE_join_type_t;

/*
 * UF_MODL_curve_fit_data = UF_CURVE_curve_fit_data
 */
struct UF_MODL_curve_fit_data_s
{
    int curve_fit_method;   /* curve fit method 0=cubic, 1=quintic, 2=advanced */
    int maximum_degree;     /* maximum degree */
    int maximum_segments;   /* maximum number of segments */

};
typedef struct UF_MODL_curve_fit_data_s
               UF_MODL_curve_fit_data, UF_CURVE_curve_fit_data;

struct UF_CURVE_proj_s
{
        int             proj_type;   /*  Projection type:
                                         1 - along face normals,
                                         2 - towards point,
                                         3 - along vector,
                                         4 - at angle to vector
                                         5 - toward a line
                                         6 - equal arclength        */
        tag_t           proj_pnt;     /*  Point eid for type 2 or 6,
                                          Line or datum axis eid for
                                          type 5                    */
        double          proj_vec[3];  /*  Vector for types 3,4,6    */
        double          x_vector[3];  /*  X axis vector for type 6  */
        int             multiplicity; /*  Multiplicity for type 3
                                          1 - Single direction
                                          2 - Both directions       */
        int             arcl_option;  /*  Equal Arclength option for type 6
                                          0 - Both X and Y
                                          1 - First X, Then Y
                                          2 - First Y, Then X
                                          3 - X Only
                                          4 - Y Only              */
        double          angle;        /*  Angle for type 4          */
        double          ref_pnt[3];   /*  Reference point for type 4 */
} ;

typedef struct UF_CURVE_proj_s UF_CURVE_proj_t,
*UF_CURVE_proj_p_t;

struct UF_CURVE_proj1_s
{
        UF_CURVE_proj_t proj_data;    /*  UF_CURVE_proj_s data */
        tag_t           proj_vector;  /*  Vector tag for types 3,4,6,
                                          if proj_vector is not NULL_TAG,
                                          proj_vec array will not be used */
        tag_t           x_vector_tag; /*  X axis vector tag for type 6
                                          if x_vector_tag is not NULL_TAG,
                                          x_vector array will not be used */
        UF_CURVE_join_type_t join_type; /* Join option for the projected curves */
        UF_CURVE_curve_fit_data curve_fit_data; /* curve fit method, max degree & max segments */
} ;

typedef struct UF_CURVE_proj1_s UF_CURVE_proj1_t,
*UF_CURVE_proj1_p_t;


/* The following has been made a union to allow for additional direction
 *  types in the future without having to change the interface.
 */
union UF_CURVE_direction_struct_u
{
    double       vector[3];    /* projection vector for along fixed vector */
};

typedef union UF_CURVE_direction_struct_u UF_CURVE_direction_struct_u,
*UF_CURVE_direction_struct_p_u;

struct UF_CURVE_combine_curves_direction_s
{
    UF_CURVE_direction_t direction_type; /* type of projection.
                                            UF_CURVE_ALONG_PLANAR_CURVE_NORMALS
                                            UF_CURVE_ALONG_FIXED_VECTOR
                                         */
    UF_CURVE_direction_struct_u direction_struct; /* Additional information
                                            required based on the direction
                                            type.  If direction type is
                                            UF_CURVE_ALONG_FIXED_VECTOR then
                                            this structure is the 3D
                                            projection vector.
                                         */
};
typedef struct UF_CURVE_combine_curves_direction_s
UF_CURVE_combine_curves_direction_t,
*UF_CURVE_combine_curves_direction_p_t;

struct  UF_CURVE_fit_error_s
{
    double      max_error;
    double      avg_error;
    int         point_with_max_error;
    int         interpolated;
};
typedef struct  UF_CURVE_fit_error_s
                UF_CURVE_fit_error_t, *UF_CURVE_fit_error_p_t;

/***********************************************************************
Interactive NX creates degree three splines by assigning  auto
slopes at the start and end points, if you do not specify slopes yourself.
To replicate the creation of these interactive splines using
UF_CURVE_create_spline_thru_pts you need to specify AUTO slopes for the first
and last points and NONE for the rest.  The following notes apply to the fields
of this data structure:

1.  The explanation of four slope types specified in the above table is
    as follows:

    . UF_CURVE_SLOPE_NONE means that no slope is assigned
      at an input point during the interpolation process. The slope at
      the point is whatever the interpolator calculates when it solves
      the system of equations to compute the spline.

    . UF_CURVE_SLOPE_AUTO means that the slope is
      internally calculated from the data points specified before the
      interpolation is done. The system uses the data points and
      slopes surrounding the current point to arrive at reasonable
      values. These values are then used during the interpolation.

    . UF_CURVE_SLOPE_VEC signifies that the slope is defined
      by the user-specified defining slope vector, whose magnitude
      and direction affect the shape of the curve.


    . UF_CURVE_SLOPE_DIR is the same as the
      UF_CURVE_SLOPE_VEC, except that only the direction of
      the slope affects the shape of the curve.

2.  The explanation of three curvature types specified in the above
      table is as follows:

    . UF_CURVE_CRVATR_NONE means that no curvature is
      assigned at an input point during the interpolation process.
      The curvature at the point is whatever the interpolator
      calculates when it solves the system of equations to compute
      the spline.

    . UF_CURVE_CRVATR_AUTO_DIR means that only the
      magnitude of the curvature vector is used as the curvatures
      magnitude. Its direction is internally determined by NX before
      the interpolation is done. Notice that the corresponding slope
      type must be UF_CURVE_SLOPE_AUTO at the point.

    . UF_CURVE_CRVATR_VEC signifies that the curvature is
      defined by the user-specified defining curvature vector, whose
      magnitude and direction affect the shape of the curve.

3.  Curvature vector must be orthogonal to the slope vector.

4.  Curvature can be specified in the following two ways:

    . When the slope type is UF_CURVE_SLOPE_VEC or
      UF_CURVE_SLOPE_DIR, the curvature vector is used to
      determine its direction and magnitude.

    . When the slope type is UF_CURVE_SLOPE_AUTO, only the
      magnitude of the curvature vector is used as the curvatures
      magnitude. The direction of the curvature and slope are
      determined internally by NX.

5.  Assigning slopes is not allowed on splines with degree less than 2.

6.  Assigning curvature is not allowed on splines with degree less
    than 3.
***********************************************************************/
struct UF_CURVE_pt_slope_crvatr_s
{
    double     point[3];           /* 3D coordinates of input ordered
                                      points. For creating periodic curves,
                                      you should not repeat the first point
                                      as the last point
                                   */
    int        slope_type;         /* type of control being defined:
                                      UF_CURVE_SLOPE_NONE,
                                      UF_CURVE_SLOPE_AUTO,
                                      UF_CURVE_SLOPE_VEC,
                                      UF_CURVE_SLOPE_DIR
                                      (see Note 1)
                                   */
    double     slope[3];           /* 3D vector defining the slope assigned
                                      at this input point (see Note 1, 4, 5)
                                   */
    int        crvatr_type;        /* type of control being defined
                                      UF_CURVE_CRVATR_NONE,
                                      UF_CURVE_CRVATR_AUTO_DIR,
                                      UF_CURVE_CRVATR_VEC
                                      (see Note 2)
                                   */
    double     crvatr[3];          /*3D vector defining the curvature assigned
                                     at this input point (see Note 2, 3, 6)
                                   */
};

typedef struct UF_CURVE_pt_slope_crvatr_s UF_CURVE_pt_slope_crvatr_t,
*UF_CURVE_pt_slope_crvatr_p_t;

enum UF_CURVE_wrap_type_e
{
    UF_CURVE_WRAP,   /* Indicates that the curves are to be wrapped from
                        the Wrap Plane onto the Wrap Face */
    UF_CURVE_UNWRAP  /* Indicates that the curves are to be unwrapped from
                        the Wrap Face onto the Wrap Plane. */
};

typedef enum UF_CURVE_wrap_type_e UF_CURVE_wrap_type_t,
*UF_CURVE_wrap_type_p_t;

struct UF_CURVE_wrap_data_s
{
    UF_CURVE_wrap_type_t  wrap_unwrap_sw;   /* Object type: UF_CURVE_WRAP
                                               or UF_CURVE_UNWRAP */
    int                   num_wrap_faces;   /* Number of tags in the
                                               wrap_faces array */
    tag_t                 *wrap_faces;      /* <len:num_wrap_faces> Conical or cylindrical faces to
                                               wrap onto/unwrap from
                                               (If multiple faces, they must
                                                be on the same cone/cylinder.
                                            */
    tag_t                 wrap_plane;       /* Datum plane or face to wrap
                                               from/ unwrap onto. Must be
                                               tangent to the wrap_face. */
    int                   num_input_curves; /* Number of tags in the
                                               input_curves array. */
    tag_t                 *input_curves;    /* <len:num_input_curves>
                                               Object Identifiers of curves,
                                               edges, faces (same as reference
                                               to the edges of the face).
                                               Curves to be wrapped/unwrapped.*/
    char                  *cut_line_angle;  /* Expression specifying the cut
                                               line angle, relative to the
                                               tangent line, in degrees
                                               0 - 360. */
    double                distance_tol;     /* Distance tolerance to use in
                                               calculations e.g. to decide
                                               if an output curve should be
                                               closed.*/
    double                angle_tol;        /* Angle tolerance to use in curve
                                               fitting */
};

typedef struct UF_CURVE_wrap_data_s UF_CURVE_wrap_data_t,
*UF_CURVE_wrap_data_p_t;

enum UF_CURVE_offset_type_e
{
    UF_CURVE_OFFSET_DISTANCE_NO_TRIM   = 1, /* This type will offset by a
                                            distance with no trimming/extending
                                            done to the offset curves */
    UF_CURVE_OFFSET_DISTANCE_FILLET,        /* This type will offset by a
                                            distance and trim/extend the
                                            offset curves to their intersection
                                             points using a fillet. The system
                                            constructs an arc tangent to the
                                            endpoint of each offset curve. The
                                            radius of the arc is equal to the
                                            offset distance. */
    UF_CURVE_OFFSET_DISTANCE_TANGENT,       /* This type will offset by a
                                            distance and extend/trim the
                                            offset curves to their intersection
                                             points. The amount of extension
                                            is unlimited. */
    UF_CURVE_OFFSET_DISTANCE_LIMITED_TANGENT,/*This type will offset by a
                                             distance and extend/trim the
                                             offset curves to their
                                             intersection points. The amount
                                             of extension is limited to the
                                             extension factor. */
    UF_CURVE_OFFSET_DRAFT_NO_TRIM,           /* This type will offset
                                             according to draft height and
                                             angle values with no trimming/
                                             extending done to the offset
                                             curves. */
    UF_CURVE_OFFSET_DRAFT_FILLET,            /* This type will offset according
                                              to draft height and angle values
                                             and trim/extend the offset curves
                                             to their intersection points using
                                              a fillet.  The system constructs
                                             an arc tangent to the endpoint of
                                             each offset curve. The radius of
                                             the arc is equal to the offset
                                             distance. */
    UF_CURVE_OFFSET_DRAFT_TANGENT,           /* This type will offset
                                             according to draft height and
                                             angle values and extend/trim the
                                             offset curves to their
                                             intersection points. The amount
                                             of extension is unlimited. */
    UF_CURVE_OFFSET_DRAFT_LIMITED_TANGENT,   /* This type will offset according
                                             to draft height and angle values
                                             and extend/trim the offset curves
                                             to their intersection points. The
                                             amount of extension is limited to
                                             the extension factor. */
    UF_CURVE_OFFSET_3D_AXIAL                /* This type will offset a 3d axial
                                            distance.
                                            The 3d axial offset corresponds to
                                            the intersection of an extrusion of
                                            the curves in the axial direction
                                            with a tube generated by the curves
                                            and having radius = axial distance */
};

typedef enum UF_CURVE_offset_type_e UF_CURVE_offset_type_t,
*UF_CURVE_offset_type_p_t;

/* The following structure holds data that is specific to the
     UF_CURVE_OFFSET_DISTANCE_NO_TRIM,
     UF_CURVE_OFFSET_DISTANCE_FILLET, and
     UF_CURVE_OFFSET_DISTANCE_TANGENT types of offset curve.
*/
struct UF_CURVE_offset_distance_data_s
{
    char     *distance;   /* Distance to offset input_curves string */
    int      rough_type ; /*  1 for rough type, 0 otherwise
                              rough_type = 1 will produce a spline or
                              splines that approximate the offset curve(s).
                              The approximation may not be as accurate as
                              for the regular offset, but should be faster.
                                                                   */
};
typedef struct UF_CURVE_offset_distance_data_s
UF_CURVE_offset_distance_data_t,
*UF_CURVE_offset_distance_data_p_t;

struct UF_CURVE_offset_distance_tangent_data_s
{
    char              *distance; /* Distance to offset input_curves string */
    double     extension_factor; /* Controls the length of the offset
                                    tangent extension lines.  The amount
                                    of extension at each end of an offset
                                    curve depends upon the extension factor
                                    used. The extension factor is a
                                    multiple of the offset distance. */
    int      rough_type ; /*  1 for rough type, 0 otherwise
                              rough_type = 1 will produce a spline or
                              splines that approximate the offset curve(s).
                              The approximation may not be as accurate as
                              for the regular offset, but should be faster.
                                                                   */

};
typedef struct UF_CURVE_offset_distance_tangent_data_s
UF_CURVE_offset_distance_tangent_data_t,
*UF_CURVE_offset_distance_tangent_data_p_t;

struct UF_CURVE_offset_draft_data_s
{
    char           *draft_height; /* Distance between the plane of the input
                                     curves (reference plane) to the plane of
                                     the offset curves (offset plane) */

    char           *draft_angle;  /* The angle from the offset vector to a line
                                     perpendicular to the reference plane. */
    int      rough_type ; /*  1 for rough type, 0 otherwise
                              rough_type = 1 will produce a spline or
                              splines that approximate the offset curve(s).
                              The approximation may not be as accurate as
                              for the regular offset, but should be faster.
                                                                   */

};
typedef struct UF_CURVE_offset_draft_data_s UF_CURVE_offset_draft_data_t,
*UF_CURVE_offset_draft_data_p_t;

struct UF_CURVE_offset_draft_tangent_data_s
{
    char           *draft_height; /* Distance between the plane of the input
                                     curves (reference plane) to the plane of
                                     the offset curves (offset plane) */
    char           *draft_angle;  /* The angle from the offset vector to a line
                                     perpendicular to the reference plane. */
    double         extension_factor; /* Controls the length of the offset
                                        tangent extension lines.  The amount
                                        of extension at each end of an offset
                                        curve depends upon the extension factor
                                        used. The extension factor is a
                                        multiple of the offset distance. */
    int      rough_type ; /*  1 for rough type, 0 otherwise
                              rough_type = 1 will produce a spline or
                              splines that approximate the offset curve(s).
                              The approximation may not be as accurate as
                              for the regular offset, but should be faster.
                                                                   */
};
typedef struct UF_CURVE_offset_draft_tangent_data_s
UF_CURVE_offset_draft_tangent_data_t,
*UF_CURVE_offset_draft_tangent_data_p_t;

/* The following structure holds data that is specific to the
     UF_CURVE_OFFSET_3D_AXIAL type of offset curve.
*/
struct UF_CURVE_offset_axial_data_s
{
    char     * offset_value ;    /* 3d distance to offset input_curves string */
    tag_t     axis_vector ;  /* Smart vector defining the direction of offset */
};
typedef struct UF_CURVE_offset_axial_data_s
UF_CURVE_offset_axial_data_t,
*UF_CURVE_offset_axial_data_p_t;

union UF_CURVE_offset_def_u
{
   UF_CURVE_offset_distance_data_t         *distance_type1;
   UF_CURVE_offset_distance_tangent_data_t *distance_type2;
   UF_CURVE_offset_draft_data_t            *draft_type1;
   UF_CURVE_offset_draft_tangent_data_t    *draft_type2;
   UF_CURVE_offset_axial_data_t              * axial_type ;
};
typedef union UF_CURVE_offset_def_u UF_CURVE_offset_def_t;

struct UF_CURVE_offset_data_s
{
    UF_STRING_p_t        input_curves;   /* Pointer to curves list structure (AKA string_list)
                                            Use UF_MODL_init_string_list and
                                             UF_MODL_create_string_list to
                                             create input strings. Use
                                             UF_MODL_free_string_list to free
                                             memory after the string is created.
                                             Documentation for UF_STRING_p_t and UF_STRING_t can be found in the NX Open
                                             Reference Manual under uf_modl -> Types ->  string_list.

                                           */
    double             approximation_tolerance; /* Step value which controls
                                                   the accuracy of the offset
                                                   curve
                                                */
    double                    string_tolerance; /* Controls the distance
                                                   determining if two curves
                                                   are close enough to be
                                                   considered contiguous.
                                                */

    UF_CURVE_offset_type_t offset_type;
    UF_CURVE_offset_def_t offset_def;
};
typedef struct UF_CURVE_offset_data_s UF_CURVE_offset_data_t,
*UF_CURVE_offset_data_p_t;


/***************************************************************************
  Enumeration fields for different types of offset methods for creating an
  associated offset curve on face.  There are four types of methods for
  creating an offset curve in an associated offset curve on face feature.
  These methods are used for calculating different types of offset distances
  based on the input offset value.
 ***************************************************************************/
enum UF_CURVE_ocf_method_e
{
    UF_CURVE_OCF_CHORDAL=0,     /* This type will offset the string based on
                                   the chordal distance
                                 */
    UF_CURVE_OCF_ARCLENGTH,     /* This type will offset the string based on
                                   the arc length
                                 */
    UF_CURVE_OCF_GEODESIC,      /* This type will offset the string based on
                                   the geodesic method, i.e. the curve is
                                   offset along the minimum distance on the
                                   input faces
                                 */
    UF_CURVE_OCF_TANGENTIAL     /* This type will offset the string in
                                   tangential direction and then and then
                                   project it back on to the faces */
};
typedef enum UF_CURVE_ocf_method_e UF_CURVE_ocf_method_t;

/***************************************************************************
  Enumeration fields for different types of trimming methods for offset
  curves in an associated offset curve on face.
  There are  two types of trimming methods for creating offset curve(s) in
  an associated offset curve on face feature.
  These methods are used for trimming the offset curves from a string.
 ***************************************************************************/
enum UF_CURVE_ocf_trim_method_e
{
   UF_CURVE_OCF_NO_EXTENSION=0, /* This type will prevent a corner being
                                   created between the offset curves
                                 */
   UF_CURVE_OCF_TANGENT         /* This type will create a corner between the
                                   offset curves along their tangents
                                 */

};
typedef enum UF_CURVE_ocf_trim_method_e UF_CURVE_ocf_trim_method_t;

/***************************************************************************
  Enumeration fields for different types of spanning methods for offset
  curves in an associated offset curve on face.
  There are  two types of spanning methods for creating offset curve(s) in
  an associated offset curve on face feature.
  The spanning method is used to control the extent to which an offset curve
  is created in case there is a gap between the offset curve and the face
  boundary.
 ***************************************************************************/
enum UF_CURVE_ocf_span_method_e
{
    UF_CURVE_OCF_SPAN_NONE = 0,  /* This type will prevent the offset curves
                                    from being extended to the boundary
                                  */
    UF_CURVE_OCF_SPAN_QUILT      /* This type will result in the offset curves
                                    being extended to the boundary
                                  */
};
typedef enum UF_CURVE_ocf_span_method_e UF_CURVE_ocf_span_method_t;

/***************************************************************************
  Enumeration fields for different types of boundary methods for offset
  curves in an associated offset curve on face.
  There are  two types of boundary methods for creating offset curve(s) in
  an associated offset curve on face feature.
  The boundary method is used to control the offset curves in case the offset
  curves are crossing the boundary of the input faces for offset.
 ***************************************************************************/
enum UF_CURVE_ocf_cross_boundaries_e
{
    UF_CURVE_OCF_CROSS_BOUNDARIES_NONE = 0,    /* This type prevents from the
                                                  offset curves from crossing
                                                  the boundary of the input of
                                                  faces
                                                */
    UF_CURVE_OCF_CROSS_BOUNDARIES              /* This type allows the offset
                                                  curves to cross the boundary
                                                  of the input faces
                                                */
};
typedef enum UF_CURVE_ocf_cross_boundaries_e UF_CURVE_ocf_cross_boundaries_t;


/***************************************************************************
 Structure that holds the offset value for a given string in an associated
 offset curve in face feature.  The offset value is stored as a string.
 ***************************************************************************/
struct UF_CURVE_ocf_values_s
{
    char   string[ MAX_FSPEC_BUFSIZE ];   /* A character string used to
                                                   hold an offset value in
                                                   form of a string (e.g "2.0")
                                                   to offset the string on the
                                                   input set of faces. 
                                                 */
};
typedef struct UF_CURVE_ocf_values_s
               UF_CURVE_ocf_values_t, *UF_CURVE_ocf_values_p_t;

/***************************************************************************
 Structure that holds identifier for a face collector.  The face collector
 has all the faces that need to be input for an associated offset curve on
 face feature.
 ***************************************************************************/
struct UF_CURVE_ocf_face_data_s {
    tag_t    face_tag;            /* Holds the tag to a face collector that
                                     has to be created for all faces on which
                                     the strings have to be offset.  All
                                     types of face collectors can be created
                                   */

};
typedef  struct UF_CURVE_ocf_face_data_s
                UF_CURVE_ocf_face_data_t, *UF_CURVE_ocf_face_data_p_t;

/***************************************************************************
 Structure that holds the string identifier for the string that has to be
 offset in an associated offset curves on face feature.  The structure also
 holds the offset direction on the string, the number of offsets desired
 along with the offset distances for each offset desired.
 ***************************************************************************/
struct UF_CURVE_ocf_string_data_s {
    tag_t                           string_tag;     /* Tag of the string to
                                                       offset
                                                     */
    int                             offset_direction; /* Flag to indicate the
                                                         offset direction.
                                                         The direction can be
                                                         either 1 or -1
                                                        */
    int                             num_offsets;      /* Number of offsets to
                                                         perform for the given
                                                         string
                                                       */
    UF_CURVE_ocf_values_p_t         offset_distances; /* <len:num_offsets>
                                                         An array that holds
                                                         the offset values for
                                                         each of the offset
                                                         to perform for the
                                                         given string
                                                       */
};
typedef struct UF_CURVE_ocf_string_data_s
               UF_CURVE_ocf_string_data_t, *UF_CURVE_ocf_string_data_p_t;


/***************************************************************************
 The main structure for the associated offset curve on face feature.
 This structure holds an allocated array of UF_CURVE_ocf_string_data_t
 structures that have the data assocated with a string, the number of offsets
 desired and the offset distances.

 This structure also holds a UF_CURVE_ocf_face_data_t pointer that has the
 face collector identifier.

 The offset method, trim method, span method and the cross boundary method
 is also stored in this structure along with the distance, angular and string
 tolerances.

 This structure has to be allocated and filled with values during create
 or has to be allocated and queried from an existing associated offset curves
 in face feature, modified to set new offset distances/string/types and then
 invoke edit to reflect the changes.
 ***************************************************************************/
struct UF_CURVE_ocf_data_s {

    UF_CURVE_ocf_string_data_p_t      string_data;    /* <len:num_string_data>
                                                         An array of strings to
                                                         be offset and the
                                                         data associated with
                                                         them, as described in
                                                         above string data
                                                         structure
                                                       */
    int                               num_string_data; /* Size of the string
                                                          array
                                                        */
    UF_CURVE_ocf_face_data_p_t        face_data;       /* Face data */
    UF_CURVE_ocf_cross_boundaries_t   cross_boundary_mode; /* boundary mode
                                                              method
                                                            */
    UF_CURVE_ocf_method_t             offset_method;       /* offset type
                                                              method
                                                            */
    UF_CURVE_ocf_trim_method_t        trim_method;         /* Trimming options
                                                              for offset
                                                            */
    UF_CURVE_ocf_span_method_t        span_method;         /* spanning options
                                                              for offset
                                                            */
    double                            dist_tol;            /* distance
                                                              tolerance
                                                            */
    double                            ang_tol;             /* angular
                                                              tolerance
                                                            */
    double                            string_tol;          /* string
                                                              tolerance
                                                            */
};
typedef struct UF_CURVE_ocf_data_s
               UF_CURVE_ocf_data_t , *UF_CURVE_ocf_data_p_t;

/*****************************************************************************
The following codes always appear fixed:
    UF_CURVE_STATE_CLOSED
    UF_CURVE_STATE_PERIODIC
    UF_CURVE_STATE_UNNORMALIZED
    UF_CURVE_STATE_CLAMPED

The following codes can never appear fixed:
    UF_CURVE_STATE_NOT_TRIMMED
****************************************************************************/

/***************************************************************************

 ****************************************************************************/

#define UF_CURVE_STATE_RANGE_START      50
#define UF_CURVE_STATE_CLOSED       50   /* always appears fixed */
#define UF_CURVE_STATE_PERIODIC     51   /* always appears fixed */
#define UF_CURVE_STATE_UNNORMALIZED 52   /* always appears fixed */
#define UF_CURVE_STATE_CLAMPED          53   /* always appears fixed */
#define UF_CURVE_STATE_DEGENERACY       55
#define UF_CURVE_STATE_G1_DISCONTINUITY 56
#define UF_CURVE_STATE_SMOOTHED_TO_CN   57
#define UF_CURVE_STATE_KNOT_NONC0       58
#define UF_CURVE_STATE_KNOT_MULT        59
#define UF_CURVE_STATE_KNOT_DECREASING  60
#define UF_CURVE_STATE_KNOT_TOOCLOSE    61
#define UF_CURVE_STATE_NOT_TRIMMED  62  /* can never appear fixed */
                                        /* 64 is reserved for a bsurface code */
#define UF_CURVE_STATE_RANGE_END    99  /* can never appear */

/* the following values are identical to those in uf_modl.h
   the analagous names are UF_MODL for UF_CURVE */
#define UF_CURVE_OPEN_CURVE                0 /* UF_CURVE_ask_parameterization */
#define UF_CURVE_CLOSED_PERIODIC_CURVE     1 /* UF_CURVE_ask_parameterization */
#define UF_CURVE_CLOSED_NON_PERIODIC_CURVE 2 /* UF_CURVE_ask_parameterization */

/* the following values are identical to those in uf_modl.h
   the analagous names are UF_MODL for UF_CURVE */
#define UF_CURVE_LOC                 0   /* UF_CURVE_evaluate_curve and UF_CURVE_evaluate_curve_structure */
#define UF_CURVE_LOC_1STDERV         1   /* UF_CURVE_evaluate_curve and UF_CURVE_evaluate_curve_structure */
#define UF_CURVE_LOC_1STDERV_2NDDERV 2   /* UF_CURVE_evaluate_curve and UF_CURVE_evaluate_curve_structure */

#ifndef UF_CURVE_STATE_DEFINED
#define UF_CURVE_STATE_DEFINED

/* Contains data indicating the situation found in a spline curve or
surface. The same structure is used to return states for fixing and smoothing
b-spline curves and surfaces.  The following states are returned for b-spline
curves, with the noted state value contents.

UF_CURVE_STATE_DEGENERACY - a degeneracy was detected in the spline or
                            bsurface flag&2 indicates U(0) or V(1) for a
                            bsurface.  flag&1 indicates if fixed (1 indicates
                            fixed). value is a point on or near the degeneracy
UF_CURVE_STATE_G1_DISCONTINUITY - the spline or bsurface is not G1 continuous
                                  flag&2 indicates U(0) or V(1) for a bsurface
                                  flag&1 indicates if smoothed to G1 (1 indicates
                                  smoothed to G1) flag&4 indicates if smoothed to Cn
                                  (1 indicates smoothed to Cn).  value[0] indicates the
                                  knot value at the discontinuity
UF_CURVE_STATE_KNOT_NONC0 - the spline or bsurface is not C0 continuous, that
                            is, it has a gap. flag&2 indicates U(0) or V(1) for
                            a bsurface.  flag&1 indicates if fixed (1
                            indicates fixed; shape change incurred).  value[0]
                            indicates the knot value at the discontinuity.
UF_CURVE_STATE_KNOT_MULT - the spline or bsurface has an illegal knot
                           multiplicity but without a gap.  flag&2
                           indicates U(0) or V(1) for a bsurface.
                           flag&1 indicates if fixed (1 indicates fixed)
                           value[0] indicates the knot value in the illegal
                           multiplicity
UF_CURVE_STATE_KNOT_DECREASING - the spline or bsurface has a knot value that
                                 is less than the value preceding it in
                                 the knot vector.  flag&2 indicates U(0) or
                                 V(1) for a bsurface.  flag&1 indicates if
                                 fixed (1 indicates fixed).  value[0] indicates
                                 the first knot value of the decreasing series
UF_CURVE_STATE_CLOSED - the spline or bsurface is closed but not Cn
                        flag&2 indicates U(0) or V(1) for a bsurface
UF_CURVE_STATE_PERIODIC - the spline or bsurface is closed and Cn at the
                          closure.  flag&2 indicates U(0) or V(1) for a
                          bsurface.
UF_CURVE_STATE_KNOT_TOOCLOSE - the spline or bsurface has a knot value that is
                               too close to the knot preceding it in the knot
                               vector.  flag&2 indicates U(0) or V(1) for a
                               bsurface.  flag&1 indicates if fixed (1
                               indicates fixed).  value[0] indicates the first
                               knot value that is too close to its preceding
                               knot
UF_CURVE_STATE_NOT_TRIMMED - the spline was not trimmed to the parameter values
                             given.  flag&2 indicates U(0) or V(1) for a
                             bsurface.
UF_CURVE_STATE_KNOTS_UNNORMALIZED - the splines or bsurfaces knots were
                                    normalized to meet Open API requirements
                                    flag&2 indicates U(0) or V(1) for a bsurface
                                    value[0] contains the factor for converting
                                    spline data parameters to values suitable
                                    for using with the NX object. Let
                                    td be a parameter value in the range defined
                                    by the spline data.  Let t0 be the
                                    corresponding parameter value to use when
                                    evaluating the NX spline. Then
                                      t0 = td*v0 + v1
                                    Apply to both directions of a bsurface as
                                    needed.
UF_CURVE_STATE_CLAMPED - the spline or bsurface end knots are of
                         multiplicity order. value[0] indicates the knot
                         value, value[1] contains the minimum distance change,
                         value[2] indicates the maximum angle change.
UF_CURVE_STATE_SMOOTHED_TO_CN - the spline or bsurface is not G1 continuous
                                and has been smoothed. For further definition
                                of the structure values see UF_CURVE_STATE_G1_DISCONTINUITY.
*/
struct UF_CURVE_state_s {
    int     state_code; /* Code giving the state found at the given place.
                           Depending on the code, the next two values will
                           contain different values.
                        */
    int     flag;      /* This is a bit field that stores information about
                          the given state code.  The interpretation of these
                          bits depends on the state code, and is given in
                          the structure comments.
                       */
    double  value[3];  /* This is an array that holds values that pertain to
                          the given state code.  Each state code stores
                          different values in this array.  See the comments
                          on the different states for how to interpret these
                          values.
                       */
};
typedef struct UF_CURVE_state_s UF_CURVE_state_t, *UF_CURVE_state_p_t;
#endif

#define UF_CURVE_STATE_IS_FIXED(x) ((x)&1) /* returns nonzero when state
                                              is marked fixed */

/*********************************************************************
Contains data defining a non-uniform rational b-spline (NURBS)
curve.  All data items are used in both input and output.
There are 4 values for each control point, or pole: wx (poles[i][0]), wy
(poles[i][1]), wz (poles[i][2]) and w (poles[i][3]) (0<= i < num_poles)
Note that the first 3 coordinates are weighted.
The number of knots num_knots and poles num_poles and the order order,
 are related as follows: num_knots = num_poles+order.

The *_param values specify how much of the spline is active, i.e.,
visible and used.  They cannot be outside the parameter range defined
by the knot vector.  The lowest allowed value is ps = knots[order-1],
where [i] denotes the C-language (zero-based) subscript.  The
largest is pe = knots[num_poles].

If is_rational is nonzero, the weights are not all equal to 1.0.  To
create a spline, this value is ignored and the rational status is
determined from the data.

For more information on the conditions spline data must meet, see
UF_CURVE_create_spline.
**************************************************************/
struct UF_CURVE_spline_s {
    int     num_poles;        /* number of poles */
    int     order;            /* order of the spline (degree +1) */
    int     is_rational;      /* 1 if it is a rational spline */
    double  *knots;           /* pointer to the array of knots */
    double  (*poles)[4];      /* pointer to the array of poles */
    double  start_param;      /* start parameter */
    double  end_param;        /* end parameter */
} ;

typedef struct UF_CURVE_spline_s UF_CURVE_spline_t,
*UF_CURVE_spline_p_t;

/* Methods for Bridge Curve creation */
enum UF_CURVE_bridge_method_e
{
   UF_CURVE_match_tangent_ends,   /* Tangent Continuous, shape controlled at
                                     end points. */
   UF_CURVE_match_tangent_peak,   /* Tangent Continuous, shape controlled at
                                     peak points. */
   UF_CURVE_match_curvature_ends, /* Curvature Continuous, shape controlled at
                                     end points. */
   UF_CURVE_match_curvature_peak, /* Curvature Continuous, shape controlled at
                                     peak points. */
   UF_CURVE_inherit_shape,       /* Shape controlled by input reference curve.*/
   UF_CURVE_tangent_conic        /* Tangent Continuous, conic curve.*/
};
typedef enum UF_CURVE_bridge_method_e UF_CURVE_bridge_method_t;


/* Main structure for bridge curve data.
The member elements method, input_curve1, input_curve2 and match_point
are required for all bridge types.
The members reverse_tangents, shape_control1 and shape_control2
are required for all except UF_CURVE_inherit_shape and UF_CURVE_tangent_conic.
The member shape_control1 is used for UF_CURVES_tangent_conic.
The member stiffness_method is used for UF_CURVES_match_curvature_peak only.
The member inherit_curve is used for UF_CURVE_inherit_shape method only.
Documentation for UF_STRING_p_t and UF_STRING_t can be found in the NX Open
Reference Manual under uf_modl -> Types ->  string_list.

*/
struct UF_CURVE_bridge_data_s
{
   UF_CURVE_bridge_method_t method; /* creation method */
   UF_STRING_p_t input_curve1;      /* First input string, must contain only one
                                       curve or edge.  Use
                                       UF_MODL_init_string_list and
                                       UF_MODL_create_string_list to
                                       create input strings. Use
                                       UF_MODL_free_string_list to free
                                       memory after the string is created.
                                       */
   UF_STRING_p_t input_curve2;      /* Second input string, must contain only
                                       one curve or edge.  Use
                                       UF_MODL_init_string_list and
                                       UF_MODL_create_string_list to
                                       create input strings. Use
                                       UF_MODL_free_string_list to free
                                       memory after the string is created.  */
   char *matchpt_parms[2];          /* Location parameter on input strings,
                                       used as a percentage along the string,
                                       must be an expression or a number between
                                       0.0 and 100.0 */
   tag_t match_point[2];            /* Location reference points (optional) */
   logical reverse_tangents[2];     /* True= Reverse Tangents,
                                       False = Dont Reverse Tangents */
   char *shape_control1;            /* Shape Control
                                       For UF_CURVE_match_*_ends: Tangent
                                       magnitude at first input curve, must be
                                       an expression or a number greater than
                                       0.0.  For UF_CURVE_match_*_peak:
                                       Controls depth at peak point, must be an
                                       expression or a number between  0.0 and
                                       100.0. For UF_CURVE_tangent_conic:
                                       Controls the rho value, must be an
                                       expression or a number between 0.0 and
                                       1.0 */
   char *shape_control2;            /* Shape Control
                                       For UF_CURVE_match_*_ends: Tangent
                                       magnatude at second input curve, must be
                                       an expression or a number greater than
                                       0.0 For UF_CURVE_match_*_peak: Controls
                                       skew at peak point, must be an expression
                                       or a number between  0.0 and 100.0 */
   int stiffness_method;            /* Controls (to some extent) the degree,
                                       continuity, and complexity of the curve
                                       0 = automatic
                                       1 = low
                                       2 = high */
   UF_STRING_p_t inherit_curve;     /* Reference shape string, must contain only
                                       one curve or edge.  Use
                                       UF_MODL_init_string_list and
                                       UF_MODL_create_string_list to
                                       create input strings. Use
                                       UF_MODL_free_string_list to free
                                       memory after the string is created.  */
};
typedef struct UF_CURVE_bridge_data_s UF_CURVE_bridge_data_t,
                                      *UF_CURVE_bridge_data_p_t;

/******************************************************************************
 * Ask curve fit data: curve fit method, maximum degree and
 * maximum number of segments from the modeling preferences
 *
 * Environment: Internal and External
 *
 * See Also:  UF_MODL_set_curve_fit_data
 *
 * History: This function is introduced in NX3.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_fit_data
(
 UF_MODL_curve_fit_data *curve_fit_data   /* <O> curve fit method, maximum degree, and maximum segments */
);

/******************************************************************************
 * Set curve fit data: curve fit method, maximum degree and
 * maximum number of segments to the modeling preferences
 *
 * Environment: Internal and External
 *
 * See Also:  UF_MODL_ask_curve_fit_data
 *
 * History: This function is introduced in NX3.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_curve_fit_data
(
 UF_MODL_curve_fit_data curve_fit_data   /* <I> curve fit method, maximum degree, and maximum segments */
);

struct UF_CURVE_section_general_data_s
{
      tag_t  *objects;    /* <len:num_objects> Array of objects to be sectioned
                              (Bodies, faces, planes, curves) */
      int     num_objects; /* Number of objects */
      int     associate;   /* 1 for associative curves,
                              0 for non_associative curves (a group
                                 of curves is returned) */
      int     grouping;    /* 1 if the curves are to be grouped by plane,
                              0 otherwise
                              (ignored if associate is 1) */
      int     join_type;   /* 0 for no joining of the section curves,
                              1 if the curves are to be joined into
                                 cubic polynomial spline curves,
                              2 if the curves are to be joined into
                                 general spline curves,
                              3 if the curves are to be joined into
                                 quintic polynomial spline curves */
      double  tolerance;   /* tolerance (in part units) for the
                                section curves */
      UF_CURVE_curve_fit_data curve_fit_data; /* <I> curve fit method, max degree & max segments */

};
typedef struct UF_CURVE_section_general_data_s
               UF_CURVE_section_general_data_t, *UF_CURVE_section_general_data_p_t;

struct UF_CURVE_section_planes_data_s
{
      tag_t  *planes;      /* <len:num_planes> Array of sectioning planes and datum planes */
      int     num_planes;  /* Number of planes */

};
typedef struct UF_CURVE_section_planes_data_s
               UF_CURVE_section_planes_data_t, *UF_CURVE_section_planes_data_p_t;

struct UF_CURVE_section_parallel_data_s
{
      tag_t   base_plane;      /* Base plane */
      double  step_distance;   /* Step distance */
      double  start_distance;  /* Start distance */
      double  end_distance;    /* End distance */

};
typedef struct UF_CURVE_section_parallel_data_s
               UF_CURVE_section_parallel_data_t, *UF_CURVE_section_parallel_data_p_t;

struct UF_CURVE_section_radial_data_s
{
      tag_t   base_axis;      /* Smart axis for base plane */
      tag_t   base_point;     /* Smart point on base plane */
      double  step_angle;     /* Step angle */
      double  start_angle;    /* Start angle */
      double  end_angle;      /* End angle */

};
typedef struct UF_CURVE_section_radial_data_s
               UF_CURVE_section_radial_data_t, *UF_CURVE_section_radial_data_p_t;

struct UF_CURVE_section_perpcrv_data_s
{
      tag_t   curve_eid;      /* Curve eid */
      int     direction;      /* 1 if percentages are from start to end
                                     of the curve
                                -1 if opposite direction */
      int     space_meth;     /* 1 for equal parameter spacing,
                                 2 for geometric progression spacing,
                                 3 for chordal tolerance spacing,
                                 4 for incremental arclength spacing */
      int     num_points;     /* Number of points on the curve */
      double  start_pct;      /* Start percentage on the curve
                                   (see direction) */
      double  end_pct;        /* End percentage on the curve
                                   (see direction) */
      double  ratio;          /* Ratio for geometric progression spacing */
      double  chord_tol;      /* Tolerance for chordal toleraance spacing */
      double  increment;      /* Increment for incremental arclength spacing */

};
typedef struct UF_CURVE_section_perpcrv_data_s
               UF_CURVE_section_perpcrv_data_t, *UF_CURVE_section_perpcrv_data_p_t;


#ifndef RATIONAL_UNKNOWN
#define RATIONAL_UNKNOWN    -1
#define RATIONAL_YES        TRUE
#define RATIONAL_NO     FALSE
#endif

/*
  This enum is used to define spline extension options, type of trim desired,
  and end of strings to trim/extend.
 */
enum UF_CURVE_trim_opts_e
{
    UF_CURVE_EXTEND_NATURAL,
    UF_CURVE_EXTEND_LINEAR,
    UF_CURVE_EXTEND_CIRCULAR,
    UF_CURVE_EXTEND_NONE,
    UF_CURVE_TRIM_TO_ONE_BOUND,
    UF_CURVE_TRIM_TO_TWO_BOUND,
    UF_CURVE_TRIM_TO_TOTAL_LENGTH,
    UF_CURVE_TRIM_TO_INCR_LENGTH,
    UF_CURVE_TRIM_OUTSIDE,
    UF_CURVE_TRIM_INSIDE,
    UF_CURVE_TRIM_EXTEND_START,
    UF_CURVE_TRIM_EXTEND_END
};
typedef enum UF_CURVE_trim_opts_e UF_CURVE_trim_opts_t;

/*
  The following structure is returned from UF_CURVE_create_trim if multiple
  intersection points were found between the bounding object and the string
  being trimmed.
 */
struct UF_CURVE_trim_mult_s
{
    int      num_bound1_pts;                  /* The number of points in
                                                 following array.
                                              */

    double   *bound1_pts;                     /* <len:num_bound1_pts * 3>
                                                 The intersection points of
                                                 boundary 1, or the single
                                                 boundary, and the string
                                                 being trimmed. The caller
                                                 must free this array.  The
                                                 array is [num_bound1_pts * 3]
                                                 long.
                                               */

    int      num_bound2_pts;                  /* The number of points in
                                                 following array.
                                              */

    double   *bound2_pts;                     /* <len:num_bound2_pts * 3>
                                                 The intersection points of
                                                 boundary 2 and the string
                                                 being trimmed. The caller
                                                 must free this array. The
                                                 array is [num_bound2_pts * 3]
                                                 long.
                                              */
};
typedef struct UF_CURVE_trim_mult_s UF_CURVE_trim_mult_t,
*UF_CURVE_trim_mult_p_t;

/*
  The following structure is used to define the bounding object.
 */
struct UF_CURVE_trim_bound_s
{
    UF_STRING_t      string; /* The string to trim at. This can contain a
                                mixture of curves, edges, features, sketches,
                                and faces. If features are included then the
                                curves produced by that feature are input as
                                the string to trim or bounding string. If
                                sketches are included then the curves in the
                                sketch are input as the string to trim or the
                                bounding string. If faces are included the
                                edges of the faces are input as the string to
                                trim or the bounding string.

                                If trimming to an object, then the num field in
                                this structure should be set to 0. Note that
                                the field dir in the string structure indicates
                                which end of the bounding string should be
                                trimmed or extended.
                             */

    tag_t            object;             /* The object to trim at. This object
                                            can be a face, point, datum plane,
                                            or datum axis. If trimming to a
                                            string then this should be set to
                                            NULL_TAG.
                                         */

    logical          use_suggested;      /* Indication if the following point
                                            should be used to select between
                                            multiple intersection points.
                                         */

    double           suggested_point[3];  /* The point that is used to select
                                             one of multiple intersection
                                             points.  The intersection point
                                             closest to this point will be used.
                                          */

};
typedef struct UF_CURVE_trim_bound_s UF_CURVE_trim_bound_t,
*UF_CURVE_trim_bound_p_t;

/* Structure to use to define the trim desired when the
   trim_type == UF_CURVE_TRIM_TO_ONE_BOUND
*/

struct UF_CURVE_trim_one_bound_s
{
    UF_CURVE_trim_opts_t  string_trim_extend_end; /* Indication of which end
                                                     of the string should be
                                                     trimmed or extended to the
                                                     bounding object, this
                                                     should be set to one of
                                                     the following values:
                                                     UF_CURVE_TRIM_EXTEND_START
                                                     UF_CURVE_TRIM_EXTEND_END
                                                     
                                                  */

    UF_CURVE_trim_bound_t bound;                  /* The bounding definition.*/

    logical               trim_bound;             /* Indication of whether the
                                                     bounding string should be
                                                     trimmed or not.
                                                  */

    UF_MODL_vector_p_t    view;                   /* Vector defining viewing
                                                     direction in which to
                                                     measure minimum distance.
                                                     If vector is defined with
                                                     a datum axis, the feature
                                                     will be associated to the
                                                     datum axis.
                                                     If vector is defined using
                                                     plane of curves option,
                                                     curves do not need to be
                                                     supplied in vector
                                                     structure, the bounding
                                                     object strings and string
                                                     being trimmed will
                                                     determine plane.
                                                     If (void *)0 then minimum
                                                     distance will be measured
                                                     3 dimensionally.
                                                  */
};
typedef struct UF_CURVE_trim_one_bound_s UF_CURVE_trim_one_bound_t;

/* use the following structure when trim_type == UF_CURVE_TRIM_TO_TWO_BOUND */

struct  UF_CURVE_trim_two_bound_s
{
    UF_CURVE_trim_opts_t  string_extend_end;      /* Indication of which end
                                                     of the string should be
                                                     extended to bounding
                                                     object 1. The other end
                                                     of the string will be
                                                     extended to bounding
                                                     object 2. This should be
                                                     set to one of the
                                                     following values:

                                                     UF_CURVE_TRIM_EXTEND_START
                                                     UF_CURVE_TRIM_EXTEND_END
                                                 */

  UF_CURVE_trim_opts_t  string_trim_option;     /* Indication of which portion
                                                    of the string should be
                                                    trimmed away, this should
                                                    be set to one of the
                                                    following values:

                                                     UF_CURVE_TRIM_OUTSIDE
                                                     UF_CURVE_TRIM_INSIDE */

                                          /*
                                                     
                                                 */

   UF_CURVE_trim_bound_t bound1;                 /* The bounding definition for
                                                    boundary 1.
                                                 */


   UF_CURVE_trim_bound_t bound2;                 /* The bounding definition for
                                                    boundary 2.
                                                 */
   logical               trim_bound;             /* Indication of whether the
                                                    bounding strings should be
                                                    trimmed or not.
                                                 */
   UF_MODL_vector_p_t    view;                   /* Vector defining viewing
                                                    direction in which to
                                                    measure minimum distance.
                                                    If vector is defined with a
                                                    datum axis, the feature
                                                    will be associated to the
                                                    datum axis. If vector is
                                                    defined using plane of
                                                    curves option, curves do
                                                    not need to be supplied in
                                                    vector structure, the
                                                    bounding object strings and
                                                     string being trimmed will
                                                    determine plane. If
                                                    (void *)0 then minimum
                                                    distance will be measured 3
                                                     dimensionally.
                                                  */

} ;
typedef struct UF_CURVE_trim_two_bound_s UF_CURVE_trim_two_bound_t;

/* use the following structure when
   trim_type == UF_CURVE_TRIM_TO_TOTAL_LENGTH */

struct UF_CURVE_trim_total_length_s
{
    UF_CURVE_trim_opts_t  string_trim_extend_end; /* Indication of which end of
                                                     the string should be
                                                     trimmed or extended to the
                                                     bounding object, this
                                                     should be set to one of
                                                     the following values:

                                                     UF_CURVE_TRIM_EXTEND_START
                                                     UF_CURVE_TRIM_EXTEND_END
                                                  */

    char value[ MAX_LINE_BUFSIZE ]; /* A character string containing the value to
                                    set the total length of the input string to.
                                    The string can be a numeric value (e.g.,
                                    "25"), a fully defined expression (e.g.,
                                    "p5  = 25"), an existing expression name
                                    (e.g., "p5"), or an expression string (e.g.,
                                    "p5+p7").  If the fully defined expression
                                    exists then an error is returned. If the
                                    expression name does not exist an error is
                                    returned. In all other cases an expression
                                    is created. When this value is returned
                                    from UF_CURVE_ask_trim, the character
                                    string is a fully defined expression
                                    (e.g., "p5=25").
                                 */

};

typedef struct UF_CURVE_trim_total_length_s UF_CURVE_trim_total_length_t;

/* use the following structure when
trim_type == UF_CURVE_TRIM_TO_INCR_LENGTH */

struct UF_CURVE_trim_incr_length_s
{
    UF_CURVE_trim_opts_t  string_trim_extend_end; /* Indication of which end of
                                                     the string should be
                                                     trimmed or extended to the
                                                     bounding object, this
                                                     should be set to one of
                                                     the following values:

                                                      UF_CURVE_TRIM_EXTEND_START
                                                      UF_CURVE_TRIM_EXTEND_END
                                                   */

    char value[ MAX_LINE_BUFSIZE ]; /* A character string containing the value to
                                    set the total length of the input string to.
                                    The string can be a numeric value (e.g.,
                                    "25"), a fully defined expression (e.g.,
                                    "p5  = 25"), an existing expression name
                                    (e.g., "p5"), or an expression string (e.g.,
                                    "p5+p7").  If the fully defined expression
                                    exists then an error is returned. If the
                                    expression name does not exist an error is
                                    returned. In all other cases an expression
                                    is created. When this value is returned
                                    from UF_CURVE_ask_trim, the character
                                    string is a fully defined expression
                                    (e.g., "p5=25").
                                 */

} ;

typedef struct UF_CURVE_trim_incr_length_s UF_CURVE_trim_incr_length_t;

union UF_CURVE_trim_to_u
{
    UF_CURVE_trim_one_bound_t     one_bound;
    UF_CURVE_trim_two_bound_t     two_bound;
    UF_CURVE_trim_total_length_t  total_length;
    UF_CURVE_trim_incr_length_t   incr_length;
};

typedef union UF_CURVE_trim_to_u UF_CURVE_trim_to_t;

/*************************************************************************
The following structure is the main structure used in the trim functions.
****************************************************************************/

struct UF_CURVE_trim_s
{
    UF_STRING_t string_to_trim; /* The string to trim.  This can be a
                                mixture of curves, edges, features, sketches,
                                and faces. If features are included then the
                                curves produced by that feature are input as
                                the string to trim or bounding string. If
                                sketches are included then the curves in the
                                sketch are input as the string to trim or the
                                bounding string. If faces are included the
                                edges of the faces are input as the string to
                                trim or the bounding string.
                                */

    UF_CURVE_trim_opts_t   spline_extend_opt;  /* The extension that will be
                                                  to splines in the string to
                                                  trim and the bounding string.
                                                  This should be set to one of
                                                  the following values:
                                                    UF_CURVE_EXTEND_NATURAL
                                                    UF_CURVE_EXTEND_LINEAR
                                                    UF_CURVE_EXTEND_CIRCULAR
                                                    UF_CURVE_EXTEND_NONE
                                               */

    UF_CURVE_trim_opts_t   trim_type;          /* Indication of which structure
                                                  within the union is being
                                                  used to define how to trim
                                                  the input string, this should
                                                  be set to one of the
                                                  following values:
                                                   UF_CURVE_TRIM_TO_ONE_BOUND
                                                   UF_CURVE_TRIM_TO_TWO_BOUND
                                                   UF_CURVE_TRIM_TO_TOTAL_LENGTH
                                                   UF_CURVE_TRIM_TO_INCR_LENGTH
                                               */

    double                 tolerances[2];      /* Tolerances used in string
                                                  processing.
                                                 [0] -> distance tolerance used
                                                        in determining
                                                        connected curves
                                                 [1] -> angle tolerance,
                                                        required but
                                                        not really utilized
                                               */

    UF_CURVE_trim_to_t     trim_to;
};

typedef struct UF_CURVE_trim_s UF_CURVE_trim_t, *UF_CURVE_trim_p_t;

/*
  This enum is used to specify the type of to be create.
 */
enum UF_CURVE_line_arc_type_e
{
    UF_CURVE_asso_none = -1, /* no asso type  */
    UF_CURVE_asso_line,      /* Create a line */
    UF_CURVE_asso_arc       /* Create a arc  */
};

typedef enum UF_CURVE_line_arc_type_e UF_CURVE_line_arc_type_t;

/*
  This enum is used to specify the type of constraint to be applied.
 */

enum UF_CURVE_asso_arc_subtype_e
{
    UF_CURVE_line_arc_three_point_arc = 0, /* 3 point arc   */
    UF_CURVE_asso_arc_from_center      /* arc from_center */

};

typedef enum UF_CURVE_asso_arc_subtype_e UF_CURVE_asso_arc_subtype_t;

/*
  This enum is used to specify the sub type of Arc .
 */


enum UF_CURVE_constraint_type_e
{
    UF_CURVE_constraint_none = -1,      /* no constraint defined */
    UF_CURVE_coincident,     /* Coincident with a point */
    UF_CURVE_tangent,        /* Tangent to a curve */
    UF_CURVE_normal,         /* Normal to a curve/Surface */
    UF_CURVE_angle,          /* At an angle to a linear entity */
    UF_CURVE_along_x,        /* Along the WCS X axis */
    UF_CURVE_along_y,        /* Along the WCS Y axis */
    UF_CURVE_along_z,        /* Along the WCS Z axis */
    UF_CURVE_radius          /* Specific radius for arc/circle */
};

typedef enum UF_CURVE_constraint_type_e UF_CURVE_constraint_type_t;

/*
 * This enum is for choice of principal axis
 */
enum UF_CURVE_principal_axis_e
{
    UF_CURVE_X_AXIS = 0,
    UF_CURVE_Y_AXIS,
    UF_CURVE_Z_AXIS
};
typedef enum UF_CURVE_principal_axis_e UF_CURVE_principal_axis_type_t;

/*
  This enum is used to specify the end of curve to which
  the constraint must be applied.
 */
enum UF_CURVE_end_type_e
{
    UF_CURVE_start = 0,     /* Apply to the start of curve */
    UF_CURVE_end,           /* Apply to the end of curve */
    UF_CURVE_middle,        /* Apply to the middle of arc */
    UF_CURVE_center         /* Apply to the center of arc */
};

typedef enum UF_CURVE_end_type_e UF_CURVE_end_type_t;

/*
  This enum is used to specify the type of limit to be applied.
 */
enum UF_CURVE_limit_type_e
{
    UF_CURVE_limit_to_constraint= 0, /* Limit upto the constrained object */
    UF_CURVE_limit_value,            /* Extend the end by a value*/
    UF_CURVE_limit_to_entity         /* Limit upto the specified object */
};

typedef enum UF_CURVE_limit_type_e UF_CURVE_limit_type_t;

/*
  This enum is used to specify the type of help data to be applied.
 */
enum UF_CURVE_help_data_type_e
{
    UF_CURVE_help_data_none = 0,
    UF_CURVE_help_data_parameter,    /* a parameter is supplied */
    UF_CURVE_help_data_value         /* coordinate of a point is supplied */
};

typedef enum UF_CURVE_help_data_type_e UF_CURVE_help_data_type_t;

/*************************************************************************
The following structure is the structure used define the help data for the
associative curves.
****************************************************************************/
struct UF_CURVE_help_data_s
{
    UF_CURVE_help_data_type_t    help_data_type;  /* Type of help data */
    double                        value[3];  /* Coordinate value of a point */
    double                        parameter;  /* Value of a point by parameter */
};

typedef struct UF_CURVE_help_data_s UF_CURVE_help_data_t, *UF_CURVE_help_data_p_t;

/**************************************************************************/


/*************************************************************************
The following structure is the structure used define the constraint
with which the associative curve must be created.
****************************************************************************/

struct UF_CURVE_constraint_s
{
    UF_CURVE_constraint_type_t    constraint_type;  /* The type of constraint */

    UF_CURVE_end_type_t            end_type;         /* The end to which this constraint
                                                   * must be applied.
                                                   */
    tag_t                        object_tag;       /* Object with which the constraint
                                                   * is to be applied.
                                                   */
    double                         value;            /* If constraint needs a value then
                                                   * use this field, ex. UF_CURVE_angle
                                                   * UF_CURVE_radius type constraints.
                                                   */
    UF_CURVE_help_data_t        help_data;        /* help data when constraint is tangent / normal */
} ;

typedef struct UF_CURVE_constraint_s UF_CURVE_constraint_t, *UF_CURVE_constraint_p_t;

/*************************************************************************
The following structure is the structure used define the limits of the
end of associative curves.
****************************************************************************/
struct UF_CURVE_limit_s
{
    UF_CURVE_limit_type_t        limit_type;  /* Type of limit */
    double                        value;       /* Value by which to extend
                                              * in case of UF_CURVE_limit_value.
                                              * In case of arc/circle the value
                                              * should be in degrees.
                                              */
    tag_t                       limiting_obj;  /* The object upto which the end must be extended, used when limit type is UF_CURVE_limit_to_entity. */
    UF_CURVE_help_data_t        help_data;    /* help data when limit type is UF_CURVE_limit_to_entity and there are multiple intersections of line/arc with limiting entity. */
};

typedef struct UF_CURVE_limit_s UF_CURVE_limit_t, *UF_CURVE_limit_p_t;

/****************************************************************************/


/*************************************************************************
The following structure is the main structure to create the associative
curve using the UF_CURVE_create_line_arc() and UF_SF_CURVE_create_line_arc interfaces.
****************************************************************************/
struct UF_CURVE_line_arc_s
{
    UF_CURVE_line_arc_type_t        curve_type;     /* Type of curve to create i.e. line/arc */
    UF_CURVE_asso_arc_subtype_t arc_constraint_subtype; /* The subtype of curve */
    UF_CURVE_constraint_t        constraints[3]; /* Array of constraint to be satisfied.
                                                 * Two constraints in case of line.
                                                 * Two constraints in case of arc by center.
                                                 * Three constraints in case of arc.
                                                 */
    UF_CURVE_limit_t             limits[2];      /* The start and end limits of the curve */
    tag_t                        plane_of_curve; /* Plane on which curve must lie.
                                                 * If NULL_TAG, plane will be infered.
                                                 * Else all the object in the constraints
                                                 * array above will be projected on the plane.
                                                 */
    logical                        complement;     /* False - Default arc will be created.
                                                 * True  - Complement of default arc will be created.
                                                 * Used only in ARC.
                                                 */
    logical                        closed;          /* False - Arc bounded by limits above will be created.
                                                 * True  - Full circle will be created.
                                                 * Used only in ARC.
                                                 */
    logical                     is_associative; /* true if associative, false if not associative */
};

typedef struct UF_CURVE_line_arc_s UF_CURVE_line_arc_t, *UF_CURVE_line_arc_p_t;

/*******************************************************************************
Creates a point in the absolute coordinate system.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_point(
double point_coords[3] ,/* <I>
                        Coordinates of point in absolute space
                        */
tag_t *point  /* <O>
               Object identifier of point
               */
);
/*****************************************************************************
Returns the coordinates for the specified object identifier of a point.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_point_data(
tag_t point ,/* <I>
             Object identifier of point to inquire about
             */
double point_coords[3]  /* <O>
                        Coordinates of point in absolute space
                        */
);
/******************************************************************************
Edits (changes) the coordinates of a point. You input the tag of the
point that you would like to edit, then pass in the new coordinate
values.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_point_data(
tag_t point ,/* <I>
             Object identifier of point to edit
             */
double point_coords[3]  /* <I>
                        Edited coordinates of point in absolute space
                        */
);
/******************************************************************************
Creates a line. You input the start and end points of the line by filling
out the line_coords data structure pointed to by UF_CURVE_line_p_t.

Environment: Internal  and  External

See Also:  UF_CURVE_line_p_t

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_line(
UF_CURVE_line_p_t line_coords ,/* <I>
                               Coordinates of line in absolute space
                               */
tag_t * line  /* <O>
              Object identifier Of new line
              */
);
/******************************************************************************
Returns the coordinates of a line with respect to the absolute
coordinate system.

Environment: Internal  and  External

See Also:  UF_CURVE_line_p_t

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_line_data(
tag_t line ,/* <I>
            Object identifier of line
            */
UF_CURVE_line_p_t line_coords  /* <O>
                               Coordinates of line in absolute space
                               */
);

/******************************************************************************
Edits (changes) the coordinates of a line. You input the tag of the
point that you would like to edit, then pass in the new coordinates
(start and end) to the line_coords data structure pointed to by
UF_CURVE_line_p_t

Environment: Internal  and  External

See Also:  UF_CURVE_line_p_t

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_line_data(
tag_t line ,/* <I>
            Object identifier of line to edit
            */
UF_CURVE_line_p_t line_coords  /* <I>
                               Edited coordinates of point in absolute space
                               */
);
/******************************************************************************
Creates an arc. You input the matrix tag, start and end angles in
radians, the coordinates of the arc center, and the radius by filling out
the arc_coords data structure pointed to by UF_CURVE_arc_p_t.
The arc is drawn counterclockwise from the start angle to the end angle

This function returns an error if the absolute value of the difference
between the start and end angle is greater than two pi (plus the system
tolerance). An error is also returned if the start angle is greater than
the end angle.

Environment: Internal  and  External

See Also:  UF_CURVE_arc_p_t

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc(
UF_CURVE_arc_p_t arc_coords ,/* <I>
                             Pointer to arc data structure
                             */
tag_t * arc  /* <O>
             Object identifier of new arc
             */
);
/******************************************************************************
Returns the data of an arc. The data is in the structure arc_coords
pointed to by UF_CURVE_arc_p_t and includes the matrix tag, start
and end angles (radian measure), the arc center coordinates, and the
arc radius.  Another function that provides arc data is UF_EVAL_ask_arc.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_arc_data(
tag_t arc ,/* <I>
           Object identifier of arc to query
           */
UF_CURVE_arc_p_t arc_coords  /* <O>
                             Data of arc in CSYS in which the arc resides.
                             */
);

/******************************************************************************
Edit an existing arc. You can edit (change) csys matrix, the start and
end angles, the coordinates of the arc center, and the radius by filling
out the arc_coords data structure pointed to by UF_CURVE_arc_p_t.
The arc is drawn counterclockwise from the start angle to the end
angle. The start and end angles are expressed in radians. This function
returns an error if the absolute value of the difference between the
start and end angle is greater than two pi (plus the system tolerance).
An error is also returned if the start angle is greater than the end
angle.

Environment: Internal  and  External

See Also:  UF_CURVE_arc_p_t

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_arc_data(
tag_t arc ,/* <I>
           Object identifier of existing arc to edit
           */
UF_CURVE_arc_p_t arc_coords  /* <I>
                             Edited coordinates of arc in absolute space
                             */
);
/******************************************************************************
Creates a conic curve. See the description of the data structure for
details on the interpretation of the data items.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0.
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_conic (
UF_CURVE_conic_p_t conic_data ,/* <I>
                               Data structure defining the conic to create
                               */
tag_t * conic  /* <O>
               Returned tag of curve
               */
);
/******************************************************************************
Reads the data from the conic arc and returns it in the data structure
provided.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_conic_data (
tag_t conic ,/* <I>
             tag of conic for which to obtain data
             */
UF_CURVE_conic_t * conic_data  /* <O>
                              pointer to a conic arc data structure to be filled
                              with the data for the conic arc
                               */
);

/**************************************************************************
Edits the defining data of a dumb conic. A dumb conic is no longer associative.

Environment: Internal & External

See Also:  UF_CURVE_ask_conic_data

History:  originally released in V15.0
*************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_conic_data
(
    tag_t conic,          /* <I> the dumb conic to edit */
    UF_CURVE_conic_p_t conic_data /* <I> defining data for the conic */
);
/*******************************************************************************
Converts general form conic data to standard form data.

The matrix for each form defines the orientation, or construction
space; the conic arc is parallel to its XY plane. The Z coordinate of
the center point gives the offset from the XY plane. The matrix for
the standard form is always the same as it was for the general form.
In the standard form, there is no way to specify the direction of
parameterization. The start and end points of the general form can
define a parameterization direction opposite that of the standard
form. When this is the case the sense argument is returned false.

For an ellipse, the process of extracting the angle of
rotation from the general form coefficients does not reliably yield the
same rotation angle with which it was created. The result may be a
parameterization in standard form between p and 3p. For this reason
many workers change the matrix of an ellipse (and possibly parabolas
and hyperbolas too) to incorporate the rotation angle and make the
conics rotation angle be zero. This produces a reliable
parameterization for the general form.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_convert_conic_to_std (
UF_CURVE_genconic_p_t gen_conic_data ,/* <I>
                                      Conic data in general form
                                      */
UF_CURVE_conic_t * conic_data ,/* <O>
                               Conic data in standard form
                               */
logical * sense  /* <O>
                 Sense of parameterization of the standard form with respect to
                 the general form. True if they are the same direction.
                 */
);

/******************************************************************************
The conic in standard form is converted to its general form. The
matrix of the general form is always the same as for the standard form.

Environment: Internal  and  External

See Also: UF_CURVE_ask_conic_data

History:Original release was in V13.0
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_convert_conic_to_gen (
UF_CURVE_conic_p_t conic_data ,/* <I>
                               Conic data in standard form
                               */
UF_CURVE_genconic_t * gen_conic_data  /* <O>
                                      Conic data in general form
                                      */
);

/******************************************************************************
Creates a spline curve from the input defining data specified by the
UF_CURVE_pt_slope_crvatr_s data structure (See the description of
the structure for a description of the data items). The spline passes
through the input points and conforms to the specified slopes and
curvatures.

The length of the array of parameters is num_points for non-periodic
curves and (num_points+1) for periodic ones. The difference with
periodic curves is that although we know the last point of the curve (it
is coincident with the first point), we dont know the parameter range
of the curve.  Therefore, you need to provide the parameter for the
last point (num_points +1) to specify the parameter range of the
curve.

Environment: Internal  and  External

See Also: UF_CURVE_edit_spline_thru_pts
          UF_CURVE_pt_slope_crvatr_t
    

History:Original release was in V13.0
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_spline_thru_pts (
int degree ,/* <I>
            degree of the spline
            */
int periodicity ,/* <I>
                 periodicity of the spline: 0=non-periodic, 1=periodic
                 */
int num_points ,/* <I>
                number of points and parameters in the following arrays
                */
UF_CURVE_pt_slope_crvatr_t point_data[] ,/* <I,len:num_points>
                                         array of data defining points and
                                         slope/curvature control
                                         */
double parameters[] ,/* <I,len:num_points>
                     parameters of input points. This is a user specified
                     parameterization for the input points, which needs to be
                     monotonic increasing (i.e. parameters(i) < parameters(i+1)
                     for all i), but does not need to be normalized, if NULL
                     then the default parameterization will be used.
                     */
int save_def_data ,/* <I>
                   If save_def_data = 1, save input defining
                   data with the created spline. Otherwise, no.
                   */
tag_t* spline_tag  /* <O>
                   tag of the created spline
                   */
);

/******************************************************************************
Queries if a spline is in synchronization with its defining data. The
shape of a spline is determined by its control pole data, which could
be obtained from its defining data. If the control pole data of a spline
is matched with its defining data, then the spline is in synchronization,
otherwise, the spline is out of synchronization. For example, users can
modify the control pole data of a spline after it is created from the
defining data, in this case, it is out of synchronization.

Environment: Internal  and  External

See also: UF_CURVE_create_spline_thru_pts
          UF_CURVE_ask_spline_thru_pts
          UF_CURVE_edit_spline_thru_pts

History: Original release was in V13.0
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_is_spline_in_sync (
tag_t spline_tag ,/* <I>
                  tag of the spline
                  */
logical * is_sync  /* <O>
                   TRUE = the spline is in synchronization with its
                   defining data.
                   FALSE = the spline is out of synchronization
                   with its defining data.
                   */
);

/******************************************************************************
Determines whether a spline has self intersecting loops.

Environment: Internal  and  External

See Also:

History:Original release was in V14.0.
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_is_spline_self_int(
tag_t  spline_tag ,/* <I>
                   Object identifier of spline to inquire.
                   */
logical * is_self_intersecting  /* <O>
                                TRUE - spline is self intersecting (has loops)
                                FALSE - spline is not self intersecting.
                                */
);

/******************************************************************************
Reads a splines defining data structure. The defining data returns
regardless of whether the spline is in or out of synchronization with its
defining data. However, if you pass the returned data structure to the
routine UF_CURVE_edit_spline_thru_pts,  the spline is recreated from
the input data. Any previous change to the spline by modifying its pole
data will be discarded. If there is no defining data stored with the
spline, an error code will be returned.

The length of the array of parameters is num_points for non-periodic
curves and (num_points+1) for periodic ones.

Environment: Internal  and  External

See Also: UF_CURVE_create_spline_thru_pts
          UF_CURVE_edit_spline_thru_pts
          UF_CURVE_pt_slope_crvatr_t


History: Original release was in V13.0
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_spline_thru_pts (
tag_t spline_tag ,/* <I>
                  tag of spline for which to return data
                  */
int * degree ,/* <O>
              degree of the spline
              */
int * periodicity ,/* <O>
                   periodicity of the spline
                   */
int * num_points ,/* <O>
                  number of points and parameters in the following arrays
                  */
UF_CURVE_pt_slope_crvatr_t ** point_data ,/* <OF,len:num_points>
                                          Array of data defining points and
                                          slope/curvature control.  This array
                                          must be freed by passing it to
                                          UF_free.
                                          */
double ** parameters  /* <OF,len:num_points>
                      Parameters of the points defining the spline. This is a
                      user specified parameterization for the
                      spline definitions points, which needs to be
                      monotonic increasing, but does not
                      need to be normalized, if NULL then
                      default parameterization will be used.
                      This array need to be freed by calling UF_free.
                      */
);


/******************************************************************************
Edits the defining data of a spline, which is replaced by the new input
data as specified. If the spline has no or incomplete defining data, its
shape is recreated from the input defining data.

The length of the array of parameters is num_points for non-periodic
curves and (num_points+1) for periodic ones. The difference with
periodic curves is that although we know the last point of the curve, it
is the first point, we dont know the parameter range of the curve. You
need to give us the parameter for the last point so we know the
parameter range of the curve.

Environment: Internal  and  External

See Also: UF_CURVE_create_spline_thru_pts
          UF_CURVE_edit_spline_thru_pts
          UF_CURVE_pt_slope_crvatr_t

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_spline_thru_pts (
tag_t spline_tag ,/* <I>
                  tag of the spline to be edited
                  */
int degree ,/* <I>
            degree of the spline
            */
int periodicity ,/* <I>
                 periodicity of the spline
                 */
int num_points ,/* <I>
                number of points and parameters in the following arrays
                */
UF_CURVE_pt_slope_crvatr_t * point_data ,/* <I,len:num_points>
                                         array of data defining points and
                                         slope/curvature control
                                         */
double * parameters ,/* <I,len:num_points>
                     parameters of input points. This is a
                     user specified parameterization for the
                     input points, which needs to be
                     monotonic increasing, but does not
                     need to be normalized, if NULL then
                     default parameterization will be used
                     */
int save_def_data  /* <I>
                   If save_def_data = 1, save input
                   defining data with the created spline.  Otherwise, no.
                   */
);

/****************************************************************************
Creates a new spline curve that represents the input list of joined
curves and edges. The curves or edges that you join may not have gaps.

The Modeling distance and angle tolerance are used to create and
validate the resulting spline curve. The modeling tolerance can be
modified by UF_MODL_set_distance_tolerance or UF_MODL_set_angle_tolerance.

The curves you join must be input in order: either clockwise or
counterclockwise.

Environment: Internal  and  External

See Also: 

History: Creation method has the advanced option in NX3.0.
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_joined_curve(
uf_list_p_t uf_curve_list ,/* <I>
                           List of curves or edges to be joined
                           */
int creation_method ,/* <I>
                     The method to join the list of curves:
                     1 = Polynomial Cubic
                     2 = General Spline
                     3 = polynomial quintic
                     4 = advanced
                     */
tag_t * joined_curve ,/* <O>
                      The resulting joined curve spline
                      */
int * status  /* <O>
              A flag indicating if the joined curve returned has corners:
              0 = Curve has no corners
              1 = Curve has corners
              */
);

/****************************************************************************
Gets the structure pointer corresponding to the specified curve id.

NOTE: This routine is to be permanently withdrawn in the near
future. Use the routines in the UF_EVAL module instead.
Gets the structure pointer corresponding to the specified curve id.

Environment: Internal  and  External

See Also: 

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_curve_struct(
tag_t  curve_id ,/* <I>
                 Object identifier of the curve
                 */
UF_CURVE_struct_p_t * curve_struct  /* <OF,free:UF_CURVE_free_curve_struct>
                                    Pointer to pointer of type
                                    UF_CURVE_struct_p_t. This routine
                                    allocates the structure and fills
                                    in the data.  This argument must be freed by
                                    calling UF_CURVE_free_curve_struct.
                                    */
);


/******************************************************************************
Frees the curve structure pointer obtained from the function
UF_CURVE_ask_curve_struct().

NOTE: This routine is to be permanently withdrawn in the near
future. Use the routines in the UF_EVAL module instead.
Frees the curve structure pointer obtained from the function
UF_CURVE_ask_curve_struct.

Environment: Internal  and  External

See Also: 

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_CURVE_free_curve_struct(
UF_CURVE_struct_p_t curve_struct  /* <I>
                                  Curve structure pointer
                                  */
);

/*****************************************************************************
Allows you to get the curve type and data for a specified curve
structure.

NOTE: This routine is to be permanently withdrawn in the near
future. Use the routines in the UF_EVAL module instead.
Allows you to get the curve type and data for a specified curve
structure. You may obtain the curve structure id using
UF_CURVE_ask_curve_struct.

Depending on the object type, curve_data may have the following data:
POINT                   curve_data[0 - 2]

LINE                    curve_data[0]           =  t0
                        curve_data[1]           =  tscale
                        curve_data[2]           =  periodicity
                        curve_data[3 - 5]       =  first point
                        curve_data[6 - 8]       =  second point

ARC                     curve_data[0]           =  t0
                        curve_data[1]           =  tscale
                        curve_data[2]           =  periodicity
                        curve_data[3]           =  start angle
                        curve_data[4]           =  end angle (radians)
                        curve_data[5]           =  radius
                        curve_data[6 - 8]       =  center
                        curve_data[9 - 11]      =  X axis of the
                                                   construction plane
                        curve_data[12 - 14]     =  Y axis of the
                                                   construction plane

CONIC                   curve_data[0]           =  t0
                        curve_data[1]           =  tscale
                        curve_data[2]           =  periodicity
                        curve_data[3]           =  T1
                        curve_data[4]           =  T2
                        curve_data[5]           =  K1
                        curve_data[6]           =  K2
                        curve_data[7]           =  conic type
                        curve_data[8  - 10]     =  center
                        curve_data[11  - 13]    =  axis1
                        curve_data[14  - 16]    =  axis2

B-CURVE                 curve_data[0]           =  t0
                        curve_data[1]           =  tscale
                        curve_data[2]           =  periodicity
                        curve_data[3]           =  number of poles
                        curve_data[4]           =  order
                        curve_data[*]           =  knot sequence
                                                   ( curve_data[3] +
                                                     curve_data[4] )
                        curve_data[*]           =  array of homogeneous
                                                   poles (wx, wy, wz, w), for
                                                   each pole.
Environment: Internal  and  External

See Also: 

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_curve_struct_data(
UF_CURVE_struct_p_t curve_struct ,/* <I>
                                  Curve structure pointer.
                                  */
int * type ,/* <O>
            Object type
            */
double ** curve_data  /* <OF>
                      Array of object data.  This array is allocated by
                      this routine.  The caller must free it by calling UF_free.
                      */
);


/******************************************************************************
Calculates inflection points of a curves projection by inputting the
curves tag, the projection matrix, and the relative range (in
percentage) in which the inflection points are to be found.

Environment: Internal  and  External

See Also: 

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_curve_inflections(
tag_t   curve_eid ,/* <I>
                   Object identifier of the curve
                   */
double proj_matrx[9] ,/* <I>
                     Projection matrix specified in a 1D
                     array(proj_matrx[9])
                     */
double range[2] ,/* <I>
                 Lower and upper limit of the relative range (in %)
                 in which inflection points are searched
                 range[0] = lower limit (umin)
                 range[1] = upper limit (umax)
                 */
int * num_infpts ,/* <O>
                  Number of inflection points found
                  */
double ** inf_pts  /* <OF,len:num_infpts>
                   The inflection points data. The size of the array is
                   inf_pts[num_infpts * 4].
                   (*inf_pts+4*i)[0] = u value of the ith inflection.
                   [1-3]= x, y, z values of the ith inflections.
                   This array must be freed by calling UF_free.
                   */
);



/****************************************************************************
Applies the move multiple curve points method to the editing of a
spline. The identifier of the curve to be edited is provided along with
a structure containing the details of the edit. The first four fields of
the structure are required. The two int fields are also required. The
need for the remaining double elements is based on the method
chosen.

There are three values for the displace_method element. They are:
   1 = distance normal to the curve
   2 = vector and distance
   3 = direction point.

If displace_method1 = 1, then displace_method2 must = 1. For
values of 1 and 2 the distance1 and distance2 fields are required. For
method 3 they are not required. Vector1 and vector2 are only used by
2, the vector method. Dir_pt1 and dir_pt2 are only used by 3, the
direction point method.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_move_mult_points(
tag_t curve_tag ,/* <I>
                 tag of curve
                 */
UF_CURVE_BCMMCP_t *mmcp_dat /* <I>
                            Structure containing spline edit data. The structure
                            is defined in uf_curve.h
                            */
);

/*****************************************************************************
Creates projection curves.

Objects to project may be points, curves, sketch feature identifiers, or
other projected curve feature identifiers. The "number of curves and
points" is the number of such object tags (and does not include the
numbers of curves in any sketch or projection curve feature).

For copy_flag=1 or 2, a group identifier is returned. You can perform
operations on the entire group or extract individual curves from the
group and operate on them.

CAUTION: Because multiple projection curves can be returned for
single defining curves, no attempt is made to assure that the order of
the output curves in the group corresponds to the order of the input
curves.  If  the order is important, for copy_flag = 1 or 2, the curves
should be projected one at a time.

NOTE: The Along Vector option (proj_type = 3) projects the selected
objects along a specified vector. You can project the curves in the
direction indicated by the vector by setting the multiplicity to 1
(single), or in both directions by setting the multiplicity to 2 (both).
The Along Vector option produces all possible images on the face.

CAUTION: For copy_flag = 2 (move), new curves/points are created
and the original curves/points are deleted.
For a projected curve feature created using copy_flag=3, the feature
can be deleted using UF_MODL_delete_feature.  Individual projection
curves of the feature can not be deleted.

UF_MODL_move_feature can be used to move the projected curve feature.

Points can not be projected using "angle and vector" (proj_type = 4)
or "equal arc length" (proj_type =6).

NOTE: You can change the tolerance used to create a curve
projection by using the subroutine UF_MODL_set_distance_tolerance.
The projection along face normals or along a vector produces an exact
projection when projecting onto a plane.

Environment: Internal  and  External

See Also: UF_MODL_create_proj_curves
          UF_MODL_ask_proj_curves
          UF_CURVE_ask_proj_curves

History: In V13.0, the proj_data argument was modified to add projection type
5 (toward a line), 6 (equal arc length), multiplicity, arcl_option, and the
x_vector.
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_proj_curves(
int n_curve_refs ,/* <I>
                  Number of curves and points
                  */
tag_t * curve_refs ,/* <I,len:n_curve_refs>
                    Array of curve and point identifiers.
                    */
int n_face_refs ,/* <I>
                 Number of sheet bodies, faces and planes
                 */
tag_t * face_refs ,/* <I,len:n_face_refs>
                   Array of plane, datum plane, face or sheet body identifiers.
                   */
int copy_flag ,/* <I>
               Copy flag:
               1 = copy
               2 =  move
               3= associate
               */
UF_CURVE_proj_p_t proj_data ,/* <I>
                             Pointer to projection curve data structure.
                             See documentation of UF_CURVE_proj_s for
                             entries.
                            */
tag_t * proj_curve_feature  /* <O>
                            Group identifier for copy_flag = 1 or 2,
                            Projected curve feature identifier for
                            copy_flag=3
                            */
);

/*****************************************************************************
Edits projection curve features.

Objects to project may be points, curves, sketch feature identifiers, or
other projected curve feature identifiers. The "number of curves and
points" is the number of such object tags (and does not include the
numbers of curves in any sketch or projection curve feature).

NOTE: The Along Vector option (proj_type = 3) projects the selected
objects along a specified vector. You can project the curves in the
direction indicated by the vector by setting the multiplicity to 1
(single), or in both directions by setting the multiplicity to 2 (both).
The Along Vector option produces all possible images on the face.

Points can not be projected using "angle and vector" (proj_type = 4)
or "equal arc length" (proj_type =6).

NOTE: You can change the tolerance used to create a curve
projection by using the subroutine UF_MODL_set_distance_tolerance.
The projection along face normals or along a vector produces an exact
projection when projecting onto a plane.

Environment: Internal  and  External

See Also: UF_MODL_create_proj_curves
          UF_MODL_ask_proj_curves
          UF_CURVE_ask_proj_curves

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_proj_curves(
tag_t proj_curve_feature,  /* <I>
                            Projected curve feature identifier
                            */
int n_curve_refs ,/* <I>
                  Number of curves and points
                  */
tag_t * curve_refs ,/* <I,len:n_curve_refs>
                    Array of curve and point identifiers.
                    */
int n_face_refs ,/* <I>
                 Number of sheet bodies, faces and planes
                 */
tag_t * face_refs ,/* <I,len:n_face_refs>
                   Array of plane, datum plane, face or sheet body identifiers.
                   */
UF_CURVE_proj_p_t proj_data  /* <I>
                             Pointer to projection curve data structure.
                             See documentation of UF_CURVE_proj_s for
                             entries.
                            */
);

/*****************************************************************************
  Initialize a project curve (UF_CURVE_proj_p_t) data structure for an
  associated project curve feature. This function assumes that memory has already been allocated

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_init_proj_curves_data(
    UF_CURVE_proj_p_t proj_data   /* <I>
                                   Pointer to projection curve data structure.
                                   See documentation of UF_CURVE_proj_s for
                                   entries.
                                   */
);

/*****************************************************************************
  Initialize a project curve (UF_CURVE_proj1_p_t) data structure for an
  associated project curve feature. This function assumes that memory has already been allocated

Environment: Internal  and  External

See Also:

History: Originally released in NX4.0
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_init_proj_curves_data1(
    UF_CURVE_proj1_p_t proj_data  /* <I>
                                   Pointer to projection curve data structure.
                                   See documentation of UF_CURVE_proj1_s for
                                   entries.
                                   */
);
/*****************************************************************************
Creates projection curves.

Objects to project may be points, curves, sketch feature identifiers, or
other projected curve feature identifiers. The "number of curves and
points" is the number of such object tags (and does not include the
numbers of curves in any sketch or projection curve feature).

For copy_flag=1 or 2, a group identifier is returned. You can perform
operations on the entire group or extract individual curves from the
group and operate on them.

CAUTION: Because multiple projection curves can be returned for
single defining curves, no attempt is made to assure that the order of
the output curves in the group corresponds to the order of the input
curves.  If  the order is important, for copy_flag = 1 or 2, the curves
should be projected one at a time.

NOTE: The Along Vector option (proj_type = 3) projects the selected
objects along a specified vector. You can project the curves in the
direction indicated by the vector by setting the multiplicity to 1
(single), or in both directions by setting the multiplicity to 2 (both).
The Along Vector option produces all possible images on the face.

CAUTION: For copy_flag = 2 (move), new curves/points are created
and the original curves/points are deleted.
For a projected curve feature created using copy_flag=3, the feature
can be deleted using UF_MODL_delete_feature.  Individual projection
curves of the feature can not be deleted.

UF_MODL_move_feature can be used to move the projected curve feature.

Points can not be projected using "angle and vector" (proj_type = 4)
or "equal arc length" (proj_type =6).

NOTE: You can change the tolerance used to create a curve
projection by using the subroutine UF_MODL_set_distance_tolerance.
The projection along face normals or along a vector produces an exact
projection when projecting onto a plane.

Environment: Internal  and  External

See Also: UF_MODL_create_proj_curves
          UF_MODL_ask_proj_curves
          UF_CURVE_ask_proj_curves

History: Originally released in NX4.0
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_proj_curves1(
int n_curve_refs ,/* <I>
                  Number of curves and points
                  */
tag_t * curve_refs ,/* <I,len:n_curve_refs>
                    Array of curve and point identifiers.
                    */
int n_face_refs ,/* <I>
                 Number of sheet bodies, faces and planes
                 */
tag_t * face_refs ,/* <I,len:n_face_refs>
                   Array of plane, datum plane, face or sheet body identifiers.
                   */
int copy_flag ,/* <I>
               Copy flag:
               1 = copy
               2 =  move
               3= associate
               */
UF_CURVE_proj1_p_t proj_data ,/* <I>
                             Pointer to projection curve data structure.
                             See documentation of UF_CURVE_proj1_s for
                             entries.
                            */
tag_t * proj_curve_feature  /* <O>
                            Group identifier for copy_flag = 1 or 2,
                            Projected curve feature identifier for
                            copy_flag=3
                            */
);

/*****************************************************************************
Edits projection curve features.

Objects to project may be points, curves, sketch feature identifiers, or
other projected curve feature identifiers. The "number of curves and
points" is the number of such object tags (and does not include the
numbers of curves in any sketch or projection curve feature).

NOTE: The Along Vector option (proj_type = 3) projects the selected
objects along a specified vector. You can project the curves in the
direction indicated by the vector by setting the multiplicity to 1
(single), or in both directions by setting the multiplicity to 2 (both).
The Along Vector option produces all possible images on the face.

Points can not be projected using "angle and vector" (proj_type = 4)
or "equal arc length" (proj_type =6).

NOTE: You can change the tolerance used to create a curve
projection by using the subroutine UF_MODL_set_distance_tolerance.
The projection along face normals or along a vector produces an exact
projection when projecting onto a plane.

Environment: Internal  and  External

See Also: UF_MODL_create_proj_curves
          UF_MODL_ask_proj_curves
          UF_CURVE_ask_proj_curves

History: Originally released in NX4.0
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_proj_curves1(
tag_t proj_curve_feature,  /* <I>
                            Projected curve feature identifier
                            */
int n_curve_refs ,/* <I>
                  Number of curves and points
                  */
tag_t * curve_refs ,/* <I,len:n_curve_refs>
                    Array of curve and point identifiers.
                    */
int n_face_refs ,/* <I>
                 Number of sheet bodies, faces and planes
                 */
tag_t * face_refs ,/* <I,len:n_face_refs>
                   Array of plane, datum plane, face or sheet body identifiers.
                   */
UF_CURVE_proj1_p_t proj_data  /* <I>
                             Pointer to projection curve data structure.
                             See documentation of UF_CURVE_proj1_s for
                             entries.
                            */
);


/******************************************************************************
Returns the curves associated with a projected curve feature.

Environment: Internal  and  External

See Also:  UF_CURVE_create_proj_curves
           UF_MODL_create_proj_curves
           UF_MODL_ask_proj_curves

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_proj_curves(
tag_t proj_curve_feature ,/* <I>
                          Projected curve feature identifier.
                          */
int * n_curve_refs ,/* <O>
                    Number of curve identifiers.
                    */
tag_t ** curve_refs  /* <OF,len:n_curve_refs>
                     Pointer to array of curve identifiers. Use UF_free
                     to deallocate memory.
                     */
);

/*****************************************************************************
Given an input projected curve, determines the feature identifier, the
target object identifier (sheet_body/face/plane/datum_plane), and the defining
curve identifier of the projected curves.

The projected curve must be a curve that was produced by
UF_CURVE_create_proj_curves. You can get this curve by calling the
function UF_CURVE_ask_proj_curves. An error is returned if the
projected curve does not belong to a projected curves feature.
The following example creates a block at origin (0,0,0) with edge
lengths of (300,25,150). The program creates and projects a line onto
the faces of the block. Next the projected curves are found, and then
the face the curves projected onto and the defining curves generating
the projected curves are determined.

Environment: Internal  and  External

See Also: 

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_proj_curve_parents(
tag_t proj_curve ,/* <I>
                  The curve identifier whose projected curve feature,
                  defining sheet_body/face/plane/datum_plane, and defining
                  curve are to be found.
                  */
tag_t * defining_feature ,/* <O>
                          The projected curves feature identifier that
                          produced the input curve.
                          */
tag_t * defining_target ,/* <O>
                         The sheet_body/face/plane/datum_plane identifier of the
                         defining target that the input curve was projected
                         onto.
                         */
tag_t * defining_curve  /* <O>
                        The defining curve identifier of the projected curve
                        feature that generated this projected curve.
                        */
);


 /************************************************************************
Creates parametric curve(s) by combining two curves along specified
direction vectors. When "normal to plane of curve" is specified as the
projection type, the curve must be planar. An error will be given if the
above is not true.

Environment: Internal  and  External

See Also:  UF_CURVE_combine_curves_direction_t
  

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_combine_curves(
tag_t first_curve_tag ,/* <I>
                       First curve tag to be projected for combine
                       */
UF_CURVE_combine_curves_direction_p_t first_dir ,/* <I>
                                                 Pointer to projection direction
                                                 info for first curve
                                                 */
tag_t second_curve_tag ,/* <I>
                        Second curve tag to be projected for combine
                        */
UF_CURVE_combine_curves_direction_p_t second_dir ,/* <I>
                                                  Pointer to projection
                                                  direction info for second
                                                  curve
                                                  */
const char * curve_aprox_tol ,/* <I>
                        String containing the value for
                        the curve approximation
                        tolerance (distance tolerance).
                        */
tag_t * combine_curve_feature  /* <O>
                               Object tag for the combined curve feature.
                               */
);

/*****************************************************************************
Edits parametric curve(s) by combining two curves along specified
direction vectors. The parameters used to create the curve should be
acquired by using UF_MODL_ask_combine_curves. Any of the
original input parameters can be modified. When "normal to plane of
curve" is specified as the projection type, the curve must be planar.
An error occurs if the above is not true.

Environment: Internal  and  External

See Also:  UF_CURVE_combine_curves_direction_t

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_combine_curves(
tag_t combine_curve_feature ,/* <I>
                             Object tag for the combined curve feature to
                             be edited.
                             */
tag_t first_curve_tag ,/* <I>
                       First curve tag to be projected for combine.
                       */
UF_CURVE_combine_curves_direction_p_t first_dir ,/* <I>
                                                  Pointer to projection
                                                  direction info for first
                                                  curve.
                                                  */
tag_t second_curve_tag ,/* <I>
                        Second curve tag to be projected for combine.
                        */
UF_CURVE_combine_curves_direction_p_t second_dir ,/* <I>
                                                   Pointer to projection
                                                   direction info for second
                                                   curve.
                                                   */
const char * curve_aprox_tol  /* <I>
                        String containing the value for the curve
                        approximation tolerance (distance tolerance).
                        */
);

/*****************************************************************************
Retrieves the parameters used to create parametric curve(s) by
combining two curves along specified direction vectors.

Environment: Internal  and  External

See Also: 
For structure refer
   UF_CURVE_combine_curves_direction_t

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_combine_curves(
tag_t  combine_curve_feature ,/* <I>
                              Object tag for the combined curve feature.
                              */
tag_t * first_curve_tag ,/* <O>
                         First curve tag projected for combine
                         */
UF_CURVE_combine_curves_direction_p_t first_dir ,/* <O>
                                                 Pointer to projection
                                                 direction info for first curve
                                                 */
tag_t * second_curve_tag ,/* <O>
                          Second curve tag projected for combine
                          */
UF_CURVE_combine_curves_direction_p_t second_dir ,/* <O>
                                                  Pointer to projection
                                                  direction info for second
                                                  curve
                                                  */
char ** tol ,/* <OF>
             String containing the value for curve approximation
             tolerance (distance tolerance).  This parameter
             must be freed by calling UF_free.
             */
uf_list_p_t * curve_list  /* <OF,free:UF_MODL_delete_list>
                          Address of pointer to list of curve tags created by
                          combining two curves. Use UF_MODL_delete_list to
                          free the space allocated for this list.
                          */
);

/******************************************************************************
Creates a fillet between the specified curves. The curves can be any
combination of points, lines, arcs, conics, or splines.

A two curve fillet is an arc generated in the
counterclockwise direction from the first curve to the
second.  The fillet formed is tangent to both curves.  The counterclockwise
direction is determined based on the current views orientation, not the
absolute or WCS coordinate systems.

NOTE:  The ability to specify whether an input curve is to be
trimmed is provided. If a "spline-type" curve is flagged to be
trimmed, the defining points and associated dimensions will be
deleted. If a trimmed curve has a length equal to zero and there is no
associative connection to the curve, the curve will be deleted.

NOTE:  The center point coordinates (for 2-curve fillet) will be
projected along the Z-axis of the WCS, to the construction plane of
the fillet if necessary.

There is no 3 curve fillet so the documentation for this option has been removed.

Environment: Internal  and  External

See Also: 

History:
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_fillet (
int type ,/* <I>
          The type of fillet that is to be created:
          UF_CURVE_2_CURVE = create 2 curve fillet
          */
tag_t  curve_objs[3] ,/* <I>
                 Object identifiers of the curves between which the
                 fillet is to be created.
                 [0] = identifier of first curve
                 [1] = identifier of second curve
                 [2] = not used in a 2 curve fillet
                 */
double center[3] ,/* <I>
                  Approximate fillet center expressed as absolute
                  coordinates
                  */
double radius ,/* <I> Radius of the fillet */
int trim_opts[3] ,/* <I>
                  Trimming options
                  FOR 2 CURVE FILLET:
                  [0] = TRUE -> trim first curve FALSE -> do not trim first
                        curve
                  [1] =  TRUE -> trim second curve FALSE -> do not trim second
                         curve
                  */
int arc_opts[3] ,/* <I> Not used */
tag_t * fillet_obj  /* <O>
                    The object identifier associated to the newly
                    created fillet NULL_TAG = fillet unable to be created
                    */
);


/***************************************************************************
Trims a curve to a bounding object. The bounding object can be a
curve, edge, plane, face, or point. The reference point is used to
determine which end of the curve to trim. The reference point is also
used to start the iteration that determines the intersection point of the
curve and the bounding object. The extension shape (ext_ind)
parameter is used when the curve is extended.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_trim_curve(
tag_t curve_tag ,/* <I>
                 tag of curve to trim
                 */
tag_t bounding_id ,/* <I>
                   tag of first bounding object ( curve, edge, plane,
                   face, point)
                   */
double ref_point[3] ,/* <I>
                    ref_point[3] are the coordinates of a point used to
                    specify which portion of the curve to trim also used
                    as start point intersection point iteration (ACS)
                    */
double int_point[3] ,/* <I>
                    int_point[3] is the start point for finding the
                    intersection of the curve to trim and the bounding object.
                    */
int ext_ind  /* <I>
             shape of the extension of the curve:
             UF_CURVE_NATURAL_SHAPE
             UF_CURVE_LINEAR_SHAPE
             UF_CURVE_CIRCULAR_SHAPE
             */
);

/*****************************************************************************
Creates a wrap or unwrap curves feature.

If wrap_unwrap_sw is UF_CURVE_WRAP, the wrap_curves will be
wrapped from the wrap_plane onto the wrap_face. The wrap_curves
should lie on the wrap_plane, however the curves will internally be
projected onto the wrap_plane along the normal to the wrap_plane
before being wrapped. If this default projection is undesirable, be sure
that the curves lie in the wrap_plane before invoking this function.

If wrap_unwrap_sw is UF_CURVE_UNWRAP, the wrap_curves will be
unwrapped from the wrap_face onto the wrap_plane. The
wrap_curves should lie on the wrap_face, however the selected curves
will internally be projected onto the wrap_face along the face normals
before being unwrapped. If this default projection is undesirable, be
sure that the curves lie in the wrap_face before invoking this function.

Environment: Internal  and  External

See Also: 

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_wrap_object(
UF_CURVE_wrap_data_p_t wrap_data,/* <I>
                                 Structure specifying the wrap /unwrap to
                                 be created.
                                 */
tag_t * wrap_curve_object  /* <O>
                           Pointer to the Object Identifier of the
                           new wrap or unwrap feature.
                           */
);

/******************************************************************************
Edits the creation parameters of a wrap or unwrap curves feature.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_wrap_object(
UF_CURVE_wrap_data_p_t wrap_data ,/* <I>
                                  Structure specifying the new wrap/unwrap
                                  data for wrap_curve_object.
                                  */
tag_t wrap_curve_object  /* <I>
                         Object Identifier of the wrap or unwrap feature.
                         */
);

/******************************************************************************
Frees any data structures pointed to by the input structure. The
existing pointers will be set to NULL after the associated memory is
freed.  The memory for the UF_CURVE_wrap_data_t structure is not
freed by this function.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_free_wrap_parms(
UF_CURVE_wrap_data_p_t wrap_data  /* <I>
                                  Structure specifying the wrap/unwrap to be
                          freed.
                                  */
);/*<NON_NXOPEN> */

/*****************************************************************************
Reads the creation parameters of a wrap or unwrap curves feature.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_wrap_parms(
tag_t wrap_curve_object ,/* <I>
                         Object Identifier of the wrap or unwrap feature.
                         */
UF_CURVE_wrap_data_p_t wrap_data  /* <OF,free:UF_CURVE_free_wrap_parms>
                                   Pointer to a structure to be filled in with
                                   the defining information for the input
                                   feature.  The calling routine must allocate
                                   a UF_CURVE_wrap_data_t structure, and pass
                                   the pointer into this routine.  This routine
                                    will fill the structure with allocated
                                   data.  The calling routine must then call
                                   UF_CURVE_free_wrap_parms to free memory
                                   allocated to support this structure.
                                  */
);

/****************************************************************************
Reads the creation parameters of a wrap or unwrap curves feature.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_wrap_curves(
tag_t wrap_curve_object ,/* <I>
                         Object Identifier of the wrap or unwrap feature.
                         */
int * num_output_curves ,/* <O>
                         Number of tags returned in the output_curves array.
                         */
tag_t ** output_curves  /* <OF,len:num_output_curves>
                        Object Identifiers of curves produced by this
                        wrap/unwrap. You are responsible for freeing the
                        memory allocated for this array by calling UF_free.
                        */
);

/****************************************************************************
Reads the creation parameters pertaining to a wrap or unwrap curve.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_wrap_curve_parents(
tag_t curve_tag ,/* <I>
                 Object Identifier of a wrap or unwrap curve.
                 */
tag_t * defining_face ,/* <O>
                       Object Identifier of the Wrap Face of the input curve.
                       */
tag_t * defining_plane ,/* <O>
                        Object Identifier of the Wrap Plane of the input curve
                        */
tag_t * defining_curve ,/* <O>
                        Object Identifiers of the curve, edge, or face that
                        produced the wrap_curve
                        */
tag_t * wrap_curve_object  /* <O>
                           Object Identifier of the wrap or unwrap feature.
                           */
);
/*****************************************************************************
Offsets a string of curves (non-associative).

Environment: Internal  and  External

See Also:  UF_CURVE_offset_data_t

History:
*************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_offset_curve(
UF_CURVE_offset_data_p_t offset_data_pointer ,/* <I>
                                             Pointer to structure containing the
                         defining data of the offset curve.
                                             */
int * num_offset_curves ,/* <O>
                         Number of offset curves created
                         */
tag_t ** offset_curve_tags  /* <OF,len:num_offset_curves>
                            Object identifiers of offset curves created.
                    Use UF_free to deallocate memory when done.
                            */
);
/**************************************************************************
Offsets a string of curves. Returns a tag to the object which associates
input curves and defining data to the output offset curves. Use
UF_CURVE_ask_offset_curves to retrieve the offset curve tags.

Only the following types of offsets are allowed for offset_data_pointer:
   UF_CURVE_OFFSET_DISTANCE_NO_TRIM
   UF_CURVE_OFFSET_DISTANCE_TANGENT
   UF_CURVE_OFFSET_DISTANCE_FILLET
   UF_CURVE_OFFSET_DRAFT_NO_TRIM
   UF_CURVE_OFFSET_DRAFT_TANGENT
   UF_CURVE_OFFSET_DRAFT_FILLET
   UF_CURVE_OFFSET_3D_AXIAL

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_offset_object(
UF_CURVE_offset_data_p_t offset_data_pointer ,/* <I>
                                              Pointer to structure containing
                          the defining data of the offset
                                              curve.
                                              */
tag_t * offset_curve_object  /* <O>
                             Object identifier of offset curve object created.
                             */
);

/***************************************************************************
Edits the creation parameters of an offset curve object.

Only the following types of offsets are allowed for offset_data_pointer:
   UF_CURVE_OFFSET_DISTANCE_NO_TRIM
   UF_CURVE_OFFSET_DISTANCE_TANGENT
   UF_CURVE_OFFSET_DISTANCE_FILLET
   UF_CURVE_OFFSET_DRAFT_NO_TRIM
   UF_CURVE_OFFSET_DRAFT_TANGENT
   UF_CURVE_OFFSET_DRAFT_FILLET
   UF_CURVE_OFFSET_3D_AXIAL

Environment: Internal & External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_offset_object(
UF_CURVE_offset_data_p_t offset_data_pointer ,/* <I>
                                              Pointer to structure containing
                          the defining data of the offset
                                              curve.
                                              */
tag_t  offset_curve_object  /* <I>
                            Object identifier of offset curve object to be
                edited.
                            */
);

/****************************************************************************
Reads the creation parameters of an offset curve object.

Environment: Internal  and  External

See Also: UF_CURVE_free_offset_parms

History:
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_offset_parms(
tag_t  offset_curve_object ,/* <I>
                            Object identifier of offset curve object
                            to be interrogated.
                            */
UF_CURVE_offset_data_p_t offset_data_pointer  /* <OF,free:UF_CURVE_free_offset_parms>
                                              Pointer to structure containing
                          the defining data of the offset
                                              curve.  The caller is responsible
                                              for allocating a
                                              UF_CURVE_offset_data_t structure,
                                              which this routine will fill with
                                              data which must be freed.  The
                                              caller can free the data allocated
                                              inside this structure by calling
                                              UF_CURVE_free_offset_parms.
                                              */
);
/****************************************************************************
This routine should be called after a call to
UF_CURVE_ask_offset_parms in order to free the space allocated by
this routine.

Environment: Internal  and  External

See Also: UF_CURVE_ask_offset_parms

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_free_offset_parms(
UF_CURVE_offset_data_p_t offset_data_pointer  /* <I>
                                              Pointer to structure containing
                                              the defining data of the offset
                                              curve.
                                              */
);/*<NON_NXOPEN>  */

/***************************************************************************
Returns an array of offset curve object identifiers.

Environment: Internal  and  External

See Also:

History:
**************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_offset_curves(
tag_t  offset_curve_object ,/* <I>
                            Object identifier of offset curve object.
                            */
int * num_curves ,/* <O>
                  Number of curves in array.
                  */
tag_t ** offset_curves  /* <OF,len:num_curves>
                        Array of offset curve object identifiers.  This array
                        must be freed by calling UF_free.
                        */
);

/*****************************************************************************

  Given a section tag and the face collector tag, get the default offset
  direction and a reference point on the section.
  The offset point and the offset direction is returned along with
  an error code that indicates if the default offset direction was
  computed succesfully or not.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ocf_offset_pt_direction
(
   tag_t     uf_string_tag,                 /* <I> Section tag */
   tag_t     uf_face_collector_tag,         /* <I> Face Collector tag */
   double    offset_point[3],               /* <O> Reference Point */
   double    offset_direction[3]            /* <O> Default offset direction*/
);

/*****************************************************************************

  Create an associated offset curves on face feature using the input offset
  data.
  A UF_CURVE_ocf_data_p_t is allocated and created. A feature tag along with an
  error code is returned.
Environment: Internal  and  External

See Also:
  
  For examples using different selection intent rules to create section
  and face collectors view:
  
  

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_ocf_feature
(
    UF_CURVE_ocf_data_p_t   offset_data,  /* <I> Pointer to the structure
                                                 containing defining data for
                                                 the offset curve on face
                                                 operation

                                                 The offset_data->string_data->string_tag
                                                 must be created via UF_MODL_create_section.
                                                 The valid string is a section created using
                                                 a connected set of edges or curves.
                                                 If the curves are used to create section,
                                                 then they should lie on set of faces used
                                                 to create the smart face container.

                                                 The offset_data->face_data->face_tag
                                                 must be created via UF_MODL_create_smart_face_container.
                                                 The faces used to create smart container
                                                 should be a connected set and come from a
                                                 single body.
                                          */
    tag_t*                     feature    /* <O> offset curve on face feature
                                                 identifier
                                           */
);


/*****************************************************************************

  Edits an associated offset curves on face feature using the input offset data
  A UF_CURVE_ocf_data_p_t is allocated and filled.
  The input UF_CURVE_ocf_data_p_t is used to update the feature and the feature
  is updated to reflect the changes
Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_ocf_feature
(
    UF_CURVE_ocf_data_p_t   offset_data,    /* <I> Pointer to the structure
                                                  containing defining data
                                                  for the offset curve on face
                                                  operation
                                             */
    tag_t                      feature      /* <I> Offset curve on face
                                                  identifier
                                             */
);


/*****************************************************************************

  Returns the offset data for a given associated offset curve on face feature.
  This data can be modified and then UF_CURVE_edit_ocf_feature invoked to
  modify a feature.
  Memory is allocated when this data is returned.  It is the responsibility of
  the caller to free that memory by calling UF_CURVE_free_ocf_data
Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_ocf_data
(
    tag_t                     feature,          /* <I> Offset curve on face
                                                      feature identifier
                                                 */
    UF_CURVE_ocf_data_p_t     *offset_data      /* <OF,free:UF_CURVE_free_ocf_data>
                                                        Pointer to the structure
                                                      containing defining data
                                                      for the offset curve on
                                                      face feature
                                                 */
);

/*****************************************************************************

  Free the input offset data allocated during crate/edit of an associated
  offset curves on face feature.
Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_free_ocf_data
(
    UF_CURVE_ocf_data_p_t  *offset_data       /* <I/O>  Free the data allocated
                                                       to define the offset
                                                       curve on face feature.
                                               */
);/*<NON_NXOPEN>*/

/*****************************************************************************

  Initialize a offset data structure for an associated offset curve in face
  feature.  This function assumes that memory has already been allocated

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_init_ocf_data
(
    UF_CURVE_ocf_data_p_t   uf_offset_data    /* <I> Init the data defining
                                                    the offset curve on face
                                                    feature
                                               */
);

/*****************************************************************************

  Add a face collector to the offset data for the associated offset curve on
  face feature.
  If the offset data already has a face collector associated with it,
  that existing face collector is ignored and the input face collector is used
Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_add_faces_ocf_data
(
    tag_t                    face_tag,           /* <I> Identifier of the face
                                                    collector to add to the
                                                    defining date */
    UF_CURVE_ocf_data_p_t    uf_offset_data      /* <I> Pointer to the data
                                                    defining the offset curve
                                                    on face feature */
);

/*****************************************************************************

  Add a string to an associated offset curve on face feature.
  If the string is invalid, an error is returned.
Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_add_string_to_ocf_data
(
    tag_t                      string_tag,       /* <I> Identifier of a string */
    int                        offset_direction, /* <I> direction along where
                                                       the offset will be
                                                       performed */
    int                        num_offsets,      /* <I> Number of offsets to
                                                       create for the input
                                                       string
                                                  */
    UF_CURVE_ocf_values_p_t    offset_distances, /* <I, len:num_offsets> Offset values for each
                                                       offset
                                                  */
    UF_CURVE_ocf_data_p_t      uf_offset_data    /* <I/O> Pointer to the
                                                         structure containing
                                                         data to define the
                                                         offset curve on face
                                                         operation
                                                  */

);

/*****************************************************************************

  Remove a string from the associated offset curves in face feature.

  If the string is not found, an error is returned.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_remove_string_from_ocf_data
(
    tag_t                        string_tag,      /* <I> Identifier of string */
    UF_CURVE_ocf_data_p_t        uf_offset_data   /* <I/O> Pointer to the data
                                                     defining the offset curve
                                                     on face operation
                                                   */
);

/*****************************************************************************

  Modify the offset values associated with a string in an associated offset
  curves on face feature.
  If the string does not exist an error is returned.
Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_modify_offsets_in_string
(
    tag_t                      string_tag,       /* <I> Identifier to string that
                                                       has to be modified
                                                  */
    UF_CURVE_ocf_data_p_t      uf_offset_data,   /* <I/O> Pointer to data
                                                         defining the offset
                                                         curve on face
                                                         operation
                                                  */
    int                        num_offsets,      /* <I> New number of offsets to
                                                       create
                                                  */
    UF_CURVE_ocf_values_p_t    offset_distance   /* <I,len:num_offsets> New offset distances */
);

/*****************************************************************************

  Return all offset curves for the associated offset curves on face feature
  The caller has to free the memory allocated when offset_curves is returned.
Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT  int  UF_CURVE_ocf_ask_curves
(
    tag_t    feature_eid,         /* <I> : Identifier to the offset curve on face
                                     feature */
    int      *num_curves,         /* <O> : Number of offset curves created */
    tag_t    **offset_curves      /* <OF,len:num_curves> pointer to array containing the offset curve
                                     identifiers */
);

/******************************************************************************
Sorts through a set of unordered curves, joining curves where
appropriate. Curves must meet the following criteria in order to join:
The curve must be open. Closed curves such as a circle or ellipse
cannot be joined.

Only curves that share a common end point can be joined.
Only valid curves can be joined (line, arc, b-spline, conics).

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_auto_join_curves(
tag_t * crv_list ,/* <I,len:crv_num>
                  Array of curves to be joined
                  */
int crv_num ,/* <I>
             Number of curves in crv_list
             */
int join_type ,/* <I>
               Join type
               1 = Polynomial Cubic
               2 = General Spline
               */
tag_t * join_list ,/* <O,len:crv_num>
                   List of output curves (joined and not joined). The
                   size of this list cannot exceed crv_num. Therefore
                   you can declare this variable as:
                   tag_t join_list[crv_num];
                   */
int * join_num  /* <O>
                Number of curves in join_list
                */
);

/******************************************************************************
Intersects two sets of objects. Objects to intersect must be 1 body, 1
datum plane, 1 face collector or multiple faces (from same body) per set.
Datum planes cannot be input for both sets since the result is a
non-associative line.  If you wish to intersect two datum planes you
can use UF_MODL_intersect_objects.

Environment: Internal  and  External

See Also:  UF_MODL_intersect_objects

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_int_object(
int num_objects_set_1 ,/* <I>
                       Number of intersection objects in object_set_1 array.
                       */
tag_t * object_set_1 ,/* <I,len:num_objects_set_1>
                      Array of tags of objects to intersect with objects in
                      object_set_2 array.
                      */
int num_objects_set_2 ,/* <I>
                       Number of intersection objects in object_set_2 array.
                       */
tag_t * object_set_2 ,/* <I,len:num_objects_set_2>
                      Array of tags of objects to intersect with objects in
                      object_set_1 array.
                      */
tag_t * int_curve_object  /* <O>
                          Feature tag of intersection curve
                          */
);

/******************************************************************************
Edits Intersection curves by allowing you to replace input intersection
objects. Objects to intersect must be 1 body, 1 datum plane, or
multiple faces (from same body) per set. Datum planes cannot be
input for both sets since the result is a non-associative line.

Environment: Internal  and  External

See Also:

History: Original release was in V13.0
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_int_object(
int num_object_set_1 ,/* <I>
                      Number of intersection objects in object_set_1 array.
                      */
tag_t * object_set_1 ,/* <I,len:num_object_set_1>
                      Array of tags of objects to intersect with objects in
                      object_set_2 array.
                      */
int num_object_set_2 ,/* <I>
                      Number of intersection objects in object_set_2 array.
                      */
tag_t * object_set_2 ,/* <I,len:num_object_set_2>
                      Array of tags of objects to intersect with objects in
                      object_set_1 array.
                      */
tag_t  int_curve_object  /* <I>
                         Feature tag of intersection curve to edit.
                         */
);



/******************************************************************************
Reads the creation parameters of an intersection curve feature.
Returns array of tags to the sets of input intersection objects.
This also has the ability to return the tag of collector in case
the objects intersecting are collectors.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_int_parms_sc(
tag_t  int_curve_object ,/* <I>
                         Feature tag of intersection curve.
                         */
int * num_objects_set_1 ,/* <O>
                         Number of intersection objects in object_set_1 array.
                         */
tag_t ** object_set_1 ,/* <OF,len:num_objects_set_1>
                       Array of tags of objects intersecting with objects in
                       object_set_2 array.  This must be freed by calling
                       UF_free.
                       */
int * num_objects_set_2 ,/* <O>
                         Number of intersection objects in object_set_2 array.
                         */
tag_t ** object_set_2, /* <OF,len:num_objects_set_2>
                       Array of tags of objects intersecting with objects in
                       object_set_1 array.  This must be freed by calling
                       UF_free.
                       */
logical *set1_is_collector, /* <O>
                            TRUE if set1 is a collector.
                            */
logical *set2_is_collector  /* <O>
                            TRUE if set2 is a collector.
                            */
);

/******************************************************************************
Reads the creation parameters of an intersection curve feature.
Returns array of tags to the sets of input intersection objects.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_int_parms(
tag_t  int_curve_object ,/* <I>
                         Feature tag of intersection curve.
                         */
int * num_objects_set_1 ,/* <O>
                         Number of intersection objects in object_set_1 array.
                         */
tag_t ** object_set_1 ,/* <OF,len:num_objects_set_1>
                       Array of tags of objects intersecting with objects in
                       object_set_2 array.  This must be freed by calling
                       UF_free.
                       */
int * num_objects_set_2 ,/* <O>
                         Number of intersection objects in object_set_2 array.
                         */
tag_t ** object_set_2  /* <OF,len:num_objects_set_2>
                       Array of tags of objects intersecting with objects in
                       object_set_1 array.  This must be freed by calling
                       UF_free.
                       */
);
/*****************************************************************************
Returns an array of intersection curve tags.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_int_curves(
tag_t  int_curve_object ,/* <I>
                         Feature tag of intersection curve.
                         */
int * num_curves ,/* <O>
                  Number of curves in array.
                  */
tag_t ** intersection_curves  /* <OF,len:num_curves>
                              Array of intersection curves.  This must be
                              freed by calling UF_free.
                              */
);

/****************************************************************************
Given an intersection curve feature, returns the Object identifier of
the intersection curve object and the object identifiers of the two
objects that produced the intersection curve. Returns an error if the
intersection curve does not belong to an intersection curve object.

Environment: Internal  and  External

See Also:

History:
***************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_int_curve_parents(
tag_t  int_curve ,/* <I>
                  Feature tag of intersection curve to inquire.
                  */
tag_t * int_curve_object ,/* <O>
                          Object identifier of intersection curve object.
                          */
tag_t  input_objects[2]  /* <O>
                         Object identifier of the two objects that produced
                         the intersection curve.  Can be face, edge, or 
                         datum plane.
                         */
);
/*****************************************************************************
Bridges two curves/edges by matching tangents or matching curvatures.  You
can control the connection of the bridge curve along the two curves/edges by
specifying the parameter along each curve/edge. You have the ability to
reverse the tangent direction vector at the parameter along the curves/edges.
The routine returns the object identifier of the new bridge curve.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_bridge_curve(
int bridge_method ,/* <I>
                   UF_CURVE_TANGENT - match tangents
                   UF_CURVE_CURVATURE - match curvatures
                   */
tag_t curve_ids[2] ,/* <I>
                    Object identifiers of the two curves/edges to bridge.
                    */
double parms[2] ,/* <I>
                 Parameters on curves/edges to connect bridge.
                 */
int reverse_tangent[2] ,/* <I>
                        Indicates whether to reverse the tangent direction
                        vector at the chosen parameter on the curve/edge.
                        0 = do not reverse
                        not 0 means to reverse
                        */
tag_t * bridge_id  /* <O>
                   Object identifier of the bridge curve.
                   */
);
/******************************************************************************
Computes the centroid (center of gravity) of a curve or solid edge.

Environment: Internal  and  External

See Also: 

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_centroid(
tag_t curve_id ,/* <I>
                Object identifier of curve or edge
                */
double  centroid[3]  /* <O>
                     Centroid of curve or edge
                     */
);
/****************************************************************************
Creates a new joined curve feature that consists of a new spline curve
that represents the input list of joined curves and edges. The curves
can be sketch curves. The curves or edges that you join may not have
gaps.

The Modeling distance and angle tolerance are used to create and
validate the resulting spline curve. The modeling tolerance can be
modified by UF_MODL_set_distance_tolerance or UF_MODL_set_angle_tolerance.

Environment: Internal  and  External

See Also:
          UF_MODL_create_isocline_curves
          UF_CURVE_ask_isocline
          UF_CURVE_edit_isocline
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_isocline (
int face_cnt ,/* <I>
              Number of faces
              */
tag_t faces[] ,/* <I,len:face_cnt>
               Array of faces used to calculate isocline curves
               */
double direction[3] ,/* <I>
                     Isocline direction vector
                     */
const char * start_angle ,/* <I>
                    Start angle  (-90 to 90 degrees)
                    */
const char * end_angle ,/* <I>
                  End angle  (-90 to 90 degrees)
                  */
const char * step_angle ,/* <I>
                   Step angle (NULL for single angle)
                   */
tag_t * isocline_feat  /* <O>
                       Tag of new feature
                       */
);
/***************************************************************************
Ask isocline curve feature data
Returns the parameters of a joined curve feature.

Environment: Internal  and  External

See Also: UF_CURVE_edit_isocline

History:
 **************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_isocline (
tag_t isocline_feat ,/* <I>
                     Tag of feature
                     */
int * face_cnt ,/* <O>
                Number of faces
                */
tag_p_t * faces ,/* <OF,len:face_cnt>
                 Array of faces used to calculate isocline curves.
                 This must be freed by calling UF_free.
                 */
double direction[3] ,/* <O>
                     Isocline direction vector
                     */
char ** start_angle ,/* <OF>
                     Start angle.  This must be freed by calling UF_free.
                     */
char ** end_angle ,/* <OF>
                   End angle (NULL for single angle)
                   This must be freed by calling UF_free.
                   */
char ** step_angle ,/* <OF>
                    Step angle (NULL for single angle)
                    This must be freed by calling UF_free.
                    */
int * curve_cnt ,/* <O>
                 Number of isocline curves
                 */
tag_p_t * curves  /* <OF,len:curve_cnt>
                  Array of isocline curves
                  This must be freed by calling UF_free.
                  */
);
/****************************************************************************
Edit isocline curve feature
Modify an isocline curve feature.

Environment: Internal  and  External

See Also: UF_CURVE_create_isocline
          UF_CURVE_ask_isocline

History:
***************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_isocline (
tag_t  isocline_feat ,/* <I>
                      Tag of feature
                      */
int face_cnt ,/* <I>
              Number of faces
              */
tag_t faces[] ,/* <I,len:face_cnt>
               Array of faces used to calculate isocline curves
               */
double direction[3] ,/* <I>
                     Isocline direction vector
                     */
const char * start_angle ,/* <I>
                    Start angle  (-90 to 90 degrees)
                    */
const char * end_angle ,/* <I>
                  End angle (-90 to 90 degrees)
                  */
const char * step_angle  /* <I>
                   Step angle (NULL for single angle)
                   */
);

/****************************************************************************
Computes the arc length of a curve between two input normalized parameters. 
It will also compute the length of a solid edge.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_arc_length (
tag_t curve_tag ,/* <I>
                 Tag of curve to query for arc length
                 */
double start_param ,/* <I>
                    Start parameter of the curve from which the arc
                    length is to be calculated. (Normalized parameter)
                    */
double end_param ,/* <I>
                  End parameter of the curve to which the arc length
                  is to be calculated. (Normalized parameter)
                  */
UF_MODL_units_t unit_flag ,/* <I>
                           Any one of  the following enumerated constants:
               UF_MODL_UNITS_PART - same as parts units
               UF_MODL_INCH              - inches
               UF_MODL_MMETER    - millimeters
               UF_MODL_CMETER     - centimeters
               UF_MODL_METER        - meters
                           */
double* arc_length  /* <O>
                    arc length of the curve from start_param to end_param.
                    */
);

/****************************************************************************
Returns an array of line and arc identifiers which approximates
curves and edges. The tolerance parameter determines the maximum
distance between a curve or edge and its approximated arc segments.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_silhouette(
tag_t solid ,/* <I>
             Solid sheet or body to get silhouette curves from
             */
tag_t view ,/* <I>
            View to generate curves in
            */
int* count ,/* <O>
            Count of curves created and returned in the curves array.
            */
tag_t** curves  /* <OF,len:count>
                Array of curves. You are responsible for freeing the
                memory allocated for this array. Use UF_free to
                deallocate memory when done.
                */
);

/*******************************************************************************
A spline curve is created from the data in the spline_data structure.

The spline is a NURBS (NonUniform Rational B-Spline) curve.  See
the description of the structure for a basic description of the data items.

If the is_rational field is nonzero, the weights must be positive.  If it is
0 (non-rational), the weights are ignored.

If the is_spcurve field is nonzero, the Z coordinates are ignored.

NURBS curves need not have Bezier end conditions (be clamped).

NX currently requires that the parameter range of a spline be
0 to 1. The User Function API normalizes the knot vector and returns
a state indicating the parameter transformation thus induced.

The multiplicity of a knot is the number of times the same value
appears in the sequence. The multiplicity of the end knots cannot
exceed the order of the spline; the multiplicity of interior knots cannot
exceed order-1. The knot sequence must be monotonically
increasing.  These problems and degeneracies are fixed using
tolerances assigned by Open API.

Utilities are provided to assist in removing many of these conditions
from your splines using larger tolerances.

Periodicity is determined directly from the spline data by Open API
on create. A periodic spline is identified as follows:

  1.      Evaluate the location and tangent vectors at the start and
          end parameter values.
  2.      If the location vectors are the same, it is closed and is
          made periodic, but it might not be smooth at the closure.
  3.      If the tangent vectors have the same direction, it is smooth
          (G1). If the tangent vectors also have the same length, it is
          parameter smooth (C1).
  4.      If the spline is rational, and it is also C1 in homogeneous
          space, it can be unclamped. If the spline is not rational,
          Cartesian space is equivalent to homogeneous space and
          so it can be unclamped.
  5.      If it can be unclamped, the closure is made  as high as
          the data allows (up to degree - 1). If the closure cannot
          be made C1, it is made G1. If it cannot be made G1, it is
          left closed, but not smooth. (Unclamping applies knot
          removal to both ends of the spline. NX chooses
          knot intervals for this process that yield wrap-around
          control points if the closure is C1.)

The period is determined from the parameter range as defined above,
largest minus smallest allowed values.

If the closure for a periodic curve must be checked using tolerances
larger than Open APIs defaults, use UF_CURVE_smooth_spline_data. If
degeneracies and knot problems must be fixed using tolerances larger
than Open APIs defaults, use UF_CURVE_fix_spline_data.

Specific errors: spline contains fixable problems, or unfixable
problems. An unfixable overrides the fixable return code.

Environment: Internal  and  External

See Also: UF_CURVE_ask_parameterization
          UF_CURVE_fix_spline_data
          UF_CURVE_smooth_spline_data

History: This function was originally released in V15.0.
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_spline (
UF_CURVE_spline_p_t spline_data ,/* <I>
                                 Address of spline structure describing the
                                 desired curve.
                                 */
tag_p_t spline_tag ,/* <O>
                    Tag of curve is returned
                    */
int *num_states ,/* <O>
                Number of entries in states array
                */
UF_CURVE_state_p_t * states  /* <OF,len:num_states>
                             Array of states indicating what kinds of
                             problems are present; if NULL no state
                             return is needed.  This array must be freed
                             by calling UF_free.
                             */
);
/*******************************************************************************
Reads the spline data and puts it in the data structure whose address
is provided.

Environment: Internal  and  External

See Also: UF_CURVE_ask_parameterization

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_spline_data (
tag_t spline_tag ,/* <I>
                  Tag of bspline curve for which to return data
                  */
UF_CURVE_spline_p_t spline_data  /* <OF>
                                 The caller must allocate a UF_CURVE_spline_t
                                 structure.  This routine will fill the
                                 structure in.  The knots and poles members
                                 will be allocated by this routine, and must
                                 be freed by the caller using UF_free, e.g.
                                    UF_free(spline_data->knots);
                                    UF_free(spline_data->poles);
                                 */
);

/****************************************************************************
See the documentation for UF_CURVE_smooth_spline_data for a description of
smoothing.  UF_CURVE_smooth_spline_data_st differs from it only in its
tolerance argument, dist_toler and in the interpretation of the continuity
state distance value.

3D curves are isotropic, that is, they occupy space with the same "density" in
all three directions.  If the curves you are smoothing are always isotropic,
use UF_CURVE_smooth_spline_data.

UF_CURVE_smooth_spline_data_st smooths using a shear tolerance specification,
meaning that it may have different values for x, y, and z.  Use it for
smoothing bcurves destined to become fin curves, which are used to trim
surfaces. (See UF_BREP).

Fin curves are defined in the surface parameter, or SP, space, of some surface
and thus are often called SP curves.  Their existence in 3-space is a
composition of their two-dimensional definition and the 3-dimensional existence
of the surface.  An SP curve defined on a surface has u,v coordinates, with
the third coordinate (normally z) being zero, instead of x, y, z coordinates.
In specifying the coordinates of the bcurves vertices, and the tolerances for
smoothing, the x coordinate is the u value and the y coordinate is the v value.

SP curves for trimming surfaces are anisotropic, that is, not isotropic.  They
do not occupy space with the same "density" in both directions.  Consider a
cylinder, which has a parameterization of part units (mm or in) in u (along
the axis) and angular units (radians) in v (around the axis).  Thus u has the
same dimensions as 3-space, but v does not, indeed the v parameter being
angular causes a dependence on the radius for the correspondence between the v
tolerance in 3D and in parameter space.

Suppose we have a cylinder of radius 10mm, and we want changes from smoothing
restricted to .02mm.  dist_toler[0] = .02 is the tolerance for u.
dist_toler[1] = .02/10 is the tolerance for v (it is not an approximation).
A curve along the surface in v is a circle, and so the distance along the curve
(the 3D tolerance) is equal to the radius times the angle (the v tolerance).
Working the algebra leads to the expression for dist_toler[1].  Similar
methods work for other analytic surface types.  Generally a method that yields
a smaller rather than larger tolerance is preferable, like finding some
approximation to the largest radius of a surface of revolution, or the radius
of a cone at the larger part of where the face occupies the cone.

For a bsurface (which is anisotropic except in some very special cases), it
may be necessary to select a u,v pair, get a point, offset the u,v pair by a
small amount, get another point, and work the proportions to obtain the
u and v deltas that correspond to the desired 3D tolerance.  Surfaces can vary
in their parameterization, and that affects the tolerances obtained.  You have
to gain some knowledge about your surfaces; surfaces made by NX dont contain
variations in parameterization from one part of the surface to another, so
selecting 0.5, 0.5 as the evaluation point should be sufficient.

Note: cont_order values greater than 1 are not currently supported, but may be
specified.

Environment: Internal  and  External

See Also: UF_BREP_attach_geometry
          UF_CURVE_smooth_spline_data
          UF_CURVE_fix_spline_data
          UF_CURVE_create_spline

History:
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_smooth_spline_data_st(
    UF_CURVE_spline_p_t spline_data,    /* <I/O>
                                        spline to smooth
                                        */
    int    cont_order,      /* <I>
                                order of continuity to get
                                */
    double dist_toler[3],     /* <I>
                                dont exceed this, x, y, z
                                */
    double ang_toler,       /* <I>
                                dont exceed this
                                */
    int    *num_states,     /* <O>
                                number of states in states array
                                */
    UF_CURVE_state_p_t *states  /* <OF,len:num_states>
                                states found during smoothing.  The caller is
                                responsible for freeing this by calling UF_free.
                                */
);

/****************************************************************************
Makes a spline continuous to cont_order, if possible.

The order of continuity may be any positive integer up to
(but not including) the degree of the spline (the degree is order-1).

NOTE: cont_order values greater than 1 are not currently supported, but 
may be specified.

Curves created interactively by NX, by creating a curve directly or
through modeling a solid body, do not need this function. Only if you
manage to create a curve with a corner, as by joining two splines, is
it possible to create a curve that would be affected by this function.

The spline must be C0 before calling this function, but it may have 
degeneracies. C0 means continuous to order zero, which means that it
has no gaps. Splines that have end knots with a multiplicity greater than 
the order of the spline, or have interior knots with a multiplicity greater 
than the degree of the spline, may have gaps.  Such splines are not of 
general utility in CAD/CAM work. The creation function 
(UF_CURVE_create_spline) will not create them and this function will 
not smooth them. They can be fixed using UF_CURVE_fix_spline_data, and 
then smoothed if necessary.

Specification of a given cont_order implies that all lower order
continuities are desired. The order of continuity is the
highest order derivative that is required to exist at all points of the
spline. At any point in the spline, if cont_order cannot be achieved,
the highest continuity within tolerance is achieved. If C1 cannot be
achieved, G1 is achieved within tolerance and a state code is returned.
If G1 cannot be achieved a state code is returned. Whatever can be
smoothed within tolerance is returned even if the entire spline cannot
be done. States are returned for all conditions found in the spline.

Any knot that has a multiplicity high enough to make it possible for
the spline to be discontinuous to the given order at the corresponding
pole is checked. If the pole can be treated in such a way as to make it
continuous to the given order without changing the shape more than
toler, it is made so. 

Think of discontinuities as 'corners'. A discontinuity in the first 
derivative is what one most often thinks of as a corner; it is readily 
visualized. A discontinuity in the second derivative is similar to a 
discontinuity in the first derivative, that is, it is a corner, but it 
is a corner in the first derivative. Basically, a knot of multiplicity 
order-n means the curve is potentially discontinuous in the nth derivative.
It now becomes apparent what C0 comes from: it means continuity in the 
'zero-th derivative', referring to the condition introduced by a knot of 
multiplicity order (or greater), which is a potential gap in the curve. 
Open curves, and some closed curves, have knots of multiplicity order at 
the ends, where they are not C0, because, naturally, they stop.

If the spline is closed the closure is also checked and smoothed if
within tolerance.

Continuity is achieved using a mathematical process called knot
removal. Geometric continuity (G1) is achieved by moving the poles.

Use this function conservatively. In particular, if simplification is to 
be done when the geometry is attached or edited on a body topology, be 
aware that smoothing may make the spline's equivalent curve (such as a 
circle) unrecognizable to the simplifier. One of two things might happen:

1. The curve may be modified in its point and knot content so as not to 
match the patterns that the simplifier uses to recognize simplifiable curves, or, 

2. If the smoothing tolerance is large enough, it may be modified so that 
it is out of matching tolerance on the possible simplified curve.

Consult a textbook on NURBS curves (NX splines are NURBS curves) for more 
information on continuity and the interpretaion of the knot vector. One such 
book is "The NURBS Book," by Piegl and Tiller, Springer Verlag, 1995. The 
first 100 pages provide a good grounding.

Environment: Internal  and  External

See Also: UF_BREP_attach_geometry
          UF_CURVE_smooth_spline_data_st
          UF_CURVE_fix_spline_data
          UF_CURVE_create_spline

History: This function was originally released in V15.0.
*******************************************************************************/
extern UFUNEXPORT int UF_CURVE_smooth_spline_data (
UF_CURVE_spline_p_t spline_data ,/* <I/O>
                                 spline data to make continuous
                                 */
int cont_order ,/* <I>
                order of continuity to achieve
                */
double distance_toler ,/* <I>
                       tolerance; smoothing is done if the deviation in
                       shape introduced is less than this amout. Zero
                       indicates use NX modelling resolution.
                       */
double angle_toler ,/* <I>
                    tolerance; smoothing is done if the angle
                    between tangents at the joint is less than this
                    amount. Zero indicates use NX modelling resolution.
                    */
int * num_states ,/* <O>
                  number of states in returned states array
                  */
UF_CURVE_state_p_t * states  /* <OF,len:num_states>
                             Pointer to array pointer for joints where
                             continuity could not be achieved within
                             tolerance.  This must be freed by calling UF_free.
                 May also contain knot fixup states.
                             */
);

/*****************************************************************************
This function scans the spline data for degeneracies, points that are or
potentially are non-C0, and knot values too close together.

If any degeneracies are found, it attempts to fix them by moving one
or more control points. If that is not successful, points and knots will
be removed, reducing the degree if necessary.

If any non-C0 or potentially non-C0 control points are found they
are coerced to C0.

If any two adjacent knot values that are distinct are not separated by
enough, they are fixed.

The fixed-up data are returned in the same memory as the supplied data.

If valid spline data cannot be returned, it means that the data cannot
be represented by a linear line of nonzero length; it is too short.  The
flags in the states return with "WAS" in the name indicate the status
of the input curve data; the output data, if there is no error, is always
valid.  The flag with "IS" in the name indicates the status of the
output curve.

Removing degeneracies and fixing illegal knot vectors may introduce
discontinuities.

Specific errors: spline is completely degenerate.



This Figure shows two possible problems with spline data. (Neither
one is to scale.) In the first case (A), the spline has an illegal knot
multiplicity at value 1. It is not C0: there is a gap between points 2 and
3. It is fixed. If poles 2 and 3 are coincident, the shape of the spline is
not changed. If they are not, the spline is changed, and a state is
returned.

In the second case (B), the spline is fixed by pushing poles 2 and 4
away from 3, if it is possible to do so without causing other problems.
If that would introduce other problems, poles and knots are deleted
until the spline is no longer degenerate.


Environment: Internal  and  External

See Also: UF_BREP_attach_geometry
          UF_CURVE_create_spline

History: This function was originally released in V15.0.
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_fix_spline_data (
UF_CURVE_spline_p_t spl ,/* <I/O>
                         spline data in which to fix degeneracies and
                         knot multiplcities
                         */
double toler ,/* <I>
              tolerance to use for determining degeneracies.
               zero indicates use NX modelling resolution.
              */
int * num_states ,/* <O>
                  number of returned states
                  */
UF_CURVE_state_p_t * states  /* <OF,len:num_states>
                             Pointer to state array pointer to receive state
                             information.  If a NULL pointer value is provided,
                             no states are returned.  The caller is responsible
                             for freeing this by calling UF_free.
                             */
);
/*****************************************************************************
Returns the parameter range and periodicity for any curve or edge.
This function returns the "natural" parameter range.  Arcs, ellipses
and hyperbolas return the start and end angles.

Environment: Internal  and  External

See Also:

History:This function was originally released in V15.0.
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_parameterization (
tag_t object ,/* <I>
              curve or edge for which to return parameterization
              data
              */
double param_range[2] ,/* <O>
                       array into which to return parameter range of the
                       curve
                       */
int * periodicity  /* <O>
                   One of:
                   UF_CURVE_OPEN_CURVE
                   UF_CURVE_CLOSED_PERIODIC_CURVE
                   UF_CURVE_CLOSED_NON_PERIODIC_CURVE
                   */
);


/*****************************************************************************
Returns the angle made up by a curve as it wanders through space.  The angle
is taken on a projection plane defined by the orientation vector.

Environment: Internal  and  External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_curve_turn_angle(
tag_t curve ,/* <I>
             Tag of the curve object.
             */
double orientation[3] ,/* <I>
                        A vector normal to the plane in which the curve
                        should be evaluated.
                        */
double * angle  /* <O>
                Angle in radians.
                */
);

/****************************************************************************
Returns the point on the curve and the requested derivatives.
This function differs from UF_MODL_evaluate_curve in two ways:

The param and deriv_flag are not pointers, and the param value is
specified in the "natural" parameter range of the curve.  For example,
to evaluate an arc, UF_MODL_evaluate_curve takes a parameter
value between 0 and 1, normalized to the parameter range of the arc
when created.  UF_CURVE_evaluate_curve takes a parameter in
radians, in the parameter range given when the arc was created.

This function differs from UF_CURVE_evaluate_curve is that the input is a curve
data structure instead of a curve tag.

Environment: Internal  and  External
See Also: UF_MODL_evaluate_curve
          UF_CURVE_ask_parameterization
          UF_CURVE_evaluate_curve

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_evaluate_curve_structure (
UF_CURVE_struct_t  * curve_data_ptr ,/* <I>
             Data structure of curve to evaluate
             */
double param ,/* <I>
              Parameter value at which to evaluate
              */
int deriv_flag ,/* <I>
                Number of derivatives to evaluate:
                  UF_CURVE_LOC = return the point
                  UF_CURVE_LOC_1STDERV = return the point and 1st derivative
                  UF_CURVE_LOC_1STDERV_2NDDERV = return the point, 1st and
                  2nd derivatives
                */
double *pos_and_deriv  /* <O>
                        Position and derivatives.
                        Dimension of the array = 3 * (deriv_flag+1)
                        */
);

/****************************************************************************
Returns the point on the curve and the requested derivatives.
This function differs from UF_MODL_evaluate_curve in two ways:

The param and deriv_flag are not pointers, and the param value is
specified in the "natural" parameter range of the curve.  For example,
to evaluate an arc, UF_MODL_evaluate_curve takes a parameter
value between 0 and 1, normalized to the parameter range of the arc
when created.  UF_CURVE_evaluate_curve takes a parameter in
radians, in the parameter range given when the arc was created.

Environment: Internal  and  External

See Also: UF_MODL_evaluate_curve
          UF_CURVE_ask_parameterization
          UF_CURVE_evaluate_curve_structure

History:
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_evaluate_curve (
tag_t curve ,/* <I>
             Tag of curve to evaluate
             */
double param ,/* <I>
              Parameter value at which to evaluate
              */
int deriv_flag ,/* <I>
                Number of derivatives to evaluate:
                  UF_CURVE_LOC = return the point
                  UF_CURVE_LOC_1STDERV = return the point and 1st derivative
                  UF_CURVE_LOC_1STDERV_2NDDERV = return the point, 1st and
                  2nd derivatives
                */
double  pos_and_deriv []/* <O,len:3*(deriv_flag+1)>
                        Position and derivatives.
                        Dimension of the array = 3 * (deriv_flag+1)
                        */
);
/************************************************************************
Creates a new joined curve feature that consists of a new spline curve
that represents the input list of joined curves and edges. The curves
can be sketch curves. The curves or edges that you join may not have
gaps.

The Modeling distance and angle tolerance are used to create and
validate the resulting spline curve. The modeling tolerance can be
modified by UF_MODL_set_distance_tolerance or UF_MODL_set_angle_tolerance.

Environment: Internal and  External.

See Also : UF_MODL_set_distance_tolerance
           UF_MODL_set_angle_tolerance
           UF_STRING_p_t AKA string_list
           UF_MODL_init_string_list
           UF_MODL_create_string_list
           UF_MODL_free_string_list

History: This function was originally released in V15.0.
         Creation method has the advanced option in NX3.0.
************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_joined_feature
(
    UF_STRING_p_t  uf_curve_string,         /* <I>
                                            string of input curves.  Use
                                            UF_MODL_init_string_list and
                                            UF_MODL_create_string_list
                                            to create input strings. Use
                                            UF_MODL_free_string_list to free
                                            memory after the string is created.
                                            */
    int            creation_method,         /* <I> 1 - Polynomial Cubic,
                                                   2 - General Spline
                                                   3 = polynomial quintic
                                                   4 = advanced
                                            */
    tag_t          *joined_curve_feature,   /* <O> CRV_JOIN feature */
    int            *status                  /* <O> 0 = Curve has no corners
                                                    1 = Curve has corners */
);

/************************************************************************
Edits a joined curve feature.

Environment: Internal and  External.

See Also : UF_MODL_set_distance_tolerance
           UF_MODL_set_angle_tolerance
           UF_STRING_p_t AKA string_list
           UF_MODL_init_string_list
           UF_MODL_create_string_list
           UF_MODL_free_string_list

History: This function was originally released in V15.0.
         Creation method has the advanced option in NX3.0.
************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_joined_feature
(
    tag_t          joined_curve_feature,    /* <I>
                                            CRV_JOIN feature
                                            */
    UF_STRING_p_t  uf_curve_string,         /* <I>
                                            string of input curves.  Use
                                            UF_MODL_init_string_list and
                                            UF_MODL_create_string_list
                                            to create input strings. Use
                                            UF_MODL_free_string_list to free
                                            memory after the string is created.
                                            */
    int            creation_method,         /* <I>
                                               1 - Polynomial Cubic,
                                               2 - General Spline
                                               3 - polynomial quintic
                                               4 - Advanced
                                            */
    double         tols[3]                  /* <I>
                                            Tolerances
                                                  [0] - distance tol
                                                  [1] - angle tol
                                                  [2] - string tol
                                            */
 );

/****************************************************************************
Returns the parameters of a joined curve feature.

Environment: Internal and  External.

See Also :  UF_STRING_p_t AKA string_list


History: This function was originally released in V15.0
**************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_joined_parms
(
    tag_t          joined_curve_feature,    /* <I>
                                            CRV_JOIN feature
                                            */
    UF_STRING_p_t  uf_curve_string,         /* <OF,free:UF_MODL_free_string_list>
                                            String of input curves.  This must
                                            be freed by calling
                                            UF_MODL_free_string_list.
                                            */
    int            *creation_method,        /* <O>
                                            1 - Polynomial Cubic,
                                            2 - General Spline
                                            */
    double         tols[3]                  /* <O>
                                            Tolerances
                                                  [0] - distance tol
                                                  [1] - angle tol
                                                  [2] - string tol
                                            */
);
/***********************************************************************
Returns the output curves of a curve feature.

Environment: Internal and External.

See Also:

History: This function was originally released in V15.0
***********************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_feature_curves
(
    tag_t          curve_feature_id,       /* <I>
                                           The tag of the curve feature.
                                           */
    int            *num_curves,            /* <O>
                                           The number of curves in the output
                                           array.
                                           */
    tag_t          **feature_curves        /* <OF,len:num_curves>
                                           The array of curves.  This must be
                                           freed by calling UF_free.
                                           */
);
/***************************************************************************
Returns an array of line and arc identifiers which approximates
curves and edges. The tolerance parameter determines the maximum
distance between a curve or edge and its approximated arc segments.
The segments returned are in random order and may not connect
end to end in the order they are returned.

Environment: Internal and  External

See Also:

History: This function was originally released in V15.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_simplified_curve (
    int curves_count,     /* <I>
                          Count of curves and edges
                          */
    tag_t *curves,        /* <I,len:curves_count>
                          Array of curve and edge identifiers
                          */
    double tolerance,     /* <I>
                          Maximum distance from arc segments to curve
                          */
    int *segments_count,  /* <O>
                          Pointer to count of line and arc identifiers
                          */
    tag_t **segments      /* <OF,len:segments_count>
                          Pointer to the returned array of line
                          and arc identifiers.  This must be freed by calling
                          UF_free.
                          */
);
/****************************************************************************
Create an arc or a circle passing through the user specified input points.

Environment: Internal  and  External
See Also:
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_thru_3pts
(
   int     create_flag,     /* <I>
                            flag indicating if an arc or a circle will be
                            created
                            = 1 -> arc will be created
                            = 2 -> circle will be created
                            */
   double  first_point[3],  /* <I>
                            Coordinates of the first point the arc will go
                            through.
                            */
   double  second_point[3], /* <I>
                            Coordinates of the second point the arc will go
                            through.
                            */
   double  third_point[3],  /* <I>
                            Coordinates of the third point the arc will go
                            through.
                            */
   tag_t   *arc_tag         /* <O>
                            Identifier of the arc or circle that is created
                            */
);

/*************************************************************************************


 Create shadow outline for a given array of solids. Solids passed to this
 routine must be on a selectable layer and visible. If created shadow curves
 can not form loops, please use UF_CURVE_create_shadow_curves instead to get
 shadow curves.

Environment: Internal and External
History Released in V15.0.3
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_shadow_outline
(
 int     solid_count, /*<I>
                       Number of solids to shadow
                       */
 tag_t  *solid_array, /*<I,len:solid_count>
                       Array of Solids to Shadow
                       */

 tag_t   view,       /*<I>
                       View tag to project to
                       */

 int    *loop_count,  /* <O>
                       Number of shadow loops obtained
                       */
 int    **count_array, /* <OF,len:loop_count>
                        Number of curves in each loop - freed by user
                       */
 tag_t ***curve_array, /* <OF,len:count_array>
                        Array of curve loops.  Each element of this array is
                        a pointer to an array of tags which make up one of the
                        shadow loops.  So curve_array[0] is a pointer to a
                        tag_t *, which contains count_array[0] tags that make
                        up the first shadow loop.  This must be freed by the
                        caller using prior freeing the entire array. Thus the
                        caller must free the sequence of curves starting with
                        curve_array[0] , curve_array[1] etc.

                        */
 double  tol[2]         /* <I> tol[0] - the tolerance for loops tol[1] - tol for angle
                        projection */

);

/*************************************************************************************
Function:             UF_CURVE_create_shadow_curves
Purpose:              Create curves for the shadow of a group of bodies in a view

Environment: Internal and External
History Released in NX 5.0.5

*************************************************************************************/

extern UFUNEXPORT int UF_CURVE_create_shadow_curves
(
int      solid_count, /*<I>
                       Number of solid bodies to shadow
                       */
tag_t    *solid_array, /*<I,len:solid_count>
                       Array of solid_body tags
                       */
tag_t    view_tag,    /* <I>
                       Tag of view for shadow
                       */
int      *shadow_curve_count, /*<O>
                               Number of curves created
                               */
tag_t    **shadow_curves      /*<OF,len:shadow_curve_count>
                               Array of curve tags.  This must be freed by the caller.
                               */
);


/****************************************************************************
Trim or extend the length of a user specified curve.  If the method is 1,
and the length is positive, the curve is extended.  If the method is 1,
and the length is negative, the curve is trimmed.  If the method is 2, the curve
will be extended or trimmed as needed to make the total curve length equal to
the specified length.

Note: When this function is used on a regular spline, it will change the
length of that particular spline.  However, when it is used on a spline feature,
it will create a new spline of the appropriate length, leaving the original intact.

Environment: Internal  and  External
See Also:
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_length (
    tag_t   curve,     /* <I>
                       tag of curve to trim
                       */
    int     method,    /* <I>
                       trim/extend method, increment or total curve length
                       = 1 -> trim/extend the curve incrementally by the
                              specified curve length
                       = 2 -> trim/extend the curve by making the total curve
                              length as the specified curve length
                       */
    double  length,    /* <I>
                       incremental or total curve length
                       */
    int     location,  /* <I>
                       Flag to indicate which end of the curve would be edited
                       = 1 -> start of curve
                       = 2 -> end of curve
                       = 3 -> both sides of curve - if method = 1, it will
                              extend/trim both ends by one half of the length - if method = 2,
                              it will determing how much the curve needs to be extended/trimmed,
                              and then apply half of that distance to both ends.
                       */
    int     ext_type   /* <I>
                       Shape of the extension of the curve. It can be either
                       of the following:
                       = UF_CURVE_NATURAL_SHAPE
                       = UF_CURVE_LINEAR_SHAPE
                       = UF_CURVE_CIRCULAR_SHAPE
                       */
);

/****************************************************************************
Create an associative trim curve feature.

Environment: Internal  and  External

See Also:

History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_trim (
    UF_CURVE_trim_p_t       trim_info,      /* <I>
                                               Information defining trim curve
                                               feature desired
                                            */
    UF_CURVE_trim_mult_p_t  out_info,       /* <OF>
                                               If the return value is
                                               UF_CURVE_TRIM_MULT_PTS
                                               then this structure will
                                               contain information about
                                               multiple intersection points
                                               for each boundary. The caller
                                               can then pass the desired point
                                               in through the suggested_point
                                               field.
                                            */
    tag_t                   *trim_feature   /* <O>
                                               Created trim curve feature
                                            */
);

/****************************************************************************
Retrieve the current parameters of an associative trim curve feature.

Environment: Internal  and  External

See Also: 

History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_trim (
    tag_t              trim_feature,     /* <I>
                                         Trim curve feature whose parameters
                                         are to be retrieved
                                         */
    UF_CURVE_trim_p_t  trim_info         /* <OF,free:UF_CURVE_free_trim>
                                         Information defining the trim curve
                                         features current parameters, the
                                         caller should free allocated memory
                                         in this structure by calling
                                         UF_CURVE_free_trim
                                         */
);

/****************************************************************************
Change the parameters of an associative trim curve feature to the parameters
supplied

Environment: Internal  and  External

See Also: 

History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_trim (
    tag_t              trim_feature,     /* <I>
                                         Trim curve feature whose parameters
                                         are to be changed
                                         */
    UF_CURVE_trim_p_t  trim_info         /* <I>
                                         Information defining the trim curve
                                         features desired parameters
                                         */
);

/****************************************************************************
Free the memory within the UF_CURVE_trim_p_t structure that was allocated
by a call to UF_CURVE_ask_trim

Environment: Internal  and  External

See Also: 

History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_CURVE_free_trim (
    UF_CURVE_trim_p_t  trim_info         /* <I>
                                         Information defining the trim curve
                                         features parameters that was
                                         generated by a call to
                                         UF_CURVE_ask_trim
                                         */
);/*<NON_NXOPEN> */

/****************************************************************************
Creates a new bridge curve feature by bridging 2 input curves.
You can control the connection of the bridge curve along the two curves by
specifying the parameter along each curve. You have the ability to
reverse the tangent direction vector at the parameter along the curves.
You can control the shape of the curve by specifing a reference curve
or by indicating shape control values.

The routine returns the object identifier of the new bridge curve feature.
The new bridge curve is associative to the input curves and any expressions
used to determine shape or end point location.

Environment: Internal  and  External

See Also :  UF_CURVE_edit_bridge_feature
            UF_CURVE_ask_bridge_feature

History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_bridge_feature
(
   UF_CURVE_bridge_data_p_t bridge_data,     /* <I>
                                             Input parameters
                                             */
   tag_p_t                  bridge_feature   /* <O>
                                             Object identifier of the bridge
                                             curve feature.
                                             */
);

/****************************************************************************
Edit a bridge curve feature

Environment: Internal  and  External

See Also :  UF_CURVE_create_bridge_feature
            UF_CURVE_ask_bridge_feature

History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_bridge_feature
(
   tag_t                   bridge_feature, /* <I>
                                           Object identifier of the bridge curve
                                           feature
                                           */
   UF_CURVE_bridge_data_p_t bridge_data    /* <I>
                                           Parameters that new bridge curve
                                           feature should have.
                                           */
);

/****************************************************************************
Inquire a bridge curve feature

Environment: Internal  and  External

See Also :  UF_CURVE_create_bridge_feature
            UF_CURVE_edit_bridge_feature

History: Originally released in V16.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_bridge_feature
(
   tag_t                    bridge_feature,  /* <I>
                                             Object identifier of the bridge cur
ve feature
                                             */
   UF_CURVE_bridge_data_p_t bridge_data      /* <I/O>
                                             Parameters of bridge curve feature
                                             */
);


/****************************************************************************

Creates an associative section curve feature or non-associative
group of section curves using an array of planes.

NOTE - If an object in the general data objects array is not fully loaded,
the section curve will not be created for that object.


See the example below for a sample execution of this function.

Environment:  Internal and External

See Also:
     UF_CURVE_section_ask_planes_data
     UF_CURVE_section_from_parallel_planes
     UF_CURVE_section_ask_parallel_data
     UF_CURVE_section_from_radial_planes
     UF_CURVE_section_ask_radial_data
     UF_CURVE_section_from_perpcrv_planes
     UF_CURVE_section_ask_perpcrv_data
     UF_CURVE_section_ask_type
     UF_CURVE_section_curve_ask_parents
     UF_CURVE_ask_feature_curves
     UF_CURVE_create_int_object
     UF_MODL_intersect_objects



History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_from_planes (

    UF_CURVE_section_general_data_p_t    general_data,  /* <I> Data provided
                                                          by the user to to be
                                                          used in creating the
                                                          section curve feature.
                                                        */

    UF_CURVE_section_planes_data_p_t    planes_data,    /*<I>  Sectioning planes
                                                          and datum planes.*/

    tag_t    *section_curves      /* <O>
                  Feature tag, if general_data->associate is 1, or
                  Group tag of section curves if general_data->associate is 0
                                       and general_data->grouping is 0, or
                  Group tag of groups of curves if general_data->associate is 0
                                       and general_data->grouping is 1  */
);


/****************************************************************************

Creates an associative section curve feature or non-associative
group of section curves using a set of parallel planes.

NOTE - If an object in the general data objects array is not fully loaded,
the section curve will not be created for that object.

Environment:  Internal and External

See Also:

    See  UF_CURVE_section_from_planes for a list of related functions.

History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_from_parallel_planes (

    UF_CURVE_section_general_data_p_t    general_data,  /* <I> Data provided
                                                          by the user to to be
                                                          used in creating the
                                                          section curve feature.
                                                        */
    UF_CURVE_section_parallel_data_p_t   parallel_data,  /* <I> Data provided
                                                          by the user describing
                                                          the parallel planes.
                                                         */

    tag_t    *section_curves      /* <O>
                  Feature tag, if general_data->associate is 1, or
                  Group tag of section curves if general_data->associate is 0
                                       and general_data->grouping is 0, or
                  Group tag of groups of curves if general_data->associate is 0
                                       and general_data->grouping is 1  */
);

/****************************************************************************

Creates an associative section curve feature or non-associative
group of section curves using a set of radial planes.

NOTE - If an object in the general data objects array is not fully loaded,
the section curve will not be created for that object.

Environment:  Internal and External

See Also:

    See  UF_CURVE_section_from_planes for a list of related functions.

History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_from_radial_planes (

    UF_CURVE_section_general_data_p_t    general_data,  /* <I> Data provided
                                                          by the user to to be
                                                          used in creating the
                                                          section curve feature.
                                                        */

    UF_CURVE_section_radial_data_p_t     radial_data,  /* <I> Data provided by
                                                          the user describing
                                                          the radial planes. */

    tag_t    *section_curves      /* <O>
                  Feature tag, if general_data->associate is 1, or
                  Group tag of section curves if general_data->associate is 0
                                       and general_data->grouping is 0, or
                  Group tag of groups of curves if general_data->associate is 0
                                       and general_data->grouping is 1  */
);


/****************************************************************************

Creates an associative section curve feature or non-associative
group of section curves using a set of planes perpendicular to a
curve.

NOTE - If an object in the general data objects array is not fully loaded,
the section curve will not be created for that object.

Environment:  Internal and External

See Also:

    See  UF_CURVE_section_from_planes for a list of related functions.

History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_from_perpcrv_planes (

    UF_CURVE_section_general_data_p_t    general_data,  /* <I> Data provided
                                                          by the user to to be
                                                          used in creating the
                                                          section curve feature.
                                                        */

    UF_CURVE_section_perpcrv_data_p_t    perpcrv_data, /* <I> Data provided
                                                          by the user describing
                                                          the perpendicular
                                                          curves.  */

    tag_t    *section_curves      /* <O>
                  Feature tag, if general_data->associate is 1, or
                  Group tag of section curves if general_data->associate is 0
                                       and general_data->grouping is 0, or
                  Group tag of groups of curves if general_data->associate is 0
                                       and general_data->grouping is 1  */
);


/****************************************************************************

Given a section curves feature, this function returns
the type of planes used in the sectioning.

Return
     0 if no error
     WRONG_FEATURE_TYPE   if not a section curves feature

Environment:  Internal and External

See Also:

    See  UF_CURVE_section_from_planes for a list of related functions.

History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_ask_type (
         tag_t    section_curves_feature,    /* <I>  The tag of the section
                                                curves feature to inquire. */
         int         *plane_type      /* <O> The plane type:
                                        0 for an array of planes
                                        1 for parallel planes
                                        2 for radial planes
                                        3 for planes perpendicular to a curve
                                      */
);


/****************************************************************************
Outputs the defining data structures for a section curves feature
defined using an array of planes.

Environment:  Internal and External

See Also:

    See  UF_CURVE_section_from_planes for a list of related functions.

History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_ask_planes_data (
    tag_t            section_curves_feature,    /* <I>  The section curve
                                                   feature to inquire about. */
    UF_CURVE_section_general_data_p_t    general_data,   /* <OF>
                     The general data describing this section curve feature.
                     Use UF_free to free the array,  general_data->objects
                                                                   */
    UF_CURVE_section_planes_data_p_t     planes_data     /* <OF>
                     The section planes data describing this feature.
                     Use UF_free to free the array,  planes_data->planes  */
);


/****************************************************************************

Outputs the defining data structures for a section curves feature
defined using a set of parallel planes.

Environment:  Internal and External

See Also:

    See  UF_CURVE_section_from_planes for a list of related functions.

History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_ask_parallel_data (
    tag_t            section_curves_feature,    /* <I>  The section curve
                                                   feature to inquire about. */
    UF_CURVE_section_general_data_p_t    general_data,   /* <OF>
                     The general data describing this section curve feature.
                     Use UF_free to free the array,  general_data->objects
                                                                   */
    UF_CURVE_section_parallel_data_p_t   parallel_data   /* <O> The data defining
                                                            the parallel planes
                                                            for this feature.  */
);


/****************************************************************************

Outputs the defining data structures for a section curves feature
defined using a set of radial planes.

Environment:  Internal and External

See Also:

    See  UF_CURVE_section_from_planes for a list of related functions.

History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_ask_radial_data (
    tag_t            section_curves_feature,    /* <I>  The section curve
                                                   feature to inquire about. */
    UF_CURVE_section_general_data_p_t    general_data,   /* <OF>
                     The general data describing this section curve feature.
                     Use UF_free to free the array,  general_data->objects
                                                                   */
    UF_CURVE_section_radial_data_p_t     radial_data   /* <O> The data defining the
                                                            radial planes for
                                                            this feature.  */
);


/****************************************************************************

Outputs the defining data structures for a section curves feature
defined using a set of planes perpendicular to a curve.

Environment:  Internal and External

See Also:

    See  UF_CURVE_section_from_planes for a list of related functions.

History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_ask_perpcrv_data (
    tag_t            section_curves_feature,    /* <I>  The section curve
                                                   feature to inquire about. */
    UF_CURVE_section_general_data_p_t    general_data,   /* <OF>
                     The general data describing this section curve feature.
                     Use UF_free to free the array,  general_data->objects
                                                                   */
    UF_CURVE_section_perpcrv_data_p_t    perpcrv_data    /* <O> The data defining
                                                            the set of planes
                                                            perpendicular to a curve
                                                            for this feature.  */
);



/****************************************************************************

Given a section curve, this function returns the section curves
feature, if any, and the defining object and sectioning objects.

Return
     0 if no error
     WRONG_FEATURE_TYPE if not a section curves feature

Environment:  Internal and External

See Also:

    See  UF_CURVE_section_from_planes for a list of related functions.

History: Originally released in V17.0
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_section_curve_ask_parents (
    tag_t            section_curve, /*  <I>  The section curve to inquire. */

    tag_t            *section_curves_feature,    /* <O>
                                                 The section curves feature, or
                                                 NULL_TAG, if none.
                                                 */
    int  *plane_type,             /*  <O> The plane type:
                                             0 for array of planes
                                             1 for parallel planes
                                             2 for radial planes
                                             3 for planes perpendicular to a
                                               curve.
                                  */
    tag_t *defining_object,       /* <O> The object sectioned. */
    tag_t sectioning_objects[2]   /* <O> The sectioning objects

                                             For plane_type = 0:
                                          sectioning_objects[0] = plane eid
                                          sectioning_objects[1] = NULL_TAG

                                      For plane_type = 1:
                                          sectioning_objects[0] = base plane
                                          sectioning_objects[1] = NULL_TAG

                                      For plane_type = 2:
                                          sectioning_objects[0] = datum axis eid
                                          sectioning_objects[1] = point on plane

                                      For plane_type = 3:
                                          sectioning_objects[0] = curve eid
                                          sectioning_objects[1] = plane eid
                                                       (NULL_TAG if none)
                                    */
);


/*****************************************************************************
Edit a B-curve with the spline order and knot vector taken from a
  template curve, when possible.

RESTRICTIONS -

1.  In some cases the edit curve cannot be edited with the selected template
      curve.  In these cases the spline order and knot vector of the edited
      curve are different from the template curve, and the edited curve is
      interpolated.  These cases are distinguished by the error_data parameter.

Failure return code: TEMPLATE_CURVE_UNABLE_TO_EDIT

Environment: Internal  and  External
See Also: UF_MODL_create_curve_mesh1 and UF_MODL_create_thru_curves1
     UF_MODL_create_curve_mesh1
     UF_MODL_create_thru_curves1
History: Originally released in V16.0
*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_with_template
(
    tag_t edit_id, /* <I>
           Curve to edit
           */
    tag_t template_id, /* <I>
                   Template curve
                 Spline order and knot vector are taken from template
                 curve
               */
    UF_CURVE_fit_error_p_t error_data /* <O>
                      Error data returned by edit with template.
                      */
);

/*****************************************************************************

  Create a general spline feature. Output the feature id.

  Return: error code

  Environment:  Internal and External

  See Also:

     UF_CURVE_edit_spline_feature
     UF_CURVE_ask_spline_feature

  History: Originally released in V18.0

*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_spline_feature
(
    tag_t  spline,       /* <I> object id of a smart spline */
    tag_t  *feature_id   /* <O> pointer to object id of the spline feature */
);

/*****************************************************************************

  Edit a general spline feature.

  Return: error code

  Environment:  Internal and External

  See Also:

      UF_CURVE_create_spline_feature
      UF_CURVE_ask_spline_feature

  History: Originally released in V18.0

*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_spline_feature
(
    tag_t  spline,       /* <I> object id of a new smart spline */
    tag_t  feature_id    /* <I> object id of the spline feature being edited */
);

/*****************************************************************************

  Inquire a general spline feature.
  Output object id of the referenced smart spline.

  Return: error code

  Environment:  Internal and External

  See Also:

      UF_CURVE_create_spline_feature
     UF_CURVE_edit_spline_feature

  History: Originally released in V18.0

*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_spline_feature
(
    tag_t  feature_id,  /* <I> object id of the spline feature */
    tag_t  *spline      /* <O> pointer to object id of the referenced
                           smart spline */
);

/*****************************************************************************

  Determine intersection between curve/edge and a
  curve/edge/face/single face body/plane/datum plane. The intersection
  will be done in the orientation of the current WCS when the entity
  is a curve/edge otherwise in 3D. If the intersection is an actual
  3D intersection then that information will be output. Also the intersection
  between the naturally extended version of the curve or edge will be
  returned if needed, however, only a curve(the first calling parameter) will be extended when the
  entity(the second calling parameter) is something other than a curve/edge.
  
  For curve (the first calling parameter) of UF_line_type or UF_spline_type, a return parameter greater than 0 or
  less than 1, indicates that the itersection is on the natural extension of the curve. 

  Return: error code

  Environment:  Internal and External

  History: Originally released in V18.0

*****************************************************************************/
extern UFUNEXPORT int UF_CURVE_intersect
(
    tag_t  curve,             /* <I> object id of the curve or edge  */
    tag_t  entity,            /* <I> object id of the curve, edge, face,
                                 single face body, plane or datum plane */
    double ref_point[3],      /* <I> reference point to select from
                                 multiple intersections, intersection closest
                                 to this point will be output */
    UF_CURVE_intersect_info_p_t out_info /* <O> - intersection information */
);

/******************************************************************************
Create an associative line/arc feature. You input a UF_CURVE_line_arc_t data structure,
which specified the data needed for the line/arc to be created. Output is the
object identifier of the associative line/arc feature. An error is returned if
line/arc cannot be created with the specified data.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_edit_line_arc
            UF_CURVE_ask_line_arc_data
            UF_CURVE_ask_line_arc_output
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_line_arc
(
    UF_CURVE_line_arc_t  *line_arc_data, /* <I> Pointer to line/arc data structure */
    tag_t * line_arc_feat_id  /* <O> Object identifier of new associative line/arc feature.
                                if is_asso == TRUE - object identifier of new associative line/arc feature.
                                if is_asso == FALSE - object identifier of new line/arc  */
);

/******************************************************************************
Populates the supplied pointer to line_arc_data struct for the given
associative line/arc feature.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
            UF_CURVE_edit_line_arc
            UF_CURVE_ask_line_arc_output

History:
******************************************************************************/

extern UFUNEXPORT int UF_CURVE_ask_line_arc_data
(
    tag_t  line_arc_feat_id,  /* <I> Object identifier of associative line/arc feature. */
    UF_CURVE_line_arc_t  *line_arc_data /* <O> Pointer to line/arc data structure to be filled up. */
);

/******************************************************************************
Edits an existing associative line/arc feature. An error is returned if
line/arc cannot be created with the specified data.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
            UF_CURVE_ask_line_arc_data
            UF_CURVE_ask_line_arc_output

History:
******************************************************************************/

extern UFUNEXPORT int UF_CURVE_edit_line_arc
(
    tag_t  line_arc_feat_id,  /* <I> Object identifier of associative line/arc feature. */
    UF_CURVE_line_arc_t  *line_arc_data /* <I> Pointer to line/arc data structure to be filled up. */
);

/******************************************************************************
Returns the ID of the line/arc created by the associative line/arc feature.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
            UF_CURVE_edit_line_arc
            UF_CURVE_ask_line_arc_data

History:
******************************************************************************/

extern UFUNEXPORT int UF_CURVE_ask_line_arc_output
(
    tag_t  line_arc_feat_id,  /* <I> Object identifier of associative line/arc feature. */
    tag_t  *line_arc_id     /* <O> Id of the line/arc created by the feature. */
);

/******************************************************************************
Create an associative line feature through two points.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_line_point_point
(
    tag_t point1, /* <I> tag of start point */
    tag_t point2, /* <I> tag of end point */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the line */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t line_feature_id /* <O> if is_asso == TRUE - object identifier of new associative line feature
                                   if is_asso == FALSE - object identifier of new associative line */
);
/******************************************************************************
Create an associative line feature through point and tangent to curve.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_line_point_tangent
(
    tag_t point, /* <I> tag of start point */
    tag_t tangent, /* <I> tag of tangent object*/
    UF_CURVE_help_data_p_t help_data_p, /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the line */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t line_feature_id /* <O> if is_asso == TRUE - object identifier of new associative line feature
                                   if is_asso == FALSE - object identifier of new associative line */
);

/******************************************************************************
Create an associative line feature tangent to a curve and through a point.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_line_tangent_point
(
    tag_t tangent, /* <I> tag of tangent object */
    tag_t point, /* <I> tag of end point */
    UF_CURVE_help_data_p_t help_data_p, /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the line */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t line_feature_id /* <O> if is_asso == TRUE - object identifier of new associative line feature
                                   if is_asso == FALSE - object identifier of new associative line */
);

/******************************************************************************
Create an associative line feature through a point and at an angle to a linear curve/edge.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_line_point_angle
(
    tag_t point, /* <I> tag of start point */
    tag_t angle_object, /* <I> tag of angle object */
    double angle_value, /* <I> value of angle in degree */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the line */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t line_feature_id /* <O> if is_asso == TRUE - object identifier of new associative line feature
                                   if is_asso == FALSE - object identifier of new associative line */
);

/******************************************************************************
Create an associative line feature through a point and along any one principal axis.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_line_point_principal_axis
(
    tag_t point, /* <I> tag of start point */
    UF_CURVE_principal_axis_type_t principal_axis, /* <I> one of the 3 principal axes : UF_CURVE_X_AXIS, UF_CURVE_Y_AXIS, UF_CURVE_Z_AXIS */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the line */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t line_feature_id /* <O> if is_asso == TRUE - object identifier of new associative line feature
                                   if is_asso == FALSE - object identifier of new associative line */
);

/******************************************************************************
Create an associative arc feature through three points.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_3point
(
    tag_t point1, /* <I> tag of start point */
    tag_t point2, /* <I> tag of end point */
    tag_t point3, /* <I> tag of middle point */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);
/******************************************************************************
Create an associative arc feature through two points and of specific radius.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_point_point_radius
(
    tag_t point1, /* <I> tag of start point */
    tag_t point2, /* <I> tag of end point */
    double radius, /* <I> value of radius */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id/* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                 if is_asso == FALSE - object identifier of new associative arc */
);
/******************************************************************************
Create an associative arc feature through one point, tangent to a curve and of specific radius.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_point_tangent_radius
(
    tag_t point, /* <I> tag of start point */
    tag_t tangent_object, /* <I> tag of tangent object at end */
    double radius, /* <I> value of radius */
    UF_CURVE_help_data_p_t help_data_p, /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature tangent to two curves and of specific radius.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_tangent_tangent_radius
(
    tag_t tangent_object1, /* <I> tag of tangent object at start */
    tag_t tangent_object2, /* <I> tag of tangent object at end */
    double radius, /* <I> value of radius */
    UF_CURVE_help_data_p_t help_data_p[2], /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature through two points and tangent to a curve.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_point_point_tangent
(
    tag_t point1, /* <I> tag of start point */
    tag_t point2, /* <I> tag of end point */
    tag_t tangent_object, /* <I> tag of tangent object at middle */
    UF_CURVE_help_data_p_t help_data_p, /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature through two points and tangent to a curve.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_point_tangent_point
(
    tag_t point1, /* <I> tag of start point */
    tag_t tangent_object, /* <I> tag of tangent object at end */
    tag_t point2, /* <I> tag of middle point */
    UF_CURVE_help_data_p_t help_data_p, /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature through two points and tangent to a curve.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_tangent_point_point
(
    tag_t tangent_object, /* <I> tag of tangent object at start */
    tag_t point1, /* <I> tag of end point */
    tag_t point2, /* <I> tag of middle point */
    UF_CURVE_help_data_p_t help_data_p, /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature through a point and tangent to two curves.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_point_tangent_tangent
(
    tag_t point, /* <I> tag of start point */
    tag_t tangent_object1, /* <I> tag of tangent object at end */
    tag_t tangent_object2, /* <I> tag of tangent object at middle */
    UF_CURVE_help_data_p_t help_data_p[2], /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature through a point and tangent to two curves.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_tangent_point_tangent
(
    tag_t tangent_object1, /* <I> tag of tangent object at start */
    tag_t point, /* <I> tag of end point */
    tag_t tangent_object2, /* <I> tag of tangent object at middle */
    UF_CURVE_help_data_p_t help_data_p[2], /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature through a point and tangent to two curves.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_tangent_tangent_point
(
    tag_t tangent_object1, /* <I> tag of tangent object at start */
    tag_t tangent_object2, /* <I> tag of tangent object at end */
    tag_t point, /* <I> tag of middle point */
    UF_CURVE_help_data_p_t help_data_p[2], /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature through tangent to three curves.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_3tangent
(
    tag_t tangent_object1, /* <I> tag of tangent object at start */
    tag_t tangent_object2, /* <I> tag of tangent object at end */
    tag_t tangent_object3, /* <I> tag of tangent object at middle */
    UF_CURVE_help_data_p_t help_data_p[3], /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature through a start point and specific center.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_point_center
(
    tag_t point, /* <I> tag of start point */
    tag_t center, /* <I> tag of center */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature tangent to a curve and specific center.

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_center_tangent
(
    tag_t center, /* <I> tag of center */
    tag_t tangent, /* <I> tag of tangent at start */
    UF_CURVE_help_data_p_t help_data_p, /* <I> help data for tangent */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);

/******************************************************************************
Create an associative arc feature of given radius and specific center

Return: error code

Environment: Internal  and  External

See Also :  UF_CURVE_create_line_arc
History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_create_arc_center_radius
(
    tag_t center, /* <I> tag of center */
    double radius, /* <I> value of radius */
    tag_t help_point, /* <I> point to define the start orientation */
    UF_CURVE_limit_p_t limit_p[2], /* <I> extension limits */
    tag_t support_plane, /* <I> tag of support plane of the arc */
    logical is_asso, /* <I> true - if associative, false - if not associative */
    tag_p_t arc_feature_id /* <O> if is_asso == TRUE - object identifier of new associative arc feature
                                  if is_asso == FALSE - object identifier of new associative arc */
);


/******************************************************************************
Test whether two lines are geometrically different

Return: 0 - Two Lines are geometrically identical
        1 - Two Lines are geometrically different

Environment: Internal and External

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_LINE_ARC__is_line_equal
(
    tag_t line1, /* <I> tag of line 1 */
    tag_t line2  /* <I> tag of line 2 */
); /*<NEC>*/

/******************************************************************************
Test whethere two arcs are geometrically different

Return: 0 - Two Arcs are geometrically identical
        1 - Two Arcs are geometrically different

Environment: Internal and External

History:
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_LINE_ARC__is_arc_equal
(
    tag_t arc1, /* <I> tag of arc 1 */
    tag_t arc2  /* <I> tag of arc 2 */
);/*<NEC>*/

/*
 ******************************************************************************
 ******************************************************************************
 *****     WARNING:  The routines that follow will be obsoleted soon.      *****
 *****     Do not use them!  Use their indicated replacements.             *****
 ******************************************************************************
 ******************************************************************************
*/

/* uf5063 create an arc through three points
   replaced by UF_CURVE_create_arc_thru_3pts */
extern UFUNEXPORT void FTN(uf5063)(int *ip1, double *rp2, double *rp3,
                        double *rp4, tag_t *nr5);

/* uf5070 create conic
   replaced by UF_CURVE_convert_conic_to_std and UF_CURVE_create_conic */
extern UFUNEXPORT void FTN(uf5070)(double *rp1, double *rp2, double *rp3, double *rp4,
double *rp5, double *rp6, double *ra7, double *ra8, double *rp9, tag_t *nr10);

/* uf5071 read conic real data
   replaced by UF_CURVE_ask_conic_data */
extern UFUNEXPORT void FTN(uf5071)(tag_t *np1, double *rar2);

/* uf5072 edit conic real data
   No replacement */
extern UFUNEXPORT void FTN(uf5072)(tag_t *np1, double *ra2);

/* uf5072x edit conic real data  without update
   No Replacement */
extern UFUNEXPORT void FTN(uf5072x)(tag_t *np1, double *ra2);

/* uf5073 read conic data
   Replaced by UF_CURVE_ask_conic_data and UF_CURVE_convert_conic_to_gen */
extern UFUNEXPORT void FTN(uf5073)(tag_t *np1, double *rr2, double *rr3, double *rr4,
double *rr5, double *rr6, double *rr7, double *rar8, double *rar9,
double *rr10);

/* uf5074 edit conic data
   No Replacement */
extern UFUNEXPORT void FTN(uf5074)(tag_t *np1, double *rp2, double *rp3, double *rp4,
double *rp5, double *rp6, double *rp7, double *ra8, double *ra9, double *rp10);

/* uf5074x edit conic data  without update
   No Replacement */
extern UFUNEXPORT void FTN(uf5074x)(tag_t *np1, double *rp2, double *rp3, double *rp4,
double *rp5, double *rp6, double *rp7, double *ra8, double *ra9, double *rp10);

/* uf5075 create conic
   Replaced by UF_CURVE_create_conic */
extern UFUNEXPORT void FTN(uf5075)(int *ip1, double *rp2, tag_t *np3, tag_t *nr4);

/* uf5080 create spline
   Replace by UF_CURVE_create_spline_thru_pts */
extern UFUNEXPORT void FTN(uf5080)(int *ip1, int *ip2, double *rp3, tag_t *nr4);

/* uf5081 create spline using complete definition
   Replaced by UF_CURVE_create_spline_thru_pts */
extern UFUNEXPORT void FTN(uf5081)(int *ip1, int *ip2, double *rp3, double *rp4,
double *rp5, tag_t *nr6);

/* uf5082 read spline data
   Replaced by UF_CURVE_ask_spline_thru_pts */
extern UFUNEXPORT void FTN(uf5082)(tag_t *np1, int *ip2, double *rr3, double *rar4,
double *rar5);

/* uf5083 edit spline data
   Replaced by UF_CURVE_edit_spline_thru_pts and
UF_CURVE_edit_move_mult_points*/
extern UFUNEXPORT void FTN(uf5083)(tag_t *np1, int *ip2, double *rp3, double *ra4,
double *ra5);

/* uf5083x edit spline data without update
   No Replacement */
extern UFUNEXPORT void FTN(uf5083x)(tag_t *np1, int *ip2, double *rp3, double *ra4,
double *ra5);


/* uf5084 add spline knot point
   Replaced by UF_CURVE_ask_spline_thru_pts and UF_CURVE_edit_spline_thru_pts*/
extern UFUNEXPORT void FTN(uf5084)(tag_t *np1, double *rp2, double *ra3, double *ra4);

/* uf5085 count spline knot points
   Replaced by UF_CURVE_ask_spine_thru_pts */
extern UFUNEXPORT int FTN(uf5085)(tag_t *np1);

/* uf5445 create spline
   Replaced by UF_MODL_create_spline */
extern UFUNEXPORT void FTN(uf5445)(int *ip1, int *ip2, int *ip3, int *ip4, double *rp5,
double *rp6, tag_t *nr7);

/* uf5446 read spline data
   No Replacement */
extern UFUNEXPORT void FTN(uf5446)(tag_t *np1, int *ir2, int *ir3, int *ir4, int *ir5,
double *rr6, double *rr7);

/* uf5447 create spline from points on curve or
   Replace by UF_CURVE_create_spline_thru_pts and UF_CURVE_create_spline */
extern UFUNEXPORT void FTN(uf5447)(int *ip1, int *ip2, int *ip3, int *ip4, double *rp5,
double *rp6, tag_t *nr7, int *ir8);

/* uf5463 reads the count of poles
   No Replacement */
extern UFUNEXPORT void FTN(uf5463)(tag_t *np1, int *ir2, int *ir3);

/* uf5466 create a spline from a curve
   Replaced by UF_CURVE_create_joined_curve */
extern UFUNEXPORT void FTN(uf5466)(tag_t *np1, int *ip2, tag_t *nr3, int *ir4);


/***************************************************************************
   Curve utilities
  ***************************************************************************/

/* uf5900 evaluate point on a curve
   Replaced by UF_CURVE_evaluate_curve or UF_MODL_ask_curve_props */
extern UFUNEXPORT void FTN(uf5900)(tag_t *np1, double *rp2, double *rr3);

/* uf5901 evaluate curve point data
   Replaced by UF_CURVE_evaluate_curve or UF_MODL_ask_curve_props */
extern UFUNEXPORT void FTN(uf5901)(tag_t *np1, double *rp2, double *rr3);

/* uf5903 trim curve by a given arclength
   Replaced by UF_CURVE_edit_length */
extern UFUNEXPORT void FTN(uf5903)(tag_t *np1, int *ip2, double *rp3, int *ip4, double *rp5
, int *ir6);

/* uf5910 evaluate point on a face
   Replaced by UF_MODL_ask_face_props */
extern UFUNEXPORT void FTN(uf5910)(int *np1, double *rp2, double *rr3);

/* uf5911 evaluate face point data
   Replaced by UF_MODL_ask_face_props */
extern UFUNEXPORT void FTN(uf5911)(tag_t *np1, double *rp2, double *rr3, double *rr4,
double *rr5, double *rr6);


/* uf5930 intersect two curves
   Replaced by UF_CURVE_intersect or UF_MODL_intersect_objects */
extern UFUNEXPORT void FTN(uf5930)(tag_t *np1, tag_t *np2, double *rp3, double *rr4,
double *rr5, double *rr6, int *ir7);

/* uf5931 intersect curve and face/plane
   Replaced by UF_CURVE_intersect or UF_MODL_intersect_objects */
extern UFUNEXPORT void FTN(uf5931)(tag_t *np1, tag_t *np2, double *rp3, double *rr4,
double *rr5, double *rr6, int *ir7);

/* uf5932 intersection of two faces
   Replaced by UF_MODL_intersect_objects */
extern UFUNEXPORT void FTN(uf5932)(tag_t *jp1, tag_t *jp2, double *rp3, tag_t *jp4,
double *rp5, tag_t *jp6, double *rp7, int *ip8, double *rp9, int *ip10,
double *rp11, int *ip12, int *ir13, int *ir14, tag_t *jr15);

/******************************************************************************
 * Ask curve fit data from the curve feature
 *
 * Environment: Internal and External
 *
 * See Also:  UF_CURVE_edit_by_curve_fit_data
 *
 * History: This function is introduced in NX3.0.
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_curve_fit_data
(
 tag_t                   curve_feature,   /* <I> tag of the curve feature */
 UF_CURVE_curve_fit_data *curve_fit_data  /* <O> curve fit method, maximum degree, and maximum segments */
);

/******************************************************************************
 * Save curve fit data to the curve feature and execute the editing process
 *
 *
 * In NX3, only the following three curve features are supported,
 * Projection curve features, Intersecion curve features and Join curve features.
 *
 * From NX4 on, the following six curve features will be supported,
 * Projection curve features, Intersecion curve features, Join curve features.
 * Combined projection curve features, Isocline curve features and
 * Offset curve features
 *
 * Environment: Internal and External
 *
 * See Also:  UF_CURVE_ask_curve_fit_data
 *
 * History: This function is introduced in NX3.0.
******************************************************************************/
extern UFUNEXPORT int UF_CURVE_edit_by_curve_fit_data
(
 tag_t                   curve_feature,   /* <I> tag of the curve feature */
 UF_CURVE_curve_fit_data curve_fit_data   /* <I> curve fit method, maximum degree, and maximum segments */
);


/***************************************************************************
Returns the offset direction vector and the draft direction vector for a
string of curves. These vectors define the positive direction. If you
want to offset in the opposite direction, then negate the values for
distance, draft height, and/or draft angle. The input string of curves
must be coplanar.

Environment: Internal  and  External

See Also: 

Documentation for UF_STRING_p_t and UF_STRING_t can be found in the NX Open
Reference Manual under uf_modl -> Types ->  string_list.

History:This function was modified in V13.0 to add the base_point parameter.
        Original function was UF_CURVE_ask_offset_direction, in NX6.0.2 this function was 
        added to return correct offset direction.
****************************************************************************/
extern UFUNEXPORT int UF_CURVE_ask_offset_direction_2(
UF_STRING_p_t input_curves ,/* <I>
                            Pointer to curves list structure
                               int num         Total number of primary strings
                                               (min=1,max=1)
                               int string[]    Total number of segment curves/
                                               sketch id of each primary string
                                               (min=1,max=402)
                               int dir[]       Direction of each primary string
                                                  1 = Start to End
                                                 -1 = End to Start
                               tag_t id[]      Identifier of primary curves
                            Use UF_MODL_init_string_list and
                            UF_MODL_create_string_list
                            to create input strings. Use
                            UF_MODL_free_string_list to free
                            memory after the string is created.
                            */
double offset_direction_vector[3] ,/* <O>
                                   positive offset direction
                                   */
double draft_direction_vector[3] ,/* <O>
                                  positive draft height direction
                                  */
double base_point[3]  /* <O>
                      base point of vectors
                      */
);



#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#include <uf_retiring.h>

#endif    /*  END UF_CURVE_INCLUDED  */
