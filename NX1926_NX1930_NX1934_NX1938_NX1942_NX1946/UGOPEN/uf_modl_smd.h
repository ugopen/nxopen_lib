/*****************************************************************************
             Copyright (c) 1998-2002 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Open API routines for Sheet Metal Design.

*****************************************************************************/

#ifndef UF_MODL_SMD_H_INCLUDED
#define UF_MODL_SMD_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

enum UF_MODL_smhole_type_e
{
    UF_DEPTH_SMHOLE = 0, /* depth type SMHole */
    UF_THROUGH_SMHOLE,   /* thru type SMHole  */
    UF_PUNCH_SMHOLE,     /* punch type SMHole */
    UF_N_TYPE_OPTS
};

typedef enum UF_MODL_smhole_type_e UF_MODL_smhole_type_e_t;
typedef UF_MODL_smhole_type_e_t UF_SMHOLE_hole_type_e_t;

enum UF_MODL_smhole_direction_type_e
{
    UF_FACE_NORMALS = 0, /* use face normals */
    UF_ALONG_VECTOR,     /* use a vector     */
    UF_ALONG_DATUM_AXIS, /* use a datum axis */
    UF_N_DIRECTION_OPTS
};
typedef enum UF_MODL_smhole_direction_type_e UF_MODL_smhole_direction_type_e_t;
typedef UF_MODL_smhole_direction_type_e_t UF_MODL_smslot_direction_type_e_t;
typedef UF_MODL_smhole_direction_type_e_t UF_MODL_smcutout_direction_type_e_t;
typedef UF_MODL_smhole_direction_type_e_t UF_SMHOLE_direction_type_e_t;

enum UF_MODL_smslot_type_e
{
    UF_PUNCH_SMSLOT = 0,
    UF_THROUGH_SMSLOT,
    UF_DEPTH_SMSLOT,
    UF_N_STYPE_OPTS
};
typedef enum UF_MODL_smslot_type_e UF_MODL_smslot_type_e_t;
typedef UF_MODL_smslot_type_e_t UF_SMSLOT_slot_type_e_t;

typedef UF_MODL_smhole_direction_type_e_t UF_MODL_smpunch_direction_type_e_t;

enum UF_MODL_smcutout_type_e
{
    UF_PUNCH_SMCUTOUT = 0,
    UF_THROUGH_SMCUTOUT,
    UF_N_SMCUTOUT_TYPE_OPTS
} ;
typedef enum UF_MODL_smcutout_type_e UF_MODL_smcutout_type_e_t;

enum UF_MODL_punch_type_e
{
  UF_EMBOSS_PUNCH = 0,
  UF_LANCE_PUNCH,
  UF_SEMI_PIERCE_PUNCH,
  UF_COIN_PUNCH
} ;
typedef enum UF_MODL_punch_type_e UF_MODL_punch_type_e_t;

enum UF_MODL_smpunch_top_type_e
{
  OFFSET_TOP_TYPE = 0,
  FLAT_TOP_TYPE,
  ROUND_TOP_TYPE,
  CONE_TOP_TYPE
} ;
typedef enum UF_MODL_smpunch_top_type_e UF_MODL_smpunch_top_type_e_t;

enum UF_MODL_smbend_curve_e
{
  UF_SMBEND_INVALID_CURVE_TYPE = -1,
  UF_SMBEND_NONE,
  UF_SMBEND_BEND_CENTERLINE,
  UF_SMBEND_BEND_AXIS,
  UF_SMBEND_BEND_TANGENT_LINE,
  UF_SMBEND_CONTOUR_LINE,
  UF_SMBEND_MOLD_LINE,
  UF_SMBEND_NUM_CURVE_TYPES
} ;
typedef enum UF_MODL_smbend_curve_e UF_MODL_smbend_curve_e_t;

enum UF_MODL_smbend_angle_e
{
  UF_SMBEND_INVALID_ANGLE_TYPE = -1,
  UF_SMBEND_BEND_ANGLE,
  UF_SMBEND_INCLUDED_ANGLE,
  UF_SMBEND_NUM_ANGLE_TYPES
} ;
typedef enum UF_MODL_smbend_angle_e UF_MODL_smbend_angle_e_t;

enum UF_MODL_smbend_radius_e
{
  UF_SMBEND_INVALID_RADIUS_TYPE = -1,
  UF_SMBEND_INNER_RADIUS,
  UF_SMBEND_OUTER_RADIUS,
  UF_SMBEND_NUM_RADIUS_TYPES
} ;
typedef enum UF_MODL_smbend_radius_e UF_MODL_smbend_radius_e_t;

enum UF_MODL_smbend_direction_e
{
  UF_SMBEND_INVALID_BEND_DIR = -1,
  UF_SMBEND_BEND_DIR_AS_SPECIFIED,
  UF_SMBEND_BEND_DIR_OPPPOSITE_SIDE,
  UF_SMBEND_NUM_BEND_DIRS
} ;
typedef enum UF_MODL_smbend_direction_e UF_MODL_smbend_direction_e_t;

enum UF_MODL_smbend_stat_side_e
{
  UF_SMBEND_INVALID_STAT_SIDE = -1,
  UF_SMBEND_STAT_SIDE_AS_SPECIFIED,
  UF_SMBEND_STAT_SIDE_OPPOSITE_SIDE,
  UF_SMBEND_NUM_STAT_SIDES
} ;
typedef enum UF_MODL_smbend_stat_side_e UF_MODL_smbend_stat_side_e_t;
/* end of smbend enumerations */


struct UF_MODL_smpunch_cut_sets_s
{
  int   num_curves;
  tag_t *curves; /* <len:num_curves> */
};
typedef struct UF_MODL_smpunch_cut_sets_s
               UF_MODL_smpunch_cut_sets_t, *UF_MODL_smpunch_cut_sets_p_t ;

