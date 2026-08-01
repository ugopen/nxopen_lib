/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function programs:      *
 *                                                                            *
 *         UF_DRF_create_offctrpt_nx                                          *
 *         UF_DRF_create_offctrpt_ny                                          *
 *         UF_DRF_create_offctrpt_cx                                          *
 *         UF_DRF_create_offctrpt_cy                                          *
 *         UF_DRF_create_offctrpt_fx                                          *
 *         UF_DRF_create_offctrpt_fy                                          *
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
   static double distance = 2.0;
   char stat_msg[133];
   tag_t wcs, arc1_tag, arc2_tag;
   tag_t cl1_tag, cl2_tag, cl3_tag, cl4_tag, cl5_tag, cl6_tag;
   UF_CURVE_arc_t  arc_coords;
   UF_DRF_object_t object, center;

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&object);
      UF_DRF_init_object_structure(&center);

      /* create two arcs */
      UF_CSYS_ask_wcs(&wcs);
      UF_CSYS_ask_matrix_of_object(wcs, &arc_coords.matrix_tag);
      arc_coords.start_angle = 0.0;
      arc_coords.end_angle = TWOPI;
      arc_coords.arc_center[0] = 5.0;
      arc_coords.arc_center[1] = 0.0;
      arc_coords.arc_center[2] = 0.0;
      arc_coords.radius = 2.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc1_tag);
   }

   if (!status)
   {
      arc_coords.arc_center[0] = -5.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc2_tag);
   }

   if (!status)
   {
      object.object_tag = arc1_tag;
      object.object_view_tag = NULL_TAG;
      object.object_assoc_type = UF_DRF_arc_center;
      object.object_assoc_modifier = 0;
      center.object_tag = arc2_tag;
      center.object_view_tag = NULL_TAG;
      center.object_assoc_type = UF_DRF_arc_center;
      center.object_assoc_modifier = 0;

      /* create an offset center point,
         x-axis: distance from arc normal */
      status = UF_DRF_create_offctrpt_nx(&object, distance, &cl1_tag);
   }

   if (!status)
      /* create an offset center point,
         y-axis: distance from arc normal */
      status = UF_DRF_create_offctrpt_ny(&object, distance, &cl2_tag);

   if (!status)
      /* create an offset center point,
         x-axis: distance from arc center */
      status = UF_DRF_create_offctrpt_cx(&object, distance, &cl3_tag);

   if (!status)
      /* create an offset center point,
         y-axis: distance from arc center */
      status = UF_DRF_create_offctrpt_cy(&object, distance, &cl4_tag);

   if (!status)
      /* create an offset center point,
         x-axis: calculate (find) distance */
      status = UF_DRF_create_offctrpt_fx(&object, &center, &cl5_tag);

   if (!status)
      /* create an offset center point,
         y-axis: calculate (find) distance */
      status = UF_DRF_create_offctrpt_fy(&object, &center, &cl6_tag);

   printf("UF_DRF_create_offctrpt_nx,_ny,_cx,_cy,_fx,_fy ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("have ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("are successful.\n");
 
   UF_terminate();
}
