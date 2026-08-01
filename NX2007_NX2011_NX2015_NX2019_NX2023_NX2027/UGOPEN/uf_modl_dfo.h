/***************************************************************************************************

                    Copyright (c) 2000-2002 Unigraphics Solutions Inc. 
                             Unpublished - All rights reserved
====================================================================================================



File description:

    APIs of Direct Modeling / Constrain_Face project

***************************************************************************************************/

#ifndef UF_MODL_DFO_H_INCLUDED
#define UF_MODL_DFO_H_INCLUDED

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/* constraint types are defined as below */
enum UF_MODL_dfo_constraint_type_e
{
   UF_distance_dim,                 /* Distance Constraint */
   UF_angle_dim,                    /* Angle Constraint */
   UF_coincident,                   /* Coincident Constraint */
   UF_parallel_con,                 /* Parallel Constraint */
   UF_perpen_con,                   /* Perpendicular Constraint */
   UF_tangent_con                   /* Tangent Constraint */
};
typedef enum UF_MODL_dfo_constraint_type_e UF_MODL_dfo_constraint_type_t;


/* Faces that will be operated by a Direct Modeling operations are defined in the following UF_MODL_dfo_region_t structure. 
"boundary_faces" are optional, and you may specify more than one seed faces.  If there is no boundary faces,
the seed faces will be processed. Otherwise, the extracted region between the first seed face and boundary
faces, as well as other seed faces, will be operated.

All blends adjacent to the extracted region will be automatically recognized. If users want to, in purpose, treat some of them as not blends, 
they can store these faces in the "excluded_faces" array. This is however not encouraged.

For sheet body, the region cannot be faces on the sheet body boundary.
*/

struct UF_MODL_dfo_region_s
{
   tag_t            *seed_faces;        /* <len:num_seed> seed faces */
   int               num_seed;          /* number of seed faces */
   tag_t            *boundary_faces;    /* <len:num_boundary> boundary faces, optional */
   int               num_boundary;      /* number of boundary faces. 0 if no boundary faces */
   tag_t            *excluded_faces;    /* <len:num_exclude> faces which shouldn't be treated as Blends, and must be kept invariant */
   int               num_exclude;       /* number of excluded faces */
};
typedef struct UF_MODL_dfo_region_s
               UF_MODL_dfo_region_t, *UF_MODL_dfo_region_p_t;


/* Constraint data is represented as below. Generally, constraints are defined by a target face ("from_face") and a reference ("to_object").
   Target Face is one of the faces defined by UF_MODL_dfo_region_t. Constraint reference can be face, edge, line, datum plane, datum axis, etc., 
   and and it is always abstracted as a direction and a point, thus the input 'to_object' should be a smart direction based
   on an underlying entity (see uf_so.h). Some constraint types, such as angle, parallel, perpendicular and tangent, will
   need a smart point to control the result, namely, "thru_point", which specifies that the destination of the target face
   will pass through some point.*/

struct UF_MODL_dfo_constraint_s
{
   UF_MODL_dfo_constraint_type_t type;
   tag_t                         from_face;  /* target face */
   tag_t                         to_object;  /* constraint reference. smart direction is needed*/
   tag_t                         thru_point; /* through point. smart point is needed */
   char                          value [ UF_MAX_EXP_BUFSIZE ];    /* <len:UF_MAX_EXP_BUFSIZE> distance or angle value. Any expression string. */
};
typedef struct UF_MODL_dfo_constraint_s
               UF_MODL_dfo_constraint_t, *UF_MODL_dfo_constraint_p_t;

/* Define the local scale types which should correspond 
   to the following three types that can be created through interactive NX
*/
typedef enum
{
   UF_LSCALE_TYPE_UNIFORM = 0,      /* uniform scale */
   UF_LSCALE_TYPE_AXISYMMETRIC,     /* axis symmetric scale  */
   UF_LSCALE_TYPE_GENERAL           /* general scale */

} UF_MODL_dfo_scale_type_t, *UF_MODL_dfo_scale_type_p_t;

/* This is the transformation types supported by feature Move_Region. */
typedef enum
{
   UF_TRANSF_POINT_POINT = 0,       /* translate from point to point */
   UF_TRANSF_DIRECTION_DISTANCE,    /* translate by direction and distance */
   UF_TRANSF_AXIS_ANGLE,            /* rotate by axis and angle */
   UF_TRANSF_AXIS_AXIS              /* rotate from axis to axis */

} UF_MODL_transform_type_t, *UF_MODL_transform_type_p_t;