struct UF_MODL_smpunch_data_s
{
  UF_MODL_punch_type_e_t            punch_type; /* punch, lance, pierce, semi pierce */
  UF_MODL_smpunch_top_type_e_t      top_type;   /* Offset, Flat, Round, Cone  */
  UF_MODL_smpunch_direction_type_e_t proj_method;/* Face, Vector, Axis        */
  tag_t    tool_center;                         /* Tag for center of tool     */
  tag_t    placement_face;                      /* Target face for punch      */
  int      n_curves;                            /* Number of outline curves   */
  tag_t    *curves;                             /* <len:n_curves> Outline curves */
  int          num_cut_curve_sets;              /* Number of cutting curve sets*/
  UF_MODL_smpunch_cut_sets_t *cut_curve_sets;   /* <len:num_cut_curve_sets> The curve sets */
  tag_t    datum_axis;                          /* Tag for datus axis         */
  char     depth[ UF_MAX_EXP_BUFSIZE ];        /* <len:UF_MAX_EXP_BUFSIZE>String for Depth */
  char     die_radius[ UF_MAX_EXP_BUFSIZE ];   /* <len:UF_MAX_EXP_BUFSIZE>String for Die Radius */
  char     taper_angle[ UF_MAX_EXP_BUFSIZE ];  /* <len:UF_MAX_EXP_BUFSIZE>String for Taper Angle */
  char     punch_radius[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>String for Punch Radius */
  char     cone_depth[ UF_MAX_EXP_BUFSIZE ];   /* <len:UF_MAX_EXP_BUFSIZE>String for Cone Depth */
  double   proj_vector[3];                      /* Projection Vector          */
  logical  flip_discard_region;                 /* Reverse Curve Dir?         */
  logical  inside_or_out;                       /* Inside or out?             */
  logical  auto_centroid;                       /* Auto Centroid?             */
} ;
typedef struct UF_MODL_smpunch_data_s UF_MODL_smpunch_data_t,
*UF_MODL_smpunch_data_p_t;

/* The following structure is used when creating, editing, or querying a
sheet metal hole.
*/
struct UF_MODL_smhole_data_s
{
    char           diameter[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE> Diameter of SMHole */
    char           depth[ UF_MAX_EXP_BUFSIZE ];    /* <len:UF_MAX_EXP_BUFSIZE> Depth of SMHole.  Only
                                                       used for depth type
                                                       SMHoles */
    char           tip_angle[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE> Tip angle of SMHole.
                                                        Only used for depth
                                                        type SMHoles */
    tag_t          edge1;                            /* Tag of the first
                                                        offset edge */
    char           offset1[ UF_MAX_EXP_BUFSIZE ];   /* <len:UF_MAX_EXP_BUFSIZE> Offset distance from
                                                        first offset edge */
    tag_t          edge2;                            /* Tag of the second
                                                        offset edge */
    char           offset2[ UF_MAX_EXP_BUFSIZE ];   /* <len:UF_MAX_EXP_BUFSIZE> Offset distance from
                                                        second offset edge */
    tag_t          hole_face;                        /* Tag of the face on
                                                        which the SMHole will
                                                        be placed */
    tag_t          thru_face;                        /* Tag of the face
                                                        through which the
                                                        Through SMHole will
                                                        be created */
    tag_t          datum_axis;                       /* Tag of the datum axis
                                                        used to determine the
                                                        angle of the central
                                                        axis of the SMHole.
                                                        Used with
                                                        UF_ALONG_DATUM_AXIS
                                                        method. */
    UF_MODL_smhole_direction_type_e_t method;/* Method used to determine angle
                                               of central axis of the SMHole.
                                              UF_FACE_NORMALS = use face normals
                                              UF_ALONG_VECTOR = use a vector
                                              UF_ALONG_DATUM_AXIS = use a
                                              datum axis*/
    double                       vec_dir[3];/* Vector used to determine the
                                               angle of the central axis of
                                               the SMHole. Used with
                                               UF_ALONG_VECTOR method*/
    UF_MODL_smhole_type_e_t      type;   /* Type of SMHole to be created.
                                          UF_DEPTH_SMHOLE = depth type SMHole
                                          UF_THROUGH_SMHOLE = thru type SMHole
                                          UF_PUNCH_SMHOLE = punch type SMHole */
} ;
typedef struct UF_MODL_smhole_data_s UF_MODL_smhole_data_t,
*UF_MODL_smhole_data_p_t;

/* The following structure is used when creating, editing, or querying a
   sheet metal slot.
*/
struct UF_MODL_smslot_data_s
{
    char                length[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE> Length of SMSlot */
    char                width[ UF_MAX_EXP_BUFSIZE ];  /* <len:UF_MAX_EXP_BUFSIZE> Width of SMSlot */
    char                depth[ UF_MAX_EXP_BUFSIZE ];  /* <len:UF_MAX_EXP_BUFSIZE>
                                                          Depth of SMSlot.
                                                          Only used for depth
                                                          type SMSlots */
    tag_t               edge1;                         /* Tag of the first
                                                          offset edge */
    char                offset1[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                           Offset distance
                                                           from first offset
                                                           edge */
    tag_t               edge2;                          /* Tag of the second
                                                           offset edge */
    char                offset2[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                           Offset distance
                                                           from second offset
                                                           edge */
    tag_t               slot_face;                      /* Tag of the face on
                                                           which the SMSlot
                                                           will be placed */
    tag_t               through_face;                   /* Tag of the face
                                                           through which the
                                                           Through SMSlot will
                                                           be created */
    UF_MODL_smslot_direction_type_e_t dir_method;/* Method used to determine
                                            angle of central axis of the SMSlot.
                                              UF_FACE_NORMALS = use face normals
                                              UF_ALONG_VECTOR = use a vector
                                              UF_ALONG_DATUM_AXIS = use a datum axis
                                                 */
    tag_t               d_datum_axis;             /* Tag of the datum axis
                                                     used to determine the
                                                     angle of the central axis
                                                     of the SMSlot.  Used when
                                                     dir_method is
                                                     UF_ALONG_DATUM_AXIS.*/
    double              d_vec_dir[3];             /* Direction vector used to
                                                     determine the angle of the
                                                     central axis of the
                                                     SMSlot.  Used when
                                                     dir_method is
                                                     UF_ALONG_VECTOR*/
    UF_MODL_smslot_direction_type_e_t orient_method;/* Method used to
                                         determine angle of the orientation
                                         along the length of the SMSlot.
                                          UF_FACE_NORMALS = use face normals
                                          UF_ALONG_VECTOR = use a vector
                                          UF_ALONG_DATUM_AXIS = use a datum axis
                                                     */
    tag_t               o_datum_axis;                /* Tag of the datum axis
                                                        used to determine the
                                                        orientation along the
                                                        length of the SMSlot.
                                                        Used when orient_method
                                                        is UF_ALONG_DATUM_AXIS.
                                                      */
    double              o_vec_dir[3];                 /* Orientation vector
                                                        used to determine the
                                                        orientation along the
                                                        length of the SMSlot.
                                                        Used when orient_method
                                                        is UF_ALONG_VECTOR.
                                                       */
    UF_MODL_smslot_type_e_t      type; /* Type of SMSlot to be created.
                                          UF_DEPTH_SMSLOT = depth type SMSlot
                                          UF_THROUGH_SMSLOT = thru type SMSlot
                                          UF_PUNCH_SMSLOT = punch type SMSlot
                                                        */
} ;
typedef struct UF_MODL_smslot_data_s UF_MODL_smslot_data_t,
*UF_MODL_smslot_data_p_t;

/*This structure is used to define the parameters for constructing the
cross sectional shape of the bead.

NOTE: The discard region is calculated by a vector pointing to the region to
be discarded.  This vector, called the discard region vector, is the cross
product between the placement face normal and the tangent of the
combined curves in the "curves" array described above.
Therefore, it is important to know the order of the curves in the
"curves" array.  Reversing the order of these curves may reverse their
tangent when combined and thus reverse the discard region vector.
*/
struct UF_MODL_smcutout_data_s
{
    tag_t                          placement_face;     /* Face to put cutout */
    int                            n_curves;           /* The number of curves
                                                         in the curves array.*/
    tag_t                          *curves;            /*<len:n_curves> An array holding the
                                                         tags to the curves
                                                         that define the
                                                         outline shape of the
                                                         SMCutout*/
    UF_MODL_smcutout_direction_type_e_t proj_method;   /* The method used to
                                                          determine the
                                                          projection vector of
                                                          the outline curves as
                                                          well as the direction
                                                          in which the cutout
                                                          will be punched
                                                          through the solid
                                                          body.  Can be one of
                                                          UF_FACE_NORMALS:
                                                            project along the
                                                            placement face
                                                            reverse normal.
                                                          UF_ALONG_VECTOR:
                                                            project along a
                                                            given vector. See
                                                            proj_vector below.
                                                          UF_ALONG_DATUM_AXIS:
                                                            project along a
                                                            given datum axis.
                                                            See datum_axis
                                                            below.*/
    double                         proj_vector[3];     /* Used when proj_method
                                                        is UF_ALONG_VECTOR.
                                                        This is the vector
                                                        along which the outline
                                                        curves will be
                                                        projected.  It also
                                                        indicates the vector
                                                        along which the cutout
                                                        will be punched through
                                                         the solid body.*/
    tag_t                          datum_axis;         /* Used when proj_method
                                                        is UF_ALONG_DATUM_AXIS.
                                                        This is the tag of a
                                                        datum axis that will
                                                        be used to determine
                                                        the vector along which
                                                        the outline curves will
                                                        be projected.  It also
                                                        indicates the vector
                                                        along which the cutout
                                                        will be punched through
                                                        the solid body.*/
    logical                        flip_discard_region;/* When true the discard
                                                       region is flipped from
                                                       its normal calculation.
                                                       See discussion above on
                                                       the discard region.*/
    UF_MODL_smcutout_type_e_t      type;               /* Punch or through   */
    tag_t                          thru_face;          /* Through face       */

} ;
typedef struct UF_MODL_smcutout_data_s UF_MODL_smcutout_data_t,
*UF_MODL_smcutout_data_p_t;

/*

    */

/* 
 */
struct UF_MODL_bracket_outline_data_s
{
    int  reference_geometry_type;       /* 0 = Clearance Points,  1 = Edge,
                                           2 = Length. The user can specify
                                               either clearance points to
                                               define the outline,  select
                                               an edge or specify a
                                               length (pad or flange)     */
    int  num_clr_pts;                   /* Number of clearance points on the
                                           reference/base face. This number
                                           is used only when
                                           reference_geometry_type = 0 ,
                                           i.e when  clearance points are
                                           specified .  The minimum number of
                                           points can be  one and maximum of
                                           two points                      */
    union {
              double    clr_pts[2][3];  /* base or reference               */
              tag_t     edge_tag;       /* base or reference               */
              char      *length;        /* pad length or flange length     */
          } data;
};

/*

*/
typedef struct UF_MODL_bracket_outline_data_s
               UF_MODL_bracket_outline_data_t, *UF_MODL_bracket_outline_data_p_t;


struct UF_MODL_smbracket_data_s
{
    tag_t           base_face;          /* base face tag                   */

    tag_t           ref_face;           /* reference face tag              */

    logical         mat_direction;      /* 0 = inside - inside,
                                           1 = outside - outside           */

    UF_MODL_bracket_outline_data_p_t  base_outline_data;/* outline data for
                                                           ref face */

    UF_MODL_bracket_outline_data_p_t  ref_outline_data; /* outline data to
                                                        define the base pad */
    char            *clr_dist;          /* clearance distance              */

    char            *bend_radius;       /* bend radius                     */

    char            *chordal_tol;       /* chordal tolerance               */

    char            *linear_tol;        /* linear  tolerance               */

    char            *mat_thickness;     /* Material thickness              */

    logical         rounded_flag;       /* 0 - no fillets,
                                           1 - fillets,                    */

    char            *bend_allow_formula;/* bend allowance formula          */

    char            *offset_dist;       /* dist by which ref face is offset*/

    logical         allow_sec_fail;     /* 1 - allow general flange to
                                           create , even if some sections
                                           fail linear tolerance check.

                                           0 - throw up error for this     */

    int             outline_type;       /* 0 - between circles,
                                           1 - normal to circles
                                           2 - Use points. end_points  will be
                                           used here , when this option is 2 */
    double          end_points[2][3];  /* Two points in ABS coordinates.
                                          These points will be projected
                                          on to the intersection curve and
                                          will be used to define the width
                                          of the bracket at the bend area  */

     double         pick_points[2][3];  /* Two points in ABS coordinates.
                                           These points will be used to
                                           determine the quadrant in which
                                           the bracket would be created.
                                           The first point is on base face.
                                           The second point is on reference
                                           face.                           */
};
typedef struct UF_MODL_smbracket_data_s
               UF_MODL_smbracket_data_t, *UF_MODL_smbracket_data_p_t;

struct UF_MODL_smrelief_data_s
{
tag_t     base_face;                               /* Planar face or any face
                                                      of a           flange */
tag_t     first_corner_edges[2];                   /* Edges defining the first
                                                      corner, should be in the
                                                      plane  of the base face,
                                                      These edges must
                                                      intersect.            */
tag_t     second_corner_edges[2];                  /* Edges defining the
                                                      second corner, should
                                                      be in the plane of the
                                                      base face, these edges
                                                      must intersect */
double    offset_corner[3];                        /* Edges defining the third
                                                      corner, should be in
                                                      the plane  of the base
                                                      face                  */
char      *first_corner_fillet_radius;             /* radius value for first
                                                      corner fillet .
                                                      This has to be greater
                                                      than zero             */
char      *second_corner_fillet_radius;            /* radius value for second
                                                      corner fillet .
                                                      This value has to be
                                                      greater than zero     */
char      *os_circle_radius;                       /* radius value for offset
                                                      corner fillet.  This
                                                      value must be greater
                                                      than zero             */
char      *offset_distance;                        /* distance by which fillet
                                                      will be offset inside
                                                      the body  from the
                                                      offset corner  . This
                                                      value must be greater
                                                      than  or equal to zero
                                                      and less than
                                                      offset_corner_fillet_
                                                      radius                */
};
typedef struct UF_MODL_smrelief_data_s
               UF_MODL_smrelief_data_t, *UF_MODL_smrelief_data_p_t;

struct UF_MODL_smjoggle_data_s
{
    tag_t     base_face;         /* <I> */
    tag_t     ref_face1;         /* <I> */
    tag_t     ref_face2;         /* <I> */
    tag_t     trans_start_edge;  /* <I> Transition start edge tag          */
    tag_t     trans_end_edge;    /* <I> Transition end edge tag          */
    tag_t     base_edge;         /* <I> Base_edge tag - in case an edge is
                                 ** picked instead of clr points     */
    double    point_on_rf1[3];  /* <I> Pick point on ref face1, used to
                                 ** infer mat direction, and to identify the
                                 ** joggle creation side */
    double    point_on_rf2[3];   /* <I> pick point on ref face2, used to
                                 ** infer mat direction, and to identify the
                                 ** joggle creation side */
    int       num_clr_pts;       /* No. of clearance points, 1/2 */
    double    clr_point1[3];     /* <I> First clearance point */
    double    clr_point2[3];     /* <I> Second Clearance point */
    logical   mat_direction;     /* <I> inside-inside=0 , outside-outside=1 */
    char      *clr_dist;         /* <I> clearance distance    */
    char      *bend_radius1;     /* <I> Ref Face1 - Base Face bend radius */
    char      *bend_radius2;     /* <I> Ref Face2 - Base Face bend radius */
    char      *transition_radius; /* <I> Ref Face - Trans Face blend radius */
    char      *run;              /* <I> */
    logical   table;             /* <I> Use table or not */
    logical   edge_to_edge;      /* <I> Is joggle of edge_to_edge type? */
    char      *mat_thickness;    /* <I> Material thickness */
    char      *bend_allowance_formula; /* <I> */
};
typedef struct UF_MODL_smjoggle_data_s
               UF_MODL_smjoggle_data_t, *UF_MODL_smjoggle_data_p_t;

/* This structure contains the parametric information used to define
 * a flange feature. */
struct UF_MODL_flange_data_s
{
    int             angle_type;     /* Bend or Included angle. */
    int             length_type;    /* Tangent or Contour length. */
    int             radius_type;    /* Inside or Outside radius. */
    int             ltaper_type;    /* Left Side: Flange, Bend Area, or Web. */
    int             rtaper_type;    /* Right Side: Flange, Bend Area, or Web. */
    logical         reverse_direction; /* Negate direction: X x Z. TRUE/FALSE */
    int             ref_line_type;   /* None(0), Contour(1), Mold(2), Both(3) */
    char            *thickness;     /* Thickness expression. */
    char            *width;         /* Width expression. */
    char            *angle;         /* Angle expression. */
    char            *length;        /* Length expression. */
    char            *radius;        /* Radius expression. */
    int             left_joint_type; /* None(0), Taper(1), Simple Miter(2),
                                        Full Miter(3), Butt(4). */
    int             right_joint_type; /* None(0), Taper(1), Simple Miter(2),
                                         Full Miter(3), Butt(4). */
    char            *ltaper[2];     /* Left Taper Angles expression. */
    char            *rtaper[2];     /* Right Taper Angles expression. */
    char            *lmiter[3];     /* Left Miter angle, Miter Phase Angle
                                       and Miter Relief angle. */
    char            *rmiter[3];     /* Right Miter angle, Miter Phase Angle
                                       and Miter Relief angle. */
    char            *lbutt;         /* Left Butt length */
    char            *rbutt;         /* Right Butt length */
    char            *bend_allowance_formula; /* Bend Allowance Formula */
};

typedef struct UF_MODL_flange_data_s UF_MODL_flange_data_t,
*UF_MODL_flange_data_p_t;

/* This structure represents the information necessary to create
 * an inset flange feature. */
struct UF_MODL_inset_flange_data_s
{
    UF_MODL_flange_data_p_t  flange_data;  /* Inheritted flange information. */
    int     inset_type;   /* Inset Dimension: Expression, Outer Tangent,
                             Inner Tangent, Outer Mold Line, DIN Mold Line,
                             Inner Mold Line. */
    int     lrelief_type; /* Left Side: None, Rectangular, Obround. */
    int     rrelief_type; /* Right Side: None, Rectangular, Obround. */
    char    *inset;       /* Inset expression. */
    char    *lrelief;     /* Left Relief expression. */
    char    *rrelief;     /* Right Relief expression. */
} ;

typedef struct UF_MODL_inset_flange_data_s UF_MODL_inset_flange_data_t,
*UF_MODL_inset_flange_data_p_t;

enum UF_MODL_gflange_e
{
    UF_MODL_gflange_parm = 0,
    UF_MODL_gflange_sections,
    UF_MODL_gflange_faces,
    UF_MODL_gflange_vector
};
typedef enum UF_MODL_gflange_e UF_MODL_gflange_mode_t,
                               *UF_MODL_gflange_mode_p_t;

enum UF_MODL_gflange_distort_e
{
    UF_MODL_gflange_along_sections =0,
    UF_MODL_gflange_bidirectional
};
typedef enum  UF_MODL_gflange_distort_e UF_MODL_gflange_distort_t,
                                        *UF_MODL_gflange_distort_p_t;

struct UF_MODL_gflange_options_data_s {
    logical     infer_thickness;    /* TRUE  = Thickness derived from target
                                               geometry,
                                       FALSE = To be given explicitly */
    logical     infer_spine;        /* TRUE  = System generates spine normal to
                                               all section curves.
                                       FALSE = Use bend edge or spine */
    char        r_value[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE >
                                                   average strain ratio.
                                                   For homogenous material this
                                                   value is 1. r_value is used
                                                   when  area_preserve is set
                                                   to FALSE. */
    logical     area_preserve;      /* FALSE = Use the above r_value,
                                       TRUE  = Do not use the  r_value, set
                                               it to infinite. */
    UF_MODL_gflange_distort_t  distortion;   /* Distortion  */
    char        tolerance[ UF_MAX_EXP_BUFSIZE ];   /* <len:UF_MAX_EXP_BUFSIZE >
                                                   Tolerance */
    char        max_sample_pts[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE >
                                                          Maximum number of
                                                          sample points */
    logical     contour_lines;      /* Contour Lines  */
    logical     form_block_lines;   /* Form Block Lines */
    logical     mold_lines;         /* Mold Lines */
};
typedef struct UF_MODL_gflange_options_data_s UF_MODL_gflange_options_data_t,
                                              *UF_MODL_gflange_options_data_p_t;

struct UF_MODL_gflange_parameters_mode_data_s {
    int              step_count;         /* The number of steps in the
                                            generalized flange.  Zero is an
                                            invalid number. For each step
                                            include a value for the
                                            bend  radius, bend angle and web
                                            length. */
    UF_MODL_parm_p_t plus;               /* <len:step_count>
                                            The law specification of the target
                                            face extension between the bend edge
                                            and the start of the bend. This is
                                            an array with step_count entries.*/
    UF_MODL_parm_p_t   bend_radius;      /* <len:step_count>
                                            The law specification of the radius
                                            of the bend. This is an array with
                                            step_count entries */
    UF_MODL_parm_p_t   bend_angle;       /* <len:step_count>
                                            The law specification of the angle
                                            of the bend. This is an array with
                                            step count entries. */

    UF_MODL_parm_p_t   web_length;       /* <len:step_count>
                                            The law specification of the length
                                            of the surface  extension after the
                                            bend. This is an array with step
                                            count entries. */

    int                *radius_in_out;   /* <len:step_count>
                                            Inner/Outer radius for steps
                                            0 = inner radius in use
                                            1 = outer radius in use,
                                            This is an array with step count
                                            entries.  */

    logical          flip_bend_direction; /* TRUE =  Bend in the direction
                                                     opposite to  the system
                                                     inferred bend direction.
                                             FALSE = Use system inferred bend
                                                     direction. */
};
typedef struct UF_MODL_gflange_parameters_mode_data_s
                           UF_MODL_gflange_parameters_mode_data_t,
                           *UF_MODL_gflange_parameters_mode_data_p_t;

struct UF_MODL_gflange_sections_mode_data_s {
    UF_STRING_p_t section_curves;  /* Each section must consist of curves
                                      and/or edges that comprise an open G1
                                      string.  They must start  tangent to
                                      the target face. Each section  must lie
                                      in a plane that is normal to spine.
                                      One end of the each section  must touch
                                      the bend edge. */
    logical   extend_start;        /* TRUE =  Maintain a constant section from
                                              last defined  section to the
                                              spine start.
                                      FALSE = To create generalized flange
                                              till the  last  section near the
                                              spine start */
    logical   extend_end;          /* TRUE =  Maintain a constant   section
                                              from last defined  section to
                                              the spine end.
                                      FALSE = To create generalized flange
                                              till the  last  section near
                                              the spine end */
};
typedef struct UF_MODL_gflange_sections_mode_data_s
                                   UF_MODL_gflange_sections_mode_data_t,
                                   *UF_MODL_gflange_sections_mode_data_p_t;

struct UF_MODL_gflange_shaping_faces_mode_data_s {
    int    number_shaping_faces;    /* Number of shaping faces */
    tag_p_t  shaping_faces;         /* Shaping faces . They must not be from
                                      the body of the  target faces. They
                                      must be G1 continuous faces from a
                                      single  body. They must be G1 with the
                                      target faces at the  bend edge. */
};

typedef struct UF_MODL_gflange_shaping_faces_mode_data_s
                                   UF_MODL_gflange_shaping_faces_mode_data_t,
                                  *UF_MODL_gflange_shaping_faces_mode_data_p_t;

struct UF_MODL_gflange_punch_vector_mode_data_s {
    int                step_count;     /* The number of steps in the
                                          generalized flange. Zero is an
                                          invalid number. For each step
                                          include a value for the bend
                                          radius, bend angle  and web length */
    UF_MODL_parm_p_t   plus;           /* <len:step_count>
                                          The law specification of the target
                                          face extension between the bend edge
                                          and the start of the bend. This is
                                          an array with step count entries. */
    UF_MODL_parm_p_t     bend_radius;  /* <len:step_count>
                                          The law specification of the radius
                                          of  the bend. This is an array
                                          with step count entries.*/
    UF_MODL_parm_p_t     bend_angle;   /* <len:step_count>
                                          The law specification of the angle of
                                          the bend.This is an array with
                                          step count entries. */
    UF_MODL_parm_p_t     web_length;   /* <len:step_count>
                                          The law specification of the length
                                          of the surface  extension after the
                                          bend. This is an array with step count
                                          entries. */
    int                *radius_in_out;   /* <len:step_count>
                                            Inner/Outer radius for steps
                                            0 = inner radius in use
                                            1 = outer radius in use
                                            Dimension of the array
                                            = step_count  */
    UF_MODL_vector_p_t punch_vector;   /* Punch Vector */
    logical       flip_bend_direction; /* TRUE =  Bend in the direction
                                                  opposite to  the system
                                                  inferred bend direction.
                                          FALSE = Use system inferred bend
                                                  direction. */
};

typedef struct UF_MODL_gflange_punch_vector_mode_data_s
                                 UF_MODL_gflange_punch_vector_mode_data_t,
                                 *UF_MODL_gflange_punch_vector_mode_data_p_t;

union UF_MODL_mode_specific_data_u
{
    UF_MODL_gflange_parameters_mode_data_t    *gflange_parameters_mode_data;
    UF_MODL_gflange_sections_mode_data_t      *gflange_sections_mode_data;
    UF_MODL_gflange_shaping_faces_mode_data_t *gflange_shaping_faces_mode_data;
    UF_MODL_gflange_punch_vector_mode_data_t  *gflange_punch_vector_mode_data;
};

typedef union UF_MODL_mode_specific_data_u  UF_MODL_mode_specific_data_t;


struct UF_MODL_genflg_state_data_s
{

    char                tolerance_str[ UF_MAX_EXP_BUFSIZE ];  /* Tolerance */

    UF_MODL_parm_p_t    plus;               /* The law specification of the target
                                            face extension between the bend edge
                                            and the start of the bend. This is
                                            an array with step_count entries.*/

    UF_MODL_parm_p_t   bend_radius;      /* The law specification of the radius
                                            of the bend. This is an array with
                                            step_count entries */

    UF_MODL_parm_p_t   bend_angle;       /* The law specification of the angle
                                            of the bend. This is an array with
                                            step count entries. */

    UF_MODL_parm_p_t   web_length;       /* The law specification of the length
                                            of the surface  extension after the
                                            bend. This is an array with step
                                            count entries. */

    char               r_value_str[ UF_MAX_EXP_BUFSIZE ]; /* Average strain ratio.
                                                   For homogenous material this
                                                   value is 1. r_value is used
                                                   when  area_preserve is set
                                                   to FALSE. */

};
typedef struct UF_MODL_genflg_state_data_s
               UF_MODL_genflg_state_data_t, *UF_MODL_genflg_state_data_p_t;


struct UF_MODL_gflange_data_s {

    UF_STRING_p_t           bend_edge;          /* An edge in the tangent face
                                                   used as the  attachment edge
                                                   for  the  generalized
                                                   flange */
    logical                 add_tangent_edges;  /* TRUE  = selects all edges
                                                   tangent to the selected edge.
                                                   FALSE = do not allow tangent
                                                   edges */

    UF_STRING_p_t           spine;              /* An edge or curve used to
                                                   define the  section  planes
                                                   for the bend  and web. If
                                                   this values is null, the
                                                   bend edge  string is used
                                                   as the spine  string. */

    UF_MODL_gflange_mode_t  mode;               /* Flange Creation Mode */

    UF_MODL_mode_specific_data_t gflange_mode_specific_data;  /* Input data
                                                                 specific to the
                                                                 generalized
                                                                 flange
                                                                 creation
                                                                 mode */

    char thickness_str[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                Thickness of the solid body
                                                created.  If the Modeling
                                                preference for body type is
                                                set to  solid,  this is used
                                                only when   infer_thickness is
                                                set to FALSE */
    int          number_target_faces;        /* Number of target faces */
    tag_p_t      target_faces;               /* <len:number_target_faces> Target Faces */
    char *bend_allow_formula;                /* Bend Allowance Formula*/
    UF_MODL_gflange_options_data_p_t gflange_options;  /* General Flange
                                                      options */
};

typedef struct UF_MODL_gflange_data_s UF_MODL_gflange_data_t,
                                      *UF_MODL_gflange_data_p_t;

/* smbend feature structure*/
struct UF_MODL_smbend_data_s
{
    tag_t                     base_face;          /* Base Face               */
    tag_t                     app_curve;          /* Application Curve Tag   */
    UF_MODL_smbend_curve_e_t  app_curve_type;     /* Application Curve Type
                                                     SMBEND_NONE
                                                     SMBEND_BEND_CENTERLINE
                                                     SMBEND_BEND_AXIS
                                                     SMBEND_BEND_TANGENT_LINE
                                                     SMBEND_CONTOUR_LINE
                                                     SMBEND_MOLD_LINE        */
    char                      angle[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                     Bend Angle      */
    UF_MODL_smbend_angle_e_t  angle_type;         /* Angle Type
                                                     SMBEND_BEND_ANGLE
                                                     SMBEND_INCLUDED_ANGLE   */
    char                      radius[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                              Bend Radius    */
    UF_MODL_smbend_radius_e_t radius_type;        /* Radius Type
                                                     SMBEND_INNER_RADIUS
                                                     SMBEND_OUTER_RADIUS     */
    UF_MODL_smbend_direction_e_t bend_dir;        /* Bend Direction
                                                     SMBEND_AS_SPECIFIED
                                                     SMBEND_OPPOSITE_SIDE    */
    UF_MODL_smbend_stat_side_e_t stat_side;   /* Stationary Side
                                                     SMBEND_AS_SPECIFIED
                                                     SMBEND_OPPOSITE_SIDE    */
    char                      baf[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                           Bend Allowance Formula*/
};
typedef struct UF_MODL_smbend_data_s
               UF_MODL_smbend_data_t, *UF_MODL_smbend_data_p_t;

/* smbend converted corner feature structure*/
struct UF_MODL_smbend_corner_data_s
{
    tag_t                     base_edge;          /* Base Face               */
    char                      radius[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                              Bend Radius    */
    UF_MODL_smbend_radius_e_t radius_type;        /* Radius Type
                                                     SMBEND_INNER_RADIUS
                                                     SMBEND_OUTER_RADIUS     */
    UF_MODL_smbend_stat_side_e_t stat_side;       /* Stationary Side
                                                     SMBEND_AS_SPECIFIED
                                                     SMBEND_OPPOSITE_SIDE    */
    char                      baf[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                           Bend Allowance Formula*/
};
typedef struct UF_MODL_smbend_corner_data_s
               UF_MODL_smbend_corner_data_t, *UF_MODL_smbend_corner_data_p_t;

/* smbend converted cylinder feature structure*/
struct UF_MODL_smbend_cylinder_data_s
{
    tag_t                     base_face;          /* Base Face               */
    UF_MODL_smbend_stat_side_e_t stat_side;       /* Stationary Side
                                                     SMBEND_AS_SPECIFIED
                                                     SMBEND_OPPOSITE_SIDE    */
    char                      baf[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                           Bend Allowance Formula*/
};
typedef struct UF_MODL_smbend_cylinder_data_s
               UF_MODL_smbend_cylinder_data_t, *UF_MODL_smbend_cylinder_data_p_t;



typedef enum
{
    UF_MODL_bend_operation_unbend = 0,
    UF_MODL_bend_operation_rebend,
    UF_MODL_bend_operation_bend_to_angle

} UF_MODL_bend_operation_e_t;

/* Bend operation data */
struct UF_MODL_bend_operation_data_s
{
    UF_MODL_bend_operation_e_t operation_type;    /* Bend operation type */

    tag_t                      bend_edge;         /* Bend edge */

    tag_t                      bend_face;         /* Bend face */

                                                  /* Use Adjacent Bend Face
                                                     switch */
    logical                    use_adjacent_bend_face;

    tag_t                      parent_operation;  /* Parent operation */


    char                       target_angle[ UF_MAX_EXP_BUFSIZE ]; /* <len:UF_MAX_EXP_BUFSIZE>
                                                     Target angle */


    char                       baf[ UF_MAX_EXP_BUFSIZE ];/* <len:UF_MAX_EXP_BUFSIZE>
                                                     Bend allowance formula */

    logical                    use_global_baf;    /* Use Global BAF switch */
};
typedef struct UF_MODL_bend_operation_data_s
               UF_MODL_bend_operation_data_t, *UF_MODL_bend_operation_data_p_t;


/**************************************************************************
*             API DATA STRUCTURE FOR THE SOLID PUNCH FEATURE.
**************************************************************************/

/* NOTE: These types should be same as the types defined in smspunch.h */
typedef enum
{
    UF_MODL_smspunch_invalid = -1,
    UF_MODL_smspunch_punch,
    UF_MODL_smspunch_die
} UF_MODL_smspunch_type_t;

struct UF_MODL_solid_punch_data_s
{
    int                      type;      /* punch type = 0; die type = 1 */
    int                      thickness_option; /* 0 - infer,1 - use exp */
    char                     thickness[ UF_MAX_EXP_BUFSIZE ];
                                       /*  <len:UF_MAX_EXP_BUFSIZE
                                           Thickness of the solid punch */
    tag_t                    target_face; /* Top target face */
    tag_t                    tool_body;   /* punch or die tool */
    tag_t                    target_csys_pt; /* A point or CSYS eid. This is
                                                FROM location from which
                                                a copy of the tool body
                                                is transformed. */
    tag_t                    tool_csys_pt; /* A point or CSYS eid. This is
                                                TO location to which the
                                                a copy of the tool body
                                                is transformed. */
    int                      n_pierce_faces; /* Number of pierce faces */
    tag_t                    *pierce_faces;  /* <len:n_pierce_faces> array of pierce faces */
    logical                  is_pt_required; /* Wether centroid is required
                                                or NOT */
};
typedef struct UF_MODL_solid_punch_data_s
               UF_MODL_solid_punch_data_t, *UF_MODL_solid_punch_data_p_t;

/* This enumeration is same as the enumeration defined in smcorner.h. If any
   changes made in the smcorner.h, please make changes here also. */
typedef enum
{
    UF_MODL_smcorner_invalid = -1,
    UF_MODL_smcorner_butt,
    UF_MODL_smcorner_machinery,
    UF_MODL_smcorner_simple_miter,
    UF_MODL_smcorner_full_miter
} UF_MODL_smcorner_type_t;

struct UF_MODL_smcorner_data_s
{
    int             corner_type;      /* smcorner type */

    tag_t           ref_edge;  /* side edge closest to the common edge */
    tag_t           ref_face;  /* side face closest to the common edge */

    char            butt_gap[ UF_MAX_EXP_BUFSIZE ]; /* butt joint gap. used only
                                                     for butt joint. */
    char            butt_overlap[ UF_MAX_EXP_BUFSIZE ]; /* butt joint overlap.
                                                     Used only for butt joint */

    char            mc_offset[ UF_MAX_EXP_BUFSIZE ]; /* Machinery corner offset */
    char            mc_gap[ UF_MAX_EXP_BUFSIZE ]; /* Machinery corner gap */
    logical         mc_linear_shape; /* Machinery corner shape */
    logical         use_enhanced_mach_corner; /* Machinery corner shape */

    logical         switch_parent_flag; /* Switch parents or not. Used only
                                           for butt and machinery corners. */

    char            simple_gap[ UF_MAX_EXP_BUFSIZE ]; /* simple miter gap. Used
                                                     only for simple miter. */

    logical         miter_toggle; /* multiple corners for simple and full
                                     miters only */

};
typedef struct UF_MODL_smcorner_data_s
               UF_MODL_smcorner_data_t, *UF_MODL_smcorner_data_p_t;


struct UF_MODL_ripedge_data_s
{
    int        n_ripedges;                  /* Number of rip edges */
    tag_p_t    ripedges;                    /* <len:n_ripedges> Array of rip edges */
    logical    add_tangent;                 /* To add tangent edges or not */
    int        gap_type;                    /* 0 - Gap, 1 - Offset */
    char       gap[ UF_MAX_EXP_BUFSIZE ];    /* Gap value Gap type */
    char       offset[ UF_MAX_EXP_BUFSIZE ]; /* Offset value - Offset type */
    char       extension[ UF_MAX_EXP_BUFSIZE ]; /* extension value */
    int        end_condition;               /* 0 - Rectangular, 1 - Obround */
};
typedef struct UF_MODL_ripedge_data_s
               UF_MODL_ripedge_data_t, *UF_MODL_ripedge_data_p_t;

/******************************************************************************
 * This procedure creates an SMPunch feature.
 *
 * Environment : Internal and External
 *
 * See Also :
 *  UF_MODL_edit_smpunch
 *  UF_MODL_ask_smpunch
 *
 * History : Originally released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smpunch
(
 UF_MODL_smpunch_data_p_t     user_data, /* <I>
                                         Data describing the punch to be
                                         created.
                                         */
 tag_p_t                      punch_tag  /* <O>
                                         Object identifier of the created punch.
                                         */
);

/******************************************************************************
 * Change an existing SMPunch feature's parameters to
 * the parameters given in user_data.  The caller should first call
 * UF_MODL_ask_smpunch to get the current parameters for the punch, then
 * change the elements that need to be changed, and then call
 * UF_MODL_edit_smpunch.
 *
 * Environment : Internal and External
 *
 * See Also :
 *  UF_MODL_ask_smpunch
 *  UF_MODL_create_smpunch
 *
 * History : Originally released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_smpunch
(
 UF_MODL_smpunch_data_p_t     user_data, /* <I>
                                         Data describing the punch edits.
                                         */
 tag_t                        punch_tag  /* <I>
                                         The object identifier of the punch
                                         feature to be modified.
                                         */
);

/******************************************************************************
 * Query the feature information from the given SMPunch tag.
 *
 * Environment : Internal and External
 *
 * See Also :
 *  UF_MODL_create_smpunch
 *  UF_MODL_edit_smpunch
 *
 * History : Originally released in V16.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_smpunch
(
 UF_MODL_smpunch_data_p_t     user_data, /* <O>
                                         Data describing the punch feature.
                                         */
 tag_t                        punch_tag  /* <I>
                                         The object identifier of the punch
                                         feature to be queried.
                                         */
);

/*****************************************************************************
Creates a sheet metal hole.

Environment: Internal  and  External
See Also:
 UF_MODL_smhole_data_p_t
History: Original release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smhole(
 UF_MODL_smhole_data_p_t user_data ,/* <I>
                                   Pointer to a UF_MODL_smhole_data_s
                                   data structure
                                   */
tag_p_t hole_tag  /* <O>
                  Pointer to the tag of the SMHole that gets
                  created
                  */
);

/*****************************************************************************
Edits an existing sheet metal hole.

Environment: Internal  and  External
See Also:
 UF_MODL_smhole_data_p_t
History:Original release was in V14.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_smhole(
tag_t hole_tag ,/* <I>
                Tag of the SMHole to edit
                */
UF_MODL_smhole_data_p_t user_data  /* <I>
                                   Pointer to user's modified
                                   UF_MODL_smhole_data_s data structure
                                   */
);

/******************************************************************************
Returns the parameter information of an existing sheet metal hole.

Environment: Internal  and  External
See Also:
 UF_MODL_smhole_data_p_t
History:Original release was in V14.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_smhole(
tag_t hole_tag ,/* <I>
                Tag of the SMHole from which to get
                information
                */
UF_MODL_smhole_data_p_t user_data  /* <O>
                                   Pass in a pointer to an UF_MODL_smhole_data_s
                                   data structure.  This routine will fill it
                                   with information about the SMHole
                                   */
);

/*******************************************************************************
Creates a sheet metal slot.

Environment: Internal  and  External
See Also:
 UF_MODL_smslot_data_p_t
History:Original release was in V14.0.
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smslot(
UF_MODL_smslot_data_p_t user_data ,/* <I>
                                   Pointer to a UF_MODL_smslot_data_s
                                   data structure
                                   */
tag_p_t slot_tag  /* <O>
                  Pointer to the tag of the SMSlot that gets
                  created
                  */
);

/******************************************************************************
Edits an existing sheet metal slot.

Environment: Internal  and  External
See Also:
 UF_MODL_smslot_data_p_t
History:Original release was in V14.0.

 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_smslot(
tag_t slot_tag ,/* <I>
                Tag of the SMSlot to edit
                */
UF_MODL_smslot_data_p_t user_data  /* <I>
                                   Pointer to user's modified
                                   UF_MODL_smslot_data_s data structure
                                   */
);

/******************************************************************************
Returns the parameter information of an existing sheet metal slot.

Environment: Internal  and  External
See Also:
 UF_MODL_smslot_data_p_t
History:Original release was in V14.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_smslot(
tag_t slot_tag ,/* <I>
                Tag of the SMSlot from which to get
                information
                */
UF_MODL_smslot_data_p_t user_data  /* <O>
                                   Pointer to a UF_MODL_smslot_data_s
                                   data structure containing information
                                   about the SMSlot
                                   */
);

/******************************************************************************
Creates a sheet metal cutout (SMCUTOUT) feature by providing its placement
face, outline curves, and projection direction.  The output of this function
is the object identifier of the SMCutout feature.

Environment: Internal  and  External
See Also:
 UF_MODL_smcutout_data_p_t
History:Original release was in V15.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smcutout
(
    UF_MODL_smcutout_data_p_t user_data, /* <I>
                                         Data needed to create cutout
                                         */
    tag_p_t                   cutout_tag /* <O>
                                         Tag of cutout created
                                         */
);

/******************************************************************************
Changes the parameter data of an existing sheet metal cutout (SMCutout) feature
by providing the object identifier associated to the SMCutout feature and a new
SMCutout parameter data structure.

Environment: Internal  and  External
See Also:
 UF_MODL_smcutout_data_p_t
History:Original release was in V15.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_smcutout
(
    tag_t                     cutout_tag, /* <I>
                                          Tag of cutout to change
                                          */
    UF_MODL_smcutout_data_p_t user_data   /* <I>
                                          New data for cutout parms
                                          */
);

/******************************************************************************
Queries the data of a sheet metal cutout (SMCUTOUT) feature by providing the
object identifier of the SMCutout feature.

Environment: Internal  and  External
See Also:
 UF_MODL_smcutout_data_p_t
History:Original release was in V15.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_smcutout
(
    tag_t                     cutout_tag, /* <I>
                                          Tag of cutout feature
                                          */
    UF_MODL_smcutout_data_p_t user_data   /* <OF>
                                          Data read from cutout
                                          NEEDS A FREE ROUTINE
                                          */
);

/******************************************************************************
Creates a bead.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_bead (
UF_MODL_project_curves_p_t centerline ,/* <I>
                                       Pointer to information to define the
                                       centerline of the bead.
                                       */
UF_MODL_faces_p_t placement_faces ,/* <I>
                                   Pointer to information to define the
                                   face(s) where the bead is placed.
                                   The first face is used to determine
                                   the target body.
                                   */
UF_MODL_offset_trans_faces_p_t secondary_faces ,/* <I>
                                                Pointer to information to define
                                                the optional secondary faces
                                                for the bead. The secondary
                                                faces can either be an offset
                                                or translation of the specified
                                                faces.  If it is desired to have
                                                the placement faces, then
                                                just set UF_MODL_faces_p_t
                                                pointer within this input
                                                pointer value A null pointer
                                                should be passed in if not used.
                                                */
UF_MODL_bead_section_plane_p_t section_plane ,/* <I>
                                              Pointer to direction information
                                              to define the normal of the
                                              orientation plane of the bead
                                              sections.
                                              */
UF_MODL_vector_p_t section_axis ,/* <I>
                                 Pointer to direction information to
                                 define the centerline of the bead
                                 cross section.  This parameter is
                                 also used to determine whether the
                                 bead is subtracted or united with
                                 the body of the first
                                 placement_face.
                                 */
UF_MODL_bead_section_parms_p_t section_parms ,/* <I>
                                              Pointer to information to define
                                              the cross sectional shape of the
                                              bead.
                                              */
tag_t* bead_tag  /* <O>
                 Object tag for the bead feature.
                 */
);

/******************************************************************************
Edits the various parameters of the bead and reconstructs it based on
these new parameters.

Environment: Internal  and  External
See Also:
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_bead(
tag_t bead_tag ,/* <I>
                Object tag for the bead feature to be
                edited.
                */
UF_MODL_project_curves_p_t centerline ,/* <I>
                                       Pointer to information to define the
                                       centerline of the bead.
                                       */
UF_MODL_faces_p_t placement_faces ,/* <I>
                                   Pointer to information to define the faces
                                   where the bead is to be placed.
                                   */
UF_MODL_offset_trans_faces_p_t secondary_faces ,/* <I>
                                                the optional secondary faces
                                                for the bead.  A null pointer
                                                should be passed in if this is
                                                not used.
                                                */
UF_MODL_bead_section_plane_p_t section_plane ,/* <I>
                                              Pointer to direction information
                                              to define the normal of the
                                              orientation plane of the bead
                                              sections.
                                              */
UF_MODL_vector_p_t section_axis ,/* <I>
                                 Pointer to direction information to define
                                 the centerline of the bead cross section.
                                 This parameter is also used to determine
                                 whether the bead is subtracted or united
                                 with the body of the first placement_face.
                                 */
UF_MODL_bead_section_parms_p_t section_parms  /* <I>
                                              Pointer to information to define
                                              the cross sectional shape of the
                                              bead.
                                              */
);

/******************************************************************************
Retrieves the parameters used to create a bead.

Environment: Internal  and  External
See Also: UF_MODL_free_bead

History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_bead(
tag_t bead_tag ,/* <I>
                Object tag for the bead feature
                */
UF_MODL_project_curves_p_t centerline ,/* <OF,free:UF_MODL_free_bead>
                                       Pointer to information which defines
                                       the centerline of the bead.  The caller
                                       must allocate a UF_MODL_project_curves_t
                                       structure and pass in a pointer to it.
                                       This routine will fill the structure
                                       with allocated data which must be freed
                                       by calling UF_MODL_free_bead.
                                       */
UF_MODL_faces_p_t placement_faces ,/* <OF>
                                   Pointer to information which defines the
                                   placement faces for the bead.  The caller
                                   must allocate a UF_MODL_faces_t
                                   structure and pass in a pointer to it.
                                   This routine will fill the structure
                                   with allocated data which must be freed
                                   by calling UF_MODL_free_bead.
                                   */
UF_MODL_offset_trans_faces_p_t secondary_faces ,/* <OF>
                                   Pointer to information used to define the
                                   optional secondary faces for the bead. The
                                   caller must allocate a
                                   UF_MODL_offset_trans_faces_t
                                   structure and pass in a pointer to it.
                                   This routine will fill the structure
                                   with allocated data which must be freed
                                   by calling UF_MODL_free_bead.
                                   */
UF_MODL_bead_section_plane_p_t section_plane ,/* <OF>
                                   Pointer to direction information for the
                                   orientation plane normal of the bead
                                   sections.  The caller must allocate a
                                   UF_MODL_bead_section_plane_t
                                   structure and pass in a pointer to it.
                                   This routine will fill the structure
                                   with allocated data which must be freed
                                   by calling UF_MODL_free_bead.
                                   */
UF_MODL_vector_p_t section_axis ,/* <OF>
                                 Pointer to direction information for
                                 the centerline of the bead cross
                                 section.  The caller must allocate a
                                 UF_MODL_vector_t structure and pass in a
                                 pointer to it.  This routine will fill the
                                 structure with allocated data which must be
                                 freed by calling UF_MODL_free_bead.
                                 */
UF_MODL_bead_section_parms_p_t section_parms  /* <OF>
                                 Pointer to information which defines the cross
                                 sectional shape of the bead.  The caller must
                                 allocate a UF_MODL_bead_section_parms_t
                                 structure and pass in a pointer to it.  This
                                 routine will fill the structure with allocated
                                 data which must be freed by calling
                                 UF_MODL_free_bead.
                                 */
);

