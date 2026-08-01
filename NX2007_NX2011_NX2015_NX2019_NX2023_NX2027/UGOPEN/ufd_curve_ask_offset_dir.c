/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_CURVE_ask_offset_direction_2                                      *
 *         UF_CURVE_create_offset_object                                      *
 *         UF_CURVE_ask_offset_curves                                         *
 *         UF_CURVE_edit_offset_object                                        *
 *         UF_CURVE_ask_offset_parms                                          *
 *         UF_CURVE_free_offset_parms                                         *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example code creates sample.prt. The code illustrates how  *
 *   to set up the inputs and use the outputs of the offset curve routines.   *
 *                                                                            *
                   *
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_part.h>
#include <uf_curve.h>
#include <uf_csys.h>
#include <uf_vec.h>
#include <uf_ui.h>

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
    double tol[3]={0.1,0.1,0.1};
    double value[6], base_point[3];
    double direction_vector[3],draft_direction_vector[3],dot = 1;
    double x_direction[3]={1,0,0};
    double step = 1.0;

    char   *part_name="sample";
    char   distance_str[] = {"0.25"};
    char   neg_distance_str[] = {"-0.25"};

    int    units = UF_PART_ENGLISH,num_curves,i;
    int    align =1,end_point=0,body_type=0, edge_type;

    tag_t  part_tag,arc1_tag,arc2_tag,face_tag,
           sheet_tag,offset_tag,*offset_curves;
    tag_t  wcs;
    

    UF_STRING_t   guide,spine,input_string;
   
    UF_CURVE_arc_t arc_coords;

    uf_list_p_t edge_list,face_list;
        
    UF_CURVE_offset_data_t offset_data, ask_offset_data;

    UF_CURVE_offset_distance_data_t offset_distance1;   

    /* Open a new part */
    
    UF_CALL(UF_PART_new(part_name, units, &part_tag));
    
    /* Create 2 arcs for guide strings for ruled surface */
    
    UF_CALL(UF_CSYS_ask_wcs(&wcs));
    UF_CALL(UF_CSYS_ask_matrix_of_object(wcs, &arc_coords.matrix_tag));
    arc_coords.start_angle = 78.0 * (PI/180);
    arc_coords.end_angle = 101.0 * (PI/180);
    arc_coords.arc_center[0] = 0.5;
    arc_coords.arc_center[1] = -2.4750;
    arc_coords.arc_center[2] = 0.0;
    arc_coords.radius = 2.525;
    
    UF_CALL(UF_CURVE_create_arc(&arc_coords,&arc1_tag));   
  
    arc_coords.arc_center[0] = 0.5;
    arc_coords.arc_center[1] = -1.9750;
    arc_coords.arc_center[2] = 0.0;

    UF_CALL(UF_CURVE_create_arc(&arc_coords,&arc2_tag)); 

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
    
    UF_CALL(UF_MODL_create_ruled(&guide,
                                 &spine,
                                 &align,
                                 value,
                                 &end_point,
                                 &body_type,
                                 UF_NULLSIGN,
                                 tol,
                                 &sheet_tag));

    UF_MODL_free_string_list(&guide);

    /* Get the tag to the face */
    
    UF_CALL(UF_MODL_ask_body_faces(sheet_tag,
                           &face_list)); 
    
    UF_CALL(UF_MODL_ask_list_item(face_list,
                                  0,
                                  &face_tag));

    UF_CALL(UF_MODL_delete_list(&face_list));
                          
    /* Get the edges of the face */
    
    UF_CALL(UF_MODL_ask_face_edges(face_tag,
                           &edge_list));
                           
    /* Set up a string for the input curves. Find the two linear edges */
    /* opposite the guide strings of the ruled surface to use in the string. */
    
    UF_MODL_create_string_list(1,8,&input_string);
    
    input_string.num = 1;
    input_string.string[0] = 4;
    input_string.dir[0] = 1;
    input_string.id[0] = arc1_tag;
    input_string.id[1] = arc2_tag;
    num_curves = 2;
    for(i = 0; i < 4; i++)
    {
      UF_MODL_ask_list_item(edge_list,
                            i,
                            &input_string.id[num_curves]);
      
      UF_MODL_ask_edge_type(input_string.id[num_curves],
                            &edge_type);
      if(edge_type == UF_MODL_LINEAR_EDGE)
         num_curves++;
    }

    UF_MODL_delete_list(&edge_list);

    /* Compute the direction vectors of the string */

    UF_CALL(UF_CURVE_ask_offset_direction_2(&input_string,
                                          direction_vector,
                                          draft_direction_vector,
                                          base_point));
     
    /* Compute the dot product between the direction vector and the +X vector */
    /* This will be used later to determine if we will use a positive or
       negative    */
    /* offset distance. */
   
    UF_VEC3_dot(direction_vector,
                x_direction,
                &dot);
                       
    
    /* Set up the structures to define a non-associative type of offset  */ 
    /* curve. This will use a distance and have a trim method of fillet. */
    
    offset_data.offset_type = UF_CURVE_OFFSET_DISTANCE_FILLET;
    offset_data.input_curves = &input_string;
    offset_data.approximation_tolerance = step;

    UF_MODL_ask_distance_tolerance(&offset_data.string_tolerance);

    offset_data.offset_def.distance_type1 = &offset_distance1;
    offset_distance1.distance = distance_str;

    if (dot >= 0)
    {
      offset_distance1.distance = distance_str;
    }
    else
    { 
      offset_distance1.distance = neg_distance_str;
    }
        
    /* Create the offset curves. */
    
     
    UF_CALL(UF_CURVE_create_offset_curve(&offset_data,
                                         &num_curves,
                                 &offset_curves)); 
    
    UF_free(offset_curves);
    
    /* Set up the structures to define an associative type of offset     */ 
    /* curve. This will use a distance and have a trim method of         */
    /* extended tangents.  (Only need to change the type, all other      */        
    /* parameters were set up previously.                                */        
    
    offset_data.offset_type = UF_CURVE_OFFSET_DISTANCE_TANGENT;
        
    /* Create the offset curve object. */
     
    UF_CALL(UF_CURVE_create_offset_object(&offset_data,
                                  &offset_tag)); 

    /* Get the tags to the output offset curves.  These will be used as */
    /* Input to create the next offset curve object.                    */

    UF_CALL(UF_CURVE_ask_offset_curves(offset_tag,
                                  &num_curves,
                          &offset_curves)); 
      
    /* Modify the input string to pass in the offset curves as input. */

    input_string.string[0] = num_curves;
    for (i=0; i<num_curves; i++)
      input_string.id[i] = offset_curves[i];
       
    UF_free(offset_curves);

    /* Create the new offset curve object.  (This is the way to do  */
    /* multiple copies or multiple Applies interactively.)          */

    UF_CALL(UF_CURVE_create_offset_object(&offset_data,
                                  &offset_tag)); 

    /* Retrieve the parameter information for the last object created.  */

    UF_CALL(UF_CURVE_ask_offset_parms(offset_tag,
                         &ask_offset_data)); 
      
    /* Change the offset type to have no extenstion/trim. */

    ask_offset_data.offset_type = UF_CURVE_OFFSET_DISTANCE_NO_TRIM;

    UF_CALL(UF_CURVE_edit_offset_object(&ask_offset_data,
                                offset_tag)); 

    UF_MODL_update();
    /* Free underlying structures. */
    
    UF_CALL(UF_CURVE_free_offset_parms(&ask_offset_data));
        
    UF_MODL_free_string_list(&input_string); 

}
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
