/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_UI_specify_screen_position                                      *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   
 *   The following example requiers an open part and allows you to create a   *
 *   circle on an arbitrary plane. The circle is defined by indicating a      *
 *   center position, followed by a position on the circle itself. As you     *
 *   move the cursor to the latter position, the motion callback (passed to   *
 *   UF_UI_specify_screen_position) will render a visual representation of    *
 *   the circle you're about to create, as well as a bounding box around the  *
 *   circle, an arc from 15 degrees to 345 degrees with radius=1.0, and a     *
 *   "rubberband" line from the circle center the cursor. This example        *
 *   supports Design in Context (that is, your Work part may be different     *
 *   than your Displayed part).                                               *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf_defs.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_csys.h>
#include <uf_vec.h>
#include <uf_disp.h>
#include <uf_curve.h>
#include <uf_mtx.h>
#include <uf_obj.h>
typedef struct
        { UF_CURVE_arc_t  *arc;
          double          abs_ctr[3];
          double          matrix[9];
          double          x_axis[3];
          double          y_axis[3];
        } my_motion_data_t;

/* Define a motion callback to render a visual representation of
 * the circle to be created, along with a bounding box around the
 * circle, an arc of radius 1.0, and a "rubberband" line from the
 * center to the cursor position.
 */
static void motion_cb( double                   *screen_pos,
                       UF_UI_motion_cb_data_p_t  motion_cb_data,
                       my_motion_data_t        *my_data )
{
    double radius, pos_array[5][3];
    double xrad[3], yrad[3], x_y_vec[3], x_ny_vec[3];
    /* Calculate the arc radius:  the distance from the arc center
     * to the current screen position.
     */
    UF_VEC3_distance( my_data->abs_ctr, screen_pos, &radius );
    /* Map the arc center to the "csys of the arc".
     */
    UF_MTX3_vec_multiply( my_data->abs_ctr,
                       my_data->matrix,
                       my_data->arc->arc_center );
    /* Draw a circle and an arc in the view of the cursor.
     */
    UF_DISP_display_ogp_circle( motion_cb_data->view_tag,
                            my_data->matrix,
                            my_data->arc->arc_center,
                            radius );
    UF_DISP_display_ogp_arc(    motion_cb_data->view_tag,
                             my_data->matrix,
                             15.0*DEGRA, 345.0*DEGRA,
                             my_data->arc->arc_center,
                             1.0 );
    /* Draw a bounding box around the circle.
     */
    UF_VEC3_scale( radius, my_data->x_axis, xrad );
    UF_VEC3_scale( radius, my_data->y_axis, yrad );
    UF_VEC3_add( xrad, yrad, x_y_vec  );
    UF_VEC3_sub( xrad, yrad, x_ny_vec );
    UF_VEC3_add( my_data->abs_ctr, x_y_vec,  pos_array[0] );
    UF_VEC3_sub( my_data->abs_ctr, x_ny_vec, pos_array[1] );
    UF_VEC3_sub( my_data->abs_ctr, x_y_vec,  pos_array[2] );
    UF_VEC3_add( my_data->abs_ctr, x_ny_vec, pos_array[3] );
    UF_VEC3_add( my_data->abs_ctr, x_y_vec,  pos_array[4] );
    UF_DISP_display_ogp_polyline( motion_cb_data->view_tag,
                              pos_array, 5 );
    /* Draw a "rubberband" line from the circle center to the
     * cursor position.
     */
    UF_DISP_display_ogp_line( motion_cb_data->view_tag,
                          my_data->abs_ctr,
                          screen_pos );
}

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

    int               default_plane;
    int               plane_resp, ctr_resp, pos_resp;
    tag_t             plane_tag, saved_wcs, mtx_id, csys_id,
                      arc_id, view_tag;
    double            plane_matrix[9], plane_origin[3],
                      x_vec[3], y_vec[3], arc_edge_pos[3];
    double           root_origin[3] = {0.0, 0.0, 0.0};
    double           work_origin[3];
    UF_CURVE_arc_t    arc;
    my_motion_data_t  my_data;
   
    my_data.arc    = &arc;
    arc.start_angle =   0.0;
    arc.end_angle   = TWOPI;    /* Create a full circle. */
    default_plane   = 5;       /* Default plane = WCS */
    do
    {
        /* Specify the plane on which the circle is to be created.
         */
        UF_CALL(UF_UI_specify_plane(
                         "Specify plane for circle creation",
                         &default_plane,
                         1,
                         &plane_resp,
                         plane_matrix,
                         plane_origin,
                         &plane_tag ));
        if (plane_resp ==3)
        {
            /* Save the current WCS for future restoration.
             */
            UF_CSYS_ask_wcs( &saved_wcs );
            /* Move the WCS to the specified plane. This is
             * necessary because the position passed to the motion
             * callback, and the position returned by
             * UF_UI_specify_screen_position, is the screen
             * position projected onto the WCS XY plane.
             */
            if (default_plane != 5)
            {
                UF_CSYS_create_matrix( plane_matrix, &mtx_id );
                UF_CSYS_create_csys(  plane_origin, mtx_id,
                                   &csys_id );
                UF_CSYS_set_wcs( csys_id );
            }
            /* Obtain unit vectors and the arc matrix relative to
             * the Work Part coordinate system.
             */
            UF_MTX3_x_vec( plane_matrix, x_vec );
            UF_MTX3_y_vec( plane_matrix, y_vec );
            UF_CSYS_map_point( UF_CSYS_ROOT_COORDS, x_vec,
                            UF_CSYS_WORK_COORDS, x_vec );
            UF_CSYS_map_point( UF_CSYS_ROOT_COORDS, y_vec,
                            UF_CSYS_WORK_COORDS, y_vec );
            UF_CSYS_map_point( UF_CSYS_ROOT_COORDS, root_origin,
                            UF_CSYS_WORK_COORDS, work_origin );
            UF_VEC3_sub( x_vec, work_origin, my_data.x_axis );
            UF_VEC3_sub( y_vec, work_origin, my_data.y_axis );
            UF_MTX3_initialize( my_data.x_axis, my_data.y_axis,
                             my_data.matrix );
            UF_CSYS_create_matrix( my_data.matrix,
                                &arc.matrix_tag );
            do
            {
                UF_CALL(UF_UI_specify_screen_position(
                                "Specify arc center",
                                NULL,
                                NULL,
                                my_data.abs_ctr,
                                &view_tag,
                                &ctr_resp ));
                if (ctr_resp == UF_UI_PICK_RESPONSE)
                {
                    /* Map the arc center to the arc csys.
                     */
                    UF_MTX3_vec_multiply( my_data.abs_ctr,
                                          my_data.matrix,
                                          arc.arc_center );
                    UF_CALL(UF_UI_specify_screen_position(
                                    "Indicate arc radius",
                                    (UF_UI_motion_fn_t)motion_cb,
                                    (void *)&my_data,
                                    arc_edge_pos,
                                    &view_tag,
                                    &pos_resp ));
                    /* If a position was obtained, create the
                     * circle.
                     */
                    if (pos_resp == UF_UI_PICK_RESPONSE)
                    {
                        UF_VEC3_distance( my_data.abs_ctr,
                                        arc_edge_pos,
                                        &arc.radius );
                        UF_CURVE_create_arc( &arc, &arc_id );
                    }
                }
            } while ( (ctr_resp == UF_UI_PICK_RESPONSE) &&
                     (pos_resp != UF_UI_CANCEL)           );
            /* Restore the WCS if it was altered above.
             */
            if (default_plane != 5)
            {
                UF_CSYS_set_wcs( saved_wcs );
                UF_OBJ_delete_object( csys_id );
            }
        }
    } while (ctr_resp == UF_UI_BACK && plane_resp == 3);
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