/* The translation from point to point */

struct UF_MODL_transf_pp_s 
{
    tag_t     from_point;
    tag_t     to_point;
};
typedef struct UF_MODL_transf_pp_s 
               UF_MODL_transf_pp_t, *UF_MODL_transf_pp_p_t;

/* Translation along a direction */
struct UF_MODL_transf_dist_s
{
    tag_t     so_dirr;
    char      dist[ UF_MAX_EXP_BUFSIZE ];
};
typedef struct UF_MODL_transf_dist_s
               UF_MODL_transf_dist_t, *UF_MODL_transf_dist_p_t;

/* Rotation about axis */
struct UF_MODL_transf_angle_s
{
    tag_t     so_dirr;
    tag_t     so_point;         /* optional */
    char      angle [ UF_MAX_EXP_BUFSIZE ];
};
typedef struct UF_MODL_transf_angle_s 
               UF_MODL_transf_angle_t, *UF_MODL_transf_angle_p_t;


/* Rotation from axis to axis */
struct UF_MODL_transf_aa_s
{
    tag_t     from_dirr;
    tag_t     to_dirr;
    tag_t     pivot_point;         /* optional */
};
typedef struct UF_MODL_transf_aa_s
               UF_MODL_transf_aa_t, *UF_MODL_transf_aa_p_t;

struct UF_MODL_reblend_face_s
{
    logical   chained;                   /* a face is chained or not */
    int       n_faces;                   /* number of selected faces of a chain */
    tag_t     *faces_eid;                /* <len:n_faces> EIDs of selected faces of a chain */
};
typedef struct UF_MODL_reblend_face_s
               UF_MODL_reblend_chain_t, *UF_MODL_reblend_chain_p_t;

struct UF_MODL_reblend_face_data_s
{
    int num_chains;                      /* number of selected chains */  
    char radius[ UF_MAX_EXP_BUFSIZE ];      /* <len:UF_MAX_EXP_BUFSIZE> reblend radius */
    UF_MODL_reblend_chain_p_t chain_data;/* <len:num_chains> chain data of selected faces */
};
typedef struct UF_MODL_reblend_face_data_s
               UF_MODL_reblend_face_data_t, *UF_MODL_reblend_face_data_p_t;





/************************* UFUN prototypes **********************************/

/**************  CONSTRAIN_FACE *********************************************/

/*************************************************************************
Create a face constraint

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_face_constraint
(
 UF_MODL_dfo_region_p_t         region,           /* <I> faces to be operated */
 UF_MODL_dfo_constraint_p_t     constraint,      /*  <I> constraints imposed on the region. */
 tag_t                         *feature_tag      /*  <O> feature_tag created by the operation. */
);


/***************************************************************************     

This function edits a face constraint with new parameters.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_face_constraint
(
 tag_t                          feature_tag,      /* <I>  feature_tag to be edited */
 UF_MODL_dfo_region_p_t         region,           /* <I> faces to be operated */
 UF_MODL_dfo_constraint_p_t     constraint    /* <I> constraints imposed on the region. */
);


/***************************************************************************     

This function ask the parameters of a face constraint.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_face_constraint
(
 tag_t                          feature_tag,     /* <I>  feature_tag. */
 UF_MODL_dfo_region_t           **region,         /* <OF> faces to be operated */
 UF_MODL_dfo_constraint_t       **constraint      /* <OF> constraints imposed on the region. */
);

/*********************  RESIZE_FACE FEATURE *************************************/

/*************************************************************************
This function changes the size of a set of cylindrical/spherical/conic faces.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_resize_face
( 
    tag_t       *target_faces,     /* <I,len:num_target>
                                          faces to be operated */ 
    int          num_target,       /* <I> number of faces */ 
    tag_t       *non_blend_faces,  /* <I,len:num_non_blend>
                                          adjacent tangent faces which are not blends */ 
    int          num_non_blend,    /* <I> number of non-blend faces */ 
    char        *new_parameter,    /* <I> new diameter for cylindrical/spherical faces, 
                                                         or half angle */ 
    tag_t        *feature_tag  /* <O> the new feature */ 
);


/***************************************************************************     

This function edits a resize_face feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_resize_face
(
    tag_t     feature_tag,       /* <I> the feature */ 
    tag_t    *target_faces,      /* <I,len:num_target>
                                        faces to be operated, NULL if won't change */ 
    int       num_target,        /* <I> number of faces, 0 if won't change */ 
    tag_t    *non_blend_faces,   /* <I,len:num_non_blend>
                                        adjacent tangent faces which are not blends, 
                                        NULL if won't change */ 
    int       num_non_blend,     /* <I> number of non-blend faces, 0 if won't change  */ 
    char     *new_parameter      /* <I> new diameter for cylindrical/spherical faces, 
                                        or half  angle */ 
);


