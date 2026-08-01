/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function programs:      *
 *                                                                            *
 *         UF_DRF_create_ordorigin                                            *
 *         UF_DRF_create_ordmargin                                            *
 *         UF_DRF_create_orddimension                                         *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_drf.h>
#include <uf_curve.h>
#include <uf_csys.h>

void ufusr(char *param, int *retcod, int param_len)
{
   int status = 0;
   /* positive quadrant: 1 = upper right; 2 = upper left  */
   /*                    3 = lower right; 4 = lower left  */
   /*                    5 = all quadrants                */
   static int pos_quad = 1;
   /* arrow display: 1 = no; 2 = yes */
   static int arrow_disp = 2;
   /* origin symbol display: 1 = origin name; 2 = no display */
   static int origin_disp = 1;
   /* margin type: 1 = horizontal;  2 = vertical */
   static int margin_type = 1;
   /* dimension type: 1 = horizontal;  2 = vertical */
   static int dim_type = 1;
   /* text origin flag: 1 = center of total text box     */
   /*                   2 = center of dimension text box */
   static int text_origin = 1;
   static double offset = 3.0;
   /* distance from object center for dogleg */
   static double dogleg_dist  = 1.0;
   static double dogleg_angle = 30.0;
   static double origin[3] = {-5.0, -5.0, 0.0};
   static char user_text[133];
   static char append_text[4][133];
   char   stat_msg[133];
   tag_t wcs, arc1_tag = 0, arc2_tag = 0, line_tag = 0;
   tag_t origin_tag = 0, margin_tag = 0, dimension_tag;
   UF_CURVE_arc_t  arc_coords;
   UF_CURVE_line_t line_coords;
   UF_DRF_object_t object;
   UF_DRF_text_t   drf_text;

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&object);

      /* create two arcs */
      UF_CSYS_ask_wcs(&wcs);
      UF_CSYS_ask_matrix_of_object(wcs, &arc_coords.matrix_tag);
      arc_coords.start_angle = 0.0;
      arc_coords.end_angle = TWOPI;
      arc_coords.arc_center[0] = 15.0;
      arc_coords.arc_center[1] = 15.0;
      arc_coords.arc_center[2] =  0.0;
      arc_coords.radius = 1.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc1_tag);
   }

   if (!status)
   {
      arc_coords.arc_center[0] = 25.0;
      arc_coords.arc_center[1] =  5.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc2_tag);
   }

   if (!status)
   {
      /* create a line */
      line_coords.start_point[0] = 0.0;
      line_coords.start_point[1] = 0.0;
      line_coords.start_point[2] = 0.0;
      line_coords.end_point[0] = 4.0;
      line_coords.end_point[1] = 0.0;
      line_coords.end_point[2] = 0.0;
      status = UF_CURVE_create_line(&line_coords, &line_tag);
   }

   if (!status)
   {
      /* create an ordinate origin */
      strcpy (user_text, "ORD ORG");
      object.object_tag = arc1_tag;
      object.object_view_tag = NULL_TAG;
      object.object_assoc_type = UF_DRF_arc_center;
      object.object_assoc_modifier = 0;
      status = UF_DRF_create_ordorigin(&object, pos_quad, arrow_disp,
               origin_disp, user_text, &origin_tag);
   }

   if (!status)
   {
      /* create an ordinate margin */
      object.object_tag = line_tag;
      object.object_view_tag = NULL_TAG;
      object.object_assoc_type = UF_DRF_end_point;
      object.object_assoc_modifier = UF_DRF_last_end_point;
      status = UF_DRF_create_ordmargin(margin_type, origin_tag,
               &object, NULL, NULL, offset, &margin_tag);
   }

   if (!status)
   {
      /* create an ordinate dimension */
      strcpy (user_text, "");
      strcpy (append_text[0], "ORD DIM");
      /* load drf_text specification */
      drf_text.user_dim_text  = user_text;
      drf_text.lines_app_text = 1;
      drf_text.appended_text  = append_text;
      object.object_tag = arc2_tag;
      object.object_view_tag = NULL_TAG;
      object.object_assoc_type = UF_DRF_arc_center;
      object.object_assoc_modifier = 0;
      status = UF_DRF_create_orddimension(margin_tag, dim_type, &object,
               dogleg_angle, dogleg_dist, &drf_text, text_origin, origin,
               &dimension_tag);
   }

   printf("UF_DRF_create_ordorigin,_ordmargin,_orddimension ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("have ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("are successful.\n");

   UF_terminate();
}
