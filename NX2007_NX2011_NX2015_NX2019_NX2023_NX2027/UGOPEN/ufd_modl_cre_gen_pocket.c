/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_create_general_pocket                                      *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates pocket.prt via code that invokes commands  *
 *   to create a block, a set of outline curves for the placement outline of  *
 *   the pocket, and then a pocket with a taper angle of 20 degrees, relative *
 *   to the face normals. Then the parameters of the pocket are asked for and *
 *   printed out, the taper angle of the pocket is changed to 30 degrees, and *
 *   finally the output parameters from UF_MODL_ask_general_pocket are freed. *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_modl.h>
#include <uf_curve.h>
#include <uf_csys.h>
#include <uf_part.h>
#include <string.h>

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
    int    units= UF_PART_METRIC;
    int    num_faces,ii;

    char   *part_name="pocket";
    char   radius[133] = {"3.0"};
    char   *edge_lens[] = {"100.0","50.0","100.0"};

    double origin[3]={0.0,0.0,0.0};
    double face_param[2],face_point[3],face_u_deriv1[3];
    double face_v_deriv1[3],face_u_deriv2[3],face_v_deriv2[3];
    double face_normal[3],face_radii[2];
    double matrix_values[9] = { 1, 0, 0, 0, 0, 1, 0, 1, 0 };


    uf_list_p_t face_list;

    UF_CURVE_line_t line1, line2, line3;
    UF_CURVE_arc_t arc1, arc2, arc3;


    UF_MODL_faces_t placement_faces,selected_floor_faces;
    UF_MODL_offset_trans_faces_t floor_faces;
    UF_MODL_pocketpad_outline_t placement_outline;
    UF_MODL_project_curves_t outline_curves;
    UF_MODL_parm_t placement_radius,floor_radius;
    UF_MODL_vector_t placement_proj_vector = 
		{0,UF_MODL_VECTOR_DIRECTION,
		 {0,1,0}};
    UF_MODL_parm_t taper_angle = 
		{UF_MODL_PARM_CONSTANT,
		 {"20.0"}};
    UF_MODL_faces_t out_placement_faces;
    UF_MODL_offset_trans_faces_t out_floor_faces;
    UF_MODL_pocketpad_outline_t out_outline;
    UF_MODL_parm_t out_placement_radius,out_floor_radius;

    tag_t  part_tag,block_tag;
    tag_t  place_face[1],floor_face[1],general_pocket_tag;
    tag_t  placement_curves[6],face_tag;
    tag_t matrix_tag;

    UF_PART_new(part_name, units, &part_tag);

/* create the block */
    UF_CALL(UF_MODL_create_block1(UF_NULLSIGN,
                          origin,
                          edge_lens,
                          &block_tag));

/* create the matrix for arcs */
    UF_CALL(UF_CSYS_create_matrix(matrix_values, &matrix_tag));

/* create the placement outline curves */
/* create an arc */
    arc1.matrix_tag = matrix_tag;
    arc1.start_angle = 0.0;
    arc1.end_angle = 90.0 * DEGRA;
    arc1.arc_center[0] = 75.0;
    arc1.arc_center[1] = 70.0;
    arc1.arc_center[2] = 0.0;
    arc1.radius =  10.0;
    UF_CALL(UF_CURVE_create_arc(&arc1, &placement_curves[0]));

/* create a straight line */
    line1.start_point[0] =  85.0;
    line1.start_point[1] =  0.0;
    line1.start_point[2] =  70.0;
    line1.end_point[0] =  85.0;
    line1.end_point[1] =  0.0;
    line1.end_point[2] =  50.0;
    UF_CALL(UF_CURVE_create_line(&line1, &(placement_curves[1])));

/* create an arc */
    arc2.matrix_tag = matrix_tag;
    arc2.start_angle =  248.198590513650 * DEGRA;
    arc2.end_angle = 360.0 * DEGRA;
    arc2.arc_center[0] = 75.0;
    arc2.arc_center[1] = 50.0;
    arc2.arc_center[2] = 0.0;
    arc2.radius =  10.0;
    UF_CALL(UF_CURVE_create_arc(&arc2, &placement_curves[2]));


/* create a straight line */
    line2.start_point[0] =  71.2860932364590;
    line2.start_point[1] =  0.0; 
    line2.start_point[2] =  40.7152330911470;
    line2.end_point[0] =  21.2860932364590;
    line2.end_point[1] =  0.0; 
    line2.end_point[2] =  60.7152330911470;
    UF_CALL(UF_CURVE_create_line(&line2, &(placement_curves[3])));

/* create an arc */
    arc3.matrix_tag = matrix_tag;
    arc3.start_angle = 90.0 * DEGRA;
    arc3.end_angle =  248.198590513650 * DEGRA;
    arc3.arc_center[0] = 25.0;
    arc3.arc_center[1] = 70.0;
    arc3.arc_center[2] = 0.0;
    arc3.radius =  10.0;
    UF_CALL(UF_CURVE_create_arc(&arc3, &placement_curves[4]));

