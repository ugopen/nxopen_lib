/*===================================================================

        Copyright (c) 2003 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *
 * DESCRIPTION -
 *   This program shows how to use the following UG/Open API routine(s):
 *
 *         UF_MODL_create_section
 *         UF_MODL_ask_section
 *         UF_MODL_add_rules_to_section
 *         UF_MODL_remove_rules_from_section
 *         UF_MODL_set_start_and_direction_to_section
 *


 ******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_sc_types.h>
#include <uf_sc.h>
#include <uf_undo.h>
#include <math.h>
#include <uf_modl_error.h>

#define IN_BODY  (1)
#define ON_BODY  (3)

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report( const char *file, int line, const char *call, int irc)
{
  if (irc)
  {
    char    messg[133];
    printf("%s, line %d:  %s\n", file, line, call);
    (UF_get_fail_message(irc, messg)) ?
      printf("    returned a %d\n", irc) :
      printf("    returned error %d:  %s\n", irc, messg);
  }
  return(irc);
}

/* Check whether two arrays of doubles are identical */
static logical identical_double_arrays
(
  double     tolerance ,
  int        n_objs1 ,
  double   * objs1 ,
  int        n_objs2 ,
  double   * objs2
)
{
  int   inx;

  if ( n_objs1 != n_objs2 )
    return ( FALSE );
  for ( inx = 0; inx < n_objs1 ; inx++ )
  {
    if ( fabs ( objs1[inx] - objs2[inx]) > tolerance )
        return (FALSE);
  }

  return (TRUE);
}/* identical_double_arrays */


/* Check whether two arrays of tags having same size
   and containning the same elements */
static logical  same_tag_arrays
(
  int        n_objs1 ,
  tag_t    * objs1 ,
  int        n_objs2 ,
  tag_t    * objs2
)
{
  int   inx , jnx ;

  if ( n_objs1 != n_objs2 )
    return ( FALSE );

/* All objs1 are in objs2 */
  for ( inx = 0; inx < n_objs1 ; inx ++ )
  {
    logical    found = FALSE ;

    for ( jnx = 0 ; !found && jnx < n_objs2  ; jnx ++ )
    {
      if ( objs1[inx] == objs2[jnx] )
        found = TRUE ;
    }
    if ( !found )
      return ( FALSE );
  }

  if ( n_objs1 == 1 )
    return (TRUE);
/* All objs2  are in objs1 */
  for ( inx = 0; inx < n_objs2 ; inx ++ )
  {
    logical    found = FALSE ;

    for ( jnx = 0 ; !found && jnx < n_objs1 ; jnx ++ )
    {
      if ( objs2[inx] == objs1[jnx] )
        found = TRUE ;
    }
    if ( !found )
      return ( FALSE );
  }

  return ( TRUE );
} /* same_tag_arrays */

