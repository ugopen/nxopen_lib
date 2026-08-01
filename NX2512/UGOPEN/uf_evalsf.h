/*******************************************************************************
             Copyright (c) 2002-2006  UGS Corp.
                       Unpublished - All Rights Reserved                       



File description:

Open API interface to functions that evaluate surfaces.  These functions are
the preferred way for fast evaluation of faces and underlying surfaces.

   Note that UF_EVALSF_evaluate and UF_EVALSF_evaluate_array may not properly
   handle parameter values returned by UF_EVALSF_find_closest_point or similar
   functions for surface types Blend or Trimmed B-surface.  The functions
   UF_MODL_evaluate_face or UF_MODL_ask_face_props should be called instead.

   Note - please use the new UF_EVALSF_initialize_2 to avoid above problem

*******************************************************************************/

#ifndef UF_EVALSF_H_INCLUDED
#define UF_EVALSF_H_INCLUDED

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>
#define UF_EVALSF_S EVALSF_s
/***************** Data Structure Section ************************************/

/* surface evaluation structure */
typedef struct       UF_EVALSF_S                        *UF_EVALSF_p_t;
typedef const struct UF_EVALSF_S                        *UF_EVALSF_pc_t;
typedef struct       UF_EVALSF_pos3_s UF_EVALSF_pos3_t, *UF_EVALSF_pos3_p_t;

/*
Definition for 3D position
*/
struct UF_EVALSF_pos3_s
{
    double  distance;   /* separation between surface and reference point */
    double  uv[2];      /* uv-parameter pair */
    double  pnt3[3];    /* 3D point */
};
typedef const UF_EVALSF_pos3_t UF_EVALSF_pos3_c_t, *UF_EVALSF_pos3_pc_t;

/* By reference components */
#define UF_EVALSF_pos3_UV(r)    ((r)->uv)
#define UF_EVALSF_pos3_PNT3(r)  ((r)->pnt3)
#define UF_EVALSF_pos3_U(r)     ((r)->uv[0])
#define UF_EVALSF_pos3_V(r)     ((r)->uv[1])
#define UF_EVALSF_pos3_D(r)     ((r)->distance)
#define UF_EVALSF_pos3_X(r)     ((r)->pnt3[0])
#define UF_EVALSF_pos3_Y(r)     ((r)->pnt3[1])
#define UF_EVALSF_pos3_Z(r)     ((r)->pnt3[2])
#define UF_EVALSF_pos3_LIST(r)  UF_EVALSF_pos3_U(r), UF_EVALSF_pos3_V(r), UF_EVALSF_pos3_D(r), UF_EVALSF_pos3_X(r), UF_EVALSF_pos3_Y(r), UF_EVALSF_pos3_Z(r)
/* By value components */
#define UF_EVALSF_pos3_uv(v)    ((v).uv)
#define UF_EVALSF_pos3_pnt3(v)  ((v).pnt3)
#define UF_EVALSF_pos3_u(v)     ((v).uv[0])
#define UF_EVALSF_pos3_v(v)     ((v).uv[1])
#define UF_EVALSF_pos3_d(v)     ((v).distance)
#define UF_EVALSF_pos3_x(v)     ((v).pnt3[0])
#define UF_EVALSF_pos3_y(v)     ((v).pnt3[1])
#define UF_EVALSF_pos3_z(v)     ((v).pnt3[2])
#define UF_EVALSF_pos3_list(v)  UF_EVALSF_pos3_u(v), UF_EVALSF_pos3_v(v), UF_EVALSF_pos3_d(v), UF_EVALSF_pos3_x(v), UF_EVALSF_pos3_y(v), UF_EVALSF_pos3_z(v)

/***************** Function Prototypes Section ********************************/

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Computes the u,v parameter space min, max  of a face

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_EVALSF_ask_face_uv_minmax
(
    UF_EVALSF_pc_t  evaluator,      /* <I> Address of evaluator structure */
    double          uv_min_max[4]   /* <O> [0] - umin
                                           [1] - umax
                                           [2] - vmin
                                           [3] - vmax */
);