/******************************************************************************
Frees all the memory associated with the parameters returned from
UF_MODL_ask_bead.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_free_bead(
UF_MODL_project_curves_p_t centerline ,/* <I>
                                       Pointer to information to define the
                                       centerline of the bead.
                                       */
UF_MODL_faces_p_t placement_faces ,/* <I>
                                   Pointer to information to define the faces
                                   where the bead is to be placed.
                                   */
UF_MODL_offset_trans_faces_p_t secondary_faces ,/* <I>
                                                Pointer to information to define
                                                the optional secondary faces
                                                for the bead.
                                                */
UF_MODL_bead_section_plane_p_t section_plane ,/* <I>
                                              Pointer to direction information
                                              to define the normal of the
                                              orientation plane of the bead
                                              sections.
                                              */
UF_MODL_vector_p_t section_axis ,/* <I>
                                 Pointer to direction information to define the
                                 centerline of the bead cross section.
                                 */
UF_MODL_bead_section_parms_p_t section_parms  /* <I>
                                              Pointer to information to define
                                              the cross sectional shape of the
                                              bead.
                                              */
);


/****************************************************************************
Creates a flange feature.  The output of the routine is the object
identifier of the flange.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_flange(
double orig[3] ,/* <I>
                Default origin of flange.
                */
