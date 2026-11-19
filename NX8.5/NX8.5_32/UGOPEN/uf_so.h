/*******************************************************************************

             Copyright (c) 1997-2004,2005  UGS Corp.
                       Unpublished - All Rights Reserved



File description:

This is the Open C API public interface to smart objects.

Smart Objects "remember their parents" and know how they were defined. For
example, a smart point that is created at the intersection of two lines
associates itself to its parent objects (two lines) and can reference its
definition at their intersection. If the parents move and maintain an
intersection, the smart point updates and knows its new coordinates.

The smart object has a subobject called parms which stores the references of
the smart object. For example, a smart line would have a parms that would store
references to a start point and an end point. It is possible for the references
to be smart objects. 

Terminology:

The following terms are used throughout this chapter and are used in describing
the status of a smart object. You can obtain the status of a smart object with
 UF_SO_ask_parent_status

parent/child relationship -  is the passing of information from one object
                             (parent) to a newly created object (child). The
                             older information from the parent is necessary to
                             create new information (child).

sleepy parent - A parent is asleep if it is no longer in the model, perhaps
                because some modeling operation has been performed on the
                parent. For example, if you blend an edge, then the edge is
                asleep.

object_in_part - Many of the smart object creation functions have an input
                 parameter, object_in_part, which determines in which part to
                 create the smart object. You input the tag of any valid object
                 that exists in the part.  Since you may be working in context,
                 the part where the smart object is created does not have to be
                 the work part.

has_become_dumb - If a smart object has its parameters deleted then we
                  say that it has become dumb.  One may edit these
                  objects via the 'set' routines since their values
                  are no longer constrained.  You may also call the
                  'ask' routines.

smart object classes - Scalar, Direction, Offset, Axis and Transform are
                       new objects classes implemented as smart objects.
                       Point, Curve and Datums are old object classes
                       which were extended as smart objects.  These new
                       smart object classes may be created via the
                       'create' routines.  For example, you can create
                       a smart Scalar via an expression to control
                       the curve parameter for point on curve.

smart object examples - Please see  ufd_draw_aux_view.c
                         ufd_draw_circ_det_vw.c
                         ufd_drw_bound_point.c
                         ufd_drw_set_view_anchor.c
                         ufd_eval.c
                        for examples of how to use smart objects.

Smart Objects are created as condemned objects by default.  Condemned
objects exist only to be referenced by other objects.  This is the
definition of "condemned".  Thus condemned Smart Objects are automatically
deleted whenever the last reference to them is deleted.  You may change
the state of a Smart Object from "condemned" to "alive"  by setting it
visible using  UF_SO_set_visibility_option

******************************************************************************/

#ifndef UF_SO_H_INCLUDED
#define UF_SO_H_INCLUDED

#include <uf_defs.h>
#include <uf_disp.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************

 ****************************************************************************/
#define ERROR_UF_SO_base       1995000

#define    UF_SO_ERR_CANNOT_EDIT_SO ( ERROR_UF_SO_base )

/*****************************************************************************
    Update options for a smart object.
******************************************************************************/
enum UF_SO_update_option_e
{
    UF_SO_dont_update, /* The smart object does not update. For future use */
    UF_SO_update_within_modeling, /* The smart object updates within modeling
                                     in time stamp order (e.g. a feature).
                                     For example if the smart object is
                                     referenced by Feature(i), the SO will
                                     update after Feature(i-1) and right before
                                     Feature(i). */
    UF_SO_update_after_modeling, /* The smart object updates after modeling
                                 (e.g. a dimension) */
    UF_SO_update_after_parent_body, /* The smart object will always update after
                                       the last feature on the parent body. */
    UF_SO_update_mixed              /* The smart object will update after the 
                                       last feature on the parent body when the 
                                       parent body is in a different part and 
                                       updates within modeling in time-stamp 
                                       order for parents in the same part */
};

typedef enum UF_SO_update_option_e UF_SO_update_option_t,
*UF_SO_update_option_p_t;

/******************************************************************************
    SO visibility options.
*******************************************************************************/
enum UF_SO_visibility_option_e
{
    UF_SO_invisible, /* The smart object is not visible */
    UF_SO_visible, /* The smart object is visible */
    UF_SO_visible_if_parent_invisible /* The smart object is visible  if
                                      a parent is not loaded (for extract). */
};

typedef enum UF_SO_visibility_option_e UF_SO_visibility_option_t,
*UF_SO_visibility_option_p_t;

/******************************************************************************
    SO parent status bit masks.
*******************************************************************************/
#define UF_SO_NO_STATUS               0
#define UF_SO_HAS_DELETED_PARENT     (1 << 0)
#define UF_SO_HAS_SLEEPY_PARENT      (1 << 1)
#define UF_SO_HAS_UNLOADED_PARENT    (1 << 2)
#define UF_SO_HAS_OUT_OF_DATE_PARENT (1 << 3)
#define UF_SO_HAS_GOT_DUMB_PARENT    (1 << 4)
#define UF_SO_HAS_SO_ERROR_PARENT    (1 << 5)

/******************************************************************************
    UF_SO_ask_parents() bit masks.
*******************************************************************************/
#define UF_SO_ASK_EXP_PARENTS         (1 << 0) /* Ask referenced expressions */
#define UF_SO_ASK_SO_PARENTS          (1 << 1) /* Ask referenced smart objects */
#define UF_SO_ASK_WIREFRAME_PARENTS   (1 << 2) /* Ask referenced wireframe protos
                                                  and hwos. ( No smart objects ) */
#define UF_SO_ASK_ALL_PARENTS         (1 << 3) /* Ask referenced objects.
                                                  Including lwos and stubs */
#define UF_SO_ASK_PARENTS_RECURSIVELY (1 << 4) /* Ask referenced objects
                                                  recursively */
#define UF_SO_ASK_UNLOADED_PARENTS    (1 << 5) /* Ask referenced unloaded
                                                  objects */
#define UF_SO_STOP_RECURSIVE_AT_DISPLAYED_GEOMETRY (1 << 6)
                                               /* The recursive query does not go beyond the displayed geometry level.
                                                  In another word, it does not recursively ask the parents of a displayed
                                                  geometry.*/
#define UF_SO_ASK_PARENTS_REFERENCING_SC     (1 << 7) /* Ask referenced objects recursively which ultimately refer a section or smart container */
#define UF_SO_ASK_PARENTS_NOT_REFERENCING_SC (1 << 8) /* Ask referenced objects which have no references recursively to a section or smart container */

/******************************************************************************
    UF_SO_ask_children() bit masks.
*******************************************************************************/
#define UF_SO_ASK_SO_CHILDREN          (1 << 0) /* Ask referencing smart objects */
#define UF_SO_ASK_CHILDREN_RECURSIVELY (1 << 1) /* Ask referencing objects
                                                   recursively */
#define UF_SO_ASK_FEATURE_CHILDREN     (1 << 2) /* Ask referencing features */
#define UF_SO_ASK_ALL_CHILDREN         (1 << 3) /* Ask referencing objects */

/******************************************************************************
    SCALAR dimensionality options
*******************************************************************************/
enum UF_SO_scalar_dim_option_e
{
    UF_SO_scalar_dimensionality_none,
    UF_SO_scalar_dimensionality_length,
    UF_SO_scalar_dimensionality_area,
    UF_SO_scalar_dimensionality_volume
};

typedef enum UF_SO_scalar_dim_option_e UF_SO_scalar_dim_option_t,
*UF_SO_scalar_dim_option_p_t;

/******************************************************************************
    DIRR_on_curve options.
*******************************************************************************/
enum UF_SO_dirr_on_curve_option_e
{
    UF_SO_dirr_on_curve_tangent, /* Use direction tangent to curve */
    UF_SO_dirr_on_curve_normal, /* Use direction normal to curve */
    UF_SO_dirr_on_curve_binormal /* Use direction binormal to curve (B = TXN) */
};

