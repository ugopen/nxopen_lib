/*===================================================================

        Copyright (c) 2007  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following NX Open C API routine(s):      *
 *                                                                            *
 *         UF_CURVE_create_ocf_feature                                        *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires an open, blank part in English UNITS.     *
 *   The code                                                                 *
 *      - creates a block (10x20x30)                                          *
 *      - blends all the edges of length 10                                   *
 *      - create a section using the tangent rule and one of the blend edge   *
 *      - create a face collector using the tangent rule and one of the blend *
 *        face as seed                                                        *
 *      - offset the section created above on the faces of collector          *
 *        with offset distance of 1.0 inside the faces of collector           *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_sc_types.h>
#include <uf_sc.h>
#include <math.h>
#include <uf_defs.h>
#include <uf_curve.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report( char *file, int line, char *call, int irc)
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

static int create_block_with_blend_edges
(
  double     origin[3] ,
  char      *block_sizes[3],
  int       *n_blend_edges,
  tag_t    **blend_edges,
  int       *n_blend_faces,
  tag_t    **blend_faces
)
{
  int                         inx , lc_n_blend_edges = 0,
                              lc_n_blend_faces = 0,
                              n_non_blend_edges = 0, rule_types[3],
                              num_objs = 0, n_rules = 0 , error = 0;
  tag_t                       block_tag = NULL_TAG , obj = NULL_TAG,
                              blend_edge_container = NULL_TAG,
                              blend_feature_eid = NULL_TAG,
                            * non_blend_edges = NULL ,
                            * lc_blend_edges = NULL,
                            * lc_blend_faces = NULL ;
  uf_list_p_t                 edge_list = NULL, face_list=NULL;
  UF_MODL_edge_blend_data_t   blend_data ;
  UF_MODL_blend_edge_t        edge_data ;
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
  UF_MODL_init_sc_input_data (rule_types[0], &rules[0]);
  rules[0].edge_dumb_input.num_edges = n_non_blend_edges ;
  rules[0].edge_dumb_input.edges = non_blend_edges ;

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

  UF_CALL( UF_MODL_ask_feat_faces ( blend_feature_eid , & face_list ));
  UF_CALL( UF_MODL_ask_list_count ( face_list , & num_objs ));
  lc_blend_faces = (tag_t *) UF_reallocate_memory ( lc_blend_faces ,
                                                    (lc_n_blend_faces+num_objs)*sizeof(tag_t),
                                                    & error );
  UF_CALL(error );
  for ( inx = 0 ; inx < num_objs ; inx ++ )
    UF_CALL( UF_MODL_ask_list_item ( face_list, inx, &lc_blend_faces[lc_n_blend_faces++] ));

  UF_CALL( UF_MODL_delete_list ( &face_list ));

  (*n_blend_faces) = lc_n_blend_faces ;
  (*blend_faces ) = lc_blend_faces ;

  (*n_blend_edges ) = lc_n_blend_edges ;
  (*blend_edges ) = lc_blend_edges ;

  return (0);
} /* create_block_with_blend_edges */


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
    int     inx, vcount =0;
    double  vec_len = 0.0;

    UF_CALL( UF_MODL_ask_edge_verts ( linear_edge , starting_point , direction , & vcount ));
    for ( inx=0 ; inx<3 ; inx++){ direction[inx] -= starting_point[inx];}
    for ( inx=0 ; inx<3 ; inx++){ vec_len += direction[inx]*direction[inx];}
    vec_len = sqrt (vec_len);
    for ( inx=0 ; inx<3 ; inx++){ direction[inx] /= vec_len ;}
} /* find_starting_point_and_direction */

