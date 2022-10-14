/*****************************************************************************
             Copyright (c) 1998-2008-2006 UGS Corp.
                       Unpublished - All Rights Reserved                       



File description: 
    Open API modeling routines to create, edit and inquire about B-surfaces.
    This file uses the structure UF_MODL_state_t which is a type define of  UF_CURVE_state_t 

*****************************************************************************/

#ifndef UF_MODL_BSURF_H_INCLUDED
#define UF_MODL_BSURF_H_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <uf_curve.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef UF_CURVE_state_p_t UF_MODL_state_p_t;
typedef UF_CURVE_state_t UF_MODL_state_t;

/****************************************************************************
Creates a b-surface sheet body.  The surface periodicity information is
based on knot sequence and pole data.  If necessary, an illegal knot
sequence and/or pole array is modified so that the sheet can be created.
The knot_fixup and pole_fixup flags signal if a modification was made.

A knot sequence gets fixed if one or more knot values has a
multiplicity greater than the degree of the surface. This means that
the surface contained rows of patches having zero width. The removal
of zero-width patches does not affect the shape of the surface.
The pole array gets fixed if it is found to have poles that are too close
together for the system to handle. The poles are either moved
together to make them coincident or spread apart slightly.

Environment: Internal  and  External
See Also:
 UF_MODL_create_spline
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_bsurf(
int nu ,/* <I>
        Number of poles in u direction
        */
int nv ,/* <I>
        Number of poles in v direction
        */
int ku ,/* <I>
        Order in u direction
        */
int kv ,/* <I>
        Order in v direction
        */
double  u_knot[] ,/* <I>
                 Knot sequence in u direction
                 */
double  v_knot[] ,/* <I>
                 Knot sequence in v direction
                 */
double poles[],/* <I>
                Array of homogeneous poles (wx,wy,wz,w) data for
                row n immediately follows row n-1 in the array. i.e.
                poles for:
                row 1 = (1,1:ip1)
                row 2 = (1,ip1+1:2*ip1)
                row n = (1,(n-1*ip1+1:n*ip1)
                */
tag_t * bsurf_obj_id ,/* <O>
                      Object identifier for b-surface
                      */
int * knot_fixup ,/* <O>
                  Knot fixup status:
                  0 = no fixups performed
                  1 = knot sequence fixed
                  */
int * pole_fixup  /* <O>
                  Pole fixup status:
                  0 = no fixup performed
                  1 = pole array fixed
                  */
);

/******************************************************************************
Create a trimmed b-surface from surface data and 3D trimming curves.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_cre_trim_bsurf(
     int nu,         /* <I>
                     number of control vertices in u direction
                     */
     int nv,         /* <I>
                     number of control vertices in v direction
                     */
     int ku,         /* <I>
                     order in u direction
                     */
     int kv,         /* <I>
                     order in v direction
                     */
     double u_knot[], /* <I>
                     knot sequence in u direction
                     */
     double v_knot[], /* <I>
                     knot sequence in v direction
                     */
     double poles[],  /* <I>
                     array of homogeneous control vertices (wx,wy,wz,w)
                     */
     int loop_count, /* <I>
                     count of trimming loops
                     */
     int *edge_counts, /* <I,len:loop_count>
                       array holding count of edges per loop
                       */
     int *edge_senses, /* <I,len:loop_count>
                       array holding sense of edge curves (sum of edge_counts[*])
                       -1 = end to start
                        1 = start to end
                       */
     tag_t *edge_curves, /* <I,len:loop_count>
                         array holding object ids of trimming curves
                         */
     int proj_curves,  /* <I>
                       do we need to project the curves? 0=no 1=yes
                       */
     double dist_tol,  /* <I>
                       distance tolerance for use in sp-curve creation
                       */
     tag_t *bsurf_id,  /* <O>
                       object identifier for b-surface
                       */
     int *knot_fixup,  /* <O>
                       knot fixup status
                       */
     int *pole_fixup /* <O>
                       pole fixup status
                       */
);