typedef enum UF_SO_dirr_on_curve_option_e UF_SO_dirr_on_curve_option_t,
*UF_SO_dirr_on_curve_option_p_t;

/******************************************************************************
    POINT_along_curve options.
*******************************************************************************/
enum UF_SO_point_along_curve_option_e
{
    UF_SO_point_along_curve_distance,
    UF_SO_point_along_curve_percent
};

typedef enum UF_SO_point_along_curve_option_e UF_SO_point_along_curve_option_t,
*UF_SO_point_along_curve_option_p_t;

/*****************************************************************************

  Structure definition for direction on surface data. It includes all the
  input elements to create a smart direction on surface object.

  The direction will be evaluated along isoparametric, normal or a specified
  section direction at a pair of (u,v) parameters on the underlying surface of
  a given face. Two scalar objects need to be created for the uv parameters.

  If the section option is chosen, a direction object needs to be created for
  specification. The direction will be projected to be perpendicular to the
  surface normal at the given uv parameters. The projected direction will
  underlie the output direction on surface object.

****************************************************************************/
struct UF_SO_dirr_on_surf_data_s
{
    tag_t   face;   /* object id of the face which contains the evaluation
                       surface */
    tag_t   uv[2];  /* scalar object ids for the u and v parameters of the
                       surface */
    int     option; /* flag for evaluation option:
                       0 = u isoparametric
                       1 = v isoparametric
                       2 = surface normal
                       3 = section */
    tag_t   secdir; /* object id of the section direction */
    logical flip;   /* flag for direction reversal
                       0 = no
                       1 = yes */
};

typedef struct UF_SO_dirr_on_surf_data_s UF_SO_dirr_on_surf_data_t,
    *UF_SO_dirr_on_surf_data_p_t;

/*****************************************************************************

  Structure definition for curvature on curve data. It includes all the input
  elements to create a smart offset object with the curvature on curve method.

  The curvature will be evaluated at a curve parameter. A scalar object needs
  to be created for the parameter.

  Note an offset object contains a vector of three components. For the
  curvature on curve subobject, the curvature vector is identified by the
  vector of the object. That is, the curvature value is represented by the
  magnitude of the vector and the curvature direction (the normal direction
  of the curve at that parameter) is represented by the direction of the
  vector.

****************************************************************************/
struct UF_SO_offset_curve_cvtr_data_s
{
    tag_t curve;  /* object id of the curve or edge */
    tag_t t;      /* scalar object id for the curve parameter */
};

typedef struct UF_SO_offset_curve_cvtr_data_s UF_SO_offset_curve_cvtr_data_t,
    *UF_SO_offset_curve_cvtr_data_p_t;

/*****************************************************************************

  Structure definition for curvature on surface data. It includes all the
  input elements to create a smart offset object with the curvature on
  surface method.

  The curvature will be evaluated along an isoparametric direction or a
  specified section direction at a pair of (u,v) parameters on the underlying
  surface of a given face. Two scalar objects need to be created for the uv
  parameters.

  If the section option is chosen, a direction object needs to be created for
  specification. This direction and the surface normal direction at the given
  uv parameters define a section plane on which the surface curvature is
  evaluated.

  Note an offset object contains a vector of three components. For the
  curvature on surface subobject, the curvature vector is identified by the
  vector of the object. That is, the curvature value is represented by the
  magnitude of the vector and the curvature direction (the normal direction
  of the surface at the parameters) is represented by the direction of the
  vector.

*****************************************************************************/
struct UF_SO_offset_surf_cvtr_data_s
{
    tag_t face;    /* object id of the face which contains the evaluation
                      surface */
    tag_t uv[2];   /* scalar object ids for the u and v parameters of the
                      surface */
    int   option;  /* flag for evaluation option:
                      0 = u isoparametric
                      1 = v isoparametric
                      2 = section */
    tag_t secdir;  /* object id of the section direction */
};

typedef struct UF_SO_offset_surf_cvtr_data_s UF_SO_offset_surf_cvtr_data_t,
    *UF_SO_offset_surf_cvtr_data_p_t;

/*****************************************************************************

  Structure definition for general spline data. It includes all the input
  elements to create a general smart spline object.

  The degree may be between 1 and 24.

  The array size of interpolation type, position, direction, magnitude,
  and curvature should all be number of positions. The array size for
  parameter is number of positions for nonperiodic case and number of
  positions + 1 for periodic case. For from pole method, the direction,
  tangency and curvature constraints can be applied to start and end
  positions only.

  The parameters are for through point method only. Default parameters will
  be used if the input is NULL.

  The symmetric option can be applied to one end only for through point
  method. You need to input symmetric direction for this option.

*****************************************************************************/
 struct UF_SO_spline_data_s
{
    int    method;        /* creation method:
                             0 = through points
                             1 = from poles */
    int    degree;        /* degree of the spline curve */
    int    periodic;      /* 0 = nonperiodic curve, 1 = periodic curve */
    int    nump;          /* number of positions (points or poles) */
    int    *itype;        /* <len:nump> array of integers for interpolation type at
                             each position:
                             0 = position only
                             1 = direction
                             2 = tangency (direction+magnitude)
                             3 = curvature (with tangency direction only)
                             4 = curvature (with tangency magnitude too) */
    tag_t  *position;     /* <len:nump> array of point ids for positions */
    double *parameter;    /* <len:nump> array of real values for point parameters */
    tag_t  *direction;    /* <len:nump>array of direction ids for tangent directions */
    tag_t  *magnitude;    /* <len:nump>array of scalar ids for tangent magnitudes */
    tag_t  *curvature;    /* <len:nump>array of offset ids for curvatures */
    int    symmetric[2];  /* symmetric option at start/end of the curve
                             0 = default
                             1 = symmetric model
                          */
};

typedef struct UF_SO_spline_data_s UF_SO_spline_data_t,
    *UF_SO_spline_data_p_t;


/******************************************************************************/

/*############################################################################*/
/*###############################    SO    ###################################*/
/*############################################################################*/

/****************************************************************************
Queries if an object inherits from the smart object class.
The object may or may not have parameters associated with it, i.e. it may
or may not be smart itself.  For that, call UF_SO_is_so.

Example:

    logical is_subclass = FALSE;

    UF_SO_is_so_subclass ( tag, &is_subclass );

    If ( is_subclass )
    {
        logical has_become_dumb = FALSE;

        UF_SO_has_become_dumb ( tag, &has_become_dumb );

        if ( has_become_dumb )
        {
            Printf ("Smart Object (tag %u) has lost its associativity\n" tag );
        }
    }

Environment: Internal  and  External

See Also:

History: Original Release was in V15.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_is_subclass (
const tag_t candidate ,/* <I>
                       Tag of object
                       */
logical * is_so  /* <O>
                 TRUE if candidate inherits from class SO
                 FALSE otherwise
                 */
);

/*****************************************************************************
Queries if an object is a smart object and is parameterized.

These objects are "smart" so they know how they were constructed and
will associatively update.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_is_so (
const tag_t candidate ,/* <I>
                       Tag of object
                       */
logical * is_so  /* <O>
                 TRUE = candidate is a smart object.
                 FALSE = candidate is not a smart object.
                 */
);

/*****************************************************************************
Returns the visibility option for the specified smart object.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_visibility_option (
const tag_t so ,/* <I>
                Tag of smart object
                */
UF_SO_visibility_option_p_t visibility_option  /* <O>
                                               Status of visibility option
                                               */
);

/*****************************************************************************
Returns the parent status for the specified smart object.
See  parent status bit masks

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_parent_status (
const tag_t so ,/* <I>
                Tag of smart object
                */
int * parent_status  /* <O>
                     Status of parent
                     */
);

/*****************************************************************************
Returns the smart object update error code.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_update_error_code (
tag_t so ,/* <I>
          Tag of smart object
          */
int * update_error_code  /* <O>
                         Status of parent
                         */
);

/****************************************************************************
Sets the visibility option for the specified smart object. It is the
responsibility of the calling routine to update the display.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_set_visibility_option (
tag_t so ,/* <I>
          Tag of smart object
          */
