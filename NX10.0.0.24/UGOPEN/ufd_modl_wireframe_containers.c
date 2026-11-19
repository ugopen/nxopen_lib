/*===================================================================

        Copyright (c) 2003 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *
 * DESCRIPTION -
 *   This program shows how to use the following UG/Open API routine(s):
 *
 *         UF_MODL_create_smart_wireframe_container
 *         UF_MODL_ask_smart_wireframe_container
 *         UF_MODL_add_rules_to_wireframe_container
 *         UF_MODL_remove_rules_from_wireframe_container
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
  if ( rule1_type == UF_SC_CURVE_FOLLOW_FILLET_CURVES )
    return (( rule1->curve_follow_fillet_input.seed_wireframe ==
              rule2->curve_follow_fillet_input.seed_wireframe ) &&
            ( rule1->curve_follow_fillet_input.end_wireframe ==
              rule2->curve_follow_fillet_input.end_wireframe ) &&
            ( rule1->curve_follow_fillet_input.from_seed_start ==
              rule2->curve_follow_fillet_input.from_seed_start ) &&
            ( fabs ( rule1->curve_follow_fillet_input.gap_angle_tols[0] -
                     rule2->curve_follow_fillet_input.gap_angle_tols[0] ) < 0.001 ) &&
            ( fabs ( rule1->curve_follow_fillet_input.gap_angle_tols[1] -
                     rule2->curve_follow_fillet_input.gap_angle_tols[1] ) < 0.001 ) &&
            same_tag_arrays ( rule1->curve_follow_fillet_input.num_features ,
                              rule1->curve_follow_fillet_input.features ,
                              rule2->curve_follow_fillet_input.num_features ,
                              rule2->curve_follow_fillet_input.features ) &&
            same_tag_arrays ( rule1->curve_follow_fillet_input.num_bodies ,
                              rule1->curve_follow_fillet_input.bodies ,
                              rule2->curve_follow_fillet_input.num_bodies ,
                              rule2->curve_follow_fillet_input.bodies ) &&
            same_tag_arrays ( rule1->curve_follow_fillet_input.num_dumb_curves ,
                              rule1->curve_follow_fillet_input.dumb_curves ,
                              rule2->curve_follow_fillet_input.num_dumb_curves ,
                              rule2->curve_follow_fillet_input.dumb_curves ));
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

/* Find two edges in the array all_edges, that are differred by the distances */
static void find_two_start_edges
(
  double   * distances ,    /*I: the absolute distances  x,y,z */
  int        n_all_edges ,
  tag_t    * all_edges ,
  tag_t    * start_edge1 ,
  tag_t    * start_edge2
)
{
  int      inx = 0 , vcount1 = 0, vcount2 = 0;
  tag_t    lc_edge1 = all_edges[0] , lc_edge2 = NULL_TAG;
  double   pt11[3] , pt12[3] , pt21[3] , pt22[3];

  (* start_edge1 ) = (* start_edge2 ) = NULL_TAG;

  UF_CALL( UF_MODL_ask_edge_verts ( lc_edge1 , pt11 , pt12 , & vcount1 ));
  for ( inx = 1; inx < n_all_edges ; inx++)
  {
    lc_edge2 = all_edges[inx];

    UF_CALL( UF_MODL_ask_edge_verts ( lc_edge2 , pt21 , pt22 , & vcount2 ));
    if ( vcount1 != vcount2 )
        continue;
    if ((( fabs ( fabs ( pt11[0] - pt21[0] ) - distances[0] ) < 0.001 ) &&
         ( fabs ( fabs ( pt11[1] - pt21[1] ) - distances[1] ) < 0.001 ) &&
         ( fabs ( fabs ( pt11[2] - pt21[2] ) - distances[2] ) < 0.001 ) &&
         ( fabs ( fabs ( pt12[0] - pt22[0] ) - distances[0] ) < 0.001 ) &&
         ( fabs ( fabs ( pt12[1] - pt22[1] ) - distances[1] ) < 0.001 ) &&
         ( fabs ( fabs ( pt12[2] - pt22[2] ) - distances[2] ) < 0.001 )) ||
        (( fabs ( fabs ( pt11[0] - pt22[0] ) - distances[0] ) < 0.001 ) &&
         ( fabs ( fabs ( pt11[1] - pt22[1] ) - distances[1] ) < 0.001 ) &&
         ( fabs ( fabs ( pt11[2] - pt22[2] ) - distances[2] ) < 0.001 ) &&
         ( fabs ( fabs ( pt12[0] - pt21[0] ) - distances[0] ) < 0.001 ) &&
         ( fabs ( fabs ( pt12[1] - pt21[1] ) - distances[1] ) < 0.001 ) &&
         ( fabs ( fabs ( pt12[2] - pt21[2] ) - distances[2] ) < 0.001 )))
    {
      (* start_edge1 ) = lc_edge1 ;
      (* start_edge2 ) = lc_edge2 ;
      return;
    }
  }
} /* find_two_start_edges */