/******************************************************************************
Create a trimmed b-surface from surface data and surface parameter curves.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_cre_2dtrim_bsurf(
     int nu,     /* <I>
                 number of control vertices in u direction
                 */
     int nv,     /* <I>
                 number of control vertices in v direction
                 */
     int ku,     /* <I>
                 order in u direction
                 */
     int kv,     /* <I>
                 order in v direction
                 */
     double u_knot[],  /* <I>
                      knot sequence in u direction
                      */
     double v_knot[],  /* <I>
                      knot sequence in v direction
                      */
     double poles[],   /* <I>
                      array of homogenous control vertices (wx,wy,wz,w)
                      */
     int loop_count,  /* <I>
                      count of trimming loops
                      */
     int *edge_counts, /* <I,len:loop_count>
                       array holding count of edges per loop
                       */
     int *edge_senses, /* <I,len:loop_count>
                       array holding sense of edge curves
                       */
     tag_t *edge_bcurves, /* <I,len:loop_count>
                          array of object ids of trimming 2D b-curves
                          in the uv domain of the b-surface */
     double edge_tol,  /* <I>
                       tolerance to attach to sp-curve edges
                       */
     tag_t *bsurf_id,  /* <O>
                       object id for b-surface
                       */
     int *knot_fixup,  /* <O>
                       knot fixup status
                       */
     int *pole_fixup /* <O>
                     pole fixup status
                     */
);
/******************************************************************************
Create the edges of a b-surface.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_bs_edges(
     int nu,  /* <I>
              number of control vertices in u direction
              */
     int nv,  /* <I>
              number of control vertices in v direction
              */
     int ku,  /* <I>
              order in u direction
              */
     int kv,  /* <I>
              order in v direction
              */
     double u_knot[], /* <I>
                     knot sequence in u direction
                     */
     double v_knot[], /* <I>
                     knot sequence in v direction
                     */
     double poles[],  /* <I>
                     array of homogenous control vertices (wx,wy,wz,w)
                     */
     int *num_loops, /* <O>
                     number of loops of curve
                     */
     int edge_counts[2], /* <O>
                       array of counts of edges per loop.  This must be declared
                       as an int edge_counts[2].
                       */
     tag_t edge_curves[4], /* <O>
                         array of b-curves.  This must be declared as a 
                         tag_t edge_curves[4].
                         */
     int *knot_fixup,    /* <O>
                         knot fixup status
                         */
     int *pole_fixup   /* <O>
                         pole fixup status
                         */
);

/******************************************************************************
Create the surface parameter curve edges of a b-surface.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_bs_2d_edges(
     int nu,  /* <I>
              number of control vertices in u direction
              */
     int nv,  /* <I>
              number of control vertices in v direction
              */
     int ku,  /* <I>
              order in u direction
              */
     int kv,  /* <I>
              order in v direction
              */
     double u_knot[], /* <I>
                     knot sequence in u direction
                     */
     double v_knot[], /* <I>
                     knot sequence in v direction
                     */
     double poles[4],  /* <I>
                     array of homogenous control vertices (wx,wy,wz,w)
                     */
     int *num_loops,    /* <O>
                        number of loops of curve
                        */
     int *edge_counts,  /* <O,len:num_loops>
                        array of counts of edges per loop
                        */
     tag_t *edge_curves, /* <O,len:num_loops>
                         array of b-curves
                         */
     int *knot_fixup,    /* <O>
                         knot fixup status
                         */
     int *pole_fixup     /* <O>
                         pole fixup status
                         */
);

