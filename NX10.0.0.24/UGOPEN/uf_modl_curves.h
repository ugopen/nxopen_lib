/*******************************************************************************
             Copyright (c) 1998-2005  UGS Corp.
                       All Rights Reserved



File description:
    Open API modeling routines to create, edit and inquire about curves.

*****************************************************************************/

#ifndef UF_MODL_CURVES_H_INCLUDED
#define UF_MODL_CURVES_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/******************************************************************************
Extracts the curve from an input edge and returns the identifier of
that curve.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_curve_from_edge(
tag_t edge_id ,/* <I>
               Object identifier of the edge
               */
tag_t * ugcrv_id  /* <O>
                  Identifier of the extracted curve
                  */
);

/****************************************************************************
Creates isoparametric curves on a face.  You cannot create isoparametric
curves of constant v from a blend.  The resulting isoparametric curves
are not "smart" curves. In other words, they are not associative to the
face from which they were created. If the face is modified, the curves
do not change.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_isocurve(
tag_t face_id ,/* <I>
               The face identifier.
               */
int uv_flag ,/* <I>
             1 = create curve along u isoparameter.
             2 = create curve along v isoparameter.
             */
double parameter ,/* <I>
                  Parameter at which to create the curve.
                  */
double dist_tol ,/* <I>
                 Tolerance value. The tolerance is only used
                 when the input face is foreign or an offset of
                 a non analytic face.
                 */
tag_t  ** isocurve_id ,/* <OF,len:isocurve_cnt>
                       Array of isoparametric curve identifiers. You may
                       get multiple curves if the face is trimmed. The
                       allocated arrays must be freed with UF_free().
                       */
int  * isocurve_cnt  /* <O>
                     Number of curves created.
                     */
);

/****************************************************************************
Creates isocline curves on the given face defined by the specified
direction and angle.


Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_isocline_curves(
tag_t face_id ,/* <I>
               The face identifier
               */
double direction[3] ,/* <I>
                     Isocline direction (normalized vector)
                     */
double angle ,/* <I>
              Isocline angle (between specified direction and
              normals of the curves) in degrees.  Angle range is
              from -90 to +90 degrees.
              */
double dist_tol ,/* <I>
                 Tolerance value. The tolerance is only used when
                 the input face is foreign or an offset of a non
                 analytic face.
                 */
tag_t  ** isocurve_id ,/* <OF,len:isocurve_cnt>
                       Array of isocline curve object identifiers. The
                       allocated arrays must be freed with UF_free().
                       */
int  * isocurve_cnt  /* <O>
                     Number of curves created.
                     */
);

/****************************************************************************
Returns the parameter and a point on a curve given a reference point.

Environment: Internal  and  External
See Also:  UF_MODL_ask_point_along_curve_2 which may handle curves with
                 sharp corners better
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_parm(
tag_t curve_id ,/* <I>
                Curve identifier.
                */
double ref_pnt[3] ,/* <I>
                  Reference point in absolute space (3 element array)
                  */
double * parm ,/* <O>
               Parameter on curve.
               */
double curve_pnt[3]  /* <O>
                    Point on curve (3 element array).
                    */
);

/****************************************************************************
Returns the point, tangent, unit principal normal, unit binormal,
torsion, and radius of curvature on a curve at a given parameter.
The input curve parameter, parm, is normalized between 0 and 1.

UF_EVAL_evaluate should be used to evaluate curves and edges instead
of using this routine.  For a full circle, the routines may return
different results, as the parameterization of the circle may be done in
two different directions.

Environment: Internal  and  External
See Also:  UF_EVAL_evaluate
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_props(
tag_t curve_id ,/* <I>
                Curve identifier.
                */
double parm ,/* <I>
             Curve parameter.
             */
double  point[3] ,/* <O>
                Point on curve (3 element array).
                */
double  tangent[3] ,/* <O>
                  Tangent of curve (3 element array).
                  */
double  p_norm[3] ,/* <O>
                 Unit Principal normal of curve (3 element array).
                 */