/* Check whether two wireframe rules are the same */
static logical same_wireframe_rules
(
  int                   rule1_type ,
  UF_SC_input_data_t  * rule1 ,
  int                   rule2_type ,
  UF_SC_input_data_t  * rule2
)
{
  if ( rule1_type != rule2_type )
    return (FALSE);
  if ( rule1_type == UF_SC_CURVE_DUMB_CURVES )
    return ( same_tag_arrays ( rule1->curve_dumb_input.num_curves ,
                           rule1->curve_dumb_input.curves ,
                           rule2->curve_dumb_input.num_curves ,
                           rule2->curve_dumb_input.curves ));
  else
  if ( rule1_type == UF_SC_CURVE_FEATURE_CURVES )
    return ( same_tag_arrays ( rule1->curve_feature_input.num_features ,
                           rule1->curve_feature_input.features ,
                           rule2->curve_feature_input.num_features ,
                           rule2->curve_feature_input.features ));
  else
  if ( rule1_type == UF_SC_CURVE_FEAT_CHAIN_CURVES )
    return (( rule1->curve_feat_chain_input.seed_curve ==
              rule2->curve_feat_chain_input.seed_curve ) &&
            ( rule1->curve_feat_chain_input.end_curve ==
              rule2->curve_feat_chain_input.end_curve ) &&
            ( rule1->curve_feat_chain_input.from_seed_start ==
              rule2->curve_feat_chain_input.from_seed_start ) &&
            ( fabs ( rule1->curve_feat_chain_input.gap_tol -
              rule2->curve_feat_chain_input.gap_tol ) < 0.001 ) &&
              same_tag_arrays ( rule1->curve_feat_chain_input.num_features ,
                            rule1->curve_feat_chain_input.features ,
                            rule2->curve_feat_chain_input.num_features ,
                            rule2->curve_feat_chain_input.features ));
  else
  if ( rule1_type == UF_SC_CURVE_FEAT_TANGENT_CURVES )
    return (( rule1->curve_feat_tangent_input.seed_curve ==
              rule2->curve_feat_tangent_input.seed_curve ) &&
            ( rule1->curve_feat_tangent_input.end_curve ==
              rule2->curve_feat_tangent_input.end_curve ) &&
            ( rule1->curve_feat_tangent_input.from_seed_start ==
              rule2->curve_feat_tangent_input.from_seed_start ) &&
            ( fabs ( rule1->curve_feat_tangent_input.gap_angle_tols[0] -
                     rule2->curve_feat_tangent_input.gap_angle_tols[0] ) < 0.001 ) &&
            ( fabs ( rule1->curve_feat_tangent_input.gap_angle_tols[1] -
                     rule2->curve_feat_tangent_input.gap_angle_tols[1] ) < 0.001 ) &&
            same_tag_arrays ( rule1->curve_feat_tangent_input.num_features ,
                          rule1->curve_feat_tangent_input.features ,
                          rule2->curve_feat_tangent_input.num_features ,
                          rule2->curve_feat_tangent_input.features ));
  else
  if ( rule1_type == UF_SC_EDGE_DUMB_EDGES )
    return ( same_tag_arrays ( rule1->edge_dumb_input.num_edges ,
                           rule1->edge_dumb_input.edges ,
                           rule2->edge_dumb_input.num_edges ,
                           rule2->edge_dumb_input.edges ));
  else
  if ( rule1_type == UF_SC_EDGE_CHAIN_EDGES )
    return (( rule1->edge_chain_input.start_edge ==
              rule2->edge_chain_input.start_edge ) &&
            ( rule1->edge_chain_input.end_edge ==
              rule2->edge_chain_input.end_edge ) &&
            ( rule1->edge_chain_input.from_start ==
              rule2->edge_chain_input.from_start ));
  else
  if ( rule1_type == UF_SC_EDGE_TANGENT_EDGES )
    return (( rule1->edge_tangent_input.start_edge ==
              rule2->edge_tangent_input.start_edge ) &&
            ( rule1->edge_tangent_input.end_edge ==
              rule2->edge_tangent_input.end_edge ) &&
            ( rule1->edge_tangent_input.from_start ==
              rule2->edge_tangent_input.from_start ) &&
            ( rule1->edge_tangent_input.same_convexity ==
              rule2->edge_tangent_input.same_convexity ) &&
            ( fabs ( rule1->edge_tangent_input.angle_tol -
                     rule2->edge_tangent_input.angle_tol ) < 0.001 ));
  else
  if ( rule1_type == UF_SC_EDGE_MSEEDTAN_EDGES )
    return (( rule1->edge_mseedtan_input.same_convexity ==
              rule2->edge_mseedtan_input.same_convexity ) &&
            ( fabs ( rule1->edge_mseedtan_input.angle_tol -
                     rule2->edge_mseedtan_input.angle_tol ) < 0.001 ) &&
            same_tag_arrays ( rule1->edge_mseedtan_input.num_seed_edges ,
                          rule1->edge_mseedtan_input.seed_edges ,
                          rule2->edge_mseedtan_input.num_seed_edges ,
                          rule2->edge_mseedtan_input.seed_edges ));
  else
  if ( rule1_type == UF_SC_EDGE_FACE_EDGES )
    return ( same_tag_arrays ( rule1->edge_face_input.num_faces ,
                           rule1->edge_face_input.faces ,
                           rule2->edge_face_input.num_faces ,
                           rule2->edge_face_input.faces ));
  else
  if ( rule1_type == UF_SC_EDGE_BODY_EDGES )
    return ( rule1->edge_body_input.body == rule2->edge_body_input.body );
  else
  if ( rule1_type == UF_SC_EDGE_FEATURE_EDGES )
    return ( same_tag_arrays ( rule1->edge_feature_input.num_features ,
                           rule1->edge_feature_input.features ,
                           rule2->edge_feature_input.num_features ,
                           rule2->edge_feature_input.features ));
  else
  if ( rule1_type == UF_SC_EDGE_SHBNDARY_EDGES )
    return ( rule1->edge_shbndary_input.sheet == rule2->edge_shbndary_input.sheet );
  else
  if ( rule1_type == UF_SC_EDGE_BOUNDARY_EDGES )
    return ( same_tag_arrays ( rule1->edge_boundary_input.num_faces_n_features ,
                           rule1->edge_boundary_input.faces_n_features ,
                           rule2->edge_boundary_input.num_faces_n_features ,
                           rule2->edge_boundary_input.faces_n_features ));
  else
  if ( rule1_type == UF_SC_EDGE_INTERSECT_EDGES )
    return ( same_tag_arrays ( rule1->edge_intersect_input.num_faces_n_features1 ,
                           rule1->edge_intersect_input.faces_n_features1 ,
                           rule2->edge_intersect_input.num_faces_n_features1 ,
                           rule2->edge_intersect_input.faces_n_features1 ) &&
             same_tag_arrays ( rule1->edge_intersect_input.num_faces_n_features2 ,
                           rule1->edge_intersect_input.faces_n_features2 ,
                           rule2->edge_intersect_input.num_faces_n_features2 ,
                           rule2->edge_intersect_input.faces_n_features2 ));
  else
    return (FALSE);
} /* same_wireframe_rules */

/* Check whether two arrays of wireframe rules having
   same size, same type, and  containning the same elements */
static logical same_wireframe_rule_arrays
(
  int                   n_rule1 ,
  int                 * rule1_types ,
  UF_SC_input_data_t  * rule1 ,
  int                   n_rule2 ,
  int                 * rule2_types ,
  UF_SC_input_data_t  * rule2
)
{
  int    inx , jnx ;

  if ( n_rule1 != n_rule2 )
    return (FALSE);
  for (inx = 0; inx < n_rule1; inx++ )
  {
    logical   found = FALSE ;
    for (jnx = 0; !found && jnx < n_rule2; jnx++ )
      found = same_wireframe_rules ( rule1_types[inx], & rule1[inx],
                                     rule2_types[inx], & rule2[inx] );
    if ( !found )
      return (FALSE);
  }

  if ( n_rule1 == 1 )
    return (TRUE);
  for (inx = 0; inx < n_rule2; inx++ )
  {
    logical   found = FALSE ;
    for (jnx = 0; !found && jnx < n_rule1; jnx++ )
      found = same_wireframe_rules ( rule2_types[inx], & rule2[inx],
                                     rule1_types[inx], & rule1[inx] );
    if ( !found )
        return (FALSE);
  }

  return (TRUE);
} /* same_wireframe_rule_arrays */

/* Check whether two UF_SC_section_data_t object are the same */
static logical same_section_rules
(
  UF_SC_section_data_p_t   section_rule1 ,
  UF_SC_section_data_p_t   section_rule2
)
{
  return (( fabs ( section_rule1->chaining_tolerance -
                   section_rule2->chaining_tolerance ) <= 1.0E-10 ) &&
          ( fabs ( section_rule1->distance_tolerance -
                   section_rule2->distance_tolerance ) <= 1.0E-10 ) &&
          ( fabs ( section_rule1->angle_tolerance -
                   section_rule2->angle_tolerance  ) <= 1.0E-10 )  &&
          ( same_wireframe_rule_arrays ( section_rule1->n_rules ,
                                         section_rule1->rule_types ,
                                         section_rule1->rules ,
                                         section_rule2->n_rules ,
                                         section_rule2->rule_types ,
                                         section_rule2->rules )));

}/* same_section_rules */