/******************************************************************************
Creates a bsurface from pole and knot data. The function makes any
necessary fixes required so the bsurface is acceptable to NX
(essentially, UF_MODL_fix_bsurface_data is called).

Environment: Internal  and  External
See Also:
 UF_MODL_fix_bsurface_data
 UF_MODL_smooth_bsurface_data
Structure UF_MODL_state_t which is a type define of  UF_CURVE_state_t
History: This function was originally released in V15.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_bsurface (
UF_MODL_bsurface_p_t surface ,/* <I>
                              structure describing bsurface to create
                              */
tag_t * eid ,/* <O>
             Tag of NX bspline surface object
             */
int * num_states ,/* <O>
                  Number of states in states array
                  */
UF_MODL_state_p_t *states  /* <OF,len:num_states>
                          Array of states representing problems in the
                          bsurface; if NULL is provided no states are
                          returned.  This must be freed by calling UF_free.
                          */
);

/****************************************************************************
Creates a B-surface sheet body using the user specified creation method and
points.

Environment: Internal  and  External
See Also: 

 UF_MODL_ask_bsurf
 UF_MODL_free_bsurf_data
 UF_MODL_bsurf_row_info_t
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_bsurf_thru_pts
(
int    create_mode, /* <I>
                    Creation mode
                    = 1 -> specified points should lie on the B-surface
                    = 2 -> specified points should be used as the control
                           vertices
                    = 3 -> specified points should be used as the control
                           vertices along with using the specified weight
                           information
                    */
int    u_closed_status,  /* <I>
                         Open/closed status in u direction
                         = 0 -> open
                         = 1 -> closed
                         */
int    v_closed_status,  /* <I>
                         Open/closed status in v direction
                         = 0 -> open
                         = 1 -> closed
                         */
int    u_degree,         /* <I>
                         Degree in u direction
                         */
int    v_degree,         /* <I>
                         Degree in v direction
                         */
int    num_rows,         /* <I>
                         Number of rows of points
                         */
UF_MODL_bsurf_row_info_t *pts_info_per_row, /* <I,len:num_rows>
                                            Points information for each row.
                                            This is an array of
                                            UF_MODL_bsurf_row_info_t
                                            structures dimensioned to num_rows.
                                            */
tag_t  *bsurf_obj_id     /* <O>
                         Tag of the created B-surface
                         */
);

/******************************************************************************
Makes a bsurface continuous to cont_order_x, where x refers to the u
or v direction. The order of continuity may be any non-negative
integer up to (but not including) the corresponding degrees of the
bsurface. Selection of a given cont_order implies that all lower order
continuities are to be achieved. The order of continuity is the number
of derivatives that are required to exist at all points of the bsurface, in
the corresponding u and v directions.

NX prefers surfaces to be continuous at least to order 1, in a
manner called in this documentation G1+. It is stronger than
mathematical G1, but is not quite C1. For G1+, at any row or column
corresponding to a knot value with multiplicity equal to the degree of
the surface in that direction, both tangent vectors (with respect to u
and with respect to v) must have the same direction, but not
necessarily the same length (if they are the same length, continuity C1 exists).

At any point in the surface, if cont_order_x cannot be achieved in the
corresponding direction, the highest continuity Cn within tolerance is
achieved. If C1 cannot be achieved, G1+ is achieved within tolerance
and a state code is returned. If G1+ cannot be achieved an error is returned.

Any seam that has any angle larger than ang_toler is not smoothed, even if
it's distance is within tolerance.  Any seam that would require a change larger
than dist_toler is not smoothed.  Any seam that can be smoothed is smoothed
even all of them cannot be smoothed.

Any knot that has a multiplicity high enough to make it possible for
the surface to be discontinuous at the corresponding row or column of
poles is checked. If the row or column of poles can be treated in such
poles is checked. If the row or column of poles can be treated in such
a way as to make the surface continuous to the given orders without
changing the shape more than toler, it is made so in u and v. If the
bsurface is closed in either or both u and v, the closure is also
checked.

Continuity is achieved using a mathematical process called knot
removal.
Use this function conservatively. In particular, if simplification is to be
done when the geometry is attached or edited, use this function only if
the geometry has some problem that prevents its use. Knot removal
may make the bsurface's equivalent surface (such as a cone)
unrecognizable by the simplifier. It can also have a long running time
(at orders of continuity greater than 1), because at every point where
a change is made the surface must be evaluated to check that the
change is within tolerance.

Bsurfaces that have end knots with a multiplcity greater than the order of the
surface in that direction, or have interior knots with a multiplicity greater
than surface order-1 in the respective directions, are not continuous, that is,
they have gaps. Such bsurfaces are not of general utility in CAD/CAM work.
NX cannot create them.  This function may be used to "clean" up such
bsurfaces.

Environment: Internal  and  External
See Also:
 UF_BREP_attach_geometry
Structure UF_MODL_state_t which is a type define of  UF_CURVE_state_t
History:This function was originally released in V15.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_smooth_bsurface_data (
int cont_order_u ,/* <I>
                  order of continuity to achieve in the u direction
                  */
