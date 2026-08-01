/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *         UF_DRF_create_sym_cline                                            *
 *                                                                            *
 
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
   char stat_msg[133];
   tag_t wcs, arc1_tag, arc2_tag, cl_tag;
   UF_CURVE_arc_t  arc_coords;
   UF_DRF_object_t object1, object2;

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&object1);
      UF_DRF_init_object_structure(&object2);

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
      arc_coords.arc_center[1] = 15.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc2_tag);
   }

   if (!status)
   {
      object1.object_tag = arc1_tag;
      object1.object_view_tag = NULL_TAG;
      object1.object_assoc_type = UF_DRF_end_point;
      object1.object_assoc_modifier = UF_DRF_first_end_point;
      object2.object_tag = arc2_tag;
      object2.object_view_tag = NULL_TAG;
      object2.object_assoc_type = UF_DRF_end_point;
      object2.object_assoc_modifier = UF_DRF_first_end_point;

      /* create a symmetrical centerline */ 
      status = UF_DRF_create_sym_cline(&object1, &object2, &cl_tag);
   }

   printf("UF_DRF_create_sym_cline ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("has ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("is successful.\n");

   UF_terminate();
}