UF_SO_visibility_option_t visibility_option  /* <I>
                                             visibility option
                                             */
);

/****************************************************************************
Replaces the parms of the old smart object with the parms of the new
smart object and then deletes the new smart object.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_replace_parms (
tag_t old_so ,/* <I>
              Tag of smart object whose parms are to be replaced.
              */
tag_t new_so  /* <I>
              Tag of smart object whose parms are to be used as
              replacement parms.
              */
);

/****************************************************************************
Asks parents of smart object. Note that the following abbreviations or
terms are used in the descriptions.

lwos = Light weight ocurrences. These are not referenced but are
selectable and are displayable.

hwos = Heavy weight ocurrences. These are referenced and have
data.

stub = References an object in another part file that is not loaded.

Environment: Internal  and  External

See Also:

History: Original Release was in V15.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_parents(
const tag_t so ,/* <I>
                Tag of smart object on which to inquire parents
                */
int options ,/* <I>
             What kind of parents (bit mask)
             UF_SO_ASK_EXP_PARENTS - Ask refernced expressions.
             UF_SO_ASK_SO_PARENTS - Ask referenced smart objects.
             UF_SO_ASK_WIREFRAME_PARENTS - Ask referenced wire frame
                                           geometry (hwos).
             UF_SO_ASK_ALL_PARENTS - Ask referenced objects including
                                     lwos and stubs.
             UF_SO_ASK_PARENTS_RECURSIVELY - Ask referenced objects recursively.
             UF_SO_ASK_UNLOADED_PARENTS - Return unloaded parents.
             */
int * n_parents ,/* <O>
                  Number of parents
                  */
tag_p_t *parents  /* <OF,len:n_parents>
                  Parents of smart object
                  */
);

/****************************************************************************
Asks smart object children of object.

Environment: Internal  and  External

See Also:

History: Original Release was in V15.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_children(
const tag_t object ,/* <I>
                    Tag of object on which to inquire smart object
                    children.
                    */
int options ,/* <I>
             What kind of children (bit mask)
             UF_SO_ASK_SO_CHILDREN - Ask referencing smart objects.
             UF_SO_ASK_CHILDREN_RECURSIVELY - Ask referencing objects
                                              recursively.
             UF_SO_ASK_FEATURE_CHILDREN - Ask referencing features.
             UF_SO_ASK_ALL_CHILDREN  - Ask all referencing features.
             */
int * n_children ,/* <O>
                  number of childen
                  */
tag_p_t *children /* <OF,len:n_children>
                  Smart object children of object.  This array must be
                  freed by calling UF_free.
                  */
);

/*****************************************************************************
Delete parms of smart object.  All unreferenced
smart object parents are put on the delete list.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_delete_parms
(
    tag_t so /* <I>
             smart object
             */
);

/****************************************************************************
Displays a smart object with the specified options.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_display (
const tag_t so ,/* <I>
                Tag of smart object to display
                */
const int view_option ,/* <I>
                       view option:
                       UF_DISP_ALL_VIEWS_BUT_DRAWING
                       UF_DISP_VIEW_OF_LAST_CURSOR
                       UF_DISP_ALL_ACTIVE_VIEWS
                       UF_DISP_WORK_VIEW_ONLY
                       */
const int color_option ,/* <I>
                        color option:
                        UF_DISP_USE_SYSTEM_COLOR
                        UF_DISP_USE_BACKGROUND_COLOR
                        UF_DISP_USE_ORIGINAL_COLOR
                        UF_DISP_USE_SPECIFIED_COLOR
                        */
const int color  /* <I>
                 color option - used only when color option is
                 UF_DISP_USE_SPECIFIED_COLOR.  See uf_obj.h for
                 valid color assignments.
                 */
);

/****************************************************************************
Displays a smart object's parents with the specified options.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_display_parents (
const tag_t so ,/* <I>
                Tag of smart object to display
                */
const int view_option ,/* <I>
                       view option:
                       UF_DISP_ALL_VIEWS_BUT_DRAWING
                       UF_DISP_VIEW_OF_LAST_CURSOR
                       UF_DISP_ALL_ACTIVE_VIEWS
                       UF_DISP_WORK_VIEW_ONLY
                       */
const int color_option ,/* <I>
                        color option:
                        UF_DISP_USE_SYSTEM_COLOR
                        UF_DISP_USE_BACKGROUND_COLOR
                        UF_DISP_USE_ORIGINAL_COLOR
                        UF_DISP_USE_SPECIFIED_COLOR
                        */
const int color  /* <I>
                 color option - used only when color option is
                 UF_DISP_USE_SPECIFIED_COLOR.  See uf_obj.h for
                 valid color assignments.
                 */
);

/****************************************************************************
Determines if the given object is out of date.  This means that the
object did not update when it needed to. For example, a smart point
"is out of date" after it does not update because some of its parents
are not loaded.

Environment: Internal  and  External

See Also:
 UF_SO_ask_parent_status

History: Originally released in V15.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_is_out_of_date
(
    tag_t    so,            /* <I>
                            smart object to check if is out of date
                            */
    logical *is_out_of_date /* <O>
                            TRUE if is out of date, else FALSE
                            */
);

/*****************************************************************************
Determines if the given object has become dumb.  This means that
the object is no longer associative. For example, a smart point "has
become dumb" after one calls UF_SO_delete_parms() on it.

Environment: Internal  and  External

See Also:  UF_SO_delete_parms

History: Originally released in V15.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_has_become_dumb
(
    tag_t    so,             /* <I>
                             smart object to check if has become dumb
                             */
    logical *has_become_dumb /* <O>
                             TRUE if has become dumb, else FALSE
                             */
);

/*****************************************************************************
Delete SO's that are condemned and not sleepy/promoted/occurrenced/referenced.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_delete_non_deletables
(
    tag_t part /* <I>
               part to process
               */
);

/*############################################################################*/
/*###############################  SCALAR  ###################################*/
/*############################################################################*/

/****************************************************************************
Creates a double scalar.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_scalar_double (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const double dbl ,/* <I>
                  Real constant
                  */
tag_p_t scalar  /* <O>
                Pointer to double scalar
                */
);

/*****************************************************************************
Creates a smart scalar via an expression.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_scalar_exp (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t exp ,/* <I>
                 Tag of expression
                 */
tag_p_t scalar  /* <O>
                Pointer to smart scalar
                */
);

/****************************************************************************
Creates smart scalar via extract scalar with optional scale.

Environment: Internal  and  External

See Also:

History: Original Release was in V14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_scalar_extract(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t scalar1 ,/* <I>
                     Tag of extracted scalar
                     */
const tag_t scale ,/* <I>
                   Tag of transform or scalar (NULL_TAG
                   implies the identity matrix for the
                   transform)
                   */
tag_p_t scalar2  /* <O>
                 Pointer to tag of smart scalar
                 */
);

/*****************************************************************************
Creates a dimensioned double scalar.  A dimensioned double scalar
should be used when the scalar represents a value with units, i.e.
inches or millimeters.  The value of the dimension can then be used to
correctly convert the scalar when the part is converted from one unit
to another.

Environment: Internal  and  External

See Also:

History: Original Release was in V14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_scalar_double_dim (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const double dbl ,/* <I>
                  Real constant
                  */
const UF_SO_scalar_dim_option_t dim ,/* <I>
                                     Dimension of scalar
                                     */
tag_p_t scalar  /* <O>
                Pointer to double scalar
                */
);

/*****************************************************************************
Creates a dimensioned smart scalar via an expression.  A dimensioned
smart scalar should be used when the scalar represents a value with
units, i.e. inches or millimeters.  The value of the dimension can then
be used to correctly convert the scalar when the part is converted
from one unit to another.

Environment: Internal  and  External

See Also:

History: Original Release was in V14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_scalar_exp_dim (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t exp ,/* <I>
                 Tag of expression
                 */