double  b_norm[3] ,/* <O>
                 Unit Binormal of curve (3 element array).
                 */
double * torsion ,/* <O>
                  Torsion.
                  */
double * rad_of_cur  /* <O>
                     Radius of Curvature.
                     */
);

/****************************************************************************
Returns a parameter value for a point along a curve or edge based
upon three inputs: a reference point, an offset distance, and a
direction flag.

The point is calculated by projecting the reference point to the curve
or edge (the reference point should already be on or near the curve or
edge), and determining a location along the curve at an arc length
distance from the projected reference point.

The direction along the curve or edge at which the point is created is
determined by the direction flag.

The tolerance is used only if the input curve is a solid edge. A
temporary curve, which approximates the solid edge, is created for
processing and deleted after processing completes.

Environment: Internal  and  External

See Also:  UF_MODL_ask_point_along_curve_2 which may handle curves with
                 sharp corners better
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_point_along_curve (
double point[3] ,/* <I>
                 Absolute coordinates of the reference point.
                 */
tag_t curve ,/* <I>
             Identifier of the selected curve.
             */
double offset ,/* <I>
               Offset distance from the reference point along the
selected curve.
               */
int direction ,/* <I>
               Direction flag,
                1=Same direction as the selected curve.
                (from start point to end point)
               -1=Reverse direction of the selected curve
                (from end point to start point)
               */
double tolerance ,/* <I>
                  Distance tolerance between solid edge and
                  approximated curve.
                  */
double  * parameter  /* <O>
                     Parameter value for the located point on the
                     selected curve.
                     */
);

/***************************************************************************
 Alternate version of UF_MODL_ask_point_along_curve to better handle
 cases of curves with sharp corners or sharp bends.  Also, returns the
 point on the curve at the offset distance.
***************************************************************************/

extern UFUNEXPORT int UF_MODL_ask_point_along_curve_2 (
double point[3] ,/* <I>
                 Absolute coordinates of the reference point.
                 */
tag_t curve ,/* <I>
             Identifier of the selected curve.
             */
double offset ,/* <I>
               Offset distance from the reference point along the
selected curve.
               */
int direction ,/* <I>
               Direction flag,
                1=Same direction as the selected curve.
                (from start point to end point)
               -1=Reverse direction of the selected curve
                (from end point to start point)
               */
double tolerance ,/* <I>
                  Distance tolerance between solid edge and
                  approximated curve.
                  */
double point_along_curve [3] ,/* <O>
                 Absolute coordinates of the point on the curve
                 at the offset distance.
                 */
double  * parameter  /* <O>
                     Parameter value for the located point on the
                     selected curve.
                     */
);

/****************************************************************************
This routine is to be obsoleted in the near future.  Please use its
replacement function UF_CURVE_create_simplified_curve.

Returns an array of line and arc identifiers which approximates curves
and edges. The tolerance parameter determines the maximum
distance between a curve or edge and its approximated arc segments.
NOTE: The size of the segments array depends on the input
parameters curve_count, tolerance, and the complexity of the
individual curves being simplified. For curves that have a lot of
curvature change, it may take a lot of arcs and lines to approximate
them.

Environment: Internal  and  External
See Also: UF_CURVE_create_simplified_curve
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_simplified_curve(
int curve_count ,/* <I>
                 Count of curves and edges (512 maximum).
                 */
tag_t  * curves ,/* <I,len:curve_count>
                 Array of curve and edge identifiers. This should be
                 declared as tag_t curves[curve_count].
                 */
double tolerance ,/* <I>
                  Maximum distance from arc segment to curve.
                  */
int  * segment_count ,/* <O>
                      Count of lines and arcs.
                      */
tag_t  * segments  /* <O,len:segment_count>
                   Array of line and arc identifiers.
                   */
);