static void do_ugopen_api(void)
{
    tag_t                       part_tag = NULL_TAG;

    double                      origin[3] = {0.0,0.0,0.0};
    double                      distances[3] = {10.0,0.0,0.0};

    char                       *block_sizes[3] = {"10.0","20.0","30.0"};
    char                       *part_name = "offset_in_face";

    int                         n_blend_edges =0,
                                n_blend_faces = 0;
    tag_t                      *blend_edges = NULL,
                               *blend_faces = NULL;
    tag_t                       start_edge1 = NULL_TAG,
                                start_edge2 = NULL_TAG;

    int                         sc_rule_type=0;
    UF_SC_input_data_t          sc_rule;
    UF_SC_section_data_t        section_rule = {0};
    tag_t                       start_connector = NULL_TAG,
                                end_connector = NULL_TAG;
    double       help_point[3]={0.0, 0.0, 0.0},
                 intersection_point_1[3]={0.0, 0.0, 0.0},
                 intersection_point_2[3]={0.0, 0.0, 0.0};

    /* The starting point is one vertex of the linear edge, and the
       direction is a vector from other vertext to the starting point */
    double starting_point[3]={0.0,0.0,0.0};
    double direction[3]={0.0,0.0,0.0};

    int n_section_rules = 1;
    tag_t section_tag = NULL_TAG;

    int                n_face_rules = 1;
    int                face_rule_type= UF_SC_FACE_TANGENT_FACES ;
    UF_SC_input_data_t face_rule;
    tag_t face_collector = NULL_TAG;

    UF_CURVE_ocf_data_t ocf_data;
    double    offset_point[3];
    double    offset_direction_vec[3];

    int offset_direction = -1;
    tag_t ocf_feature = NULL_TAG;
    UF_CURVE_ocf_values_t offset_distances ={0};

    UF_CALL( UF_PART_new ( part_name , ENGLISH , &part_tag ));
    UF_CALL( create_block_with_blend_edges ( origin ,
                                             block_sizes ,
                                            &n_blend_edges ,
                                            &blend_edges,
                                            &n_blend_faces,
                                            &blend_faces ));

    /* create a section from the blend edges */
    find_two_start_edges ( distances , n_blend_edges, blend_edges,
                         &start_edge1 , &start_edge2 );

    sc_rule_type = UF_SC_EDGE_TANGENT_EDGES ;
    UF_MODL_init_sc_input_data (sc_rule_type, &sc_rule);
    sc_rule.edge_tangent_input.start_edge = start_edge1 ;
    sc_rule.edge_tangent_input.end_edge = NULL_TAG;
    sc_rule.edge_tangent_input.from_start = FALSE;
    sc_rule.edge_tangent_input.angle_tol = 0.5;
    sc_rule.edge_tangent_input.same_convexity = FALSE;

    UF_MODL_initialize_section_data (&section_rule);

    section_rule.n_rules = 1;
    section_rule.rule_types = &sc_rule_type;
    section_rule.rules = &sc_rule;
    section_rule.chaining_tolerance = 0.0001;
    section_rule.distance_tolerance = 0.0001;
    section_rule.angle_tolerance = 0.5;
    section_rule.start_connector = start_connector;
    section_rule.end_connector = end_connector;

    memcpy ( section_rule.help_point , help_point , 3*sizeof(double));
    memcpy ( section_rule.intersection_point_1 , intersection_point_1 , 3*sizeof(double));
    memcpy ( section_rule.intersection_point_2 , intersection_point_2 , 3*sizeof(double));

    find_starting_point_and_direction ( start_edge1 , starting_point , direction );

    UF_CALL( UF_MODL_create_section ( start_edge1,
        n_section_rules,
        &section_rule,
        start_edge1,
        starting_point,
        direction ,
        FALSE,
        &section_tag));

    /* Create a collector for the faces on which to offset the section.
       We will create a collector which represent the blend faces, using
       the tangent faces rule with one of the blend faces as seed face.

       Offset in face allows you to select set of connected faces to
       create offset curves. You can always select all the faces of
       of the body by using face_rule_type=UF_SC_FACE_BODY_FACES.

     */
    UF_MODL_init_sc_input_data (face_rule_type, &face_rule);

    face_rule.face_tangent_input.seed_face = blend_faces[0] ;
    face_rule.face_tangent_input.num_bndary_faces = 0;
    face_rule.face_tangent_input.bndary_faces = NULL;
    face_rule.face_tangent_input.angle_tol = 0.5;

    UF_CALL( UF_MODL_create_smart_face_container ( blend_faces[0] ,
        n_face_rules ,
        &face_rule_type,
        &face_rule,
        &face_collector ));

    /* create offset curves */

    /* Initialize the data with default values as follows
       cross_boundary_mode = UF_CURVE_OCF_CROSS_BOUNDARIES_NONE
       offset_method = UF_CURVE_OCF_CHORDAL
       trim_method = UF_CURVE_OCF_NO_EXTENSION
       span_method = UF_CURVE_OCF_SPAN_NONE
     */
    UF_CALL(UF_CURVE_init_ocf_data( &ocf_data ));

    /* Set the tolerances */
    ocf_data.dist_tol = 0.0001;
    ocf_data.string_tol = ocf_data.dist_tol;
    ocf_data.ang_tol = 0.5;

    UF_CALL(UF_CURVE_add_faces_ocf_data( face_collector, &ocf_data ));

    /* Get the reference point on the section and the default offset direction.
       The default direction is to the left of a section when looked down the
       face normal. Mathematically the default offset direction is cross product
       of face normal and section tangent at the offset point. */
    UF_CALL( UF_CURVE_ocf_offset_pt_direction( section_tag, face_collector, offset_point, offset_direction_vec ));

    /* Using the offset_point and offset direction vec, we can decide we want to offset curves
       in the default direction or not. In this case for the given section and faces, offseting
       the curve in default direction will produce curves which will lie outside the face.
       So, we will the offset_direction to be -1, so that curves will lie on the face.

       Please note that the offset curve on face allows you to create the curves outside the
       face boundary as long there is surface. You will have set following option to do this
           cross_boundary_mode = UF_CURVE_OCF_CROSS_BOUNDARIES

       In this example if you want the offset curves on the extension of blend faces then
       set the above option and offset_direction to "1".
     */
    strcpy ( offset_distances.string , "1.0");

    UF_CALL( UF_CURVE_add_string_to_ocf_data( section_tag, offset_direction, 1, &offset_distances, &ocf_data ) );

    UF_CALL(UF_CURVE_create_ocf_feature( &ocf_data, &ocf_feature ) );

    UF_free ( blend_edges );
    UF_free ( blend_faces );
}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
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
