/*===========================================================================

        Copyright (c) 1998,2003  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===========================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *         UF_DRF_create_angular_dim                                          *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_drf.h>
#include <uf_curve.h>

void ufusr(char *param, int *retcod, int param_len)
{
   int status = 0;
   static double origin[3] = {8.0, 11.0, 0.0};
   static char dimtxt[15+1] = "ANGULAR DIM TXT";
   static char apptxt[3][132+1] = {"APPENDED TEXT",
                                   "APP TXT LINE 2",
                                   "APP TXT LINE 3"};
   char  stat_msg[133];
   tag_t line1_tag = 0, line2_tag = 0, dimension_tag;
   UF_CURVE_line_t line_coords;
   UF_DRF_object_t line1, line2;
   UF_DRF_text_t   drf_text;

   status = UF_initialize();

   if (!status)
   {
      /* initialize the object structures */
      UF_DRF_init_object_structure(&line1);
      UF_DRF_init_object_structure(&line2);

      /* load drf_text specification */
      drf_text.user_dim_text  = dimtxt;
      drf_text.lines_app_text = 3;
      drf_text.appended_text  = apptxt;

      /* create two lines */
      line_coords.start_point[0] = 10.0;
      line_coords.start_point[1] = 11.0;
      line_coords.start_point[2] =  0.0;
      line_coords.end_point[0] = 8.0;
      line_coords.end_point[1] = 8.0;
      line_coords.end_point[2] = 0.0;
      status = UF_CURVE_create_line(&line_coords, &line1_tag);
   }

   if (!status)
   {
      line_coords.end_point[0] =  5.0;
      line_coords.end_point[1] = 13.0;
      status = UF_CURVE_create_line(&line_coords, &line2_tag);
   }

   if (!status)
   {
      int idata[100];
      double rdata[70];
      char rad_value[27], diameter_value[27];

      /* set the text entry mode preference so
         manual text and appended text will be applied */
      UF_DRF_ask_preferences(idata, rdata, rad_value, diameter_value);
      idata[7] = 4;
      UF_DRF_set_preferences(idata, rdata, rad_value, diameter_value);

      /* create an angular dimension */
      line1.object_tag = line1_tag;
      line1.object_view_tag = NULL_TAG;
      line1.object_assoc_type = UF_DRF_end_point;
      line1.object_assoc_modifier = UF_DRF_last_end_point;
      line2.object_tag = line2_tag;
      line2.object_view_tag = NULL_TAG;
      line2.object_assoc_type = UF_DRF_end_point;
      line2.object_assoc_modifier = UF_DRF_last_end_point;
      status = UF_DRF_create_angular_dim(1, &line1, &line2,
               &drf_text, origin, &dimension_tag);
   }

   printf("UF_DRF_create_angular_dim ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("has ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("is successful.\n");

   UF_terminate();
}
