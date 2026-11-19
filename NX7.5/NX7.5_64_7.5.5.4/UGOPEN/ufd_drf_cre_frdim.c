/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *         UF_DRF_create_foldedradius_dim                                     *
 *                                                                            *
 *                 *
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
   static char user_text[133];
   static char append_text[4][133];
   char  stat_msg[133];
   double fold_pt[3], fold_angle, origin[3];
   tag_t wcs, arc1_tag = 0, arc2_tag = 0, dimension_tag;
   UF_CURVE_arc_t  arc_coords;
   UF_DRF_object_t object1, object2;
   UF_DRF_text_t   drf_text;

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&object1);
      UF_DRF_init_object_structure(&object2);

      strcpy(user_text, "");
      strcpy(append_text[0], "One");
      strcpy(append_text[1], "Two");
      strcpy(append_text[2], "Three");
      /* load drf_text specification */
      drf_text.user_dim_text  = user_text;
      drf_text.lines_app_text = 3;
      drf_text.appended_text  = append_text;

      /* create two arcs */
      UF_CSYS_ask_wcs(&wcs);
      UF_CSYS_ask_matrix_of_object(wcs, &arc_coords.matrix_tag);
      arc_coords.start_angle = 0.0;
      arc_coords.end_angle = TWOPI;
      arc_coords.arc_center[0] = 10.0;
      arc_coords.arc_center[1] = 10.0;
      arc_coords.arc_center[2] =  0.0;
      arc_coords.radius = 1.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc1_tag);
   }

   if (!status)
   {
      arc_coords.arc_center[0] = 15.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc2_tag);
   }

   if (!status)
   {
      fold_angle = 45.0;
      fold_pt[0] = 5.0;
      fold_pt[1] = 0.0;
      fold_pt[2] = 0.0;
      origin[0] = -4.0;
      origin[1] = 15.0;
      origin[2] =  0.0;
      object1.object_tag = arc1_tag;
      object1.object_view_tag = NULL_TAG;
      object1.object_assoc_type = UF_DRF_end_point;
      object1.object_assoc_modifier = UF_DRF_first_end_point;
      object2.object_tag = arc2_tag;
      object2.object_view_tag = NULL_TAG;
      object2.object_assoc_type = UF_DRF_end_point;
      object2.object_assoc_modifier = UF_DRF_first_end_point;
      status = UF_DRF_create_foldedradius_dim(&object1, &object2,
               fold_pt, fold_angle, &drf_text, origin, &dimension_tag);
   }

   printf("UF_DRF_create_foldedradius_dim ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("has ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("is successful.\n");

   UF_terminate();
}