const UF_SO_scalar_dim_option_t dim ,/* <I>
                                     Dimension of scalar
                                     */
tag_p_t scalar  /* <O>
                Pointer to smart scalar
                */
);

/****************************************************************************
Creates a dimensioned smart scalar via extract scalar with optional
scale.  A dimensioned smart scalar should be used when the scalar
represents a value with units, i.e. inches or millimeters.  The value of
the dimension can then be used to correctly convert the scalar when
the part is converted from one unit to another.

Environment: Internal  and  External

See Also:

History: Original Release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_scalar_extract_dim(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t scalar1 ,/* <I>
                     Tag of extracted scalar
                     */
const tag_t scale ,/* <I>
                   Tag of transform or scalar (NULL_TAG
                   implies the identity matrix for the
                   transform)
                   */
const UF_SO_scalar_dim_option_t dim ,/* <I>
                                     Dimension of scalar
                                     */
tag_p_t scalar2  /* <O>
                 Pointer to tag of smart scalar
                 */
);

/****************************************************************************
Creates a smart scalar via distance between two points.

Environment: Internal  and  External

See Also:

History: Original Release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_scalar_dist_2_pnts(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t points[2] ,/* <I>
                       Array of tags for two points for point,
                       curve, edge, face, or body.
                       */
tag_p_t scalar  /* <O>
                Pointer to tag of smart scalar
                */
);


/****************************************************************************
Creates a smart scalar via the length of a curve or edge.

Environment: Internal  and  External

See Also:

History: Original Release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_scalar_length_crv(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t curve ,/* <I>
                   Tag of curve or edge
                   */
tag_p_t scalar  /* <O>
                Pointer to tag of smart scalar
                */
);

/*****************************************************************************
Returns value of a scalar.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_double_of_scalar (
const tag_t scalar ,/* <I>
              Tag of scalar
              */
double * dbl  /* <O>
              Value of scalar
              */
);

/*****************************************************************************
Sets value of a dumb scalar.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_set_double_of_scalar (
tag_t scalar ,/* <I>
              Tag of dumb scalar
              */
const double dbl  /* <I>
                  Value of scalar
                  */
);

/****************************************************************************
Returns the expression of the smart scalar object which was created
with UF_SO_create_scalar_exp.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_exp_of_scalar(
const tag_t scalar ,/* <I>
                    Tag of scalar
                    */
tag_p_t exp  /* <O>
             Expression of scalar
             */
);

/*###########################################################################*/
/*##############################   DIRR   ###################################*/
/*###########################################################################*/

/*****************************************************************************
Creates a double direction.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_doubles (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const double direction[3] ,/* <I>
                           Real direction vector
                           */
tag_p_t dirr  /* <O>
              Pointer to tag of smart direction
              */
);

/*****************************************************************************
Create a double direction.  The user defined real point of the
double direction is used for display.

Environment: Internal  and  External

See Also:

History: Original Release was in V16.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_doubles_pnt
(
    const tag_t                 object_in_part, /* <I>
                                                Object in the part to create
                                                the double direction in.
                                                */
    const UF_SO_update_option_t update_option,  /* <I>
                                                update option
                                                */
    const double                point[3],       /* <I>
                                                real point of direction
                                                */
    const double                direction[3],   /* <I>
                                                real direction vector
                                                */
    tag_p_t                     dirr            /* <O>
                                                Double direction object that
                                                was created.
                                                */

);

/*****************************************************************************
Creates a smart direction via two points.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_two_points (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t points[2] ,/* <I>
                       Two points
                       */
tag_p_t dirr  /* <O>
              Pointer to tag of smart direction
              */
);

/*****************************************************************************
Creates a direction on a curve using t value.

Note:  This function can not be used to compute the normal for a line or
       a spline made from two points.  This is due to the fact that lines
       have no associated csys so there is no unique normal.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_on_curve (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t curve ,/* <I>
                   Tag of curve
                   */
const tag_t t ,/* <I>
               Tag of parameter object
               */
const UF_SO_dirr_on_curve_option_t option ,/* <I>
                                           Tangent/Normal/Binormal
                                           */
const logical flip ,/* <I>
                    TRUE = Flip direction
                    FALSE = Do not flip direction
                    */
tag_p_t direction  /* <O>
                   Pointer to tag of direction
                   */
);

/*****************************************************************************
Creates direction of line.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_line (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t line ,/* <I>
                  Tag of line (curve/edge/axis)
                  */
const logical flip ,/* <I>
                    TRUE = Flip direction
                    FALSE = Do not flip direction
                    */
tag_p_t direction  /* <O>
                   Pointer to tag of smart direction
                   */
);

/*****************************************************************************
Creates direction of plane.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_plane (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t plane ,/* <I>
                   Tag of plane (face/datum)
                   */
const logical flip ,/* <I>
                    TRUE = Flip direction
                    FALSE = Do not flip direction
                    */
tag_p_t direction  /* <O>
                   Pointer to tag of smart direction
                   */
);

/*****************************************************************************
Creates direction via axis of conic.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_axis_of_conic (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t conic ,/* <I>
                   Tag of plane (curve/edge)
                   */
const logical flip ,/* <I>
                    TRUE = Flip direction
                    FALSE = Do not flip direction
                    */
tag_p_t direction  /* <O>
                   Pointer to tag of smart direction
                   */
);

/*****************************************************************************
Creates direction via extract direction with optional transformation.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_extract (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t dir ,/* <I>
                 Tag of direction
                 */
const tag_t xform ,/* <I>
                   Tag of transformation
                   (NULL_TAG => identity)
                   */
tag_p_t direction  /* <O>
                   Pointer to tag of smart direction
                   */
);

/****************************************************************************
Creates a direction via two directions.  The output direction is
the cross product of the two input directions.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_two_dirs (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t directions[2] ,/* <I>
                           Array of tags of two directions
                           */
tag_p_t direction  /* <O>
                   Pointer to tag of smart direction
                   */
);

/*****************************************************************************
Creates direction via axis of surface.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_surface_axis (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t conic ,/* <I>
                   Tag of face
                   */
const logical flip ,/* <I>
                    TRUE = Flip direction
                    FALSE = Do not flip direction
                    */
tag_p_t direction  /* <O>
                   Pointer to tag of smart direction
                   */
);
/*****************************************************************************
Creates a direction normal to a surface at a given point on that surface.

Environment: Internal  and  External

See Also:

History: Original Release was in V16.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_normal_to_surface_point (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t face,/* <I>
                    Tag of the face.
                 */
const tag_t point ,/* <I>
                      Tag of the point on the face where the normal is to be
                      created.
                   */
const logical flip ,/* <I>
                       TRUE = Flip direction
                       FALSE = Do not flip direction
                    */
tag_p_t direction  /* <O>
                      Pointer to the tag of a smart direction.
                   */
);

/*****************************************************************************

  Create a direction on surface smart object.

  Environment: Internal  and  External

  See Also:

  History: Originally released in V18.0.

*****************************************************************************/
extern UFUNEXPORT int UF_SO_create_dirr_on_surf
(
    tag_t                       object_in_part,
                                /* <I> the part context */
    UF_SO_update_option_t       update_option,
                                /* <I> update option */
    UF_SO_dirr_on_surf_data_p_t dirr_on_surf_data,
                                /* <I> pointer to Open API data structure
                                   for direction on surface */
    tag_t                       *direction
                                /* <O> pointer to object id of the direction
                                   on surface */
);

/*****************************************************************************

  Inquire a direction on surface smart object.

  Environment: Internal  and  External

  See Also:

  History: Originally released in V18.0.

*****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_dirr_on_surf
(
    tag_t                       direction,
                                /* <I> object id of the direction on surface */
    UF_SO_dirr_on_surf_data_p_t dirr_on_surf_data
                                /* <O> pointer to Open API data structure
                                   for direction on surface */
);

/*****************************************************************************
Returns the value of direction.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_direction_of_dirr (
const tag_t direction ,/* <I>
                       Tag of direction
                       */