/***************************************************************************     

This function ask the parameters of a resize_face feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_resize_face
(
    tag_t      feature_tag,        /* <I>  the feature */ 
    tag_t    **target_faces,       /* <OF,len:num_target> - target faces */ 
    int       *num_target,         /* <O>  number of faces */ 
    tag_t    **non_blend_faces,    /* <OF,len:num_non_blend> num_non_blend
                                           adjacent tangent faces which are not blends */ 
    int       *num_non_blend,      /* <O>  number of non-blend faces */ 
    char     **parameter           /* <OF>  diameter for cylindrical/spherical faces, 
                                           or half  angle */ 
);



/*********************  REPLACE_FACE FEATURE *************************************/

/*************************************************************************
This function replaces the surface data of target faces with that of a tool face.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_replace_face
(
    tag_t    *target_faces,      /* <I,len:num_target>
                                        target faces */ 
    int       num_target,        /* <I> number of faces */ 
    tag_t    *non_blend_faces,   /* <I,len:num_non_blend>
                                        adjacent tangent faces which are not blends */ 
    int       num_non_blend,     /* <I> number of non-blend faces */ 
    tag_t     tool_face,         /* <I> tool face */ 
    logical   reverse_direction, /* <I> reverse direction of the tool face or not */
    tag_t    *feature_tag        /* <O> feature_tag created by the operation. */ 
);


/***************************************************************************     

This function edits a replace_face feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_replace_face
(
    tag_t     feature_tag,       /* <I> the feature */ 
    tag_t    *target_faces,      /* <I,len:num_target>
                                        faces to be operated, NULL if won't change */ 
    int       num_target,        /* <I> number of faces, 0 if won't change */ 
    tag_t    *non_blend_faces,   /* <I,len:num_non_blend>
                                        adjacent tangent faces which are not blends, 
                                        NULL if won't change */ 
    int       num_non_blend,     /* <I> number of non-blend faces, 0 if won't change  */ 
    tag_t     tool_face,         /* <I> tool face */ 
    logical   reverse_direction  /* <I> reverse direction of the tool face or not */
);


/***************************************************************************     

This function ask the parameters of a replace_face feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_replace_face
(
    tag_t      feature_tag,        /* <I>  the feature */ 
    tag_t    **target_faces,       /* <OF,len:num_target> target faces */ 
    int       *num_target,         /* <O>  number of faces */ 
    tag_t    **non_blend_faces,    /* <OF,len:num_non_blend> 
                                          adjacent tangent faces which are not blends */ 
    int       *num_non_blend,      /* <O>  number of non-blend faces */ 
    tag_t     *tool_face,          /* <O>  tool face */ 
    logical   *reverse_direction   /* <O> reverse direction of the tool face or not */

);


/************************  OFFSET_REGION *****************************************/

/*************************************************************************
This function offset a region by a given distance along face normals.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_offset_region
(
    UF_MODL_dfo_region_p_t      region,     /* <I> faces to be operated */
    char                       *offset,     /* <I> offset value, in expression string */
    tag_t                      *feature_tag /* <O> feature_tag created by the operation. */
);


/***************************************************************************     

This function edits an offset_region feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_offset_region
(
    tag_t                          feature_tag,   /* <I> feature_tag to be edited */
    UF_MODL_dfo_region_p_t         region,        /* <I> faces to be operated */
    char                          *offset         /* <I> offset value, in expression string */
);


/***************************************************************************     

This function ask the parameters of a offset_region.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_offset_region
(
    tag_t                         feature_tag,    /* <I>  feature_tag. */
    UF_MODL_dfo_region_t        **region,         /* <OF> faces to be operated */
    char                        **offset          /* <OF> offset value, in expression string */
);



/************************  PATTERN_FACE *****************************************/

/*************************************************************************
This function create rectangular patterns for a given set of faces.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_rectangular_pattern_face
(
    UF_MODL_dfo_region_p_t      region,        /* <I> region*/ 
    tag_t                       x_axis,        /* <I> x-axis to define offset */
    tag_t                       y_axis,        /* <I> y-axis */
    int                         num_x,         /* <I> number along XC */ 
    int                         num_y,         /* <I> number along YC, only for type==0 */ 
    char                       *x_offset,      /* <I> offset along XC*/ 
    char                       *y_offset,      /* <I> offset along YC */ 
    tag_t                      *feature_tag    /* <O> the new feature */ 
); 


