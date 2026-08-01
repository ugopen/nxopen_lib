/*
          Copyright (c) 2002-2003 Unigraphics Solutions Inc.
                 Unpublished - All rights reserved

*****************************************************************************





File description:

   Internal type definitions for UF_SF_MSHVLD (Scenario Mesh Validation)
   module.

******************************************************************************/



#ifndef UF_SF_MSHVLD_H_INCLUDED
#define UF_SF_MSHVLD_H_INCLUDED


#include <uf_sf_types.h>
#include <libufun_cae_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/**************************************************************************
 *   This enumeration allows the specification of types of mesh errors
 *   found during mesh validation.
 **************************************************************************/
enum UF_SF_mesh_error_type_e
{
UF_SF_MSHVLD_NOT_CLASSIFIED = 0,
/*  Errors have not been classified yet  */


/*  1. Mesh associativity errors  */

UF_SF_MSHVLD_MESH_NOT_ASSOCIATED_TO_MR,
/*  Meshes are not associated to mesh recipes  */

UF_SF_MSHVLD_MESH_WITH_NO_ELEM,
/*  Meshes associated to alive mesh recipes
    do not contain any element */

UF_SF_MSHVLD_MESH_WITH_DIFF_DIM_ELEM,
/*  Meshes contain elements with diff dimensions  */


/*  2. Element associativity errors  */

UF_SF_MSHVLD_INVALID_ELEM_OWNER,
/*  The owner meshes of elements are incorrectly set  */

UF_SF_MSHVLD_INVALID_ELEM_NODE_NUM,
/*  The numbers of element nodes are invalid  */


/*  3. Node associativity errors  */

UF_SF_MSHVLD_ORPHAN_NODE,
/*  Orphan nodes (with no owner elem)
    are found in scenario model  */

UF_SF_MSHVLD_INVALID_NODE_OWNER,
/*  The owner elements of nodes are invalid  */

UF_SF_MSHVLD_INVALID_CORNER_MID_NODE_ORDER,
/*  The orders of corner nodes and mid nodes are invalid  */

UF_SF_MSHVLD_NODE_NOT_ASSOCIATED_TO_MG,
/*  The nodes are not associated to any mesh geometry  */

UF_SF_MSHVLD_CORNER_MID_NODE_OVERLAP,
/*  The corner/mid nodes are set as mid/corner nodes  */

UF_SF_MSHVLD_MID_NODE_NOT_PROPERLY_SET,
/*  Mid nodes are not properly set for
    Quad8/Tria6/Tetra10/Hex20/Wdg15 elements  */

UF_SF_MSHVLD_INVALID_NODE_BTYPE,
/*  The boundary types of nodes are not properly set  */

UF_SF_MSHVLD_NODE_ASSOCIATED_TO_CHILD_FACE,
/*  Nodes are associated to child faces of compound faces  */

UF_SF_MSHVLD_NODE_ASSOCIATED_TO_INTERIOR_EDGE,
/*  Nodes are associated to interior edges of compound faces  */

UF_SF_MSHVLD_NODE_SHARED_BY_MULTIPLE_COLLECTORS,
/*  A node belongs to more than one node collector.*/

UF_SF_MSHVLD_DUPLICATE_NODE_LABEL,
/* Two or more nodes have same label.*/


/*  4. Mesh recipe errors  */

UF_SF_MSHVLD_MR_WITH_NO_MG,
/* Mesh recipes do not contain any mesh geometry  */

UF_SF_MSHVLD_INVALID_1D_CONNECT_ELEM,
/*  Nodes of 1D connection elements
    are not on proper mesh geometries  */

UF_SF_MSHVLD_INVALID_1D_WELD_ELEM,
/*  Nodes of 1D weld elements are not on hard points  */

UF_SF_MSHVLD_INVALID_1D_CONTACT_ELEM,
/*  Nodes of 1D contact elements are not in their edge limits  */

UF_SF_MSHVLD_INVALID_EDGE_LIMIT,
/*  Edge limits are not correct  */


/*  5. Geometric constraint errors  */

UF_SF_MSHVLD_HARD_PNT_NOT_HONORED,
/*  Hard points are not honored in meshes  */

UF_SF_MSHVLD_INVALID_MATCH_EDGE_MESH,
/*  Matched edges in sheet bodies do not share common nodes  */

UF_SF_MSHVLD_INVALID_GLUE_MATE_EDGE_MESH,
/*  The edges which are part of coincident GLUE mesh mated faces
    do not share common nodes  */

UF_SF_MSHVLD_INVALID_FREE_MATE_EDGE_MESH,
/*  The edges which are part of coincident FREE mesh mated faces
    dot not have duplicate nodes  */

UF_SF_MSHVLD_INVALID_GLUE_MATE_FACE_MESH,
/*  The faces having coincident GLUE MMC do not
    share common element nodes and faces  */

UF_SF_MSHVLD_INVALID_FREE_MATE_FACE_MESH,
/*  The faces having coincident FREE MMC do not
    have duplicate element nodes and faces  */

UF_SF_MSHVLD_INVALID_MATCH_MATE_EDGE_MESH,
/*  Matched/glue mated edge do not share common nodes  */

UF_SF_MSHVLD_INVALID_EDGE_MATE_FOR_MMC,
/*  Edges on a face coincidently mating with another one
    are not mated with an edge on the mated face  */

UF_SF_MSHVLD_INVALID_END_NODE_ASSOCIATIVITY,
/*  A node on an end of an edge is not associated to
    all edges of the same body with the same end  */

UF_SF_MSHVLD_NODE_ASSOCIATED_TO_TINY_EDGE,
/*  Tiny edges have associated elements/nodes  */


/*  6. User attribute errors  */

UF_SF_MSHVLD_EDGE_DENSITY_NOT_HONORED,
/*  The user attribute Edge Density is not honored  */

UF_SF_MSHVLD_FACE_DENSITY_NOT_HONORED,
/*  The user attribute Face Density is not honored  */

UF_SF_MSHVLD_EDGE_DENSITY_NOT_HONORED_FOR_MATCH_MATE_PNRS,
/* The user attribute Edge Density is not honored for matched/mated edges  */

UF_SF_MSHVLD_FACE_DENSITY_NOT_HONORED_FOR_MATE_PNRS,
/* The user attribute Face Density is not honored for mated faces  */

UF_SF_MSHVLD_EDGE_FACE_DENSITY_NOT_HONORED,
/* The user attribute Edge/Face Density is not honored  */

UF_SF_MSHVLD_MESH_WITH_PENDING_UPDATE
/* Mesh with pending update */
};
typedef enum UF_SF_mesh_error_type_e UF_SF_mesh_error_type_t, *UF_SF_mesh_error_type_p_t;




