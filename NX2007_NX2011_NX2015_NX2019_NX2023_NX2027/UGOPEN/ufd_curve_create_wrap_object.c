/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine:         *
 *                                                                            *
 *         UF_CURVE_create_wrap_object                                        *
 *         UF_CURVE_ask_wrap_curves                                           *
 *         UF_CURVE_ask_wrap_curve_parents                                    *
 *         UF_CURVE_ask_wrap_parms                                            *
 *         UF_CURVE_edit_wrap_object                                          *
 *         UF_CURVE_free_wrap_parms                                           *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates wrap_example_o.prt. The code creates       *
 *   a cone, circle, and lines. The code then demonstrates the wrap functions.*
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <uf.h>
#include <uf_curve.h>
#include <uf_csys.h>
#include <uf_defs.h>
#include <uf_modl.h>
#include <uf_modl_error.h>
#include <uf_mtx.h>
#include <uf_obj.h>
#include <uf_object_types.h>
#include <uf_part.h>
#include <uf_ui.h>

/* Cut line angle for wrap_data. */
static char ang180[]    = {"180"};

/* Output part */
static char *outputPart = "wrap_example_o.prt";
static int  find_type = UF_datum_plane_type;

static int UF_wrap_example(void);

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

  UF_CALL(UF_wrap_example());

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

