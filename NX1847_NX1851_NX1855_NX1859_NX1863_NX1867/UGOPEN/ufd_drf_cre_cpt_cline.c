/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function programs:      *
 *                                                                            *
 *         UF_DRF_create_cpt_cline_fcir                                       *
 *         UF_DRF_create_cpt_cline_pcir                                       *
 *         UF_DRF_create_cpt_cline_fbolt                                      *
 *         UF_DRF_create_cpt_cline_pbolt                                      *
 *                                                                            *
 *                 *
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
   tag_t wcs, arc1_tag, arc2_tag, arc3_tag, arc4_tag;
   tag_t cl1_tag, cl2_tag, cl3_tag, cl4_tag;
   UF_CURVE_arc_t  arc_coords;
   UF_DRF_object_t center, objects[3];

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&objects[0]);
      UF_DRF_init_object_structure(&objects[1]);
      UF_DRF_init_object_structure(&objects[2]);
      UF_DRF_init_object_structure(&center);

      /* create four arcs */
      UF_CSYS_ask_wcs(&wcs);
      UF_CSYS_ask_matrix_of_object(wcs, &arc_coords.matrix_tag);
      arc_coords.start_angle = 0.0;
      arc_coords.end_angle = TWOPI;
      arc_coords.arc_center[0] = 5.0;
      arc_coords.arc_center[1] = 0.0;
      arc_coords.arc_center[2] = 0.0;
      arc_coords.radius = 1.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc1_tag);
   }

   if (!status)
   {
      arc_coords.arc_center[0] = -5.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc2_tag);
   }

   if (!status)
   {
      arc_coords.arc_center[0] = 0.0;
      arc_coords.arc_center[1] = 5.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc3_tag);
   }

   if (!status)
   {
      arc_coords.arc_center[0] = 0.0;
      arc_coords.arc_center[1] = 0.0;
      status = UF_CURVE_create_arc(&arc_coords, &arc4_tag);
   }

   if (!status)
   {
      objects[0].object_tag = arc1_tag;
      objects[0].object_view_tag = NULL_TAG;
      objects[0].object_assoc_type = UF_DRF_arc_center;
      objects[0].object_assoc_modifier = 0;
      objects[1].object_tag = arc2_tag;
      objects[1].object_view_tag = NULL_TAG;
      objects[1].object_assoc_type = UF_DRF_arc_center;
      objects[1].object_assoc_modifier = 0;
      objects[2].object_tag = arc3_tag;
      objects[2].object_view_tag = NULL_TAG;
      objects[2].object_assoc_type = UF_DRF_arc_center;
      objects[2].object_assoc_modifier = 0;

      /* construct centerline center structure */ 
      center.object_tag = arc4_tag;
      center.object_view_tag = NULL_TAG;
      center.object_assoc_type = UF_DRF_arc_center;
      center.object_assoc_modifier = 0;

      /* create a full circular centerline: center point method */
      status = UF_DRF_create_cpt_cline_fcir(3, objects, &center, &cl1_tag);
   }

   if (!status)
      /* create a partial circular centerline: center point method */
      status = UF_DRF_create_cpt_cline_pcir(3, objects, &center, &cl2_tag);

   if (!status)
      /* create a full bolt circle centerline: center point method */
      status = UF_DRF_create_cpt_cline_fbolt(3, objects, &center, &cl3_tag);

   if (!status)
      /* create a partial bolt circle centerline: center point method */
      status = UF_DRF_create_cpt_cline_pbolt(3, objects, &center, &cl4_tag);

   printf("UF_DRF_create_cpt_cline_fcir,_pcir,_fbolt,_pbolt ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("have ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("are successful.\n");
 
   UF_terminate();
}