int cont_order_v ,/* <I>
                  order of continuity to achieve in the v direction
                  */
double dist_toler ,/* <I>
                   distance tolerance not to be exceeded
                   */
double ang_toler ,/* <I>
                  angular tolerance not to be exceeded
                  */
UF_MODL_bsurface_p_t bsurf ,/* <I>
                            spline surface data to make continuous
                            */
int * num_states ,/* <O>
                  number of states in states array
                  */
UF_MODL_state_p_t * states  /* <OF,len:num_states>
                            state values for smoothing operation; if NULL
                            is provided no states are returned.  This array
                            must be freed by calling UF_free.
                            */
);

/******************************************************************************
This function inspects the b-surface data for degeneracies. If it finds
any, it attempts to fix them by moving one or more control points. The
fixed-up data is returned in the same memory as the supplied data.

Environment: Internal  and  External
See Also:
 UF_BREP_attach_geometry
Structure UF_MODL_state_t which is a type define of  UF_CURVE_state_t
History: This function was originally released in V15.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_fix_bsurface_data (
double degen_toler ,/* <I>
                    threshold for reporting fixes: fixes less than this
                    value are not reported
                    */
UF_MODL_bsurface_p_t bsurface ,/* <I>
                               b-surface for which to remove degeneracies
                               */
int * num_states ,/* <O>
                  number of states in the states array
                  */
UF_MODL_state_p_t * states  /* <OF,len:num_states>
                            states, some of original spline, some of output
                            spline; if NULL is provided no states are
                            returned.  This must be freed by calling UF_free.
                            */
);

/****************************************************************************
Returns the B-surface data associated with the input face or the body
(with a single face) tag.  The underlying data in this structure should be 
freed by calling UF_MODL_free_bsurf_data.

Note: The valid face types are UF_MODL_PARAMETRIC_FACE and UF_MODL_OFFSET_FACE.
All the other types do not have any bsurface data.

Environment: Internal  and  External
See Also: 

 UF_MODL_create_bsurf_thru_pts
 UF_MODL_free_bsurf_data
 UF_MODL_ask_face_type
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_bsurf
(
   tag_t                  face,   /* <I>
                                  Face or body (with a single face) tag being 
                                  inquired.  Only face types
                                  UF_MODL_PARAMETRIC_FACE and UF_MODL_OFFSET_FACE
                                  will have any bsurface data.
                                  */
   UF_MODL_bsurface_p_t   bsurf   /* <O,free:UF_MODL_free_bsurf_data>
                                  Returned B-surface information.  The user
                                  should allocate a UF_MODL_bsurface_t structure
                                  and pass in a pointer to this structure.  This
                                  routine will fill this structure with
                                  dynamically allocated data.  This must be
                                  freed by calling UF_MODL_free_bsurf_data.
                                  */
);