/***************************************************************************
 *
 *   This structure allows specification of mesh errors.
 ***************************************************************************/
 struct UF_SF_mesh_error_s {
    tag_t                         err_object;
    /*  The tag of object with mesh errors  */

    UF_SF_mesh_error_type_t       err_type;
};
typedef struct UF_SF_mesh_error_s UF_SF_mesh_error_t, *UF_SF_mesh_error_p_t;



/***************************************************************************
 *
 *   This structure allows specification of mesh error lists.
 ***************************************************************************/
struct UF_SF_mesh_error_list_s {
    int                     num_mesh_errors;
    /*  The number of mesh errors  */

    UF_SF_mesh_error_p_t   mesh_errors;
    /*  pointer to the array of mesh errors  */
};
typedef struct UF_SF_mesh_error_list_s UF_SF_mesh_error_list_t, *UF_SF_mesh_error_list_p_t;



/***************************************************************************
 *
 *   This structure allows specification of mesh error containers.
 **************************************************************************/
struct UF_SF_mesh_error_container_s {
    UF_SF_mesh_error_list_t  node_asso_error_list;
    /*  The list of errors in node associativity group  */

    UF_SF_mesh_error_list_t  elem_asso_error_list;
    /*  The list of errors in elem associativity group  */

    UF_SF_mesh_error_list_t  mesh_asso_error_list;
    /*  The list of errors in mesh associativity group  */

    UF_SF_mesh_error_list_t  mesh_recipe_error_list;
    /*  The list of errors in mesh recipe group   */