double xdir[3] ,/* <I>
                X-direction of flange (across bend.)
                */
double zdir[3] ,/* <I>
                Z-direction, normal to the face.
                */
tag_t face ,/* <I>
            Face to which the flange should attach.
            */
tag_t edge ,/* <I>
            Horizontal edge.
            */
char * thick ,/* <I>
              Thickness expression string (if null, infer from face)
              */
char * width ,/* <I>
              Width expression string (if null, infer from edge)
              */
char * angle ,/* <I>
              Bend angle expression string
              */
char * length ,/* <I>
               Tangent length expression string
               */
char * radius ,/* <I>
               Inside radius of the bend
               */
char * taper_l ,/* <I>
                Left taper of flange
                */
char * taper_r ,/* <I>
                Right taper of flange
                */
int ang_tgl ,/* <I>
             Bend/Include angle switch
             */
int len_tgl ,/* <I>
             Tangent/Contour length switch
             */
int rad_tgl ,/* <I>
             Inside/Outside radius switch
             */
tag_t * flange  /* <O>
                Object identifier for the flange feature.
                */
);

/*****************************************************************************
Generates a Sheet Metal Design inset flange feature.  It provides the
ability to create the feature along the complete extent of the
attachment face or partially with reliefs automatically added during
construction.


Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_inset_flange (
tag_t attach_face ,/* <I>
                   Attachment face of target body.
                   */