/* Check whether two arrays of UF_SC_section_data_t having same size
   and containning the same elements */
static logical same_section_rule_arrays
(
  int                     n_section_rules1 ,
  UF_SC_section_data_t  * section_rules1 ,
  int                     n_section_rules2 ,
  UF_SC_section_data_t  * section_rules2
)
{
  int  inx, jnx;

  if ( n_section_rules1 != n_section_rules2 )
    return (FALSE);

  for ( inx = 0; inx < n_section_rules1 ; inx ++ )
  {
    logical    found = FALSE ;

    for ( jnx = 0 ; !found && jnx < n_section_rules2  ; jnx ++ )
    {
      if ( same_section_rules ( & section_rules1[inx] ,
                                & section_rules2[jnx] ))
        found = TRUE ;
    }
    if ( !found )
      return ( FALSE );
  }

  if ( n_section_rules1 == 1 )
     return (TRUE);
/* All objs2  are in objs1 */
  for ( inx = 0; inx < n_section_rules2 ; inx ++ )
  {
    logical    found = FALSE ;

    for ( jnx = 0 ; !found && jnx < n_section_rules1 ; jnx ++ )
    {
      if ( same_section_rules ( & section_rules2[inx] ,
                                & section_rules1[jnx] ))
        found = TRUE ;
    }
    if ( !found )
      return ( FALSE );
  }
  return (TRUE);
} /* same_section_rule_arrays */

/* Check whether the UF_SC_section_output_data in an array
   of UF_SC_section_data_t having same tags as the
   input arrays of tags */
static logical check_output_data
(
  int                     n_section_rules ,
  UF_SC_section_data_t  * section_rules ,
  int                     n_objs ,
  tag_t                 * objs
)
{
  tag_t   * lc_objs = NULL;
  int       n_lc_objs = 0, inx, jnx, error = 0;
  logical   ret_val = FALSE;

  lc_objs = (tag_t *) UF_allocate_memory ( n_objs * sizeof (tag_t ), & error);
  if ( error )
      return ( FALSE );
  for ( inx = 0; inx < n_section_rules ; inx ++ )
  {
    for ( jnx = 0 ; jnx < section_rules[inx].n_output_objects ; jnx ++ )
    {
      lc_objs[n_lc_objs++] = (section_rules[inx].output_objects)[jnx].output_object ;
      if ( n_lc_objs > n_objs )
        return ( FALSE );
    }
  }

  ret_val = same_tag_arrays ( n_objs , objs , n_lc_objs , lc_objs );
  UF_free ( lc_objs );
  return ( ret_val );
} /* check_output_data */

/*
   Construct a point, from the first vertex of the linear edge, and a vector,
   from the second vertex to the first one
 */
static void find_starting_point_and_direction
(
  tag_t     linear_edge ,      /*I*/
  double    starting_point[3] ,/*O*/
  double    direction[3]       /*O*/
)
{
  int     inx, vcount = 0.0;
  double  vec_len = 0.0;

  UF_CALL( UF_MODL_ask_edge_verts ( linear_edge , starting_point , direction , & vcount ));
  for ( inx=0 ; inx<3 ; inx++){ direction[inx] -= starting_point[inx];}
  for ( inx=0 ; inx<3 ; inx++){ vec_len += direction[inx]*direction[inx];}
  vec_len = sqrt (vec_len);
  for ( inx=0 ; inx<3 ; inx++){ direction[inx] /= vec_len ;}
} /* find_starting_point_and_direction */

static logical same_point_with_distance
(
  double     pt1[3] ,
  double     pt2[3] ,
  double     distances[3] ,
  double     tolerance
)
{
  if (( fabs ( fabs ( pt1[0] - pt2[0] ) - distances[0] ) < tolerance ) &&
      ( fabs ( fabs ( pt1[1] - pt2[1] ) - distances[1] ) < tolerance ) &&
      ( fabs ( fabs ( pt1[2] - pt2[2] ) - distances[2] ) < tolerance ))
    return TRUE;
  else
    return FALSE;
} /* same_point_with_distance */

static void swap_elem ( tag_t   * elem1 , tag_t   * elem2 )
{
  tag_t  tmp_elem = (* elem1 ) ;
  (* elem1 ) = (* elem2 );
  (* elem2 ) = tmp_elem ;
} /* swap_elem */

/*
   Return 1 if one vertex of the edge is connected to end_pt2 and
             update end_pt2 to the other vertex of the edge
   Return 2 if both vertices of the edge are connected to end_pt1 and end_pt2
   Return 0 otherwise
*/
static int connected_edge
(
  double    tolerance ,
  tag_t     edge ,       /*I*/
  double    end_pt1[3] , /*I*/
  double    end_pt2[3]   /*I/0*/
)
{
  int     vcount;
  double  pt1[3], pt2[3], dist[3] = {0.0, 0.0, 0.0};

  UF_CALL( UF_MODL_ask_edge_verts ( edge , pt1 , pt2 , & vcount ));

  if ( same_point_with_distance ( end_pt2 , pt1 , dist, tolerance )) /* pt1 connects end_pt2 */
  {
    if ( same_point_with_distance ( end_pt1 , pt2 , dist, tolerance )) /* connect both ends */
      return (2);
    else /* pt1 connects end_pt2, update end_pt2 with  pt2 */
    {
      memcpy ( end_pt2, pt2 , 3*sizeof(double));
      return (1);
    }
  }
  else
  if ( same_point_with_distance ( end_pt2 , pt2, dist, tolerance )) /* pt2 connects end_pt2 */
  {
    if ( same_point_with_distance ( end_pt1 , pt1, dist, tolerance )) /* connect both ends */
      return (2);
    else /* pt2 connects end_pt2, update end_pt2 with  pt1 */
    {
      memcpy ( end_pt2, pt1, 3*sizeof(double));
      return (1);
    }
  }

  return (0);
} /* connected_edge */

/*
   Find the loop start with start_edge in the direction from the
   first vertex of start_edge. This loop will be stored in
   the array all_edges from all_edges[0] to all_edges[(* n_edges_in_loop)];
 */
