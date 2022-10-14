/*******************************************************************************
             Copyright (c) 1998-1999 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File Description:

Open C API definitions for UF_BREP specific structures, typedefs, and
macro definitions.

**************************************************************************/

/***************************************************************************

  ***************************************************************************/

#ifndef UF_BREP_TYPES_INCLUDED
#define UF_BREP_TYPES_INCLUDED

#include <uf_defs.h>         /* Common to all Open C API, e.g., tag_t, NULL_TAG */
#include <uf_error_bases.h>  /* For UF error codes not specific to a module. */
#include <uf_forgeo.h>       /* FORGEO support */


#ifdef __cplusplus
extern "C" {
#endif

/*******************************************************************************
* UF_BREP/PX_BREP error codes, e.g., for UF_get_fail_message().
* ERROR_PX_BREP_base is the error base for UF_BREP and PX_BREP.
* 
*******************************************************************************/
#define ERROR_PX_BREP_base     1838000
#define UF_BREP_err_none                    0
#define UF_BREP_err_topology                (ERROR_PX_BREP_base +  0)
#define UF_BREP_err_bad_ug_entity           (ERROR_PX_BREP_base +  1)
#define UF_BREP_err_null_pointer            (ERROR_PX_BREP_base +  2)
#define UF_BREP_err_bad_geom_sense          (ERROR_PX_BREP_base +  3)
#define UF_BREP_err_topo_geom_mismatch      (ERROR_PX_BREP_base +  4)
#define UF_BREP_err_bad_surf_type           (ERROR_PX_BREP_base +  5)
#define UF_BREP_err_bad_curve_type          (ERROR_PX_BREP_base +  6)
#define UF_BREP_err_geom_attach             (ERROR_PX_BREP_base +  7)
#define UF_BREP_err_bad_ug_tag              (ERROR_PX_BREP_base +  8)
#define UF_BREP_err_bad_root_topology_type  (ERROR_PX_BREP_base +  9)
#define UF_BREP_err_validate_topology       (ERROR_PX_BREP_base + 10)
#define UF_BREP_err_edges_dont_trim_face    (ERROR_PX_BREP_base + 11)
#define UF_BREP_err_already_has_geom        (ERROR_PX_BREP_base + 12)
#define UF_BREP_err_no_geometry             (ERROR_PX_BREP_base + 13)
#define UF_BREP_err_topo_cant_have_geom     (ERROR_PX_BREP_base + 14)
#define UF_BREP_err_flatten_non_face        (ERROR_PX_BREP_base + 15)
#define UF_BREP_err_trim_loop_degenerate    (ERROR_PX_BREP_base + 16)
#define UF_BREP_err_cant_make_trimsurf      (ERROR_PX_BREP_base + 17)
#define UF_BREP_err_tight_tolerances        (ERROR_PX_BREP_base + 18)
#define UF_BREP_err_cant_make_bspline       (ERROR_PX_BREP_base + 19)
#define UF_BREP_err_ref_cache_obj_is_sleepy (ERROR_PX_BREP_base + 20)


/******************************************************************************
* UF_BREP_state_t codes, e.g., from UF_BREP_ask_geometry().
*
* IMPORTANT:
*     UF_BREP shares state code `space' with UF_CURVE and UF_MODL.
*     The complete list of UF_BREP state codes is:
*         UF_CURVE_STATE_*   (see uf_curve.h)
*         UF_MODL_STATE_*    (see uf_modl.h)
*         UF_BREP_STATE_*    (see below)
******************************************************************************/
#define UF_BREP_STATE_base  200   /* codes <200 are UF_CURVE_STATE_*
                                  UF_MODL_STATE_* */

/* Topology creation problems */

#define UF_BREP_STATE_unknown_child    (UF_BREP_STATE_base +  1)
#define UF_BREP_STATE_duplicate_child  (UF_BREP_STATE_base +  2)
                                   /* Repeated parent-child relationship */
#define UF_BREP_STATE_wrong_child      (UF_BREP_STATE_base +  3)
                                   /* Child topology type not consistent with
                                   parent */
#define UF_BREP_STATE_missing_child    (UF_BREP_STATE_base +  4)
                                   /* Parent topology has too few children */
#define UF_BREP_STATE_extra_child      (UF_BREP_STATE_base +  5)
                                   /* Parent topology has too many children */
#define UF_BREP_STATE_wrong_parent     (UF_BREP_STATE_base +  6)
                                   /* Vertex has both edge and loop parents */
#define UF_BREP_STATE_missing_parent   (UF_BREP_STATE_base +  7)
                                   /* Child topology has too few parents */
#define UF_BREP_STATE_extra_parent     (UF_BREP_STATE_base +  8)
                                   /* Child topology has too many parents */
#define UF_BREP_STATE_bad_loop         (UF_BREP_STATE_base +  9)
                                   /* Loop edges' start & end vertices and
                                   sense do not match up */
#define UF_BREP_STATE_disjoint_shell   (UF_BREP_STATE_base + 10)
                                   /* Shell's faces not all connected */
#define UF_BREP_STATE_non_manifold     (UF_BREP_STATE_base + 11)
                                   /* Non-manifold vertex */
#define UF_BREP_STATE_topology_error   (UF_BREP_STATE_base + 12)
                                   /* Uncategorizable topology error */

/* Body check conditions */

#define UF_BREP_STATE_unknown_body_fault      (UF_BREP_STATE_base + 13)
                                             /* Uncategorizable body failure */
#define UF_BREP_STATE_body_inside_out         (UF_BREP_STATE_base + 14)
#define UF_BREP_STATE_self_intersecting       (UF_BREP_STATE_base + 15)
#define UF_BREP_STATE_degenerate_geometry     (UF_BREP_STATE_base + 16)
#define UF_BREP_STATE_invalid_geometry        (UF_BREP_STATE_base + 17)
#define UF_BREP_STATE_face_face_inconsistency (UF_BREP_STATE_base + 18)
#define UF_BREP_STATE_face_error              (UF_BREP_STATE_base + 19)
                                             /* uncategorizable face problem */
#define UF_BREP_STATE_vertex_not_on_curve     (UF_BREP_STATE_base + 20)
                                             /* specify larger tolerance */
#define UF_BREP_STATE_edge_reversed           (UF_BREP_STATE_base + 21)
                                             /* vertex order appears backward */
#define UF_BREP_STATE_vertex_not_on_surface   (UF_BREP_STATE_base + 22)
                                             /* specify larger tolerance */
#define UF_BREP_STATE_edge_not_on_surface     (UF_BREP_STATE_base + 23)
                                             /* specify larger tolerance */
#define UF_BREP_STATE_loop_inconsistent       (UF_BREP_STATE_base + 24)
                                             /* loop vertices out of order */
#define UF_BREP_STATE_face_or_edge_non_g1     (UF_BREP_STATE_base + 25)
                                             /* not G1 continuous */
#define UF_BREP_STATE_invalid_entity_ids      (UF_BREP_STATE_base + 26)

/* attach geometry conditions */

#define UF_BREP_STATE_edge_tol_too_big        (UF_BREP_STATE_base + 27)
                                             /* required tolerance exceeds
                                             user request */
#define UF_BREP_STATE_inconsistent_geom       (UF_BREP_STATE_base + 28)
#define UF_BREP_STATE_invalid_geom            (UF_BREP_STATE_base + 29)
                                             /* geometry does not pass checks */
#define UF_BREP_STATE_unknown_geom_fault      (UF_BREP_STATE_base + 30)
                                             /* possibly corrupt geometry
                                             data */

/* validate topology errors */

#define UF_BREP_STATE_bad_child_count         (UF_BREP_STATE_base + 31)
                                             /* child count illegal for parent
                                             topology */
#define UF_BREP_STATE_null_child_array        (UF_BREP_STATE_base + 32)
                                             /* children exist but child
                                             array is NULL */
#define UF_BREP_STATE_null_child_pointer      (UF_BREP_STATE_base + 33)
                                             /* a child pointer is NULL */
#define UF_BREP_STATE_multi_vertex_loop       (UF_BREP_STATE_base + 34)
                                             /* loop can have only one
                                             vertex, e.g., tip of cone */


/* Structures and macros  */

/*
* Geometry types:  points, curves, surfaces, etc.
* Note:
*     The order of enum items is important, e.g., the code relies on
*     surface types lying numerically between UF_BREP_SURFACE_ALL and
*     UF_BREP_SPECIAL_BASE.
*/
enum UF_BREP_geom_type_e
{
    UF_BREP_GEOM_ALL = 0,
    UF_BREP_POINT_GEOM,

    UF_BREP_CURVE_ALL  = 100,
    UF_BREP_LINE_GEOM,
    UF_BREP_SPLINE_GEOM,
    UF_BREP_ARC_GEOM,
    UF_BREP_ELLIPSE_GEOM,       /* conic */
    UF_BREP_HYPERBOLA_GEOM,     /* conic */
    UF_BREP_PARABOLA_GEOM,      /* conic */
    UF_BREP_INTERSECTION_GEOM,  /* for conv mapping; no corresponding structure
                                   yet */
    UF_BREP_COMPOSITE_GEOM,

    UF_BREP_SURFACE_ALL  = 200,
    UF_BREP_CYLINDER_GEOM,
    UF_BREP_CONE_GEOM,
    UF_BREP_SPHERE_GEOM,
    UF_BREP_TORUS_GEOM,
    UF_BREP_REVOLVE_GEOM,
    UF_BREP_EXTRUDE_GEOM,
    UF_BREP_BSURFACE_GEOM,
    UF_BREP_OFFSET_GEOM,
    UF_BREP_PLANE_GEOM,
    UF_BREP_BLEND_GEOM,   /* conv mapping; no corresponding structure yet */
    UF_BREP_FORSURF_GEOM,

    UF_BREP_SPECIAL_BASE  = 300,
    UF_BREP_UVBOX_GEOM,
    UF_BREP_TAG_GEOM
};

typedef enum UF_BREP_geom_type_e UF_BREP_geom_type_t;

/* These are the topology types for the type member of the topology
   structure. A topology may contain only one of UF_BREP_SOLID_TOPO
   or UF_BREP_SHEET_TOPO. It contains as many of the others as needed.
*/
enum UF_BREP_topo_type_e
    {
    UF_BREP_NULL_TOPO,
    UF_BREP_SOLID_TOPO,
    UF_BREP_SHEET_TOPO,
    UF_BREP_TRIMSURF_TOPO,
    UF_BREP_SHELL_TOPO,
    UF_BREP_FACE_TOPO,
    UF_BREP_LOOP_TOPO,
    UF_BREP_FIN_TOPO,
    UF_BREP_EDGE_TOPO,
    UF_BREP_VERTEX_TOPO
};

typedef enum UF_BREP_topo_type_e UF_BREP_topo_type_t;

/* These are the topology sources for the body topology structure
   (UF_BREP_ask_topology_source).
*/
enum UF_BREP_topo_source_e
{
    UF_BREP_APP_BODY_SOURCE,
    UF_BREP_APP_TRIMSURF_SOURCE,
    UF_BREP_UGO_BODY_SOURCE,
    UF_BREP_UGO_TRIMSURF_SOURCE
};

typedef enum UF_BREP_topo_source_e UF_BREP_topo_source_t;


/* Edge topology and geometry classifications for UF_BREP_ask_edge_class.
*/
enum UF_BREP_edge_class_e
    {
    UF_BREP_EDGE_OPEN = 1,     /* Two distinct vertices. */
    UF_BREP_EDGE_CLOSED,       /* Start and end vertex are the same. */
    UF_BREP_EDGE_RING,         /* Edge has no vertices. */

    UF_BREP_EDGE_NORMAL = 10,  /* Has a 3D curve. */
    UF_BREP_EDGE_INTERSECTION, /* Two intersecting surfaces implicitly define 3D curve. */
    UF_BREP_EDGE_TOLERANT,     /* Fins define edge curve. */
    UF_BREP_EDGE_SP            /* Has an SP curve, but not a tolerant edge. */
    };


/* The definition of a line. */
struct UF_BREP_line_s
{
    double  start_point[3];  /* Start point of the line.  Parameterization is
                                from 0 being the start point to 1 being the
                                end point. */
    double  end_point[3];    /* End point of the line */
};

typedef struct UF_BREP_line_s UF_BREP_line_t, *UF_BREP_line_p_t;

/* Contains data defining an arc. The matrix defines an orientation thus: The
   first 3 elements are the X axis of the orientation matrix in absolute
   coordinates, the next 3 are the Y axis, and the last 3 are the Z axis. The
   center defines the location of the arc in orientation space. The line
   through the center parallel to the orientation X axis defines the zero
   angle, zero being along the portion of the line from the center to the
   positive X axis. The value start_angle must be in the interval [0,2pi) and
   end_angle-start_angle <= 2pi.
*/
struct UF_BREP_arc_s
{
    tag_t   matrix_tag;     /* Rotation only; arc lies in matrix's X-Y plane */
    double  start_angle;    /* Radian start angle with zero along positive
                               X-axis, with positive being CCW using right hand
                               rule. */
    double  end_angle;      /* Radian end angle with zero along positive X-axis,
                               with positive being CCW using right hand rule. */
    double  arc_center[3];  /* Center with respect to the arc's coordinate
                               system */
    double  radius;         /* The radius of the arc. */
};

typedef struct UF_BREP_arc_s UF_BREP_arc_t, *UF_BREP_arc_p_t;

/*
Definition for a conic.

If the subtype is an ellipse then it is counterclockwise when viewed in the
direction opposite the Z axis of the matrix.  The parameters meet the same
requirements as for an arc.  The major axis is parallel to the X axis of the
matrix, and the minor axis is parallel to the Y axis.  Conic_type is
UF_conic_ellipse_subtype.  K1 is the semimajor axis, and k2 is the semiminor
axis.

If the subtype is a parabola, then the X axis of the matrix is the direction
of the centerline of a parabola, which opens out along that direction.  The
start and end angles may be any real numbers, as long as start_angle is less
than end_angle.  Conic type is UF_conic_parabola_subtype.

If the subtype is a hyperbola, then the X axis of the matrix is the direction
of the centerline of the hyperbola, which opens out along that direction.  The
start and end angles must be in the interval (-pi/2, +pi/2).  Note that the
hyperbola is numerically unstable at values close to the endpoints of this
interval.  Conic_type is UF_conic_hyperbola_subtype.
*/
struct UF_BREP_conic_s
{
    tag_t   matrix_tag;       /* Conic lies in matrix's X-Y plane */
    int     conic_type;       /* subtype of the conic section. See
                                 uf_object_types.h */
    double  rotation_angle;   /* angle of rotation of conic X from matrix X */
    double  start_param;      /* start parameter value */
    double  end_param;        /* end parameter value */
    double  center[3];        /* center of conic in orientation space */
    double  k1;               /* first shape parameter */
    double  k2;               /* second shape parameter */
};

typedef struct UF_BREP_conic_s UF_BREP_conic_t, *UF_BREP_conic_p_t;

/* Contains data defining a non-uniform rational b-spline (NURBS) curve.
   There are 4 values for each control point or pole: x, y, z and w.  The
   coordinates are weighted.  The parameter values specify how much of
   the spline is to be active, i.e. visible and used.  They cannot be outside
   the interval defined by the knot vector.  The lowest allowed value is
   knots[order-1].  The largest is knots[num_poles].  NURBS curves need not have
   Bezier end conditions (be clamped).

   The number of knots and poles, and the order are related as follows:
       nknots = num_poles + order.
*/
struct UF_BREP_spline_s
{
    int      num_poles;     /* Number of control points or poles, i.e.,
                               poles[num_poles][4] */
    int      order;         /* degree + 1 of the basis functions */
    logical  is_rational;   /* Set according to whether the spline is rational:
                               True if the spline is rational, else false. */
    double  *knots;         /* knots[num_poles+order].  If this is an output
                               structure then this member must be freed by
                               calling UF_free. */
    double (*poles)[4];     /* control point vectors.  If this is an output
                               structure, then this member must be freed by
                               calling UF_free. */
    double   start_param;   /* smallest t value of curve's active region */
    double   end_param;     /* largest  t value of curve's active region */
};

typedef struct UF_BREP_spline_s UF_BREP_spline_t, *UF_BREP_spline_p_t;

/* Contains data representing a plane. The u parameter is along the reference
   direction and the v parameter is at right angles to it, which places the
   plane in the x-y plane of a right handed coordinate system with the
   reference direction as the x axis and the normal vector as the z axis.
   Parameter values are in part units.
*/
struct UF_BREP_plane_s
{
    double  pt_on_plane[3];    /* Defines the location of the plane in space. */
    double  normal[3];         /* Vector normal to the plane. */
    double  u0_ref_direc[3];   /* Defines orientation of zero u. */
};

typedef struct UF_BREP_plane_s UF_BREP_plane_t, *UF_BREP_plane_p_t;


/* A sphere is represented by its location (center), axis, and radius. The axis
   vector represents the axis around which the parameterization is 0 to 2pi and
   is u. The reference direction vector indicates the orientation of the 0
   parameter value in u. It need not be perpendicular to the axis vector but
   must not be parallel to it. V parameterization is -pi/2 to +pi/2, on an
   implicit generator of a half-circle.  Looking at the sphere in the direction
   opposite the axis vector, -p on the generator is away from the observer.
   U increases counterclockwise, and v increases towards the observer.
*/
struct UF_BREP_sphere_s
{
    double  center[3];       /* Center location of the sphere. */
    double  axis[3];         /* Axis of the sphere. */
    double  u0_ref_direc[3]; /* Reference direction which defines the
                                orientation of zero u. */
    double  radius;          /* Radius of the sphere. */
};

typedef struct UF_BREP_sphere_s UF_BREP_sphere_t, *UF_BREP_sphere_p_t;


/* A cylinder is represented by its location, axis vector, and radius.  The
   reference vector need not be perpendicular to the axis, but must not
   be parallel to it.  Parameterization is 0 to 2pi in u and by length in
   part units along the axis in v, positive in the direction of the axis
   vector. */
struct UF_BREP_cylinder_s
{
    double  pt_on_axis[3];    /* Location on axis to position the cylinder,
                                 defines zero v. */
    double  axis[3];          /* The axis vector for the cylinder. */
    double  u0_ref_direc[3];  /* Reference direction which defines the
                                 orientation of zero u. */
    double  radius;           /* The radius of the cylinder. */
};

typedef struct UF_BREP_cylinder_s UF_BREP_cylinder_t, *UF_BREP_cylinder_p_t;

/* A cone is represented by its location, axis vector, and half-angle. The
   reference direction need not be perpendicular to the axis vector but must
   not be parallel to it. Parameterization is 0 to 2pi in u and length along
   the axis in v, positive in the direction of the axis vector. The point
   defines the apex of the cone. A mathematical cone consists of two half-cones.
   The half retained by this representation is the half in which the axis points
   away from the apex of the cone. Note that this means that v parameter values
   are always positive.
*/
struct UF_BREP_cone_s
{
    double  pt_at_apex[3];    /* Apex location, defines zero v */
    double  axis[3];          /* Axis vector of the cone. */
    double  u0_ref_direc[3];  /* Reference direction, defines the orientation
                                 of zero u. */
    double  half_apex_angle;  /* half angle of the cone in radians. */
};

typedef struct UF_BREP_cone_s UF_BREP_cone_t, *UF_BREP_cone_p_t;

/* A torus is represented with its location (point at center), axis vector of
   the major spin, and the major and minor radii. The reference direction need
   not be perpendicular to the axis vector but must not be parallel to it.
   Parameterization is 0 to 2pi in u for the spin around the axis and -pi to +pi
   in v along the (implied) generator circle. The 0 value for u and v is on the
   outside of the torus (away from the axis). When looking at the torus from
   the direction opposite the axis, -pi/2 of the generator is away from the
   observer.

   There are 3 classes of torus: doughnut, apple (including the oscillating
   apple), and lemon. For a doughnut, major_rad > minor_rad > 0. For an apple,
   major_rad <= minor_rad and major_rad > 0. The case where
   major_rad = minor_rad is the oscillating apple and it is periodic in both
   directions. For a lemon, major_rad < 0 and |major_rad| < minor_rad. These
   may be determined by calling UF_MODL_ask_torus_face_type.
*/
struct UF_BREP_torus_s
{
    double  center[3];       /* Defines the location of the major center. */
    double  axis[3];         /* Major axis of the torus, through the center
                                of the doughnut. */
    double  u0_ref_direc[3]; /* Defines the orientation of zero in u. */
    double  major_radius;    /* Radius from axis to center of generation
                                circle. */
    double  minor_radius;    /* Radius of generator circle. */
};

typedef struct UF_BREP_torus_s UF_BREP_torus_t, *UF_BREP_torus_p_t;

/* A non-uniform rational b-spline (NURBS) surface is represented. The poles
   array is constructed as follows. Each row is a u spline and each column is a
   v spline, stored in row-major order. U indexes the columns and v indexes the
   rows. The subscript into the poles array for any given pole defining the
   surface is obtained as follows:

      subscr = (num_poles_u * v + u)
      poles[subscr][0] = x coordinate
      poles[subscr][1] = y coordinate
      poles[subscr][2] = z coordinate
      poles[subscr][3] = weight

   In each direction, the number of knots = num_poles + order. The x, y, and z
   coordinates are weighted.

   A periodic NURBS surface in one or both directions is one that closes with
   the same location and tangent vectors at the matching edges. Open C API
   determines periodicity from the bsurface data.

   Note that this structure is identical to UF_MODL_bsurface_s.
*/

struct UF_BREP_bsurface_s
{
    int  num_poles_u;       /* The number of control points(poles) in the
                               u direction. */
    int  num_poles_v;       /* The number of control points(poles) in the
                               v direction. */
    int  order_u;           /* The order (degree +1) of the basis functions in
                               the u direction. */
    int  order_v;           /* The order (degree +1) of the basis functions in
                               the v direction. */
    logical  is_rational;   /* True if the surface is rational (the weights
                               are not all equal). */
    double *knots_u;        /* Knot vector for the u direction. */
    double *knots_v;        /* Knot vector for the v direction. */
    double (*poles)[4];     /* An array of the control points (poles). */
};

typedef struct UF_BREP_bsurface_s UF_BREP_bsurface_t, *UF_BREP_bsurface_p_t;

/* This structure defines a box in U/V space that contains faces, surfaces,
   SP-curves, and SP-curve loops.
*/
struct UF_BREP_uvbox_s
{
    double  umin;   /* Minimum u parameter of the box. */
    double  umax;   /* Maximum u parameter of the box. */
    double  vmin;   /* Minimum v parameter of the box. */
    double  vmax;   /* Maximum v parameter of the box. */
};

typedef struct UF_BREP_uvbox_s UF_BREP_uvbox_t, *UF_BREP_uvbox_p_t;

/* This structure specifies a tagged NX object to be used in a topology. When
   these objects are attached, they are no longer available as a separately
   tagged NX object.
*/
struct UF_BREP_tagged_object_s
{
    tag_t  object;  /* curve or suface object. */
};

typedef struct UF_BREP_tagged_object_s UF_BREP_tagged_object_t,
*UF_BREP_tagged_object_p_t;

/* This provides a means of having a list of curves fill the function of a
   single curve.  This may be used as a generator or a curve in a loop.  Some
   cautions are in order, however.  When used as a generator, a multi-face
   sheet body is produced.  Such a sheet may not be trimmed with curves.

   A composite curve may be attached to an edge, but the component curves
   are joined to make one curve to attach.
*/
struct UF_BREP_composite_s
{
    int  num_curves;                   /* The number of curves in the
                                          composite. */
    struct UF_BREP_geometry_s  *curves; /* <len:num_curves> An array of geometry structures.
                                           Only curves may be present. */
};

typedef struct UF_BREP_composite_s UF_BREP_composite_t,
*UF_BREP_composite_p_t;

/* A surface of revolution is represented with its axis vector and generator
   curve. The v parameterization is 0 to 2pi around the axis. U parameterization
   is the parameterization of the generator curve. The reference vector need
   not be perpendicular to the axis but must not be parallel to it. The
   location of the generator curve in space defines the zero parameter value
   in v. Note that this parameterization is counterintuitive with respect to
   treating cylinders, cones, spheres, and torii as surfaces of revolution,
   because the parameterization is flipped u for v.
*/
struct UF_BREP_revolve_s
{
    double  pt_on_axis[3];
    double  rot_axis[3];
    struct UF_BREP_geometry_s  *generator;
};

typedef struct UF_BREP_revolve_s UF_BREP_revolve_t, *UF_BREP_revolve_p_t;

/* An extruded surface is represented by its direction of extrusion and
   generator curve. The curve is also the zero point of the v parameter, which
   is positive in the direction of extrusion, and is in part units. U is the
   same as the parameterization of the generator curve.
*/

struct UF_BREP_extrude_s
{
    double  direction[3];                /* Vector which indicates the
                                            direction to sweep the generator. */
    struct UF_BREP_geometry_s  *generator; /* The geometry structure for the
                                              generator, only a curve may be
                                              specified. */
};

typedef struct UF_BREP_extrude_s UF_BREP_extrude_t, *UF_BREP_extrude_p_t;

/* Contains data representing an offset from a base surface.  The distance is
   in part units, and is positive if in the direction of the normal of the
   base surface.  Only surface geometry may be offset.  To offset a finished
   face, use UF_MODL_create_face_offset.
*/
struct UF_BREP_offset_s
{
    struct UF_BREP_geometry_s *base; /* Surface forming the basis of
                                     the offset surface.
                                     */
    double  distance;                /* Signed distance from base. Distance > 0
                                     for offset surfaces on the side that
                                     the base surface's normal indicates.
                                     */
};

typedef struct UF_BREP_offset_s UF_BREP_offset_t, *UF_BREP_offset_p_t;

union UF_BREP_geom_u
{
    double  point[3];

    UF_BREP_line_t       line;
    UF_BREP_arc_t        arc;
    UF_BREP_conic_t      conic;
    UF_BREP_spline_t     spline;
    UF_BREP_composite_t  composite;

    UF_BREP_plane_t      plane;
    UF_BREP_cylinder_t   cylinder;
    UF_BREP_cone_t       cone;
    UF_BREP_sphere_t     sphere;
    UF_BREP_torus_t      torus;
    UF_BREP_bsurface_t   bsurface;
    UF_BREP_revolve_t    revolve;
    UF_BREP_extrude_t    extrude;
    UF_BREP_offset_t     offset;
    UF_FORGEO_forsurf_t  foreign;

    UF_BREP_uvbox_t          uvbox;
    UF_BREP_tagged_object_t  tagged;
};

typedef union UF_BREP_geom_u UF_BREP_geom_t;


/* The generic geometry structure. The union gathers all the curve and surface
   structures for the purpose of defining a pointer or variable without having
   to know which type of geometry is represented. The type value is from the
   enumeration below.  */

struct UF_BREP_geometry_s
{
    UF_BREP_geom_type_t  type;
    UF_BREP_geom_t       geom;
};

typedef struct UF_BREP_geometry_s UF_BREP_geometry_t, *UF_BREP_geometry_p_t;

/* Shorthand to fill in a topology element (UF_BREP_topology_s). */

#define UF_BREP_INITIALIZE_TOPOLOGY(topology,child_array,nchildren,topo_type) \
    (topology)->children     = (child_array);  \
    (topology)->num_children = (nchildren);    \
    (topology)->type         = (topo_type);    \
    (topology)->tag          = NULL_TAG;       \
    (topology)->u.user_ptr   = NULL;           \
    (topology)->extension    = NULL;


enum UF_BREP_orientation_e
{
    UF_BREP_ORIENTATION_REVERSE = -1,
    UF_BREP_ORIENTATION_NONE,
    UF_BREP_ORIENTATION_FORWARD
};

typedef enum UF_BREP_orientation_e UF_BREP_orientation_t;

/* Describes a child and its orientation with respect to its parent. */
struct UF_BREP_oriented_child_s
{
    struct UF_BREP_topology_s  *child; /* Topology structure for any kind
                                       of Parasolid topology entity.
                                       */
    int  orientation;                  /* Only for loop and fin children,
                                       otherwise UF_BREP_ORIENTATION_NONE.
                                       Since fins are always oriented
                                       positively (forward) with respect to
                                       their loop parent, `orientation' only
                                       applies to an edge whose parent is a
                                       loop or fin.
                                       UF_BREP_ORIENTATION_FORWARD:
                                       edge traverse from start to end vertex
                                       UF_BREP_ORIENTATION_REVERSE:
                                       edge traverse from end to start vertex
                                       */
};

typedef struct UF_BREP_oriented_child_s UF_BREP_oriented_child_t,
*UF_BREP_oriented_child_p_t;

/* User data (C union) that only Open C API programmer uses. (Although
UF_BREP_INITIALIZE_TOPOLOGY does initialize the value to zero.) The
union allows user code to conveniently mark topology entities
(e.g., for tree traversal algorithms) or attach arbitrary user data.  */

union UF_BREP_u
{
   void *user_ptr;
   int   user_int;
};

typedef union UF_BREP_u UF_BREP_t;

/*
Describes an item of topology. A tree of topology items (connected via the
children pointers) describes a body or face. If the tree's root item is a body
the type is one of UF_BREP_SOLID_TOPO, UF_BREP_SHEET_TOPO, or
UF_BREP_TRIMSURF_TOPO. If the body topology element is not present, the first
one must be UF_BREP_FACE_TOPO and there can only be one. It is assumed to be a
UF_BREP_TRIMSURF_TOPO. The face may be part of a body topology.

If there is more than one shell, the outer shell must be the first in the body's
child list. Only vertices cannot have children. Faces are the children of
shells, loops are the children of faces, edges are the children of loops, and
vertices are the children of edges. If fins are present, the fins are children
of the loops and edges are children of the fins. Edges may be absent only in a
trimmed surface topology. Vertices may be children of edges or loops but not of
fins. A loop may have fins or edges as children, or only one vertex. Such a
vertex is is used to represent a loop at a singularity, like the tip of a cone.

The sense of geometry with respect to its topology (faces, fins, edges) is
specified when it is attached, using the sense argument to the attach function.

The order of children also matters for loops and edges. Edges are oriented in
the order given by their child vertices. The edges or fins of a loop must be
listed in order, and the curves must match end to start after accommodating the
fin or edge orientation (the end vertex of one curve must be the same as the
start vertex of the next curve). All loops in a solid or sheet body are ordered
such that the material in the face (the surface of the body) is on the left
when walking the loop with one's head outside the body. Thus, an outer loop
(peripheral border of a face) is counterclockwise when looking from the outside
into the body. Hole loops are clockwise. Sometimes a loop cannot be classified;
it is the left-hand material rule that applies.

The orientation member of the child structure is used for the children of loops
and the children of fins. (All other uses should set the value to
UF_BREP_ORIENTATION_NONE.) Fins are considered always to be positively oriented
with respect to their loop; thus the orientation of the edge is what is
specified, either where the fin is the child of the loop, where the edge is the
child of the loop, or where the edge is the child of the fin. It indicates if
the edge is traced from its first vertex to its second (forward) or from its
second vertex to its first reverse) for the loop in which the edge is used. An
edge must be used in two loops, unless it is a border edge of a sheet body. If
the orientation of an edge is specified (i.e., not NONE) both in its fin and in
its loop, the two values must agree.

On input, fins may be specified. SP curves may be attached directly.

The tag and extension members must be set to NULL_TAG and NULL, respectively.
Use the UF_BREP_INITIALIZE_TOPOLOGY macro.

You can access an identifier for all topology entities using
UF_BREP_ask_identifier. Vertices, fins, and shells do not have NX tags, but do
have identifiers, which are unique within the body.

A fin is where a face joins an edge. The geometry for a fin is the SP curve
that shapes the surface to match the 3D edge. On output from NX, not all edges
in a solid model have fin curves; only tolerant edges do. Other edges do not
have any fin curves and only have a 3D edge curve.

On input to NX, SP curves and 3D curves may be specified for the same edge. All
the information available is used to construct the final edge, which conforms
to the above description of tolerant and non-tolerant edges.

NOTE: SP curves may not be used for creating an edge in V15.0. They may be
specified but are ignored.

Use the macro UF_BREP_INITIALIZE_TOPOLOGY to set all the input fields:

UF_BREP_INITIALIZE_TOPOLOGY(topology, children, nchildren, type).

*/

struct UF_BREP_topology_s
{
    UF_BREP_topo_type_t       type;        /* See UF_BREP_topo_type_s, e.g.,
                                           solid, sheet, trimmed surface, shell,
                                           face, loop, fin, edge, and vertex.
                                           */
    tag_t                     tag;         /* NX tag, except for shells, fins,
                                           and vertices, in which case `tag'
                                           is NULL_TAG.  If you need unique
                                           identifiers for all topologies in
                                           a body, use the value from
                                           UF_BREP_ask_identifier.
                                           */
    int                       num_children;/*Number of child indices in the
                                             children array.  This can be zero
                                             if the parent topology structure
                                             is a vertex.
                                           */
    UF_BREP_oriented_child_t *children;    /* <len:num_children> An array of oriented child
                                              structures designating the
                                              children of this topology item.
                                              This may be NULL if the parent
                                              topology structure is a vertex.
                                              For example loops are children of
                                              a face, vertices are children of
                                              an edge.  The outer shell, if any,
                                              must be the first child.  Fins,
                                              if any, are always children of
                                              loops while the corresponding
                                              edges are children of the fins.
                                              Only trimmed surfaces may omit
                                              edge topologies.  A loop may have
                                              as children:  one or more fins,
                                              one or more edges, or even one
                                              vertex (e.g., tip of cone).
                                              Children order matters for fins
                                              and edges, e.g., child vertex
                                              order orients edges.  A loop's
                                              edges (fins) must be in order,
                                              i.e., the end of one edge (fin)
                                              must be the start of the next
                                              edge (fin).  All loops (except
                                              those in trimmed surfaces) have a
                                              left hand rule orientation, i.e.,
                                              the face material is on the left
                                              while traveling the loop with `up'
                                              pointing in the face normal
                                              direction, which for bodies points
                                              away from the inside.  Unless on
                                              the border of a sheet body, an
                                              edge must appear in two loops
                                              with an opposite orientation in
                                              each loop.
                                           */
    UF_BREP_t                u;
    void                     *extension;   /* Opaque pointer reserved for
                                           UF_BREP module internal data.
                                           Do not modify (except indirectly
                                           via UF_BREP_INITIALIZE_TOPOLOGY).
                                           */
};


typedef struct UF_BREP_topology_s UF_BREP_topology_t, *UF_BREP_topology_p_t;

/*
* Topology and geometry options for many of the UF_BREP functions.
*/

struct UF_BREP_options_s
{
    int      count;    /*Option count:  options[count],
                       opt_data[count]
                       */
    int     *options;  /* Array of option tokens. */
    double  *opt_data; /* opt_data[i] specfies a numeric
                       value corresponding to options[i].
                       */
};

typedef struct UF_BREP_options_s UF_BREP_options_t, *UF_BREP_options_p_t;

/*
* Options and data (see UF_BREP_options_t)
*
*     UF_BREP_SIMPLIFY_DIST_OPTION
*         Part unit tolerance to simplify extrudes, revolves, B-surfaces.
*
*     UF_BREP_FINSP_OPTION
*       Supply fins (UF_BREP_ask_topology) or use SP curves (UF_BREP_make_body).
*     UF_BREP_EDGE3D_OPTION
*      Supply edges (UF_BREP_ask_topology) or use 3D curves (UF_BREP_make_body).
*     UF_BREP_ASATTACHED_OPTION
*       UF_BREP_make_body uses the attached SP or 3D curves.
*
*     UF_BREP_FLATTEN_OPTION
*       UF_BREP_ask_topology flattens periodic surfaces, but not necessarily
*       with a closed peripheral loop.
*     UF_BREP_FLATTEN_PERIPH_OPTION
*       UF_BREP_ask_topology flattens periodic surfaces with one closed
*       peripheral loop.
*
*     UF_BREP_SPLIT_OPTION
*       UF_BREP_make_body splits B-surfaces at any discontinuities.
*
*     UF_BREP_PROJECTION_DIST_OPTION
*       Tolerance in part units for UF_BREP_make_body to project 3D
*       trimming curves onto a surface.
*
*     UF_BREP_BSURF_DIST_OPTION
*       Tolerance in part units with which UF_BREP_ask_geometry
*       approximates B-surfaces.
*     UF_BREP_CURVE_DIST_OPTION
*       Tolerance in part units with which UF_BREP_ask_geometry
*       approximates B-curves (for fins and edges).
*
*   Please note that the following options have been removed from
*   the documentation because the code does not use these options.
*     UF_BREP_SIMPLIFY_MULT_OPTION
*     UF_BREP_PROJECTION_MULT_OPTION
*     UF_BREP_BSURF_MULT_OPTION
*     UF_BREP_CURVE_MULT_OPTION
*/
#define UF_BREP_SIMPLIFY_DIST_OPTION     0
#define UF_BREP_SIMPLIFY_MULT_OPTION     1
#define UF_BREP_FINSP_OPTION             2
#define UF_BREP_EDGE3D_OPTION            3
#define UF_BREP_ASATTACHED_OPTION        4
#define UF_BREP_FLATTEN_OPTION           5
#define UF_BREP_FLATTEN_PERIPH_OPTION    6
#define UF_BREP_SPLIT_OPTION             7
#define UF_BREP_PROJECTION_DIST_OPTION   8
#define UF_BREP_PROJECTION_MULT_OPTION   9
#define UF_BREP_BSURF_DIST_OPTION       10
#define UF_BREP_BSURF_MULT_OPTION       11
#define UF_BREP_CURVE_DIST_OPTION       12
#define UF_BREP_CURVE_MULT_OPTION       13


/*
* UF_BREP_ask_geometry extraction mappings, i.e., specifies conversion
* of geometry in a NX body to the geometry the caller receives.
*
*     (source[i] corresponds to extracted[i] to form a mapping pair)
*
* For now, the extracted types can only be B-surfaces and B-curves.
* Furthermore, two required mappings are:
*     source[]                      extracted[]
*     --------                      -----------
*     UF_BREP_BLEND_GEOM            UF_BREP_BSURFACE_GEOM
*     UF_BREP_INTERSECTION_GEOM     UF_BREP_SPLINE_GEOM
*/

struct UF_BREP_mapping_s
{
    int                   count; /* Mapping pair count:  source[count],
                                 extracted[count]
                                 */
    UF_BREP_geom_type_t  *source;/* NX body geometry types. */
    UF_BREP_geom_type_t  *extracted;/*Geometry types that UF_BREP_ask_geometry
                                      returns.
                                    */
};

typedef struct UF_BREP_mapping_s UF_BREP_mapping_t, *UF_BREP_mapping_p_t;

/*
This structure reports potential problems related to the topology item. A
problem can be an unfixable error, e.g., missing geometry, or a fixable error,
e.g., some types of self-intersections.  Use the macro UF_BREP_STATE_IS_FIXED
on the flag field to determine if UF_BREP could fix the problem, e.g.,

UF_BREP_STATE_IS_FIXED (states[i].flag).

Free state arrays that UF_BREP routines return by using UF_free.

The UF_BREP state codes have the following names and meanings. See uf_curve.h 
and uf_modl.h or the UF_CURVE and UF_MODL documentation for state codes 
specific to curve and surface geometry.


UF_BREP_STATE_unknown_child    
UF_BREP_STATE_duplicate_child  Repeated parent-child relationship
UF_BREP_STATE_wrong_child      Child topology type not consistent with parent
UF_BREP_STATE_missing_child    Parent topology has too few children
UF_BREP_STATE_extra_child      Parent topology has too many children
UF_BREP_STATE_wrong_parent     Vertex has both edge and loop parents
UF_BREP_STATE_missing_parent   Child topology has too few parents
UF_BREP_STATE_extra_parent     Child topology has too many parents
UF_BREP_STATE_bad_loop         Loop edges' start & end vertices and sense do not match up
UF_BREP_STATE_disjoint_shell   Shell's faces not all connected
UF_BREP_STATE_non_manifold     Non-manifold vertex
UF_BREP_STATE_topology_error   Uncategorizable topology error

Body check conditions

UF_BREP_STATE_unknown_body_fault      Uncategorizable body failure
UF_BREP_STATE_body_inside_out         
UF_BREP_STATE_self_intersecting       
UF_BREP_STATE_degenerate_geometry     
UF_BREP_STATE_invalid_geometry        
UF_BREP_STATE_face_face_inconsistency 
UF_BREP_STATE_face_error              uncategorizable face problem
UF_BREP_STATE_vertex_not_on_curve     specify larger tolerance
UF_BREP_STATE_edge_reversed           vertex order appears backward
UF_BREP_STATE_vertex_not_on_surface   specify larger tolerance
UF_BREP_STATE_edge_not_on_surface     specify larger tolerance
UF_BREP_STATE_loop_inconsistent       loop vertices out of order
UF_BREP_STATE_face_or_edge_non_g1     not G1 continuous
UF_BREP_STATE_invalid_entity_ids      

attach geometry conditions

UF_BREP_STATE_edge_tol_too_big        required tolerance exceeds user request
UF_BREP_STATE_inconsistent_geom       
UF_BREP_STATE_invalid_geom            geometry does not pass checks
UF_BREP_STATE_unknown_geom_fault      possibly corrupt geometry data

*/

struct UF_BREP_state_s
{
    int                 state_code; /*See the UF_BREP_STATE_* definitions for
                                    the problem descriptions. See uf_curve.h
                                    and uf_modl.h for state codes specific
                                    to curves and surfaces.
                                    */
    int                 flag;       /* Modifier to the state_code.
                                    For UF_BREP the modifier indicates
                                    whether UF_BREP could fix the
                                    problem.  Use UF_BREP_STATE_IS_FIXED
                                    to query the value.
                                    See uf_curve.h and uf_modl.h for
                                    modifiers specific to curves
                                    and surfaces, e.g., the problem
                                    is in U (as opposed to V) direction.
                                    */
    double              value[3];   /* Numeric attributes related to the
                                    problem, e.g., a point coordinate
                                    in the vicinity of a curve degeneracy.
                                    */
    UF_BREP_topology_t *item;       /* UF_BREP_topology_t entity having the
                                    problem, e.g., the edge not
                                    having attached geometry.
                                    */
    tag_t               ug_tag;     /* NX entity have the problem, if any.
                                    Some topology entities do not
                                    have NX tags, e.g., vertices.
                                    */
    int                 misc;       /* For internal bookkeeping only.*/

};

typedef struct UF_BREP_state_s UF_BREP_state_t, *UF_BREP_state_p_t;

/*
* Read/write macros for the UF_BREP_state_t's flag field, which indicates
* whether the state_code problem is fixed or unfixed.
*/
#define UF_BREP_STATE_IS_FIXED(x)  ((x) & 1)
#define UF_BREP_STATE_SET_FIXED(x) ((x) | 1)



#ifdef __cplusplus
}
#endif

#endif    /*  END UF_BREP_TYPES_INCLUDED  */