/****************************************************************************
Returns an array of 3D point coordinates (x,y,z) based on an input
curve, chordal tolerance, angular tolerance, and step tolerance.
A chord is the straight line between adjacent coordinates. The
tolerances provide independent values for controlling the output of
the coordinates located on the curve. The chordal tolerance (ctol) is
the maximum allowable distance from a chord to the curve between
the ends of the chord. The angular tolerance (atol) is the maximum
allowable sum of the angles between the chord and the tangents to the
curve at the ends of the chord. The step length (stol) is the maximum
allowable chordal length.

This routine does not create point objects as the GRIP and interactive 
methods do.

If curve_id is an occurrence, then the points returned are relative to
the occurrence, and not the prototype.

Return:
         Error code:
        0 = OK
        1 = Invalid curve
        2 = Modeler error

Note that this function treats the input "ctol" and "stol" tolerances 
and returns point coordinates in the base units of the current displayed 
part rather than the units of the part containing the input curve/edge.

In order it to return the expected coordinatesthe displayed part must be 
set to the part containing the curve (or any other part using the units 
of that part) and the display must have also been refreshed after setting 
the new displayed part.

For example:

    orig = UF_PART_ask_display_part();
    UF_PART_ask_units(orig, &display_units);

    UF_PART_ask_units(curve_owner, &units);
    if (units != display_units)
    {
        UF_PART_set_display_part(curve_owner);
        UF_DISP_refresh();  // required!
    }
...
    UF_MODL_ask_curve_points(curve, ...
...
    UF_PART_set_display_part(orig);

Environment: Internal  and  External
See Also: 
History: Modified in V15.0 to work relative to the occurrence.
         Added comments in NX8.5 regarding part units.
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_points(
tag_t curve_id ,/* <I>
                The identifier of the curve on which the points are
                to be determined.
                */
double ctol ,/* <I>
             The chordal tolerance.
             0=  do not use chordal tolerance.
             */
double atol ,/* <I>
             The angular tolerance in radians
             0=  do not use angular tolerance.
             */
double stol ,/* <I>
             Maximum step length.
             0 = do not use
             */
int * numpts ,/* <O>
              Number of points in the points array.
              */
double ** pts  /* <OF,len:3*numpts>
               Pointer to the array containing the 3D points. The
               array returned is a single dimension array of size
               pts[3*numpts]. The allocated arrays must be freed
               with UF_free.
               */
);

/****************************************************************************
Creates associated projected curves.  The tolerance used to create a
curve projection can be changed by using the subroutine
UF_MODL_set_distance_tolerance.  The projection along face normals or
along a vector produces an exact projection when projecting onto a plane.
The projected curve feature can be deleted using UF_MODL_delete_feature or
the curves can be accessed using UF_MODL_ask_proj_curves and deleted
individually. Similarly, UF_MODL_move_feature can be used to move the
projected curve feature.


Environment: Internal  and  External
See Also: UF_MODL_ask_proj_curves
          UF_CURVE_ask_proj_curves
         UF_MODL_set_distance_tolerance
          UF_MODL_delete_feature
          UF_MODL_move_feature


History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_proj_curves(
uf_list_p_t curve_refs ,/* <I>
                        List of curve, sketch, or projected curve feature
                        identifiers.
                        */
uf_list_p_t face_refs ,/* <I>
                       List of plane, datum plane, or face identifiers.
                       */
int along_face_normal ,/* <I>
                       0 = Use projection vector (proj_vector)
                       1 =  Use face normals
                       */
double proj_vector[3] ,/* <I>
                      3D vector in absolute space
                      */
tag_t * proj_curve_feature  /* <O>
                            Projected curve feature identifier
                            */
);

/****************************************************************************
Returns the curves associated with a projected curve feature.

Environment: Internal  and  External
See Also: UF_MODL_create_proj_curves
          UF_CURVE_create_proj_curves
          UF_CURVE_ask_proj_curves
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_proj_curves(
tag_t proj_curve_feature ,/* <I>
                          Projected curve feature identifier.
                          */
uf_list_p_t * uf_curve_refs  /* <OF,free:UF_MODL_delete_list>
                             Pointer to list of curve identifiers.  This list
                             must be freed by calling UF_MODL_delete_list.
                             */
);

