/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *         UF_DRF_create_id_symbol                                            *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_drf.h>
#include <uf_curve.h>

void ufusr(char *param, int *retcod, int param_len)
{
   int status = 0;
   static double  origin[3] = {22.0, 3.0, 0.0};
   static double base_pt[3] = {20.0, 5.0, 0.0};
   char text[10][132+1];
   char stat_msg[133];
   tag_t base_pt_tag, text_aid_tag;
   UF_DRF_object_t object;

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&object);

      /* create a base point */
      status = UF_CURVE_create_point(base_pt, &base_pt_tag);
   }

   if (!status)
   {
      /* create an id symbol */
      strcpy(text[0], "ID SYMBOL");
      strcpy(text[1], "LOWER");
      object.object_tag = base_pt_tag;
      object.object_view_tag = NULL_TAG;
      object.object_assoc_type = UF_DRF_end_point;
      object.object_assoc_modifier = UF_DRF_first_end_point;
      status = UF_DRF_create_id_symbol(UF_DRF_sym_divhex,
               text[0], text[1], origin, UF_DRF_with_leader,
               UF_DRF_leader_attach_object, &object, base_pt,
               &text_aid_tag);
   }

   printf("UF_DRF_create_id_symbol ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("has ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("is successful.\n");

   UF_terminate();
}