    UF_SF_mesh_error_list_t  geom_constraint_error_list;
    /*  The list of errors in geometric constraint group  */

    UF_SF_mesh_error_list_t  user_attribute_error_list;
    /*  The list of errors in user attribute group  */
};
typedef struct UF_SF_mesh_error_container_s UF_SF_mesh_error_container_t, *UF_SF_mesh_error_container_p_t;


/*  Check all meshes without selection    */
#define UF_SF_VALIDATE_ALL_MESHES                    (1U<<0)

/*  Check mesh associativity errors       */
#define UF_SF_VALIDATE_MESH_ASSOCIATIVITY            (1U<<1)

/*  Check element associativity errors    */
#define UF_SF_VALIDATE_ELEM_ASSOCIATIVITY            (1U<<2)

/*  Check node associativity errors       */
#define UF_SF_VALIDATE_NODE_ASSOCIATIVITY            (1U<<3)

/*  Check mesh recipe errors              */
#define UF_SF_VALIDATE_MESH_RECIPES                  (1U<<4)

/*  Check geometric constraint errors     */
#define UF_SF_VALIDATE_GEOM_CONSTRAINT_SATISFACTION  (1U<<5)

/*  Check user attribute errors           */
#define UF_SF_VALIDATE_USER_DEFINED_ATTRIBUTES       (1U<<6)

/*  Check all mesh errors                 */
#define UF_SF_VALIDATE_MESH_ALL                      (~0U)



/**************************************************************************
*
*   Function: UF_SF_validate_meshes
*
*   DESCRIPTION
*
*   This user function is used to perform mesh validation.
*   It's prototype is available in uf_sf_mshvld.h
*
*   INPUT
*
*   tag_p_t       mesh_ents_p   :  the list of mesh/ mesh_recipe tags
*                                  If mesh_ents_tag = NULL, mesh validation
*                                  is performed on all mesh recipes/meshes.
*                                  For this case, we do not care about the
*                                  value of num_mesh_ents.
*   int           num_mesh_ents :  The number of tags in the list mesh_ents_p.
*
*   unsigned int  option_mask   :  the mesh validation options are defined in
*                                  the head file uf_sf_mshvld.h.
*
*   OUTPUT
*
*   UF_SF_mesh_error_container_p_t error_container :
*
*   the structure holding the mesh errors found.
*
*   The caller is required to free the memory of all mesh_errors of type
*   UF_SF_mesh_error_p_t in each mesh error list in this container.
*
*   RETURN
*
*   0 for success
*   Error code for failure
**************************************************************************/
extern UFUN_CAEEXPORT int UF_SF_validate_meshes
                      (
                      tag_p_t                           mesh_ents_p,
                      int                               num_mesh_ents,
                      unsigned int                      option_mask,
                      UF_SF_mesh_error_container_p_t    error_container
                      );


/**************************************************************************
*
*   Function: UF_SF_init_mshvld_error_container
*
*   DESCRIPTION
*
*   This user function is used to initialize the error container
*   of mesh validation. It's prototype is available in uf_sf_mshvld.h
*
*   INPUT/OUTPUT
*
*   UF_SF_mesh_error_container_p_t error_container :
*
*   the structure holding the mesh errors found in mesh validation.
*
*   RETURN
*
*   void
*
**************************************************************************/


extern UFUN_CAEEXPORT void UF_SF_init_mshvld_error_container
                       (
                       UF_SF_mesh_error_container_p_t container
                       );


/**************************************************************************
*
*   Function: UF_SF_clean_mshvld_error_container
*
*   DESCRIPTION
*
*   This user function is used to clean the error container
*   of mesh validation. It's prototype is available in uf_sf_mshvld.h
*
*   INPUT/OUTPUT
*
*   UF_SF_mesh_error_container_p_t error_container :
*
*   the structure holding the mesh errors found in mesh validation.
*
*   RETURN
*
*   void
*
**************************************************************************/


extern UFUN_CAEEXPORT void UF_SF_clean_mshvld_error_container
                       (
                       UF_SF_mesh_error_container_p_t container
                       );

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif   /* This ends UF_SF_MSHVLD_H_INCLUDED  */