/****************************************************************************
Returns whether a curve is a closed curve or not.

Return:
         Return code:
        0 = The identifier given is not a closed curve.
        1 = The identifier given is a closed curve.

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_closed(
tag_t tag  /* <I>
           Identifier of the curve.
           */
);/*<NEC>*/


/******************************************************************************
Evaluates a curve for position and derivatives. The derivative types
can be found in uf_modl.h.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_evaluate_curve(
tag_t curve_id ,/* <I>
                Object identifier for the curve
                */
double * param ,/* <I>
                Parameter at which to evaluate
                */
int * deriv_flag ,/* <I>
                  Number of derivatives to evaluate.
                  UF_MODL_LOC = Return the point
                  UF_MODL_LOC_1STDERV = Return the
                  point and 1st derivative
                  UF_MODL_LOC_1STDERV_2NDDERV =
                  Return the point, 1st and 2nd derivative
                  */
double  pos_and_deriv []  /* <O,len:3*(deriv_flag+1)>
                        Position and derivative.
                        Dimension of the array = 3 * (deriv_flag+1)
                        */
);

/******************************************************************************
Inquires the periodicity of the curve.  OPEN_CURVE may be periodic
(mathematically speaking, for example a sinusoidal curve) but it is not closed.

Environment: Internal  and  External
See Also:


History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_periodicity(
tag_t curve_id ,/* <I>
                Object identifier for the curve
                */
int * status  /* <O>
              Status of the curve.
              UF_MODL_OPEN_CURVE
              UF_MODL_CLOSED_PERIODIC_CURVE
              UF_MODL_CLOSED_NON_PERIODIC_CURVE
              */
);

/******************************************************************************
Returns the parameter value of the point on a curve (without
extension) closest to the input point.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_parm_no_ext(
tag_t curve_id ,/* <I>
                Object identifier for the curve
                */
double ref_point[3] ,/* <I>
                     Reference point (in absolute coordinates)
                     */
double * parm  /* <O>
               Parameter of the point on the curve
               */
);

/******************************************************************************
Returns the current setting of the curve fit method modeling preference.

Environment: Internal  and  External
See Also: UF_MODL_set_curve_fit_method
History: This function was originally released in V15.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_fit_method(
      int *fit_method    /* <O>
                         curve fit method  0=cubic, 1=quinti
                         */
);

/******************************************************************************
Sets the curve fit method modeling preference.

Environment: Internal  and  External
See Also: UF_MODL_ask_curve_fit_method
History: This function was originally released in V15.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_curve_fit_method(
      int fit_method     /* <I>
                         curve fit method  0=cubic, 1=quintic
                         */
);

/********************************************************************
Creates a spline by "fitting" the curve to the data points. The system
does not store defining points for curves created using the spline
creation function. However, these points are stored for B-curve
creation functions.

Environment: Internal  and  External

See Also:

History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_create_fitted_spline(
SPLINE_FIT_p_t spline_data ,/* <I>
                            Structure containing the spline data.
                            */
double         *max_err ,   /* <O>
                            The maximum error at any point used in the
                            approximation.
                            */
int            *max_err_pt ,/* <O>
                            The point at which the maximum error exists.
                            */
tag_p_t        obj_id       /* <O>
                            Identifier of the created curve.
                            */
);

/******************************************************************************
Creates a spline. The periodic status of the curve is inherited from the
defining data. If the curve is not periodic on input, but can be made
periodic, the resulting curve is made C1 periodic.

Tips and Techniques
This routine takes standard NURB (nonuniform rational B-spline) data as input.
The poles are ordered quadruplets consisting of the ABS coordinates and a 
weight .  As a general guideline, let all of the weights = 1.0. For the knot 
sequence values:
Let u1, ..., uorder = 0.0
Let upoles+1, ..., upoles+order = 1.0

This sets the beginning four sequence values to 0.0 and the last four
sequence values to 1.0 when the order is four. For the other sequence
values, let nu = 1/(poles-order+1). Then the remaining normalized
sequence values would be:

uorder+1 = 1nu, uorder+2 = 2nu, ..., upoles =(poles-order)nu.

For example, suppose we have 8 poles and order = 4, then:
nu = 1/(8-4+1) = 0.2 and
u1, ..., uorder = u1, ..., u4 = 0.0,
upoles+1, ..., upoles+order  = u9, ..., u12 = 1.0,
u5 = .2, u6 = .4, u7 = .6, u8 = .8 which gives us the following
normalized, non-decreasing knot sequence:

{0,0,0,0,.2,.4,.6,.8,1,1,1,1}.


Environment: Internal  and  External
See Also:

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_spline(
int nc ,/* <I>
        Number of control vertices (poles)
        */
