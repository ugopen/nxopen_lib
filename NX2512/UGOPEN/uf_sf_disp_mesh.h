/*******************************************************************************

   Copyright (c) 1998-2001 Unigraphics Solutions Inc.
                 Unpublished - All rights reserved
________________________________________________________________________________





File description:

   Internal type definitions for UF_SF_DISP_MESH (Scenario Display Mesh) module.

*******************************************************************************/


#ifndef UF_SF_DISP_MESH_H_INCLUDED
#define UF_SF_DISP_MESH_H_INCLUDED

#include <uf_sf_types.h>


#ifdef __cplusplus
extern "C" {
#endif


/*****************************************************************************
  Structure defining the components of a shell mesh represented by a set of
  nodes and nodal connectivity information.
******************************************************************************/
struct UF_SF_disp_mesh_s
{
    UF_SF_mesh_dimension_t  elem_dimension;
                              /* Global dimension of mesh element for the whole mesh
                                 = UF_SF_DIMENSION_0D  -> CMASS or MASS
                                 = UF_SF_DIMENSION_1D  -> Bar, beam, rods, rigid, links,
                                                          springs and contact elements
                                 = UF_SF_DIMENSION_2D  -> quad4, quad8, tri3, tri6
                                 = UF_SF_DIMENSION_3D  -> tet4, tet10
                                 = UF_SF_DIMENSION_ANY -> any dimension */
    int     num_elements;     /* Number of elements in mesh   */
    int     num_nodes;        /* Number of nodes in mesh      */
    int     num_elem_nodes;   /* Number of nodes for each element.
                                 This number along with the dimension defines the element type.
                                 I.e. if the number is 4 and the dimension is 2d the type will
                                 be QUAD4 but if the dimension is 3d the type will be TET4. */
    double (*node_coords)[3]; /* <len:num_nodes>
								 Node coordinates array size of num_nodes.
                                 The i-th node is defined by the triplet:
                                  node_coords[i][0], node_coords[i][1], node_coords[i][1] */
    int     *node_ids;        /* <len:num_nodes>
								 Node ID array size of num_nodes: node_ids[node_idx] */
    int     *elem_ids;        /* <len:num_elements>
								 Element ID array size of num_elements */
    int     **elem_node_ids;  /* Node IDs for each element: elem_node_ids[elem_idx][elem_node_idx] */
};
typedef struct UF_SF_disp_mesh_s UF_SF_disp_mesh_t, *UF_SF_disp_mesh_p_t;

/*****************************************************************************
  Structure defining element node results associated with a mesh.
******************************************************************************/
struct UF_SF_mesh_elem_node_result_s
{
    tag_t   mesh_tag;         /* Tag of mesh object */
    int     num_elem;         /* Number of elements in mesh   */
    int     *elem_ids;        /* <len:num_elem>
									Element ID array size of num_elem */
    tag_t   *elem_tags;       /* <len:num_elem>
									Element tag array size of num_elem */
    int     *num_nodes;       /* <len:num_elem>
									For each element, the number of nodes: num_nodes[elem_idx] */
    int     **node_ids;       /* Node IDs for each element: node_ids[elem_idx][node_idx] */
    tag_t   **node_tags;      /* Node tags for each element: node_tags[elem_idx][node_idx] */
    double  **node_results;   /* Node results for each element: node_results[elem_idx][node_idx] */
};
typedef struct UF_SF_mesh_elem_node_result_s UF_SF_mesh_elem_node_result_t, *UF_SF_mesh_elem_node_result_p_t;



#ifdef __cplusplus
}
#endif

#endif  /* UF_SF_DISP_MESH_H_INCLUDED  */

