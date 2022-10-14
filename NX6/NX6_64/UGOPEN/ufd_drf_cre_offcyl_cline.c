/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function programs:      *
 *                                                                            *
 *         UF_DRF_create_offcyl_cline_off                                     *
 *         UF_DRF_create_offcyl_cline_obj                                     *
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
   static double distance;
   tag_t wcs, arc1_tag, arc2_tag, arc3_tag, cl_tag;
   UF_CURVE_arc_t  arc_coords;
   UF_DRF_object_t object1, object2, center;

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&object1);
      UF_DRF_init_object_structure(&object2);
      UF_DRF_init_object_structure(&center);

      /* create three arcs */
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
      arc_coords.arc_center[0] = 20.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc3_tag);
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

      /* create an offset cylindrical centerline:
         keyed-in offset distance */ 
      distance = 2.0;
      status = UF_DRF_create_offcyl_cline_off(&object1, &object2,
               distance, &cl_tag);
   }

   if (!status)
   {
      /* create an offset cylindrical centerline:
         calculate offset distance from object */ 
      center.object_tag = arc3_tag;
      center.object_view_tag = NULL_TAG;
      center.object_assoc_type = UF_DRF_end_point;
      center.object_assoc_modifier = UF_DRF_first_end_point;
      status = UF_DRF_create_offcyl_cline_obj(&object1, &object2,
               &center, &cl_tag);
   }

   printf("UF_DRF_create_offcyl_cline_off,_obj ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("have ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("are successful.\n");

   UF_terminate();
}