int kc ,/* <I>
        Order (degree + 1)
        */
double knot[] ,/* <I,len:nc + kc> 
               Knot sequence (dimensioned to poles + order, e.g.
               knot[nc + kc]
               */
double poles[] ,/* <I,len:nc*4>
                Array homogeneous control vertices (wx,wy,wz,w)
                - dimensioned to (poles * 4), e.g. poles[nc * 4]
                */
tag_t * spline_id ,/* <O>
                   object identifier for the spline
                   */
int * knot_fixup ,/* <O>
                  Knot fixup status
                  0 = no fixups performed
                  1 = knot sequence fixed
                  */
int * pole_fixup  /* <O>
                  Pole fixup status
                  0 = no fixups performed
                  1 = pole array fixed
                  */
);

/************************************************************************
 *
 *      This routine shows the parent NX curves of an input feature.
 *      The customer default variable Solids_MoveCurvesToOtherLayer,
 *      defined in ug_english.def and ug_metric.def will control the
 *      behavior of this routine.
 *
 *      If Solids_MoveCurvesToOtherLayer = on, this routine
 *      will unblank all parent NX curves of the selected feature,
 *      and  will move the parent NX curves that lie on the non-selectable
 *      layers to the work layer.
 *
 *      If Solids_MoveCurvesToOtherLayer = off, this routine
 *      unblank all parent NX curves of the selected feature, and
 *      will change the mask of all non-selectable layers on which
 *      the parent NX curves lie to be selectable layers.
 *
 *      If selectable is TRUE and the parent NX curves are on visible but
 *      non-selectable layers, this routine will either move these
 *      parent NX curves to the work layer or change the mask of the
 *      layers according to the value of Solids_MoveCurvesToOtherLayer.
 *
 * Environment : Internal  and  External
 *
 * See Also: UF_MODL_hide_parent_curves
 *
 * History:  Originally released in V16.0.
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_show_parent_curves
(
    tag_t                   feature_tag,       /* <I>
                                                 Input feature record eid
                                               */
    logical                 selectable,        /* <I>
                                                 The parent curves are to be
                                                 selectable
                                               */
    int                    *n_unch_disp_stat,  /* <O>
                                                 The number of parent curves
                                                 whose display status were
                                                 unchanged after the show action
                                               */
    UF_MODL_disp_info_p_t  *unch_parents_disp_status,
                                               /* <IOF,len:n_unch_disp_stat>
                                               If NULL is passed in, then
                                               nothing is returned.  If a
                                               pointer is passed in, then
                                               an array of UF_MODL_disp_info_t
                                               structures will be allocated, one
                                               for each parent curve whose
                                               display status was unchanged. The
                                               UF_MODL_disp_info_t structure
                                               will have the original display
                                               information for the parent curve.
                                               This array can then be passed
                                               to UF_MODL_hide_parent_curves to
                                               restore the curves to their
                                               original display status.
                                               This array must be freed by the
                                               caller by calling UF_free.
                                                */
    int                    *n_ch_disp_stat,    /* <O>
                                               The number of parent curves whose
                                               display status were changed after
                                               the show action, i.e. the layer
                                               number or blank status was
                                               changed by this function.
                                                */
    UF_MODL_disp_info_p_t  *ch_parents_disp_status
                                                 /* <IOF,len:n_ch_disp_stat>
                                                 If NULL is passed in, then
                                                 nothing is returned.  If a
                                                 pointer is passed in, then
                                                 an array of UF_MODL_disp_info_t
                                                 structures will be allocated,
                                                 one for each parent curve whose
                                                 display status was changed.
                                                 The UF_MODL_disp_info_t
                                                 structure will have the
                                                 original display information
                                                 for the parent curve.This array
                                                 can then be passed
                                                 to UF_MODL_hide_parent_curves
                                                 to restore the curves to their
                                                 original display status.
                                                 This array must be freed by the
                                                 caller by calling UF_free.
                                                */
);