/****************************************************************************
Returns the B-surface data associated with the input face or the body
(with a single face) tag.  The underlying data in this structure should be
freed by calling UF_MODL_free_bsurf_data.

Note: This function support all face types

Environment: Internal  and  External
See Also:

 UF_MODL_create_bsurf_thru_pts
 UF_MODL_free_bsurf_data
 UF_MODL_ask_face_type
History: Originally released in NX5
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_2dtrim_bsurf
(
   tag_t               face,    /* <I>
                                  Face or body (with a single face) tag being
                                  inquired.  for all face types
                                */

   int                 opts[4], /* <I>
                                  Convert options.
                                     [0] - cubic degree           (  N/A  )
                                     [1] - non rational           (  N/A  )
                                     [2] - non periodic           ( 1-yes, 0-no )
                                     [3] - normalize parameter    ( 1-yes, 0-no )
                                */

   double            tolerance, /* <I>
                                  Tolerance for convert B-surface and the
                                  2D-trimming-curves.
                                */

   UF_MODL_bsurface_p_t bsurf,  /* <O>
                                  Returned B-surface information.  The user
                                  should allocate a UF_MODL_bsurface_t structure
                                  and pass in a pointer to this structure.  This
                                  routine will fill this structure with
                                  dynamically allocated data.  This must be
                                  freed by calling UF_MODL_free_bsurf_data.
                                */

   int            *loop_count,  /* <O>
                                  Number of trimming loops.
                                */

   int            **edge_count, /* <OF>
                                  Array for edge count in each loop.
                                  This should be freed by calling the UF_free. 
                                */

   int            **edge_sense, /* <OF>
                                  Array for edge sense of each edge curve.
                                  This should be freed by calling the UF_free.
                                */

   tag_t          **edge_bcurves/* <OF>
                                  Array for 2D-trimming curve ID.
                                  All temporary curves must be deleted
                                  before the array can be freed by a UF_free call.
                                */
);


/****************************************************************************
Frees the B-surface data.

Environment: Internal  and  External
See Also: 

 UF_MODL_create_bsurf_thru_pts
 UF_MODL_ask_bsurf
History: Originally released in V16.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_free_bsurf_data
(
   UF_MODL_bsurface_p_t   bsurf   /* <I>
                                  B-surf data to be freed
                                  */
);

/****************************************************************************
Replace the b_surface data of entity face_eid with the new data stored in 
bsurf.  The calling function needs to make an update call to update all
the changes. This routine doesn't handle periodic surface yet and works
only on single face sheet body.


Environment: Internal  and  External

 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_bsurf (
    tag_t face_eid,               /* <I>
                                  Target surface to be edited.
                                  */

    UF_MODL_bsurface_p_t   bsurf  /* <I>
                                  New geometry to be applied to target surface.
                                  */
);

/****************************************************************************
 Set the B-surface pole flag.
 
 Environment: Internal  and  External
 History: Originally released in NX2.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_set_bsurf_pole_display(
   tag_t      face,    /* <I> Face tag of B-surface to be set pole flag */
   logical    state    /* <I> surface pole flag status */
);

/****************************************************************************
 Get the B-surface pole flag.

 Environment: Internal  and  External
 History: Originally released in NX2.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_bsurf_pole_display(
   tag_t      face,    /* <I> Face tag being inquired */
   logical    *state   /* <O> Returned B-surface pole flag information */
);

/****************************************************************************
 Set the B-surface knot flag.
 
 Environment: Internal  and  External
 History: Originally released in NX5.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_set_bsurf_knot_display(
   tag_t      face,    /* <I> Face tag of B-surface to be set pole flag */
   logical    state    /* <I> surface knot flag status */
);

/****************************************************************************
 Get the B-surface knot flag.

 Environment: Internal  and  External
 History: Originally released in NX5.0
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_bsurf_knot_display(
   tag_t      face,    /* <I> Face tag being inquired */
   logical    *state   /* <O> Returned B-surface knot flag information */
);
#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_BSURF_H_INCLUDED */