tag_t reference_edge ,/* <I>
                      Horizontal edge reference of target
                      body.
                      */
double  position[3] ,/* <I>
                   Default origin of inset flange
                   feature.
                   */
double  xdirection[3] ,/* <I>
                     Direction of inset flange along the
                     width of the bend.
                     */
double  zdirection[3] ,/* <I>
                     Normal of attachment/link face.
                     */
UF_MODL_inset_flange_data_p_t parameters ,/* <I>
                                          Structure which defines the size and
                                          shape of the inset flange feature.
                                          */
tag_p_t feature_tag  /* <O>
                     Object identifier of the inset flange
                     feature.
                     */
);

/*****************************************************************************
Modifies the size and shape of a Sheet Metal Design inset flange
feature. By populating the set of parameters with similar and/or
updated values, the feature can be altered.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_inset_flange (
tag_t feature_tag ,/* <I>
                   Object identifier of flange feature.
                   */
UF_MODL_inset_flange_data_p_t parameters  /* <I>
                                          Modified set of parameters which
                                          represent the new  size and shape of
                                          the feature.
                                          */
);

/*****************************************************************************
Returns the parameters of an existing straight-brake inset flange
feature. Returns the thickness, width, angle, length, radius, and the
independent taper angles for the left and right side of the feature,
along with the inset distance and left and right reliefs for the feature.
The memory for the structure is allocated by the routine and must be
freed by the caller of the routine.

Environment: Internal  and  External
See Also:
History: Original release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_inset_flange_parms (
tag_t feature_tag ,/* <I>
                   Object identifier of an existing
                   straight-brake inset flange
                   feature.
                   */
UF_MODL_inset_flange_data_p_t * parameters  /* <OF>
                                            The parameters associated with
                                            the existing straight-brake inset
                                            flange feature. Use UF_free to
                                            deallocate memory.
                                            NEEDS FREE ROUTINE
                                            */
);

/*****************************************************************************
Generates a Sheet Metal Design flange feature. It differs from the
existing UF_MODL_create_flange in that it provides the ability to
independently taper the bend and web areas of the feature and you
can create Miter and Butt joints also. Negative bend angle is no more
allowed as a way to change the bend direction of the Flange. Parameter
'reverse_direction' of structure UF_MODL_flange_data_t should be used to
change the direction of the Flange.


Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smd_flange (
tag_t attach_face ,/* <I>
                   Attachment face of target body.
                   */
tag_t reference_edge ,/* <I>
                      Horizontal edge reference of target body. This should
                      lie on the attachment face of the Flange, else an error
                      will be returned.
                      */
double  position[3] ,/* <I>
                   NOT USED. Origin of flange feature will be found
                   automatically.
                   */