/************************************************************************
 *
 *      This routine hides the parent NX curves of an input feature.
 *      If the fourth parameter is null, this routine will blank all
 *      the parent NX curves of the feature.
 *
 *      If the fourth parameter is not null, it is assumed to be an array
 *      of UF_MODL_display_info_t structures returned by
        UF_MODL_show_parent_curves.
 *      This routine will restore the curves in this array to their original
 *      layers and blank status.
 *
 * Environment : Internal  and  External
 *
 * See Also: UF_MODL_show_parent_curves
 *
 * History: Originally released in V16.0
 ************************************************************************/
extern UFUNEXPORT int UF_MODL_hide_parent_curves
(
    tag_t                  feature_tag,        /* <I>
                                                  Input feature record eid
                                                */
    int                    n_unch_disp_stat,   /* <I>
                                                  The number of parent NX curves
                                                  whose original display status
                                                  are in the array
                                                  unch_parents_disp_status.
                                                  Usually, this is an output
                                                  from
                                                  UF_MODL_show_parent_curves.
                                                */
    UF_MODL_disp_info_p_t  unch_parents_disp_status, /* <I,len:n_unch_disp_stat>
                                                  If NULL, then all of the NX
                                                  curves used to construct the
                                                  feature will be blanked.
                                                  If not NULL this is an array
                                                  of structures that contain
                                                  the original display status
                                                  for the parent NX curves.
                                                  The display status for each
                                                  parent NX curve will be
                                                  restored to the original
                                                  values in this array. Normally
                                                  this array is an output from
                                                  UF_MODL_show_parent_curves
                                                */
    int                    n_ch_disp_stat,     /* <I>
                                                  The number of parent NX curves
                                                  whose original display status
                                                  are in the array
                                                  ch_parents_disp_status.
                                                  Usually, this is an output
                                                  from UF_MODL_show_parent_
                                                                         curves.
                                                */

    UF_MODL_disp_info_p_t *ch_parents_disp_status /* <I,len:n_ch_disp_stat>
                                                  If NULL, then all of the NX
                                                  curves used to construct the
                                                  feature will be blank.
                                                  If not NULL this is an array
                                                  of structures that contain the
                                                  original display status
                                                  for the parent NX curves.  The
                                                  display status for each parent
                                                  NX curve will be restored to
                                                  the original values in this
                                                  array.  Normally
                                                  this array is an output from
                                                  UF_MODL_show_parent_curves
                                                */
);


/*==========================================================================
   Prototypes for createa LAW parm 

    extern int UF_MODL_create_law()

  INPUT-
  ------
       law_method = type of law
                    1 - constant         (numeric law)
                    2 - linear           (numeric law)
                    3 - cubic s-shape    (numeric law)
                    4 - linear on spine  (numeric law)
                    5 - by equation      (equation law)
                    6 - cubic on spine   (numeric law)
                    7 - by curves        (graphic law)

       *law_str1 = contents depend on law_method setting
                 = 1 - expression for constant radius
                 = 2,3 - expression start radius value
                 = 5 - expression for t function

       *law_str2 = contents depend on law_method setting
                 = 0,1 - not used
                 = 2,3 - expression end radius value
                 = 5 - expression for f function

       spine_string  = spine curves depending on law_method setting
                     = 4,6   - (required)
                     = other - (optional)

       law_cv_string = law curves  (only for method = 7)

       num_spine_points = number of spine points (method 4 and 6 only)

       spine_xyz[] = 3D point coordinates of spine points selected (law_method
                     4 and 6 only)

       spine_values[] = law function value on the 3d points (law_method
                        4 and 6 only)

       base_line_tag = base line (law method 7 only)

       base_direction = base line direction
                         +1 or
                         -1

  OUTPUT-
  -------
       *law_parm_ptr = a pointer for a LAW_PARM data struct

  RETURNS-
  --------
       int = status
               0 - no error
               1 - invalid method
               2 - missing spine
               3 - missing law curve

  ==========================================================================*/