double dir[3]  /* <O>
               Value of direction
               */
);

/*****************************************************************************
Sets value of dumb direction.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_set_direction_of_dirr (
tag_t direction ,/* <I>
                 Tag of dumb direction
                 */
const double dir[3]  /* <I>
                     Value of direction.
                     */
);

/*############################################################################*/
/*###############################  OFFSET  ###################################*/
/*############################################################################*/

/*****************************************************************************
Creates a double offset.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_offset_double (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const double offset1[3] ,/* <I>
                         Real vector
                         */
tag_p_t offset2  /* <O>
                 Pointer to tag of double offset
                 */
);

/*****************************************************************************
Create a double offset.  The user defined real point of the
double offset is used for display.

Environment: Internal  and  External

See Also:

History: Original Release was in V16.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_offset_double_pnt
(
    const tag_t                 object_in_part, /* <I>
                                                Object in the part where the
                                                double offset will be created.
                                                */
    const UF_SO_update_option_t update_option,  /* <I>
                                                update option
                                                */
    const double                point[3],       /* <I>
                                                real point of offset
                                                */
    const double                offset1[3],     /* <I>
                                                real offset vector
                                                */
    tag_p_t                     offset2        /* <O>
                                               Tag of the double offset created.
                                               */

);

/*****************************************************************************
Creates a direction/distance offset.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_offset_dir_dist (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const  tag_t direction ,/* <I>
                        Tag of direction vector
                        */
const  tag_t distance ,/* <I>
                       Tag of scalar offset distance
                       */
tag_p_t offset  /* <O>
                Pointer to tag of direction/distance offset
                */
);

/*****************************************************************************
Creates a smart offset via extract  offset with optional transformation.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_offset_extract (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const  tag_t offset1 ,/* <I>
                      Tag of extract offset
                      */
const  tag_t xform ,/* <I>
                    Tag of transformation
                    */
tag_p_t offset2  /* <O>
                 Pointer to tag of smart offset
                 */
);

/*****************************************************************************
Creates a smart offset using three smart scalars.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_offset_3_scalars(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
tag_t xyz[3] ,/* <I>
              Array of tags of smart scalars
              */
tag_p_t offset  /* <O>
                Pointer to smart offset
                */
);

/****************************************************************************
Creates a smart cylindrical offset. The radius, angle, and zdelta are
the three parameters of cylindrical coordinates.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_offset_cylindrical(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
tag_t radius ,/* <I>
              Tag of scalar radius
              */
tag_t angle ,/* <I>
             Tag of scalar angle in radians
             */
tag_t zdelta ,/* <I>
              Tag of scalar delta along axis of
              cylinder.
              */
tag_p_t offset  /* <O>
                Pointer to tag of vector offset
                */
);

/****************************************************************************
Creates a smart spherical offset. The radius, angle1, and angle2 are
the three parameters of spherical coordinates (r,q,f) respectively.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_offset_spherical(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
tag_t radius ,/* <I>
              Tag of scalar spherical radius
              */
tag_t angle1 ,/* <I>
              Tag of scalar angle (longitude) in
              radians
              */
tag_t angle2 ,/* <I>
              Tag of scalar angle (colatitude) in
              radians
              */
tag_p_t offset  /* <O>
                Pointer to tag of vector offset
                */
);

/*****************************************************************************

  Create a curvature on curve smart offset object.

  Environment: Internal  and  External

  See Also:

  History: Originally released in V18.0.

*****************************************************************************/
extern UFUNEXPORT int UF_SO_create_offset_curve_cvtr
(
    tag_t                            object_in_part,
                                     /* <I> the part context */
    UF_SO_update_option_t            update_option,
                                     /* <I> update option */
    UF_SO_offset_curve_cvtr_data_p_t offset_curve_cvtr_data,
                                     /* <I> pointer to Open API data structure
                                        for curvature on curve */
    tag_t                            *curvature
                                     /* <O> pointer to object id of the smart
                                        offset for curvature on curve */
);

/*****************************************************************************

  Inquire a curvature on curve smart offset object.

  Environment: Internal  and  External

  See Also:

  History: Originally released in V18.0.

*****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_offset_curve_cvtr
(
    tag_t                            curvature,
                                     /* <I> object id of the smart
                                        offset for curvature on curve */
    UF_SO_offset_curve_cvtr_data_p_t offset_curve_cvtr_data
                                     /* <O> pointer to Open API data structure
                                        for curvature on curve */
);

/*****************************************************************************

  Create a curvature on surface smart offset object.

  Environment: Internal  and  External

  See Also:

  History: Originally released in V18.0.

*****************************************************************************/
extern UFUNEXPORT int UF_SO_create_offset_surf_cvtr
(
    tag_t                           object_in_part,
                                    /* <I> the part context */
    UF_SO_update_option_t           update_option,
                                    /* <I> update option */
    UF_SO_offset_surf_cvtr_data_p_t offset_surf_cvtr_data,
                                    /* <I> pointer to Open API data structure
                                        for curvature on surface */
    tag_t                           *curvature
                                    /* <O> pointer to object id of the smart
                                       offset for curvature on surface */
);

/*****************************************************************************

  Inquire a curvature on surface smart offset object.

  Environment: Internal  and  External

  See Also:

  History: Originally released in V18.0.

*****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_offset_surf_cvtr
(
    tag_t                           curvature,
                                    /* <I> object id of the smart
                                       offset for curvature on surface */
    UF_SO_offset_surf_cvtr_data_p_t offset_surf_cvtr_data
                                    /* <O> pointer to Open API data structure
                                        for curvature on surface */
);

/*****************************************************************************
Returns offset vector of specified offset object.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
******************************************************************************/
extern UFUNEXPORT int UF_SO_ask_offset_of_offset (
const tag_t offset ,/* <I>
                    Tag of offset
                    */
double offset_vec[3]  /* <O>
                      Value of offset
                      */
);

/*****************************************************************************
Sets offset of dumb offset.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_set_offset_of_offset (
tag_t offset ,/* <I>
              Tag of dumb offset
              */
const  double new_offset[3]  /* <I>
                             Value of offset
                             */
);

/*############################################################################*/
/*###############################   AXIS   ###################################*/
/*############################################################################*/

/*****************************************************************************
Creates a double axis.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_axis_doubles (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const double point[3] ,/* <I>
                       Axis point
                       */
const double direction[3] ,/* <I>
                           Axis direction
                           */
tag_p_t axis  /* <O>
              Pointer to tag of axis
              */
);

/*****************************************************************************
Creates a point/direction axis.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
****************************************************************************/
extern UFUNEXPORT int UF_SO_create_axis_point_dir (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t point ,/* <I>
                   Tag of axis point
                   */
const tag_t direction ,/* <I>
                       Tag of axis direction
                       */
tag_p_t axis  /* <O>
              Pointer to tag of smart axis
              */
);

/*****************************************************************************
Creates a smart axis via extract axis with optional transformation.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
*****************************************************************************/
extern UFUNEXPORT int UF_SO_create_axis_extract (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const  tag_t axis ,/* <I>
                   Tag of extract axis
                   */
const  tag_t xform ,/* <I>
                    Tag of transformation
                    */
tag_p_t axis2  /* <O>
               Pointer to tag of smart axis
               */
);

/*****************************************************************************
Returns point of axis.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
*****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_point_of_axis (
const tag_t axis ,/* <I>
                  Tag of axis
                  */
double point[3]  /* <O>
                 Value of axis point
                 */
);

/*****************************************************************************
Returns direction of axis.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_direction_of_axis (
const tag_t axis ,/* <I>
                  Tag of axis
                  */
double direction[3]  /* <O>
                     Value of axis direction
                     */
);

/*****************************************************************************
Sets point of dumb axis.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
****************************************************************************/
extern UFUNEXPORT int UF_SO_set_point_of_axis (
tag_t axis ,/* <I>
            Tag of dumb axis
            */
const  double new_point[3]  /* <I>
                            Value of axis point
                            */
);