double xdirection[3] ,/* <I>
                     NOT USED. Direction of flange along the width of the
                     bend will be derived automatically.
                     */
double zdirection[3] ,/* <I>
                     NOT USED. Normal of attachment/link face will be found
                     automatically.
                     */
UF_MODL_flange_data_p_t flange_data ,/* <I>
                                     Structure which defines the size and shape
                                     of the flange feature. This is expanded to
                                     include the parameters for Miter and Butt
                                     joints also.
                                     */
tag_p_t feature_tag  /* <O>
                     Object identifier of the flange feature.
                     */
);

/*****************************************************************************
Modifies the size and shape of a Sheet Metal Design flange feature.
The caller should use UF_MODL_ask_flange_parms to get the current parameters
and by changing the required parameters, the feature can be altered.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_smd_flange (
tag_t feature_tag ,/* <I>
                   Object identifier of flange feature.
                   */
UF_MODL_flange_data_p_t parameters  /* <I>
                                    Modified set of parameters which
                                    represent the new  size and shape of the
                                    feature.
                                    */
);

/*****************************************************************************
Returns the parameters of an existing straight-brake flange feature.
The structure returns the thickness, width, angle, length, radius and
the taper/miter/butt for the left and right side of the feature.
The memory for the structure is allocated by the routine and must be
freed by the caller of the routine.

Environment: Internal  and  External
See Also:
History: Original release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_flange_parms (
tag_t feature_tag ,/* <I>
                   Object identifier of an existing
                   straight-brake flange feature.
                   */
UF_MODL_flange_data_p_t * parameters  /* <OF>
                                      The parameters associated with the
                                      existing straight-brake flange feature.
                                      Use UF_free to deallocate memory
                                      when done.
                                      NEEDS FREE ROUTINE
                                      */
);

/*****************************************************************************
Inquires the current process factor.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_flange_proc_factor(
tag_t flange ,/* <I>
              Object identifier for the flange feature.
              */
double * proc_factor  /* <O>
                      Process factor
                      */
);

/*****************************************************************************
Sets the process factor for a specified flange feature.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_set_flange_proc_factor(
tag_t flange ,/* <I>
              Object identifier for the flange feature.
              */
double proc_factor  /* <I>
                    Process factor
                    */
);

/******************************************************************************
Creates a general flange from its target face, bend radius, bend angle,
and web length. Along with these items an optional spine, thickness,
tolerance string, bend direction, and step data can be set. The output
is the object identifier associated to the general flange.

Environment: Internal  and  External
See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_general_flange(
tag_t  target_face ,/* <I>
                    Attachment face for the generalized flange.  The
                    flange is constrained to be tangent to this face
                    along the bend edge.
                    */
UF_STRING_p_t bend_edge_string ,/* <I>
                                An edge in the tangent face, used as the
                                attachment edge the generalized flange.
                                */
UF_STRING_p_t spine_string ,/* <I>
                            An edge or curve used to define the section
                            planes for the bend and web.  If this values is
                            null, the bend edge string is used as the spine
                            string.
                            */
UF_STRING_p_t section_curves ,/* <I>
                              Two or more section curves used as an alternate
                              method for creating a general flange.  The curves
                              must start tangent to the target face, be C0 with
                              the bend edge, be coplanar, end to end and be
                              made up of alternating lines and arcs.  If this
                              parameter is used, the plus, bend_radius,
                              bend_angle and web_length is ignored.
                              */
int step_count ,/* <I>
                The number of steps in the generalized flange.
                Zero is an invalid number.  For each step include
                a value for the bend radius, bend angle and web.
                */
int poly_cubic    ,/* <I>
                   =0 Use Rational Exact B-splines curves
                   represented by exact conics.
                   =1 Use Polynomial approximate to produce a
                   surface with better parameterization.  This does
                   not produce exact conics.
                   */
int reverse_normal ,/* <I>
                    =0 Use the tangent face normal at the center of
                    the bend edge to determine the direction of the flange.
                    =1 Use the reverse of the tangent face normal at
                    the center of the bend edge to determine the
                    direction of the flange.
                    */
int reverse_thicken ,/* <I>
                     =0 If Body type is solid, thicken the plus bend
                     and web along the direction of the bend.
                     =1 If Body type is solid, thicken the plus bend
                     and web opposite to the direction of the bend.
                     */
char * thickness_str ,/* <I>
                      Thickness of the solid body created if the
                      Modeling preference for body type is set to solid.
                      */
char * tolerance_str ,/* <I>
                      This is initially set from the the modeling
                      distance tolerance.  This value has the same
                      effect as the modeling distance tolerance.
                      */
UF_MODL_parm_p_t plus ,/* <I>
                       The law specification of the target face extension
                       between the bend edge and the start of the bend.
                       */
UF_MODL_parm_t bend_radius[] ,/* <I>
                              The law specification of the radius of the bend.
                              */
UF_MODL_parm_t bend_angle[] ,/* <I>
                             The law specification of the angle of the bend.
                             */
UF_MODL_parm_t web_length[] ,/* <I>
                             The law specification of the length of the surface
                             extension after the bend.
                             */
tag_p_t general_flange_tag  /* <O>
                            Pointer to Feature object identifier of created
                            flange
                            */
);

/******************************************************************************
Retrieves the parameters used to create a general flange.

Environment: Internal  and  External
See Also:
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_general_flange(
tag_t  general_flange_tag ,/* <I>
                           Attachment face for the generalized flange.  The
                           flange is constrained to be tangent to this face
                           along the bend edge.
                           */
UF_STRING_p_t bend_edge_string ,/* <O>
                                An edge in the tangent face, used as the
                                attachment edge the generalized flange.
                                */
UF_STRING_p_t spine_string ,/* <O>
                            An edge or curve used to define the section
                            planes for the bend and web.  If this value is null,
                            the bend edge string is used as the spine string.
                            */
int *step_count ,/* <O>
                 The number of steps in the generalized flange.
                 Zero is an invalid number.  For each step include
                 a value for the bend radius, bend angle and web.
                 */
int *poly_cubic ,/* <O>
                 =0 Use Rational Exact B-splines curves represented by exact
                 conics.
                 =1 Use Polynomial approximate to produce a surface with better
                 parameterization.  This does not produce exact conics.
                 */
int *reverse_normal ,/* <O>
                     =0 Use the tangent face normal at the center of
                     the bend edge to determine the direction of the flange.
                     =1 Use the reverse of the tangent face normal at the center
                     of the bend edge to determine the direction of the flange.
                     */
int *reverse_thicken ,/* <O>
                      =0 If Body type is solid, thicken the plus bend
                      and web along the direction of the bend.
                      =1 If Body type is solid, thicken the plus bend
                      and web opposite to the direction of the bend.
                      */
char thickness_str[ UF_MAX_EXP_BUFSIZE ] ,/* <O>
                      Thickness of the solid body created if the
                      Modeling preference for body type is set to solid.  The
                      calling program must pass in a character array large
                      enough to hold the thickness string.
                      */
char tolerance_str[ UF_MAX_EXP_BUFSIZE ] ,/* <O>
                      This is initially set from the the modeling
                      distance tolerance.  This value has the same
                      effect as the modeling distance tolerance.  The calling
                      program must pass in a character array large enough to
                      hold the tolerance string.
                      */
UF_MODL_parm_p_t plus ,/* <O>
                       The law specification of the target face extension
                       between the bend edge and the start of the bend.
                       */
UF_MODL_parm_t bend_radius[] ,/* <O>
                              The law specification of the radius of the bend.
                              There will be one value in this array for each
                              step in the flange.  The caller is responsible
                              for allocating an array large enough to handle
                              the number of steps.
                              */
UF_MODL_parm_t bend_angle[] ,/* <O>
                             The law specification of the angle of the bend.
                             There will be one value in this array for each
                             step in the flange.  The caller is responsible
                             for allocating an array large enough to handle
                             the number of steps.
                             */
UF_MODL_parm_t web_length[]  /* <O>
                             The law specification of the length of the surface
                             extension after the bend.  There will be one value
                             in this array for each step in the flange.  The
                             caller is responsible for allocating an array
                             large enough to handle the number of steps.
                             */
);

/******************************************************************************
Modifies the size and shape of a Sheet Metal Design general flange
feature.  By populating the set of parameters with similar and/or
updated values, the feature can be altered.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_general_flange (
tag_t feature_tag ,/* <I>
                   Object identifier of general flange feature.
                   */
tag_t tangent_face_tag ,/* <I>
                        Object identifier of the face which the feature will
                        maintain a tangency relationship.
                        */
UF_STRING_p_t bend_string ,/* <I>
                           Collection of objects which represent the location of
                           the initial bend area.
                           */
UF_STRING_p_t spine_string ,/* <I>
                            Collection of objects which represent the spine
                            associated witth the feature.
                            */
UF_STRING_p_t section_string ,/* <I>
                              Collection of objects which represent a set of
                              curves/edges to infer the size/shape of the
                              feature.
                              */
int nsteps ,/* <I>
            The number of bend area/web extensions which
            define the size/shape of the feature.
            */
int poly_cubic ,/* <I>
                The method for generation of the surface geometry
                associated with the feature.
                0=Rational (exact)
                1=Polynomial (approximate)
                */
int reverse_normal ,/* <I>
                    Whether or not the direction of the normal has
                    been reversed.
                    0=Do not reverse normal direction.
                    1=Reverse normal direction.
                    */
int reverse_thicken ,/* <I>
                     Whether or not the direction in which the tool body
                     is to be thickened has been reversed.
                     0=Do not reverse thickening direction.
                     1=Reverse thickening direction.
                     */
char * thickness ,/* <I>
                  Character string used to define the thickness of the
                  feature.
                  */
char * tolerance ,/* <I>
                  Character string used to define the tolerance of the
                  feature.
                  */
UF_MODL_parm_p_t plus_length ,/* <I>
                              A law controlled value which determines the length
                              of the extension associated with the tangent_face.
                              */
UF_MODL_parm_t bend_radius[] ,/* <I>
                              A law controlled value which determines the radius
                              of each bend area of the feature.
                              */
UF_MODL_parm_t bend_angle[] ,/* <I>
                             A law controlled value which determines the angle
                             of each bend area associated with the feature.
                             */
UF_MODL_parm_t web_length[]  /* <I>
                             A law controlled value which determines the length
                             of each web associated with the feature.
                             */
);

/******************************************************************************
Creates a sheet metal bracket (SMBRACKET).

Environment: Internal  and  External
See Also:

History:Original release was in V16.0
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smbracket (
UF_MODL_smbracket_data_p_t user_data,  /* <I>
                                       smbracket Open API Data
                                       Structure
                                              */
tag_t      *bracket_body_tag           /* <I/O>
                                       If set to NULL_TAG, tag of the created
                                       bracket body is returned.
                                       If set to tag of the target body,
                                       bracket is created and united with the
                                       target body. It returns the tag of the
                                       target body.
                                              */
);

/******************************************************************************
Creates a sheet metal relief (SMRELIEF).

Environment: Internal  and  External
See Also:

History:Original release was in V16.0
 *****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smrelief (
UF_MODL_smrelief_data_p_t user_data          /* <I>
                                              smrelief Open API Data
                                              Structure
                                              */
);

/* *************************************************************************
Creates a Sheet Metal Joggle from input joggle data structure.
Environment  : Internal  and  External
See Also:

History:Original release was in V16.0
 *****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smjoggle
(
    UF_MODL_smjoggle_data_p_t joggle_data, /* <I> Joggle data structure   */
    tag_t                     *joggle      /* <O> Tag of the body created */
);


/******************************************************************************
Creates a generalized flange.

Environment: Internal  and  External

See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_gflange(
    UF_MODL_gflange_data_p_t gflange_data,    /* <I>    Data struct
                                              */
    tag_p_t gflange_tag                       /* <O>    Genflg tag
                                              */
);

