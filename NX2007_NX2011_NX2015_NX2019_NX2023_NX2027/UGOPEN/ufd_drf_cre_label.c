/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *         UF_DRF_create_label                                                *
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
   int lines_of_text = 7;
   static double  origin[3] = {20.0, 0.0, 0.0};
   static double base_pt[3] = {20.0, 5.0, 0.0};
   char text[10][MAX_LINE_BUFSIZE];
   char stat_msg[133];
   tag_t base_pt_tag= NULL_TAG, text_aid_tag;
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
      /* create a label */
      strcpy(text[0], "This is a LABEL.");
      strcpy(text[1], "It points to the screen position at (20,5).");
      strcpy(text[2], "The next line is BLANK.");
      strcpy(text[3], "");
      strcpy(text[4], "The next line is very long....");
      strcpy(text[5], "ABCDEFGHIJKLMNOPQRSTUVWXYZYXWV");
      strcpy(text[6], "This is the LAST line.");
      object.object_tag = base_pt_tag;
      object.object_view_tag = NULL_TAG;
      object.object_assoc_type = UF_DRF_end_point;
      object.object_assoc_modifier = UF_DRF_first_end_point;
      status = UF_DRF_create_label(lines_of_text, text, origin,
               UF_DRF_leader_attach_screen, &object, base_pt,
               &text_aid_tag);
   }

   printf("UF_DRF_create_label ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("has ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("is successful.\n");

   UF_terminate();
}