/*****************************************************************************
Sets direction of dumb axis.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_set_direction_of_axis (
tag_t axis ,/* <I>
            Tag of dumb axis
            */
const  double new_direction[3]  /* <I>
                                Value of axis direction
                                */
);

/*############################################################################*/
/*##############################   XFORM   ###################################*/
/*############################################################################*/

/****************************************************************************
Creates a dumb double transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_xform_doubles (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Unused - set to zero
                                           */
const double point[3] ,/* <I>
                       Point
                       */
const double x_direction[3] ,/* <I>
                             X-direction
                             */
const double y_direction[3] ,/* <I>
                             Y-direction
                             */
const double scale ,/* <I>
                    Scale value
                    */
tag_p_t xform  /* <O>
               Pointer to tag of smart transform
               */
);

/*****************************************************************************
Creates a smart transform given a point, x and y directions, and an
optional scale.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
****************************************************************************/
extern UFUNEXPORT int UF_SO_create_xform_pnt_xy_dirs (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option - must be the same as the
                                           update option used to create the input
                                           point
                                           */
const tag_t point ,/* <I>
                   Tag of point
                   */
const tag_t x_direction ,/* <I>
                         Tag of x-direction
                         */
const tag_t y_direction ,/* <I>
                         Tag of y-direction
                         */
const tag_t scale ,/* <I>
                   Tag of scale value
                   */
tag_p_t xform  /* <O>
               Pointer to tag of smart transform
               */
);

/*****************************************************************************
Creates a smart transform given a point, x and z directions, and an
optional scale.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_xform_pnt_xz_dirs (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t point ,/* <I>
                   Tag of point
                   */
const tag_t x_direction ,/* <I>
                         Tag of x-direction
                         */
const tag_t z_direction ,/* <I>
                         Tag of z-direction
                         */
const tag_t scale ,/* <I>
                   Tag of scale value
                   */
tag_p_t xform  /* <O>
               Pointer to tag of smart transform
               */
);

/****************************************************************************
Creates a smart transform given a point, y and z directions, and an
optional scale.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_xform_pnt_yz_dirs (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t point ,/* <I>
                   Tag of point
                   */
const tag_t y_direction ,/* <I>
                         Tag of x-direction
                         */
const tag_t z_direction ,/* <I>
                         Tag of z-direction
                         */
const tag_t scale ,/* <I>
                   Tag of scale value
                   */
tag_p_t xform  /* <O>
               Pointer to tag of smart transform
               */
);

/*****************************************************************************
Creates a smart transform given a reference csys, point0, point1, rotational_offsets
(if any) and an optional scale.  It will translate then rotate.  The csys will be
rotated about the X axis, the Y axis then about the Z axis.  Angles should be 
specified in degrees.

Environment: Internal  and  External

See Also:

History: Original Release was in NX3

****************************************************************************/
extern UFUNEXPORT int UF_SO_create_xform_offset_xform(

 const tag_t                                         object_in_part,         /* <I> determines the context */
 const UF_SO_update_option_t update_option,         /* <I> update option */
 const tag_t                                         csys,                            /* <I> reference csys */
 const tag_t                                         point0,                         /* <I> from point */
 const tag_t                                         point1,                         /* <I> to point */
 const tag_t                                         rot_scalar_tags[3], /* <I> Rotation offset expressions tags */
 const tag_t                                         scale,                          /* <I> scalar ( NULL_TAG => IDENTITY ) */
 const tag_p_t                                    xform                           /* <O> Smart xform*/

);

/*****************************************************************************
Creates a smart transform given a three points and the scale.  The three points
used to construct the xform must NOT be collinear.  In other words, one point 
can't be collinear with the other 2 points.

Environment: Internal  and  External

See Also:

History: Original Release was in NX301
****************************************************************************/
extern UFUNEXPORT int UF_SO_create_xform_three_points
(
 const tag_t                                        object_in_part,       /* <I> determines the context */
 const UF_SO_update_option_t                        update_option,        /* <I> update option */
 const tag_t                                        point0,               /* <I> origin point */
 const tag_t                                        point1,               /* <I> x-dir point */
 const tag_t                                        point2,               /* <I> y-dir point 
                                                                          NOTE: The y-dir specified as an input may be
                                                                          modified slightly if it doesn not result in a
                                                                          true orthogonal direction given the specified
                                                                          origin and x-dir. */
 const tag_t                                        scale,                /* <I> scalar ( NULL_TAG => IDENTITY ) */
 const tag_p_t                                      xform                 /* <O> Smart xform*/
);

/*****************************************************************************
Creates a smart transform given a three planes/faces and the scale.

Environment: Internal  and  External

See Also:

History: Original Release was in NX301
****************************************************************************/
extern UFUNEXPORT int UF_SO_create_xform_three_planes
(
 const tag_t              object_in_part, /* <I> determines the context */
 const UF_SO_update_option_t  update_option,        /* <I> update option */
 const tag_t              plane0,         /* <I> first plane */
 const tag_t              plane1,         /* <I> second plane */
 const tag_t              plane2,         /* <I> third plane */
 const tag_t              scale,           /* <I> scalar ( NULL_TAG => IDENTITY ) */
 const tag_p_t            xform           /* <O> Smart xform*/
);

/*****************************************************************************
Creates a smart transform via extract transform with optional
transformation.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_xform_extract (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t xform1 ,/* <I>
                    Tag of transform to extract from
                    */
const tag_t xform2 ,/* <I>
                    Tag of transform
                    */
tag_p_t xform  /* <O>
               Pointer to tag of smart transform
               */
);

/*****************************************************************************
Create an assy_context smart transform, encapsulating the transform to go
from one part occurrence in an assembly tree to another.  Either
from_part_occ or to_part_occ can be NULL_TAG, indicating that the
transform goes to or from the root part occ of the specified part.  If
they are both non-NULL, they must be in the same part.
If from_part_occ and to_part_occ are the same, including if they are
both NULL_TAG, then no assy_context_xform is created, and
NULL_TAG is returned in the relevant argument.
If to_part_occ is not NULL_TAG, its prototype part has to be the part
that contains object_in_part.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_xform_assy_ctxt (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const tag_t from_part_occ ,/* <I>
                           Beginning position for transform
                           */
const tag_t to_part_occ ,/* <I>
                         End position for transform
                         */
tag_p_t xform  /* <O>
               Pointer to tag of transform
               */
);

/*****************************************************************************
Returns point of transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_point_of_xform (
const tag_t xform ,/* <I>
                   Tag of transform
                   */
double point[3]  /* <O>
                 Value of transform point
                 */
);

/*****************************************************************************
Returns x-direction of transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_x_direction_of_xform (
tag_t xform ,/* <I>
             Tag of transform
             */
double x_direction[3]  /* <O>
                       Value of transform X direction
                       */
);

/*****************************************************************************
Returns y-direction of transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_y_direction_of_xform (
tag_t xform ,/* <I>
             Tag of transform
             */
double y_direction[3]  /* <O>
                       Value of transform Y direction
                       */
);

/*****************************************************************************
Returns z-direction of transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_z_direction_of_xform (
tag_t xform ,/* <I>
             Tag of transform
             */
double z_direction[3]  /* <O>
                       Value of transform Z direction
                       */
);

/****************************************************************************
Returns scale of transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_scale_of_xform (
tag_t xform ,/* <I>
             Tag of transform
             */
double * scale  /* <O>
                Value of transform scale
                */
);

/****************************************************************************
Returns matrix of transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_SO_ask_matrix_of_xform (
tag_t xform ,/* <I>
             Tag of transform
             */
double matrix[16]  /* <O>
                   4 x 4 transform matrix
                   */
);

/*****************************************************************************
Sets point of dumb transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_set_point_of_xform (
tag_t xform ,/* <I>
             Tag of dumb transform
             */
const double point[3]  /* <I>
                       Value of transform point
                       */
);