/******************************************************************************
Returns the minimum distance parameter and point on the surface of a face
given a reference point.

The surface point is on the portion which is bounded by the edges of the face.

To find the closest point on the extended surface (not within bounding edges)
use UF_EVALSF_find_closest_point

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_EVALSF_ask_minimum_face_dist
(
    UF_EVALSF_pc_t      evaluator,  /* <I> Address of evaluator structure */
    const double        point[3],   /* <I> Given point in absolute space */
    UF_EVALSF_pos3_p_t  srf_pos3    /* <O> Address of point position on surface */
);

/******************************************************************************
Evaluates a point and the derivatives of a face at the given parameter value.

Environment: Internal  and  External
See Also:  UF_MODL_evaluate_face and UF_MODL_ask_face_props 
   Note that UF_EVALSF_evaluate may not properly handle parameter values
   returned by UF_EVALSF_find_closest_point or similar functions for
   surface types Blend or Trimmed B-surface.  The above functions should be
   called instead.
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_EVALSF_evaluate
(
    UF_EVALSF_pc_t      evaluator,  /* <I> Address of evaluator structure */
    int                 deriv_flag, /* <I>
                            order of the derivative to be computed:
                            UF_MODL_EVAL        - position
                            UF_MODL_EVAL_DERIV1 - position and 1. partial
                            UF_MODL_EVAL_DERIV2 - position, 1. and 2. partials
                            UF_MODL_EVAL_DERIV3 - position, 1., 2. and 3. partials
                            UF_MODL_EVAL_UNIT_NORMAL - position, 1. partials and 
                                                       unitized normal.
                            UF_MODL_EVAL_NORMAL - position, 1. partials and the
                                                  ununitized normal.
                            UF_MODL_EVAL_ALL - position, normals and all the partials
                                               up to the third order.
                            */
    const double            uv_pair[2], /* <I> uv-parameter pair
                                               at which derivatives are to be computed.
                                               The parameter limits for a given face can be found
                                               by calling UF_EVALSF_ask_face_uv_minmax.
                                        */
    UF_MODL_SRF_VALUE_p_t   surf_eval   /* <O> Address of evaluation result structure
                                                containing position and derivatives:
                                                srf_pos[3]      - position
                                                srf_du[3]       - d/du
                                                srf_dv[3]       - d/dv
                                                srf_unormal[3]  - unit normal
                                                srf_d2u[3]      - d2/du2
                                                srf_dudv[3]     - d2/dudv
                                                srf_d2v[3]      - d2/dv2
                                                srf_d3u[3]      - d3/du3
                                                srf_d2udv[3]    - d3/du2dv
                                                srf_dud2v[3]    - d3/dud2v
                                                srf_d3v[3]      - d3/dv3
                                                srf_normal[3]   - d/du X d/dv
                                        */
);