static int UF_wrap_example(void)
{
    uf_list_p_t face_list;

    int i, index, new_num_input_curves, old_num_input_curves, num_dplane;
    int point_sel[] = {0,0,0}, count, norm_dir, type;
    int num_curves;

    double center[3], dir[3], box[6], radius, rad_data;
    double X_abs[]={1.,0.,0.}, Z_abs[]={0.,0.,1.}, arc_mtx[9];
    double cone_origin[] = {15., 2.5, 0.}, axis[] = {0., 0., 1.};
    double ref_point[] = {15., 1.5, 5.};

    char cone_height[] = "5.", *cone_diams[] = {"5.", "2."};

    UF_CURVE_arc_t arc_coords = {NULL_TAG, 0., TWOPI, 15., 2.5, -7., 2.25};
    UF_CURVE_line_t line1_pts={11., 7., 7., 15., 7., 1.};
    UF_CURVE_line_t line2_pts={19., 7., 7., 15., 7., 1.};

    tag_t outputPartTag, cone_feat_id, input_const[2], dplanes[2], body;
    tag_t arc_id, line1_id, line2_id, face, dplane1, dplane2, face_id;
    tag_t defining_curve, defining_face, defining_plane;
    tag_t *new_input_curves = NULL, *old_input_curves = NULL;
    tag_t wrap_curve_object, wrap_tag, *output_curve_tags = NULL;
   
    UF_CURVE_wrap_data_t              ask_wrap_data;
    UF_CURVE_wrap_data_t              wrap_data;

/* ================ Create the file and input geometry ==================*/
    /* Create a new, empty part file */
 
    if (UF_CALL(UF_PART_new(outputPart,UF_PART_ENGLISH,&outputPartTag)))
    {
        return( PROCESS_FAILURE );
    }

    /* build a cone and get the id of the conical face */
    UF_CALL(UF_MODL_create_cone1(UF_NULLSIGN, cone_origin,
                    cone_height, cone_diams, axis, &cone_feat_id));
    UF_CALL(UF_MODL_create_list(&face_list));
    UF_CALL(UF_MODL_ask_feat_body(cone_feat_id, &body));
    UF_CALL(UF_MODL_ask_body_faces(body,&face_list));
    UF_CALL(UF_MODL_ask_list_count(face_list, &count));
    for(i = 0; i < count; i++)
    {
      UF_CALL(UF_MODL_ask_list_item(face_list, i, &face));
      UF_CALL(UF_MODL_ask_face_data(face, &type, center, dir, box, &radius,
                              &rad_data, &norm_dir));
        if(type == UF_cone_type) face_id = face;
    }
    UF_CALL(UF_MODL_delete_list(&face_list));

    /* build a datum plane through the axis of the cone and get its id */
    input_const[0] = face_id;
    UF_CALL(UF_MODL_create_relative_dplane (1, input_const, point_sel, 
                           1, NULL, NULL, NULL, &num_dplane, dplanes));
    dplane1 = NULL_TAG;
    UF_CALL(UF_OBJ_cycle_objs_in_part(outputPartTag, find_type, &dplane1));

    /* build a datum plane tangent to the cone, normal to datum plane 1 */
    input_const[0] = face_id;
    input_const[1] = dplane1;
    UF_CALL(UF_MODL_create_relative_dplane ( 2, input_const, point_sel,
                        2, ref_point, NULL, NULL, &num_dplane, dplanes ));
    dplane2 = dplane1;
    UF_CALL(UF_OBJ_cycle_objs_in_part(outputPartTag, find_type, &dplane2));

    /* build a circle and lines to be wrapped */
    UF_CALL(UF_MTX3_initialize (X_abs, Z_abs, arc_mtx));
    UF_CALL(UF_CSYS_create_matrix(arc_mtx, &arc_coords.matrix_tag));
    UF_CALL(UF_CURVE_create_arc(&arc_coords, &arc_id));
    UF_CALL(UF_CURVE_create_line(&line1_pts, &line1_id));
    UF_CALL(UF_CURVE_create_line(&line2_pts, &line2_id));
                     
/* ================== Demonstrate the wrap functions =====================*/

    /* creation defaults: yellow on layer 3 */
    UF_CALL(UF_OBJ_modify_defaults( 6, 3, -1, -1 ));

    /* Initialize wrap_data structure */
    wrap_data.wrap_unwrap_sw = UF_CURVE_WRAP;
    wrap_data.num_wrap_faces = 1;
    wrap_data.wrap_faces = &face_id;
    wrap_data.wrap_plane = dplane2;
    wrap_data.num_input_curves = 1;
    wrap_data.input_curves = &arc_id;
    wrap_data.cut_line_angle = ang180;
    UF_MODL_ask_distance_tolerance(&wrap_data.distance_tol);
    UF_MODL_ask_angle_tolerance(&wrap_data.angle_tol);

    /* Create the wrap object */
    wrap_tag = 0;
     
    if ( UF_CALL(UF_CURVE_create_wrap_object ( &wrap_data,
                                  &wrap_tag)) )
    {
      
        return( PROCESS_FAILURE );
    }

    UF_CALL(UF_MODL_update()); 

    /* Get a list of all the output curves created above. */ 
    if ( UF_CALL(UF_CURVE_ask_wrap_curves (wrap_tag,
                                           &num_curves,
                                           &output_curve_tags)) )
    {
        return( PROCESS_FAILURE );
    }

    /* Loop through the output curves, examining each curve's */
    /* defining data.                                         */
    for ( index = 0; index < num_curves; index++)
    {
        
        if ( UF_CALL(UF_CURVE_ask_wrap_curve_parents
            (
                output_curve_tags[index],
                &defining_face,
                &defining_plane,
                &defining_curve,
                &wrap_curve_object
            )) )
        {
            return( PROCESS_FAILURE );
        }
    }

    /* Free the storage allocated by UF_CURVE_ask_wrap_curves */
    UF_free(output_curve_tags);

    /* Get the parameters from the created wrap object in preparation */
    /* for an edit.                                                   */
    ;
    if ( UF_CALL(UF_CURVE_ask_wrap_parms ( wrap_tag,
                                      &ask_wrap_data )) )
    {
        return( PROCESS_FAILURE );
    }

    /* Add two additional input curves. */
    old_num_input_curves = ask_wrap_data.num_input_curves;
    old_input_curves = ask_wrap_data.input_curves;
    new_num_input_curves = old_num_input_curves + 2;
    new_input_curves = (tag_t *)malloc( new_num_input_curves * 
                                        sizeof(tag_t));
    for ( index = 0; index < old_num_input_curves; index++ )
        new_input_curves[index] = old_input_curves[index];
    new_input_curves[index++] = line1_id;
    new_input_curves[index++] = line2_id;

    ask_wrap_data.num_input_curves = new_num_input_curves;
    ask_wrap_data.input_curves = new_input_curves;
    UF_CALL(UF_CURVE_edit_wrap_object ( &ask_wrap_data,
                                             wrap_tag )); 

    /* Free the memory allocated for the new input_curves tag list and put */
    /* the ask_wrap_data structure back the way it was for                 */
    /* UF_CURVE_free_wrap_parms to free it correctly.                      */
    free (new_input_curves);
    ask_wrap_data.num_input_curves = old_num_input_curves;
    ask_wrap_data.input_curves = old_input_curves;
    
    /* Free the storage allocated by UF_CURVE_ask_wrap_parms */
    if ( UF_CALL(UF_CURVE_free_wrap_parms ( &ask_wrap_data )) )
    {
          return( PROCESS_FAILURE );
    }
    UF_CALL(UF_MODL_update()); 
    return ( 0 );
}