/*****************************************************************************
Sets x and y directions of dumb transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_set_xy_direction_of_xform (
tag_t xform ,/* <I>
             Tag of dumb transform
             */
const double x_direction[3] ,/* <I>
                             Value of transform X direction
                             */
const double y_direction[3]  /* <I>
                             Value of transform Y direction
                             */
);

/****************************************************************************
Sets scale of dumb transform.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_set_scale_of_xform (
tag_t xform ,/* <I>
             Tag of dumb transform
             */
const double scale  /* <I>
                    Value of transform scale
                    */
);

/****************************************************************************
Asks if an transform is an assy_context smart transform.  Returns an error if
given a non-transform object.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_is_assy_ctxt_xform (
const tag_t xform ,/* <I>
                   Tag of transform.
                   */
logical * is_assy_xform  /* <O>
                         True if transform is an assy_context transform, false
                         otherwise
                         */
);

/*****************************************************************************
Given a to_part_occ for the assy_context xform, get the corresponding
from_part_occ (i.e. one that is part of the same assembly part occ
tree). The to_part_occ must be one whose prototype part contains the
assy_context xform. Returns an error if given a non-assy_context
xform object.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_assy_ctxt_part_occ (
const tag_t assy_context_xform ,/* <I>
                                Tag of assy_context transform
                                */
const tag_t to_part_occ ,/* <I>
                         to_part_occ giving assy context.
                         */
tag_p_t from_part_occ  /* <O>
                       from_part_occ corresponding to given
                       to_part_occ.
                       */
);

/*############################################################################*/
/*###############################  POINT   ###################################*/
/*############################################################################*/

/*****************************************************************************
Creates a smart point via a curve and scalar value t.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_on_curve (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t curve ,/* <I>
                   Tag of curve
                   */
const tag_t t ,/* <I>
               Tag of scale
               */
tag_p_t point  /* <O>
               Pointer to tag of point
               */
);

/*****************************************************************************
Creates a smart point via a point and an offset.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_offset (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t base_point ,/* <I>
                        Tag of base point
                        */
const tag_t offset ,/* <I>
                    Tag of offset
                    */
tag_p_t point  /* <O>
               Pointer to tag of point
               */
);

/****************************************************************************
Creates a smart point via the center of a conic.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ***************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_conic_center (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t conic ,/* <I>
                   Tag of conic
                   */
tag_p_t point  /* <O>
               Pointer to tag of point
               */
);

/*****************************************************************************
Creates a smart point via two curve intersection.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_two_curves (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t curve1 ,/* <I>
                    Tag of first curve
                    */
const tag_t curve2 ,/* <I>
                    Tag of second curve
                    */
const tag_t help_point1 ,/* <I>
                         Tag of point
                         */
const tag_t help_point2 ,/* <I>
                         Tag of point
                         */
tag_p_t point  /* <O>
               Pointer to tag of smart point
               */
);

/****************************************************************************
Creates a smart point on a surface via uv scalars for the surface. Call
one of the create scalar routines to obtain the input u and v
parameters. For example, to create a point on the surface at (.25, .50)
call UF_SO_create_scalar_double_dim() twice - once for the u value
and once for the v value.

Note the u,v parameters are normalized from 0 to 1, so if you have read
surface parameters with UF_MODL_ask_face_parms, or UF_MODL_ask_face_uv_minmax,
you will have to normalize the parameters to the range of 0 to 1 prior to
creating the smart point on the surface.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_on_surface (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t face ,/* <I>
                  Tag of face
                  */
const tag_t u ,/* <I>
               Tag of u scalar parameter
               */
const tag_t v ,/* <I>
               Tag of v scalar parameter
               */
tag_p_t point  /* <O>
               Pointer to tag of smart point
               */
);

/*****************************************************************************
Creates a smart point via an extract point with optional
transformation.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_extract (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t point1 ,/* <I>
                    Tag of point to be extracted
                    */
const tag_t xform ,/* <I>
                   Tag of transformation
                   */
tag_p_t point2  /* <O>
                Pointer to tag of smart point
                */
);

/*****************************************************************************
Creates a smart point via an extract point with a display marker and optional
transformation.

Environment: Internal  and  External

See Also:

History: Original Release was in V16.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_extract_with_disp_marker
(
    const tag_t                 object_in_part ,/* <I>
                                                Tag of object in part
                                                */
    const UF_SO_update_option_t update_option ,/* <I>
                                               Update option
                                               */
    const tag_t                 point1 ,/* <I>
                                        Tag of point to be extracted
                                        */
    const tag_t                 xform ,/* <I>
                                       Tag of transformation
                                       */
    UF_DISP_poly_marker_t    disp_marker ,/* <I>
                                          Display marker type
                                          */
    tag_p_t                     point2  /* <O>
                                        Pointer to tag of smart point
                                        */
);

/*****************************************************************************
Sets/changes the display marker type for points created using
UF_SO_create_point_extract_with_disp_marker()

Environment: Internal  and  External

See Also:

History: Original Release was in V16.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_set_display_marker_of_point
(
    tag_t point ,/* <I>
                 Tag of the smart point
                 */
    UF_DISP_poly_marker_t disp_marker /* <I>
                                             Display marker type for the point
                                             */
);
/*****************************************************************************
Returns the display marker type for a point

Environment: Internal  and  External

See Also:

History: Original Release was in V16.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_display_marker_of_point
(
    tag_t point ,/* <I>
                 Tag of the smart point
                 */
    UF_DISP_poly_marker_t *disp_marker /* <O>
                                          Pointer to display marker type for
                                          the point
                                          */
);

/*****************************************************************************
Creates a smart point via three scalars.  The smart point update option must
ensure that the parent scalars update before the point.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_3_scalars (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t xyz[3] ,/* <I>
                    Array of tags of x,y, and z scalars
                    */
tag_p_t point  /* <O>
               Pointer to tag of smart point
               */
);

/*****************************************************************************
Creates a smart point using an arc and angle.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_on_arc_angle(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t arc ,/* <I>
                 Tag of arc
                 */
const tag_t angle ,/* <I>
                   Tag of angle in radians
                   */
const tag_t xform ,/* <I>
                   Tag of optional transform
                   */
tag_p_t point  /* <O>
               Pointer to tag of smart point
               */
);

/*****************************************************************************
Creates a smart point via surface/curve intersection.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_surface_crv(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t face ,/* <I>
                  Tag of surface
                  */
const tag_t curve ,/* <I>
                   Tag of curve or edge
                   */
const tag_t help_point1 ,/* <I>
                         Tag of point (optional)
                         */
const tag_t help_point2 ,/* <I>
                         Tag of point (optional)
                         */
tag_p_t point  /* <O>
               Pointer to tag of smart point
               */
);

/****************************************************************************
Creates a smart point along curve using a curve, point, and t (scalar
offset along curve).  This point is derived by finding the closest point
on the given curve to the given point and then offsetting this point
along the given curve by the arc length defined by t via absolute
distance or relative percent.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_along_curve(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t curve ,/* <I>
                   Curve or edge
                   */
const tag_t point1 ,/* <I>
                    point
                    */
const tag_t t ,/* <I>
               Scalar offset along curve
               */
const UF_SO_point_along_curve_option_t option ,/* <I>
                                               Absolute/Relative offset option.
                                               Can be one of the following
                                               enumerated constants:
                                               UF_SO_point_along_curve_distance
                                               UF_SO_point_along_curve_percent
                                               */
const logical flip ,/* <I>
                    If flip is set to TRUE, then t = -t
                    */
tag_p_t point2  /* <O>
                Pointer to tag of smart point
                */
);

/****************************************************************************
Creates a smart point on the axis of a surface by projecting a reference point
onto the given axis. The axis tag should be that of an already defined axis
smart object.  The point tag argument may be that of a point smart object.

Environment: Internal  and  External

See Also:

History:  Original release was in v17.0
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_on_axis(
const tag_t object_in_part, /* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option, /* <I>
                                           Update option
                                           */
