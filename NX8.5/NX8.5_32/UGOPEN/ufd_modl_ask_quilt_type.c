/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_quilt_type                                             *
 *         UF_MODL_edit_quilt                                                 *
 *         UF_MODL_free_quilt                                                 *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example code creates a quilt.prt which demonstrates the    *
 *   calling sequence for the quilt functions.                                *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_part.h>
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

static void do_ugopen_api(void)
{

    double block_origin[3]={0,1,0};
    double tol[3]={0.1,0.1,0.1};
    double distance_tol=0.01;
    double angle_tol=0.5;
    double pt1[3],pt2[3],pt3[3],value[6];

    char   *part_name="quilt";
    char   *block_length[3] = {"2","2","2"};
    char   project_limit[] = {"0.5"};
    char   inside_angle[] = {"90.0"};
    char   edge_angle[] = {"90.0"};
    char   inside_dist[] = {"0.01"};
    char   edge_dist[] = {"0.01"};

    int    units=2,err,tolerance_achieved;
    int    arc_mode=1;
    int    align=1,end_point=0,body_type=0;

    tag_t  part_tag,arc1_tag,arc2_tag,sheet_tag,face_tag,block_tag;
    tag_t target_faces[1],quilt_tag,bsurface_tag;   
    
    UF_MODL_quilt_type_t quilt_type;

    UF_STRING_t   guide,spine,cross;

    uf_list_p_t edge_list,face_list;
        
    UF_MODL_quilt_data_structures_u quilt_structure,ask_quilt_structure;

    UF_MODL_curve_mesh_along_driver_normals_data_t quilt_data2;   
    UF_MODL_b_surface_along_fixed_vector_data_t quilt_data3,*ask_ptr;   

    /* Open a new part */
    UF_PART_new(part_name, units, &part_tag);
    
    /* Create 2 arcs for guide strings for ruled surface */
    pt1[0] =   0.0; pt1[1] =  0.0; pt1[2] =   0.0;
    pt2[0] =   0.5; pt2[1] = 0.05; pt2[2] =   0.0;
    pt3[0] =   1.0; pt3[1] =  0.0; pt3[2] =   0.0;
    FTN(uf5063) (&arc_mode,pt1,pt2,pt3,&arc1_tag);

    pt1[0] =   0.0; pt1[1] =  0.0; pt1[2] =   1.0;
    pt2[0] =   0.5; pt2[1] = 0.05; pt2[2] =   1.0;
    pt3[0] =   1.0; pt3[1] =  0.0; pt3[2] =   1.0;
    FTN(uf5063) (&arc_mode,pt1,pt2,pt3,&arc2_tag);

    UF_MODL_create_string_list(2,2,&guide);

    guide.num = 2;
    guide.string[0] = 1;
    guide.dir[0] = 1;
    guide.id[0] = arc1_tag;
    guide.string[1] = 1;
    guide.dir[1] = 1;
    guide.id[1] = arc2_tag;
    spine.num = 0;
    
    /* Create ruled surface */
    UF_MODL_create_ruled(&guide,
                       	      &spine,
                         &align,
                         value,
                         &end_point,
                         &body_type,
                         UF_NULLSIGN,
                         tol,
                         &sheet_tag);

    /* Get the tag to the face */
    UF_MODL_ask_body_faces(sheet_tag, &face_list); 
    
    UF_MODL_ask_list_item(face_list, 0, &face_tag);

    UF_MODL_delete_list(&face_list);
                          
    /* Get the edges of the face */
    UF_MODL_ask_face_edges(face_tag, &edge_list);
                           
    /* Set up a string for the cross curves. Find the two edges opposite
       the guide strings of the ruled surface to use as the cross curves.
    */
    UF_MODL_create_string_list(2,2,&cross);

    cross.num = 2;
    cross.string[0] = 1;
    cross.dir[0] = 1;
    UF_MODL_ask_list_item(edge_list, 1, &cross.id[0]);
    cross.string[1] = 1;
    cross.dir[1] = 1;
    UF_MODL_ask_list_item(edge_list, 3, &cross.id[1]);

    UF_MODL_delete_list(&edge_list);

    /* Convert the ruled surface to a B-surface to be used as the
       driver surface.
    */
    FTN(uf5444)(&face_tag, &distance_tol, &angle_tol,
			&bsurface_tag, &err);
                       
    /* Create a block */
    UF_MODL_create_block1(UF_NULLSIGN, block_origin, block_length,
                          &block_tag);
    
    /* Find the faces of the block. */
    UF_MODL_ask_feat_faces(block_tag, &face_list);             
    
    /* Grab one of the faces to be used as the target face. */
    UF_MODL_ask_list_item(face_list, 3, &target_faces[0]);
                          
    UF_MODL_delete_list(&face_list);
                          
    /* Set up the structures to define a quilt surface with a
       driver type of Mesh of Curves. The projection type will be
       Along Driver Normals. Use the two guide curves as the
       primary curves and two edge curves of the ruled surface as
       the cross curves.
    */
    quilt_type = UF_MODL_CURVE_MESH_ALONG_DRIVER_NORMALS;
    quilt_data2.quilt_data.check_overlap =
                                    UF_MODL_OVERLAP_CHECK_OFF;
    quilt_data2.quilt_data.num_target_faces = 1;
    quilt_data2.quilt_data.target_faces = target_faces;
    quilt_data2.quilt_data.inside_distance = inside_dist;
    quilt_data2.quilt_data.inside_angle = inside_angle;
    quilt_data2.quilt_data.edge_distance = edge_dist;
    quilt_data2.quilt_data.edge_angle = edge_angle;
    quilt_data2.primary_curves = &guide;
    quilt_data2.cross_curves = &cross;
    quilt_data2.projection_limit = project_limit;
    quilt_structure.quilt_type2 = &quilt_data2;
        
    /* Create the quilt surface */
    UF_CALL(UF_MODL_create_quilt(quilt_type,
                                 &quilt_structure,
                                 &quilt_tag,
				 &tolerance_achieved));

    UF_MODL_free_string_list(&guide);
    UF_MODL_free_string_list(&cross);

    /* Set up the structures to define a quilt surface with a
       driver type of B Surface. The projection type will be Along
       Fixed Vector (+Y). Use the b-surface created from the ruled
       surface as the driver surface.
    */
    quilt_type = UF_MODL_B_SURFACE_ALONG_FIXED_VECTOR;
    quilt_data3.quilt_data.check_overlap =
                             UF_MODL_OVERLAP_CHECK_OFF;
    quilt_data3.quilt_data.num_target_faces = 1;
    quilt_data3.quilt_data.target_faces = target_faces;
    quilt_data3.quilt_data.inside_distance = inside_dist;
    quilt_data3.quilt_data.inside_angle = inside_angle;
    quilt_data3.quilt_data.edge_distance = edge_dist;
    quilt_data3.quilt_data.edge_angle = edge_angle;
    quilt_data3.driver_surface = bsurface_tag;
    quilt_data3.projection_vector[0] = 0;
    quilt_data3.projection_vector[1] = 1;
    quilt_data3.projection_vector[2] = 0;
    quilt_structure.quilt_type3 = &quilt_data3;
        
    /* Edit the previously created quilt surface to have the new
       definition.
    */
    UF_CALL(UF_MODL_edit_quilt(quilt_type, &quilt_structure,
					   quilt_tag));

    /* Find the type of quilt surface. */
    UF_CALL(UF_MODL_ask_quilt_type(quilt_tag, &quilt_type));

    /* Retrieve the quilt defining data. */
    UF_CALL(UF_MODL_ask_quilt(quilt_tag, &quilt_type,
		              &ask_quilt_structure)); 

    /* Modify the defining data slightly - increase the inside
	 distance tolerance from .01 to .05 and change the Y vector
	 component from 1 to .9. */
    
    ask_ptr = ask_quilt_structure.quilt_type3;
    strcpy(ask_ptr->quilt_data.inside_distance,"0.05"); 
    ask_ptr->projection_vector[1] = 0.9;

    /* Edit the quilt surface to have the new definition. */
    UF_CALL(UF_MODL_edit_quilt(quilt_type, &ask_quilt_structure,
                               quilt_tag)); 


    /* Free the memory allocated by UF_MODL_ask_quilt. */
    UF_CALL(UF_MODL_free_quilt(quilt_type, &ask_quilt_structure)); 
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