extern UFUNEXPORT int UF_MODL_create_law (
    int          law_method,            /* <I> */
    const char  *law_str1,              /* <I> */
    const char  *law_str2,              /* <I> */
    UF_STRING_t  spine_str,             /* <I> */
    UF_STRING_t  law_cv_str,            /* <I> */
    int          num_spine_points,      /* <I> */
    double       spine_xyz[],           /* <I> */
    double       spine_values[],        /* <I> */
    tag_t        base_line_tag,         /* <I> */
    int          base_direction,        /* <I> */
    void       **uf_law_parms           /* <O> */
);


/* ***************************************************************************
  Generate law param data <uf_law_parms> for multi-transition laws
  on base curves.

    extern int UF_MODL_create_multi_transition_law ()

  INPUT-
  ------
       UF_STRING_t spine_string    = string for base curves, <Required>
       int         num_pts         = number of law points,   <Required>
       double      *pt_xyzs        = array of 3D coords,     <Required>
       char        **pt_law_values = array of law values,    <Required>
       int         *pt_trans_types = array of law types,     <Required>

  OUTPUT-
  -------
       *uf_law_parms = pointer for law_param data, To be freed from caller
         MODL_law_pm_free ((MODL_law_p_t)(uf_law_parms));

  RETURNS-
  --------
       0 = no error
       2 = error
************************************************************************** */

extern UFUNEXPORT int UF_MODL_create_multi_transition_law (
                  UF_STRING_t  spine,                  /* <I> */
                  int          num_pts,                /* <I> */
                  double       *pt_xyzs,               /* <I,len:num_pts> */
                  char         **pt_law_values,        /* <I,len:num_pts> */
                  int          *pt_trans_types,        /* <I,len:num_pts> */
                  void         **uf_law_parms          /* <O> */);


/* **********************************************************************
 
    Free the dtat struct for uf_law_parms

************************************************************************* */

extern UFUNEXPORT void UF_MODL_free_law ( void *uf_law_parms /* <I> */);

/****************************************************************************
Creates geodesic curves on a connected set of faces given a start point, 
direction and desired length. If the length is greater than the extent 
of input face(s), then curves up to the face boundary are returned.
The resulting geodesic curves are not "smart" curves. 

Environment: Internal  and  External
See Also:
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_geodesic_curves(
int number_of_faces ,/* <I>
                     the number of faces to be used to create geodesic curve.
                     */
tag_t face_eids[] ,  /* <I,len:number_of_faces>
                     The faces to be used to create geodesic curves.
                     The faces should be connected and come from same body.
                     */
double start_pnt[3] ,/* <I>
                     Start point of geodesic curve in absolute space (3 element array).
                     The point should lie on one of the face specified in face_eids
                     */
double start_dir[3] ,/* <I>
                     Start direction of geodesic curve(normalized vector)
                     */
double length,       /* <I>
                     Desired length of geodesic curve measured from start_pnt 
                     */
double dist_tol ,    /* <I>
                     Tolerance value. The tolerance is used in fitting geodesic curves.
                     */
tag_t  ** geodesiccurve_id ,/* <OF,len:geodesiccurve_cnt>
                            Array of geodesic curve identifiers. The
                            allocated arrays must be freed with UF_free().
                            */
int  * geodesiccurve_cnt,  /* <O>
                           Number of curves created.
                           */ 
double *achieved_length    /* <O>
                           The total length of result Geodesic curves.
                           */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_CURVES_H_INCLUDED */