const tag_t ref_point, /* <I>
                       Tag of point to project onto axis
                       */
const tag_t axis, /* <I>
                  Tag of axis of cylindrical or conical face
                  */
tag_p_t point_on_axis /* <O>
                      Pointer to tag of smart point
                      */
);

/****************************************************************************
Find the x, y and z values of a smart point.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_3_scalars_of_point
(
    tag_t so_point, /* <I>
                    Tag of the smart point
                    */
    tag_t scalars[3] /* <O>
                     Array that holds the three scalars
                     */
);

/****************************************************************************
Creates a smart point at an offset xyz from the given CSYS.

NOTE: If you use UF_SO_update_within_modeling as the update_option, then the
input csys must also have its modeling option set to UF_SO_update_within_modeling.

Environment: Internal  and  External

See Also:

History: The original release was in V18.0
****************************************************************************/
extern UFUNEXPORT int UF_SO_create_point_3_scalars_csys
(
    const tag_t object_in_part ,                /* <I> Tag of object in part */
    const tag_t csys_tag,                       /* <I> Tag of the csys to reference the SO. */
    const tag_t xyz[3] ,                        /* <I> Array of tags of x, y and z scalars */
    const UF_SO_update_option_t update_option , /* <I> Update option */
    tag_p_t point                               /* <O> Pointer to tag of smart point */
);

/*############################################################################*/
/*###############################  CURVE   ###################################*/
/*############################################################################*/
/******************************************************************************/

/* Bcurve slope type options */
enum UF_SO_bcurv_slope_type_e
{
    UF_SO_bcurve_no_slope = -1,
    UF_SO_bcurve_auto_slope,
    UF_SO_bcurve_slope_direction, /* use only direction of slope */
    UF_SO_bcurve_slope_mag_and_dir /* use both direction and magnitude of the
                                      slope */
};

typedef enum UF_SO_bcurv_slope_type_e UF_SO_bcurv_slope_type_t,
*UF_SO_bcurv_slope_type_p_t;

/*****************************************************************************/
/* Bcurve options : Periodic (closed) or non-periodic */
enum UF_SO_bcurv_type_e
{
    UF_SO_bcurve_non_periodic,
    UF_SO_bcurve_periodic
};

typedef enum UF_SO_bcurv_type_e UF_SO_bcurv_type_t,
*UF_SO_point_bcurv_type_p_t;

/*****************************************************************************
Create a smart b-spline curve through points

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_bcurve_thru_points
(
    UF_SO_update_option_t update_option,     /* <I>
                                             update option
                                             */
    int                   num_of_points,     /* <I>
                                             Number of points used to define the B-spline
                                             */
    tag_p_t               points,            /* <I,len:num_of_points>
                                             Array of points
                                             */
    double *              point_parameters,  /* <I>
                                             Array of user-specified parameters for points. The array length
                                             should be num_of_points for non-periodic curve and num_of_points+1
                                             for periodic curves. The parameters need to start from 0.0 and be
                                             monotonically increasing; however, they need not to be normalized.
                                             Pass in NULL to use the default chord-length parametrization.
                                             */
    int                   degree,            /* <I>
                                             Degree of the B-spline curve
                                             */
    int                   periodic,          /* <I>
                                             Curve type - 0 = non-periodic and 1 = Periodic.
                                             */
    tag_t                 start_slope,       /* <I>
                                             Tag of a point whose coordinates are used as the start slope of
                                             a non-periodic cubic bcurve.
                                             */
    tag_t                 end_slope,         /* <I>
                                             Tag of a point whose coordinates are used as the end slope of
                                             a non-periodic cubic bcurve.
                                             */
    int                   start_slope_type,  /* <I>
                                             Start slope type of a non-periodic cubic bcurve.
                                             The available slope types are:
                                             -1 = no slope
                                              0 = auto slope
                                              1 = use only direction of slope
                                              2 = use both direction and magnitude of slope
                                             */
    int                   end_slope_type,    /* <I>
                                             End slope type of a non-periodic cubic bcurve.
                                             The available slope types are the same as above.
                                             */
    tag_p_t               bcurve             /* <O>
                                             The smart B-spline
                                             */

);
/****************************************************************************
Creates a smart curve via extract curve with optional transformation.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_curve_extract (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t curve1 ,/* <I>
                    Tag of curve from which to extract
                    */
const int type ,/* <I>
                Curve type
                */
const int subtype ,/* <I>
                   Curve subtype
                   */
const tag_t xform ,/* <I>
                   Tag of transformation
                   */
tag_p_t curve2  /* <O>
                Pointer to tag of smart curve
                */
);

/*****************************************************************************

  Create a general smart spline object.

  Environment: Internal  and  External

  See Also:

  History: Originally released in V18.0.

*****************************************************************************/
extern UFUNEXPORT int UF_SO_create_spline
(
    UF_SO_update_option_t update_option, /* <I> update option */
    UF_SO_spline_data_p_t spline_data,   /* <I> pointer to Open API data
                                            structure for general spline */
    tag_t                 *spline        /* <O> pointer to object id of
                                            the created smart spline */
);

/*****************************************************************************

  Inquire a general smart spline object.

  Environment: Internal  and  External

  See Also:

  History: Originally released in V18.0.

*****************************************************************************/
extern UFUNEXPORT int UF_SO_ask_spline
(
    tag_t                 spline,      /* <I> object id of the smart spline */
    UF_SO_spline_data_p_t spline_data  /* <O> pointer to Open API data
                                          structure for general spline */
);

/*############################################################################*/
/*###############################   LINE   ###################################*/
/*############################################################################*/

/*****************************************************************************
Creates a smart line between two points.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_line_two_points(
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t points[2] ,/* <I>
                       Array of tags of two points
                       */
tag_p_t line  /* <O>
              Pointer to tag of smart line
              */
);

/*############################################################################*/
/*###############################   ARC    ###################################*/
/*############################################################################*/

/*****************************************************************************
Creates a smart arc through three points.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 *****************************************************************************/
extern UFUNEXPORT int UF_SO_create_arc_three_points (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t points[3] ,/* <I>
                       Array of tags of three points
                       */
tag_p_t arc  /* <O>
             Pointer to tag of smart arc
             */
);

/****************************************************************************
Creates a smart arc via center and two points.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_arc_center_2_pnts (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t points[3] ,/* <I>
                       Array of tags of three points (center, start, and
                       end point)
                       */
tag_p_t arc  /* <O>
             Pointer to tag of smart arc
             */
);

/****************************************************************************
Creates a smart arc via transformation, radius, and angles. To obtain
the transformation tag use any of the UF_SO_create_xform_*
routines. The radius and angles are scalars; use any of the
UF_SO_create_scalar_* routines to get tags for these scalars.

Environment: Internal  and  External

See Also:

History: Original Release was in V13.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_arc_radius_angles (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t xform ,/* <I>
                   Tag of transformation
                   */
const tag_t radius ,/* <I>
                    Tag of radius
                    */
const tag_t angles[2] ,/* <I>
                       Tags of start and end angles
                       */
tag_p_t arc  /* <O>
             Pointer to tag of smart arc
             */
);

/****************************************************************************
Creates a smart arc via two points and a transform. The arc always
lies on the xy plane of the xform. The two points are projected onto
the xy plane to give start and end points for the arc.

Environment: Internal  and  External

See Also:

History: Original Release was in V14.0.
 ****************************************************************************/
extern UFUNEXPORT int UF_SO_create_arc_xform_2_points (
const tag_t object_in_part ,/* <I>
                            Tag of object in part
                            */
const UF_SO_update_option_t update_option ,/* <I>
                                           Update option
                                           */
const tag_t xform ,/* <I>
                   Tag of transform
                   */
const tag_t points[2] ,/* <I>
                       Array of tags of two points (start and end point)
                       */
tag_p_t arc  /* <O>
             Pointer to tag of smart arc
             */
);

/* */

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SO_H_INCLUDED */