/* Create a block with blend edges.  See more details in the code. */
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
  UF_MODL_init_sc_input_data (rule_types[0], (UF_SC_input_data_t *)&rules[0]);
  rules[0].edge_dumb_input.num_edges = n_non_blend_edges ;
  rules[0].edge_dumb_input.edges     = non_blend_edges ;

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
  int                         inx , error = 0, n_rules = 0 , n_out_rules = -1,
                            * out_rule_types = NULL, rule_types[6] ,
                              n_out_container_edges = 0, n_good_container_edges = 0,
                              n_blend_edges1 = 0, n_blend_edges2 = 0;
  tag_t                       part_tag = NULL_TAG, wireframe_container = NULL_TAG,
                            * blend_edges1 = NULL, * blend_edges2 = NULL,
                              start_edge1 = NULL_TAG, start_edge2 = NULL_TAG,
                            * out_container_edges = NULL, * good_container_edges = NULL;
  double                      origin[3] = {0.0,0.0,0.0}, distances[3] = {10.0,0.0,0.0};
  char                      * part_name = "wireframe_containers",
                            * block_sizes[3] = {"10.0","20.0","30.0"};
  UF_SC_EDGE_tangent_data_t   tangent_edge_data[4] ;
  UF_SC_input_data_t          rules[6] , * out_rules = NULL ;

/* Create the part and one body */
  UF_CALL( UF_PART_new ( part_name , ENGLISH , & part_tag ));
  UF_CALL( create_block_with_blend_edges ( origin ,
                                           block_sizes ,
                                           & n_blend_edges1 ,
                                           & blend_edges1 ));

/* Create a wireframe container for all the tangent edges */

  find_two_start_edges ( distances , n_blend_edges1 , blend_edges1 ,
                         & start_edge1 , & start_edge2 );
  n_rules = 2;

  rule_types[0] = UF_SC_EDGE_TANGENT_EDGES ;
  UF_MODL_init_sc_input_data (rule_types[0], (UF_SC_input_data_t *)&tangent_edge_data[0]);
  tangent_edge_data[0].start_edge = start_edge1 ;
  tangent_edge_data[0].end_edge = NULL_TAG;
  tangent_edge_data[0].from_start = FALSE;
  tangent_edge_data[0].angle_tol = 0.5;
  tangent_edge_data[0].same_convexity = FALSE;
  rules[0].edge_tangent_input = tangent_edge_data[0] ;

  rule_types[1] = UF_SC_EDGE_TANGENT_EDGES ;
  UF_MODL_init_sc_input_data (rule_types[1], (UF_SC_input_data_t *)&tangent_edge_data[1]);
  tangent_edge_data[1].start_edge = start_edge2 ;
  tangent_edge_data[1].end_edge = NULL_TAG;
  tangent_edge_data[1].from_start = FALSE;
  tangent_edge_data[1].angle_tol = 0.5;
  tangent_edge_data[1].same_convexity = FALSE;
  rules[1].edge_tangent_input = tangent_edge_data[1] ;

  UF_CALL( UF_MODL_create_smart_wireframe_container ( start_edge1 ,
                                                     n_rules ,
                                                     rule_types ,
                                                     rules ,
                                                     & wireframe_container ));

/* This container should contain 16 edges as in blend_edges1,
   and the rule should be the same */

  UF_CALL( UF_MODL_ask_smart_wireframe_container ( wireframe_container ,
                                                  & n_out_rules ,
                                                  & out_rule_types ,
                                                  & out_rules ,
                                                  & n_out_container_edges ,
                                                  & out_container_edges ));

  if (( n_out_rules != n_rules ) ||
      ( ! same_tag_arrays ( n_blend_edges1 , blend_edges1 ,
                            n_out_container_edges , out_container_edges )) ||
      ( ! same_wireframe_rules ( out_rule_types[0] , & out_rules[0] ,
                                 rule_types[0] , & rules[0] )))
  {
    printf (" UF_MODL_create_smart_wireframe_container does not work. Verify output rules. OR \n" );
    printf (" UF_MODL_ask_smart_wireframe_container produces wrong answer \n" );
  }
  else
  {
    printf (" UF_MODL_create_smart_wireframe_container works. Verify output rules. AND \n" );
    printf (" UF_MODL_ask_smart_wireframe_container works. \n" );
  }
  printf ("-------------------------------------------------------------------------------------\n");

  for(inx=0;inx<n_out_rules;inx++){ UF_MODL_free_sc_input_data ( out_rule_types[inx], & out_rules[inx]);}
  UF_free ( out_rule_types );      out_rule_types = NULL;
  UF_free ( out_rules );           out_rules = NULL; n_out_rules=-1;
  UF_free ( out_container_edges );  out_container_edges = NULL; n_out_container_edges=0;