static void  find_loop
(
  double    tolerance ,       /*I*/
  tag_t     start_edge ,      /*I*/
  int       n_all_edges ,     /*I*/
  int     * n_edges_in_loop , /*O*/
  tag_t   * all_edges         /*I/O*/
)
{
  int      inx , jnx, vcount , connected = 0 ;
  double   end_pt1[3] , end_pt2[3];
  logical  finish = FALSE;

 (* n_edges_in_loop ) = 1;
/* Put the start_edge at the begin of the loop */
  if ( start_edge != all_edges[0] )
  {
    for ( inx = 1; inx < n_all_edges ; inx ++ )
    {
      if ( start_edge == all_edges[inx] )
        swap_elem ( & all_edges[0] , & all_edges[inx] );
    }
  }
  UF_CALL( UF_MODL_ask_edge_verts ( all_edges[0] , end_pt1 , end_pt2 , & vcount ));

/* Find the edges that connected to start_edge from end_pt1 */
  for ( inx = 1; !finish && inx < n_all_edges ; inx ++ )
  {
    logical  found_edge = FALSE;

    for ( jnx = inx ; ! finish && ! found_edge && jnx < n_all_edges ; jnx ++ )
    {
      connected = connected_edge ( tolerance , all_edges[jnx] , end_pt1 , end_pt2 );

     /* The edge connected to end_pt2, go to the next one */
      if ( connected > 0 ) /* find the edge, swap it to the right place */
      {
        found_edge = TRUE;
        swap_elem ( & all_edges[inx] , & all_edges[jnx] );
        (* n_edges_in_loop )++;
      }

     /* If both ends of the edge are connected to the end points, we finish the loop */
      if (connected == 2 )
        finish = TRUE;
    }
  }
} /* find_loop */

/* Find an edge of edge_type  in a range of an array */
static tag_t find_edge_type
(
  int       edge_type ,
  int       start_index ,
  int       end_index ,
  tag_t   * all_edges
)
{
  int  inx ;

  for ( inx = start_index; inx < end_index ; inx++)
  {
    int   lc_edge_type = 0;

    UF_CALL( UF_MODL_ask_edge_type ( all_edges[inx], & lc_edge_type ));
    if ( lc_edge_type == edge_type )
      return ( all_edges[inx] );
  }
  return (NULL_TAG);
}/* find_edge_type */

/*
   Rearrange the all_edges array into two loops.
   On output, the all_edges array will contain the two loops.
   The first loop will be started with linear edge.  This loop
   will have (* start_loop2 +1) edges, and be stored in all_edges[0]
   to all_edges[(* start_loop2)-1].  The second loop will
   be started with linear edge which is paralleled and within distances
   from the started edge of the first loop. The second loop also
   have (n_all_edges - (* start_loop2)-1) edges, and be stored in
   all_edges[* start_loop2] to all_edges[n_all_edges-1]
*/
static int find_two_loops
(
  double     tolerance ,          /*I*/
  double   * distances ,          /*I: the absolute distances  x,y,z */
  int        n_all_edges ,        /*I*/
  int      * start_loop2 , /*0*/
  tag_t    * all_edges
)
{
  int      inx = 0 , vcount1 = 0, vcount2 = 0, n_connected_edges = 0;
  tag_t    lc_edge1 = NULL_TAG , lc_edge2 = NULL_TAG;
  double   pt11[3] , pt12[3] , pt21[3] , pt22[3];
  logical  found_edge = FALSE;

  (* start_loop2 ) = 0;
/* Find the first linear edge from on loop */
  lc_edge1 = find_edge_type ( UF_MODL_LINEAR_EDGE , 0 , n_all_edges , all_edges );
  if ( lc_edge1 == NULL_TAG )
    return 1;

/* Find the second linear edge from the other loop */
  UF_CALL( UF_MODL_ask_edge_verts ( lc_edge1 , pt11 , pt12 , & vcount1 ));
  found_edge = FALSE;
  for ( inx = 0; ! found_edge && inx < n_all_edges ; inx++)
  {
    lc_edge2 = all_edges[inx];

    UF_CALL( UF_MODL_ask_edge_verts ( lc_edge2 , pt21 , pt22 , & vcount2 ));
    if ( vcount1 != vcount2 )
      continue;
    if (( same_point_with_distance ( pt11 , pt21 , distances , tolerance ) &&
          same_point_with_distance ( pt12 , pt22 , distances , tolerance )) ||
        ( same_point_with_distance ( pt11 , pt22 , distances , tolerance ) &&
          same_point_with_distance ( pt12 , pt21 , distances , tolerance )))
    {
      found_edge = TRUE;
    }
  }

  if (( lc_edge1 == NULL_TAG ) || ( lc_edge2 == NULL_TAG ))
    return 1;

/* Find the two loops start with the lc_edge1 and lc_edge2 */
  find_loop ( tolerance ,
              lc_edge1 ,
              n_all_edges ,
              & n_connected_edges ,
              all_edges );
  find_loop ( tolerance ,
              lc_edge2 ,
              n_all_edges - n_connected_edges,
              & n_connected_edges ,
              & all_edges[n_connected_edges]);
  (* start_loop2 ) = n_connected_edges;
  return 0;
} /* find_two_loops */

/* Create a tube body with the input section and diameters */
static int create_tube
(
  tag_t      section ,
  char     * diameters[2] ,
  tag_t    * tube_body
)
{
  uf_list_p_t    tubelist = NULL, tubefeats = NULL;
  tag_t          tube_feature = NULL_TAG;

  (* tube_body ) = NULL_TAG;
  UF_CALL( UF_MODL_create_list ( & tubelist  ));
  UF_CALL( UF_MODL_put_list_item ( tubelist , section ));
  UF_CALL( UF_MODL_create_tube ( tubelist , diameters , UF_NULLSIGN, & tubefeats ));
  UF_CALL( UF_MODL_ask_list_item ( tubefeats , 0, & tube_feature ));
  UF_CALL( UF_MODL_ask_feat_body ( tube_feature , tube_body ));

  UF_CALL( UF_MODL_delete_list ( & tubelist  ));
  UF_CALL( UF_MODL_delete_list ( & tubefeats  ));

  if ((* tube_body ) == NULL_TAG )
     return ( GET_FEATURE_TAG_ERROR );
  else
     return (0);
} /* create_tube */

