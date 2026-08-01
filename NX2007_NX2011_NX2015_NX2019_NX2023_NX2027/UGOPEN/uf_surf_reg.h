/*****************************************************************************

             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File description:

Open C API interface to manipulate the different surface region feature types.
This allows you to create the feature, edit the feature, inquire the
current parameters of the feature and inquire the type of surface region.

******************************************************************************/

/* Do not process this file again if already included */
#ifndef UF_SURF_REG_H_INCLUDED
#define UF_SURF_REG_H_INCLUDED

/*****************************************************************************

******************************************************************************/

/**************************************************************************
 *
 *   Include files necessary for UF_SURF_REG feature definition
 *
 **************************************************************************/
#include <uf_defs.h>
#include <libufun_cam_exports.h>
/*****************************************************************************

******************************************************************************/
#define ERROR_UF_SURF_REG_base 1925000

#ifdef __cplusplus
extern "C" {
#endif


/**************************************************************************
 *
 *    UF_SURF_REG data definitions (#defines, enums, typedefs, etc.)
 *
 **************************************************************************/
/* UF_SURF_REG error codes */
#define UF_SURF_REG_err_invalid_name       ERROR_UF_SURF_REG_base + 0
#define UF_SURF_REG_err_face_not_on_body   ERROR_UF_SURF_REG_base + 1
#define UF_SURF_REG_err_unsupp_alg_version ERROR_UF_SURF_REG_base + 2

/* The different methods that can be used to create a surface region feature.
   This also indicates which structure is being used for the union parameter
   data structure.
*/
enum UF_SURF_REG_type_e
{
    UF_SURF_REG_SEED = 1,  /* Surface region from the seed face and boundary
                              faces. */
    UF_SURF_REG_ALL_FACES_OF_BODY, /* Surface region from all faces of the
                                      body. */
    UF_SURF_REG_EXPLICIT_FACES, /* Surface region from explicit faces on a
                                   body. */
    UF_SURF_REG_STEEP           /* Surface region gathered from either the
                                   steep or non-steep faces of a body. */
}  ;
typedef enum UF_SURF_REG_type_e UF_SURF_REG_type_t, *UF_SURF_REG_type_p_t;

/* The parameters for defining the seed surface region feature.  Boundary faces
    and/or tangential edge expression can be used to limit the region.
*/
struct UF_SURF_REG_seed_s
{
    char  *name;              /* Optional name of feature */
    tag_t seed_face;          /* The seed face of the body */
    tag_t *boundary_faces;    /* Array of boundary faces or NULL if not used */
    int   bnd_face_count;     /* Number of faces in boundary array */
    int   traverse_holes;     /* Flag whether to traverse interior holes */
    char  *tang_edge_str;     /* String value of the tangential edge
                                 expression or NULL if not used. */
    int   update_after_body;  /* Flag to indicate when to update.  Set this
                                 to 1 to update after the body, set it to
                                 0 to update at the time stamp. */
}  ;
typedef struct UF_SURF_REG_seed_s UF_SURF_REG_seed_t, *UF_SURF_REG_seed_p_t;


/* The parameters for defining all faces of a body surface region feature. */
struct UF_SURF_REG_all_faces_s
{
    char  *name;                /* Optional name of feature */
    tag_t body;                 /* The target body used to create the feature */
    int update_after_body;      /* Flag to indicate when to update.  Set this
                                   to 1 to update after the body, set it to
                                   0 to update at the time stamp. */
}  ;
typedef struct UF_SURF_REG_all_faces_s  UF_SURF_REG_all_faces_t,
               *UF_SURF_REG_all_faces_p_t;

/* The parameters for defining explicit faces of a body, surface region feature.
*/
struct UF_SURF_REG_explicit_s
{
    char  *name;                /* Optional name of feature */
    tag_t *feature_faces;       /* Array of faces on the body */
    int   face_count;           /* Number of faces in the array */
    int update_after_body;      /* Flag to indicate when to update.  Set this
                                   to 1 to update after the body, set it to
                                   0 to update at the time stamp. */
}  ;
typedef struct UF_SURF_REG_explicit_s UF_SURF_REG_explicit_t,
               *UF_SURF_REG_explicit_p_t;

/* The parameters for defining the steep surface region feature.
   Uses the subdiv_isocline feature to actually apply the splitting
   of the faces on the body. See uf_subdiv.h for more information.
*/
struct UF_SURF_REG_steep_s
{
    char  *name;                /* Optional name of feature */
    tag_t body;                 /* The target body used to create the feature */
    tag_t *subdiv_isocline;     /* An array subdiv isocline features that
                                   were applied to the body.(Currently only 1)*/
    int   sub_iso_count;        /* Number of subdiv isocline features. */
    logical steep_faces;        /* Whether to gather steep or nonsteep faces */
    int update_after_body;      /* Flag to indicate when to update.  Set this
                                   to 0 to update at the time stamp. */
    int   version_number;       /* Current version must be 1 */
}  ;
typedef struct UF_SURF_REG_steep_s UF_SURF_REG_steep_t, *UF_SURF_REG_steep_p_t;


union UF_SURF_REG_data_structures_t
{
    UF_SURF_REG_seed_p_t      surf_reg_type1;
    UF_SURF_REG_all_faces_p_t surf_reg_type2;
    UF_SURF_REG_explicit_p_t  surf_reg_type3;
    UF_SURF_REG_steep_p_t     surf_reg_type4;
} ;
typedef union UF_SURF_REG_data_structures_t UF_SURF_REG_data_structures_u,
              *UF_SURF_REG_data_structures_p_u;

/************************************************************************
 *
 *   UF_SURF_REG function interface
 *
 ************************************************************************/

/************************************************************************
Creates a surface region feature. It uses one of the following defining types:
 - gather faces on a body using a seed face and limiting progression by
   boundary faces and-or tangential edge angle.
 - all faces on the body.
 - explicitly selected faces on a body.
 - gather the steep or non-steep faces on a body.

Return:
    UF_SURF_REG_err_invalid_name
    UF_SURF_REG_err_face_not_on_body

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
***********************************************************************/
extern UFUN_CAMEXPORT int UF_SURF_REG_create(
UF_SURF_REG_type_t surf_reg_type ,/* <I>
                                  Type of Surface Region
                                  */
UF_SURF_REG_data_structures_p_u surf_reg_struct_ptr ,/* <I>
                                                     Pointer to one of the surf
                                                     reg data structures.
                                                     */
tag_p_t surf_reg_tag  /* <O>
                      Object identifier of the surface region feature.
                      */
);

/***********************************************************************
Edits a surface region feature.  The "surf_reg_type" contains the type of
surface region feature being edited. It indicates the type of parameters used
in the "surf_reg_struct_ptr" structure.

Return:
    UF_SURF_REG_err_invalid_name
    UF_SURF_REG_err_face_not_on_body

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
**********************************************************************/
extern UFUN_CAMEXPORT int UF_SURF_REG_edit(
UF_SURF_REG_type_t surf_reg_type ,/* <I>
                                  Type of Surface Region
                                  */
UF_SURF_REG_data_structures_p_u surf_reg_struct_ptr ,/* <I>
                                                     Pointer to one of the
                                                     surface region data
                                                     structures.
                                                     */
tag_t surf_reg_tag  /* <I>
                    Object identifier of the surface region feature.
                    */
);

/**************************************************************************
Gets the parameters used for a surface region feature.
Given a surface region tag, determines the surf_reg_type and the
parameters for the given type in the surf_reg_struct_ptr structure.
See UF_SURF_REG_free for freeing the data structures allocated by
this routine.

Environment: surf_reg_type

See Also:

History: Original release was in V14.0.
*************************************************************************/
extern UFUN_CAMEXPORT int UF_SURF_REG_ask_parms(
tag_t surf_reg_tag ,/* <I>
                    Object identifier of the surface region feature.
                    */
UF_SURF_REG_type_p_t surf_reg_type ,/* <O>
                                    Type of Surface Region
                                    */
UF_SURF_REG_data_structures_p_u surf_reg_struct_ptr  /* <OF,free:UF_SURF_REG_free>
                                                     Pointer to one of the surf
                                                     reg data structures. Use
                                                     UF_SURF_REG_free to
                                                     deallocate memory when
                                                     done.
                                                     */
);

/***************************************************************************
Free the space allocated to a UF_SURF_REG_data_structures_p_u stucture.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
**************************************************************************/
extern UFUN_CAMEXPORT int UF_SURF_REG_free(
UF_SURF_REG_type_t surf_reg_type ,/* <I>
                                  Type of Surface Region
                                  */
UF_SURF_REG_data_structures_p_u surf_reg_struct_ptr  /* <I>
                                                     Pointer to one of the surf
                                                     reg data structures.
                                                     */
);

/*************************************************************************
Gets the type of surface region feature.  Given a surface region tag,
determines the surf_reg_type.

Environment: Internal  and  External

See Also:

History: Original release was in V14.0.
************************************************************************/
extern UFUN_CAMEXPORT int UF_SURF_REG_ask_type(
tag_t surf_reg_tag ,/* <I>
                    Object identifier of the surface region feature.
                    */
UF_SURF_REG_type_p_t surf_reg_type  /* <O>
                                    Type of Surface Region
                                    */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_SURF_REG_H_INCLUDED */