/***************************************************************************     

This function edits a rectangular pattern_face feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_rectangular_pattern_face
(
    tag_t                       feature_tag,   /* <I> the feature */ 
    UF_MODL_dfo_region_p_t      region,        /* <I> region*/ 
    tag_t                       x_axis,        /* <I> x-axis to define offset */
    tag_t                       y_axis,        /* <I> y-axis */
    int                         num_x,         /* <I> number along XC */ 
    int                         num_y,         /* <I> number along YC, only for type==0 */ 
    char                       *x_offset,      /* <I> offset along XC*/ 
    char                       *y_offset       /* <I> offset along YC */ 
);


/***************************************************************************     

This function returns the parameters of a rectangular pattern_face.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rectangular_pattern_face
(
    tag_t                       feature_tag,   /* <I> the feature */ 
    UF_MODL_dfo_region_p_t     *region,        /* <OF> region*/ 
    tag_t                      *x_axis,        /* <O> X-Axis */
    tag_t                      *axis,          /* <O> Y-Axis */
    int                        *num_x,         /* <O> number along XC */ 
    int                        *num_y,         /* <O> number along YC */
    char                      **x_offset,      /* <OF>offset along XC */
    char                      **y_offset       /* <OF>offset along YC */
);


/*************************************************************************
This function create circular patterns for a given set of faces.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_circular_pattern_face
(
    UF_MODL_dfo_region_p_t      region,        /* <I> region*/ 
    tag_t                       axis,          /* <I> center axis to define pattern */
    int                         n_pattern,     /* <I> number of patterns */ 
    char                       *angle,         /* <I> angle between patterns*/ 
    tag_t                      *feature_tag    /* <O> the new feature */ 
); 


/***************************************************************************     

This function edits a circular pattern_face feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_circular_pattern_face
(
    tag_t                       feature_tag,   /* <I> the feature */ 
    UF_MODL_dfo_region_p_t      region,        /* <I> region*/ 
    tag_t                       axis,          /* <I> center axis to define pattern */
    int                         n_pattern,     /* <I> number of patterns */ 
    char                       *angle         /* <I> angle between patterns*/ 
);


/***************************************************************************     

This function returns the parameters of a circular pattern_face.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_circular_pattern_face
(
    tag_t                       feature_tag,   /* <I> the feature */ 
    UF_MODL_dfo_region_p_t     *region,        /* <OF> region*/ 
    tag_t                      *axis,          /* <O> axis to define pattern */
    int                        *n_pattern,     /* <O> pattern number */ 
    char                      **angle          /* <OF>angle between instance */
);

/*************************************************************************
This function create mirror for a given set of faces.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_mirror_pattern_face
(
    UF_MODL_dfo_region_p_t      region,        /* <I> region*/ 
    tag_t                       mirror_plane,  /* <I> mirror plane */
    tag_t                      *feature_tag    /* <O> the new feature */ 
); 


/***************************************************************************     

This function edits a mirror pattern_face feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_mirror_pattern_face
(
    tag_t                       feature_tag,   /* <I> the feature */ 
    UF_MODL_dfo_region_p_t      region,        /* <I> region*/ 
    tag_t                       mirror_plane  /* <I> mirror plane */
);


/***************************************************************************     

This function returns the parameters of a mirror pattern_face.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_mirror_pattern_face
(
    tag_t                       feature_tag,   /* <I> the feature */ 
    UF_MODL_dfo_region_p_t     *region,        /* <OF> region*/ 
    tag_t                      *mirror_plane   /* <O>  mirror plane */
);

/*************************************************************************
This function performs a local scale

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_local_scale
(
    UF_MODL_dfo_scale_type_t type,      /* <I> local scale type */
    UF_MODL_dfo_region_p_t region,      /* <I> faces to be operated */
    tag_t                  so_point,    /* <I> smart point */
    tag_t                  so_dir,      /* <I> smart direction */
    tag_t                  so_csys,     /* <I> smart coordinate system */
    char factors[3][ UF_MAX_EXP_BUFSIZE ], /* <I,len:UF_MAX_EXP_BUFSIZE> scale factors */
    tag_t                  *feature_tag /* <O> Feature object identifier 
                                               of a created local scale */
);