/* Verify that the body has n_faces and n_edges , and
   the input point is on or in the body */
static logical verify_body
(
  tag_t     tube_body ,
  int       n_faces ,
  int       n_edges ,
  double    test_pt[3] ,
  int       on_body
)
{
  int           status = -1, lc_n_edges = 0, lc_n_faces = 0;
  uf_list_p_t   face_list = NULL, edge_list = NULL;

  UF_CALL( UF_MODL_ask_body_faces ( tube_body , & face_list ));
  UF_CALL( UF_MODL_ask_body_edges ( tube_body , & edge_list ));
  UF_CALL( UF_MODL_ask_list_count ( edge_list , & lc_n_edges ));
  UF_CALL( UF_MODL_ask_list_count ( face_list , & lc_n_faces ));
  UF_CALL( UF_MODL_delete_list ( & face_list ));
  UF_CALL( UF_MODL_delete_list ( & edge_list ));

  if (( n_edges != lc_n_edges ) || ( n_faces != lc_n_faces ))
    return FALSE;

  UF_CALL( UF_MODL_ask_point_containment ( test_pt , tube_body , & status ));
  if ( status == on_body )
    return TRUE;
  else
    return FALSE;
} /* verify_body */

/* Create a block with blend edges.  See more details in the code.  */
static int create_block_with_blend_edges
(
  double      origin[3] ,
  char      * block_sizes[3] ,
  int       * n_blend_edges ,
  tag_t    ** blend_edges
)
{
  int                         inx , lc_n_blend_edges = 0,
                              n_non_blend_edges = 0, rule_types[3],
                              num_objs = 0, n_rules = 0 , error = 0;
  tag_t                       block_tag = NULL_TAG , obj = NULL_TAG,
                              blend_edge_container = NULL_TAG,
                              blend_feature_eid = NULL_TAG,
                            * non_blend_edges = NULL , * lc_blend_edges = NULL;
  uf_list_p_t                 edge_list = NULL;
  UF_MODL_edge_blend_data_t   blend_data ;
  UF_MODL_blend_edge_t        edge_data ;
  UF_SC_EDGE_dumb_data_t      dumb_container_edge_data ;
  UF_SC_input_data_t          rules [3];

  UF_CALL( UF_MODL_create_block1 ( UF_NULLSIGN ,
                                   origin ,
                                   block_sizes ,
                                   & block_tag ));

  UF_CALL( UF_MODL_ask_feat_edges ( block_tag , & edge_list ));

/* Get all the edges of lengths 20 and 30 and put them in lc_blend_edges */
  UF_CALL( UF_MODL_ask_list_count ( edge_list , & num_objs ));
  for ( inx = 0 ; inx < num_objs ; inx ++ )
  {
    double   pt1[3] , pt2[3];
    int      vcount = 0;

    UF_CALL( UF_MODL_ask_list_item ( edge_list , inx , & obj ));
    UF_CALL( UF_MODL_ask_edge_verts ( obj , pt1 , pt2 , & vcount ));
    if (( fabs ( fabs ( pt1[1] -  pt2[1] ) - 20.0 ) < 0.001 ) ||
        ( fabs ( fabs ( pt1[2] -  pt2[2] ) - 30.0 ) < 0.001 ))
    {
      lc_blend_edges = (tag_t *) UF_reallocate_memory ( lc_blend_edges ,
                                                        (lc_n_blend_edges+1)*sizeof(tag_t),
                                                        & error );
      UF_CALL( error );
      lc_blend_edges[lc_n_blend_edges++] = obj ;
    }
    else
    {
      non_blend_edges = (tag_t *) UF_reallocate_memory ( non_blend_edges ,
                                                         (n_non_blend_edges+1)*sizeof(tag_t),
                                                         & error );
      UF_CALL( error );
      non_blend_edges[n_non_blend_edges++] = obj ;
    }
  }
  UF_CALL( UF_MODL_delete_list ( & edge_list ));

/* Create wireframe collector for the blend edge */
  n_rules = 1;
  rule_types[0] = UF_SC_EDGE_DUMB_EDGES ;
  UF_MODL_init_sc_input_data (rule_types[0], (UF_SC_input_data_t *)&dumb_container_edge_data);
  dumb_container_edge_data.num_edges = n_non_blend_edges ;
  dumb_container_edge_data.edges = non_blend_edges ;
  rules[0].edge_dumb_input = dumb_container_edge_data ;

  UF_CALL( UF_MODL_create_smart_wireframe_container ( non_blend_edges[0] ,
                                                      n_rules ,
                                                      rule_types ,
                                                      rules ,
                                                      & blend_edge_container ));
  UF_free ( non_blend_edges );
/* Blend the edges */
  edge_data.edge = blend_edge_container;
  edge_data.cliff_edge = NULL_TAG;
  edge_data.number_points = 0;
  strcpy ( edge_data.start_setback_dis ,  "");
  strcpy ( edge_data.end_setback_dis , "" );
  edge_data.point_data = NULL;

  blend_data.blend_type = 0;
  blend_data.blend_instanced = FALSE;
  blend_data.blend_setback = FALSE;
  blend_data.vrb_tolerance = 0.0;
  strcpy ( blend_data.blend_radius , "3.0");
  blend_data.smooth_overflow = FALSE;
  blend_data.cliff_overflow = FALSE;
  blend_data.notch_overflow = FALSE;
  blend_data.number_edges = 1;
  blend_data.edge_data = & edge_data ;

  UF_CALL( UF_MODL_create_edge_blend ( & blend_data , & blend_feature_eid ));

/* Find the faces created by the blend feature */
  UF_CALL( UF_MODL_ask_feat_edges ( blend_feature_eid , & edge_list ));
  UF_CALL( UF_MODL_ask_list_count ( edge_list , & num_objs ));
  UF_CALL(error );

  for ( inx = 0 ; inx < num_objs ; inx ++ )
  {
    int    edge_type = 0;

    UF_CALL( UF_MODL_ask_list_item ( edge_list , inx , & obj ));
    UF_CALL( UF_MODL_ask_edge_type ( obj , & edge_type ));
    if ( edge_type != UF_MODL_LINEAR_EDGE )
    {
      lc_blend_edges = (tag_t *) UF_reallocate_memory ( lc_blend_edges ,
                                                        (lc_n_blend_edges+1)*sizeof(tag_t),
                                                        & error );
      UF_CALL( error );
      lc_blend_edges[lc_n_blend_edges++] = obj ;
    }
  }

  UF_CALL( UF_MODL_delete_list ( & edge_list ));

  (* n_blend_edges ) = lc_n_blend_edges ;
  (* blend_edges ) = lc_blend_edges ;

  return (0);
} /* create_block_with_blend_edges */