/****************************************************************************
 *           Retrieves the parameters of general flange used to create a
 *           general flange.
 *
 * Return :
 *   Return code:
 *            = 0 No Error
 *            = not  0 Error code
 *
 * Environment: Internal and External
 * See Also:
 * History:
 ****************************************************************************/

extern  UFUNEXPORT int UF_MODL_ask_gflange(
tag_t                    gflange_tag,        /* <I>
                                                general flange tag
                                             */

UF_MODL_gflange_data_p_t *gflange_data       /* <OF,free:UF_MODL_free_gflange_data>
                                                general flange data structure.
                                                This should be freed by calling
                                                UF_MODL_free_gflange_data.
                                           */
);
/***************************************************************************
 *         Frees the memory allocated to general flange data structure
 *         This function is called after the UF_MODL_ask_gflange routine to
 *         free memory allocated to members of gflange_data structure.
 *
 * Return:
 *  Return code:
 *           = 0  No Error
 *           = not 0  Error code
 *
 * Environment: Internal and External
 * See Also:
 * History :
 ***************************************************************************/

extern  UFUNEXPORT int UF_MODL_free_gflange_data(

UF_MODL_gflange_data_p_t gflange_data       /* <I>
                                               general flange data structure
                                            */
);/* <NON_NXOPEN> */

/*************************************************************************
 * Change an existing General Flange feature's parameters to
 * the parameters given in user_data.  The caller should first call
 * UF_MODL_ask_gflange to get the current parameters for the general flange,
 * then change the elements that need to be changed, and then call
 * UF_MODL_edit_gflange
 *
 * Return:
 *   Return code:
 *        = 0  No error
 *        = not 0 Error code
 * Environment  : Internal and External
 * See Also:
 * History:
 ***************************************************************************/
extern  UFUNEXPORT int UF_MODL_edit_gflange(
tag_t                    gflange_tag,      /* <I>
                                              general flange tag
                                           */
UF_MODL_gflange_data_p_t gflange_data      /* <I>
                                              general flange data
                                            */
);

/*****************************************************************************
Creates a smbend feature.

Environment: Internal and External

Return:
    Return code:
        = 0  No error
        = not 0 Error code
See Also:
History: Originally released in V17.0
*****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smbend
(
    UF_MODL_smbend_data_p_t    user_data,  /* <I>
                                              Data supplied by the user
                                              to define the feature
                                           */
    tag_p_t                    bend_tag    /* <O>
                                              the tag of the new bend
                                              feature that was created
                                           */
);

/*****************************************************************************
Edits an existing smbend feature.

Environment: Internal and External

Return:
    Return code:
        = 0  No error
        = not 0 Error code
See Also:
History: Originally released in V17.0
*****************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_smbend
(
    tag_t                      bend_tag,    /* <I>
                                               tag of the bend
                                               feature to be edited
                                            */
    UF_MODL_smbend_data_p_t    user_data    /* <I>
                                               new user data for
                                               the bend
                                            */
);

/*****************************************************************************
Queries an existing smbend feature.

Environment: Internal and External

Return:
    Return code:
        = 0  No error
        = not 0 Error code
See Also:
History: Originally released in V17.0
*****************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_smbend
(
    tag_t                      bend_tag,    /* <I>
                                               tag of the bend
                                               feature in question
                                            */
    UF_MODL_smbend_data_p_t    user_data    /* <O>
                                               data which represents
                                               this feature
                                            */
);

/***************************************************************************
* This procedure uses data from the user to create a new smbend feature
* from a converted corner.
*
* Return:
*     Return code:
*     = 0 No Error
*     = not 0 Error code
*
* Environment: External
* See Also:
* History: Originally released in V17.0.3
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smbend_corner
(
    UF_MODL_smbend_corner_data_p_t user_data,  /* <I>
                                              UF data supplied by user
                                              to define the feature
                                           */
    tag_p_t                    bend_tag    /* <O>
                                              the tag of the new bend
                                              feature that was created
                                           */
);

/***************************************************************************
* This procedure uses data from the user to edit an existing smbend feature
* that was created by converting a corner.
*
* Return:
*     Return code:
*     = 0 No Error
*     = not 0 Error code
*
* Environment: External
* See Also:
* History: Originally released in V17.0.3
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_smbend_corner
           (
               tag_t                      bend_tag,  /* <I>
                                                        tag of the bend
                                                        feature to be edited
                                                     */
               UF_MODL_smbend_corner_data_p_t user_data  /* <I>
                                                        new user data for
                                                        the bend
                                                     */
);

/***************************************************************************
* This procedure uses a tag for an smbend feature that was created by
* converting a corner, it then outputs the user's parameters for that bend
* feature.
*
* Return:
*     Return code:
*     = 0 No Error
*     = not 0 Error code
*
* Environment: External
* See Also:
* History: Originally released in V17.0.3
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_smbend_corner
           (
               tag_t                      bend_tag,    /* <I>
                                                          the tag of the bend
                                                          feature in question
                                                       */
               UF_MODL_smbend_corner_data_p_t    user_data    /* <O>
                                                          UF data which represents
                                                          this feature
                                                       */
);

/***************************************************************************
* This procedure uses data from the user to create a new smbend feature
* from a converted cylindrical face.
*
* Return:
*     Return code:
*     = 0 No Error
*     = not 0 Error code
*
* Environment: External
* See Also:
* History: Originally released in V17.0.3
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_smbend_cylinder
(
    UF_MODL_smbend_cylinder_data_p_t user_data,  /* <I>
                                              UF data supplied by user
                                              to define the feature
                                           */
    tag_p_t                    bend_tag    /* <O>
                                              the tag of the new bend
                                              feature that was created
                                           */
);

/***************************************************************************
* This procedure uses data from the user to edit an existing smbend feature
* that was created by converting a cylindrical face.
*
* Return:
*     Return code:
*     = 0 No Error
*     = not 0 Error code
*
* Environment: External
* See Also:
* History: Originally released in V17.0.3
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_smbend_cylinder
           (
               tag_t                      bend_tag,  /* <I>
                                                        tag of the bend
                                                        feature to be edited
                                                     */
               UF_MODL_smbend_cylinder_data_p_t user_data  /* <I>
                                                        new user data for
                                                        the bend
                                                     */
);

/***************************************************************************
* This procedure uses a tag for an smbend feature that was created by
* converting a cylindrical face, it then outputs the user's parameters for
* that bend feature.
*
* Return:
*     Return code:
*     = 0 No Error
*     = not 0 Error code
*
* Environment: External
* See Also:
* History: Originally released in V17.0.3
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_smbend_cylinder
           (
               tag_t                      bend_tag,    /* <I>
                                                          the tag of the bend
                                                          feature in question
                                                       */
               UF_MODL_smbend_cylinder_data_p_t    user_data    /* <O>
                                                          UF data which represents
                                                          this feature
                                                       */
);

enum UF_MODL_err_feature_e
{
    UF_MODL_ERR_NOT_A_FORMABLE_FEATURE = 1,
    UF_MODL_ERR_FEATURE_NOT_USING_BAF,
    UF_MODL_ERR_NOT_A_SUPPORTED_FEATURE,
    UF_N_ERR_FEATURE_OPTS
};

/******************************************************************************
 This routine asks for the Bend Allowance Formula (BAF) of a
 Flange, Inset Flange, General Flange, SMBridge, or SMBend feature.
 The expression returned is in the form:

        (Radius+(Thickness)*0.44)*rad(Angle)

 Return:
        Return code:
        =0                                      : Successful
        >0                                      : Failing error number
        <0                                      : Failing error number
        = UF_MODL_ERR_NOT_A_FORMABLE_FEATURE    : The given tag was not
                                                  the tag of a formable
                                                  feature.
        = UF_MODL_ERR_FEATURE_NOT_USING_BAF     : The given feature is not
                                                  using a bend allowance
                                                  formula. This is the case
                                                  when the user has selected
                                                  "Using Bend Allowance Table"
                                                  in the preferences dialog.

 Environment: Internal and External
 See also:  UF_MODL_edit_bend_allowance_formula
 History: Originally released in V18.0
 *******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_bend_allowance_formula
(
        const tag_t feature_tag,                /* <I>
                                                   The tag of a Flange, Inset Flange,
                                                   General Flange, SMBridge, or
                                                   SMBend feature.
                                                */
        char    **exp_str                       /* <OF>
                                                   The Bend Allowance Formula.
                                                   This must be freed using
                                                   UF_free.
                                                */
);

/******************************************************************************
 This routine edits the Bend Allowance Formula (BAF) of a
 Flange, Inset Flange, General Flange, SMBridge, or SMBend feature.
 The expression returned is in the form:

        (Radius+(Thickness)*0.44)*rad(Angle)

 Return:
        Return code:
        =0                                      : Successful
        >0                                      : Failing error number
        <0                                      : Failing error number
        = UF_MODL_ERR_NOT_A_FORMABLE_FEATURE    : The given tag was not
                                                  the tag of a formable
                                                  feature.
        = UF_MODL_ERR_FEATURE_NOT_USING_BAF     : The given feature is not
                                                  using a bend allowance
                                                  formula. This is the case
                                                  when the user has selected
                                                  "Using Bend Allowance Table"
                                                  in the preferences dialog.

 Environment: Internal and External
 See also:  UF_MODL_ask_bend_allowance_formula
 History: Originally released in V18.0
 *******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_bend_allowance_formula
(
        const tag_t     feature_tag,    /* <I>
                                           The tag of a Flange, Inset Flange,
                                           General      Flange, SMBridge, or
                                           SMBend feature.
                                        */
        const char* const exp_str       /* <I>
                                           The Bend Allowance Formula.
                                        */
);

/******************************************************************************
 This routine will set the state of an array of formable features
 so that the features will be fully formed.
 The given feaure tags must be tags of Flange, Inset Flange,
 General Flange, SMBridge, or SMBend feature.

 The caller of this routine may start an update cycle (if any of the features
 are not already in their fully formed state) by using UF_MODL_update.

 Return:
        Return code:
        =0                                      : Successful
        >0                                      : Failing error number
        <0                                      : Failing error number
        = UF_MODL_ERR_NOT_A_FORMABLE_FEATURE    : The given tag was not
                                                  the tag of a formable
                                                  feature.

 Environment: Internal and External
 See also:  UF_MODL_unform_features
 History: Originally released in V18.0
 *******************************************************************************/
extern UFUNEXPORT int UF_MODL_form_features
(
        const int       n_features,             /* <I>
                                                   The number of features tags
                                                   in the array.
                                                */
        const tag_t *const feature_tag_array,   /* <I,len:n_features>
                                                   The array of formable feature
                                                   tags.
                                                */
        logical *const is_update_required       /* <O>
                                                   If update is required.
                                                */

);

/******************************************************************************
 This routine will set the state of an array of formable features
 so that the features will be fully unformed.
 The given feaure tags must be tags of Flange, Inset Flange,
 General Flange, SMBridge, or SMBend feature.

 The caller of this routine may start an update cycle (if any of the features
 are not already in their fully unformed state) by using UF_MODL_update.

 Return:
        Return code:
        =0                                      : Successful
        >0                                      : Failing error number
        <0                                      : Failing error number
        = UF_MODL_ERR_NOT_A_FORMABLE_FEATURE    : The given tag was not
                                                  the tag of a formable
                                                  feature.

 Environment: Internal and External
 See also:  UF_MODL_form_features
 History: Originally released in V18.0
 *******************************************************************************/
extern UFUNEXPORT int UF_MODL_unform_features
(
        const int       n_features,             /* <I>
                                                   The number of features tags
                                                   in the array.
                                                */
        const tag_t *const feature_tag_array,   /* <I,len:n_features>
                                                   The array of formable feature
                                                   tags.
                                                */
        logical *const is_update_required       /* <O>
                                                   If update is required.
                                                */
);