/* Create another body and add two more rules to the container */

  for (inx=0;inx<3;inx++){ origin[inx] += 50;}
  UF_CALL( create_block_with_blend_edges ( origin ,
                                           block_sizes ,
                                           & n_blend_edges2 ,
                                           & blend_edges2 ));

  find_two_start_edges ( distances , n_blend_edges2 , blend_edges2 ,
                         & start_edge1 , & start_edge2 );

  n_rules = 2;

  rule_types[2] = UF_SC_EDGE_TANGENT_EDGES ;
  tangent_edge_data[2].start_edge = start_edge1 ;
  tangent_edge_data[2].end_edge = NULL_TAG;
  tangent_edge_data[2].from_start = FALSE;
  tangent_edge_data[2].angle_tol = 0.5;
  tangent_edge_data[2].same_convexity = FALSE;
  rules[2].edge_tangent_input = tangent_edge_data[2];

  rule_types[3] = UF_SC_EDGE_TANGENT_EDGES ;
  tangent_edge_data[3].start_edge = start_edge2 ;
  tangent_edge_data[3].end_edge = NULL_TAG;
  tangent_edge_data[3].from_start = FALSE;
  tangent_edge_data[3].angle_tol = 0.5;
  tangent_edge_data[3].same_convexity = FALSE;
  rules[3].edge_tangent_input = tangent_edge_data[3] ;

  UF_CALL( UF_MODL_add_rules_to_wireframe_container ( n_rules ,
                                                      & rule_types[2] ,
                                                      & rules[2] ,
                                                      wireframe_container ));

/* This container should contain 32 edges as in blend_edges1,
   blend_edges2 and the rules should be the same */

  n_good_container_edges = n_blend_edges1 + n_blend_edges2;
  good_container_edges = (tag_t *) UF_allocate_memory ( n_good_container_edges*sizeof(tag_t) ,
                                                        & error );
  UF_CALL( error );
  n_good_container_edges=0;
  for (inx=0;inx<n_blend_edges1;inx++){ good_container_edges[n_good_container_edges++] = blend_edges1[inx];}
  for (inx=0;inx<n_blend_edges2;inx++){ good_container_edges[n_good_container_edges++] = blend_edges2[inx];}

  UF_CALL( UF_MODL_ask_smart_wireframe_container ( wireframe_container ,
                                                   & n_out_rules ,
                                                   & out_rule_types ,
                                                   & out_rules ,
                                                   & n_out_container_edges ,
                                                   & out_container_edges ));

  n_rules = 4;
  if (( n_out_rules != n_rules ) ||
      ( ! same_tag_arrays ( n_good_container_edges , good_container_edges ,
                            n_out_container_edges , out_container_edges )) ||
      ( ! same_wireframe_rule_arrays ( n_out_rules , out_rule_types , out_rules ,
                                       n_rules , rule_types , rules )))
  {
    printf (" UF_MODL_add_rules_to_wireframe_container does not work. Verify output rules. OR \n" );
    printf (" UF_MODL_ask_smart_wireframe_container produces wrong answer \n" );
  }
  else
  {
    printf (" UF_MODL_add_rules_to_wireframe_container works. Verify output rules. AND \n" );
    printf (" UF_MODL_ask_smart_wireframe_container works. \n" );
  }
  printf ("-------------------------------------------------------------------------------------\n");

  for(inx=0;inx<n_out_rules;inx++){ UF_MODL_free_sc_input_data ( out_rule_types[inx], & out_rules[inx]);}
  UF_free ( out_rule_types );       out_rule_types = NULL;
  UF_free ( out_rules );            out_rules = NULL; n_out_rules=-1;
  UF_free ( good_container_edges ); good_container_edges = NULL; n_good_container_edges=0;
  UF_free ( out_container_edges );  out_container_edges = NULL;  n_out_container_edges=0;

/* Remove the first two tangent rules */
  n_rules = 2;
  UF_CALL( UF_MODL_remove_rules_from_wireframe_container ( n_rules ,
                                                           rule_types ,
                                                           rules ,
                                                           wireframe_container ));
/* This container should contain 16 edges as in blend_edges2,
   and the rule should be the same */
  UF_CALL( UF_MODL_ask_smart_wireframe_container ( wireframe_container ,
                                                   & n_out_rules ,
                                                   & out_rule_types ,
                                                   & out_rules ,
                                                   & n_out_container_edges ,
                                                   & out_container_edges ));
  n_rules = 2;
  if (( n_out_rules != n_rules ) ||
      ( ! same_tag_arrays ( n_blend_edges2 , blend_edges2 ,
                            n_out_container_edges , out_container_edges )) ||
      ( ! same_wireframe_rule_arrays ( n_out_rules , out_rule_types , out_rules ,
                                       n_rules , & rule_types[2] , & rules[2] )))
  {
    printf (" UF_MODL_remove_rules_from_wireframe_container does not work. Verify output rules. OR \n" );
    printf (" UF_MODL_ask_smart_wireframe_container produces wrong answer \n" );
  }
  else
  {
    printf (" UF_MODL_remove_rules_from_wireframe_container works. Verify output rules. AND \n" );
    printf (" UF_MODL_ask_smart_wireframe_container works. \n" );
  }
  printf ("-------------------------------------------------------------------------------------\n");

  for(inx=0;inx<n_out_rules;inx++){ UF_MODL_free_sc_input_data ( out_rule_types[inx], & out_rules[inx]);}
  UF_free ( out_rule_types );
  UF_free ( out_rules );
  UF_free ( out_container_edges );
  UF_free ( blend_edges1 );
  UF_free ( blend_edges2 );
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
