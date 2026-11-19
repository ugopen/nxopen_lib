/*===================================================================

        Copyright (c) 1998  Unigraphics Solutions Corporation
                     Unpublished - All rights reserved

===================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_MODL_ask_bounding_box                                           *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example creates bound.prt which creates an arc and then    *
 *   asks for its bounding box.                                               *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/

#include <stdio.h>
#include <uf.h>
#include <uf_part.h>
#include <uf_curve.h>
#include <uf_modl.h>
#include <uf_csys.h>
#include <uf_defs.h>

#define UF_CALL(X) (report( __FILE__, __LINE__, #X, (X)))

static int report( char *file, int line, char *call, int irc)
{
  if (irc)
  {
     char    messg[133];
     printf("%s, line %d:  %s\n", file, line, call);
     (UF_get_fail_message(irc, messg)) ?
       printf("    returned a %d\n", irc) :
       printf("    returned error %d:  %s\n", irc, messg);
  }
  return(irc);
}

static void do_ugopen_api(void)
{
  char *part_name = "bound";
  tag_t part, arc_id, wcs_tag;
  double box[6];
  UF_CURVE_arc_t arc_coords;
  
  /* Fill out the data structure */

  arc_coords.start_angle = 0.0;
  arc_coords.end_angle = 270.0 * DEGRA;
  arc_coords.arc_center[0] = 0.0;
  arc_coords.arc_center[1] = 0.0;
  arc_coords.arc_center[2] = 1.0;
  arc_coords.radius = 2.0;

  UF_PART_new(part_name, UF_PART_ENGLISH, &part);
  UF_CSYS_ask_wcs( &wcs_tag );
  UF_CSYS_ask_matrix_of_object( wcs_tag,&arc_coords.matrix_tag );
  
  /* Create arc */
  
  UF_CURVE_create_arc(&arc_coords,&arc_id);
  
  /* Ask bounding box of arc */
  
  UF_MODL_ask_bounding_box(arc_id,box);

  /* Print bounding box values */
  printf("\nMinimum x value: %f\n", box[0]);
  printf("Maximum x value: %f\n", box[3]);
  printf("Minimum y value: %f\n", box[1]);
  printf("Maximum y value: %f\n", box[4]);
  printf("Minimum z value: %f\n", box[2]);
  printf("Maximum z value: %f\n", box[5]);

}

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
  if (!UF_CALL(UF_initialize()))
  {
    do_ugopen_api();
    UF_CALL(UF_terminate());
  }
}

int ufusr_ask_unload(void)
{
  return (UF_UNLOAD_IMMEDIATELY);
}