/***************************************************************
This function inquires the parameters of a local scale feature

Environment : Internal  and  External
See Also:
History:
****************************************************************/
extern UFUNEXPORT int UF_MODL_ask_local_scale 
( 
    tag_t feature_tag,                /* <I> feature object identifier of a scale */
    UF_MODL_dfo_scale_type_t * type,  /* <O> scale type */
    UF_MODL_dfo_region_t **region,    /* <OF>faces to be operated */
    tag_t *so_point,                  /* <O> smart point */ 
    tag_t *so_dir,                    /* <O> smart direction */
    tag_t *so_csys,                   /* <O> smart coordinate system */
    char  factor[3][ UF_MAX_EXP_BUFSIZE ]/* <O> scale factors */
);

/***************************************************************************     
This function edits a local scale feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_local_scale
(
    tag_t                  feature_tag,   /* <I> feature_tag to be edited */
    UF_MODL_dfo_scale_type_t type,        /* <I> scale type */
    UF_MODL_dfo_region_p_t region,        /* <I> faces to be operated */
    tag_t                  so_point,      /* <I> smart point */
    tag_t                  so_dir,        /* <I> smart direction */
    tag_t                  so_csys,       /* <I> smart coordinate system */
    char factors[3][ UF_MAX_EXP_BUFSIZE ]    /* <I,len:UF_MAX_EXP_BUFSIZE> scale factors */
);



/*************************************************************************
This function moves a set of faces by given transformation

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_move_region
(
    UF_MODL_transform_type_t type,           /* <I> transformation type */
    UF_MODL_dfo_region_p_t   region,         /* <I> faces to be operated */
    void                    *transf_data,    /* <I> transformation data, can be of following types:
                                                UF_MODL_transf_pp_p_t  - point to point translation
                                                UF_MODL_transf_dist_p_t - translation along direction
                                                UF_MODL_transf_angle_p_t - rotation about axis
                                                UF_MODL_transf_aa_p_t - rotation between two axes
                                                */
    tag_t                  *feature_tag      /* <O> Feature tag */
);

/***************************************************************
This function inquires the parameters of a move_region feature.

Environment : Internal  and  External
See Also:
History:
****************************************************************/
extern UFUNEXPORT int UF_MODL_ask_move_region
( 
    tag_t                          feature_tag,  /* <I> feature tag */
    UF_MODL_transform_type_t      *type,         /* <O> scale type */
    UF_MODL_dfo_region_p_t        *region,       /* <OF>faces to be operated */
    void                         **transf_data   /* <OF>transformation data */
);

/***************************************************************************     
This function edits a move_region feature.

Environment : Internal  and  External
See Also:
History:
***************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_move_region
(
    tag_t                    feature_tag,    /* <I> feature tag to be edited */
    UF_MODL_transform_type_t type,           /* <I> transformation type */
    UF_MODL_dfo_region_p_t   region,         /* <I> faces to be operated */
    void                    *transf_data     /* <I> transformation data, can be of following types:
                                                UF_MODL_transf_pp_p_t  - point to point translation
                                                UF_MODL_transf_dist_p_t - translation along direction
                                                UF_MODL_transf_angle_p_t - rotation about axis
                                                UF_MODL_transf_aa_p_t - rotation between two axes
                                                */
);

/*************************************************************************
Create a reblend face feature

Environment : Internal  and  External
See Also:
History: V19 release
***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_reblend_face
(
    UF_MODL_reblend_face_data_p_t reblend_data, /* <I> 
                                                   User defining reblend data
                                                */
    tag_t *reblend_eid                          /* <O>
                                                   Feature object identifier of 
                                                   a created reblend face feature
                                                */  
);

/********************************************************************
Ask a reblend face feature data

Environment: Internal  and  External
See Also:
History: V19 release
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_reblend_face
(   
    tag_t feature_eid,                         /* <I> 
                                                  Feature object identifier of a created reblend face
                                               */
    UF_MODL_reblend_face_data_p_t reblend_data /* <OF>
                                                  Data describing the created reblend face feature
                                               */
);

/********************************************************************
Edit a reblend face feature data

Environment: Internal  and  External
See Also:
History: V19 release
********************************************************************/
extern UFUNEXPORT int UF_MODL_edit_reblend_face
(   
    tag_t feature_eid,                        /* <I> 
                                                 Feature object identifier of a created reblend face
                                              */
    UF_MODL_reblend_face_data_p_t reblend_data /* <I>
                                                  User defining reblend face feature data
                                               */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_MODL_DFO_H_INCLUDED */