/* create a straight line */
    line3.start_point[0] =  25.0;
    line3.start_point[1] =  0.0;
    line3.start_point[2] =  80.0;
    line3.end_point[0] =  75.0;
    line3.end_point[1] =  0.0;
    line3.end_point[2] =  80.0;
    UF_CALL(UF_CURVE_create_line(&line3, &(placement_curves[5])));


/* determine the placement face from the block,it is the    */
/* face whose normal is mostly in the positive y_direction, */
/* the floor face will be the face whose normal is mostly   */
/* in the negative y_direction                              */
    UF_MODL_ask_feat_faces(block_tag,
                           &face_list);

    UF_MODL_ask_list_count(face_list,
                           &num_faces);

    face_param[0] = 0.5;
    face_param[1] = 0.5;
    for (ii = 0;ii < num_faces;ii++)
    {
      UF_MODL_ask_list_item(face_list,
                            ii,
                            &face_tag);

      UF_MODL_ask_face_props(face_tag,
                             face_param,
                             face_point,
                             face_u_deriv1,face_v_deriv1,
                             face_u_deriv2,face_v_deriv2,
                             face_normal,face_radii);

      if (face_normal[1] > 0.75)
        place_face[0] = face_tag;
      if (face_normal[1] < -0.75)
        floor_face[0] = face_tag;
    }

    UF_MODL_delete_list(&face_list);
/* set up input data to create the pocket */

/* set up data for placement faces */
    placement_faces.number_of_faces = 1;
    placement_faces.faces = place_face;
    placement_faces.face_extension = 
			UF_MODL_FACE_EXTENSION_NONE;

/* set up data for floor faces */
    selected_floor_faces.number_of_faces = 1;
    selected_floor_faces.faces = floor_face;
    selected_floor_faces.face_extension =
			UF_MODL_FACE_EXTENSION_NONE;

    floor_faces.faces = &selected_floor_faces;
    floor_faces.method_type = UF_MODL_OFFSET_OF_FACES;
    strcpy(floor_faces.distance,"-40.0");
    floor_faces.direction = NULL;

/* set up data for placement outline */
    outline_curves.number_of_curves = 6;
    outline_curves.curves = placement_curves;
    outline_curves.curve_projection_type = 
		UF_MODL_PROJ_ALONG_VECTOR;
    outline_curves.curve_projection_vector = 
			&placement_proj_vector;

    placement_outline.outline_type = UF_MODL_SINGLE_OUTLINE;
    placement_outline.defined_by.single_outline.
	outline_curves = &outline_curves;
    placement_outline.defined_by.single_outline.
	curves_represent = UF_MODL_TANGENT_AT_END_OF_BLEND;
    placement_outline.defined_by.single_outline.
	outline_represents = UF_MODL_SHAPE_AT_PLACEMENT;
    placement_outline.defined_by.single_outline.
	taper_angle = &taper_angle;
    placement_outline.defined_by.single_outline.
	taper_relative_to = UF_MODL_TAPER_FACE_NORMALS;
    placement_outline.defined_by.single_outline.
	taper_vector = NULL;

/* set up placement and floor radius */
    placement_radius.method_type = UF_MODL_PARM_CONSTANT;
    strcpy(placement_radius.defined_by.constant.value,radius);
    floor_radius.method_type = UF_MODL_PARM_CONSTANT;
    strcpy(floor_radius.defined_by.constant.value,radius);
/* call the function to create the pocket */
    UF_MODL_create_general_pocket(&placement_faces,
                                  &floor_faces,
                                  &placement_outline,
                                  &placement_radius,
                                  &floor_radius,
                                  &general_pocket_tag);

/* retrieve the pocket parameters and print some of */
/* them out                                         */
    UF_MODL_ask_general_pocket(general_pocket_tag,
                               &out_placement_faces,
                               &out_floor_faces,
                               &out_outline,
                               &out_placement_radius,
                               &out_floor_radius);

printf("The following are the pocket parameters\n");
printf("number of placement faces = %d\n",
       out_placement_faces.number_of_faces);
printf("taper angle = %s\n",
       out_outline.defined_by.single_outline.taper_angle
                                 ->defined_by.constant.value);
printf("floor offset value = %s\n",out_floor_faces.distance);

/* change the taper angle to 30 degrees and modify */
/* the pocket, use the retrieved parameters, and   */
/* just change the taper angle                     */
    strcpy(out_outline.defined_by.single_outline.taper_angle
                          ->defined_by.constant.value,"30.0");
    UF_MODL_edit_general_pocket(general_pocket_tag,
                                &out_placement_faces,
                                &out_floor_faces,
                                &out_outline,
                                &out_placement_radius,
                                &out_floor_radius);

/* free returned parameters */
    UF_MODL_free_general_pocket(&out_placement_faces,
                                &out_floor_faces,
                                &out_outline,
                                &out_placement_radius,
                                &out_floor_radius);

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
