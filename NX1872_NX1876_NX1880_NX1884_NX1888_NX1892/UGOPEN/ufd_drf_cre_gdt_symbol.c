/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *         UF_DRF_create_gdt_symbol                                           *
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

void ufusr(char *param, int *retcod, int param_len)
{
   int status = 0;
   int lines_of_text = 8;
   static double  origin[3] = {24.0, 7.0, 0.0};
   static double base_pt[3] = {20.0, 5.0, 0.0};
   char text[10][MAX_LINE_BUFSIZE];
   char stat_msg[133];
   tag_t text_aid_tag;
   tag_t base_pt_tag;
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
      /* create a geometric dimensioning and tolerancing symbol */
      strcpy(text[0], "GEOMETRIC DIMENSIONING     <+>");
      strcpy(text[1], "AND TOLERANCING SYMBOLS    <+>");
      strcpy(text[2], "<M><+><(><S><)><+><O><+>");
      strcpy(text[3], "<&1><&2><&3><&4><&5><&6><+>");
      strcpy(text[4], "<&7><+><&8><+><&9>");
      strcpy(text[5], "<&10><&11><&12><&13><&14>");
      strcpy(text[6], "It points to the screen position at (20,5).");
      strcpy(text[7], "This is the LAST line<+>");
      object.object_tag = NULL_TAG;
      object.object_view_tag = NULL_TAG;
      object.object_assoc_type = UF_DRF_end_point;
      object.object_assoc_modifier = UF_DRF_first_end_point;
      status = UF_DRF_create_gdt_symbol(lines_of_text, text, origin,
               UF_DRF_leader_type_line, UF_DRF_leader_attach_screen,
               &object, base_pt, UF_DRF_frame_none, &text_aid_tag);
   }

   printf("UF_DRF_create_gdt_symbol ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("has ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("is successful.\n");

   UF_terminate();
}
