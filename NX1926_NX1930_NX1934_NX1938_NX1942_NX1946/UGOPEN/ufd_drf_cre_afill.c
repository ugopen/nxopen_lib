/*===================================================================

        Copyright (c) 1998,2004  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/
/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following User Function program:       *
 *                                                                            *
 *         UF_DRF_create_areafill                                             *
 *                                                                            *
 
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_defs.h>
#include <uf_disp.h>
#include <uf_drf.h>
#include <uf_obj.h>
#include <uf_curve.h>
#include <uf_csys.h>


#define NUM_MATERIAL     10
#define NUM_OBJECTS     100

void ufusr(char *param, int *retcod, int param_len)
{

   int status = 0;
   int num_islands, num_elements[NUM_OBJECTS];
   static int i;
   static int mpi[100];
   static double mpr[70];
   static char rad_symbol[7], dia_symbol[7];
   char  stat_msg[133];
   tag_t elems[NUM_OBJECTS], circles[NUM_MATERIAL] = {NULL_TAG};
   tag_t wcs, areafill_tag, view_tag = NULL_TAG;
   UF_CURVE_arc_t arc_coords;

   status = UF_initialize();

   if (!status)
   {
      /* create some circles to areafill */
      UF_CSYS_ask_wcs(&wcs);
      UF_CSYS_ask_matrix_of_object(wcs, &arc_coords.matrix_tag);
      arc_coords.start_angle = 0.0;
      arc_coords.end_angle = TWOPI;
      arc_coords.arc_center[0] = -10.0;
      arc_coords.arc_center[1] =  -5.0;
      arc_coords.arc_center[2] =   0.0;
      arc_coords.radius = 1.25;
      for (i = 0; i < NUM_MATERIAL; i++)
      {
         status = UF_CURVE_create_arc(&arc_coords, &circles [i]);
         if (status)
            break;
         /* create circles moving right on x */
         arc_coords.arc_center[0] += 3.0;
      }
   }

   if (!status)
   {
      /* read the current module parameters arrays */
      UF_DRF_ask_preferences(mpi, mpr, rad_symbol, dia_symbol);
      /* set crosshatch color */
      /* 1-22-04 Jason Bell NX3210 : map hardcoded colors to new color wheel */
      UF_DISP_ask_closest_color_in_displayed_part(UF_DISP_MEDIUM_AZURE_BLUE_NAME,
                                                  &(mpi[67])); /* blue */
      /* set crosshatch density */
      mpi[68] = UF_DRF_THIN;
      /* set area fill angle */
      mpr[49] = 30.0;
      /* set area fill scale */
      mpr[50] = 1.0;
      /* set area fill tolerance */
      mpr[51] = 0.01;

      num_islands = 1;
      num_elements[0] = 1;
      for (i = 0; i < NUM_MATERIAL; i++)
      {
         /* set the area fill material */
         mpi[92] = i + 1;
         /* set the module parameters arrays */
         uc5521(mpi, mpr, rad_symbol, dia_symbol);

         elems[0] = circles[i];
         status = UF_DRF_create_areafill(num_islands, num_elements,
                  elems, view_tag, &areafill_tag);
         if (status)
            break;
      }
   }

   printf("UF_DRF_create_areafill ");
   if (status)
   {
      UF_get_fail_message(status, stat_msg);
      printf("has ERROR %d: %s.\n", status, stat_msg);
   }
   else
      printf("is successful.\n");

   UF_terminate();
}