struct UF_MODL_state_info_s
{
        double process_factor; /* The process factor of a
                                  Flange or Inset Flange feature.
                                */
        int    state_index;     /* The current state index of
                                  a General Flange or SMBridge
                                  feature. Future enhancement.
                                  Currently, this is always
                                  set to zero.
                                */

};
typedef struct UF_MODL_state_info_s UF_MODL_state_info_t,
                                   *UF_MODL_state_info_p_t;
enum UF_MODL_state_e
{
    UF_MODL_unformed_state = 0,
    UF_MODL_formed_state,
    UF_MODL_other_state,
    UF_N_STATE_OPTS
};
typedef enum UF_MODL_state_e UF_MODL_state_e_t;


/******************************************************************************
 This routine will return the current state of the given feature.
 The given feature tag must be the tag Flange, Inset Flange,
 General Flange, SMBridge, or SMBend feature.

 The state returned will be either UF_MODL_formed_state,
 UF_MODL_unformed_state, or UF_MODL_other_state.

 When UF_MODL_other_state is returned and a non-NULL pointer to a
 UF_MODL_state_info structure is given, this structure will be filled
 with the current intermediate state of the feature.

 The UF_MODL_state_info structure will hold a Process Factor if the
 feature tag belongs to a Flange, Inset Flange feature. The Process
 Factor can be thought of as a percentage of the design angle of the
 feature. For example, a Process Factor of 1.0 represents a fully
 Flange. A Process Factor of 0.0 represents a fully unformed
 Flange. A Process Factor of 0.5 represents a Flange in an intermediate
 state that is half-formed.

 The UF_MODL_state_info structure will hold a State Index if the feature
 tag belongs to a General Flange or SMBridge. The State Index
 represents an index into the array of states stored by the General
 Flange or SMBridge feature. Note: this value is currently not used.

 If the given_feature is an SMBend, no state information other than
 UF_MODL_formed_state or UF_MODL_unfromed_state will be returned.

 Return:
        Return code:
        =0                                      : Successful
        >0                                      : Failing error number
        <0                                      : Failing error number
        = UF_MODL_ERR_NOT_A_FORMABLE_FEATURE    : The given tag was not
                                                  the tag of a formable
                                                  feature.
        = UF_MODL_ERR_NOT_A_SUPPORTED_FEATURE   : A given tag belongs to a
                                                  formable feature that is
                                                  not yet supported.

 Environment: Internal and External
 See also:  UF_MODL_edit_formable_feature_state
 History: Originally released in V18.0
 *******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_formable_feature_state
(
        const tag_t     feature_tag,            /* <I>
                                                   The tag of a Flange, Inset
                                                   Flange, General Flange,
                                                   SMBridge, or SMBend feature.
                                                */
        UF_MODL_state_e_t *const state,         /* <O>
                                                   The current state of an
                                                   SMBend feature: either
                                                   UF_MODL_formed_state,
                                                   UF_MODL_unformed_state or
                                                   UF_MODL_other_state.
                                                */
        UF_MODL_state_info_t *const state_info  /* <O> Optional.
                                                   If a non-NULL pointer to a
                                                   UF_MODL_state_info_t structure
                                                   is given here, it will be filled
                                                   with the state information of
                                                   the feature.
                                                 */
);

/******************************************************************************
 This routine will set the state of the given feature.
 The given feature tag must be the tag Flange, Inset Flange,
 General Flange, SMBridge, or SMBend feature.

 The state you want to set must be either UF_MODL_formed_state,
 UF_MODL_unformed_state, or UF_MODL_other_state.

 When UF_MODL_other_state is given and the UF_MODL_state_info structure
 must be filled with the intermediate state to which you want to set
 the feature.

 The UF_MODL_state_info structure must hold a Process Factor if the
 feature tag belongs to a Flange, Inset Flange feature. The Process
 Factor can be thought of as a percentage of the design angle of the
 feature. For example, a Process Factor of 1.0 represents a fully
 Flange. A Process Factor of 0.0 represents a fully unformed
 Flange. A Process Factor of 0.5 represents a Flange in an intermediate
 state that is half-formed.

 The UF_MODL_state_info structure must hold a State Index if the feature
 tag belongs to a General Flange or SMBridge. The State Index
 represents an index into the array of states stored by the General
 Flange or SMBridge feature. Note: this value is currently not used.

 If the given_feature is an SMBend, no state information other than
 UF_MODL_formed_state or UF_MODL_unfromed_state can be given.

 Return:
        Return code:
        =0                                      : Successful
        >0                                      : Failing error number
        <0                                      : Failing error number
        = UF_MODL_ERR_NOT_A_FORMABLE_FEATURE    : The given tag was not
                                                  the tag of a formable
                                                  feature.
        = UF_MODL_ERR_NOT_A_SUPPORTED_FEATURE   : A given tag belongs to a
                                                  formable feature that is
                                                  not yet supported.

 Environment: Internal and External
 See also:  UF_MODL_ask_formable_feature_state
 History: Originally released in V18.0
 *******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_formable_feature_state
(
   const tag_t  feature_tag,                    /* <I>
                                                   The tag of a Flange, Inset
                                                   Flange, General Flange,
                                                   SMBridge, or SMBend feature.
                                                */
   const UF_MODL_state_e_t state,               /* <I>
                                                   The current state of an
                                                   SM feature: either
                                                   UF_MODL_formed_state,
                                                   UF_MODL_unformed_state or
                                                   UF_MODL_other_state.
                                                */
   const UF_MODL_state_info_t* const state_info /* <I>
                                                   It will be filled
                                                   with the state information of
                                                   the feature.
                                                */
);

/***************************************************************************
 *
 * Create an Unbend/Rebend operation
 *
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_create_bend_operation
(
    UF_MODL_bend_operation_data_p_t bend_data,    /* <I>
                                                     Data supplied by the user
                                                     to define the operation
                                                  */
    tag_p_t                         operation_tag /* <O>
                                                     The operation tag
                                                  */
);

/***************************************************************************
 *
 * Edit an Unbend/Rebend operation
 *
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_edit_bend_operation
(
    tag_t                           operation_tag,/* <I>
                                                     The operation tag
                                                  */
    UF_MODL_bend_operation_data_p_t bend_data     /* <I>
                                                     Data supplied by the user
                                                     to edit the operation
                                                  */
);

/***************************************************************************
 *
 * Ask an Unbend/Rebend operation
 *
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in V19.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_ask_bend_operation
(
    tag_t                           operation_tag,/* <I>
                                                     The operation tag
                                                  */
    UF_MODL_bend_operation_data_p_t bend_data     /* <O>
                                                     The operation data
                                                  */
);

/***************************************************************************
 *
 * Create a Solid Punch feature.
 *
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_create_solid_punch
(
    UF_MODL_solid_punch_data_p_t smspunch_ufdata, /* <I> Data supplied by the
                                                         user to create the
                                                         solid punch feature */
    tag_t                        *smspunch_tag    /* <O> The solid punch tag */
);

/***************************************************************************
 *
 * Edit solid punch
 *
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_edit_solid_punch
(
    tag_t                        smspunch_tag,   /* <I> The solidpunch tag */
    UF_MODL_solid_punch_data_p_t smspunch_ufdata /* <I> Data supplied by the
                                                        user to edit the
                                                        solid punch feature */
);

/***************************************************************************
 *
 * Ask an Solid Punch tag
 *
 * Return :
 *           Return code :
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX2.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_ask_solid_punch
(
    tag_t                        smspunch_tag,    /* <I>  The solid punch tag */
    UF_MODL_solid_punch_data_p_t smspunch_ufdata  /* <OF> The solidpunch data */
);

/***************************************************************************
 *
 * Create a SMCorner feature.
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_create_smcorner
(
    UF_MODL_smcorner_data_p_t smcorner_ufdata, /* <I> Data supplied by the
                                                      user to create the
                                                      smcorner feature */
    tag_t                        *smcorner_tag    /* <O> The smcorner tag */
);

/***************************************************************************
 *
 * Edit smcorner
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_edit_smcorner
(
    tag_t                        smcorner_tag,   /* <I> The smcorner tag */
    UF_MODL_smcorner_data_p_t    smcorner_ufdata /* <I> Data supplied by the
                                                        user to edit the
                                                        smcorner feature */
);

/***************************************************************************
 *
 * Ask an SMCorner tag
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_ask_smcorner
(
    tag_t                     smcorner_tag,    /* <I>  The smcorner tag */
    UF_MODL_smcorner_data_p_t smcorner_ufdata  /* <O> The smcorner data */
);

/***************************************************************************
 *
 * Initialize the SMCorner UF data. This will load the default values for
 * creation of SMCorner feature.
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 ********************************************************************** */
extern UFUNEXPORT void UF_MODL_init_smcorner_ufdata
(
    UF_MODL_smcorner_data_p_t smcorner_ufdata  /* <I/O> SMCorner UF data */
);

/***************************************************************************
 *
 * Create a Edge Rip feature.
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_create_ripedge
(
    UF_MODL_ripedge_data_p_t ripedge_ufdata, /* <I> Data supplied by the
                                                      user to create the
                                                      ripedge feature */
    tag_t                        *ripedge_tag    /* <O> The ripedge tag */
);

/***************************************************************************
 *
 * Edit Edge Rip
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 ********************************************************************** */
extern UFUNEXPORT int UF_MODL_edit_ripedge
(
    tag_t                        ripedge_tag,   /* <I> The ripedge tag */
    UF_MODL_ripedge_data_p_t    ripedge_ufdata /* <I> Data supplied by the
                                                        user to edit the
                                                        ripedge feature */
);

/***************************************************************************
 *
 * Ask an Rip Edge tag
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 ***********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_ripedge
(
    tag_t                     ripedge_tag,    /* <I>  The ripedge tag */
    UF_MODL_ripedge_data_p_t ripedge_ufdata   /* <OF> The ripedge data */
);



/***************************************************************************
 *
 * Initialize the Edge Rip UF data. This will load the default values for
 * creation of Edge Rip feature.
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 ********************************************************************** */
extern UFUNEXPORT void UF_MODL_init_ripedge_ufdata
(
    UF_MODL_ripedge_data_p_t ripedge_ufdata  /* <I/O> Edge Rip UF data */
);

/**************************************************************************
 *  UF_MODL_genflg_create_state
 *
 *  Create a new state in the genflg feature.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_MODL_genflg_create_state
(
    tag_t                         genflg,      /* <I> Genflg frec tag      */
    UF_MODL_genflg_state_data_p_t state,       /* <I> State data structure */
    int*                          state_index  /* <O> created state index  */
);

/**************************************************************************
 *  UF_MODL_genflg_ask_num_states
 *
 *  Returns the number of states in a given feature.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_MODL_genflg_ask_num_states
(
    tag_t    genflg,      /* <I> Genflg frec      */
    int      *num_states  /* <O> number of states */
);

/**************************************************************************
 *  UF_MODL_genflg_edit_state
 *
 *  Edit the state of given general flange feature.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_MODL_genflg_edit_state
(
    tag_t                genflg,      /* <I> Genflg frec to create new state */
    int                  state_index, /* <I> state index to be edited   */
    UF_MODL_genflg_state_data_p_t   state   /* <I> state info to be edited */
);

/**************************************************************************
 *  UF_MODL_genflg_ask_state_data
 *
 *  Gives the state info data for a given state index.
 *
 *
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_MODL_genflg_ask_state_data
(
    tag_t                genflg,      /* <I> Genflg frec to create new state */
    int                  state_index, /* <I> State to be inquired            */
    UF_MODL_genflg_state_data_p_t  state        /* <O> state info */
);

/**************************************************************************
 *  UF_MODL_genflg_delete_state
 *
 *  Deletes the state for a given state index.
 *
 * Environment: Internal  and  External
 *
 * See Also:
 * History: Released in NX3.0
 **************************************************************************/
extern UFUNEXPORT int UF_MODL_genflg_delete_state
(
    tag_t                genflg,     /* <I> Genflg frec to create new state */
    int                  state_index /* <I> state to be delted */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_SMD_H_INCLUDED */
