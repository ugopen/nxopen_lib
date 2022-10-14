/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *         UF_DRF_create_concir_dim                                           *
 *                                                                            *
 *                  *
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_drf.h>
#include <uf_curve.h>
#include <uf_csys.h>

void ufusr(char *param, int *retcod, int param_len)
{
   int status = 0;
   static double origin[3] = {18.0, 11.0, 0.0};
   static char dimtxt[15+1] = "CONCIR DIM TEXT";
   static char apptxt[3][132+1] = {"APPENDED TEXT",
                                   "APP TXT LINE 2",
                                   "APP TXT LINE 3"};
   char  stat_msg[133];
   tag_t wcs, arc1_tag = 0, arc2_tag = 0, dimension_tag;
   UF_CURVE_arc_t  arc_coords;
   UF_DRF_object_t arc1, arc2;
   UF_DRF_text_t   drf_text;

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&arc1);
      UF_DRF_init_object_structure(&arc2);

      /* load drf_text specification */
      drf_text.user_dim_text  = dimtxt;
      drf_text.lines_app_text = 3;
      drf_text.appended_text  = apptxt;

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
      arc_coords.start_angle = 0.0;
      arc_coords.end_angle = 1.5 * PI;
      arc_coords.radius = 3.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc2_tag);
   }

   if (!status)
   {
      /* create a concentric circle dimension */
      arc1.object_tag = arc1_tag;
      arc1.object_view_tag = NULL_TAG;
      arc1.object_assoc_type = UF_DRF_arc_center;
      arc1.object_assoc_modifier = 0;
      arc2.object_tag = arc2_tag;
      arc2.object_view_tag = NULL_TAG;
      arc2.object_assoc_type = UF_DRF_arc_center;
      arc2.object_assoc_modifier = 0;
      status = UF_DRF_create_concir_dim(&arc1, &arc2, &drf_text,
               origin, &dimension_tag);
   }

   printf("UF_DRF_create_concir_dim ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("has ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("is successful.\n");

   UF_terminate();
}