static void do_ugopen_api (void)
{
  int                         n_section_rules = 0, n_out_section_rules = -1,
                              sc_rule_types[6] , start_loop1 = 0, start_loop2 = -1,
                              n_blend_edges = 0, inx;
  tag_t                     * blend_edges = NULL, part_tag = NULL_TAG,
                              section_tag1 = NULL_TAG, section_tag2 = NULL_TAG,
                              tube_body1 = NULL_TAG, tube_body2 = NULL_TAG,
                              starting_edge = NULL_TAG , out_starting_edge = NULL_TAG,
                              start_connector = NULL_TAG , end_connector = NULL_TAG;
  double                      origin[3] = {0.0,0.0,0.0}, distances[3] = {10.0,0.0,0.0},
                              starting_point[3] , direction[3],
                              out_starting_point[3] , out_direction[3],
                              help_point[3]={0.0, 0.0, 0.0},
                              intersection_point_1[3]={0.0, 0.0, 0.0},
                              intersection_point_2[3]={0.0, 0.0, 0.0};
  char                      * part_name = "sections",
                            * diameters[2] = {"1.0" , "0.0"},
                            * block_sizes[3] = {"10.0","20.0","30.0"};
  UF_SC_EDGE_tangent_data_t   tangent_edge_data[4];
  UF_SC_EDGE_dumb_data_t      dumb_edge_data[4];
  UF_SC_input_data_t          sc_rules[6];
  UF_SC_section_data_t        section_rules[3], * out_section_rules = NULL;

/* Create the part and one body */
  UF_CALL( UF_PART_new ( part_name , ENGLISH , & part_tag ));
  UF_CALL( create_block_with_blend_edges ( origin ,
                                           block_sizes ,
                                           & n_blend_edges ,
                                           & blend_edges ));

/* Arrange blend_edges into two loops of connected edges */
  find_two_loops ( 0.001 , distances , n_blend_edges , & start_loop2 , blend_edges  );

/* Create a section that contains the first 4 edges of the first loop */
  n_section_rules = 1;
  sc_rule_types[0] = UF_SC_EDGE_DUMB_EDGES ;
  UF_MODL_init_sc_input_data (sc_rule_types[0], (UF_SC_input_data_t *)&dumb_edge_data[0]);
  dumb_edge_data[0].num_edges = 2;
  dumb_edge_data[0].edges = & blend_edges[start_loop1];
  sc_rules[0].edge_dumb_input = dumb_edge_data[0];

  sc_rule_types[1] = UF_SC_EDGE_DUMB_EDGES ;
  UF_MODL_init_sc_input_data (sc_rule_types[1], (UF_SC_input_data_t *)&dumb_edge_data[1]);
  dumb_edge_data[1].num_edges = 2;
  dumb_edge_data[1].edges = & blend_edges[start_loop1+2];
  sc_rules[1].edge_dumb_input = dumb_edge_data[1];

  UF_MODL_initialize_section_data (& section_rules[0] );
  section_rules[0].n_rules = 2;
  section_rules[0].rule_types = sc_rule_types ;
  section_rules[0].rules = sc_rules ;
  section_rules[0].chaining_tolerance = 0.0001;
  section_rules[0].distance_tolerance = 0.0001;
  section_rules[0].angle_tolerance = 0.5;
  section_rules[0].start_connector = start_connector;
  section_rules[0].end_connector = end_connector;
  memcpy ( section_rules[0].help_point , help_point , 3*sizeof(double));
  memcpy ( section_rules[0].intersection_point_1 , intersection_point_1 , 3*sizeof(double));
  memcpy ( section_rules[0].intersection_point_2 , intersection_point_2 , 3*sizeof(double));

/* The starting point is one vertex of the linear edge, and the
   direction is a vector from other vertext to the starting point */

  starting_edge = blend_edges[start_loop1];
  find_starting_point_and_direction ( starting_edge , starting_point , direction );

  UF_CALL( UF_MODL_create_section ( starting_edge ,
                                    n_section_rules ,
                                    section_rules ,
                                    starting_edge ,
                                    starting_point ,
                                    direction ,
                                    FALSE ,
                                    & section_tag1 ));

/* This section should contain 4 edges. To verify it, we use the section
   to create a tube with radius 1. This tube should have 6 faces,
   two end faces and 4 side face, and 5 edges, 2 end edges and 3 side edges.
   Also it should contain the starting_point */

  UF_CALL( create_tube ( section_tag1 , diameters , & tube_body1 ));
  if ( ! verify_body ( tube_body1 , 6, 5, starting_point , ON_BODY ))
    printf (" UF_MODL_create_section does not work. Cannot verify body. \n" );
  else
    printf (" UF_MODL_create_section works. Verify body. \n" );

  UF_CALL( UF_MODL_ask_section ( section_tag1 ,
                                 & n_out_section_rules ,
                                 & out_section_rules ,
                                 & out_starting_edge ,
                                 out_starting_point ,
                                 out_direction ));

  if (( n_section_rules != n_out_section_rules ) ||
      ( ! same_section_rule_arrays ( n_section_rules , section_rules ,
                                     n_out_section_rules , out_section_rules )) ||
      ( ! check_output_data ( n_out_section_rules , out_section_rules ,
                              4 , & blend_edges[start_loop1] )))
  {
    printf (" UF_MODL_create_section does not work. Cannot verify output rules. OR \n" );
    printf (" UF_MODL_ask_section produces wrong answer. \n" );
  }
  else
  {
    printf (" UF_MODL_ask_section works. Verify output rules. AND \n" );
    printf (" UF_MODL_ask_section works. \n" );
  }
  printf ("-------------------------------------------------------------------------------------\n");

  for (inx=0;inx<n_out_section_rules;inx++){ UF_MODL_free_section_data (& out_section_rules[inx] );}
  UF_free ( out_section_rules ); out_section_rules = NULL; n_out_section_rules=-1;

/* Add two more rules to the section */
  sc_rule_types[2] = UF_SC_EDGE_DUMB_EDGES ;
  dumb_edge_data[2].num_edges = 2;
  dumb_edge_data[2].edges = & blend_edges[start_loop1+4];
  sc_rules[2].edge_dumb_input = dumb_edge_data[2];

  UF_MODL_initialize_section_data (& section_rules[1] );
  section_rules[1].n_rules = 1;
  section_rules[1].rule_types = & sc_rule_types[2] ;
  section_rules[1].rules = & sc_rules[2] ;
  section_rules[1].chaining_tolerance = 0.0001;
  section_rules[1].distance_tolerance = 0.0001;
  section_rules[1].angle_tolerance = 0.5;
  section_rules[1].start_connector = start_connector;
  section_rules[1].end_connector = end_connector;
  memcpy ( section_rules[1].help_point , help_point , 3*sizeof(double));
  memcpy ( section_rules[1].intersection_point_1 , intersection_point_1 , 3*sizeof(double));
  memcpy ( section_rules[1].intersection_point_2 , intersection_point_2 , 3*sizeof(double));

  sc_rule_types[3] = UF_SC_EDGE_DUMB_EDGES ;
  dumb_edge_data[3].num_edges = 2;
  dumb_edge_data[3].edges = & blend_edges[start_loop1+6];
  sc_rules[3].edge_dumb_input = dumb_edge_data[3];

  UF_MODL_initialize_section_data (& section_rules[2] );
  section_rules[2].n_rules = 1;
  section_rules[2].rule_types = & sc_rule_types[3] ;
  section_rules[2].rules = & sc_rules[3] ;
  section_rules[2].chaining_tolerance = 0.0001;
  section_rules[2].distance_tolerance = 0.0001;
  section_rules[2].angle_tolerance = 0.5;
  section_rules[2].start_connector = start_connector;
  section_rules[2].end_connector = end_connector;
  memcpy ( section_rules[2].help_point , help_point , 3*sizeof(double));
  memcpy ( section_rules[2].intersection_point_1 , intersection_point_1 , 3*sizeof(double));
  memcpy ( section_rules[2].intersection_point_2 , intersection_point_2 , 3*sizeof(double));

  UF_CALL( UF_MODL_add_rules_to_section ( 2 ,
                                          & section_rules[1] ,
                                          section_tag1 ));
  UF_CALL( UF_MODL_update ());

/* This section should contain 8 edges. The body tube_body1 should have 8
   faces, no end faces, and 8 edges, no end edges,.  Also it should contain the starting_point */

  if ( ! verify_body ( tube_body1 , 8, 8, starting_point , IN_BODY ))
    printf (" UF_MODL_add_rules_to_section does not work. Cannot verify body. \n" );
  else
    printf (" UF_MODL_add_rules_to_section works. Verify body. \n" );

  n_section_rules = 3;
  UF_CALL( UF_MODL_ask_section ( section_tag1 ,
                                 & n_out_section_rules ,
                                 & out_section_rules ,
                                 & out_starting_edge ,
                                 out_starting_point ,
                                 out_direction ));

  if (( n_section_rules != n_out_section_rules ) ||
      ( ! same_section_rule_arrays ( n_section_rules , section_rules ,
                                     n_out_section_rules , out_section_rules )) ||
      ( ! check_output_data ( n_out_section_rules , out_section_rules ,
                              8 , blend_edges )))
  {
    printf (" UF_MODL_add_rules_to_section does not work. Cannot verify output rules. OR\n" );
    printf (" UF_MODL_ask_section does not work. \n" );
  }
  else
  {
    printf (" UF_MODL_add_rules_to_section works. Verify output rules. AND\n" );
    printf (" UF_MODL_ask_section works \n" );
  }
  printf ("-------------------------------------------------------------------------------------\n");

  for (inx=0;inx<n_out_section_rules;inx++){ UF_MODL_free_section_data (& out_section_rules[inx] );}
  UF_free ( out_section_rules ); out_section_rules = NULL; n_out_section_rules=-1;

/* We remove the last section rule from section_tag1 */
  UF_CALL( UF_MODL_remove_rules_from_section ( 1 ,
                                               & section_rules[2] ,
                                               section_tag1 ));
  UF_CALL( UF_MODL_update ());

/* This section should contain 6 edges. The body tube_body1 should have 8
   faces, 2 end faces and 6 side faces, and 7 edges, two end edges and 5 side edges.
   Also it should contain the starting_point */

  if ( ! verify_body ( tube_body1 , 8, 7,  starting_point , ON_BODY ))
    printf (" UF_MODL_remove_rules_from_section does not work. Cannot verify body. \n" );
  else
    printf (" UF_MODL_remove_rules_from_section works. Verify body. \n" );

  n_section_rules = 2;
  UF_CALL( UF_MODL_ask_section ( section_tag1 ,
                                 & n_out_section_rules ,
                                 & out_section_rules ,
                                 & out_starting_edge ,
                                 out_starting_point ,
                                 out_direction ));

  if (( n_section_rules != n_out_section_rules ) ||
      ( ! same_section_rule_arrays ( n_section_rules , section_rules ,
                                     n_out_section_rules , out_section_rules )) ||
      ( ! check_output_data ( n_out_section_rules , out_section_rules ,
                              6 , blend_edges )))
  {
    printf (" UF_MODL_remove_rules_from_section does not work. Cannot verify output rules. OR\n" );
    printf (" UF_MODL_ask_section does not work. \n" );
  }
  else
  {
    printf (" UF_MODL_remove_rules_from_section works. Verify output rules. AND\n" );
    printf (" UF_MODL_ask_section works. \n" );
  }
  printf ("-------------------------------------------------------------------------------------\n");

  for (inx=0;inx<n_out_section_rules;inx++){ UF_MODL_free_section_data (& out_section_rules[inx] );}
  UF_free ( out_section_rules ); out_section_rules = NULL; n_out_section_rules=-1;

/*
 * Create a tangent section that contains 8 edges of the second loop
 */
  n_section_rules = 1;
  sc_rule_types[0] = UF_SC_EDGE_TANGENT_EDGES ;
  UF_MODL_init_sc_input_data (sc_rule_types[1], (UF_SC_input_data_t *)&tangent_edge_data[0]);
  tangent_edge_data[0].start_edge = blend_edges[start_loop2+3];
  tangent_edge_data[0].end_edge = NULL_TAG;
  tangent_edge_data[0].from_start = FALSE;
  tangent_edge_data[0].angle_tol = 0.5;
  tangent_edge_data[0].same_convexity = FALSE;
  sc_rules[0].edge_tangent_input = tangent_edge_data[0] ;

  section_rules[0].n_rules = 1;
  section_rules[0].rule_types = sc_rule_types ;
  section_rules[0].rules = sc_rules ;
  section_rules[0].chaining_tolerance = 0.0001;
  section_rules[0].distance_tolerance = 0.0001;
  section_rules[0].angle_tolerance = 0.5;
  section_rules[0].start_connector = start_connector;
  section_rules[0].end_connector = end_connector;

  memcpy ( section_rules[0].help_point , help_point , 3*sizeof(double));
  memcpy ( section_rules[0].intersection_point_1 , intersection_point_1 , 3*sizeof(double));
  memcpy ( section_rules[0].intersection_point_2 , intersection_point_2 , 3*sizeof(double));

/* The starting point is one vertex of the linear edge, and the
   direction is a vector from other vertext to the starting point */

  starting_edge = blend_edges[start_loop2] ;
  find_starting_point_and_direction ( starting_edge , starting_point , direction );

  UF_CALL( UF_MODL_create_section ( starting_edge ,
                                    n_section_rules ,
                                    section_rules ,
                                    starting_edge ,
                                    starting_point ,
                                    direction ,
                                    FALSE ,
                                    & section_tag2 ));

/* This section should contain 8 edges. To verify it, we use the section
   to create a tube with radius 1. This tube should have 8 faces and 8 edges.
   Also it should contain the starting_point */

  UF_CALL( create_tube ( section_tag2 , diameters , & tube_body2 ));
  if ( ! verify_body ( tube_body2 ,8,8, starting_point , IN_BODY))
    printf (" UF_MODL_create_section does not work. Cannot verify body. \n" );
  else
    printf (" UF_MODL_create_section works. Verify body. \n" );

  UF_CALL( UF_MODL_ask_section ( section_tag2 ,
                                 & n_out_section_rules ,
                                 & out_section_rules ,
                                 & out_starting_edge ,
                                 out_starting_point ,
                                 out_direction ));

  if (( n_section_rules != n_out_section_rules ) ||
      ( starting_edge != out_starting_edge ) ||
      ( ! same_section_rule_arrays ( n_section_rules , section_rules ,
                                     n_out_section_rules , out_section_rules )) ||
      ( ! check_output_data ( n_out_section_rules , out_section_rules ,
                              8 , & blend_edges[start_loop2] )))
  {
    printf (" UF_MODL_create_section does not work. Cannot verify output rules. OR\n" );
    printf (" UF_MODL_ask_section does not work. \n" );
  }
  else
  {
    printf (" UF_MODL_create_section works. Verify output rules. AND\n" );
    printf (" UF_MODL_ask_section works.  \n" );
  }
  printf ("-------------------------------------------------------------------------------------\n");

  for (inx=0;inx<n_out_section_rules;inx++){ UF_MODL_free_section_data (& out_section_rules[inx] );}
  UF_free ( out_section_rules ); out_section_rules = NULL; n_out_section_rules=-1;

/* Reset the starting edge and direction */
  starting_edge = find_edge_type ( UF_MODL_LINEAR_EDGE ,
                                   start_loop2+1 ,
                                   n_blend_edges ,
                                   blend_edges );
  find_starting_point_and_direction ( starting_edge , starting_point , direction );
  UF_CALL( UF_MODL_set_start_and_direction_to_section ( starting_edge ,
                                                        starting_point ,
                                                        direction ,
                                                        section_tag2 ));
  UF_CALL( UF_MODL_ask_section ( section_tag2 ,
                                 & n_out_section_rules ,
                                 & out_section_rules ,
                                 & out_starting_edge ,
                                 out_starting_point ,
                                 out_direction ));

  if (( n_section_rules != n_out_section_rules ) ||
      ( starting_edge != out_starting_edge ) ||
      ( ! identical_double_arrays ( 0.0001, 3, starting_point , 3, out_starting_point )) ||
      ( ! identical_double_arrays ( 0.0001, 3, direction , 3, out_direction )) ||
      ( ! same_section_rule_arrays ( n_section_rules , section_rules ,
                                     n_out_section_rules , out_section_rules )) ||
      ( ! check_output_data ( n_out_section_rules , out_section_rules ,
                              8 , & blend_edges[start_loop2] )))
  {
    printf (" UF_MODL_set_start_and_direction_to_section does not work. Cannot verify output rules. OR\n" );
    printf (" UF_MODL_ask_section does not work. \n" );
  }
  else
  {
    printf (" UF_MODL_set_start_and_direction_to_section works. Verify output rules. AND\n" );
    printf (" UF_MODL_ask_section works.  \n" );
  }
  printf ("-------------------------------------------------------------------------------------\n");

  for (inx=0;inx<n_out_section_rules;inx++){ UF_MODL_free_section_data (& out_section_rules[inx] );}
  UF_free ( out_section_rules ); out_section_rules = NULL; n_out_section_rules=-1;
  UF_free ( blend_edges );
} /* do_ugopen_api */

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int paramLen)
{
  if (!UF_CALL(UF_initialize()))
  {
    do_ugopen_api();
    UF_CALL(UF_terminate());
  }
}

int ufusr_ask_unload(void)
{
  return (UF_UNLOAD_IMMEDIATELY);
}