/******************************************************************************
Evaluates an array of points and derivatives of a face for a given array of parameter values.


Environment: Internal  and  External
See Also:  UF_MODL_evaluate_face and UF_MODL_ask_face_props 
   Note that UF_EVALSF_evaluate_array may not properly handle parameter values
   returned by UF_EVALSF_find_closest_point or similar functions for
   surface types Blend or Trimmed B-surface.  The above functions should be
   called instead.
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_EVALSF_evaluate_array
(
    UF_EVALSF_pc_t      evaluator,  /* <I> Address of evaluator structure */
    int                 deriv_flag, /* <I>
                            order of the derivative to be computed:
                            UF_MODL_EVAL        - position
                            UF_MODL_EVAL_DERIV1 - position and 1. partial
                            UF_MODL_EVAL_DERIV2 - position, 1. and 2. partials
                            UF_MODL_EVAL_DERIV3 - position, 1., 2. and 3. partials
                            UF_MODL_EVAL_UNIT_NORMAL - position, 1. partials and 
                                                       unitized normal.
                            UF_MODL_EVAL_NORMAL - position, 1. partials and the
                                                  ununitized normal.
                            UF_MODL_EVAL_ALL - position, normals and all the partials
                                               up to the third order.
                            */
    int                 num_points, /* <I> number of points to evaluate */                   
    const double        uv_pairs[], /* <I,len:num_points> num_points uv-parameter pairs
                                           The parameter limits for a given face can be found
                                           by calling UF_EVALSF_ask_face_uv_minmax.
                                    */
    UF_MODL_SRF_VALUE_t surf_evals[]/* <O,len:num_points> Address of array of evaluation results
                                    The caller must provide space of 
                                    size = sizeof(UF_MODL_SRF_VALUE_t) * num_points
                                    Each structure element contains:
                                    srf_pos[3]      - position
                                    srf_du[3]       - d/du
                                    srf_dv[3]       - d/dv
                                    srf_unormal[3]  - unit normal
                                    srf_d2u[3]      - d2/du2
                                    srf_dudv[3]     - d2/dudv
                                    srf_d2v[3]      - d2/dv2
                                    srf_d3u[3]      - d3/du3
                                    srf_d2udv[3]    - d3/du2dv
                                    srf_dud2v[3]    - d3/dud2v
                                    srf_d3v[3]      - d3/dv3
                                    srf_normal[3]   - d/du X d/dv
                                    */
);

/******************************************************************************
Finds on the surface the closest point and uv-parameter pair to a given point.

Note that the returned point will be on the underlying surface
but may not be on the portion which is bounded by the edges
of the face.

Note that in some cases, there is a potential risk that the returned point might
be adjusted incorrectly where the underlying surface has an extended UV range.
Please use UF_EVALSF_find_closest_point_2 instead.

To find the closest point within bounding edges, use
UF_EVALSF_ask_minimum_face_dist

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_EVALSF_find_closest_point
(
    UF_EVALSF_pc_t      evaluator,  /* <I> Address of evaluator structure */
    const double        point[3],   /* <I> Given point in absolute space */
    UF_EVALSF_pos3_p_t  srf_pos3    /* <O> Address of point position on surface */
);

/******************************************************************************
Finds on the surface the closest point and uv-parameter pair to a given point.

Note that the returned point will be on the underlying surface
but may not be on the portion which is bounded by the edges
of the face.

To find the closest point within bounding edges, use
UF_EVALSF_ask_minimum_face_dist

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_EVALSF_find_closest_point_2
(
    UF_EVALSF_pc_t      evaluator,  /* <I> Address of evaluator structure */
    const double        point[3],   /* <I> Given point in absolute space */
    UF_EVALSF_pos3_p_t  srf_pos3    /* <O> Address of point position on surface */
);

/******************************************************************************
Frees the evaluator of a face

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_EVALSF_free
(
    UF_EVALSF_p_t *evaluator    /* <O> address of evaluator pointer */
);

/******************************************************************************
Initializes a face evaluator structure

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_EVALSF_initialize
(
    tag_t         face_tag,  /* <I>  Object identifier of a face */
    UF_EVALSF_p_t *evaluator /* <OF,free:UF_EVALFS_free> Evaluator structure for this face.
                                     It must be freed by calling UF_EVALFS_free. */
);

/******************************************************************************
Initializes a face evaluator structure with correct parameter mapping

Environment: Internal  and  External
See Also:
History:
 *****************************************************************************/
extern UFUNEXPORT int UF_EVALSF_initialize_2
(
    tag_t         face_tag,  /* <I>  Object identifier of a face */
    UF_EVALSF_p_t *evaluator /* <OF> Evaluator structure for this face.
                                     It must be freed by calling UF_EVALFS_free. */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_EVALSF_H_INCLUDED */
